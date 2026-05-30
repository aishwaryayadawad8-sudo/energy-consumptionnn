html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Objective 2: Predict Carbon Emissions</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
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
            background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
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
        
        .loading {
            text-align: center;
            padding: 40px;
            color: #7f8c8d;
        }
        
        .spinner-border {
            width: 3rem;
            height: 3rem;
        }
        
        .best-model-badge {
            background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
            color: white;
            padding: 8px 15px;
            border-radius: 20px;
            font-weight: bold;
            display: inline-block;
            margin-top: 10px;
        }
        
        .co2-icon {
            color: #e74c3c;
        }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <div class="header-section">
            <button class="back-btn" onclick="window.location.href='/'">
                <i class="fas fa-arrow-left"></i> Back to Objectives
            </button>
            <h1><i class="fas fa-smog co2-icon"></i> Objective 2: Predict Carbon Emissions</h1>
            <p class="text-muted">Machine Learning Model Comparison for CO₂ Emissions Forecasting</p>
        </div>
        
        <!-- Model Comparison Section -->
        <div class="section-card">
            <div id="modelComparisonLoading" class="loading">
                <div class="spinner-border text-danger" role="status"></div>
                <p>Training models and comparing performance...</p>
            </div>
            <div id="bestModelInfo" style="display: none; margin-top: 15px;"></div>
            <div class="chart-container">
                <canvas id="mseChart"></canvas>
            </div>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        let mseChart = null;
        
        window.onload = function() {
            loadModelComparison();
        };
        
        function loadModelComparison() {
            document.getElementById('modelComparisonLoading').style.display = 'block';
            
            // Fetch from comprehensive comparison API
            fetch('/api/comprehensive-comparison/')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('modelComparisonLoading').style.display = 'none';
                    
                    if (data.success && data.results) {
                        // Find Sub-objective 2 data
                        const obj2 = data.results.find(obj => obj.sub_no === 2);
                        
                        if (obj2 && obj2.mse_scores) {
                            // Show best model
                            document.getElementById('bestModelInfo').innerHTML = 
                                `<div class="best-model-badge"><i class="fas fa-star"></i> Best Model: ${obj2.best_model}</div>`;
                            document.getElementById('bestModelInfo').style.display = 'block';
                            
                            const ctx = document.getElementById('mseChart').getContext('2d');
                            
                            if (mseChart) {
                                mseChart.destroy();
                            }
                            
                            const modelOrder = ['Linear Regression', 'Decision Tree', 'KNN', 'XGBoost', 'LightGBM', 'CatBoost', 'Random Forest'];
                            const models = [];
                            const mseValues = [];
                            const backgroundColors = [];
                            const borderColors = [];
                            
                            modelOrder.forEach(model => {
                                if (obj2.mse_scores[model] !== undefined) {
                                    models.push(model);
                                    mseValues.push(obj2.mse_scores[model]);
                                    
                                    if (model === 'XGBoost') {
                                        backgroundColors.push('rgba(255, 193, 7, 0.8)');
                                        borderColors.push('rgba(255, 193, 7, 1)');
                                    } else {
                                        backgroundColors.push('rgba(102, 126, 234, 0.7)');
                                        borderColors.push('rgba(102, 126, 234, 1)');
                                    }
                                }
                            });
                            
                            mseChart = new Chart(ctx, {
                                type: 'bar',
                                data: {
                                    labels: models,
                                    datasets: [{
                                        label: 'MSE',
                                        data: mseValues,
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
                                            text: 'Sub-objective 2: CO2 Emission Forecasting (MSE)',
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
                                                    return 'MSE: ' + context.parsed.y.toFixed(4);
                                                }
                                            }
                                        }
                                    },
                                    scales: {
                                        y: {
                                            beginAtZero: true,
                                            title: {
                                                display: true,
                                                text: 'MSE',
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
                        }
                    }
                })
                .catch(error => {
                    document.getElementById('modelComparisonLoading').style.display = 'none';
                    console.error('Error:', error);
                    alert('Error loading model comparison');
                });
        }
    </script>
</body>
</html>'''

with open('sustainable_energy/dashboard/templates/dashboard/objective2.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Objective 2 HTML file updated to use comprehensive comparison data!")
