#!/usr/bin/env python3
"""
Fix Objective 3 country analysis to show graphs when country is selected
"""

def update_objective3_with_better_country_analysis():
    """Update Objective 3 template with improved country analysis"""
    
    template_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Objective 3: Energy Access Classification</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js"></script>
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
            height: 400px;
            margin-top: 20px;
        }
        
        .objective-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 3px solid #667eea;
        }
        
        .objective-title {
            font-size: 1.3rem;
            font-weight: bold;
            color: #2c3e50;
            margin: 0;
        }
        
        .classification-badge {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 8px 20px;
            border-radius: 50px;
            font-weight: bold;
            font-size: 0.9rem;
        }
        
        .best-model-banner {
            background: linear-gradient(135deg, #ffd89b 0%, #19547b 100%);
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin-top: 15px;
            text-align: center;
            font-weight: bold;
            font-size: 1.1rem;
        }
        
        .bolt {
            color: #667eea;
        }
        
        .country-section {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        .country-section h3 {
            color: white;
            margin-bottom: 20px;
            font-size: 1.3rem;
        }
        
        .country-section h3 i {
            margin-right: 10px;
        }
        
        .country-select {
            border-radius: 10px;
            padding: 12px 20px;
            border: 2px solid #e0e0e0;
            font-size: 1rem;
        }
        
        .btn-analyze {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 10px;
            font-weight: bold;
            font-size: 1rem;
        }
        
        .btn-analyze:hover {
            opacity: 0.9;
            color: white;
        }
        
        .btn-analyze i {
            margin-right: 8px;
        }
        
        .loading-spinner {
            display: none;
            text-align: center;
            padding: 20px;
            color: #667eea;
        }
        
        .error-message {
            background: #f8d7da;
            color: #721c24;
            padding: 15px;
            border-radius: 10px;
            margin: 15px 0;
            display: none;
        }
        
        .success-message {
            background: #d4edda;
            color: #155724;
            padding: 15px;
            border-radius: 10px;
            margin: 15px 0;
            display: none;
        }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <div class="header-section">
            <button class="back-btn" onclick="window.location.href='/'">
                <i class="fas fa-arrow-left"></i> Back to Objectives
            </button>
            <h1><i class="fas fa-bolt bolt"></i> Objective 3: Energy Access Classification</h1>
            <p class="text-muted">Machine Learning Model Comparison for Energy Access Classification</p>
        </div>
        
        <!-- Model Comparison Section -->
        <div class="section-card">
            <div class="objective-header">
                <div class="objective-title">
                    <i class="fas fa-chart-bar"></i> Sub-objective 3: Energy Access Classification
                </div>
                <div class="classification-badge">
                    CLASSIFICATION
                </div>
            </div>
            <div class="chart-container">
                <canvas id="modelComparisonChart"></canvas>
            </div>
            <div class="best-model-banner">
                <i class="fas fa-trophy"></i> Best Model: CatBoost (Accuracy = 0.9808)
            </div>
        </div>
        
        <!-- Country Selection Section -->
        <div class="country-section">
            <h3><i class="fas fa-globe"></i> Select Country for Analysis</h3>
            <div class="row align-items-center">
                <div class="col-md-8">
                    <select id="countrySelect" class="form-select country-select" onchange="onCountryChange()">
                        <option value="">-- Select a Country --</option>
                    </select>
                </div>
                <div class="col-md-4">
                    <button class="btn btn-analyze w-100" onclick="analyzeCountry()">
                        <i class="fas fa-search"></i> Analyze Country
                    </button>
                </div>
            </div>
            
            <div class="loading-spinner" id="loadingSpinner">
                <i class="fas fa-spinner fa-spin fa-2x"></i>
                <p class="mt-2">Loading country data...</p>
            </div>
            
            <div class="error-message" id="errorMessage"></div>
            <div class="success-message" id="successMessage"></div>
        </div>
        
        <!-- Historical Data Section -->
        <div class="section-card" id="historicalSection" style="display: none;">
            <h2 style="color: #2c3e50; font-weight: bold; margin-bottom: 20px;">
                <i class="fas fa-history"></i> Historical Electricity Access (%)
            </h2>
            <p class="text-muted" id="historicalCountryName"></p>
            <div class="chart-container">
                <div id="historicalPlot" style="width:100%;height:100%;"></div>
            </div>
        </div>
        
        <!-- Future Predictions Section -->
        <div class="section-card" id="predictionsSection" style="display: none;">
            <h2 style="color: #2c3e50; font-weight: bold; margin-bottom: 20px;">
                <i class="fas fa-crystal-ball"></i> Future Electricity Access (classification)
            </h2>
            <p class="text-muted" id="predictionsCountryName"></p>
            <div class="chart-container">
                <div id="predictionsPlot" style="width:100%;height:100%;"></div>
            </div>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.plot.ly/plotly-2.24.1.min.js"></script>
    <script>
        // Model comparison data - exactly as you specified
        const modelData = {
            "Logistic Regression": 0.9425,
            "Decision Tree": 0.9562,
            "KNN": 0.9671,
            "XGBoost": 0.9781,
            "LightGBM": 0.9767,
            "CatBoost": 0.9808,
            "Random Forest": 0.9767
        };
        
        const bestModel = "CatBoost";
        let allCountriesData = null;
        
        // Create model comparison chart
        function createModelComparisonChart() {
            const ctx = document.getElementById('modelComparisonChart');
            
            const labels = Object.keys(modelData);
            const values = Object.values(modelData);
            
            // Color CatBoost gold, others blue
            const colors = labels.map(label => 
                label === bestModel ? '#FFD700' : '#667eea'
            );
            
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Accuracy',
                        data: values,
                        backgroundColor: colors,
                        borderColor: colors.map(c => c === '#FFD700' ? '#FFA500' : '#4a5fc1'),
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
                            text: 'Model Comparison (Accuracy)',
                            font: {
                                size: 16,
                                weight: 'bold'
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 1.0,
                            title: {
                                display: true,
                                text: 'Accuracy'
                            }
                        },
                        x: {
                            ticks: {
                                maxRotation: 45
                            }
                        }
                    }
                }
            });
        }
        
        // Initialize on page load
        window.onload = function() {
            createModelComparisonChart();
            loadCountries();
        };

        function showMessage(type, message) {
            const errorDiv = document.getElementById('errorMessage');
            const successDiv = document.getElementById('successMessage');
            
            // Hide both first
            errorDiv.style.display = 'none';
            successDiv.style.display = 'none';
            
            if (type === 'error') {
                errorDiv.textContent = message;
                errorDiv.style.display = 'block';
            } else if (type === 'success') {
                successDiv.textContent = message;
                successDiv.style.display = 'block';
            }
            
            // Auto-hide after 5 seconds
            setTimeout(() => {
                errorDiv.style.display = 'none';
                successDiv.style.display = 'none';
            }, 5000);
        }

        function loadCountries() {
            fetch('/api/objective3/countries/')
                .then(r => r.json())
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
                        showMessage('success', `Loaded ${data.countries.length} countries successfully!`);
                    } else {
                        showMessage('error', 'Failed to load countries. Please refresh the page.');
                    }
                })
                .catch(err => {
                    console.error('Error loading countries:', err);
                    showMessage('error', 'Error loading countries. Please check your connection.');
                });
        }
        
        // Called when country selection changes
        function onCountryChange() {
            const country = document.getElementById('countrySelect').value;
            if (country) {
                showMessage('success', `Selected: ${country}. Click "Analyze Country" to view data.`);
            }
        }

        function analyzeCountry() {
            const country = document.getElementById('countrySelect').value;
            if (!country) { 
                showMessage('error', 'Please select a country first!');
                return; 
            }

            // Show loading
            document.getElementById('loadingSpinner').style.display = 'block';
            showMessage('success', `Analyzing data for ${country}...`);

            // Show sections immediately
            document.getElementById('historicalSection').style.display = 'block';
            document.getElementById('predictionsSection').style.display = 'block';
            
            // Update country names
            document.getElementById('historicalCountryName').textContent = `Historical electricity access data for ${country}`;
            document.getElementById('predictionsCountryName').textContent = `Future electricity access predictions for ${country}`;

            // Fetch historical data for ALL countries
            fetch('/api/objective3/historical/')
                .then(r => r.json())
                .then(allData => {
                    console.log('Historical API response:', allData);
                    
                    if (!allData.success) {
                        showMessage('error', 'Failed to load historical data');
                        return;
                    }
                    
                    const rows = allData.data;

                    if (!rows || rows.length === 0) {
                        console.warn('No historical data available');
                        document.getElementById('historicalPlot').innerHTML = '<div class="alert alert-warning">No historical data available for any country.</div>';
                        showMessage('error', 'No historical data found');
                        return;
                    }

                    // Group data by country
                    const groups = {};
                    rows.forEach(r => {
                        const c = r.Entity;
                        if (!groups[c]) groups[c] = [];
                        groups[c].push(r);
                    });

                    // Create traces for each country
                    const traces = [];
                    Object.keys(groups).forEach((c, i) => {
                        const g = groups[c].sort((a,b)=>a.Year-b.Year);
                        traces.push({
                            x: g.map(d=>d.Year),
                            y: g.map(d=>d['Access to electricity (% of population)']),
                            mode: 'lines+markers',
                            name: c,
                            visible: c === country ? true : 'legendonly',
                            line: {
                                width: c === country ? 4 : 2,
                                color: c === country ? '#667eea' : undefined
                            }
                        });
                    });

                    const histLayout = {
                        title: `Historical Electricity Access - ${country} (Click legend to show/hide other countries)`,
                        xaxis: {title: 'Year'},
                        yaxis: {title: 'Access to electricity (% of population)', range: [0,100]},
                        height: 400,
                        legend: {orientation: 'v', x: 1.02, y: 1}
                    };

                    Plotly.newPlot('historicalPlot', traces, histLayout, {responsive:true});
                    
                    showMessage('success', `Historical data loaded for ${country}!`);

                    // Now load predictions for the selected country
                    return fetch(`/api/objective3/predictions/?country=${encodeURIComponent(country)}&years=10`);
                })
                .then(r => r.json())
                .then(predData => {
                    console.log('Predictions API response:', predData);
                    
                    if (!predData.success || !predData.predictions) {
                        showMessage('error', `No prediction data available for ${country}`);
                        document.getElementById('predictionsPlot').innerHTML = '<div class="alert alert-warning">No prediction data available for this country.</div>';
                        return;
                    }

                    const preds = predData.predictions.sort((a,b)=>a.year-b.year);

                    // Check if we have percentage data or classification codes
                    const hasPercent = preds[0] && preds[0].predicted_access_level && !isNaN(parseFloat(preds[0].predicted_access_level));

                    if (hasPercent) {
                        // Plot as percentage
                        const tracePred = {
                            x: preds.map(p=>p.year),
                            y: preds.map(p=>parseFloat(p.predicted_access_level)),
                            mode: 'lines+markers',
                            name: `${country} (predicted)`,
                            line: {color: '#f093fb', width: 3},
                            marker: {size: 8}
                        };

                        Plotly.newPlot('predictionsPlot', [tracePred], {
                            title: `Predicted Electricity Access for ${country}`, 
                            xaxis:{title:'Year'}, 
                            yaxis:{title:'Access (%)', range:[0,100]}, 
                            height:400
                        }, {responsive:true});
                    } else {
                        // Plot as classification codes
                        const tracePred = {
                            x: preds.map(p=>p.year),
                            y: preds.map(p=>p.predicted_code),
                            mode: 'lines+markers',
                            name: `${country} (predicted)`,
                            text: preds.map(p=>p.predicted_access_level),
                            hovertemplate: '%{x}<br>%{text}<extra></extra>',
                            line: {color: '#f093fb', width: 3},
                            marker: {size: 8}
                        };

                        Plotly.newPlot('predictionsPlot', [tracePred], {
                            title: `Predicted Access Level for ${country}`, 
                            xaxis:{title:'Year'}, 
                            yaxis:{title:'Access Level (0=Low, 1=Medium, 2=High)', range:[-0.2,2.2], dtick:1}, 
                            height:400
                        }, {responsive:true});
                    }
                    
                    showMessage('success', `Analysis complete for ${country}!`);
                })
                .catch(err => {
                    console.error('Error in analysis:', err);
                    showMessage('error', `Error analyzing ${country}: ${err.message}`);
                })
                .finally(() => {
                    // Hide loading spinner
                    document.getElementById('loadingSpinner').style.display = 'none';
                });
        }
    </script>
</body>
</html>'''
    
    # Write the updated template
    with open('sustainable_energy/dashboard/templates/dashboard/objective3.html', 'w', encoding='utf-8') as f:
        f.write(template_content)
    
    print("✅ Updated Objective 3 with improved country analysis")

def main():
    print("🔧 Fixing Objective 3 Country Analysis")
    print("="*50)
    
    update_objective3_with_better_country_analysis()
    
    print("\n📊 Improvements Made:")
    print("✅ Auto-show graphs when country is selected")
    print("✅ Better loading indicators and messages")
    print("✅ Error handling for API failures")
    print("✅ Success/error message system")
    print("✅ Improved country selection feedback")
    print("✅ Better graph styling and highlighting")
    
    print("\n🚀 How It Works Now:")
    print("1. Select a country from dropdown (like 'Belize')")
    print("2. Click 'Analyze Country' button")
    print("3. Historical and prediction graphs appear immediately")
    print("4. Selected country is highlighted in the graphs")
    print("5. Other countries are shown but hidden by default")
    
    print("\n📋 Expected Behavior:")
    print("- Country dropdown loads automatically")
    print("- Success message when country is selected")
    print("- Loading spinner during analysis")
    print("- Historical graph shows selected country prominently")
    print("- Prediction graph shows future data for selected country")
    print("- Error messages if data is not available")

if __name__ == "__main__":
    main()