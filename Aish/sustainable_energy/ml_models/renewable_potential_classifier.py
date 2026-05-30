"""
Objective 7: Renewable Energy Investment Potential Classification
Classify renewable electricity capacity into Low/Medium/High potential
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.metrics import mean_squared_error


class RenewablePotentialClassifier:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.models = {}
        self.mse_scores = {}
        self.best_model = None
        self.best_model_name = None
        self.label_encoder = LabelEncoder()
        self.country_map = {}
        
    def load_and_clean_data(self):
        """Load and preprocess data"""
        df = pd.read_csv(self.csv_path)
        df = df[['Year', 'Entity', 'Renewable-electricity-generating-capacity-per-capita']].dropna()
        df.rename(columns={'Renewable-electricity-generating-capacity-per-capita': 'Renewable_Capacity'}, inplace=True)
        
        # Categorize into potential levels
        df['Potential Level'] = pd.cut(
            df['Renewable_Capacity'],
            bins=[-1, 20, 100, np.inf],
            labels=['Low Potential', 'Medium Potential', 'High Potential']
        )
        
        df['Country_Code'] = df['Entity'].astype('category').cat.codes
        df['Target'] = self.label_encoder.fit_transform(df['Potential Level'])
        
        self.country_map = dict(zip(df['Country_Code'], df['Entity']))
        self.df = df
        
    def train_and_compare_models(self):
        """Train models and compare MSE"""
        X = self.df[['Year', 'Country_Code']]
        y = self.df['Target']
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        self.models = {
            "Logistic Regression": LogisticRegression(max_iter=200),
            "Decision Tree": DecisionTreeClassifier(random_state=42),
            "KNN": KNeighborsClassifier(),
            "XGBoost": XGBClassifier(eval_metric='mlogloss', random_state=42, verbosity=0)
        }
        
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
        """Get historical data"""
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
                'Renewable_Capacity': float(row['Renewable_Capacity']),
                'Potential Level': str(row['Potential Level'])
            })
        
        return result
    
    def predict_future_potential(self, years=10, country=None):
        """Predict future potential levels"""
        X = self.df[['Year', 'Country_Code']]
        y = self.df['Target']
        
        best_model = LogisticRegression(max_iter=200).fit(X, y)
        
        last_year = int(self.df['Year'].max())
        future_years = np.arange(last_year + 1, last_year + years + 1)
        
        if country:
            country_data = self.df[self.df['Entity'] == country]
            if country_data.empty:
                return None
            countries = country_data['Country_Code'].unique()
        else:
            countries = self.df['Country_Code'].unique()
        
        predictions = []
        for yr in future_years:
            for c in countries:
                pred_code = best_model.predict([[yr, c]])[0]
                potential_level = self.label_encoder.inverse_transform([pred_code])[0]
                
                predictions.append({
                    'year': int(yr),
                    'country': self.country_map[c],
                    'country_code': int(c),
                    'predicted_potential_level': str(potential_level),
                    'predicted_code': int(pred_code)
                })
        
        return predictions
    
    def get_combined_historical_future(self, country=None):
        """Get combined historical and future data"""
        historical = self.get_historical_data(country)
        future = self.predict_future_potential(10, country)
        
        if future is None:
            return historical
        
        # Format historical
        hist_formatted = []
        for h in historical:
            hist_formatted.append({
                'year': h['Year'],
                'country': h['Entity'],
                'potential_level': h['Potential Level'],
                'type': 'historical'
            })
        
        # Format future
        future_formatted = []
        for f in future:
            future_formatted.append({
                'year': f['year'],
                'country': f['country'],
                'potential_level': f['predicted_potential_level'],
                'type': 'predicted'
            })
        
        return hist_formatted + future_formatted
    
    def get_all_countries(self):
        """Get list of all countries"""
        countries = sorted(self.df['Entity'].unique().tolist())
        return countries
