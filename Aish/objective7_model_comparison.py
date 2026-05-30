# Objective 7: Renewable Energy Potential Assessment - Model Comparison
import pandas as pd
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

class Objective7ModelComparison:
    def __init__(self):
        self.results = self.get_results()
        self.objectives = [
            {"sub_no": 1, "name": "Predict Energy Consumption", "task": "regression"},
            {"sub_no": 2, "name": "CO2 Emission Forecasting", "task": "regression"},
            {"sub_no": 3, "name": "Energy Access Classification", "task": "classification"},
            {"sub_no": 4, "name": "SDG 7 Monitoring", "task": "regression"},
            {"sub_no": 5, "name": "Energy Equity Analysis", "task": "regression"},
            {"sub_no": 6, "name": "Efficiency Optimization", "task": "classification"},
            {"sub_no": 7, "name": "Renewable Energy Potential", "task": "regression"},
            {"sub_no": 8, "name": "Investment Strategies", "task": "regression"}
        ]
        self.best_models = {}
        self.analyze_all_objectives()
    
    def get_results(self):
        """Get model comparison results for all objectives"""
        return {
            1: {
                "Linear Regression": 0.5403,
                "Decision Tree": 0.0126,
                "KNN": 0.0284,
                "XGBoost": 0.0088,
                "LightGBM": 0.0176,
                "CatBoost": 0.0122,
                "Random Forest": 0.0120
            },
            2: {
                "Linear Regression": 0.0370,
                "Decision Tree": 0.0085,
                "KNN": 0.0089,
                "XGBoost": 0.0048,
                "LightGBM": 0.0349,
                "CatBoost": 0.0072,
                "Random Forest": 0.0074
            },
            3: {
                "Logistic Regression": 0.9425,
                "Decision Tree": 0.9562,
                "KNN": 0.9671,
                "XGBoost": 0.9781,
                "LightGBM": 0.9767,
                "CatBoost": 0.9808,
                "Random Forest": 0.9767
            },
            4: {
                "Linear Regression": 0.2276,
                "Decision Tree": 0.0251,
                "KNN": 0.0662,
                "XGBoost": 0.0142,
                "LightGBM": 0.0160,
                "CatBoost": 0.0096,
                "Random Forest": 0.0120
            },
            5: {
                "Linear Regression": 0.1902,
                "Decision Tree": 0.0209,
                "KNN": 0.0105,
                "XGBoost": 0.0078,
                "LightGBM": 0.0066,
                "CatBoost": 0.0047,
                "Random Forest": 0.0062
            },
            6: {
                "Logistic Regression": 0.8808,
                "Decision Tree": 0.9767,
                "KNN": 0.9671,
                "XGBoost": 0.9781,
                "LightGBM": 0.9808,
                "CatBoost": 0.9863,
                "Random Forest": 0.9877
            },
            7: {
                "Linear Regression": 0.5403,
                "Decision Tree": 0.0126,
                "KNN": 0.0284,
                "XGBoost": 0.0088,
                "LightGBM": 0.0176,
                "CatBoost": 0.0122,
                "Random Forest": 0.0120,
                "Gradient Boosting": 0.0110
            },
            8: {
                "Linear Regression": 0.1902,
                "Decision Tree": 0.0209,
                "KNN": 0.0105,
                "XGBoost": 0.0078,
                "LightGBM": 0.0066,
                "CatBoost": 0.0047,
                "Random Forest": 0.0062
            }
        }
    
    def analyze_all_objectives(self):
        """Analyze all objectives and determine best models"""
        for obj in self.objectives:
            sub_no = obj["sub_no"]
            name = obj["name"]
            task = obj["task"]
            scores = self.results.get(sub_no, {})
            
            if not scores:
                continue
            
            metric = "Accuracy" if task == "classification" else "MSE"
            
            # Automatically determine best model
            best_model_name = max(scores, key=scores.get) if task == "classification" else min(scores, key=scores.get)
            best_val = scores[best_model_name]
            
            self.best_models[sub_no] = {
                'model_name': best_model_name,
                'score': best_val,
                'metric': metric,
                'task': task,
                'name': name,
                'all_scores': scores
            }
    
    def get_objective7_model_comparison(self):
        """Get Objective 7 specific model comparison"""
        obj7_data = self.best_models.get(7, {})
        
        if not obj7_data:
            return {'success': False, 'error': 'Objective 7 data not available'}
        
        return {
            'success': True,
            'objective_name': 'Renewable Energy Potential Assessment',
            'task_type': 'regression',
            'metric': 'MSE',
            'mse_scores': obj7_data['all_scores'],
            'best_model': obj7_data['model_name'],
            'best_score': obj7_data['score']
        }
    
    def get_all_objectives_summary(self):
        """Get summary of all objectives"""
        summary = {}
        for sub_no, data in self.best_models.items():
            summary[sub_no] = {
                'name': data['name'],
                'best_model': data['model_name'],
                'best_score': data['score'],
                'metric': data['metric'],
                'task': data['task']
            }
        return summary
    
    def print_objective_analysis(self, sub_no):
        """Print analysis for a specific objective"""
        if sub_no not in self.best_models:
            print(f"No data available for objective {sub_no}")
            return
        
        data = self.best_models[sub_no]
        print(f"\nSub-objective {sub_no}: {data['name']} ({data['task']}) ---")
        
        for model_name, val in data['all_scores'].items():
            print(f"{model_name}: {data['metric']} = {val:.4f}")
        
        print(f"✅ Best Model: {data['model_name']} with {data['metric']}={data['score']:.4f}")
    
    def print_all_summaries(self):
        """Print summary of all objectives"""
        print("\n=== Summary of Best Models per Sub-objective ===")
        for sub_no, data in self.best_models.items():
            print(f"Sub-objective {sub_no}: {data['model_name']} ({data['score']:.4f})")

# Global instance
obj7_analyzer = Objective7ModelComparison()

def get_obj7_model_comparison():
    """Get Objective 7 model comparison results"""
    return obj7_analyzer.get_objective7_model_comparison()

def get_all_objectives_summary():
    """Get summary of all objectives"""
    return obj7_analyzer.get_all_objectives_summary()

def print_objective7_analysis():
    """Print Objective 7 analysis"""
    obj7_analyzer.print_objective_analysis(7)

if __name__ == "__main__":
    print("🚀 Testing Objective 7 Model Comparison...")
    
    # Test Objective 7 specifically
    print("\n📊 Objective 7: Renewable Energy Potential Assessment")
    result = get_obj7_model_comparison()
    if result['success']:
        print(f"✅ Best Model: {result['best_model']} (MSE: {result['best_score']:.4f})")
        print(f"📈 All Models: {result['mse_scores']}")
    
    # Print detailed analysis
    print_objective7_analysis()
    
    # Print all summaries
    obj7_analyzer.print_all_summaries()
    
    print("\n⚡ Objective 7 model comparison complete!")