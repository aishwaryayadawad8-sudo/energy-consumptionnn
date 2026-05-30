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

class CO2EmissionsPredictor:
    """Objective 3: Predict Carbon Emissions"""
    
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
        
        target_col = "Value_co2_emissions_kt_by_country"
        
        # Drop rows where target is missing
        df_model = self.df.dropna(subset=[target_col]).copy()
        
        # Separate features and target
        X = df_model.drop(columns=[target_col, 'Entity'])
        y = df_model[target_col]
        
        # Get numeric columns
        num_cols = X.select_dtypes(include=[np.number]).columns
        
        # Impute missing values
        X[num_cols] = self.imputer.fit_transform(X[num_cols])
        
        # Final check for non-numeric data
        for col in X.columns:
            if not pd.api.types.is_numeric_dtype(X[col]):
                X[col] = pd.to_numeric(X[col], errors='coerce')
                X[col] = self.imputer.fit_transform(X[[col]])[:, 0]
        
        # Check target
        if not pd.api.types.is_numeric_dtype(y):
            y = pd.to_numeric(y, errors='coerce')
            if y.isnull().any():
                y = pd.Series(self.imputer.fit_transform(y.to_frame())[:, 0], name=y.name)
        
        # Handle any remaining NaN or Inf values
        if X.isnull().values.any() or np.isinf(X.values).any():
            X = pd.DataFrame(self.imputer.fit_transform(X), columns=X.columns)
        
        if y.isnull().values.any() or np.isinf(y.values).any():
            y = pd.Series(self.imputer.fit_transform(y.to_frame())[:, 0], name=y.name)
        
        # Scale features
        X[num_cols] = self.scaler.fit_transform(X[num_cols])
        
        return train_test_split(X, y, test_size=0.2, random_state=0)
    
    def train_and_compare_models(self):
        """Train multiple models and compare MSE scores"""
        X_train, X_test, y_train, y_test = self.prepare_features()
        
        self.models = {
            "Linear Regression": LinearRegression(),
            "Decision Tree": DecisionTreeRegressor(random_state=0),
            "K-Nearest Neighbors": KNeighborsRegressor(),
            "XGBoost": XGBRegressor(objective='reg:squarederror', random_state=0, verbosity=0)
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
        """Get historical CO2 emissions data"""
        if self.df is None:
            self.load_and_clean_data()
        
        target_col = "Value_co2_emissions_kt_by_country"
        df_hist = self.df[['Year', 'Entity', target_col]].dropna()
        
        if country_name:
            df_hist = df_hist[df_hist['Entity'].str.lower() == country_name.lower()]
        
        return df_hist.to_dict('records')
    
    def predict_future_emissions(self, years_ahead=10, country_name=None):
        """Predict future CO2 emissions with realistic variations"""
        if self.df is None:
            self.load_and_clean_data()
        
        target_col = "Value_co2_emissions_kt_by_country"
        df_simple = self.df[['Year', 'Entity', 'Country_Code', target_col]].dropna()
        
        # Filter by country if specified
        if country_name:
            df_simple = df_simple[df_simple['Entity'].str.lower() == country_name.lower()]
            if df_simple.empty:
                return None
        
        predictions = []
        
        if country_name:
            # Single country prediction with polynomial trend and variations
            country_data = df_simple.sort_values('Year')
            years = country_data['Year'].values.reshape(-1, 1)
            emissions = country_data[target_col].values
            
            # Calculate historical volatility for realistic variations
            if len(emissions) > 1:
                year_changes = np.diff(emissions)
                volatility = np.std(year_changes) * 0.8  # Use 80% of historical volatility for more zigzag
            else:
                volatility = np.std(emissions) * 0.05
            
            # Use polynomial features for better trend capture
            from sklearn.preprocessing import PolynomialFeatures
            poly = PolynomialFeatures(degree=2)
            years_poly = poly.fit_transform(years)
            
            model = LinearRegression()
            model.fit(years_poly, emissions)
            
            # Generate future predictions with variations
            last_year = int(country_data['Year'].max())
            future_years = np.arange(last_year + 1, last_year + years_ahead + 1).reshape(-1, 1)
            future_years_poly = poly.transform(future_years)
            future_predictions = model.predict(future_years_poly)
            
            # Add realistic fluctuations with more pronounced zigzag
            np.random.seed(42)  # For reproducibility
            for i, (year, pred_value) in enumerate(zip(future_years.flatten(), future_predictions)):
                # Add some variation with alternating direction for zigzag effect
                base_variation = np.random.normal(0, volatility * (1 + i * 0.15))
                # Add alternating pattern for more zigzag
                alternating_factor = 1 if i % 2 == 0 else -1
                variation = base_variation + (volatility * 0.5 * alternating_factor)
                adjusted_value = pred_value + variation
                
                predictions.append({
                    'year': int(year),
                    'country': country_name,
                    'predicted_emissions': float(max(0, adjusted_value))  # Ensure non-negative
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
                emissions = country_data[target_col].values
                
                # Calculate historical volatility
                if len(emissions) > 1:
                    year_changes = np.diff(emissions)
                    volatility = np.std(year_changes) * 0.8  # Use 80% for more zigzag
                else:
                    volatility = np.std(emissions) * 0.05
                
                # Use polynomial features
                from sklearn.preprocessing import PolynomialFeatures
                poly = PolynomialFeatures(degree=2)
                years_poly = poly.fit_transform(years)
                
                model = LinearRegression()
                model.fit(years_poly, emissions)
                
                # Generate future predictions with variations
                last_year = int(country_data['Year'].max())
                future_years = np.arange(last_year + 1, last_year + years_ahead + 1).reshape(-1, 1)
                future_years_poly = poly.transform(future_years)
                future_predictions = model.predict(future_years_poly)
                
                for i, (year, pred_value) in enumerate(zip(future_years.flatten(), future_predictions)):
                    # Add variation with alternating pattern for zigzag
                    base_variation = np.random.normal(0, volatility * (1 + i * 0.15))
                    alternating_factor = 1 if i % 2 == 0 else -1
                    variation = base_variation + (volatility * 0.5 * alternating_factor)
                    adjusted_value = pred_value + variation
                    
                    predictions.append({
                        'year': int(year),
                        'country': country,
                        'predicted_emissions': float(max(0, adjusted_value))
                    })
        
        return predictions
    
    def get_all_countries(self):
        """Get list of all countries with CO2 emissions data"""
        if self.df is None:
            self.load_and_clean_data()
        
        target_col = "Value_co2_emissions_kt_by_country"
        countries = self.df[self.df[target_col].notna()]['Entity'].unique().tolist()
        return sorted([str(c) for c in countries])
