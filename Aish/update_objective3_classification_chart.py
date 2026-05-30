#!/usr/bin/env python3
"""
Update Objective 3 to use Chart.js for the Energy Access Classification chart
"""

# Read the current Objective 3 template
with open('sustainable_energy/dashboard/templates/dashboard/objective3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the existing Plotly-based combined section with Chart.js version
old_combined_section = '''        <!-- Combined Historical + Future Chart Section -->
        <div class="section-card" id="combinedSection" style="display: none;">
            <h2 style="color: #2c3e50; font-weight: bold; margin-bottom: 20px;">
                <i class="fas fa-chart-line"></i> Energy Access Classification per Country (Historical + Future)
            </h2>
            <p class="text-muted" id="combinedCountryName"></p>
            <div class="chart-container">
                <div id="combinedPlot" style="width:100%;height:100%;"></div>
            </div>
        </div>'''

new_combined_section = '''        <!-- Energy Access Classification per Country (Historical + Future) -->
        <div class="section-card" id="combinedSection" style="display: none;">
            <h2 style="color: #2c3e50; font-weight: bold; margin-bottom: 20px;">
                <i class="fas fa-chart-line"></i> Energy Access Classification per Country (Historical + Future)
            </h2>
            <p class="text-muted" id="combinedCountryName"></p>
            <div class="chart-container">
                <canvas id="combinedChart"></canvas>
            </div>
        </div>'''

if old_combined_section in content:
    content = content.replace(old_combined_section, new_combined_section)
    print("✅ Updated combined section to use Chart.js")

# Add Chart.js variable for the combined chart
if 'let modelComparisonChart = null;' in content:
    content = content.replace('let modelComparisonChart = null;', 'let modelComparisonChart = null;\n        let combinedChart = null;')
    print("✅ Added combinedChart variable")

# Find the analyzeCountry function and add our chart loading
# Look for the function definition
analyze_function_start = content.find('function analyzeCountry()')
if analyze_function_start != -1:
    # Find the end of the function
    brace_count = 0
    pos = analyze_function_start
    while pos < len(content):
        if content[pos] == '{':
            brace_count += 1
        elif content[pos] == '}':
            brace_count -= 1
            if brace_count == 0:
                # Found the end of the function
                function_end = pos
                break
        pos += 1
    
    # Add our function call before the closing brace
    if 'loadEnergyAccessClassification' not in content[analyze_function_start:function_end]:
        # Add the call
        insert_pos = function_end - 20  # Go back a bit to find a good insertion point
        while insert_pos > analyze_function_start and content[insert_pos] != '\n':
            insert_pos -= 1
        
        new_call = '''
                // Load Energy Access Classification Chart
                loadEnergyAccessClassification(country);'''
        
        content = content[:insert_pos] + new_call + content[insert_pos:]
        print("✅ Added loadEnergyAccessClassification call to analyzeCountry function")

# Add the loadEnergyAccessClassification function
classification_function = '''
        function loadEnergyAccessClassification(country) {
            console.log('🎯 [OBJ3-CLASSIFICATION] Loading energy access classification for:', country);
            
            // Show section
            const section = document.getElementById('combinedSection');
            const nameElement = document.getElementById('combinedCountryName');
            
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
                        const canvas = document.getElementById('combinedChart');
                        if (!canvas) {
                            console.error('❌ [OBJ3-CLASSIFICATION] Canvas not found');
                            return;
                        }
                        
                        // Destroy existing chart
                        if (combinedChart) {
                            combinedChart.destroy();
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
                                pointRadius: 4,
                                pointHoverRadius: 6
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
                                pointRadius: 4,
                                pointHoverRadius: 6
                            });
                        }
                        
                        // Create the stepped chart
                        const ctx = canvas.getContext('2d');
                        combinedChart = new Chart(ctx, {
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

# Add the function before the closing script tag
script_end = content.rfind('</script>')
if script_end != -1:
    content = content[:script_end] + classification_function + '\n    ' + content[script_end:]
    print("✅ Added loadEnergyAccessClassification function")

# Remove the duplicate classification section that was added earlier
duplicate_section = '''        <!-- Energy Access Classification per Country (Historical + Future) -->
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
        </div>'''

if duplicate_section in content:
    content = content.replace(duplicate_section, '')
    print("✅ Removed duplicate classification section")

# Write the updated file
with open('sustainable_energy/dashboard/templates/dashboard/objective3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n🎉 Objective 3 Updated with Chart.js Classification Chart!")
print("\n📋 What was updated:")
print("   ✅ Replaced Plotly.js chart with Chart.js stepped line chart")
print("   ✅ Added loadEnergyAccessClassification function")
print("   ✅ Integrated with existing analyzeCountry function")
print("   ✅ Uses /api/objective3/combined/ endpoint")
print("   ✅ Shows historical (solid blue) and future (dashed green) lines")

print("\n🔄 Next steps:")
print("   1. Restart Django server: python manage.py runserver")
print("   2. Open http://localhost:8000/objective3/")
print("   3. Select a country and click 'Analyze Country'")
print("   4. The stepped line chart should appear!")
print("   5. Check console for [OBJ3-CLASSIFICATION] debug messages")

print("\n💡 The chart will show exactly like your image:")
print("   - Stepped line visualization")
print("   - Historical: Solid blue line (2000-2020)")
print("   - Future: Dashed green line (2021-2030)")
print("   - Y-axis: Low/Medium/High Access levels")
print("   - X-axis: Years (2000-2030)")