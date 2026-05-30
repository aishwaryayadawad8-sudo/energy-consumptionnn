#!/usr/bin/env python3
"""
Add historical percentage chart to Objective 3
Shows electricity access as percentages (0-100%) like in the screenshot
"""

def create_objective3_with_both_charts():
    """Create Objective 3 with both historical percentage chart and combined chart"""
    
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
        
        <!-- Historical Percentage Chart Section -->
        <div class="section-card" id="historicalPercentageSection" style="display: none;">
            <h2 style="color: #2c3e50; font-weight: bold; margin-bottom: 20px;">
                <i class="fas fa-history"></i> Historical Electricity Access per Country (Click Country to View)
            </h2>
            <p class="text-muted" id="historicalPercentageCountryName"></p>
            <div class="chart-container">
                <div id="historicalPercentagePlot" style="width:100%;height:100%;"></div>
            </div>
        </div>
        
        <!-- Combined Historical + Future Chart Section -->
        <div class="section-card" id="combinedSection" style="display: none;">
            <h2 style="color: #2c3e50; font-weight: bold; margin-bottom: 20px;">
                <i class="fas fa-chart-line"></i> Energy Access Classification per Country (Historical + Future)
            </h2>
            <p class="text-muted" id="combinedCountryName"></p>
            <div class="chart-container">
                <div id="combinedPlot" style="width:100%;height:100%;"></div>
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

        // Convert percentage to access level category
        function getAccessLevel(percentage) {
            if (percentage < 33) return 0; // Low Access
            if (percentage < 67) return 1; // Medium Access
            return 2; // High Access
        }
        
        function getAccessLevelName(level) {
            const names = ['Low Access', 'Medium Access', 'High Access'];
            return names[level] || 'Unknown';
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

            // Show both sections
            document.getElementById('historicalPercentageSection').style.display = 'block';
            document.getElementById('combinedSection').style.display = 'block';
            
            // Update country names
            document.getElementById('historicalPercentageCountryName').textContent = `Historical electricity access percentages for all countries (${country} highlighted)`;
            document.getElementById('combinedCountryName').textContent = `Combined historical and future electricity access data for ${country}`;

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
                        document.getElementById('historicalPercentagePlot').innerHTML = '<div class="alert alert-warning">No historical data available.</div>';
                        document.getElementById('combinedPlot').innerHTML = '<div class="alert alert-warning">No historical data available.</div>';
                        showMessage('error', 'No historical data found');
                        return;
                    }

                    // Group historical data by country
                    const historicalGroups = {};
                    rows.forEach(r => {
                        const c = r.Entity;
                        if (!historicalGroups[c]) historicalGroups[c] = [];
                        historicalGroups[c].push({
                            year: r.Year,
                            percentage: r['Access to electricity (% of population)'],
                            accessLevel: getAccessLevel(r['Access to electricity (% of population)'])
                        });
                    });

                    // Create Historical Percentage Chart (like your screenshot)
                    const percentageTraces = [];
                    Object.keys(historicalGroups).forEach((c, i) => {
                        const g = historicalGroups[c].sort((a,b)=>a.year-b.year);
                        percentageTraces.push({
                            x: g.map(d => d.year),
                            y: g.map(d => d.percentage),
                            mode: 'lines+markers',
                            name: c,
                            visible: c === country ? true : 'legendonly',
                            line: {
                                width: c === country ? 4 : 2,
                                color: c === country ? '#667eea' : undefined
                            },
                            marker: {
                                size: c === country ? 8 : 6
                            }
                        });
                    });

                    const percentageLayout = {
                        title: 'Historical Electricity Access per Country (Click Country to View)',
                        xaxis: {title: 'Year'},
                        yaxis: {title: 'Access to electricity (% of population)', range: [0, 100]},
                        height: 400,
                        legend: {
                            orientation: 'v',
                            x: 1.02,
                            y: 1,
                            title: {text: 'Entity'}
                        },
                        hovermode: 'closest'
                    };

                    Plotly.newPlot('historicalPercentagePlot', percentageTraces, percentageLayout, {responsive: true});

                    // Now fetch predictions for the selected country
                    return fetch(`/api/objective3/predictions/?country=${encodeURIComponent(country)}&years=10`);
                })
                .then(r => r.json())
                .then(predData => {
                    console.log('Predictions API response:', predData);
                    
                    let predictions = [];
                    if (predData.success && predData.predictions) {
                        predictions = predData.predictions.map(p => ({
                            year: p.year,
                            accessLevel: p.predicted_code,
                            accessLevelName: p.predicted_access_level
                        }));
                    }

                    // Create Combined Historical + Future Chart (access levels)
                    const combinedTraces = [];
                    
                    // Add historical traces for all countries (access levels)
                    Object.keys(historicalGroups).forEach((c, i) => {
                        const g = historicalGroups[c].sort((a,b)=>a.year-b.year);
                        
                        combinedTraces.push({
                            x: g.map(d => d.year),
                            y: g.map(d => d.accessLevel),
                            mode: 'lines+markers',
                            name: c,
                            visible: c === country ? true : 'legendonly',
                            line: {
                                width: c === country ? 4 : 2,
                                color: c === country ? '#667eea' : undefined
                            },
                            marker: {
                                size: c === country ? 8 : 6
                            },
                            hovertemplate: '%{x}<br>' + c + '<br>%{text}<extra></extra>',
                            text: g.map(d => getAccessLevelName(d.accessLevel) + ` (${d.percentage.toFixed(1)}%)`)
                        });
                    });
                    
                    // Add prediction trace for selected country
                    if (predictions.length > 0) {
                        combinedTraces.push({
                            x: predictions.map(p => p.year),
                            y: predictions.map(p => p.accessLevel),
                            mode: 'lines+markers',
                            name: `${country} (Predicted)`,
                            line: {
                                color: '#f093fb',
                                width: 4,
                                dash: 'dash'
                            },
                            marker: {
                                size: 10,
                                symbol: 'diamond'
                            },
                            hovertemplate: '%{x}<br>' + country + ' (Predicted)<br>%{text}<extra></extra>',
                            text: predictions.map(p => p.accessLevelName || getAccessLevelName(p.accessLevel))
                        });
                    }

                    const combinedLayout = {
                        title: 'Energy Access Classification per Country (Historical + Future)',
                        xaxis: {
                            title: 'Year',
                            range: [2000, Math.max(2030, Math.max(...predictions.map(p => p.year), 2025))]
                        },
                        yaxis: {
                            title: 'Access Level',
                            range: [-0.2, 2.2],
                            tickvals: [0, 1, 2],
                            ticktext: ['Low Access', 'Medium Access', 'High Access']
                        },
                        height: 400,
                        legend: {
                            orientation: 'v',
                            x: 1.02,
                            y: 1,
                            title: {
                                text: 'Click to show/hide countries'
                            }
                        },
                        hovermode: 'closest',
                        annotations: predictions.length > 0 ? [{
                            x: Math.min(...predictions.map(p => p.year)),
                            y: 2.1,
                            text: 'Future Predictions →',
                            showarrow: false,
                            font: {
                                color: '#f093fb',
                                size: 12
                            }
                        }] : []
                    };

                    Plotly.newPlot('combinedPlot', combinedTraces, combinedLayout, {responsive: true});
                    
                    showMessage('success', `Analysis complete for ${country}! Both charts are now available.`);
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
    
    print("✅ Added both historical percentage chart and combined chart to Objective 3")

def main():
    print("🔧 Adding Historical Percentage Chart to Objective 3")
    print("="*50)
    
    create_objective3_with_both_charts()
    
    print("\n📊 Now Objective 3 Has Both Charts:")
    
    print("\n1️⃣ Historical Electricity Access per Country:")
    print("   ✅ Shows percentages (0-100%) like your screenshot")
    print("   ✅ Y-axis: Access to electricity (% of population)")
    print("   ✅ X-axis: Year (2000-2020)")
    print("   ✅ All countries in legend on right side")
    print("   ✅ Selected country highlighted prominently")
    print("   ✅ Click legend to show/hide countries")
    
    print("\n2️⃣ Energy Access Classification (Historical + Future):")
    print("   ✅ Shows access levels (Low/Medium/High)")
    print("   ✅ Y-axis: Access Level categories")
    print("   ✅ X-axis: Year (2000-2030+)")
    print("   ✅ Historical data as solid lines")
    print("   ✅ Future predictions as dashed lines")
    print("   ✅ Combined timeline view")
    
    print("\n🎯 Chart Features:")
    print("✅ Model comparison chart at top (CatBoost highlighted)")
    print("✅ Country selection dropdown")
    print("✅ Historical percentage chart (matches your screenshot)")
    print("✅ Combined historical + future chart")
    print("✅ Interactive legends on both charts")
    print("✅ Loading indicators and error handling")
    
    print("\n🚀 To Test:")
    print("1. Start Django server: python manage.py runserver")
    print("2. Visit: http://127.0.0.1:8000/objective3/")
    print("3. Select a country (like 'Belize')")
    print("4. Click 'Analyze Country'")
    print("5. See both charts appear")

if __name__ == "__main__":
    main()