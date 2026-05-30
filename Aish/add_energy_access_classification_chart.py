#!/usr/bin/env python3
"""
Add the Energy Access Classification per Country (Historical + Future) chart
This creates the stepped line chart showing Low/Medium/High access levels
"""

# Read the current template
with open('sustainable_energy/dashboard/templates/dashboard/objective5_classification.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the new Energy Access Classification section
classification_section = '''        
        <!-- Energy Access Classification Section -->
        <div class="section-card" id="classificationSection" style="display: none;">
            <h2 class="section-title"><i class="fas fa-layer-group"></i> Energy Access Classification per Country (Historical + Future)</h2>
            <p class="text-muted" id="classificationCountryName"></p>
            <div class="chart-container">
                <canvas id="classificationChart"></canvas>
            </div>
        </div>
'''

# Find where to insert the new section (after predictions section)
predictions_section_end = content.find('</div>\n        \n        <!-- Combined Historical + Future Section -->')
if predictions_section_end != -1:
    content = content[:predictions_section_end] + '</div>' + classification_section + '\n        \n        <!-- Combined Historical + Future Section -->' + content[predictions_section_end + len('</div>\n        \n        <!-- Combined Historical + Future Section -->'):]
    print("✅ Added Energy Access Classification section")
else:
    # Alternative insertion point
    combined_section_start = content.find('<!-- Combined Historical + Future Section -->')
    if combined_section_start != -1:
        content = content[:combined_section_start] + classification_section + '\n        ' + content[combined_section_start:]
        print("✅ Added Energy Access Classification section (alternative position)")

# Add classification chart variable
content = content.replace('let predictionsChart = null;', 'let predictionsChart = null;\n        let classificationChart = null;')

# Add loadClassification function call in loadCountryData
load_country_data_old = '''            // Load predictions data
            loadPredictions(country);
            
            // Load combined historical + future data
            loadCombinedData(country);'''

load_country_data_new = '''            // Load predictions data
            loadPredictions(country);
            
            // Load energy access classification
            loadEnergyAccessClassification(country);
            
            // Load combined historical + future data
            loadCombinedData(country);'''

content = content.replace(load_country_data_old, load_country_data_new)

# Add the loadEnergyAccessClassification function
classification_function = '''        
        function loadEnergyAccessClassification(country) {
            console.log('🎯 [CLASSIFICATION] Loading energy access classification for:', country);
            
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
            const url = `/api/objective5/combined/?country=${encodeURIComponent(country)}`;
            console.log('📡 [CLASSIFICATION] Calling API:', url);
            
            fetch(url)
                .then(response => {
                    console.log('📊 [CLASSIFICATION] Response status:', response.status);
                    return response.json();
                })
                .then(data => {
                    console.log('📋 [CLASSIFICATION] Data received:', data);
                    
                    if (data.success && data.data && data.data.length > 0) {
                        console.log('✅ [CLASSIFICATION] Found', data.data.length, 'data points');
                        
                        // Get canvas
                        const canvas = document.getElementById('classificationChart');
                        if (!canvas) {
                            console.error('❌ [CLASSIFICATION] Canvas not found');
                            return;
                        }
                        
                        // Destroy existing chart
                        if (classificationChart) {
                            classificationChart.destroy();
                        }
                        
                        // Separate historical and future data
                        const historical = data.data.filter(d => d.type === 'historical');
                        const future = data.data.filter(d => d.type === 'predicted');
                        
                        console.log('📊 [CLASSIFICATION] Historical points:', historical.length);
                        console.log('📊 [CLASSIFICATION] Future points:', future.length);
                        
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
                        
                        console.log('✅ [CLASSIFICATION] Chart created successfully!');
                        
                    } else {
                        console.error('❌ [CLASSIFICATION] No data available');
                        if (nameElement) {
                            nameElement.textContent = `No classification data available for ${country}`;
                        }
                    }
                })
                .catch(error => {
                    console.error('❌ [CLASSIFICATION] Error:', error);
                    if (nameElement) {
                        nameElement.textContent = `Error loading classification for ${country}: ${error.message}`;
                    }
                });
        }'''

# Insert the function before loadCombinedData
load_combined_pos = content.find('function loadCombinedData(country) {')
if load_combined_pos != -1:
    content = content[:load_combined_pos] + classification_function + '\n        ' + content[load_combined_pos:]
    print("✅ Added loadEnergyAccessClassification function")

# Write the updated file
with open('sustainable_energy/dashboard/templates/dashboard/objective5_classification.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n🎉 Energy Access Classification Chart Added!")
print("\n📋 What was added:")
print("   ✅ New section: Energy Access Classification per Country (Historical + Future)")
print("   ✅ Stepped line chart showing Low/Medium/High access levels")
print("   ✅ Historical data (solid blue line)")
print("   ✅ Future predictions (dashed green line)")
print("   ✅ Y-axis with access level labels")
print("   ✅ X-axis from 2000 to 2030")
print("   ✅ Automatic loading when country is selected")

print("\n🎯 Chart Features:")
print("   - Type: Stepped line chart")
print("   - Historical: Solid blue line")
print("   - Future: Dashed green line")
print("   - Y-axis: Low Access, Medium Access, High Access")
print("   - X-axis: Years (2000-2030)")
print("   - Title: Energy Access Classification per Country (Historical + Future)")

print("\n🔄 Next steps:")
print("   1. Restart Django server: python manage.py runserver")
print("   2. Open http://localhost:8000/objective5/")
print("   3. Select a country and click 'Analyze Country'")
print("   4. You should now see the classification chart!")
print("   5. Check console for [CLASSIFICATION] debug messages")

print("\n💡 This chart will show the exact same visualization as in your image!")
print("   The stepped line will show how countries transition between access levels over time.")