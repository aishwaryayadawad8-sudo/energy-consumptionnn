#!/usr/bin/env python3
"""Update Objective 4 to load model comparison first, then show country selection"""

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Objective 4: SDG 7 Monitoring - Model Comparison</title>
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
        
        .section-title {
            color: #2c3e50;
            font-weight: bold;
            margin-bottom: 20px;
            font-size: 1.5rem;
        }
        
        .chart-container {
            position: relative;
            height: 400px;
            margin-top: 20px;
        }
        
        .country-select {
            border-radius: 50px;
            padding: 12px 20px;
            border: 2px solid #e0e0e0;
        }
        
        .country-select:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
        }
        
        .btn-load {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 50px;
            font-weight: bold;
        }
        
        .btn-load:hover {
            opacity: 0.9;
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
            background: linear-gradient(135deg, #f39c12 0%, #f1c40f 100%);
            color: white;
            padding: 8px 15px;
            border-radius: 20px;
            font-weight: bold;
            display: inline-block;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <div class="header-section">
            <button class="back-btn" onclick="window.location.href='/'">
                <i class="fas fa-arrow-left"></i> Back to Objectives
            </button>
            <h1><i class="fas fa-chart-bar"></i> Objective 4: SDG 7 Monitoring</h1>
            <p class="text-muted">Compare 7 ML algorithms for electricity access prediction</p>
        </div>
        
        <!-- Model Comparison Section (Loads First) -->
        <div class="section-card">
            <h2 class="section-title"><i class="fas fa-trophy"></i> Model Comparison (7 Algorithms)</h2>
            <p class="text-muted">Lower MSE = Better Model Performance</p>
            <div id="modelComparisonLoading" class="loading">
                <div class="spinner-border text-primary" role="status"></div>
                <p>Training and comparing 7 ML models...</p>
            </div>
            <div id="bestModelInfo" style="display: none; margin-top: 15px;"></div>
            <div class="chart-container" style="display: none;" id="mseChartContainer">
                <canvas id="mseChart"></canvas>
            </div>
        </div>
        
        <!-- Country Selection (Shows After Model Comparison) -->
        <div class="section-card" id="countrySelectionSection" style="display: none;">
            <h2 class="section-title"><i class="fas fa-globe"></i> Select Country for Analysis</h2>
            <p class="text-muted">View historical data and future predictions for a specific country</p>
            <div class="row">
                <div class="col-md-8">
                    <select id="countrySelect" class="form-select country-select">
                        <option value="">Loading countries...</option>
                    </select>
                </div>
                <div class="col-md-4">
                    <button class="btn btn-load w-100" onclick="loadCountryData()">
                        <i class="fas fa-search"></i> Analyze Country
                    </button>
                </div>
            </div>
        </div>
        
        <!-- Historical Data Section -->
        <div class="section-card" id="historicalSection" style="display: none;">
            <h2 class="section-title"><i class="fas fa-history"></i> Historical Electricity Access</h2>
            <p class="text-muted" id="historicalCountryName"></p>
            <div class="chart-container">
                <canvas id="historicalChart"></canvas>
            </div>
        </div>
        
        <!-- Future Predictions Section -->
        <div class="section-card" id="predictionsSection" style="display: none;">
            <h2 class="section-title"><i class="fas fa-crystal-ball"></i> Future Predictions (Next 7 Years)</h2>
            <p class="text-muted" id="predictionsCountryName"></p>
            <div class="chart-container">
                <canvas id="predictionsChart"></canvas>
            </div>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        let mseChart = null;
        let historicalChart = null;
        let predictionsChart = null;
        
        // Load model comparison automatically on page load
        window.onload = function() {
            loadModelComparison();
        };
        
        function loadModelComparison() {
            document.getElementById('modelComparisonLoading').style.display = 'block';
            document.getElementById('mseChartContainer').style.display = 'none';
            
            fetch('/api/objective4/model-comparison/')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('modelComparisonLoading').style.display = 'none';
                    
                    if (data.success) {
                        // Show best model
                        document.getElementById('bestModelInfo').innerHTML = 
                            `<div class="best-model-badge"><i class="fas fa-star"></i> Best Model: ${data.best_model}</div>`;
                        document.getElementById('bestModelInfo').style.display = 'block';
                        
                        // Show chart container
                        document.getElementById('mseChartContainer').style.display = 'block';
                        
                        // Create chart
                        const ctx = document.getElementById('mseChart').getContext('2d');
                        
                        if (mseChart) {
                            mseChart.destroy();
                        }
                        
                        const models = Object.keys(data.mse_scores);
                        const mseValues = Object.values(data.mse_scores);
                        
                        // Find best model index for highlighting
                        const bestIndex = mseValues.indexOf(Math.min(...mseValues));
                        
                        // Create colors array - gold for best, blue for others
                        const colors = mseValues.map((val, idx) => 
                            idx === bestIndex ? 'rgba(255, 215, 0, 0.7)' : 'rgba(102, 126, 234, 0.7)'
                        );
                        
                        const borderColors = mseValues.map((val, idx) => 
                            idx === bestIndex ? 'rgba(255, 215, 0, 1)' : 'rgba(102, 126, 234, 1)'
                        );
                        
                        mseChart = new Chart(ctx, {
                            type: 'bar',
                            data: {
                                labels: models,
                                datasets: [{
                                    label: 'Mean Squared Error (MSE)',
                                    data: mseValues,
                                    backgroundColor: colors,
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
                                        text: 'Model Performance Comparison (Lower is Better)',
                                        font: {
                                            size: 16
                                        }
                                    }
                                },
                                scales: {
                                    y: {
                                        beginAtZero: true,
                                        title: {
                                            display: true,
                                            text: 'MSE Score'
                                        }
                                    }
                                }
                            }
                        });
                        
                        // After model comparison loads, show country selection and load countries
                        document.getElementById('countrySelectionSection').style.display = 'block';
                        loadCountries();
                    }
                })
                .catch(error => {
                    document.getElementById('modelComparisonLoading').style.display = 'none';
                    console.error('Error:', error);
                    alert('Error loading model comparison');
                });
        }
        
        function loadCountries() {
            fetch('/api/objective4/countries/')
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        const select = document.getElementById('countrySelect');
                        select.innerHTML = '<option value="">-- Select a Country --</option>';
                        data.countries.forEach(country => {
                            const option = document.createElement('option');
                            option.value = country;
                            option.textContent = country;
                            select.appendChild(option);
                        });
                    }
                })
                .catch(error => console.error('Error loading countries:', error));
        }
        
        function loadCountryData() {
            const country = document.getElementById('countrySelect').value;
            
            if (!country) {
                alert('Please select a country');
                return;
            }
            
            // Load historical data
            fetch(`/api/objective4/historical/?country=${encodeURIComponent(country)}`)
                .then(response => response.json())
                .then(data => {
                    if (data.success && data.data.length > 0) {
                        document.getElementById('historicalSection').style.display = 'block';
                        document.getElementById('historicalCountryName').textContent = 
                            `Electricity access trends for ${country}`;
                        
                        const ctx = document.getElementById('historicalChart').getContext('2d');
                        
                        if (historicalChart) {
                            historicalChart.destroy();
                        }
                        
                        const years = data.data.map(d => d.Year);
                        const access = data.data.map(d => d['Access to electricity (% of population)']);
                        
                        historicalChart = new Chart(ctx, {
                            type: 'line',
                            data: {
                                labels: years,
                                datasets: [{
                                    label: 'Electricity Access (%)',
                                    data: access,
                                    borderColor: 'rgba(102, 126, 234, 1)',
                                    backgroundColor: 'rgba(102, 126, 234, 0.1)',
                                    borderWidth: 3,
                                    fill: true,
                                    tension: 0.4
                                }]
                            },
                            options: {
                                responsive: true,
                                maintainAspectRatio: false,
                                plugins: {
                                    legend: {
                                        display: true
                                    }
                                },
                                scales: {
                                    y: {
                                        beginAtZero: true,
                                        max: 100,
                                        title: {
                                            display: true,
                                            text: 'Access (%)'
                                        }
                                    },
                                    x: {
                                        title: {
                                            display: true,
                                            text: 'Year'
                                        }
                                    }
                                }
                            }
                        });
                    }
                })
                .catch(error => console.error('Error loading historical data:', error));
            
            // Load predictions
            fetch(`/api/objective4/predictions/?country=${encodeURIComponent(country)}&years=7`)
                .then(response => response.json())
                .then(data => {
                    if (data.success && data.predictions.length > 0) {
                        document.getElementById('predictionsSection').style.display = 'block';
                        document.getElementById('predictionsCountryName').textContent = 
                            `Predicted electricity access for ${country}`;
                        
                        const ctx = document.getElementById('predictionsChart').getContext('2d');
                        
                        if (predictionsChart) {
                            predictionsChart.destroy();
                        }
                        
                        const years = data.predictions.map(d => d.year);
                        const predictions = data.predictions.map(d => d.predicted_access);
                        
                        predictionsChart = new Chart(ctx, {
                            type: 'line',
                            data: {
                                labels: years,
                                datasets: [{
                                    label: 'Predicted Access (%)',
                                    data: predictions,
                                    borderColor: 'rgba(39, 174, 96, 1)',
                                    backgroundColor: 'rgba(39, 174, 96, 0.1)',
                                    borderWidth: 3,
                                    fill: true,
                                    tension: 0.4,
                                    borderDash: [5, 5]
                                }]
                            },
                            options: {
                                responsive: true,
                                maintainAspectRatio: false,
                                plugins: {
                                    legend: {
                                        display: true
                                    }
                                },
                                scales: {
                                    y: {
                                        beginAtZero: true,
                                        max: 100,
                                        title: {
                                            display: true,
                                            text: 'Access (%)'
                                        }
                                    },
                                    x: {
                                        title: {
                                            display: true,
                                            text: 'Year'
                                        }
                                    }
                                }
                            }
                        });
                    }
                })
                .catch(error => console.error('Error loading predictions:', error));
        }
    </script>
</body>
</html>'''

# Write the file
output_path = 'sustainable_energy/dashboard/templates/dashboard/objective4.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"✅ Updated {output_path}")
print("\n📋 New Flow:")
print("   1. Page loads → Model comparison starts automatically")
print("   2. Model comparison completes → Country selection appears")
print("   3. User selects country → Historical + Predictions load")
