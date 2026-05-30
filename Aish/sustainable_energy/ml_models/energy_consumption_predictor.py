import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from sklearn.metrics import mean_squared_error
import os

class EnergyConsumptionPredictor:
    """Objective 1: Forecast Energy Consumption per Capita"""
    
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.df_clean = None
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
        self.df.columns = self.df.columns.str.strip().str.replace('\n', ' ').str.replace(r'\s+', ' ', regex=True)
        
        # Convert numeric columns
        for col in self.df.columns:
            if col not in ['Entity']:
                self.df[col] = self.df[col].astype(str).str.replace(',', '', regex=False)
                self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
        
        # Encode countries
        self.df['Entity'] = self.df['Entity'].astype('category')
        self.df['Country_Code'] = self.df['Entity'].cat.codes
        
        return self.df
    
    def prepare_features(self):
        """Prepare features for model training"""
        if self.df is None:
            self.load_and_clean_data()
        
        target_col = "Primary energy consumption per capita (kWh/person)"
        
        # Drop rows where target is missing
        df_model = self.df.dropna(subset=[target_col]).copy()
        
        # Separate features and target
        X = df_model.drop(columns=[target_col, 'Entity'])
        y = df_model[target_col]
        
        # Impute missing values
        num_cols = X.select_dtypes(include=[np.number]).columns
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
            "KNN": KNeighborsRegressor(),
            "XGBoost": XGBRegressor(objective='reg:squarederror', random_state=0, verbosity=0),
            "LightGBM": LGBMRegressor(random_state=0, verbosity=-1),
            "CatBoost": CatBoostRegressor(random_state=0, verbose=0),
            "Random Forest": RandomForestRegressor(random_state=0, n_estimators=100)
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
        """Get historical energy consumption data"""
        if self.df is None:
            self.load_and_clean_data()
        
        target_col = "Primary energy consumption per capita (kWh/person)"
        df_hist = self.df[['Year', 'Entity', target_col]].dropna()
        
        if country_name:
            df_hist = df_hist[df_hist['Entity'].str.lower() == country_name.lower()]
        
        return df_hist.to_dict('records')
    
    def predict_future_consumption(self, years_ahead=10, country_name=None):
        """Predict future energy consumption with trend analysis"""
        if self.df is None:
            self.load_and_clean_data()
        
        target_col = "Primary energy consumption per capita (kWh/person)"
        df_simple = self.df[['Year', 'Entity', 'Country_Code', target_col]].dropna()
        
        # Filter by country if specified
        if country_name:
            df_simple = df_simple[df_simple['Entity'].str.lower() == country_name.lower()]
            if df_simple.empty:
                return None
        
        predictions = []
        
        if country_name:
            # Single country prediction with polynomial trend and realistic variations
            country_data = df_simple.sort_values('Year')
            years = country_data['Year'].values.reshape(-1, 1)
            consumption = country_data[target_col].values
            
            # Calculate historical volatility for realistic variations
            if len(consumption) > 1:
                year_changes = np.diff(consumption)
                volatility = np.std(year_changes) * 0.3  # Use 30% of historical volatility
            else:
                volatility = np.std(consumption) * 0.02
            
            # Use polynomial features for better trend capture
            from sklearn.preprocessing import PolynomialFeatures
            poly = PolynomialFeatures(degree=2)
            years_poly = poly.fit_transform(years)
            
            model = LinearRegression()
            model.fit(years_poly, consumption)
            
            # Generate future predictions with variations
            last_year = int(country_data['Year'].max())
            future_years = np.arange(last_year + 1, last_year + years_ahead + 1).reshape(-1, 1)
            future_years_poly = poly.transform(future_years)
            future_predictions = model.predict(future_years_poly)
            
            # Add realistic fluctuations
            np.random.seed(42)  # For reproducibility
            for i, (year, pred_value) in enumerate(zip(future_years.flatten(), future_predictions)):
                # Add some variation that decreases over time (more uncertainty further out)
                variation = np.random.normal(0, volatility * (1 + i * 0.1))
                adjusted_value = pred_value + variation
                
                predictions.append({
                    'year': int(year),
                    'country': country_name,
                    'predicted_consumption': float(max(0, adjusted_value))  # Ensure non-negative
                })
        else:
            # All countries prediction with individual trends and variations
            countries = df_simple['Entity'].unique()
            np.random.seed(42)  # For reproducibility
            
            for country in countries:
                country_data = df_simple[df_simple['Entity'] == country].sort_values('Year')
                
                if len(country_data) < 3:  # Need at least 3 points for trend
                    continue
                
                years = country_data['Year'].values.reshape(-1, 1)
                consumption = country_data[target_col].values
                
                # Calculate historical volatility
                if len(consumption) > 1:
                    year_changes = np.diff(consumption)
                    volatility = np.std(year_changes) * 0.3
                else:
                    volatility = np.std(consumption) * 0.02
                
                # Use polynomial features
                from sklearn.preprocessing import PolynomialFeatures
                poly = PolynomialFeatures(degree=2)
                years_poly = poly.fit_transform(years)
                
                model = LinearRegression()
                model.fit(years_poly, consumption)
                
                # Generate future predictions with variations
                last_year = int(country_data['Year'].max())
                future_years = np.arange(last_year + 1, last_year + years_ahead + 1).reshape(-1, 1)
                future_years_poly = poly.transform(future_years)
                future_predictions = model.predict(future_years_poly)
                
                for i, (year, pred_value) in enumerate(zip(future_years.flatten(), future_predictions)):
                    variation = np.random.normal(0, volatility * (1 + i * 0.1))
                    adjusted_value = pred_value + variation
                    
                    predictions.append({
                        'year': int(year),
                        'country': country,
                        'predicted_consumption': float(max(0, adjusted_value))
                    })
        
        return predictions
    
    def get_all_countries(self):
        """Get list of all countries with energy consumption data"""
        if self.df is None:
            self.load_and_clean_data()
        
        target_col = "Primary energy consumption per capita (kWh/person)"
        countries = self.df[self.df[target_col].notna()]['Entity'].unique().tolist()
        return sorted([str(c) for c in countries])
