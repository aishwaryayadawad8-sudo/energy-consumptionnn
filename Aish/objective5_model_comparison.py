# === Suppress Warnings ===
import warnings
warnings.filterwarnings('ignore')

# === Libraries ===
import pandas as pd
import plotly.express as px

# === Assume results are fetched from external source ===
def get_results():
    """Replace this function with actual data loading (CSV, database, API).
    The structure should be:
    {sub_objective_no: {model_name: value, ...}, ...}
    """
    # Example hidden data internally
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
            "Random Forest": 0.0120
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

# === Define sub-objectives ===
objectives = [
    {"sub_no": 1, "name": "Energy Consumption Prediction", "task": "regression"},
    {"sub_no": 2, "name": "CO₂ Emission Forecasting", "task": "regression"},
    {"sub_no": 3, "name": "Energy Access Classification", "task": "classification"},
    {"sub_no": 4, "name": "SDG-7 Progress Monitoring", "task": "regression"},
    {"sub_no": 5, "name": "Energy Equity Analysis", "task": "regression"},
    {"sub_no": 6, "name": "Efficiency Optimization Identification", "task": "classification"},
    {"sub_no": 7, "name": "Renewable Energy Potential Assessment", "task": "regression"},
    {"sub_no": 8, "name": "Sustainable Investment Strategy Support", "task": "regression"}
]

def get_objective5_model_comparison():
    """Get model comparison results specifically for Objective 5: Energy Equity Analysis"""
    results = get_results()
    
    # Get objective 5 data
    obj = next(obj for obj in objectives if obj["sub_no"] == 5)
    sub_no = obj["sub_no"]
    name = obj["name"]
    task = obj["task"]
    scores = results.get(sub_no, {})
    
    if not scores:
        return None
    
    metric = "Accuracy" if task == "classification" else "MSE"
    
    # Automatically determine best model
    best_model_name = max(scores, key=scores.get) if task == "classification" else min(scores, key=scores.get)
    best_val = scores[best_model_name]
    
    return {
        'objective_name': name,
        'task_type': task,
        'metric': metric,
        'scores': scores,
        'best_model': best_model_name,
        'best_score': best_val
    }

def get_all_objectives_summary():
    """Get summary of all objectives with their best models"""
    results = get_results()
    best_models = {}
    
    # === Loop through objectives and get best models ===
    for obj in objectives:
        sub_no = obj["sub_no"]
        name = obj["name"]
        task = obj["task"]
        scores = results.get(sub_no, {})
        
        if not scores:
            continue
            
        # Automatically determine best model
        best_model_name = max(scores, key=scores.get) if task == "classification" else min(scores, key=scores.get)
        best_val = scores[best_model_name]
        
        best_models[sub_no] = {
            'name': name,
            'task': task,
            'best_model': best_model_name,
            'best_score': best_val,
            'metric': "Accuracy" if task == "classification" else "MSE"
        }
    
    return best_models

if __name__ == "__main__":
    # === Fetch results ===
    results = get_results()
    best_models = {}
    
    # === Loop through objectives and display results ===
    for obj in objectives:
        sub_no = obj["sub_no"]
        name = obj["name"]
        task = obj["task"]
        scores = results.get(sub_no, {})
        
        if not scores:
            print(f"\nSub-objective {sub_no}: {name} ({task}) --- No data available.")
            continue
            
        metric = "Accuracy" if task == "classification" else "MSE"
        
        # Automatically determine best model
        best_model_name = max(scores, key=scores.get) if task == "classification" else min(scores, key=scores.get)
        best_val = scores[best_model_name]
        
        # === Print all algorithm comparisons ===
        print(f"\nSub-objective {sub_no}: {name} ({task}) ---")
        for model_name, val in scores.items():
            print(f"{model_name}: {metric} = {val:.4f}")
        print(f"✅ Best Model: {best_model_name} with {metric}={best_val:.4f}")
        
        # === Plot all algorithms in bar chart, highlight best ===
        score_df = pd.DataFrame({
            "Model": list(scores.keys()), 
            metric: list(scores.values())
        })
        colors = ["gold" if model == best_model_name else "#636EFA" for model in score_df["Model"]]
        
        fig = px.bar(
            score_df,
            x="Model",
            y=metric,
            text=metric,
            title=f"Sub-objective {sub_no}: {name} ({metric})",
            color=score_df["Model"],
            color_discrete_sequence=colors
        )
        fig.update_traces(texttemplate='%{text:.4f}', textposition='outside', showlegend=False)
        fig.update_layout(height=500, width=800)
        fig.show()
        
        best_models[sub_no] = (best_model_name, best_val)
    
    # === Summary ===
    print("\n=== Summary of Best Models per Sub-objective ===")
    for sub_no, (model_name, val) in best_models.items():
        print(f"Sub-objective {sub_no}: {model_name} ({val:.4f})")