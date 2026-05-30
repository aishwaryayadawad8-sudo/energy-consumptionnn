import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

class ElectricityAccessClassifier:
    """Objective 4: Classify Electricity Access Levels"""
    
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.df_class = None
        self.models = {}
        self.accuracy_scores = {}
        self.best_model = None
        self.best_model_name = None
        self.label_encoder = LabelEncoder()
        self.country_map = {}
        
    def load_and_clean_data(self):
        """Load and preprocess the dataset"""
        self.df = pd.read_csv(self.csv_path)
        
        # Clean column names
        self.df.columns = self.df.columns.str.strip().str.replace('\n', ' ').str.replace(r'\s+', ' ', regex=True)
        
        # Create classification dataset
        self.df_class = self.df[['Year', 'Entity', 'Access to electricity (% of population)']].dropna().copy()
        
        # Create access level categories
        self.df_class['Access Level'] = pd.cut(
            self.df_class['Access to electricity (% of population)'],
            bins=[-1, 50, 90, 100],
            labels=['Low Access', 'Medium Access', 'High Access']
        )
        
        # Encode countries
        self.df_class['Country_Code'] = self.df_class['Entity'].astype('category').cat.codes
        self.country_map = dict(zip(self.df_class['Country_Code'], self.df_class['Entity']))
        
        return self.df_class
    
    def prepare_features(self):
        """Prepare features for classification"""
        if self.df_class is None:
            self.load_and_clean_data()
        
        X = self.df_class[['Year', 'Country_Code']]
        y = self.df_class['Access Level']
        
        # Encode target labels
        y_encoded = self.label_encoder.fit_transform(y)
        
        return train_test_split(X, y_encoded, test_size=0.2, random_state=42)
    
    def train_and_compare_models(self):
        """Train multiple classification models and compare accuracy"""
        X_train, X_test, y_train, y_test = self.prepare_features()
        
        self.models = {
            "Logistic Regression": LogisticRegression(max_iter=200),
            "Decision Tree": DecisionTreeClassifier(random_state=42),
            "K-Nearest Neighbors": KNeighborsClassifier(),
            "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='mlogloss', random_state=42, verbosity=0)
        }
        
        self.accuracy_scores = {}
        best_accuracy = 0
        
        for name, model in self.models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            self.accuracy_scores[name] = float(accuracy)
            
            # Track best model (highest accuracy)
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                self.best_model = model
                self.best_model_name = name
        
        return self.accuracy_scores
    
    def get_historical_data(self, country_name=None):
        """Get historical electricity access data"""
        if self.df_class is None:
            self.load_and_clean_data()
        
        df_hist = self.df_class[['Year', 'Entity', 'Access to electricity (% of population)', 'Access Level']].copy()
        
        if country_name:
            df_hist = df_hist[df_hist['Entity'].str.lower() == country_name.lower()]
        
        # Convert Access Level to string for JSON serialization
        df_hist['Access Level'] = df_hist['Access Level'].astype(str)
        
        return df_hist.to_dict('records')
    
    def predict_future_access(self, years_ahead=10, country_name=None):
        """Predict future electricity access levels"""
        if self.df_class is None:
            self.load_and_clean_data()
        
        # Train final model on all data
        X = self.df_class[['Year', 'Country_Code']]
        y = self.df_class['Access Level']
        y_encoded = self.label_encoder.fit_transform(y)
        
        model_final = LogisticRegression(max_iter=200)
        model_final.fit(X, y_encoded)
        
        # Generate future predictions
        last_year = int(self.df_class['Year'].max())
        future_years = np.arange(last_year + 1, last_year + years_ahead + 1)
        
        predictions = []
        
        if country_name:
            # Single country prediction
            country_data = self.df_class[self.df_class['Entity'].str.lower() == country_name.lower()]
            if country_data.empty:
                return None
            
            country_code = country_data['Country_Code'].iloc[0]
            
            for year in future_years:
                pred_encoded = model_final.predict([[year, country_code]])[0]
                pred_label = self.label_encoder.inverse_transform([pred_encoded])[0]
                
                predictions.append({
                    'year': int(year),
                    'country': country_name,
                    'predicted_access_level': str(pred_label)
                })
        else:
            # All countries prediction
            countries = self.df_class[['Entity', 'Country_Code']].drop_duplicates()
            
            for _, row in countries.iterrows():
                country = row['Entity']
                country_code = row['Country_Code']
                
                for year in future_years:
                    pred_encoded = model_final.predict([[year, country_code]])[0]
                    pred_label = self.label_encoder.inverse_transform([pred_encoded])[0]
                    
                    predictions.append({
                        'year': int(year),
                        'country': country,
                        'predicted_access_level': str(pred_label)
                    })
        
        return predictions
    
    def get_all_countries(self):
        """Get list of all countries with electricity access data"""
        if self.df_class is None:
            self.load_and_clean_data()
        
        countries = self.df_class['Entity'].unique().tolist()
        return sorted([str(c) for c in countries])
    
    def get_access_level_distribution(self, country_name=None):
        """Get distribution of access levels over time"""
        if self.df_class is None:
            self.load_and_clean_data()
        
        if country_name:
            df_filtered = self.df_class[self.df_class['Entity'].str.lower() == country_name.lower()]
        else:
            df_filtered = self.df_class
        
        distribution = df_filtered.groupby(['Year', 'Access Level']).size().reset_index(name='count')
        distribution['Access Level'] = distribution['Access Level'].astype(str)
        
        return distribution.to_dict('records')
