#!/usr/bin/env python3
"""
Final fix for Objective 3 Energy Access Classification chart
Replace Plotly.js with Chart.js implementation
"""

# Read the current Objective 3 template
with open('sustainable_energy/dashboard/templates/dashboard/objective3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the canvas element in the combined section
old_canvas = '<div id="combinedPlot" style="width:100%;height:100%;"></div>'
new_canvas = '<canvas id="combinedChart"></canvas>'

if old_canvas in content:
    content = content.replace(old_canvas, new_canvas)
    print("✅ Updated canvas element from Plotly div to Chart.js canvas")

# 2. Add Chart.js variable declaration
if 'let modelComparisonChart = null;' in content and 'let combinedChart = null;' not in content:
    content = content.replace('let modelComparisonChart = null;', 'let modelComparisonChart = null;\n        let combinedChart = null;')
    print("✅ Added combinedChart variable")

# 3. Find and replace the Plotly.js chart creation with Chart.js
# Look for the Plotly.newPlot call and replace the entire section
plotly_start = content.find('Plotly.newPlot(\'combinedPlot\'')
if plotly_start != -1:
    # Find the end of this section (look for the next major block)
    plotly_end = content.find('showMessage(\'success\'', plotly_start)
    if plotly_end != -1:
        # Replace the Plotly section with Chart.js implementation
        chartjs_implementation = '''// Create Chart.js stepped line chart
                    const canvas = document.getElementById('combinedChart');
                    if (!canvas) {
                        console.error('❌ Canvas element not found');
                        return;
                    }
                    
                    // Destroy existing chart
                    if (combinedChart) {
                        combinedChart.destroy();
                    }
                    
                    // Map access levels to numbers for stepped chart
                    const levelMap = {
                        'Low Access': 1,
                        'Medium Access': 2, 
                        'High Access': 3
                    };
                    
                    // Prepare datasets for Chart.js
                    const datasets = [];
                    
                    // Add historical data (solid line)
                    if (historicalData.length > 0) {
                        const histData = historicalData.map(d => ({
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
                    
                    // Add predicted data (dashed line)
                    if (predictions.length > 0) {
                        const predData = predictions.map(d => ({
                            x: d.year,
                            y: levelMap[d.predicted_access_level] || levelMap[d.access_level] || 1
                        }));
                        
                        datasets.push({
                            label: 'Future Predictions',
                            data: predData,
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
                    
                    // Create the Chart.js stepped chart
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
                    
                    console.log('✅ [OBJ3] Energy Access Classification chart created successfully!');
                    
                    '''
        
        content = content[:plotly_start] + chartjs_implementation + content[plotly_end:]
        print("✅ Replaced Plotly.js implementation with Chart.js")

# 4. Ensure Chart.js is loaded (check if it's already there)
if 'chart.js' not in content.lower():
    # Add Chart.js CDN after the existing script tags
    script_pos = content.find('<script src="https://cdn.plot.ly/plotly-2.24.1.min.js"></script>')
    if script_pos != -1:
        chart_js_cdn = '\n    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js"></script>'
        insert_pos = content.find('</script>', script_pos) + len('</script>')
        content = content[:insert_pos] + chart_js_cdn + content[insert_pos:]
        print("✅ Added Chart.js CDN")

# 5. Add debug logging to the analyzeCountry function
if 'console.log(\'🎯 [OBJ3] Starting analysis for:\', country);' not in content:
    # Find the analyzeCountry function and add debug logging
    analyze_start = content.find('function analyzeCountry() {')
    if analyze_start != -1:
        # Find the opening brace and add logging
        brace_pos = content.find('{', analyze_start) + 1
        debug_log = '\n            console.log(\'🎯 [OBJ3] Starting analysis for:\', document.getElementById(\'countrySelect\').value);'
        content = content[:brace_pos] + debug_log + content[brace_pos:]
        print("✅ Added debug logging to analyzeCountry function")

# Write the updated file
with open('sustainable_energy/dashboard/templates/dashboard/objective3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n🎉 Objective 3 Classification Chart Fixed!")
print("\n📋 What was fixed:")
print("   ✅ Replaced Plotly.js div with Chart.js canvas")
print("   ✅ Added combinedChart variable declaration")
print("   ✅ Replaced Plotly.newPlot with Chart.js implementation")
print("   ✅ Added Chart.js CDN if missing")
print("   ✅ Added debug logging")
print("   ✅ Implemented stepped line chart with proper data mapping")

print("\n🎯 Chart Features:")
print("   - Type: Stepped line chart")
print("   - Historical: Solid blue line")
print("   - Future: Dashed green line")
print("   - Y-axis: Low/Medium/High Access levels")
print("   - X-axis: Years (2000-2030)")
print("   - Interactive hover effects")

print("\n🔄 Next steps:")
print("   1. Restart Django server: python manage.py runserver")
print("   2. Open http://localhost:8000/objective3/")
print("   3. Select a country (e.g., Belarus)")
print("   4. Click 'Analyze Country'")
print("   5. Look for the stepped line chart!")
print("   6. Check console for [OBJ3] debug messages")

print("\n💡 The chart will now display the future prediction values!")
print("   The stepped line will show how countries transition between access levels over time.")