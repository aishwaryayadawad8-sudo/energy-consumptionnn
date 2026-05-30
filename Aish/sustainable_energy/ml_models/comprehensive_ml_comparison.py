"""
Comprehensive ML Model Comparison Across All Objectives
Compares 7 ML algorithms across 8 sub-objectives
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, accuracy_score
import xgboost as xgb
import lightgbm as lgb
from catboost import CatBoostRegressor, CatBoostClassifier
import warnings
warnings.filterwarnings('ignore')


class ComprehensiveMLComparison:
    """Compare 7 ML algorithms across all 8 objectives"""
    
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.results = {}
        
        # Define all 8 sub-objectives
        self.objectives = [
            {
                "sub_no": 1,
                "name": "Predict Energy Consumption",
                "task": "regression",
                "target": "Primary energy consumption per capita (kWh/person)",
                "features": ['Year', 'gdp_per_capita', 'Renewable energy share in the total final energy consumption (%)',
                           'Electricity from fossil fuels (TWh)', 'Electricity from renewables (TWh)']
            },
            {
                "sub_no": 2,
                "name": "CO2 Emission Forecasting",
                "task": "regression",
                "target": "Value_co2_emissions_kt_by_country",
                "features": ['Year', 'Primary energy consumption per capita (kWh/person)', 
                           'Electricity from fossil fuels (TWh)', 'gdp_per_capita']
            },
            {
                "sub_no": 3,
                "name": "Energy Access Classification",
                "task": "classification",
                "target": "Access to electricity (% of population)",
                "features": ['Year', 'gdp_per_capita', 'Renewable energy share in the total final energy consumption (%)',
                           'Electricity from renewables (TWh)']
            },
            {
                "sub_no": 4,
                "name": "SDG 7 Monitoring",
                "task": "regression",
                "target": "Access to electricity (% of population)",
                "features": ['Year', 'gdp_per_capita', 'Renewable energy share in the total final energy consumption (%)',
                           'Electricity from renewables (TWh)', 'Electricity from fossil fuels (TWh)']
            },
            {
                "sub_no": 5,
                "name": "Energy Equity Analysis",
                "task": "regression",
                "target": "Access to clean fuels for cooking",
                "features": ['Year', 'gdp_per_capita', 'Access to electricity (% of population)',
                           'Renewable energy share in the total final energy consumption (%)']
            },
            {
                "sub_no": 6,
                "name": "Efficiency Optimization",
                "task": "classification",
                "target": "Renewable energy share in the total final energy consumption (%)",
                "features": ['Year', 'gdp_per_capita', 'Electricity from renewables (TWh)',
                           'Electricity from fossil fuels (TWh)', 'Access to electricity (% of population)']
            },
            {
                "sub_no": 7,
                "name": "Renewable Energy Potential",
                "task": "regression",
                "target": "Renewable-electricity-generating-capacity-per-capita",
                "features": ['Year', 'gdp_per_capita', 'Renewable energy share in the total final energy consumption (%)',
                           'Electricity from renewables (TWh)']
            },
            {
                "sub_no": 8,
                "name": "Investment Strategies",
                "task": "regression",
                "target": "Financial flows to developing countries (US $)",
                "features": ['Year', 'gdp_per_capita', 'Renewable energy share in the total final energy consumption (%)',
                           'Access to electricity (% of population)']
            }
        ]
    
    def load_and_clean_data(self):
        """Load and clean the dataset"""
        self.df = pd.read_csv(self.csv_path)
        
        # Clean column names
        self.df.columns = self.df.columns.str.strip()
        
        # Handle missing values
        numeric_columns = self.df.select_dtypes(include=[np.number]).columns
        self.df[numeric_columns] = self.df[numeric_columns].fillna(self.df[numeric_columns].median())
        
        return self.df
    
    def classify_target(self, values, task):
        """Convert continuous values to classes for classification tasks"""
        if task == "classification":
            # Create 3 classes: Low, Medium, High
            percentile_33 = np.percentile(values, 33)
            percentile_67 = np.percentile(values, 67)
            
            classes = []
            for val in values:
                if val < percentile_33:
                    classes.append(0)  # Low
                elif val < percentile_67:
                    classes.append(1)  # Medium
                else:
                    classes.append(2)  # High
            return np.array(classes)
        return values
    
    def train_all_models(self, X_train, X_test, y_train, y_test, task):
        """Train all 7 ML models and return scores"""
        scores = {}
        
        if task == "regression":
            # Regression models
            models = {
                "Linear Regression": LinearRegression(),
                "Decision Tree": DecisionTreeRegressor(random_state=42, max_depth=10),
                "KNN": KNeighborsRegressor(n_neighbors=5),
                "XGBoost": xgb.XGBRegressor(random_state=42, n_estimators=100, max_depth=5, verbosity=0),
                "LightGBM": lgb.LGBMRegressor(random_state=42, n_estimators=100, max_depth=5, verbosity=-1),
                "CatBoost": CatBoostRegressor(random_state=42, iterations=100, depth=5, verbose=False),
                "Random Forest": RandomForestRegressor(random_state=42, n_estimators=100, max_depth=10)
            }
            
            for name, model in models.items():
                try:
                    model.fit(X_train, y_train)
                    y_pred = model.predict(X_test)
                    mse = mean_squared_error(y_test, y_pred)
                    scores[name] = mse
                except Exception as e:
                    print(f"Error training {name}: {e}")
                    scores[name] = float('inf')
        
        else:  # classification
            models = {
                "Logistic Regression": LogisticRegression(random_state=42, max_iter=1000),
                "Decision Tree": DecisionTreeClassifier(random_state=42, max_depth=10),
                "KNN": KNeighborsClassifier(n_neighbors=5),
                "XGBoost": xgb.XGBClassifier(random_state=42, n_estimators=100, max_depth=5, verbosity=0, use_label_encoder=False, eval_metric='mlogloss'),
                "LightGBM": lgb.LGBMClassifier(random_state=42, n_estimators=100, max_depth=5, verbosity=-1),
                "CatBoost": CatBoostClassifier(random_state=42, iterations=100, depth=5, verbose=False),
                "Random Forest": RandomForestClassifier(random_state=42, n_estimators=100, max_depth=10)
            }
            
            for name, model in models.items():
                try:
                    model.fit(X_train, y_train)
                    y_pred = model.predict(X_test)
                    accuracy = accuracy_score(y_test, y_pred)
                    scores[name] = accuracy
                except Exception as e:
                    print(f"Error training {name}: {e}")
                    scores[name] = 0.0
        
        return scores
    
    def compare_all_objectives(self):
        """Compare all 7 models across all 8 objectives"""
        self.load_and_clean_data()
        
        for obj in self.objectives:
            sub_no = obj["sub_no"]
            name = obj["name"]
            task = obj["task"]
            target = obj["target"]
            features = obj["features"]
            
            print(f"\n{'='*70}")
            print(f"Sub-objective {sub_no}: {name} ({task})")
            print(f"{'='*70}")
            
            try:
                # Prepare data
                available_features = [f for f in features if f in self.df.columns]
                if target not in self.df.columns:
                    print(f"Target '{target}' not found in dataset")
                    continue
                
                # Drop rows with missing values
                data = self.df[available_features + [target]].dropna()
                
                if len(data) < 100:
                    print(f"Insufficient data: only {len(data)} samples")
                    continue
                
                X = data[available_features]
                y = data[target]
                
                # Convert to classification if needed
                if task == "classification":
                    y = self.classify_target(y.values, task)
                
                # Split data
                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, test_size=0.2, random_state=42
                )
                
                # Scale features
                scaler = StandardScaler()
                X_train_scaled = scaler.fit_transform(X_train)
                X_test_scaled = scaler.transform(X_test)
                
                # Train all models
                scores = self.train_all_models(
                    X_train_scaled, X_test_scaled, y_train, y_test, task
                )
                
                # Store results
                self.results[sub_no] = scores
                
                # Print results
                metric = "Accuracy" if task == "classification" else "MSE"
                for model_name, score in scores.items():
                    print(f"{model_name}: {metric} = {score:.4f}")
                
                # Find best model
                if task == "classification":
                    best_model = max(scores, key=scores.get)
                    best_score = scores[best_model]
                else:
                    best_model = min(scores, key=scores.get)
                    best_score = scores[best_model]
                
                print(f"\n✅ Best Model: {best_model} with {metric}={best_score:.4f}")
                
            except Exception as e:
                print(f"Error processing objective {sub_no}: {e}")
                import traceback
                traceback.print_exc()
        
        return self.results
    
    def get_summary(self):
        """Get summary of best models for each objective"""
        summary = {}
        
        for sub_no, scores in self.results.items():
            obj = next(o for o in self.objectives if o["sub_no"] == sub_no)
            task = obj["task"]
            
            if task == "classification":
                best_model = max(scores, key=scores.get)
                best_score = scores[best_model]
            else:
                best_model = min(scores, key=scores.get)
                best_score = scores[best_model]
            
            summary[sub_no] = {
                "name": obj["name"],
                "task": task,
                "best_model": best_model,
                "best_score": best_score,
                "all_scores": scores
            }
        
        return summary
    
    def get_results_for_api(self):
        """Format results for API response"""
        return {
            "objectives": self.objectives,
            "results": self.results,
            "summary": self.get_summary()
        }
