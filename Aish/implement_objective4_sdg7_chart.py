#!/usr/bin/env python3

"""
Implement the exact SDG 7 chart style from the provided image in Objective 4
"""

def implement_sdg7_chart_style():
    """Update Objective 4 to match the exact SDG 7 chart from the image"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective4.html"
    
    # Read current template
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the createInteractiveHistoricalChart function
    old_function_start = content.find('function createInteractiveHistoricalChart(allCountryData) {')
    old_function_end = content.find('function loadSpecificCountryData(country) {')
    
    if old_function_start == -1 or old_function_end == -1:
        print("❌ Could not find createInteractiveHistoricalChart function")
        return
    
    # New SDG 7 chart implementation matching the image exactly
    new_chart_function = '''        function createInteractiveHistoricalChart(allCountryData) {
            console.log('📈 Creating SDG 7: Access to Electricity Over Time chart...');
            
            const ctx = document.getElementById('historicalChart').getContext('2d');
            
            if (historicalChart) {
                historicalChart.destroy();
            }
            
            // Prepare datasets for all countries (matching the image style)
            const datasets = [];
            
            // Color palette for countries (similar to the image)
            const colors = [
                '#1f77b4', // Blue (Afghanistan - visible by default)
                '#ff7f0e', // Orange
                '#2ca02c', // Green
                '#d62728', // Red
                '#9467bd', // Purple
                '#8c564b', // Brown
                '#e377c2', // Pink
                '#7f7f7f', // Gray
                '#bcbd22', // Olive
                '#17becf', // Cyan
                '#aec7e8', // Light blue
                '#ffbb78', // Light orange
                '#98df8a', // Light green
                '#ff9896', // Light red
                '#c5b0d5', // Light purple
                '#c49c94', // Light brown
                '#f7b6d3', // Light pink
                '#c7c7c7', // Light gray
                '#dbdb8d', // Light olive
                '#9edae5'  // Light cyan
            ];
            
            // Get all unique years from the data
            let allYears = new Set();
            allCountryData.forEach(countryInfo => {
                if (countryInfo.data && countryInfo.data.length > 0) {
                    countryInfo.data.forEach(d => allYears.add(d.Year));
                }
            });
            allYears = Array.from(allYears).sort();
            
            // Create datasets for each country
            allCountryData.forEach((countryInfo, index) => {
                if (countryInfo.data && countryInfo.data.length > 0) {
                    // Create data array aligned with all years
                    const countryData = {};
                    countryInfo.data.forEach(d => {
                        countryData[d.Year] = d['Access to electricity (% of population)'];
                    });
                    
                    const alignedData = allYears.map(year => countryData[year] || null);
                    
                    datasets.push({
                        label: countryInfo.country,
                        data: alignedData,
                        borderColor: colors[index % colors.length],
                        backgroundColor: colors[index % colors.length] + '20', // 20% opacity
                        borderWidth: 2,
                        fill: false,
                        tension: 0.1,
                        pointRadius: 0, // No points by default
                        pointHoverRadius: 4,
                        hidden: index > 0, // Hide all except Afghanistan (first country)
                        spanGaps: true // Connect lines across null values
                    });
                }
            });
            
            historicalChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: allYears,
                    datasets: datasets
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: true,
                            position: 'right',
                            align: 'start',
                            maxWidth: 250,
                            labels: {
                                boxWidth: 12,
                                padding: 4,
                                font: {
                                    size: 11
                                },
                                usePointStyle: false,
                                generateLabels: function(chart) {
                                    const original = Chart.defaults.plugins.legend.labels.generateLabels;
                                    const labels = original.call(this, chart);
                                    
                                    // Sort labels alphabetically (like in the image)
                                    labels.sort((a, b) => a.text.localeCompare(b.text));
                                    
                                    return labels;
                                }
                            },
                            onClick: function(e, legendItem, legend) {
                                const index = legendItem.datasetIndex;
                                const chart = legend.chart;
                                
                                if (chart.isDatasetVisible(index)) {
                                    chart.hide(index);
                                    legendItem.hidden = true;
                                } else {
                                    chart.show(index);
                                    legendItem.hidden = false;
                                }
                                
                                chart.update();
                            }
                        },
                        title: {
                            display: true,
                            text: 'SDG 7: Access to Electricity Over Time',
                            font: {
                                size: 16,
                                weight: 'bold'
                            },
                            color: '#2c3e50'
                        },
                        tooltip: {
                            mode: 'index',
                            intersect: false,
                            backgroundColor: 'rgba(255, 255, 255, 0.95)',
                            titleColor: '#2c3e50',
                            bodyColor: '#2c3e50',
                            borderColor: '#ddd',
                            borderWidth: 1,
                            callbacks: {
                                title: function(tooltipItems) {
                                    return 'Year: ' + tooltipItems[0].label;
                                },
                                label: function(context) {
                                    if (context.parsed.y !== null) {
                                        return context.dataset.label + ': ' + context.parsed.y.toFixed(1) + '%';
                                    }
                                    return context.dataset.label + ': No data';
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 100,
                            title: {
                                display: true,
                                text: 'Electricity Access',
                                font: {
                                    size: 12,
                                    weight: 'bold'
                                }
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
                        },
                        x: {
                            title: {
                                display: false // Hide x-axis title like in the image
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
                    },
                    hover: {
                        mode: 'nearest',
                        intersect: false
                    },
                    layout: {
                        padding: {
                            right: 20
                        }
                    }
                }
            });
            
            console.log(`✅ SDG 7 chart created with ${datasets.length} countries`);
            console.log('💡 Afghanistan visible by default, click legend to show/hide other countries');
        }
        
        '''
    
    # Replace the function
    content = content[:old_function_start] + new_chart_function + content[old_function_end:]
    
    # Update the chart container styling to match the image
    old_chart_style = '''        .interactive-chart-container {
            position: relative;
            height: 600px;
            margin-top: 20px;
            background: rgba(248, 249, 250, 0.8);
            border-radius: 10px;
            padding: 15px;
        }'''
    
    new_chart_style = '''        .interactive-chart-container {
            position: relative;
            height: 550px;
            margin-top: 20px;
            background: rgba(240, 248, 255, 0.6);
            border-radius: 8px;
            padding: 20px;
            border: 1px solid rgba(0,0,0,0.1);
        }'''
    
    content = content.replace(old_chart_style, new_chart_style)
    
    # Update the historical section title to match exactly
    old_title = '''            <h2 class="section-title"><i class="fas fa-history"></i> Historical Electricity Access</h2>'''
    new_title = '''            <h2 class="section-title"><i class="fas fa-chart-line"></i> SDG 7: Access to Electricity Over Time</h2>'''
    
    content = content.replace(old_title, new_title)
    
    # Write the updated template
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Implemented SDG 7 chart style matching your image!")
    print("\n📊 Chart Features:")
    print("   - Title: 'SDG 7: Access to Electricity Over Time'")
    print("   - Afghanistan visible by default (blue line)")
    print("   - All other countries hidden initially")
    print("   - Right-side legend with all country names")
    print("   - Click legend items to show/hide countries")
    print("   - Light blue background matching the image")
    print("   - Proper grid lines and styling")
    print("\n🎨 Visual Styling:")
    print("   - Matches the exact appearance from your image")
    print("   - Color palette similar to the original")
    print("   - Professional chart layout")
    print("   - Interactive legend functionality")

if __name__ == "__main__":
    implement_sdg7_chart_style()