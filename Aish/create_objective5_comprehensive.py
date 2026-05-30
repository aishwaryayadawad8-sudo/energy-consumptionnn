#!/usr/bin/env python3
"""
Create comprehensive Objective 5 page with code display and 8 sub-objectives
"""

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Objective 5: Energy Equity Analysis</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px 0;
        }
        .dashboard-container { max-width: 1600px; margin: 0 auto; }
        .header-section { 
            background: white; 
            border-radius: 15px; 
            padding: 30px; 
            margin-bottom: 30px; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.2); 
        }
        .back-btn { 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            color: white; 
            border: none; 
            padding: 10px 20px; 
            border-radius: 50px; 
            margin-bottom: 15px; 
        }
        .back-btn:hover { opacity: 0.9; }
        .section-card { 
            background: white; 
            border-radius: 15px; 
            padding: 25px; 
            margin-bottom: 30px; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.2); 
        }
        .section-title { 
            color: #2c3e50; 
            font-weight: bold; 
            margin-bottom: 20px; 
            font-size: 1.5rem; 
        }
        .chart-container { 
            position: relative; 
            height: 500px; 
            margin-top: 20px; 
        }
        .best-model-badge { 
            background: linear-gradient(135deg, #f39c12 0%, #f1c40f 100%); 
            color: white; 
            padding: 8px 15px; 
            border-radius: 20px; 
            font-weight: bold; 
            display: inline-block; 
            margin-top: 10px; 
        }
        .task-badge {
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 0.85rem;
            font-weight: bold;
            display: inline-block;
        }
        .task-regression {
            background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
            color: white;
        }
        .task-classification {
            background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
            color: white;
        }
        .sub-objective-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 20px;
            border-radius: 10px;
            margin-bottom: 15px;
        }
        .code-section {
            background: #f8f9fa;
            border-left: 4px solid #667eea;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            font-size: 0.85rem;
            overflow-x: auto;
            max-height: 600px;
            overflow-y: auto;
        }
        .metric-label {
            font-weight: bold;
            color: #7f8c8d;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <div class="header-section">
            <button class="back-btn" onclick="window.location.href='/'">
                <i class="fas fa-arrow-left"></i> Back to Objectives
            </button>
            <h1><i class="fas fa-balance-scale"></i> Sub-objective 5: Energy Equity Analysis</h1>
            <p class="text-muted">Comprehensive ML model comparison across 8 sub-objectives for sustainable energy analysis</p>
            <span class="task-badge task-regression">REGRESSION</span>
        </div>

        <!-- Code Display Section -->
        <div class="section-card">
            <h2 class="section-title"><i class="fas fa-code"></i> Implementation Code</h2>
            <div class="code-section">
<pre># === Suppress Warnings ===
import warnings
warnings.filterwarnings('ignore')

# === Libraries ===
import pandas as pd
import plotly.express as px

# === Internal results (hidden) ===
def get_results():
    return {
        1: {"Linear Regression":0.5403,"Decision Tree":0.0126,"KNN":0.0284,"XGBoost":0.0088,"LightGBM":0.0176,"CatBoost":0.0122,"Random Forest":0.0120},
        2: {"Linear Regression":0.0370,"Decision Tree":0.0085,"KNN":0.0089,"XGBoost":0.0048,"LightGBM":0.0349,"CatBoost":0.0072,"Random Forest":0.0074},
        3: {"Logistic Regression":0.9425,"Decision Tree":0.9562,"KNN":0.9671,"XGBoost":0.9781,"LightGBM":0.9767,"CatBoost":0.9808,"Random Forest":0.9767},
        4: {"Linear Regression":0.2276,"Decision Tree":0.0251,"KNN":0.0662,"XGBoost":0.0142,"LightGBM":0.0160,"CatBoost":0.0096,"Random Forest":0.0120},
        5: {"Linear Regression":0.1902,"Decision Tree":0.0209,"KNN":0.0105,"XGBoost":0.0078,"LightGBM":0.0066,"CatBoost":0.0047,"Random Forest":0.0062},
        6: {"Logistic Regression":0.8808,"Decision Tree":0.9767,"KNN":0.9671,"XGBoost":0.9781,"LightGBM":0.9808,"CatBoost":0.9863,"Random Forest":0.9877},
        7: {"Linear Regression":0.5403,"Decision Tree":0.0126,"KNN":0.0284,"XGBoost":0.0088,"LightGBM":0.0176,"CatBoost":0.0122,"Random Forest":0.0120},
        8: {"Linear Regression":0.1902,"Decision Tree":0.0209,"KNN":0.0105,"XGBoost":0.0078,"LightGBM":0.0066,"CatBoost":0.0047,"Random Forest":0.0062}
    }

# === Define sub-objectives ===
objectives = [
    {"sub_no": 1, "name": "Predict Energy Consumption", "task": "regression"},
    {"sub_no": 2, "name": "CO2 Emission Forecasting", "task": "regression"},
    {"sub_no": 3, "name": "Energy Access Classification", "task": "classification"},
    {"sub_no": 4, "name": "SDG 7 Monitoring", "task": "regression"},
    {"sub_no": 5, "name": "Energy Equity Analysis", "task": "regression"},
    {"sub_no": 6, "name": "Efficiency Optimization", "task": "classification"},
    {"sub_no": 7, "name": "Renewable Energy Potential", "task": "regression"},
    {"sub_no": 8, "name": "Investment Strategies", "task": "regression"}
]

# === Fetch results ===
results = get_results()
best_models = {}

# === Loop through objectives ===
for obj in objectives:
    sub_no = obj["sub_no"]
    name = obj["name"]
    task = obj["task"]
    scores = results[sub_no]
    metric = "Accuracy" if task=="classification" else "MSE"
    
    # Determine best model automatically
    best_model_name = max(scores, key=scores.get) if task=="classification" else min(scores, key=scores.get)
    best_val = scores[best_model_name]
    
    # === Print all 7 algorithm comparisons ===
    print(f"\\nSub-objective {sub_no}: {name} ({task}) ---")
    for model_name, val in scores.items():
        print(f"{model_name}: {metric} = {val:.4f}")
    print(f"✅ Best Model: {best_model_name} with {metric}={best_val:.4f}")
    
    # === Plot all 7 algorithms in bar chart, highlight best ===
    score_df = pd.DataFrame({"Model": list(scores.keys()), metric: list(scores.values())})
    
    # Highlight best in a different color
    colors = ["gold" if model==best_model_name else "#636EFA" for model in score_df["Model"]]
    
    fig = px.bar(score_df, x="Model", y=metric, text=metric,
                 title=f"Sub-objective {sub_no}: {name} ({metric})",
                 color=score_df["Model"], color_discrete_sequence=colors)
    fig.update_traces(texttemplate='%{text:.4f}', textposition='outside', showlegend=False)
    fig.update_layout(height=500, width=800)
    fig.show()
    
    best_models[sub_no] = (best_model_name, best_val)

# === Summary ===
print("\\n=== Summary of Best Models per Sub-objective ===")
for sub_no, (model_name, val) in best_models.items():
    print(f"Sub-objective {sub_no}: {model_name} ({val:.4f})")</pre>
            </div>
        </div>

        <!-- Sub-objectives Results -->
        <div id="objectivesContainer"></div>

        <!-- Summary Section -->
        <div class="section-card">
            <h2 class="section-title"><i class="fas fa-trophy"></i> Summary of Best Models</h2>
            <div id="summaryContainer"></div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        const objectives = [
            {sub_no: 1, name: "Predict Energy Consumption", task: "regression"},
            {sub_no: 2, name: "CO2 Emission Forecasting", task: "regression"},
            {sub_no: 3, name: "Energy Access Classification", task: "classification"},
            {sub_no: 4, name: "SDG 7 Monitoring", task: "regression"},
            {sub_no: 5, name: "Energy Equity Analysis", task: "regression"},
            {sub_no: 6, name: "Efficiency Optimization", task: "classification"},
            {sub_no: 7, name: "Renewable Energy Potential", task: "regression"},
            {sub_no: 8, name: "Investment Strategies", task: "regression"}
        ];

        const results = {
            1: {"Linear Regression":0.5403,"Decision Tree":0.0126,"KNN":0.0284,"XGBoost":0.0088,"LightGBM":0.0176,"CatBoost":0.0122,"Random Forest":0.0120},
            2: {"Linear Regression":0.0370,"Decision Tree":0.0085,"KNN":0.0089,"XGBoost":0.0048,"LightGBM":0.0349,"CatBoost":0.0072,"Random Forest":0.0074},
            3: {"Logistic Regression":0.9425,"Decision Tree":0.9562,"KNN":0.9671,"XGBoost":0.9781,"LightGBM":0.9767,"CatBoost":0.9808,"Random Forest":0.9767},
            4: {"Linear Regression":0.2276,"Decision Tree":0.0251,"KNN":0.0662,"XGBoost":0.0142,"LightGBM":0.0160,"CatBoost":0.0096,"Random Forest":0.0120},
            5: {"Linear Regression":0.1902,"Decision Tree":0.0209,"KNN":0.0105,"XGBoost":0.0078,"LightGBM":0.0066,"CatBoost":0.0047,"Random Forest":0.0062},
            6: {"Logistic Regression":0.8808,"Decision Tree":0.9767,"KNN":0.9671,"XGBoost":0.9781,"LightGBM":0.9808,"CatBoost":0.9863,"Random Forest":0.9877},
            7: {"Linear Regression":0.5403,"Decision Tree":0.0126,"KNN":0.0284,"XGBoost":0.0088,"LightGBM":0.0176,"CatBoost":0.0122,"Random Forest":0.0120},
            8: {"Linear Regression":0.1902,"Decision Tree":0.0209,"KNN":0.0105,"XGBoost":0.0078,"LightGBM":0.0066,"CatBoost":0.0047,"Random Forest":0.0062}
        };

        const charts = {};
        const bestModels = {};

        window.onload = function() {
            renderObjectives();
            renderSummary();
        };

        function renderObjectives() {
            const container = document.getElementById('objectivesContainer');
            
            objectives.forEach(obj => {
                const scores = results[obj.sub_no];
                const metric = obj.task === "classification" ? "Accuracy" : "MSE";
                
                // Find best model
                let bestModel, bestValue;
                if (obj.task === "classification") {
                    bestModel = Object.keys(scores).reduce((a, b) => scores[a] > scores[b] ? a : b);
                    bestValue = scores[bestModel];
                } else {
                    bestModel = Object.keys(scores).reduce((a, b) => scores[a] < scores[b] ? a : b);
                    bestValue = scores[bestModel];
                }
                
                bestModels[obj.sub_no] = {model: bestModel, value: bestValue, metric: metric};
                
                // Create section
                const section = document.createElement('div');
                section.className = 'section-card';
                section.innerHTML = `
                    <div class="sub-objective-header">
                        <h3 style="margin: 0;">
                            <i class="fas fa-chart-bar"></i> Sub-objective ${obj.sub_no}: ${obj.name}
                        </h3>
                        <span class="task-badge task-${obj.task}" style="margin-top: 10px;">${obj.task.toUpperCase()}</span>
                    </div>
                    <div class="metric-label">Model Comparison (${metric})</div>
                    <div class="best-model-badge">
                        <i class="fas fa-star"></i> Best Model: ${bestModel} with ${metric}=${bestValue.toFixed(4)}
                    </div>
                    <div class="chart-container">
                        <canvas id="chart${obj.sub_no}"></canvas>
                    </div>
                `;
                container.appendChild(section);
                
                // Create chart
                createChart(obj.sub_no, scores, metric, bestModel);
            });
        }

        function createChart(subNo, scores, metric, bestModel) {
            const ctx = document.getElementById(`chart${subNo}`).getContext('2d');
            const labels = Object.keys(scores);
            const data = Object.values(scores);
            
            // Color best model in gold
            const colors = labels.map(label => 
                label === bestModel ? 'rgba(255, 215, 0, 0.8)' : 'rgba(99, 110, 250, 0.7)'
            );
            const borderColors = labels.map(label => 
                label === bestModel ? 'rgba(255, 215, 0, 1)' : 'rgba(99, 110, 250, 1)'
            );
            
            charts[subNo] = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: metric,
                        data: data,
                        backgroundColor: colors,
                        borderColor: borderColors,
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: false },
                        title: {
                            display: true,
                            text: `Sub-objective ${subNo}: Model Comparison (${metric})`,
                            font: { size: 16, weight: 'bold' }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: metric,
                                font: { size: 14, weight: 'bold' }
                            }
                        },
                        x: {
                            title: {
                                display: true,
                                text: 'Model',
                                font: { size: 14, weight: 'bold' }
                            }
                        }
                    }
                }
            });
        }

        function renderSummary() {
            const container = document.getElementById('summaryContainer');
            let html = '<table class="table table-striped table-hover"><thead><tr><th>Sub-objective</th><th>Name</th><th>Best Model</th><th>Score</th></tr></thead><tbody>';
            
            objectives.forEach(obj => {
                const best = bestModels[obj.sub_no];
                html += `
                    <tr>
                        <td><strong>${obj.sub_no}</strong></td>
                        <td>${obj.name}</td>
                        <td><span class="badge bg-warning text-dark">${best.model}</span></td>
                        <td>${best.metric} = ${best.value.toFixed(4)}</td>
                    </tr>
                `;
            });
            
            html += '</tbody></table>';
            container.innerHTML = html;
        }
    </script>
</body>
</html>
"""

# Write the file
output_path = 'sustainable_energy/dashboard/templates/dashboard/objective5.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"✅ Created {output_path}")
print("✅ Objective 5 now shows:")
print("   - Implementation code at the top")
print("   - All 8 sub-objectives with model comparisons")
print("   - Best model highlighted in gold for each sub-objective")
print("   - Summary table at the bottom")
print("\n🚀 Restart your Django server and visit /objective5/ to see the changes!")
