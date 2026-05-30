html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Objective 3: Energy Access Classification</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px 0;
        }
        
        .dashboard-container {
            max-width: 1400px;
            margin: 0 auto;
        }
        
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
        
        .back-btn:hover {
            opacity: 0.9;
        }
        
        .section-card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        .chart-container {
            position: relative;
            height: 500px;
            margin-top: 20px;
        }
        
        .best-model-badge {
            background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
            color: white;
            padding: 8px 15px;
            border-radius: 20px;
            font-weight: bold;
            display: inline-block;
            margin-bottom: 15px;
        }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <div class="header-section">
            <button class="back-btn" onclick="window.location.href='/'">
                <i class="fas fa-arrow-left"></i> Back to Objectives
            </button>
            <h1><i class="fas fa-bolt"></i> Objective 3: Energy Access Classification</h1>
            <p class="text-muted">Machine Learning Model Comparison for Energy Access Classification</p>
        </div>
        
        <!-- Model Comparison Section -->
        <div class="section-card">
            <div class="best-model-badge"><i class="fas fa-star"></i> Best Model: CatBoost (Accuracy = 0.9808)</div>
            <div class="chart-container">
                <canvas id="accuracyChart"></canvas>
            </div>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        // Hardcoded results for Sub-objective 3 (Classification - Accuracy)
        const accuracyScores = {
            "Logistic Regression": 0.9425,
            "Decision Tree": 0.9562,
            "KNN": 0.9671,
            "XGBoost": 0.9781,
            "LightGBM": 0.9767,
            "CatBoost": 0.9808,
            "Random Forest": 0.9767
        };
        
        window.onload = function() {
            const ctx = document.getElementById('accuracyChart').getContext('2d');
            
            const modelOrder = ['Logistic Regression', 'Decision Tree', 'KNN', 'XGBoost', 'LightGBM', 'CatBoost', 'Random Forest'];
            const models = [];
            const accuracyValues = [];
            const backgroundColors = [];
            const borderColors = [];
            
            modelOrder.forEach(model => {
                if (accuracyScores[model] !== undefined) {
                    models.push(model);
                    accuracyValues.push(accuracyScores[model]);
                    
                    // Highlight CatBoost (best model) in yellow
                    if (model === 'CatBoost') {
                        backgroundColors.push('rgba(255, 193, 7, 0.8)');
                        borderColors.push('rgba(255, 193, 7, 1)');
                    } else {
                        backgroundColors.push('rgba(102, 126, 234, 0.7)');
                        borderColors.push('rgba(102, 126, 234, 1)');
                    }
                }
            });
            
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: models,
                    datasets: [{
                        label: 'Accuracy',
                        data: accuracyValues,
                        backgroundColor: backgroundColors,
                        borderColor: borderColors,
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false
                        },
                        title: {
                            display: true,
                            text: 'Sub-objective 3: Energy Access Classification (Accuracy)',
                            font: {
                                size: 18,
                                weight: 'bold'
                            },
                            padding: {
                                top: 10,
                                bottom: 20
                            },
                            align: 'start'
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return 'Accuracy: ' + context.parsed.y.toFixed(4);
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 1.0,
                            title: {
                                display: true,
                                text: 'Accuracy',
                                font: {
                                    size: 14,
                                    weight: 'bold'
                                }
                            },
                            grid: {
                                color: 'rgba(0, 0, 0, 0.05)'
                            }
                        },
                        x: {
                            grid: {
                                display: false
                            },
                            ticks: {
                                font: {
                                    size: 11
                                }
                            }
                        }
                    },
                    layout: {
                        padding: {
                            top: 30
                        }
                    }
                },
                plugins: [{
                    afterDatasetsDraw: function(chart) {
                        const ctx = chart.ctx;
                        chart.data.datasets.forEach(function(dataset, i) {
                            const meta = chart.getDatasetMeta(i);
                            if (!meta.hidden) {
                                meta.data.forEach(function(element, index) {
                                    ctx.fillStyle = 'rgb(0, 0, 0)';
                                    const fontSize = 11;
                                    const fontStyle = 'bold';
                                    const fontFamily = 'Arial';
                                    ctx.font = fontStyle + ' ' + fontSize + 'px ' + fontFamily;
                                    
                                    const dataString = dataset.data[index].toFixed(4);
                                    ctx.textAlign = 'center';
                                    ctx.textBaseline = 'bottom';
                                    
                                    const padding = 5;
                                    const position = element.tooltipPosition();
                                    ctx.fillText(dataString, position.x, position.y - padding);
                                });
                            }
                        });
                    }
                }]
            });
        };
    </script>
</body>
</html>'''

with open('sustainable_energy/dashboard/templates/dashboard/objective3.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Objective 3 HTML file updated with hardcoded Accuracy values!")
print("Values used:")
print("  Logistic Regression: 0.9425")
print("  Decision Tree: 0.9562")
print("  KNN: 0.9671")
print("  XGBoost: 0.9781")
print("  LightGBM: 0.9767")
print("  CatBoost: 0.9808 (Best)")
print("  Random Forest: 0.9767")
