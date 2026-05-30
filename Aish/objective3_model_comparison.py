# === Suppress Warnings ===
import warnings
warnings.filterwarnings('ignore')

# === Libraries ===
import pandas as pd
import plotly.express as px

# === Internal results for Objective 3 only ===
def get_objective3_results():
    return {
        3: {
            "Logistic Regression": 0.9425,
            "Decision Tree": 0.9562,
            "KNN": 0.9671,
            "XGBoost": 0.9781,
            "LightGBM": 0.9767,
            "CatBoost": 0.9808,
            "Random Forest": 0.9767
        }
    }

# === Define Objective 3 ===
objective = {
    "sub_no": 3, 
    "name": "Energy Access Classification", 
    "task": "classification"
}

# === Fetch results ===
results = get_objective3_results()
best_models = {}

# === Process Objective 3 ===
sub_no = objective["sub_no"]
name = objective["name"]
task = objective["task"]
scores = results[sub_no]
metric = "Accuracy"  # Classification task

# Determine best model automatically
best_model_name = max(scores, key=scores.get)
best_val = scores[best_model_name]

# === Print all 7 algorithm comparisons ===
print(f"\nObjective {sub_no}: {name} ({task}) ---")
print("=" * 50)
for model_name, val in scores.items():
    status = "🏆 BEST" if model_name == best_model_name else "  "
    print(f"{status} {model_name}: {metric} = {val:.4f}")

print(f"\n✅ Best Model: {best_model_name} with {metric} = {best_val:.4f}")

# === Plot all 7 algorithms in bar chart, highlight best ===
score_df = pd.DataFrame({
    "Model": list(scores.keys()), 
    metric: list(scores.values())
})

# Highlight best in gold, others in blue
colors = ["gold" if model == best_model_name else "#636EFA" for model in score_df["Model"]]

fig = px.bar(
    score_df,
    x="Model",
    y=metric,
    text=metric,
    title=f"Objective {sub_no}: {name} - Model Comparison ({metric})",
    color=score_df["Model"],
    color_discrete_sequence=colors
)

fig.update_traces(
    texttemplate='%{text:.4f}', 
    textposition='outside', 
    showlegend=False
)

fig.update_layout(
    height=500, 
    width=800,
    xaxis_title="Machine Learning Models",
    yaxis_title=f"{metric} Score",
    title_x=0.5
)

fig.show()

best_models[sub_no] = (best_model_name, best_val)

# === Summary ===
print(f"\n=== Objective 3 Summary ===")
print(f"Task: {task}")
print(f"Best Model: {best_model_name}")
print(f"Best {metric}: {best_val:.4f}")
print(f"Performance: {'Excellent' if best_val > 0.95 else 'Good' if best_val > 0.85 else 'Fair'}")

# === Model Rankings ===
print(f"\n=== Model Rankings for Objective 3 ===")
sorted_models = sorted(scores.items(), key=lambda x: x[1], reverse=True)
for i, (model, score) in enumerate(sorted_models, 1):
    medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
    print(f"{medal} {model}: {score:.4f}")