#!/usr/bin/env python3
"""
Fix Objective 5 Classification Template
This script fixes the API endpoints and adds the missing predictions chart
"""

# Read the current file
with open('sustainable_energy/dashboard/templates/dashboard/objective5_classification.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace API endpoints from objective4 to objective5
content = content.replace('/api/objective4/', '/api/objective5/')

# Add the predictions section after the historical section
predictions_section = '''        
        <!-- Future Predictions Section -->
        <div class="section-card" id="predictionsSection" style="display: none;">
            <h2 class="section-title"><i class="fas fa-crystal-ball"></i> Future Access Predictions</h2>
            <p class="text-muted" id="predictionsCountryName"></p>
            <div class="chart-container">
                <canvas id="predictionsChart"></canvas>
            </div>
        </div>
'''

# Find where to insert the predictions section (after historical section)
historical_section_end = content.find('</div>\n        \n        <!-- Combined Historical + Future Section -->')
if historical_section_end != -1:
    content = content[:historical_section_end] + '</div>' + predictions_section + '\n        \n        <!-- Combined Historical + Future Section -->' + content[historical_section_end + len('</div>\n        \n        <!-- Combined Historical + Future Section -->'):]

# Add predictions chart variable
content = content.replace('let policyChart = null;', 'let policyChart = null;\n        let predictionsChart = null;')

# Add loadPredictions function call in loadCountryData
load_country_data_old = '''function loadCountryData() {
            const country = document.getElementById('countrySelect').value;
            
            if (!country) {
                alert('Please select a country');
                return;
            }
            
            // Load historical data
            loadHistoricalData(country);
            
            // Load combined historical + future data
            loadCombinedData(country);
            
            // Load policy markers if applicable
            loadPolicyData(country);
        }'''

load_country_data_new = '''function loadCountryData() {
            const country = document.getElementById('countrySelect').value;
            
            if (!country) {
                alert('Please select a country');
                return;
            }
            
            // Load historical data
            loadHistoricalData(country);
            
            // Load predictions data
            loadPredictions(country);
            
            // Load combined historical + future data
            loadCombinedData(country);
            
            // Load policy markers if applicable
            loadPolicyData(country);
        }'''

content = content.replace(load_country_data_old, load_country_data_new)

# Add the loadPredictions function before loadCombinedData
load_predictions_function = '''        
        function loadPredictions(country) {
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
        }
        '''

# Insert the function before loadCombinedData
load_combined_pos = content.find('function loadCombinedData(country) {')
if load_combined_pos != -1:
    content = content[:load_combined_pos] + load_predictions_function + '\n        ' + content[load_combined_pos:]

# Write the updated content
with open('sustainable_energy/dashboard/templates/dashboard/objective5_classification.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Successfully fixed Objective 5 classification template!")
print("\n📋 Changes made:")
print("   ✓ Fixed API endpoints: /api/objective4/ → /api/objective5/")
print("   ✓ Added Future Predictions section")
print("   ✓ Added loadPredictions() function")
print("   ✓ Added predictions chart rendering")
print("   ✓ Added console logging for debugging")
print("\n🔄 Next steps:")
print("   1. Restart Django server: python manage.py runserver")
print("   2. Open http://localhost:8000/objective5/")
print("   3. Select a country (e.g., Belarus)")
print("   4. Click 'Analyze Country'")
print("   5. Check browser console (F12) for debug messages")
print("   6. Verify all charts appear including the predictions chart")