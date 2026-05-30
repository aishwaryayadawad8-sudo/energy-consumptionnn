#!/usr/bin/env python3
"""
Make Objective 1 Country Charts Load Instantly
This script adds instant loading with sample data while real data loads in background
"""

import os

def add_instant_chart_loading():
    """Add instant chart loading with sample data"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective1.html"
    
    if not os.path.exists(template_path):
        print(f"❌ {template_path} not found")
        return
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the loadCountryData function and replace it with an optimized version
    function_start = content.find('function loadCountryData() {')
    function_end = content.find('function', function_start + 1)
    
    if function_start == -1:
        print("❌ Could not find loadCountryData function")
        return
    
    # If there's no next function, find the end of the script
    if function_end == -1:
        function_end = content.find('</script>', function_start)
    
    # Create new optimized function
    new_function = '''function loadCountryData() {
            const country = document.getElementById('countrySelect').value;
            if (!country) {
                alert('Please select a country');
                return;
            }
            
            // Show sections immediately
            document.getElementById('historicalSection').style.display = 'block';
            document.getElementById('predictionsSection').style.display = 'block';
            
            // Update titles immediately
            document.getElementById('historicalCountryName').textContent = 
                `Historical energy consumption for ${country}`;
            document.getElementById('predictionsCountryName').textContent = 
                `Historical & Predicted energy consumption for ${country}`;
            
            // Show instant sample charts while loading real data
            showInstantSampleCharts(country);
            
            // Load real data in background
            loadRealCountryData(country);
        }
        
        function showInstantSampleCharts(country) {
            // Create instant historical chart with sample data
            const ctx1 = document.getElementById('historicalChart').getContext('2d');
            
            if (historicalChart) {
                historicalChart.destroy();
            }
            
            // Sample historical data (will be replaced with real data)
            const sampleYears = [2015, 2016, 2017, 2018, 2019, 2020];
            const sampleConsumption = [3500, 3600, 3750, 3800, 3900, 3850];
            
            historicalChart = new Chart(ctx1, {
                type: 'line',
                data: {
                    labels: sampleYears,
                    datasets: [{
                        label: 'Energy Consumption (kWh/person)',
                        data: sampleConsumption,
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
                        legend: { display: true },
                        title: {
                            display: true,
                            text: 'Loading real data...',
                            color: '#666'
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: { display: true, text: 'kWh per person' }
                        },
                        x: {
                            title: { display: true, text: 'Year' }
                        }
                    }
                }
            });
            
            // Create instant predictions chart
            const ctx2 = document.getElementById('predictionsChart').getContext('2d');
            
            if (predictionsChart) {
                predictionsChart.destroy();
            }
            
            // Sample combined data
            const allYears = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025];
            const historicalData = [3500, 3600, 3750, 3800, 3900, 3850, null, null, null, null, null];
            const predictionData = [null, null, null, null, null, null, 3900, 4000, 4100, 4200, 4300];
            
            predictionsChart = new Chart(ctx2, {
                type: 'line',
                data: {
                    labels: allYears,
                    datasets: [
                        {
                            label: 'Historical Consumption (kWh/person)',
                            data: historicalData,
                            borderColor: 'rgba(52, 152, 219, 1)',
                            backgroundColor: 'rgba(52, 152, 219, 0.1)',
                            borderWidth: 2,
                            fill: true,
                            tension: 0.4
                        },
                        {
                            label: 'Predicted Consumption (kWh/person)',
                            data: predictionData,
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
                        legend: { display: true },
                        title: {
                            display: true,
                            text: 'Loading real data...',
                            color: '#666'
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: { display: true, text: 'kWh per person' }
                        },
                        x: {
                            title: { display: true, text: 'Year' }
                        }
                    }
                }
            });
        }
        
        function loadRealCountryData(country) {
            // Load historical data
            fetch(`/api/objective1/historical/?country=${encodeURIComponent(country)}`)
                .then(response => response.json())
                .then(historicalData => {
                    if (historicalData.success && historicalData.data && historicalData.data.length > 0) {
                        // Update historical chart with real data
                        const years = historicalData.data.map(d => d.Year);
                        const consumption = historicalData.data.map(d => d['Primary energy consumption per capita (kWh/person)']);
                        
                        // Store for predictions chart
                        historicalDataStore = { years: years, consumption: consumption };
                        
                        // Update historical chart
                        if (historicalChart) {
                            historicalChart.data.labels = years;
                            historicalChart.data.datasets[0].data = consumption;
                            historicalChart.options.plugins.title.text = `Historical Data for ${country}`;
                            historicalChart.update();
                        }
                        
                        // Load predictions
                        return fetch(`/api/objective1/predictions/?country=${encodeURIComponent(country)}&years=10`);
                    } else {
                        throw new Error('No historical data available');
                    }
                })
                .then(response => response.json())
                .then(predictionsData => {
                    if (predictionsData.success && predictionsData.predictions && predictionsData.predictions.length > 0) {
                        // Update predictions chart with real data
                        const historicalYears = historicalDataStore.years;
                        const historicalData = historicalDataStore.consumption;
                        const predictionYears = predictionsData.predictions.map(d => d.year);
                        const predictionData = predictionsData.predictions.map(d => d.predicted_consumption);
                        
                        const allYears = [...historicalYears, ...predictionYears];
                        const historicalFull = [...historicalData, ...Array(predictionYears.length).fill(null)];
                        const predictionFull = [...Array(historicalYears.length).fill(null), ...predictionData];
                        
                        if (predictionsChart) {
                            predictionsChart.data.labels = allYears;
                            predictionsChart.data.datasets[0].data = historicalFull;
                            predictionsChart.data.datasets[1].data = predictionFull;
                            predictionsChart.options.plugins.title.text = `Real Data for ${country}`;
                            predictionsChart.update();
                        }
                    }
                })
                .catch(error => {
                    console.error('Error loading data:', error);
                    // Update chart titles to show error
                    if (historicalChart) {
                        historicalChart.options.plugins.title.text = 'Error loading data. Please try again.';
                        historicalChart.update();
                    }
                    if (predictionsChart) {
                        predictionsChart.options.plugins.title.text = 'Error loading data. Please try again.';
                        predictionsChart.update();
                    }
                });
        }
        
        '''
    
    # Replace the function
    new_content = content[:function_start] + new_function + content[function_end:]
    
    # Write back to file
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ Added instant chart loading with sample data")
    print("📊 Charts will appear immediately with sample data")
    print("🔄 Real data will load in background and update charts")

if __name__ == "__main__":
    print("🚀 Making Objective 1 Country Charts Load Instantly...")
    print("=" * 60)
    add_instant_chart_loading()
    print("=" * 60)
    print("✅ COMPLETE! Country analysis charts will now appear instantly!")
    print("🔄 Please refresh the Objective 1 page to test the instant loading.")