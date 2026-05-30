"""
Final bulletproof fix - ensure historical data loads before predictions
"""

def final_fix():
    with open('sustainable_energy/dashboard/templates/dashboard/objective1.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Find the loadCountryData function and replace it completely with a version that uses Promise.all
    # First, find where the function starts
    function_start = "        function loadCountryData() {"
    function_end = "        }"
    
    # Find the start position
    start_pos = content.find(function_start)
    if start_pos == -1:
        print("❌ Could not find loadCountryData function")
        return False
    
    # Find the end of the function (look for the closing brace after the predictions fetch)
    # We need to find the right closing brace
    search_from = start_pos + len(function_start)
    
    # Look for the pattern that indicates end of loadCountryData
    end_pattern = "                .catch(error => console.error('Error loading predictions:', error));\n        }"
    end_pos = content.find(end_pattern, search_from)
    
    if end_pos == -1:
        # Try alternative pattern
        end_pattern = "                });\n        }"
        end_pos = content.find(end_pattern, search_from)
    
    if end_pos == -1:
        print("❌ Could not find end of loadCountryData function")
        return False
    
    end_pos += len(end_pattern)
    
    # New function that loads both together
    new_function = '''        function loadCountryData() {
            const country = document.getElementById('countrySelect').value;
            if (!country) {
                alert('Please select a country');
                return;
            }
            
            console.log('Loading data for:', country);
            
            // Load historical data first
            fetch(`/api/objective1/historical/?country=${encodeURIComponent(country)}`)
                .then(response => response.json())
                .then(historicalData => {
                    console.log('Historical API Response:', historicalData);
                    
                    if (historicalData.success && historicalData.data && historicalData.data.length > 0) {
                        // Display historical chart
                        document.getElementById('historicalSection').style.display = 'block';
                        document.getElementById('historicalCountryName').textContent = 
                            `Historical energy consumption for ${country}`;
                        
                        const ctx = document.getElementById('historicalChart').getContext('2d');
                        
                        if (historicalChart) {
                            historicalChart.destroy();
                        }
                        
                        const years = historicalData.data.map(d => d.Year);
                        const consumption = historicalData.data.map(d => d['Primary energy consumption per capita (kWh/person)']);
                        
                        console.log('Historical Years:', years);
                        console.log('Historical Consumption:', consumption);
                        
                        // Store for predictions chart
                        historicalDataStore = {
                            years: years,
                            consumption: consumption
                        };
                        
                        historicalChart = new Chart(ctx, {
                            type: 'line',
                            data: {
                                labels: years,
                                datasets: [{
                                    label: 'Energy Consumption (kWh/person)',
                                    data: consumption,
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
                        
                        // Now load predictions
                        return fetch(`/api/objective1/predictions/?country=${encodeURIComponent(country)}&years=10`);
                    } else {
                        throw new Error('No historical data available');
                    }
                })
                .then(response => response.json())
                .then(predictionsData => {
                    console.log('Predictions API Response:', predictionsData);
                    
                    if (predictionsData.success && predictionsData.predictions && predictionsData.predictions.length > 0) {
                        document.getElementById('predictionsSection').style.display = 'block';
                        document.getElementById('predictionsCountryName').textContent = 
                            `Historical & Predicted energy consumption for ${country}`;
                        
                        const ctx2 = document.getElementById('predictionsChart').getContext('2d');
                        
                        if (predictionsChart) {
                            predictionsChart.destroy();
                        }
                        
                        // Get stored historical data
                        const historicalYears = historicalDataStore.years;
                        const historicalData = historicalDataStore.consumption;
                        
                        // Get prediction data
                        const predictionYears = predictionsData.predictions.map(d => d.year);
                        const predictionData = predictionsData.predictions.map(d => d.predicted_consumption);
                        
                        console.log('Creating combined chart...');
                        console.log('Historical:', historicalYears.length, 'points');
                        console.log('Predictions:', predictionYears.length, 'points');
                        
                        // Combine years
                        const allYears = [...historicalYears, ...predictionYears];
                        
                        // Create combined chart
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
                        
                        console.log('✅ Combined chart created successfully!');
                    }
                })
                .catch(error => {
                    console.error('Error loading data:', error);
                    alert('Error loading data: ' + error.message);
                });
        }'''
    
    # Replace the function
    before = content[:start_pos]
    after = content[end_pos:]
    new_content = before + new_function + after
    
    with open('sustainable_energy/dashboard/templates/dashboard/objective1.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ Final bulletproof fix applied!")
    print("📊 Changes:")
    print("   - Completely rewrote loadCountryData function")
    print("   - Historical data loads first, then predictions")
    print("   - Proper promise chaining ensures correct order")
    print("   - Comprehensive console logging")
    print("   - Error handling with alerts")
    print("\n🔧 Now refresh your browser and try again!")
    return True

if __name__ == '__main__':
    final_fix()
