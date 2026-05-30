#!/usr/bin/env python3
"""
Fix Objective 5 Predictions Chart
This script fixes the predictions chart to show individual country data instead of all countries
"""

# Read the current objective5.html file
with open('sustainable_energy/dashboard/templates/dashboard/objective5.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the loadPredictions function
old_function = """        function loadPredictions(country) {
            // Load predictions for ALL countries
            fetch(`/api/objective4/countries/`)
                .then(response => response.json())
                .then(countriesData => {
                    if (countriesData.success) {
                        const countries = countriesData.countries;
                        const colors = generateColors(countries.length);
                        const datasets = [];
                        let completed = 0;
                        
                        countries.forEach((c, index) => {
                            fetch(`/api/objective4/predictions/?country=${encodeURIComponent(c)}&years=7`)
                                .then(response => response.json())
                                .then(data => {
                                    if (data.success && data.predictions.length > 0) {
                                        datasets.push({
                                            label: c,
                                            data: data.predictions.map(d => d.predicted_access),
                                            borderColor: colors[index],
                                            backgroundColor: colors[index] + '20',
                                            borderWidth: 2,
                                            fill: false,
                                            tension: 0.4,
                                            pointRadius: 0,
                                            pointHoverRadius: 4
                                        });
                                    }
                                    completed++;
                                    
                                    if (completed === countries.length) {
                                        document.getElementById('predictionsSection').style.display = 'block';
                                        document.getElementById('predictionsCountryName').textContent = `Forecasted Access to Electricity (% population) by Country (SDG7) 2024-2030`;
                                        const ctx = document.getElementById('predictionsChart').getContext('2d');
                                        if (predictionsChart) predictionsChart.destroy();
                                        predictionsChart = new Chart(ctx, {
                                            type: 'line',
                                            data: {
                                                labels: [2024, 2025, 2026, 2027, 2028, 2029, 2030],
                                                datasets: datasets
                                            },
                                            options: {
                                                responsive: true,
                                                maintainAspectRatio: false,
                                                plugins: { 
                                                    legend: { 
                                                        display: true,
                                                        position: 'right',
                                                        labels: {
                                                            font: { size: 11 },
                                                            padding: 8,
                                                            boxWidth: 15
                                                        }
                                                    },
                                                    title: {
                                                        display: true,
                                                        text: `Forecasted Access to Electricity (% population) by Country (SDG7) 2024-2030`,
                                                        font: { size: 14, weight: 'bold' },
                                                        padding: 15
                                                    }
                                                },
                                                scales: {
                                                    y: { 
                                                        min: 85,
                                                        max: 95, 
                                                        title: { 
                                                            display: true, 
                                                            text: 'Access to electricity (% of population)',
                                                            font: { size: 12 }
                                                        },
                                                        grid: { color: 'rgba(0, 0, 0, 0.1)' }
                                                    },
                                                    x: { 
                                                        title: { 
                                                            display: true, 
                                                            text: 'Year',
                                                            font: { size: 12 }
                                                        },
                                                        grid: { color: 'rgba(0, 0, 0, 0.1)' }
                                                    }
                                                },
                                                interaction: {
                                                    mode: 'nearest',
                                                    intersect: false
                                                }
                                            }
                                        });
                                    }
                                })
                                .catch(error => console.error(`Error loading predictions for ${c}:`, error));
                        });
                    }
                })
                .catch(error => console.error('Error loading countries:', error));
        }"""

new_function = """        function loadPredictions(country) {
            console.log('Loading predictions for:', country);
            fetch(`/api/objective5/predictions/?country=${encodeURIComponent(country)}&years=10`)
                .then(response => response.json())
                .then(data => {
                    console.log('Predictions data received:', data);
                    if (data.success && data.predictions.length > 0) {
                        document.getElementById('predictionsSection').style.display = 'block';
                        document.getElementById('predictionsCountryName').textContent = `Future predictions for ${country}`;
                        const ctx = document.getElementById('predictionsChart').getContext('2d');
                        if (predictionsChart) predictionsChart.destroy();
                        
                        console.log('Rendering predictions:', data.predictions); // DEBUG
                        
                        predictionsChart = new Chart(ctx, {
                            type: 'line',
                            data: {
                                labels: data.predictions.map(d => d.year),
                                datasets: [{
                                    label: `${country} - Predicted Access (%)`,
                                    data: data.predictions.map(d => d.predicted_access),
                                    borderColor: 'rgba(56, 239, 125, 1)',
                                    backgroundColor: 'rgba(56, 239, 125, 0.2)',
                                    borderWidth: 3,
                                    borderDash: [10, 5],
                                    fill: true,
                                    tension: 0.1,
                                    pointRadius: 4,
                                    pointHoverRadius: 6,
                                    pointBackgroundColor: 'rgba(56, 239, 125, 1)',
                                    pointBorderColor: '#fff',
                                    pointBorderWidth: 2
                                }]
                            },
                            options: {
                                responsive: true,
                                maintainAspectRatio: false,
                                plugins: {
                                    legend: { 
                                        display: true,
                                        position: 'top',
                                        labels: {
                                            font: { size: 14, weight: 'bold' },
                                            padding: 15
                                        }
                                    },
                                    title: {
                                        display: true,
                                        text: `Future Predictions - ${country}`,
                                        font: { size: 16, weight: 'bold' },
                                        padding: 20
                                    }
                                },
                                scales: {
                                    y: {
                                        beginAtZero: true,
                                        max: 100,
                                        title: { 
                                            display: true, 
                                            text: 'Access (%)',
                                            font: { size: 14, weight: 'bold' }
                                        },
                                        grid: { color: 'rgba(0, 0, 0, 0.1)' }
                                    },
                                    x: {
                                        title: { 
                                            display: true, 
                                            text: 'Year',
                                            font: { size: 14, weight: 'bold' }
                                        },
                                        grid: { color: 'rgba(0, 0, 0, 0.1)' }
                                    }
                                }
                            }
                        });
                    } else {
                        console.error('No predictions data available for', country);
                    }
                })
                .catch(error => console.error('Error loading predictions:', error));
        }"""

# Replace the function
if old_function in content:
    content = content.replace(old_function, new_function)
    print("✓ Replaced loadPredictions function")
else:
    print("✗ Could not find loadPredictions function to replace")
    print("  Searching for alternative patterns...")

# Write the updated content back
with open('sustainable_energy/dashboard/templates/dashboard/objective5.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ Objective 5 predictions chart has been fixed!")
print("\n📋 What was changed:")
print("   - Changed API endpoint from /api/objective4/ to /api/objective5/predictions/")
print("   - Now loads predictions for the selected country only")
print("   - Added proper data mapping: predictions.map(d => d.predicted_access)")
print("   - Added console logging for debugging")
print("   - Improved chart styling with dashed line for predictions")
print("\n🔄 Next steps:")
print("   1. Restart Django server: python manage.py runserver")
print("   2. Open http://localhost:8000/objective5/")
print("   3. Select a country (e.g., Belarus)")
print("   4. Click 'Analyze Country'")
print("   5. Check browser console (F12) for debug messages")
print("   6. Verify the predictions chart appears with data")
