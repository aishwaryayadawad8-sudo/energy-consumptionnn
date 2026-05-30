"""
Objective 3: Energy Access Classification
Classify electricity access into Low/Medium/High categories
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score


class EnergyAccessClassification:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.models = {}
        self.accuracy_scores = {}
        self.best_model = None
        self.best_model_name = None
        self.label_encoder = LabelEncoder()
        self.country_map = {}
        
    def load_and_clean_data(self):
        """Load and preprocess data"""
        df = pd.read_csv(self.csv_path)
        
        # Clean column names
        df.columns = df.columns.str.strip().str.replace('\n', ' ').str.replace(r'\s+', ' ', regex=True)
        
        # Select required columns
        df = df[['Year', 'Entity', 'Access to electricity (% of population)']].dropna().copy()
        
        # Create Access Level categories
        df['Access_Level'] = pd.cut(
            df['Access to electricity (% of population)'],
            bins=[-1, 50, 90, 100],
            labels=['Low Access', 'Medium Access', 'High Access']
        )
        
        # Encode country
        df['Country_Code'] = df['Entity'].astype('category').cat.codes
        self.country_map = dict(zip(df['Country_Code'], df['Entity']))
        
        self.df = df
        
    def train_and_compare_models(self):
        """Train models and compare accuracy"""
        X = self.df[['Year', 'Country_Code']]
        y = self.df['Access_Level']
        
        # Encode target
        y_encoded = self.label_encoder.fit_transform(y)
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y_encoded, test_size=0.2, random_state=42
        )
        
        self.models = {
            "Logistic Regression": LogisticRegression(max_iter=200),
            "Decision Tree": DecisionTreeClassifier(random_state=42),
            "K-Nearest Neighbors": KNeighborsClassifier(),
            "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='mlogloss', random_state=42, verbosity=0)
        }
        
        best_accuracy = 0
        for name, model in self.models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            self.accuracy_scores[name] = float(accuracy)
            
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                self.best_model = model
                self.best_model_name = name
        
        return self.accuracy_scores
    
    def get_historical_data(self, country=None):
        """Get historical electricity access data"""
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
                'Access_Percentage': float(row['Access to electricity (% of population)']),
                'Access_Level': str(row['Access_Level'])
            })
        
        return result
    
    def predict_future_access(self, years=10, country=None):
        """Predict future access levels"""
        X = self.df[['Year', 'Country_Code']]
        y = self.label_encoder.fit_transform(self.df['Access_Level'])
        
        # Use Logistic Regression as final model
        model_final = LogisticRegression(max_iter=200).fit(X, y)
        
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
                pred_encoded = model_final.predict([[yr, c]])[0]
                access_level = self.label_encoder.inverse_transform([pred_encoded])[0]
                
                predictions.append({
                    'year': int(yr),
                    'country': self.country_map[c],
                    'country_code': int(c),
                    'predicted_access_level': str(access_level)
                })
        
        return predictions
    
    def get_combined_historical_future(self, country=None):
        """Get combined historical and future data"""
        historical = self.get_historical_data(country)
        future = self.predict_future_access(10, country)
        
        if future is None:
            return historical
        
        # Format historical
        hist_formatted = []
        for h in historical:
            hist_formatted.append({
                'year': h['Year'],
                'country': h['Entity'],
                'access_level': h['Access_Level'],
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
    
    def get_all_countries(self):
        """Get list of all countries"""
        countries = sorted(self.df['Entity'].unique().tolist())
        return countries
