"""
Advanced ML Model Comparison for SDG 7 Project
Compares 5+ ML models and selects the best one automatically
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
import warnings
warnings.filterwarnings('ignore')

# Try to import advanced models
try:
    from catboost import CatBoostRegressor
    CATBOOST_AVAILABLE = True
except:
    CATBOOST_AVAILABLE = False
    print("⚠️  CatBoost not available")

try:
    from xgboost import XGBRegressor
    XGBOOST_AVAILABLE = True
except:
    XGBOOST_AVAILABLE = False
    print("⚠️  XGBoost not available")

try:
    from lightgbm import LGBMRegressor
    LIGHTGBM_AVAILABLE = True
except:
    LIGHTGBM_AVAILABLE = False
    print("⚠️  LightGBM not available")


class AdvancedMLComparison:
    """
    Compare multiple ML models and automatically select the best one
    """
    
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.models = {}
        self.results = {}
        self.best_model = None
        self.best_model_name = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        
    def load_and_prepare_data(self):
        """Load and prepare data for training"""
        df = pd.read_csv(self.csv_path)
        
        # Select features
        feature_columns = [
            'Year',
            'Access to electricity (% of population)',
            'Access to clean fuels for cooking',
            'Renewable energy share in the total final energy consumption (%)',
            'Electricity from fossil fuels (TWh)',
            'Electricity from nuclear (TWh)',
            'Electricity from renewables (TWh)',
            'Low-carbon electricity (% electricity)',
            'Primary energy consumption per capita (kWh/person)',
            'Energy intensity level of primary energy (MJ/$2017 PPP GDP)',
            'Value_co2_emissions_kt_by_country',
            'gdp_growth',
            'gdp_per_capita',
            'Density\\n(P/Km2)',
            'Land Area(Km2)',
            'Latitude',
            'Longitude'
        ]
        
        # Filter available columns
        available_features = [col for col in feature_columns if col in df.columns]
        
        # Prepare data
        df_clean = df[available_features + ['Entity']].dropna()
        
        X = df_clean[available_features]
        y = df_clean['Access to electricity (% of population)']
        
        # Split data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        print(f"✅ Data loaded: {len(X)} samples, {len(available_features)} features")
        return self
    
    def initialize_models(self):
        """Initialize all available ML models"""
        
        # 1. CatBoost (Best overall)
        if CATBOOST_AVAILABLE:
            self.models['CatBoost'] = CatBoostRegressor(
                iterations=500,
                learning_rate=0.1,
                depth=6,
                verbose=False,
                random_state=42
            )
        
        # 2. XGBoost (Industry standard)
        if XGBOOST_AVAILABLE:
            self.models['XGBoost'] = XGBRegressor(
                n_estimators=500,
                learning_rate=0.1,
                max_depth=6,
                random_state=42,
                verbosity=0
            )
        
        # 3. LightGBM (Fastest)
        if LIGHTGBM_AVAILABLE:
            self.models['LightGBM'] = LGBMRegressor(
                n_estimators=500,
                learning_rate=0.1,
                num_leaves=31,
                random_state=42,
                verbose=-1
            )
        
        # 4. Random Forest (Reliable baseline)
        self.models['Random Forest'] = RandomForestRegressor(
            n_estimators=300,
            max_depth=10,
            random_state=42,
            n_jobs=-1
        )
        
        # 5. Gradient Boosting (Traditional)
        self.models['Gradient Boosting'] = GradientBoostingRegressor(
            n_estimators=300,
            learning_rate=0.1,
            max_depth=5,
            random_state=42
        )
        
        # 6. Neural Network (Deep Learning)
        self.models['Neural Network'] = MLPRegressor(
            hidden_layer_sizes=(100, 50, 25),
            activation='relu',
            solver='adam',
            max_iter=500,
            random_state=42,
            early_stopping=True
        )
        
        print(f"✅ Initialized {len(self.models)} models")
        return self
    
    def train_and_evaluate_all(self):
        """Train and evaluate all models"""
        print("\n🚀 Training and evaluating all models...")
        print("=" * 70)
        
        for name, model in self.models.items():
            print(f"\n📊 Training {name}...")
            
            try:
                # Train model
                model.fit(self.X_train, self.y_train)
                
                # Make predictions
                y_pred_train = model.predict(self.X_train)
                y_pred_test = model.predict(self.X_test)
                
                # Calculate metrics
                mse_train = mean_squared_error(self.y_train, y_pred_train)
                mse_test = mean_squared_error(self.y_test, y_pred_test)
                rmse_test = np.sqrt(mse_test)
                mae_test = mean_absolute_error(self.y_test, y_pred_test)
                r2_test = r2_score(self.y_test, y_pred_test)
                
                # Store results
                self.results[name] = {
                    'model': model,
                    'mse_train': mse_train,
                    'mse_test': mse_test,
                    'rmse_test': rmse_test,
                    'mae_test': mae_test,
                    'r2_test': r2_test,
                    'accuracy': r2_test * 100  # Convert R² to percentage
                }
                
                print(f"   ✅ MSE: {mse_test:.2f} | RMSE: {rmse_test:.2f} | R²: {r2_test:.4f} | Accuracy: {r2_test*100:.2f}%")
                
            except Exception as e:
                print(f"   ❌ Error training {name}: {e}")
                continue
        
        return self
    
    def select_best_model(self):
        """Select the best model based on MSE"""
        if not self.results:
            print("❌ No models trained yet!")
            return self
        
        # Find model with lowest MSE
        best_name = min(self.results.keys(), key=lambda k: self.results[k]['mse_test'])
        self.best_model_name = best_name
        self.best_model = self.results[best_name]['model']
        
        print("\n" + "=" * 70)
        print("🏆 BEST MODEL SELECTED")
        print("=" * 70)
        print(f"Model: {best_name}")
        print(f"MSE: {self.results[best_name]['mse_test']:.2f}")
        print(f"RMSE: {self.results[best_name]['rmse_test']:.2f}")
        print(f"R² Score: {self.results[best_name]['r2_test']:.4f}")
        print(f"Accuracy: {self.results[best_name]['accuracy']:.2f}%")
        print("=" * 70)
        
        return self
    
    def get_comparison_results(self):
        """Get comparison results for all models"""
        comparison = []
        
        for name, result in self.results.items():
            comparison.append({
                'model': name,
                'mse': result['mse_test'],
                'rmse': result['rmse_test'],
                'mae': result['mae_test'],
                'r2': result['r2_test'],
                'accuracy': result['accuracy']
            })
        
        # Sort by MSE (lower is better)
        comparison.sort(key=lambda x: x['mse'])
        
        return comparison
    
    def predict(self, X):
        """Make predictions using the best model"""
        if self.best_model is None:
            raise ValueError("No best model selected. Run train_and_evaluate_all() first.")
        
        return self.best_model.predict(X)
    
    def get_model_summary(self):
        """Get summary of all models"""
        return {
            'total_models': len(self.models),
            'best_model': self.best_model_name,
            'best_mse': self.results[self.best_model_name]['mse_test'] if self.best_model_name else None,
            'best_accuracy': self.results[self.best_model_name]['accuracy'] if self.best_model_name else None,
            'all_results': self.get_comparison_results()
        }


# Quick test function
if __name__ == '__main__':
    print("🧪 Testing Advanced ML Comparison")
    print("=" * 70)
    
    # Initialize
    comparison = AdvancedMLComparison('../global-data-on-sustainable-energy.csv')
    
    # Load data
    comparison.load_and_prepare_data()
    
    # Initialize models
    comparison.initialize_models()
    
    # Train and evaluate
    comparison.train_and_evaluate_all()
    
    # Select best
    comparison.select_best_model()
    
    # Show results
    print("\n📊 Final Comparison:")
    for result in comparison.get_comparison_results():
        print(f"  {result['model']:20s} - MSE: {result['mse']:6.2f} | Accuracy: {result['accuracy']:5.2f}%")
