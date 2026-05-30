"""
Objective 5: Energy Equity Analysis
Based on the provided code for SDG7 tracking with multiple ML models
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
import os


class Objective5EnergyEquity:
    """Energy Equity Analysis using multiple regression models"""
    
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.df_sdg7 = None
        self.models = {}
        self.mse_scores = {}
        self.best_model_name = None
        self.best_model = None
        self.country_map = {}
        self.scaler = StandardScaler()
        self.imputer = SimpleImputer(strategy='mean')
        
    def load_and_clean_data(self):
        """Load and clean the dataset"""
        self.df = pd.read_csv(self.csv_path)
        
        # Clean column names
        self.df.columns = (
            self.df.columns
            .str.strip()
            .str.replace('\n', ' ')
            .str.replace(r'\s+', ' ', regex=True)
        )
        
        # Convert numeric columns
        for col in self.df.columns:
            if col not in ['Entity']:
                self.df[col] = self.df[col].astype(str).str.replace(',', '', regex=False)
                self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
        
        # Prepare SDG7 dataset
        target_col = 'Access to electricity (% of population)'
        self.df_sdg7 = self.df[['Year', 'Entity', target_col]].dropna().copy()
        
        # Encode Entity to numeric country codes
        self.df['Entity'] = self.df['Entity'].astype('category')
        self.df['Country_Code'] = self.df['Entity'].cat.codes
        
        # Create country mapping
        self.country_map = dict(zip(self.df['Country_Code'], self.df['Entity']))
        
        # Impute and scale numerical features
        num_cols = self.df.select_dtypes(include=[np.number]).columns.drop(['Country_Code'])
        self.df[num_cols] = self.imputer.fit_transform(self.df[num_cols])
        self.df[num_cols] = self.scaler.fit_transform(self.df[num_cols])
        
        return True
    
    def train_and_compare_models(self):
        """Train multiple models and compare MSE scores"""
        target_col = 'Access to electricity (% of population)'
        
        X = self.df.drop(columns=[target_col, 'Entity'])
        y = self.df[target_col]
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=0
        )
        
        self.models = {
            "Linear Regression": LinearRegression(),
            "Decision Tree": DecisionTreeRegressor(random_state=0),
            "KNN": KNeighborsRegressor(),
            "XGBoost": XGBRegressor(objective='reg:squarederror', random_state=0)
        }
        
        self.mse_scores = {}
        for name, model in self.models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            self.mse_scores[name] = mse
            print(f"{name} MSE: {mse:.4f}")
        
        # Find best model (lowest MSE)
        self.best_model_name = min(self.mse_scores, key=self.mse_scores.get)
        self.best_model = self.models[self.best_model_name]
        
        return self.mse_scores
    
    def get_historical_data(self, country=None):
        """Get historical access to electricity data with classification"""
        if country:
            country_data = self.df_sdg7[self.df_sdg7['Entity'] == country].copy()
            country_data = country_data.sort_values('Year')
            # Add access level classification
            country_data['access_level'] = country_data['Access to electricity (% of population)'].apply(
                self.classify_access_level
            )
            return country_data.to_dict('records')
        else:
            # Return all countries with classification
            all_data = self.df_sdg7.copy()
            all_data['access_level'] = all_data['Access to electricity (% of population)'].apply(
                self.classify_access_level
            )
            return all_data.to_dict('records')
    
    def classify_access_level(self, access_percentage):
        """Classify access percentage into High/Medium/Low"""
        if access_percentage >= 80:
            return "High Access"
        elif access_percentage >= 50:
            return "Medium Access"
        else:
            return "Low Access"
    
    def predict_future_access(self, years, country=None):
        """Predict future access to electricity with classification"""
        # Prepare simple dataset for forecasting
        df_future = self.df_sdg7.copy()
        df_future['Country_Code'] = df_future['Entity'].astype('category').cat.codes
        
        # Update country map
        country_map = dict(zip(df_future['Country_Code'], df_future['Entity']))
        
        target_col = 'Access to electricity (% of population)'
        X_future = df_future[['Year', 'Country_Code']]
        y_future = df_future[target_col]
        
        # Use Linear Regression for future predictions (simple and reliable)
        model_simple = LinearRegression()
        model_simple.fit(X_future, y_future)
        
        last_year = int(df_future['Year'].max())
        future_years = np.arange(last_year + 1, last_year + 1 + years)
        
        if country:
            # Get country code
            country_code = df_future[df_future['Entity'] == country]['Country_Code'].iloc[0]
            
            # Predict for specific country
            future_data = pd.DataFrame({
                'Year': future_years,
                'Country_Code': [country_code] * len(future_years)
            })
            
            predictions = model_simple.predict(future_data)
            
            # Clip predictions to 0-100 range
            predictions = np.clip(predictions, 0, 100)
            
            result = []
            for i, year in enumerate(future_years):
                access_pct = float(predictions[i])
                result.append({
                    'year': int(year),
                    'predicted_access': access_pct,
                    'access_level': self.classify_access_level(access_pct)
                })
            
            return result
        else:
            # Predict for all countries
            countries = df_future['Country_Code'].unique()
            future_data = pd.DataFrame([
                {'Year': yr, 'Country_Code': c}
                for yr in future_years
                for c in countries
            ])
            
            future_data[target_col] = model_simple.predict(future_data)
            future_data[target_col] = np.clip(future_data[target_col], 0, 100)
            future_data['Country'] = future_data['Country_Code'].map(country_map)
            
            # Add access level classification
            future_data['access_level'] = future_data[target_col].apply(self.classify_access_level)
            
            return future_data.to_dict('records')
    
    def get_all_countries(self):
        """Get list of all countries"""
        if self.df_sdg7 is not None:
            countries = sorted(self.df_sdg7['Entity'].unique().tolist())
            return countries
        return []
    
    def get_combined_historical_future(self, country):
        """Get combined historical and future data for a country"""
        historical = self.get_historical_data(country)
        future = self.predict_future_access(10, country)
        
        if not historical or not future:
            return None
        
        combined = []
        
        # Add historical data
        for item in historical:
            combined.append({
                'year': int(item['Year']),
                'access': float(item['Access to electricity (% of population)']),
                'type': 'historical'
            })
        
        # Add future predictions
        for item in future:
            combined.append({
                'year': int(item['year']),
                'access': float(item['predicted_access']),
                'type': 'predicted'
            })
        
        return combined


# Test the class
if __name__ == "__main__":
    import os
    
    # Get the CSV path
    csv_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        'global-data-on-sustainable-energy.csv'
    )
    
    print("Testing Objective 5 Energy Equity Analysis")
    print("=" * 60)
    
    # Initialize
    obj5 = Objective5EnergyEquity(csv_path)
    
    # Load data
    print("\n1. Loading and cleaning data...")
    obj5.load_and_clean_data()
    print(f"   ✓ Loaded {len(obj5.df)} rows")
    print(f"   ✓ SDG7 data: {len(obj5.df_sdg7)} rows")
    
    # Train models
    print("\n2. Training and comparing models...")
    mse_scores = obj5.train_and_compare_models()
    print(f"   ✓ Best model: {obj5.best_model_name}")
    
    # Get countries
    print("\n3. Getting countries...")
    countries = obj5.get_all_countries()
    print(f"   ✓ Found {len(countries)} countries")
    print(f"   Sample: {countries[:5]}")
    
    # Test historical data
    print("\n4. Testing historical data for Belarus...")
    historical = obj5.get_historical_data('Belarus')
    print(f"   ✓ Found {len(historical)} historical points")
    if historical:
        print(f"   Sample: Year {historical[0]['Year']}, Access: {historical[0]['Access to electricity (% of population)']}%")
    
    # Test predictions
    print("\n5. Testing future predictions for Belarus...")
    predictions = obj5.predict_future_access(10, 'Belarus')
    print(f"   ✓ Generated {len(predictions)} prediction points")
    if predictions:
        print(f"   Sample: Year {predictions[0]['year']}, Predicted: {predictions[0]['predicted_access']:.2f}%")
    
    # Test combined data
    print("\n6. Testing combined historical + future for Belarus...")
    combined = obj5.get_combined_historical_future('Belarus')
    if combined:
        hist_count = sum(1 for x in combined if x['type'] == 'historical')
        pred_count = sum(1 for x in combined if x['type'] == 'predicted')
        print(f"   ✓ Historical: {hist_count}, Predicted: {pred_count}")
    
    print("\n" + "=" * 60)
    print("Testing Complete!")
