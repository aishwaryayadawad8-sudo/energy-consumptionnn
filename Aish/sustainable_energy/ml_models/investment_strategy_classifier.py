"""
Objective 8: Renewable Energy Investment Strategy Classification
Combines multiple features to classify investment potential
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.metrics import mean_squared_error


class InvestmentStrategyClassifier:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.models = {}
        self.mse_scores = {}
        self.best_model = None
        self.best_model_name = None
        self.label_encoder = LabelEncoder()
        self.scaler = StandardScaler()
        self.country_map = {}
        
    def load_and_clean_data(self):
        """Load and preprocess data"""
        df = pd.read_csv(self.csv_path)
        
        # Select required columns
        df = df[[
            'Year', 
            'Entity',
            'Access to electricity (% of population)',
            'Renewable-electricity-generating-capacity-per-capita',
            'Renewable energy share in the total final energy consumption (%)'
        ]].dropna()
        
        # Rename for simplicity
        df.rename(columns={
            'Access to electricity (% of population)': 'Access',
            'Renewable-electricity-generating-capacity-per-capita': 'Capacity',
            'Renewable energy share in the total final energy consumption (%)': 'RE_Share'
        }, inplace=True)
        
        # Create Investment Score (weighted combination)
        df['Investment_Score'] = (
            0.4 * df['RE_Share'] +
            0.4 * df['Capacity'] +
            0.2 * df['Access']
        )
        
        # Classify into investment categories
        df['Investment_Category'] = pd.cut(
            df['Investment_Score'],
            bins=[-1, 30, 70, np.inf],
            labels=['Low Potential', 'Medium Potential', 'High Potential']
        )
        
        # Encode country and target
        df['Country_Code'] = df['Entity'].astype('category').cat.codes
        df['Target'] = self.label_encoder.fit_transform(df['Investment_Category'])
        
        self.country_map = dict(zip(df['Country_Code'], df['Entity']))
        self.df = df
        
    def train_and_compare_models(self):
        """Train models and compare MSE"""
        X = self.df[['Year', 'Country_Code', 'RE_Share', 'Capacity', 'Access']]
        y = self.df['Target']
        
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )
        
        self.models = {
            "Logistic Regression": LogisticRegression(max_iter=1000),
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
        """Get historical investment score data"""
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
                'Investment_Score': float(row['Investment_Score']),
                'Investment_Category': str(row['Investment_Category']),
                'RE_Share': float(row['RE_Share']),
                'Capacity': float(row['Capacity']),
                'Access': float(row['Access'])
            })
        
        return result
    
    def predict_future_investment(self, years=10, country=None):
        """Predict future investment categories"""
        X = self.df[['Year', 'Country_Code', 'RE_Share', 'Capacity', 'Access']]
        y = self.df['Target']
        X_scaled = self.scaler.fit_transform(X)
        
        # Use best model
        best_model = LogisticRegression(max_iter=1000).fit(X_scaled, y)
        
        last_year = int(self.df['Year'].max())
        future_years = np.arange(last_year + 1, last_year + years + 1)
        
        if country:
            country_data = self.df[self.df['Entity'] == country]
            if country_data.empty:
                return None
            countries = country_data['Country_Code'].unique()
        else:
            countries = self.df['Country_Code'].unique()
        
        # Get latest values for each country
        latest = self.df.sort_values('Year').groupby('Country_Code').last()
        
        predictions = []
        for yr in future_years:
            for c in countries:
                if c in latest.index:
                    latest_data = latest.loc[c]
                    features = [[
                        yr, 
                        c, 
                        latest_data['RE_Share'], 
                        latest_data['Capacity'], 
                        latest_data['Access']
                    ]]
                    features_scaled = self.scaler.transform(features)
                    pred_code = best_model.predict(features_scaled)[0]
                    category = self.label_encoder.inverse_transform([pred_code])[0]
                    
                    predictions.append({
                        'year': int(yr),
                        'country': self.country_map[c],
                        'country_code': int(c),
                        'predicted_category': str(category),
                        'predicted_code': int(pred_code)
                    })
        
        return predictions
    
    def get_combined_historical_future(self, country=None):
        """Get combined historical and future data"""
        historical = self.get_historical_data(country)
        future = self.predict_future_investment(10, country)
        
        if future is None:
            return historical
        
        # Format historical
        hist_formatted = []
        for h in historical:
            hist_formatted.append({
                'year': h['Year'],
                'country': h['Entity'],
                'investment_category': h['Investment_Category'],
                'type': 'historical'
            })
        
        # Format future
        future_formatted = []
        for f in future:
            future_formatted.append({
                'year': f['year'],
                'country': f['country'],
                'investment_category': f['predicted_category'],
                'type': 'predicted'
            })
        
        return hist_formatted + future_formatted
    
    def get_all_countries(self):
        """Get list of all countries"""
        countries = sorted(self.df['Entity'].unique().tolist())
        return countries
