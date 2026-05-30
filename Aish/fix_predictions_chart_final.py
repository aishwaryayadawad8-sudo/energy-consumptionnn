#!/usr/bin/env python3
"""
Final fix for Objective 5 predictions chart
This will add comprehensive debugging and ensure the chart works
"""

# Read the current template
with open('sustainable_energy/dashboard/templates/dashboard/objective5_classification.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Enhanced loadPredictions function with better debugging
enhanced_load_predictions = '''        function loadPredictions(country) {
            console.log('🔍 [PREDICTIONS] Loading predictions for:', country);
            
            // Show loading state
            const section = document.getElementById('predictionsSection');
            const nameElement = document.getElementById('predictionsCountryName');
            
            if (!section) {
                console.error('❌ [PREDICTIONS] predictionsSection element not found!');
                return;
            }
            
            if (!nameElement) {
                console.error('❌ [PREDICTIONS] predictionsCountryName element not found!');
                return;
            }
            
            // Show section immediately
            section.style.display = 'block';
            nameElement.textContent = `Loading predictions for ${country}...`;
            
            const url = `/api/objective5/predictions/?country=${encodeURIComponent(country)}&years=10`;
            console.log('📡 [PREDICTIONS] Calling API:', url);
            
            fetch(url)
                .then(response => {
                    console.log('📊 [PREDICTIONS] API Response Status:', response.status);
                    if (!response.ok) {
                        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('📋 [PREDICTIONS] API Response Data:', data);
                    
                    if (data.success && data.predictions && data.predictions.length > 0) {
                        console.log('✅ [PREDICTIONS] Success! Found', data.predictions.length, 'predictions');
                        
                        // Update section title
                        nameElement.textContent = `Future predictions for ${country} (${data.predictions.length} points)`;
                        
                        // Get canvas element
                        const canvas = document.getElementById('predictionsChart');
                        if (!canvas) {
                            console.error('❌ [PREDICTIONS] Canvas element not found!');
                            return;
                        }
                        
                        const ctx = canvas.getContext('2d');
                        if (!ctx) {
                            console.error('❌ [PREDICTIONS] Could not get canvas context!');
                            return;
                        }
                        
                        // Destroy existing chart
                        if (predictionsChart) {
                            console.log('🗑️ [PREDICTIONS] Destroying previous chart');
                            predictionsChart.destroy();
                        }
                        
                        // Prepare data
                        const years = data.predictions.map(d => d.year);
                        const values = data.predictions.map(d => d.predicted_access);
                        
                        console.log('📊 [PREDICTIONS] Chart Data:');
                        console.log('   Years:', years);
                        console.log('   Values:', values.map(v => v.toFixed(1)));
                        
                        // Create chart
                        console.log('🎨 [PREDICTIONS] Creating chart...');
                        
                        try {
                            predictionsChart = new Chart(ctx, {
                                type: 'line',
                                data: {
                                    labels: years,
                                    datasets: [{
                                        label: `${country} - Predicted Access (%)`,
                                        data: values,
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
                            
                            console.log('✅ [PREDICTIONS] Chart created successfully!');
                            
                        } catch (chartError) {
                            console.error('❌ [PREDICTIONS] Chart creation failed:', chartError);
                            nameElement.textContent = `Error creating chart for ${country}: ${chartError.message}`;
                        }
                        
                    } else {
                        console.error('❌ [PREDICTIONS] API returned no data or failed');
                        console.log('   Success:', data.success);
                        console.log('   Predictions:', data.predictions ? data.predictions.length : 'undefined');
                        console.log('   Error:', data.error || 'None');
                        
                        nameElement.textContent = `No predictions available for ${country}`;
                    }
                })
                .catch(error => {
                    console.error('❌ [PREDICTIONS] Fetch error:', error);
                    nameElement.textContent = `Error loading predictions for ${country}: ${error.message}`;
                });
        }'''

# Find and replace the existing loadPredictions function
start_marker = "function loadPredictions(country) {"
end_marker = ".catch(error => console.error('Error loading predictions:', error));\n        }"

start_pos = content.find(start_marker)
if start_pos == -1:
    print("❌ Could not find loadPredictions function")
    exit(1)

end_pos = content.find(end_marker, start_pos)
if end_pos == -1:
    print("❌ Could not find end of loadPredictions function")
    exit(1)

end_pos += len(end_marker)

# Replace the function
new_content = content[:start_pos] + enhanced_load_predictions + content[end_pos:]

# Write back the file
with open('sustainable_energy/dashboard/templates/dashboard/objective5_classification.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Enhanced loadPredictions function with comprehensive debugging!")
print("\n📋 Improvements made:")
print("   ✓ Added detailed console logging with [PREDICTIONS] prefix")
print("   ✓ Added element existence checks")
print("   ✓ Added error handling for chart creation")
print("   ✓ Added loading states")
print("   ✓ Added data validation")
print("   ✓ Added try-catch for chart creation")
print("\n🔄 Next steps:")
print("   1. Restart Django server")
print("   2. Open http://localhost:8000/objective5/")
print("   3. Open browser console (F12)")
print("   4. Select a country and click 'Analyze Country'")
print("   5. Look for [PREDICTIONS] messages in console")
print("   6. The chart should now appear with detailed debugging info")
print("\n💡 If it still doesn't work, the console will show exactly what's wrong!")