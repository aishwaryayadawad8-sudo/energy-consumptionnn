import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import joblib
import os

class EnergyPredictor:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.models = {}
        self.scaler = StandardScaler()
        self.best_model = None
        self.best_model_name = None
        
    def load_data(self):
        """Load and preprocess the dataset"""
        self.df = pd.read_csv(self.csv_path)
        return self.df
    
    def get_country_data(self, country_name):
        """Get data for a specific country"""
        if self.df is None:
            self.load_data()
        country_data = self.df[self.df['Entity'].str.lower() == country_name.lower()]
        return country_data if not country_data.empty else None
    
    def prepare_features(self, target='Access to electricity (% of population)'):
        """Prepare features for training"""
        if self.df is None:
            self.load_data()
        
        feature_columns = [
            'Renewable energy share in the total final energy consumption (%)',
            'Value_co2_emissions_kt_by_country',
            'Electricity from fossil fuels (TWh)',
            'Electricity from renewables (TWh)',
            'Primary energy consumption per capita (kWh/person)',
            'gdp_per_capita',
            'Year'
        ]
        
        df_clean = self.df.dropna(subset=feature_columns + [target])
        X = df_clean[feature_columns]
        y = df_clean[target]
        
        return train_test_split(X, y, test_size=0.2, random_state=42)
    
    def train_models(self):
        """Train multiple ML models"""
        X_train, X_test, y_train, y_test = self.prepare_features()
        
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        self.models = {
            'Linear Regression': LinearRegression(),
            'Decision Tree': DecisionTreeRegressor(random_state=42),
            'KNN': KNeighborsRegressor(n_neighbors=5),
            'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
            'XGBoost': XGBRegressor(random_state=42, verbosity=0),
            'LightGBM': LGBMRegressor(random_state=42, verbose=-1),
            'CatBoost': CatBoostRegressor(random_state=42, verbose=0)
        }
        
        results = {}
        best_score = -float('inf')
        
        for name, model in self.models.items():
            model.fit(X_train_scaled, y_train)
            y_pred = model.predict(X_test_scaled)
            
            mse = mean_squared_error(y_test, y_pred)
            rmse = np.sqrt(mse)
            mae = mean_absolute_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            
            results[name] = {
                'MSE': mse,
                'RMSE': rmse,
                'MAE': mae,
                'R2': r2
            }
            
            if r2 > best_score:
                best_score = r2
                self.best_model = model
                self.best_model_name = name
        
        return results
    
    def predict_electricity_access(self, country_name, future_years=5):
        """Predict electricity access for a country"""
        country_data = self.get_country_data(country_name)
        
        if country_data is None or country_data.empty:
            return None
        
        latest_data = country_data.sort_values('Year').iloc[-1]
        
        # Check if required features have data
        required_features = [
            'Renewable energy share in the total final energy consumption (%)',
            'Value_co2_emissions_kt_by_country',
            'Electricity from fossil fuels (TWh)',
            'Electricity from renewables (TWh)',
            'Primary energy consumption per capita (kWh/person)',
            'gdp_per_capita'
        ]
        
        # Check for missing values
        if any(pd.isna(latest_data[feat]) for feat in required_features):
            return None
        
        predictions = []
        current_year = int(latest_data['Year'])
        
        for i in range(1, future_years + 1):
            future_year = current_year + i
            
            features = np.array([[
                float(latest_data['Renewable energy share in the total final energy consumption (%)']),
                float(latest_data['Value_co2_emissions_kt_by_country']),
                float(latest_data['Electricity from fossil fuels (TWh)']),
                float(latest_data['Electricity from renewables (TWh)']),
                float(latest_data['Primary energy consumption per capita (kWh/person)']),
                float(latest_data['gdp_per_capita']),
                future_year
            ]])
            
            features_scaled = self.scaler.transform(features)
            prediction = self.best_model.predict(features_scaled)[0]
            
            predictions.append({
                'year': future_year,
                'predicted_access': float(min(100, max(0, prediction)))
            })
        
        return predictions
    
    def get_country_status(self, country_name):
        """Determine if country's electricity situation is good or critical"""
        country_data = self.get_country_data(country_name)
        
        if country_data is None or country_data.empty:
            return None
        
        latest_data = country_data.sort_values('Year').iloc[-1]
        
        electricity_access = latest_data['Access to electricity (% of population)']
        renewable_share = latest_data['Renewable energy share in the total final energy consumption (%)']
        co2_emissions = latest_data['Value_co2_emissions_kt_by_country']
        
        status = {
            'electricity_access': float(electricity_access) if pd.notna(electricity_access) else None,
            'renewable_share': float(renewable_share) if pd.notna(renewable_share) else None,
            'co2_emissions': float(co2_emissions) if pd.notna(co2_emissions) else None,
            'status': 'GOOD',
            'message': '',
            'alerts': []
        }
        
        if pd.notna(electricity_access):
            if electricity_access < 50:
                status['status'] = 'CRITICAL'
                status['alerts'].append('⚠️ Electricity access is critically low (< 50%)')
            elif electricity_access < 80:
                status['status'] = 'WARNING'
                status['alerts'].append('⚡ Electricity access needs improvement (< 80%)')
            else:
                status['alerts'].append('✅ Good electricity access (≥ 80%)')
        
        if pd.notna(renewable_share):
            if renewable_share < 10:
                status['status'] = 'CRITICAL' if status['status'] == 'CRITICAL' else 'WARNING'
                status['alerts'].append('⚠️ Very low renewable energy share (< 10%)')
            elif renewable_share < 25:
                status['alerts'].append('🔋 Renewable energy share can be improved')
            else:
                status['alerts'].append('✅ Good renewable energy adoption')
        
        if pd.notna(co2_emissions) and co2_emissions > 100000:
            status['status'] = 'WARNING' if status['status'] == 'GOOD' else status['status']
            status['alerts'].append('🏭 High CO₂ emissions detected')
        
        return status
