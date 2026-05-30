#!/usr/bin/env python3
"""
Create a simple, guaranteed working version of Objective 5 chart
"""

def create_simple_objective5_chart():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective5_classification.html"
    
    print("🔧 Creating simple, guaranteed working Objective 5 chart...")
    
    # Create a minimal working template
    simple_template = '''<!DOCTYPE html>
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
            height: 450px;
            margin-top: 20px;
            width: 100%;
        }
        
        .section-title {
            color: #2c3e50;
            font-weight: bold;
            margin-bottom: 20px;
            font-size: 1.5rem;
        }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <div class="header-section">
            <button class="back-btn" onclick="window.location.href='/country-forecasts/?t=' + Date.now()">
                <i class="fas fa-arrow-left"></i> Back to Objectives
            </button>
            <h1><i class="fas fa-balance-scale"></i> Objective 5: Energy Equity Analysis</h1>
            <p class="text-muted">To evaluate disparities in energy access and consumption among developed, developing, and underdeveloped countries.</p>
        </div>
        
        <!-- Model Comparison Section -->
        <div class="section-card">
            <h2 class="section-title"><i class="fas fa-trophy"></i> Model Comparison</h2>
            <p class="text-muted">Instant model comparison with pre-computed results - loads automatically</p>
            <div class="chart-container">
                <canvas id="mseChart"></canvas>
            </div>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        let mseChart = null;
        
        // Exact results from your provided code for Objective 5
        const exactResults = {
            "Linear Regression": 0.1902,
            "Decision Tree": 0.0209,
            "KNN": 0.0105,
            "XGBoost": 0.0078,
            "LightGBM": 0.0066,
            "CatBoost": 0.0047,
            "Random Forest": 0.0062
        };
        
        const bestModel = "CatBoost"; // Lowest MSE for regression
        
        function createChart() {
            console.log('🚀 Creating chart with exact results...');
            
            const canvas = document.getElementById('mseChart');
            if (!canvas) {
                console.error('❌ Canvas not found!');
                return;
            }
            
            const ctx = canvas.getContext('2d');
            if (!ctx) {
                console.error('❌ Canvas context not found!');
                return;
            }
            
            const models = Object.keys(exactResults);
            const scores = Object.values(exactResults);
            
            // Create colors - gold for best model, blue for others
            const colors = models.map(model => 
                model === bestModel ? '#FFD700' : '#667eea'
            );
            
            console.log('📊 Models:', models);
            console.log('📊 Scores:', scores);
            console.log('🏆 Best model:', bestModel);
            
            try {
                mseChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: models,
                        datasets: [{
                            label: 'MSE Score',
                            data: scores,
                            backgroundColor: colors,
                            borderColor: colors,
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
                                text: 'Energy Equity Analysis - Model Comparison (MSE - Lower is Better)',
                                font: {
                                    size: 16,
                                    weight: 'bold'
                                }
                            },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        const value = context.parsed.y.toFixed(4);
                                        const isBest = context.label === bestModel;
                                        return `${context.label}: ${value}${isBest ? ' ⭐ (Best)' : ''}`;
                                    }
                                }
                            }
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                title: {
                                    display: true,
                                    text: 'MSE (Mean Squared Error)'
                                }
                            },
                            x: {
                                title: {
                                    display: true,
                                    text: 'Machine Learning Models'
                                }
                            }
                        }
                    },
                    plugins: [{
                        afterDatasetsDraw: function(chart) {
                            const ctx = chart.ctx;
                            chart.data.datasets.forEach(function(dataset, i) {
                                const meta = chart.getDatasetMeta(i);
                                meta.data.forEach(function(element, index) {
                                    ctx.fillStyle = 'black';
                                    ctx.font = 'bold 12px Arial';
                                    ctx.textAlign = 'center';
                                    ctx.textBaseline = 'bottom';
                                    
                                    const dataString = dataset.data[index].toFixed(4);
                                    const position = element.tooltipPosition();
                                    ctx.fillText(dataString, position.x, position.y - 5);
                                });
                            });
                        }
                    }]
                });
                
                console.log('✅ Chart created successfully!');
                
            } catch (error) {
                console.error('❌ Chart creation error:', error);
                alert('Chart creation failed: ' + error.message);
            }
        }
        
        // Load chart immediately when page loads
        window.addEventListener('load', function() {
            console.log('🌟 Page loaded, creating chart...');
            setTimeout(createChart, 100); // Small delay to ensure everything is ready
        });
        
        // Fallback - try again after 1 second if first attempt fails
        setTimeout(function() {
            if (!mseChart) {
                console.log('🔄 Fallback: Trying to create chart again...');
                createChart();
            }
        }, 1000);
    </script>
</body>
</html>'''
    
    try:
        # Write the simple template
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(simple_template)
        
        print("✅ Simple, guaranteed working Objective 5 template created!")
        print("📝 Features:")
        print("   - Hardcoded exact results from your code")
        print("   - CatBoost highlighted in gold (best model)")
        print("   - All 7 models with exact MSE values")
        print("   - Instant loading with fallback retry")
        print("   - Comprehensive error handling")
        print("🔄 Please refresh your browser to see the chart")
        
    except Exception as e:
        print(f"❌ Error creating simple template: {e}")

if __name__ == "__main__":
    create_simple_objective5_chart()