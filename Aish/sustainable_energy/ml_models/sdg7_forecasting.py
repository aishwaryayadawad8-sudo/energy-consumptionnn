"""
Objective 5: SDG 7 Electricity Access Forecasting
Complete implementation with model comparison, historical tracking, and future predictions
"""

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


class SDG7Forecasting:
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
        self.target_col = 'Access to electricity (% of population)'
        self.country_map = {}
        
    def load_and_clean_data(self):
        """Load and clean SDG 7 data"""
        df = pd.read_csv(self.csv_path)
        
        # Clean column names
        df.columns = (df.columns.str.strip()
                     .str.replace('\n', ' ')
                     .str.replace(r'\s+', ' ', regex=True))
        
        # Convert all potentially numeric columns to numeric
        for col in df.columns:
            if col not in ['Entity']:
                df[col] = df[col].astype(str).str.replace(',', '', regex=False)
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Prepare SDG7 tracking dataset
        self.df_sdg7 = df[['Year', 'Entity', self.target_col]].dropna().copy()
        
        # Encode Entity to numeric country codes
        df['Entity'] = df['Entity'].astype('category')
        df['Country_Code'] = df['Entity'].cat.codes
        
        # Create country mapping
        self.country_map = dict(zip(df['Country_Code'], df['Entity']))
        
        # Impute & scale numerical features
        num_cols = df.select_dtypes(include=[np.number]).columns.drop(['Country_Code'], errors='ignore')
        df[num_cols] = self.imputer.fit_transform(df[num_cols])
        df[num_cols] = self.scaler.fit_transform(df[num_cols])
        
        self.df = df
        
    def train_and_compare_models(self):
        """Train multiple regression models and compare MSE scores"""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_and_clean_data() first.")
        
        # Prepare features and target
        X = self.df.drop(columns=[self.target_col, 'Entity'], errors='ignore')
        y = self.df[self.target_col]
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=0
        )
        
        # Define models
        self.models = {
            "Linear Regression": LinearRegression(),
            "Decision Tree": DecisionTreeRegressor(random_state=0),
            "K-Nearest Neighbors": KNeighborsRegressor(),
            "XGBoost": XGBRegressor(objective='reg:squarederror', random_state=0, verbosity=0)
        }
        
        # Train and evaluate
        best_mse = float('inf')
        for name, model in self.models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            self.mse_scores[name] = float(mse)
            
            if mse < best_mse:
                best_mse = mse
                self.best_model = model
                self.best_model_name = name
        
        return self.mse_scores
    
    def get_historical_data(self, country=None):
        """Get historical electricity access data"""
        if self.df_sdg7 is None:
            raise ValueError("Data not loaded. Call load_and_clean_data() first.")
        
        if country:
            data = self.df_sdg7[self.df_sdg7['Entity'] == country].copy()
        else:
            data = self.df_sdg7.copy()
        
        data = data.sort_values('Year')
        
        result = []
        for _, row in data.iterrows():
            result.append({
                'Year': int(row['Year']),
                'Entity': row['Entity'],
                'Access to electricity (% of population)': float(row[self.target_col])
            })
        
        return result
    
    def predict_future_access(self, years=10, country=None):
        """Predict future electricity access using simple Linear Regression"""
        if self.df_sdg7 is None:
            raise ValueError("Data not loaded. Call load_and_clean_data() first.")
        
        # Prepare simple dataset for forecasting
        df_future = self.df_sdg7.copy()
        df_future['Country_Code'] = df_future['Entity'].astype('category').cat.codes
        country_map = dict(zip(df_future['Country_Code'], df_future['Entity']))
        
        if country:
            # Filter for specific country
            country_data = df_future[df_future['Entity'] == country]
            if country_data.empty:
                return None
            countries = country_data['Country_Code'].unique()
        else:
            countries = df_future['Country_Code'].unique()
        
        # Train simple model for forecasting
        X_future = df_future[['Year', 'Country_Code']]
        y_future = df_future[self.target_col]
        
        model_simple = LinearRegression()
        model_simple.fit(X_future, y_future)
        
        # Generate future predictions
        last_year = int(df_future['Year'].max())
        future_years = np.arange(last_year + 1, last_year + years + 1)
        
        predictions = []
        for yr in future_years:
            for c in countries:
                pred_value = model_simple.predict([[yr, c]])[0]
                # Clip to 0-100 range
                pred_value = max(0, min(100, pred_value))
                
                predictions.append({
                    'year': int(yr),
                    'country': country_map[c],
                    'country_code': int(c),
                    'predicted_access': float(pred_value)
                })
        
        return predictions
    
    def get_combined_historical_future(self, country=None):
        """Get combined historical and future data"""
        historical = self.get_historical_data(country)
        future = self.predict_future_access(7, country)  # 2024-2030
        
        if future is None:
            return historical
        
        # Format historical
        hist_formatted = []
        for h in historical:
            hist_formatted.append({
                'year': h['Year'],
                'country': h['Entity'],
                'access': h['Access to electricity (% of population)'],
                'type': 'historical'
            })
        
        # Format future
        future_formatted = []
        for f in future:
            future_formatted.append({
                'year': f['year'],
                'country': f['country'],
                'access': f['predicted_access'],
                'type': 'predicted'
            })
        
        return hist_formatted + future_formatted
    
    def get_all_countries(self):
        """Get list of all countries in dataset"""
        if self.df_sdg7 is None:
            raise ValueError("Data not loaded. Call load_and_clean_data() first.")
        
        countries = sorted(self.df_sdg7['Entity'].unique().tolist())
        return countries
    
    def get_country_statistics(self, country):
        """Get statistics for a specific country"""
        if self.df_sdg7 is None:
            raise ValueError("Data not loaded. Call load_and_clean_data() first.")
        
        country_data = self.df_sdg7[self.df_sdg7['Entity'] == country]
        
        if country_data.empty:
            return None
        
        country_data = country_data.sort_values('Year')
        
        latest = country_data.iloc[-1]
        earliest = country_data.iloc[0]
        
        return {
            'country': country,
            'latest_year': int(latest['Year']),
            'latest_access': float(latest[self.target_col]),
            'earliest_year': int(earliest['Year']),
            'earliest_access': float(earliest[self.target_col]),
            'improvement': float(latest[self.target_col] - earliest[self.target_col]),
            'years_tracked': int(latest['Year'] - earliest['Year']),
            'data_points': len(country_data)
        }
    
    def get_global_statistics(self):
        """Get global statistics"""
        if self.df_sdg7 is None:
            raise ValueError("Data not loaded. Call load_and_clean_data() first.")
        
        latest_year = self.df_sdg7['Year'].max()
        latest_data = self.df_sdg7[self.df_sdg7['Year'] == latest_year]
        
        return {
            'latest_year': int(latest_year),
            'countries_tracked': len(latest_data),
            'global_average': float(latest_data[self.target_col].mean()),
            'highest_access': float(latest_data[self.target_col].max()),
            'lowest_access': float(latest_data[self.target_col].min()),
            'countries_100_percent': int((latest_data[self.target_col] >= 99.9).sum()),
            'countries_below_50': int((latest_data[self.target_col] < 50).sum())
        }
