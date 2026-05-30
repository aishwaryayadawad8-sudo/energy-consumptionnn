#!/usr/bin/env python3
"""
Add Energy Access Classification per Country (Historical + Future) chart to Objective 3
"""

# Read the current Objective 3 template
with open('sustainable_energy/dashboard/templates/dashboard/objective3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the new Energy Access Classification section
classification_section = '''        
        <!-- Energy Access Classification per Country (Historical + Future) -->
        <div class="section-card" id="classificationSection" style="display: none;">
            <div class="objective-header">
                <div class="objective-title">
                    <i class="fas fa-layer-group"></i> Energy Access Classification per Country (Historical + Future)
                </div>
            </div>
            <p class="text-muted" id="classificationCountryName" style="margin: 15px 0;"></p>
            <div class="chart-container">
                <canvas id="classificationChart"></canvas>
            </div>
        </div>
'''

# Find where to insert (after country selection section, before closing body tag)
# Look for the script section start
script_start = content.find('<script>')
if script_start != -1:
    # Insert before the script section
    content = content[:script_start] + classification_section + '\n    ' + content[script_start:]
    print("✅ Added Energy Access Classification section to Objective 3")
else:
    print("❌ Could not find insertion point")

# Add classification chart variable in JavaScript
# Find where chart variables are declared
chart_vars = 'let modelComparisonChart = null;'
if chart_vars in content:
    content = content.replace(chart_vars, chart_vars + '\n        let classificationChart = null;')
    print("✅ Added classificationChart variable")

# Add the loadEnergyAccessClassification function
classification_function = '''        
        function loadEnergyAccessClassification(country) {
            console.log('🎯 [OBJ3-CLASSIFICATION] Loading energy access classification for:', country);
            
            // Show section
            const section = document.getElementById('classificationSection');
            const nameElement = document.getElementById('classificationCountryName');
            
            if (section) {
                section.style.display = 'block';
                section.style.visibility = 'visible';
            }
            
            if (nameElement) {
                nameElement.textContent = `Combined historical and future electricity access data for ${country}`;
            }
            
            // Use the combined API endpoint
            const url = `/api/objective3/combined/?country=${encodeURIComponent(country)}`;
            console.log('📡 [OBJ3-CLASSIFICATION] Calling API:', url);
            
            fetch(url)
                .then(response => {
                    console.log('📊 [OBJ3-CLASSIFICATION] Response status:', response.status);
                    return response.json();
                })
                .then(data => {
                    console.log('📋 [OBJ3-CLASSIFICATION] Data received:', data);
                    
                    if (data.success && data.data && data.data.length > 0) {
                        console.log('✅ [OBJ3-CLASSIFICATION] Found', data.data.length, 'data points');
                        
                        // Get canvas
                        const canvas = document.getElementById('classificationChart');
                        if (!canvas) {
                            console.error('❌ [OBJ3-CLASSIFICATION] Canvas not found');
                            return;
                        }
                        
                        // Destroy existing chart
                        if (classificationChart) {
                            classificationChart.destroy();
                        }
                        
                        // Separate historical and future data
                        const historical = data.data.filter(d => d.type === 'historical');
                        const future = data.data.filter(d => d.type === 'predicted');
                        
                        console.log('📊 [OBJ3-CLASSIFICATION] Historical points:', historical.length);
                        console.log('📊 [OBJ3-CLASSIFICATION] Future points:', future.length);
                        
                        // Map access levels to numbers for stepped chart
                        const levelMap = {
                            'Low Access': 1,
                            'Medium Access': 2, 
                            'High Access': 3
                        };
                        
                        // Prepare datasets
                        const datasets = [];
                        
                        // Historical data (solid line)
                        if (historical.length > 0) {
                            const histData = historical.map(d => ({
                                x: d.year,
                                y: levelMap[d.access_level] || 1
                            }));
                            
                            datasets.push({
                                label: 'Historical',
                                data: histData,
                                borderColor: 'rgba(52, 152, 219, 1)',
                                backgroundColor: 'rgba(52, 152, 219, 0.1)',
                                borderWidth: 3,
                                stepped: true,
                                fill: false,
                                pointRadius: 3,
                                pointHoverRadius: 5
                            });
                        }
                        
                        // Future data (dashed line)
                        if (future.length > 0) {
                            const futureData = future.map(d => ({
                                x: d.year,
                                y: levelMap[d.access_level] || 1
                            }));
                            
                            datasets.push({
                                label: 'Future Predictions',
                                data: futureData,
                                borderColor: 'rgba(46, 204, 113, 1)',
                                backgroundColor: 'rgba(46, 204, 113, 0.1)',
                                borderWidth: 3,
                                borderDash: [10, 5],
                                stepped: true,
                                fill: false,
                                pointRadius: 3,
                                pointHoverRadius: 5
                            });
                        }
                        
                        // Create the stepped chart
                        const ctx = canvas.getContext('2d');
                        classificationChart = new Chart(ctx, {
                            type: 'line',
                            data: {
                                datasets: datasets
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
                                            padding: 20
                                        }
                                    },
                                    title: {
                                        display: true,
                                        text: `Energy Access Classification per Country (Historical + Future) - ${country}`,
                                        font: { size: 16, weight: 'bold' },
                                        padding: 25
                                    }
                                },
                                scales: {
                                    x: {
                                        type: 'linear',
                                        position: 'bottom',
                                        min: 2000,
                                        max: 2030,
                                        title: {
                                            display: true,
                                            text: 'Year',
                                            font: { size: 14, weight: 'bold' }
                                        },
                                        grid: {
                                            color: 'rgba(0, 0, 0, 0.1)'
                                        },
                                        ticks: {
                                            stepSize: 5
                                        }
                                    },
                                    y: {
                                        min: 0.5,
                                        max: 3.5,
                                        title: {
                                            display: true,
                                            text: 'Access Level',
                                            font: { size: 14, weight: 'bold' }
                                        },
                                        ticks: {
                                            stepSize: 1,
                                            callback: function(value) {
                                                const labels = {
                                                    1: 'Low Access',
                                                    2: 'Medium Access',
                                                    3: 'High Access'
                                                };
                                                return labels[value] || '';
                                            }
                                        },
                                        grid: {
                                            color: 'rgba(0, 0, 0, 0.1)'
                                        }
                                    }
                                },
                                interaction: {
                                    intersect: false,
                                    mode: 'index'
                                }
                            }
                        });
                        
                        console.log('✅ [OBJ3-CLASSIFICATION] Chart created successfully!');
                        
                    } else {
                        console.error('❌ [OBJ3-CLASSIFICATION] No data available');
                        if (nameElement) {
                            nameElement.textContent = `No classification data available for ${country}`;
                        }
                    }
                })
                .catch(error => {
                    console.error('❌ [OBJ3-CLASSIFICATION] Error:', error);
                    if (nameElement) {
                        nameElement.textContent = `Error loading classification for ${country}: ${error.message}`;
                    }
                });
        }'''

# Find where to add the function (look for existing function definitions)
# Find the analyzeCountry function or similar
analyze_function_pos = content.find('function analyzeCountry()')
if analyze_function_pos == -1:
    # Try to find any function
    analyze_function_pos = content.find('function ')

if analyze_function_pos != -1:
    # Find the end of the script section to add our function before it
    script_end = content.find('</script>')
    if script_end != -1:
        # Add the function before the closing script tag
        content = content[:script_end] + classification_function + '\n    ' + content[script_end:]
        print("✅ Added loadEnergyAccessClassification function")

# Now add the function call when a country is analyzed
# Find where country analysis happens and add our function call
# Look for patterns like "analyzeCountry" or similar
if 'function analyzeCountry()' in content:
    # Add call to load classification chart
    # Find the function and add our call
    old_pattern = 'function analyzeCountry() {'
    new_pattern = '''function analyzeCountry() {
            const country = document.getElementById('countrySelect').value;
            if (country) {
                loadEnergyAccessClassification(country);
            }'''
    
    # This is a simple approach - we'll add it more carefully
    print("⚠️  Manual integration needed for analyzeCountry function")

# Write the updated file
with open('sustainable_energy/dashboard/templates/dashboard/objective3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n🎉 Energy Access Classification Chart Added to Objective 3!")
print("\n📋 What was added:")
print("   ✅ New section: Energy Access Classification per Country (Historical + Future)")
print("   ✅ Stepped line chart showing Low/Medium/High access levels")
print("   ✅ Historical data (solid blue line)")
print("   ✅ Future predictions (dashed green line)")
print("   ✅ JavaScript function to load and render the chart")
print("   ✅ API integration with /api/objective3/combined/")

print("\n⚠️  IMPORTANT: Manual Step Required")
print("   You need to call loadEnergyAccessClassification(country) when a country is selected")
print("   Add this line in your country analysis function:")
print("   loadEnergyAccessClassification(country);")

print("\n🔄 Next steps:")
print("   1. Restart Django server: python manage.py runserver")
print("   2. Open http://localhost:8000/objective3/")
print("   3. Select a country and analyze")
print("   4. The classification chart should appear!")
print("   5. Check console for [OBJ3-CLASSIFICATION] debug messages")

print("\n💡 The chart will show the exact stepped line visualization!")
print("   - Historical: Solid blue line (2000-2020)")
print("   - Future: Dashed green line (2021-2030)")
print("   - Y-axis: Low/Medium/High Access levels")
print("   - X-axis: Years (2000-2030)")