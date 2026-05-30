"""
Fix predictions by loading both historical and predicted data together
"""

def fix_predictions():
    with open('sustainable_energy/dashboard/templates/dashboard/objective1.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Find the loadCountryData function and modify it to load both historical and predictions together
    old_function_start = '''        function loadCountryData() {
            const country = document.getElementById('countrySelect').value;
            if (!country) {
                alert('Please select a country');
                return;
            }
            
            // Load historical data
            fetch(`/api/objective1/historical/?country=${encodeURIComponent(country)}`)
                .then(response => response.json())
                .then(data => {
                    if (data.success && data.historical.length > 0) {
                        document.getElementById('historicalSection').style.display = 'block';
                        document.getElementById('historicalCountryName').textContent = 
                            `Historical energy consumption for ${country}`;
                        
                        const ctx = document.getElementById('historicalChart').getContext('2d');
                        
                        if (historicalChart) {
                            historicalChart.destroy();
                        }
                        
                        const years = data.historical.map(d => d.Year);
                        const consumption = data.historical.map(d => d['Primary energy consumption per capita (kWh/person)']);
                        
                        historicalChart = new Chart(ctx, {
                            type: 'line',
                            data: {
                                labels: years,
                                datasets: [{
                                    label: 'Energy Consumption (kWh/person)',
                                    data: consumption,
                                    borderColor: 'rgba(52, 152, 219, 1)',
                                    backgroundColor: 'rgba(52, 152, 219, 0.1)',
                                    borderWidth: 2,
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
                                        title: {
                                            display: true,
                                            text: 'kWh per person'
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
            
            // Load predictions and combine with historical data
            fetch(`/api/objective1/predictions/?country=${encodeURIComponent(country)}&years=10`)'''
    
    new_function_start = '''        function loadCountryData() {
            const country = document.getElementById('countrySelect').value;
            if (!country) {
                alert('Please select a country');
                return;
            }
            
            // Load both historical and predictions data
            Promise.all([
                fetch(`/api/objective1/historical/?country=${encodeURIComponent(country)}`).then(r => r.json()),
                fetch(`/api/objective1/predictions/?country=${encodeURIComponent(country)}&years=10`).then(r => r.json())
            ]).then(([historicalResponse, predictionsResponse]) => {
                // Display historical chart
                if (historicalResponse.success && historicalResponse.historical.length > 0) {
                    document.getElementById('historicalSection').style.display = 'block';
                    document.getElementById('historicalCountryName').textContent = 
                        `Historical energy consumption for ${country}`;
                    
                    const ctx = document.getElementById('historicalChart').getContext('2d');
                    
                    if (historicalChart) {
                        historicalChart.destroy();
                    }
                    
                    const years = historicalResponse.historical.map(d => d.Year);
                    const consumption = historicalResponse.historical.map(d => d['Primary energy consumption per capita (kWh/person)']);
                    
                    historicalChart = new Chart(ctx, {
                        type: 'line',
                        data: {
                            labels: years,
                            datasets: [{
                                label: 'Energy Consumption (kWh/person)',
                                data: consumption,
                                borderColor: 'rgba(52, 152, 219, 1)',
                                backgroundColor: 'rgba(52, 152, 219, 0.1)',
                                borderWidth: 2,
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
                                    title: {
                                        display: true,
                                        text: 'kWh per person'
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
                
                // Display combined historical + predictions chart
                if (predictionsResponse.success && predictionsResponse.predictions.length > 0) {
                    const historicalYears = historicalResponse.historical.map(d => d.Year);
                    const historicalData = historicalResponse.historical.map(d => d['Primary energy consumption per capita (kWh/person)']);
                    const predictionYears = predictionsResponse.predictions.map(d => d.year);
                    const predictionData = predictionsResponse.predictions.map(d => d.predicted_consumption);
                    
                    // Combine for display
                    const allYears = [...historicalYears, ...predictionYears];
                    
                    document.getElementById('predictionsSection').style.display = 'block';
                    document.getElementById('predictionsCountryName').textContent = 
                        `Historical & Predicted energy consumption for ${country}`;
                    
                    const ctx2 = document.getElementById('predictionsChart').getContext('2d');
                    
                    if (predictionsChart) {
                        predictionsChart.destroy();
                    }
                    
                    predictionsChart = new Chart(ctx2, {
                        type: 'line',
                        data: {
                            labels: allYears,
                            datasets: [
                                {
                                    label: 'Historical Consumption (kWh/person)',
                                    data: [...historicalData, ...Array(predictionYears.length).fill(null)],
                                    borderColor: 'rgba(52, 152, 219, 1)',
                                    backgroundColor: 'rgba(52, 152, 219, 0.1)',
                                    borderWidth: 2,
                                    fill: true,
                                    tension: 0.4
                                },
                                {
                                    label: 'Predicted Consumption (kWh/person)',
                                    data: [...Array(historicalYears.length).fill(null), ...predictionData],
                                    borderColor: 'rgba(39, 174, 96, 1)',
                                    backgroundColor: 'rgba(39, 174, 96, 0.1)',
                                    borderWidth: 3,
                                    fill: true,
                                    tension: 0.4,
                                    borderDash: [5, 5]
                                }
                            ]
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
                                    title: {
                                        display: true,
                                        text: 'kWh per person'
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
            }).catch(error => console.error('Error loading data:', error));
            
            // OLD CODE REMOVED - Now using Promise.all above
            /*fetch(`/api/objective1/predictions/?country=${encodeURIComponent(country)}&years=10`)'''
    
    if old_function_start in content:
        # Find the end of the old predictions fetch block
        start_pos = content.find(old_function_start)
        # Find the closing of the predictions fetch (look for the next function or closing brace)
        end_marker = '''                })
                .catch(error => console.error('Error loading predictions:', error));
        }'''
        
        end_pos = content.find(end_marker, start_pos)
        
        if end_pos != -1:
            # Replace everything from start to end
            before = content[:start_pos]
            after = content[end_pos + len(end_marker):]
            
            new_content = before + new_function_start + '''
        }'''  + after
            
            with open('sustainable_energy/dashboard/templates/dashboard/objective1.html', 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ Successfully fixed predictions!")
            print("📊 Changes:")
            print("   - Using Promise.all to load both historical and predictions together")
            print("   - No dependency on historicalChart being loaded first")
            print("   - Combined chart shows both historical and predicted data")
            print("   - Proper error handling")
            return True
    
    print("❌ Could not find the code to replace")
    return False

if __name__ == '__main__':
    fix_predictions()
