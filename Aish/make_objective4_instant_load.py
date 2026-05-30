#!/usr/bin/env python3

"""
Fix Objective 4 to load model comparison instantly without delays
"""

import os

def fix_objective4_instant_load():
    """Fix Objective 4 template to load model comparison instantly"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective4.html"
    
    # Read current template
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create the new JavaScript section with instant loading
    new_js_section = '''    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        let mseChart = null;
        let historicalChart = null;
        let predictionsChart = null;
        
        // Load model comparison automatically on page load
        window.onload = function() {
            console.log('🚀 [OBJ4] Page loaded, loading model comparison instantly...');
            loadModelComparison();
        };
        
        function loadModelComparison() {
            console.log('🚀 [OBJ4] Loading model comparison instantly...');
            
            // Hide loading spinner immediately
            document.getElementById('modelComparisonLoading').style.display = 'none';
            
            // Hardcoded data from Sub-objective 4: SDG 7 Monitoring (regression)
            const modelData = {
                "Linear Regression": 0.2276,
                "Decision Tree": 0.0251,
                "KNN": 0.0662,
                "XGBoost": 0.0142,
                "LightGBM": 0.0160,
                "CatBoost": 0.0096,      // Best model (lowest MSE)
                "Random Forest": 0.0120
            };
            
            const bestModel = "CatBoost";
            const bestMSE = 0.0096;
            
            console.log('📊 [OBJ4] Using hardcoded model data for instant loading');
            
            // Show best model info immediately
            document.getElementById('bestModelInfo').innerHTML = 
                `<div class="best-model-badge"><i class="fas fa-star"></i> Best Model: ${bestModel} (MSE = ${bestMSE})</div>`;
            document.getElementById('bestModelInfo').style.display = 'block';
            
            // Show chart container immediately
            document.getElementById('mseChartContainer').style.display = 'block';
            
            // Create chart instantly
            const ctx = document.getElementById('mseChart').getContext('2d');
            
            if (mseChart) {
                mseChart.destroy();
            }
            
            const models = Object.keys(modelData);
            const mseValues = Object.values(modelData);
            
            // Find best model index for gold highlighting
            const bestIndex = mseValues.indexOf(Math.min(...mseValues));
            
            // Create colors array - gold for best, blue for others
            const colors = mseValues.map((val, idx) => 
                idx === bestIndex ? 'rgba(255, 215, 0, 0.8)' : 'rgba(102, 126, 234, 0.7)'
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
                            text: 'Sub-objective 4: SDG 7 Monitoring - Model Comparison (Lower MSE is Better)',
                            font: {
                                size: 16,
                                weight: 'bold'
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
            
            console.log('✅ [OBJ4] Model comparison chart created instantly!');
            
            // Auto-show country selection after chart is created
            setTimeout(() => {
                document.getElementById('countrySelectionSection').style.display = 'block';
                loadCountries();
            }, 500);
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
                                    tension: 0,
                                    pointRadius: 5,
                                    pointHoverRadius: 7
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
                                    tension: 0,
                                    pointRadius: 5,
                                    pointHoverRadius: 7,
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
    </script>'''
    
    # Find the script section and replace it
    script_start = content.find('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>')
    script_end = content.find('</body>')
    
    if script_start != -1 and script_end != -1:
        # Replace the entire script section
        new_content = content[:script_start] + new_js_section + '\n</body>\n</html>'
        
        # Write the fixed template
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✅ Fixed Objective 4 template for instant model comparison loading!")
        print("🚀 Model comparison will now load instantly with hardcoded data")
        print("📊 No more waiting for API calls - chart appears immediately!")
        
    else:
        print("❌ Could not find script section to replace")

if __name__ == "__main__":
    fix_objective4_instant_load()