import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

class SDG7ElectricityAccess:
    """Objective 6: SDG 7 - Access to Electricity Forecasting"""
    
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.df_sdg7 = None
        self.models = {}
        self.mse_scores = {}
        self.best_model = None
        self.best_model_name = None
        self.scaler = StandardScaler()
        self.imputer = SimpleImputer(strategy='mean')
        
    def load_and_clean_data(self):
        """Load and preprocess the dataset"""
        self.df = pd.read_csv(self.csv_path)
        
        # Clean column names
        self.df.columns = (self.df.columns.str.strip()
                          .str.replace('\n', ' ')
                          .str.replace(r'\s+', ' ', regex=True))
        
        # Convert numeric columns
        for col in self.df.columns:
            if col not in ['Entity']:
                self.df[col] = self.df[col].astype(str).str.replace(',', '', regex=False)
                self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
        
        # Prepare SDG7 specific dataset
        target_col = 'Access to electricity (% of population)'
        self.df_sdg7 = self.df[['Year', 'Entity', target_col]].dropna().copy()
        
        # Encode countries
        self.df['Entity'] = self.df['Entity'].astype('category')
        self.df['Country_Code'] = self.df['Entity'].cat.codes
        
        return self.df
    
    def prepare_features(self):
        """Prepare features for model training"""
        if self.df is None:
            self.load_and_clean_data()
        
        target_col = 'Access to electricity (% of population)'
        
        # Drop rows where target is missing
        df_model = self.df.dropna(subset=[target_col]).copy()
        
        # Separate features and target
        X = df_model.drop(columns=[target_col, 'Entity'])
        y = df_model[target_col]
        
        # Get numeric columns
        num_cols = X.select_dtypes(include=[np.number]).columns.drop(['Country_Code'], errors='ignore')
        
        # Impute missing values
        X[num_cols] = self.imputer.fit_transform(X[num_cols])
        
        # Scale features
        X[num_cols] = self.scaler.fit_transform(X[num_cols])
        
        return train_test_split(X, y, test_size=0.2, random_state=0)
    
    def train_and_compare_models(self):
        """Train multiple models and compare MSE scores"""
        X_train, X_test, y_train, y_test = self.prepare_features()
        
        self.models = {
            "Linear Regression": LinearRegression(),
            "Decision Tree": DecisionTreeRegressor(random_state=0),
            "K-Nearest Neighbors": KNeighborsRegressor(),
            "XGBoost": XGBRegressor(objective='reg:squarederror', random_state=0, verbosity=0)
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
        if self.df_sdg7 is None:
            self.load_and_clean_data()
        
        df_hist = self.df_sdg7.copy()
        
        if country_name:
            df_hist = df_hist[df_hist['Entity'].str.lower() == country_name.lower()]
        
        return df_hist.to_dict('records')
    
    def predict_future_access(self, years_ahead=10, country_name=None):
        """Predict future electricity access"""
        if self.df_sdg7 is None:
            self.load_and_clean_data()
        
        target_col = 'Access to electricity (% of population)'
        
        # Prepare simple dataset for forecasting
        df_future = self.df_sdg7.copy()
        df_future['Country_Code'] = df_future['Entity'].astype('category').cat.codes
        country_map = dict(zip(df_future['Country_Code'], df_future['Entity']))
        
        # Filter by country if specified
        if country_name:
            df_future = df_future[df_future['Entity'].str.lower() == country_name.lower()]
            if df_future.empty:
                return None
        
        # Prepare features
        X_future = df_future[['Year', 'Country_Code']]
        y_future = df_future[target_col]
        
        # Train simple model for predictions
        model_simple = LinearRegression()
        model_simple.fit(X_future, y_future)
        
        # Generate future predictions
        last_year = int(df_future['Year'].max())
        future_years = np.arange(last_year + 1, last_year + years_ahead + 1)
        
        predictions = []
        
        if country_name:
            # Single country prediction
            country_code = df_future['Country_Code'].iloc[0]
            for year in future_years:
                pred_value = model_simple.predict([[year, country_code]])[0]
                # Clamp between 0 and 100
                pred_value = float(min(100, max(0, pred_value)))
                
                predictions.append({
                    'year': int(year),
                    'country': country_name,
                    'predicted_access': pred_value
                })
        else:
            # All countries prediction
            countries = df_future[['Entity', 'Country_Code']].drop_duplicates()
            
            for _, row in countries.iterrows():
                country = row['Entity']
                country_code = row['Country_Code']
                
                for year in future_years:
                    pred_value = model_simple.predict([[year, country_code]])[0]
                    # Clamp between 0 and 100
                    pred_value = float(min(100, max(0, pred_value)))
                    
                    predictions.append({
                        'year': int(year),
                        'country': country,
                        'predicted_access': pred_value
                    })
        
        return predictions
    
    def get_all_countries(self):
        """Get list of all countries with electricity access data"""
        if self.df_sdg7 is None:
            self.load_and_clean_data()
        
        countries = self.df_sdg7['Entity'].unique().tolist()
        return sorted([str(c) for c in countries])
