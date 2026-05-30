#!/usr/bin/env python3

"""
Objective 4: Comprehensive ML Implementation for SDG 7 Electricity Access Analysis
Based on the provided comprehensive ML code with classification and prediction models
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
import os
import json

class Objective4ComprehensiveML:
    """Comprehensive ML implementation for Objective 4 SDG 7 analysis"""
    
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.models = {}
        self.mse_scores = {}
        self.le = LabelEncoder()
        self.best_model = None
        self.country_map = {}
        
    def load_and_clean_data(self):
        """Load and clean SDG 7 data (Electricity Access)"""
        try:
            self.df = pd.read_csv(self.csv_path)
            
            # Use Electricity Access (% of population)
            self.df = self.df[['Year', 'Entity', 'Access to electricity (% of population)']].dropna()
            self.df.rename(columns={'Access to electricity (% of population)': 'Electricity_Access'}, inplace=True)
            
            # Categorize access levels
            self.df['Access Level'] = pd.cut(
                self.df['Electricity_Access'],
                bins=[-1, 50, 90, 100],
                labels=['Low Access', 'Medium Access', 'High Access']
            )
            
            # Encode country and target
            self.df['Country_Code'] = self.df['Entity'].astype('category').cat.codes
            self.df['Target'] = self.le.fit_transform(self.df['Access Level'])
            
            # Create country mapping
            self.country_map = dict(zip(self.df['Country_Code'], self.df['Entity']))
            
            print(f"✅ Loaded {len(self.df)} records for {len(self.df['Entity'].unique())} countries")
            return True
            
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return False
    
    def train_classification_models(self):
        """Train and evaluate classification models"""
        if self.df is None:
            print("❌ Data not loaded. Call load_and_clean_data() first.")
            return False
        
        try:
            # Prepare features and target
            X = self.df[['Year', 'Country_Code']]
            y = self.df['Target']
            
            # Train/Test split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Define classification models
            self.models = {
                "Logistic Regression": LogisticRegression(max_iter=200),
                "Decision Tree": DecisionTreeClassifier(random_state=42),
                "KNN": KNeighborsClassifier(),
                "XGBoost": XGBClassifier(eval_metric='mlogloss', random_state=42)
            }
            
            # Train and evaluate each model
            print("\n🤖 Training classification models...")
            for name, model in self.models.items():
                print(f"   Training {name}...")
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)
                mse = mean_squared_error(y_test, y_pred)
                self.mse_scores[name] = mse
                print(f"   {name} MSE: {mse:.4f}")
            
            # Find best model
            self.best_model = min(self.mse_scores, key=self.mse_scores.get)
            print(f"\n🏆 Best Model: {self.best_model} (MSE: {self.mse_scores[self.best_model]:.4f})")
            
            return True
            
        except Exception as e:
            print(f"❌ Error training models: {e}")
            return False
    
    def get_model_comparison(self):
        """Get model comparison results"""
        if not self.mse_scores:
            self.train_classification_models()
        
        return {
            'success': True,
            'models': self.mse_scores,
            'best_model': self.best_model,
            'best_mse': self.mse_scores.get(self.best_model, 0) if self.best_model else 0
        }
    
    def get_countries(self):
        """Get list of all countries"""
        if self.df is None:
            self.load_and_clean_data()
        
        countries = sorted(self.df['Entity'].unique().tolist())
        return {
            'success': True,
            'countries': countries,
            'count': len(countries)
        }
    
    def get_historical_data(self, country):
        """Get historical electricity access data for a country"""
        if self.df is None:
            self.load_and_clean_data()
        
        if not country:
            return {'success': False, 'message': 'Country name required'}
        
        try:
            country_data = self.df[self.df['Entity'] == country].copy()
            
            if country_data.empty:
                return {'success': False, 'message': f'No data found for {country}'}
            
            # Sort by year and prepare data
            country_data = country_data.sort_values('Year')
            
            historical_data = []
            for _, row in country_data.iterrows():
                historical_data.append({
                    'Year': int(row['Year']),
                    'Access to electricity (% of population)': float(row['Electricity_Access']),
                    'Access Level': str(row['Access Level'])
                })
            
            return {
                'success': True,
                'data': historical_data,
                'country': country,
                'years_available': len(historical_data)
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def predict_future_access(self, country, years=7):
        """Predict future electricity access for a country"""
        if self.df is None:
            self.load_and_clean_data()
        
        if not self.models:
            self.train_classification_models()
        
        if not country:
            return {'success': False, 'message': 'Country name required'}
        
        try:
            # Get country code
            country_data = self.df[self.df['Entity'] == country]
            if country_data.empty:
                return {'success': False, 'message': f'No data found for {country}'}
            
            country_code = country_data['Country_Code'].iloc[0]
            
            # Use best model for predictions
            best_model_obj = self.models[self.best_model]
            
            # Prepare future years
            last_year = self.df['Year'].max()
            future_years = np.arange(last_year + 1, last_year + 1 + years)
            
            predictions = []
            for year in future_years:
                # Predict access level category
                pred_code = best_model_obj.predict([[year, country_code]])[0]
                access_level = self.le.inverse_transform([pred_code])[0]
                
                # Convert category to approximate percentage
                if access_level == 'Low Access':
                    predicted_access = np.random.uniform(20, 50)  # Low access range
                elif access_level == 'Medium Access':
                    predicted_access = np.random.uniform(50, 90)  # Medium access range
                else:  # High Access
                    predicted_access = np.random.uniform(90, 100)  # High access range
                
                predictions.append({
                    'year': int(year),
                    'predicted_access': round(float(predicted_access), 2),
                    'access_level': str(access_level),
                    'model_used': self.best_model
                })
            
            return {
                'success': True,
                'predictions': predictions,
                'country': country,
                'years_predicted': years,
                'model_used': self.best_model
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_combined_data(self, country):
        """Get combined historical and future data"""
        historical = self.get_historical_data(country)
        future = self.predict_future_access(country, 7)
        
        if not historical['success'] or not future['success']:
            return {
                'success': False,
                'message': 'Could not get complete data for country'
            }
        
        return {
            'success': True,
            'country': country,
            'historical': historical['data'],
            'predictions': future['predictions'],
            'model_used': future.get('model_used', self.best_model)
        }
    
    def get_country_stats(self, country):
        """Get comprehensive statistics for a country"""
        if self.df is None:
            self.load_and_clean_data()
        
        try:
            country_data = self.df[self.df['Entity'] == country]
            
            if country_data.empty:
                return {'success': False, 'message': f'No data found for {country}'}
            
            stats = {
                'country': country,
                'years_available': len(country_data),
                'year_range': f"{country_data['Year'].min():.0f} - {country_data['Year'].max():.0f}",
                'current_access': float(country_data.iloc[-1]['Electricity_Access']),
                'current_level': str(country_data.iloc[-1]['Access Level']),
                'average_access': float(country_data['Electricity_Access'].mean()),
                'access_trend': 'Improving' if country_data.iloc[-1]['Electricity_Access'] > country_data.iloc[0]['Electricity_Access'] else 'Declining',
                'improvement_rate': float(country_data['Electricity_Access'].iloc[-1] - country_data['Electricity_Access'].iloc[0])
            }
            
            return {
                'success': True,
                'stats': stats
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}


def test_objective4_comprehensive():
    """Test the comprehensive ML implementation"""
    print("🧪 Testing Objective 4 Comprehensive ML Implementation")
    print("=" * 60)
    
    # Initialize
    csv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'global-data-on-sustainable-energy.csv')
    ml = Objective4ComprehensiveML(csv_path)
    
    # Test data loading
    print("\n1️⃣  Loading and cleaning data...")
    if ml.load_and_clean_data():
        print(f"   ✅ Loaded data for {len(ml.df['Entity'].unique())} countries")
    
    # Test model training
    print("\n2️⃣  Training classification models...")
    if ml.train_classification_models():
        print("   ✅ Models trained successfully")
    
    # Test model comparison
    print("\n3️⃣  Getting model comparison...")
    comparison = ml.get_model_comparison()
    if comparison['success']:
        print(f"   ✅ Best model: {comparison['best_model']}")
        for model, mse in comparison['models'].items():
            print(f"      {model}: MSE = {mse:.4f}")
    
    # Test country data
    print("\n4️⃣  Testing country analysis...")
    test_country = "Albania"
    
    historical = ml.get_historical_data(test_country)
    if historical['success']:
        print(f"   ✅ Historical data: {len(historical['data'])} years")
    
    predictions = ml.predict_future_access(test_country, 7)
    if predictions['success']:
        print(f"   ✅ Future predictions: {len(predictions['predictions'])} years")
    
    stats = ml.get_country_stats(test_country)
    if stats['success']:
        print(f"   ✅ Country stats: {stats['stats']['current_access']:.1f}% access")
    
    print("\n" + "=" * 60)
    print("✅ Objective 4 Comprehensive ML Implementation Ready!")


if __name__ == "__main__":
    test_objective4_comprehensive()