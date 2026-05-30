"""
Objective 4: SDG 7 Electricity Access Classification
Classify electricity access levels and predict future trends
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.metrics import mean_squared_error, accuracy_score
import os


class SDG7AccessClassifier:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.models = {}
        self.best_model = None
        self.best_model_name = None
        self.label_encoder = LabelEncoder()
        self.country_map = {}
        
    def load_and_clean_data(self):
        """Load and clean SDG 7 data (Electricity Access)"""
        df = pd.read_csv(self.csv_path)
        
        # Use Electricity Access (% of population)
        df = df[['Year', 'Entity', 'Access to electricity (% of population)']].dropna()
        df.rename(columns={'Access to electricity (% of population)': 'Electricity_Access'}, inplace=True)
        
        # Categorize access levels
        df['Access Level'] = pd.cut(
            df['Electricity_Access'],
            bins=[-1, 50, 90, 100],
            labels=['Low Access', 'Medium Access', 'High Access']
        )
        
        # Encode country and target
        df['Country_Code'] = df['Entity'].astype('category').cat.codes
        df['Target'] = self.label_encoder.fit_transform(df['Access Level'])
        
        # Create country mapping
        self.country_map = dict(zip(df['Country_Code'], df['Entity']))
        
        self.df = df
        
    def train_and_compare_models(self):
        """Train multiple classification models and compare MSE scores"""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_and_clean_data() first.")
        
        X = self.df[['Year', 'Country_Code']]
        y = self.df['Target']
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Define classification models
        self.models = {
            "Logistic Regression": LogisticRegression(max_iter=200),
            "Decision Tree": DecisionTreeClassifier(random_state=42),
            "KNN": KNeighborsClassifier(),
            "XGBoost": XGBClassifier(eval_metric='mlogloss', random_state=42, verbosity=0)
        }
        
        # Train and evaluate each model
        mse_scores = {}
        accuracy_scores = {}
        best_mse = float('inf')
        
        for name, model in self.models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            
            mse = mean_squared_error(y_test, y_pred)
            acc = accuracy_score(y_test, y_pred)
            
            mse_scores[name] = float(mse)
            accuracy_scores[name] = float(acc)
            
            if mse < best_mse:
                best_mse = mse
                self.best_model = model
                self.best_model_name = name
        
        return mse_scores
    
    def get_historical_data(self, country=None):
        """Get historical electricity access data"""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_and_clean_data() first.")
        
        if country:
            data = self.df[self.df['Entity'] == country].copy()
        else:
            data = self.df.copy()
        
        data = data.sort_values('Year')
        
        result = []
        for _, row in data.iterrows():
            result.append({
                'Year': int(row['Year']),
                'Entity': row['Entity'],
                'Access to electricity (% of population)': float(row['Electricity_Access']),
                'Access Level': str(row['Access Level'])
            })
        
        return result
    
    def predict_future_access(self, years=10, country=None):
        """Predict future electricity access levels"""
        if self.df is None or self.best_model is None:
            raise ValueError("Data not loaded or models not trained.")
        
        # Train on all data for best predictions
        X = self.df[['Year', 'Country_Code']]
        y = self.df['Target']
        best_model = LogisticRegression(max_iter=200).fit(X, y)
        
        last_year = int(self.df['Year'].max())
        future_years = np.arange(last_year + 1, last_year + years + 1)
        
        if country:
            # Get country code
            country_data = self.df[self.df['Entity'] == country]
            if country_data.empty:
                return None
            country_code = int(country_data['Country_Code'].iloc[0])
            countries = [country_code]
        else:
            countries = self.df['Country_Code'].unique()
        
        predictions = []
        for yr in future_years:
            for c in countries:
                pred_code = best_model.predict([[yr, c]])[0]
                access_level = self.label_encoder.inverse_transform([pred_code])[0]
                
                predictions.append({
                    'year': int(yr),
                    'country': self.country_map[c],
                    'country_code': int(c),
                    'predicted_access_level': str(access_level),
                    'predicted_code': int(pred_code)
                })
        
        return predictions
    
    def get_combined_historical_future(self, country=None):
        """Get combined historical and future data for visualization"""
        historical = self.get_historical_data(country)
        future = self.predict_future_access(10, country)
        
        if future is None:
            return historical
        
        # Convert historical to match future format
        hist_formatted = []
        for h in historical:
            hist_formatted.append({
                'year': h['Year'],
                'country': h['Entity'],
                'access_level': h['Access Level'],
                'type': 'historical'
            })
        
        # Format future
        future_formatted = []
        for f in future:
            future_formatted.append({
                'year': f['year'],
                'country': f['country'],
                'access_level': f['predicted_access_level'],
                'type': 'predicted'
            })
        
        return hist_formatted + future_formatted
    
    def get_policy_impact_data(self, country=None):
        """Get policy intervention markers for specific countries"""
        policy_years = {
            'India': 2010,
            'Bangladesh': 2008,
            'Kenya': 2013,
            'Nigeria': 2015,
            'Brazil': 2003
        }
        
        policy_markers = []
        
        for policy_country, year in policy_years.items():
            if country and country != policy_country:
                continue
            
            country_data = self.df[
                (self.df['Entity'] == policy_country) & 
                (self.df['Year'] == year)
            ]
            
            if not country_data.empty:
                policy_markers.append({
                    'country': policy_country,
                    'year': int(year),
                    'electricity_access': float(country_data['Electricity_Access'].iloc[0]),
                    'access_level': str(country_data['Access Level'].iloc[0])
                })
        
        return policy_markers
    
    def get_all_countries(self):
        """Get list of all countries in dataset"""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_and_clean_data() first.")
        
        countries = sorted(self.df['Entity'].unique().tolist())
        return countries
    
    def get_access_level_distribution(self, country=None):
        """Get distribution of access levels over time"""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_and_clean_data() first.")
        
        if country:
            data = self.df[self.df['Entity'] == country]
        else:
            data = self.df
        
        distribution = data.groupby(['Year', 'Access Level']).size().reset_index(name='count')
        
        result = []
        for _, row in distribution.iterrows():
            result.append({
                'year': int(row['Year']),
                'access_level': str(row['Access Level']),
                'count': int(row['count'])
            })
        
        return result
