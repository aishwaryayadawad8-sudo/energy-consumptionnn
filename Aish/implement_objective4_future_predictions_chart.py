#!/usr/bin/env python3

"""
Implement the "Electricity Access Levels (Historical + Future)" chart for Objective 4 future predictions
"""

def implement_future_predictions_chart():
    """Update Objective 4 to show the categorical access levels chart for future predictions"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective4.html"
    
    # Read current template
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add a new section for the combined historical + future chart
    predictions_section_start = content.find('<!-- Future Predictions Section -->')
    predictions_section_end = content.find('</div>\n    </div>\n    \n        <script')
    
    if predictions_section_start == -1:
        print("❌ Could not find Future Predictions Section")
        return
    
    # New combined historical + future section
    new_combined_section = '''        <!-- Future Predictions Section -->
        <div class="section-card" id="predictionsSection" style="display: none;">
            <h2 class="section-title"><i class="fas fa-crystal-ball"></i> Future Predictions (Next 7 Years)</h2>
            <p class="text-muted" id="predictionsCountryName"></p>
            <div class="chart-container">
                <canvas id="predictionsChart"></canvas>
            </div>
        </div>
        
        <!-- Combined Historical + Future Access Levels -->
        <div class="section-card" id="combinedAccessLevelsSection" style="display: none;">
            <h2 class="section-title"><i class="fas fa-chart-area"></i> Electricity Access Levels (Historical + Future)</h2>
            <p class="text-muted" id="combinedAccessCountryName"></p>
            <div class="interactive-chart-container">
                <canvas id="combinedAccessChart"></canvas>
            </div>
        </div>
    </div>
    
    '''
    
    # Replace the predictions section
    content = content[:predictions_section_start] + new_combined_section + content[predictions_section_end:]
    
    # Add the new chart creation function
    load_specific_function_start = content.find('function loadSpecificCountryData(country) {')
    load_specific_function_end = content.find('        }')
    
    if load_specific_function_start == -1:
        print("❌ Could not find loadSpecificCountryData function")
        return
    
    # Find the end of the loadSpecificCountryData function properly
    function_content = content[load_specific_function_start:]
    brace_count = 0
    function_end_pos = 0
    
    for i, char in enumerate(function_content):
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0:
                function_end_pos = load_specific_function_start + i + 1
                break
    
    # Add new function after loadSpecificCountryData
    new_combined_function = '''
        
        function createCombinedAccessLevelsChart(country, historicalData, predictionsData) {
            console.log('📊 Creating combined historical + future access levels chart...');
            
            // Show the combined section
            document.getElementById('combinedAccessLevelsSection').style.display = 'block';
            document.getElementById('combinedAccessCountryName').textContent = 
                `Access level progression for ${country} (Historical + ML Predictions)`;
            
            const ctx = document.getElementById('combinedAccessChart').getContext('2d');
            
            if (window.combinedAccessChart) {
                window.combinedAccessChart.destroy();
            }
            
            // Prepare data for categorical chart
            const allYears = [];
            const accessLevels = [];
            
            // Add historical data
            historicalData.forEach(point => {
                allYears.push(point.Year);
                const access = point['Access to electricity (% of population)'];
                
                // Categorize access levels
                if (access <= 50) {
                    accessLevels.push('Low Access');
                } else if (access <= 90) {
                    accessLevels.push('Medium Access');
                } else {
                    accessLevels.push('High Access');
                }
            });
            
            // Add future predictions
            predictionsData.forEach(pred => {
                allYears.push(pred.year);
                accessLevels.push(pred.access_level);
            });
            
            // Convert categorical data to numeric for Chart.js
            const numericData = accessLevels.map(level => {
                switch(level) {
                    case 'Low Access': return 1;
                    case 'Medium Access': return 2;
                    case 'High Access': return 3;
                    default: return 1;
                }
            });
            
            // Find the transition point between historical and future
            const historicalLength = historicalData.length;
            
            window.combinedAccessChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: allYears,
                    datasets: [{
                        label: country,
                        data: numericData,
                        borderColor: '#1f77b4',
                        backgroundColor: 'rgba(31, 119, 180, 0.1)',
                        borderWidth: 3,
                        fill: false,
                        tension: 0, // Sharp angles like in the image
                        pointRadius: 4,
                        pointHoverRadius: 6,
                        pointBackgroundColor: function(context) {
                            // Different colors for historical vs future
                            return context.dataIndex < historicalLength ? '#1f77b4' : '#ff7f0e';
                        },
                        pointBorderColor: function(context) {
                            return context.dataIndex < historicalLength ? '#1f77b4' : '#ff7f0e';
                        },
                        segment: {
                            borderDash: function(ctx) {
                                // Dashed line for future predictions
                                return ctx.p0DataIndex >= historicalLength - 1 ? [5, 5] : undefined;
                            }
                        }
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: true,
                            position: 'right',
                            labels: {
                                boxWidth: 12,
                                padding: 8,
                                font: {
                                    size: 11
                                }
                            }
                        },
                        title: {
                            display: true,
                            text: 'Electricity Access Levels (Historical + Future)',
                            font: {
                                size: 16,
                                weight: 'bold'
                            },
                            color: '#2c3e50'
                        },
                        tooltip: {
                            callbacks: {
                                title: function(tooltipItems) {
                                    const index = tooltipItems[0].dataIndex;
                                    const isHistorical = index < historicalLength;
                                    return `Year: ${tooltipItems[0].label} ${isHistorical ? '(Historical)' : '(Predicted)'}`;
                                },
                                label: function(context) {
                                    const level = accessLevels[context.dataIndex];
                                    return `${context.dataset.label}: ${level}`;
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            min: 0.5,
                            max: 3.5,
                            title: {
                                display: true,
                                text: 'Access Level',
                                font: {
                                    size: 12,
                                    weight: 'bold'
                                }
                            },
                            ticks: {
                                stepSize: 1,
                                callback: function(value) {
                                    switch(value) {
                                        case 1: return 'Low Access';
                                        case 2: return 'Medium Access';
                                        case 3: return 'High Access';
                                        default: return '';
                                    }
                                },
                                font: {
                                    size: 11
                                }
                            },
                            grid: {
                                color: function(context) {
                                    // Horizontal dotted lines at each level
                                    if ([1, 2, 3].includes(context.tick.value)) {
                                        return 'rgba(0,0,0,0.3)';
                                    }
                                    return 'rgba(0,0,0,0.1)';
                                },
                                lineWidth: function(context) {
                                    return [1, 2, 3].includes(context.tick.value) ? 2 : 1;
                                },
                                drawBorder: false
                            }
                        },
                        x: {
                            title: {
                                display: false
                            },
                            grid: {
                                color: 'rgba(0,0,0,0.1)',
                                drawBorder: false
                            },
                            ticks: {
                                font: {
                                    size: 11
                                }
                            }
                        }
                    },
                    interaction: {
                        mode: 'nearest',
                        axis: 'x',
                        intersect: false
                    }
                }
            });
            
            console.log('✅ Combined access levels chart created');
        }'''
    
    # Insert the new function
    content = content[:function_end_pos] + new_combined_function + content[function_end_pos:]
    
    # Update the loadSpecificCountryData function to also create the combined chart
    old_predictions_load = '''            // Load predictions for specific country
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
                .catch(error => console.error('Error loading predictions:', error));'''
    
    new_predictions_load = '''            // Load predictions for specific country
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
                        
                        // Also create the combined historical + future chart
                        // Get historical data from the previous API call
                        fetch(`/api/objective4/historical/?country=${encodeURIComponent(country)}`)
                            .then(response => response.json())
                            .then(historicalResponse => {
                                if (historicalResponse.success) {
                                    createCombinedAccessLevelsChart(country, historicalResponse.data, data.predictions);
                                }
                            })
                            .catch(error => console.error('Error loading historical data for combined chart:', error));
                    }
                })
                .catch(error => console.error('Error loading predictions:', error));'''
    
    content = content.replace(old_predictions_load, new_predictions_load)
    
    # Write the updated template
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Implemented 'Electricity Access Levels (Historical + Future)' chart!")
    print("\n📊 New Chart Features:")
    print("   - Title: 'Electricity Access Levels (Historical + Future)'")
    print("   - Categorical Y-axis: Low Access, Medium Access, High Access")
    print("   - Historical data: Solid line with blue points")
    print("   - Future predictions: Dashed line with orange points")
    print("   - Sharp angles (tension: 0) matching your image")
    print("   - Horizontal dotted lines at each access level")
    print("\n🎨 Visual Styling:")
    print("   - Matches the categorical chart from your image")
    print("   - Clear distinction between historical and future")
    print("   - Professional step-like visualization")
    print("   - Interactive tooltips showing historical vs predicted")
    print("\n🎮 User Experience:")
    print("   - Loads automatically when analyzing specific country")
    print("   - Shows both percentage chart and categorical chart")
    print("   - Clear visual separation of historical vs future data")

if __name__ == "__main__":
    implement_future_predictions_chart()