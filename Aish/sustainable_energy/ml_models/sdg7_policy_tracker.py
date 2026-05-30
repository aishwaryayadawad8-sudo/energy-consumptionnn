import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.metrics import mean_squared_error

class SDG7PolicyTracker:
    """Objective 5: SDG 7 Tracking with Policy Impact Analysis"""
    
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.models = {}
        self.mse_scores = {}
        self.best_model = None
        self.best_model_name = None
        self.label_encoder = LabelEncoder()
        self.country_map = {}
        
        # Policy intervention years for key countries
        self.policy_years = {
            'India': 2010,
            'Bangladesh': 2008,
            'Kenya': 2013,
            'Nigeria': 2015,
            'Brazil': 2003
        }
        
    def load_and_clean_data(self):
        """Load and preprocess the dataset"""
        df_raw = pd.read_csv(self.csv_path)
        
        # Clean column names
        df_raw.columns = df_raw.columns.str.strip().str.replace('\n', ' ').str.replace(r'\s+', ' ', regex=True)
        
        # Extract electricity access data
        self.df = df_raw[['Year', 'Entity', 'Access to electricity (% of population)']].dropna().copy()
        self.df.rename(columns={'Access to electricity (% of population)': 'Electricity_Access'}, inplace=True)
        
        # Categorize access levels
        self.df['Access Level'] = pd.cut(
            self.df['Electricity_Access'],
            bins=[-1, 50, 90, 100],
            labels=['Low Access', 'Medium Access', 'High Access']
        )
        
        # Encode countries
        self.df['Country_Code'] = self.df['Entity'].astype('category').cat.codes
        self.country_map = dict(zip(self.df['Country_Code'], self.df['Entity']))
        
        # Encode target
        self.df['Target'] = self.label_encoder.fit_transform(self.df['Access Level'])
        
        return self.df
    
    def prepare_features(self):
        """Prepare features for classification"""
        if self.df is None:
            self.load_and_clean_data()
        
        X = self.df[['Year', 'Country_Code']]
        y = self.df['Target']
        
        return train_test_split(X, y, test_size=0.2, random_state=42)
    
    def train_and_compare_models(self):
        """Train multiple classification models and compare MSE"""
        X_train, X_test, y_train, y_test = self.prepare_features()
        
        self.models = {
            "Logistic Regression": LogisticRegression(max_iter=200),
            "Decision Tree": DecisionTreeClassifier(random_state=42),
            "KNN": KNeighborsClassifier(),
            "XGBoost": XGBClassifier(eval_metric='mlogloss', random_state=42, verbosity=0)
        }
        
        self.mse_scores = {}
        best_mse = float('inf')
        
        for name, model in self.models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            self.mse_scores[name] = float(mse)
            
            # Track best model (lowest MSE)
            if mse < best_mse:
                best_mse = mse
                self.best_model = model
                self.best_model_name = name
        
        return self.mse_scores
    
    def get_historical_data(self, country_name=None):
        """Get historical electricity access data"""
        if self.df is None:
            self.load_and_clean_data()
        
        df_hist = self.df[['Year', 'Entity', 'Electricity_Access', 'Access Level']].copy()
        
        if country_name:
            df_hist = df_hist[df_hist['Entity'].str.lower() == country_name.lower()]
        
        # Convert Access Level to string
        df_hist['Access Level'] = df_hist['Access Level'].astype(str)
        
        return df_hist.to_dict('records')
    
    def predict_future_access(self, years_ahead=10, country_name=None):
        """Predict future electricity access levels"""
        if self.df is None:
            self.load_and_clean_data()
        
        # Train final model on all data
        X = self.df[['Year', 'Country_Code']]
        y = self.df['Target']
        
        best_model = LogisticRegression(max_iter=200)
        best_model.fit(X, y)
        
        # Generate future predictions
        last_year = int(self.df['Year'].max())
        future_years = np.arange(last_year + 1, last_year + years_ahead + 1)
        
        predictions = []
        
        if country_name:
            # Single country prediction
            country_data = self.df[self.df['Entity'].str.lower() == country_name.lower()]
            if country_data.empty:
                return None
            
            country_code = country_data['Country_Code'].iloc[0]
            
            for year in future_years:
                pred_code = best_model.predict([[year, country_code]])[0]
                pred_label = self.label_encoder.inverse_transform([pred_code])[0]
                
                predictions.append({
                    'year': int(year),
                    'country': country_name,
                    'predicted_access_level': str(pred_label)
                })
        else:
            # All countries prediction
            countries = self.df[['Entity', 'Country_Code']].drop_duplicates()
            
            for _, row in countries.iterrows():
                country = row['Entity']
                country_code = row['Country_Code']
                
                for year in future_years:
                    pred_code = best_model.predict([[year, country_code]])[0]
                    pred_label = self.label_encoder.inverse_transform([pred_code])[0]
                    
                    predictions.append({
                        'year': int(year),
                        'country': country,
                        'predicted_access_level': str(pred_label)
                    })
        
        return predictions
    
    def get_all_countries(self):
        """Get list of all countries"""
        if self.df is None:
            self.load_and_clean_data()
        
        countries = self.df['Entity'].unique().tolist()
        return sorted([str(c) for c in countries])
    
    def get_policy_impact_data(self, country_name=None):
        """Get policy intervention markers for visualization"""
        if self.df is None:
            self.load_and_clean_data()
        
        policy_markers = []
        
        for country, year in self.policy_years.items():
            if country_name and country.lower() != country_name.lower():
                continue
            
            # Find electricity access value at policy year
            country_data = self.df[(self.df['Entity'] == country) & (self.df['Year'] == year)]
            
            if not country_data.empty:
                policy_markers.append({
                    'country': country,
                    'year': int(year),
                    'electricity_access': float(country_data['Electricity_Access'].iloc[0]),
                    'policy_label': f"{country} Policy"
                })
        
        return policy_markers
    
    def get_combined_historical_future(self, country_name=None):
        """Get combined historical and future data for visualization"""
        if self.df is None:
            self.load_and_clean_data()
        
        # Historical data
        hist_data = self.df[['Year', 'Entity', 'Access Level']].copy()
        hist_data.rename(columns={'Entity': 'Country'}, inplace=True)
        hist_data['Access Level'] = hist_data['Access Level'].astype(str)
        hist_data['is_future'] = False
        
        # Future predictions
        predictions = self.predict_future_access(10, country_name)
        if predictions:
            future_data = pd.DataFrame(predictions)
            future_data.rename(columns={'predicted_access_level': 'Access Level'}, inplace=True)
            future_data['is_future'] = True
            
            # Combine
            combined = pd.concat([
                hist_data[['Year', 'Country', 'Access Level', 'is_future']],
                future_data[['year', 'country', 'Access Level', 'is_future']].rename(columns={'year': 'Year', 'country': 'Country'})
            ], ignore_index=True)
            
            if country_name:
                combined = combined[combined['Country'].str.lower() == country_name.lower()]
            
            return combined.to_dict('records')
        
        return hist_data.to_dict('records')
