# Objective 5: Energy Equity Analysis - Country Analysis
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
import os

class Objective5CountryAnalysis:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.df_sdg7 = None
        self.models = None
        self.mse_scores = {}
        self.scaler = None
        self.imputer = None
        
    def load_and_clean_data(self):
        """Load and clean the dataset"""
        self.df = pd.read_csv(self.csv_path)
        
        # Clean column names
        self.df.columns = (self.df.columns.str.strip()
                          .str.replace('\n', ' ')
                          .str.replace(r'\s+', ' ', regex=True))
        
        # Convert all potentially numeric columns to numeric, handling commas and errors
        for col in self.df.columns:
            if col not in ['Entity']:
                self.df[col] = self.df[col].astype(str).str.replace(',', '', regex=False)
                self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
        
        # Prepare for SDG7 Tracking: Access to Electricity (% of population)
        target_col = 'Access to electricity (% of population)'
        self.df_sdg7 = self.df[['Year', 'Entity', target_col]].dropna().copy()
        
        # Encode Entity to numeric country codes
        self.df['Entity'] = self.df['Entity'].astype('category')
        self.df['Country_Code'] = self.df['Entity'].cat.codes
        
        # Impute & scale numerical features (excluding Country_Code)
        num_cols = self.df.select_dtypes(include=[np.number]).columns.drop(['Country_Code'])
        self.imputer = SimpleImputer(strategy='mean')
        self.df[num_cols] = self.imputer.fit_transform(self.df[num_cols])
        
        self.scaler = StandardScaler()
        self.df[num_cols] = self.scaler.fit_transform(self.df[num_cols])
        
        return True
    
    def train_models(self):
        """Train and compare models"""
        target_col = 'Access to electricity (% of population)'
        
        X = self.df.drop(columns=[target_col, 'Entity'])
        y = self.df[target_col]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        
        self.models = {
            "Linear Regression": LinearRegression(),
            "Decision Tree": DecisionTreeRegressor(random_state=0),
            "K-Nearest Neighbors": KNeighborsRegressor(),
            "XGBoost": XGBRegressor(objective='reg:squarederror', random_state=0)
        }
        
        self.mse_scores = {}
        for name, model in self.models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            self.mse_scores[name] = mean_squared_error(y_test, y_pred)
        
        return self.mse_scores
    
    def get_countries(self):
        """Get list of available countries"""
        if self.df_sdg7 is None:
            return []
        return sorted(self.df_sdg7['Entity'].unique().tolist())
    
    def get_historical_data(self, country=None):
        """Get historical access to electricity data"""
        if self.df_sdg7 is None:
            return None
            
        if country:
            country_data = self.df_sdg7[self.df_sdg7['Entity'] == country].copy()
            if country_data.empty:
                return None
            return country_data.to_dict('records')
        else:
            # Return all countries data
            return self.df_sdg7.to_dict('records')
    
    def get_future_predictions(self, country=None):
        """Get future predictions for access to electricity"""
        if self.df_sdg7 is None:
            return None
            
        # Prepare simple dataset for forecasting
        df_future = self.df_sdg7.copy()
        df_future['Country_Code'] = df_future['Entity'].astype('category').cat.codes
        country_map = dict(zip(df_future['Country_Code'], df_future['Entity']))
        
        if country:
            # Filter for specific country
            country_code = df_future[df_future['Entity'] == country]['Country_Code'].iloc[0] if not df_future[df_future['Entity'] == country].empty else None
            if country_code is None:
                return None
            countries = [country_code]
        else:
            countries = df_future['Country_Code'].unique()
        
        X_future = df_future[['Year', 'Country_Code']]
        y_future = df_future['Access to electricity (% of population)']
        
        model_simple = LinearRegression()
        model_simple.fit(X_future, y_future)
        
        last_year = df_future['Year'].max()
        future_years = np.arange(last_year + 1, 2031)
        
        future_data = pd.DataFrame([
            {'Year': yr, 'Country_Code': c}
            for yr in future_years for c in countries
        ])
        
        future_data['Access to electricity (% of population)'] = model_simple.predict(future_data)
        future_data['Country'] = future_data['Country_Code'].map(country_map)
        
        return future_data.to_dict('records')
    
    def get_combined_data(self, country):
        """Get combined historical and future data for a specific country"""
        historical = self.get_historical_data(country)
        future = self.get_future_predictions(country)
        
        if not historical or not future:
            return None
            
        # Combine historical and future data
        combined_data = []
        
        # Add historical data
        for record in historical:
            combined_data.append({
                'Year': record['Year'],
                'Access_Percentage': record['Access to electricity (% of population)'],
                'Type': 'Historical',
                'Country': country
            })
        
        # Add future data
        for record in future:
            combined_data.append({
                'Year': record['Year'],
                'Access_Percentage': record['Access to electricity (% of population)'],
                'Type': 'Predicted',
                'Country': record['Country']
            })
        
        return combined_data

def get_objective5_analysis(csv_path, country=None):
    """Main function to get analysis results"""
    try:
        analyzer = Objective5CountryAnalysis(csv_path)
        analyzer.load_and_clean_data()
        
        # Train models for comparison
        mse_scores = analyzer.train_models()
        
        # Get best model
        best_model = min(mse_scores, key=mse_scores.get)
        
        result = {
            'success': True,
            'mse_scores': mse_scores,
            'best_model': best_model,
            'countries': analyzer.get_countries()
        }
        
        if country:
            result['country'] = country
            result['historical_data'] = analyzer.get_historical_data(country)
            result['future_predictions'] = analyzer.get_future_predictions(country)
            result['combined_data'] = analyzer.get_combined_data(country)
        
        return result
        
    except Exception as e:
        return {'success': False, 'error': str(e)}

if __name__ == "__main__":
    # Test the implementation
    csv_path = "global-data-on-sustainable-energy.csv"  # Update path as needed
    
    print("Testing Objective 5 Country Analysis...")
    
    # Test without specific country
    result = get_objective5_analysis(csv_path)
    if result['success']:
        print(f"✅ Models trained successfully")
        print(f"📊 MSE Scores: {result['mse_scores']}")
        print(f"🏆 Best Model: {result['best_model']}")
        print(f"🌍 Available Countries: {len(result['countries'])}")
        
        # Test with specific country
        if result['countries']:
            test_country = result['countries'][0]
            country_result = get_objective5_analysis(csv_path, test_country)
            if country_result['success']:
                print(f"✅ Country analysis for {test_country} successful")
                print(f"📈 Historical data points: {len(country_result['historical_data']) if country_result['historical_data'] else 0}")
                print(f"🔮 Future predictions: {len(country_result['future_predictions']) if country_result['future_predictions'] else 0}")
            else:
                print(f"❌ Country analysis failed: {country_result['error']}")
    else:
        print(f"❌ Analysis failed: {result['error']}")