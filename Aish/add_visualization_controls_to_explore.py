#!/usr/bin/env python3
"""
Add Interactive Visualization Controls to Explore Dashboard
"""

import os

def add_visualization_controls():
    """Add time period control buttons to explore dashboard"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔄 Adding Interactive Visualization Controls...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add CSS for visualization controls
        controls_css = '''        
        .visualization-controls {
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            display: none; /* Hidden initially */
        }
        
        .controls-header {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
            color: #333;
        }
        
        .controls-header i {
            margin-right: 10px;
            color: #007bff;
        }
        
        .time-period-buttons {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            justify-content: center;
        }
        
        .time-period-btn {
            background: #f8f9fa;
            color: #495057;
            border: 2px solid #e9ecef;
            padding: 12px 20px;
            border-radius: 25px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            min-width: 180px;
            text-align: center;
        }
        
        .time-period-btn:hover {
            background: #e9ecef;
            border-color: #007bff;
            transform: translateY(-2px);
        }
        
        .time-period-btn.active {
            background: #007bff;
            color: white;
            border-color: #007bff;
            box-shadow: 0 4px 15px rgba(0,123,255,0.3);
        }
        
        @media (max-width: 768px) {
            .time-period-buttons {
                flex-direction: column;
                align-items: center;
            }
            
            .time-period-btn {
                min-width: 250px;
            }
        }'''
        
        # Find the existing CSS section and add our controls CSS
        css_end = content.find('</style>')
        if css_end != -1:
            content = content[:css_end] + controls_css + '\n    ' + content[css_end:]
            print("✅ Added visualization controls CSS")
        
        # Add the HTML for visualization controls after the search section
        controls_html = '''
        <!-- Visualization Controls -->
        <div class="visualization-controls" id="visualizationControls">
            <div class="controls-header">
                <i class="fas fa-sliders-h"></i>
                <h3>Interactive Visualization Controls</h3>
            </div>
            
            <div class="mb-3">
                <strong>Time Period:</strong>
            </div>
            
            <div class="time-period-buttons">
                <button class="time-period-btn active" onclick="filterByTimePeriod('all')" id="btnAllYears">
                    All Years (2000-2030)
                </button>
                <button class="time-period-btn" onclick="filterByTimePeriod('historical')" id="btnHistorical">
                    Historical (2000-2020)
                </button>
                <button class="time-period-btn" onclick="filterByTimePeriod('predictions')" id="btnPredictions">
                    Predictions (2021-2030)
                </button>
                <button class="time-period-btn" onclick="filterByTimePeriod('recent')" id="btnRecent">
                    Recent Trends (2015-2030)
                </button>
            </div>
        </div>'''
        
        # Find the world map div and add controls before it
        map_div = content.find('<!-- World Map -->')
        if map_div != -1:
            content = content[:map_div] + controls_html + '\n\n        ' + content[map_div:]
            print("✅ Added visualization controls HTML")
        
        # Add JavaScript functions for time period filtering
        filter_functions = '''
        
        let currentTimePeriod = 'all';
        
        function filterByTimePeriod(period) {
            console.log(`🔄 Filtering charts by time period: ${period}`);
            
            // Update active button
            document.querySelectorAll('.time-period-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            
            const activeBtn = document.getElementById(`btn${period.charAt(0).toUpperCase() + period.slice(1)}`);
            if (activeBtn) {
                activeBtn.classList.add('active');
            } else if (period === 'all') {
                document.getElementById('btnAllYears').classList.add('active');
            }
            
            currentTimePeriod = period;
            
            // Re-render charts with new time period if country is selected
            if (currentCountry) {
                const coords = countryCoordinates[currentCountry];
                if (coords) {
                    renderChartsWithTimePeriod(currentCountry, coords, period);
                }
            }
        }
        
        function renderChartsWithTimePeriod(countryName, coords, timePeriod) {
            console.log(`📊 Rendering charts for ${countryName} with time period: ${timePeriod}`);
            
            try {
                // Determine year ranges based on time period
                let startYear, endYear, forecastStart, forecastEnd;
                
                switch(timePeriod) {
                    case 'historical':
                        startYear = 2000;
                        endYear = 2020;
                        forecastStart = null;
                        forecastEnd = null;
                        break;
                    case 'predictions':
                        startYear = null;
                        endYear = null;
                        forecastStart = 2021;
                        forecastEnd = 2030;
                        break;
                    case 'recent':
                        startYear = 2015;
                        endYear = 2020;
                        forecastStart = 2021;
                        forecastEnd = 2030;
                        break;
                    default: // 'all'
                        startYear = 2000;
                        endYear = 2020;
                        forecastStart = 2021;
                        forecastEnd = 2030;
                }
                
                // 1. Timeline Chart with filtered data
                if (startYear && endYear) {
                    const years = Array.from({length: endYear - startYear + 1}, (_, i) => startYear + i);
                    const accessData = years.map(year => {
                        return Math.max(0, coords.access - 15 + (year - 2000) * 0.7 + Math.random() * 3 - 1.5);
                    });

                    const timelineTrace = {
                        x: years,
                        y: accessData,
                        type: 'scatter',
                        mode: 'lines+markers',
                        name: `${countryName} Historical`,
                        line: { color: '#3498db', width: 3 },
                        marker: { color: '#3498db', size: 6 }
                    };

                    const traces = [timelineTrace];
                    
                    // Add forecast data if needed
                    if (forecastStart && forecastEnd && (timePeriod === 'all' || timePeriod === 'recent' || timePeriod === 'predictions')) {
                        const forecastYears = Array.from({length: forecastEnd - forecastStart + 1}, (_, i) => forecastStart + i);
                        const forecastData = forecastYears.map(year => {
                            return Math.min(100, coords.access + (year - 2021) * 0.5 + Math.random() * 2 - 1);
                        });
                        
                        const forecastTrace = {
                            x: forecastYears,
                            y: forecastData,
                            type: 'scatter',
                            mode: 'lines+markers',
                            name: `${countryName} Forecast`,
                            line: { color: '#e74c3c', width: 3, dash: 'dash' },
                            marker: { color: '#e74c3c', size: 6 }
                        };
                        
                        traces.push(forecastTrace);
                    }

                    const timelineLayout = {
                        title: {
                            text: `${countryName} - Electricity Access (${getTimePeriodLabel(timePeriod)})`,
                            font: { size: 16, color: '#333' }
                        },
                        xaxis: { title: 'Year', gridcolor: '#f0f0f0' },
                        yaxis: { title: 'Electricity Access (%)', gridcolor: '#f0f0f0', range: [0, 100] },
                        plot_bgcolor: '#fafafa',
                        paper_bgcolor: 'white',
                        margin: { t: 50, r: 30, b: 50, l: 60 }
                    };

                    Plotly.newPlot('mainChart', traces, timelineLayout, { 
                        responsive: true, displayModeBar: false
                    });
                } else if (timePeriod === 'predictions') {
                    // Show only forecast chart for predictions
                    const forecastYears = Array.from({length: 10}, (_, i) => 2021 + i);
                    const forecastData = forecastYears.map(year => {
                        return Math.min(100, coords.access + (year - 2021) * 1.2 + Math.random() * 1.5 - 0.75);
                    });

                    const forecastTrace = {
                        x: forecastYears,
                        y: forecastData,
                        type: 'bar',
                        marker: { 
                            color: '#27ae60',
                            opacity: 0.8,
                            line: { color: '#229954', width: 1 }
                        },
                        name: 'Forecast'
                    };

                    const forecastLayout = {
                        title: {
                            text: `${countryName} - Electricity Access Predictions (2021-2030)`,
                            font: { size: 16, color: '#333' }
                        },
                        xaxis: { title: 'Year', gridcolor: '#f0f0f0' },
                        yaxis: { title: 'Access (%)', gridcolor: '#f0f0f0', range: [0, 100] },
                        plot_bgcolor: '#fafafa',
                        paper_bgcolor: 'white',
                        margin: { t: 50, r: 30, b: 50, l: 60 }
                    };

                    Plotly.newPlot('mainChart', [forecastTrace], forecastLayout, { 
                        responsive: true, displayModeBar: false
                    });
                }
                
                // Render other charts (these remain the same for all time periods)
                renderOtherCharts(countryName, coords);
                
                console.log(`✅ Charts rendered for ${timePeriod} period`);
                
            } catch (error) {
                console.error(`❌ Error rendering charts for ${timePeriod}:`, error);
            }
        }
        
        function getTimePeriodLabel(period) {
            switch(period) {
                case 'historical': return '2000-2020';
                case 'predictions': return '2021-2030';
                case 'recent': return '2015-2030';
                default: return '2000-2030';
            }
        }
        
        function renderOtherCharts(countryName, coords) {
            // Energy Mix Pie Chart (same for all periods)
            const renewableShare = Math.min(60, 15 + (coords.access * 0.4));
            const fossilShare = Math.max(20, 75 - renewableShare);
            const nuclearShare = Math.max(5, 15 - (renewableShare * 0.2));
            const otherShare = Math.max(0, 100 - fossilShare - renewableShare - nuclearShare);

            const pieTrace = {
                values: [fossilShare, renewableShare, nuclearShare, otherShare],
                labels: ['Fossil Fuels', 'Renewables', 'Nuclear', 'Other'],
                type: 'pie',
                marker: { 
                    colors: ['#e74c3c', '#27ae60', '#3498db', '#9b59b6'],
                    line: { color: '#fff', width: 2 }
                },
                textinfo: 'label+percent',
                textposition: 'outside',
                hole: 0.3
            };

            const pieLayout = {
                title: {
                    text: `${countryName} - Energy Source Distribution`,
                    font: { size: 16, color: '#333' }
                },
                plot_bgcolor: '#fafafa',
                paper_bgcolor: 'white',
                margin: { t: 50, r: 30, b: 30, l: 30 },
                showlegend: true,
                legend: {
                    orientation: 'h',
                    x: 0.5,
                    xanchor: 'center',
                    y: -0.1
                }
            };

            Plotly.newPlot('pieChart', [pieTrace], pieLayout, { 
                responsive: true, displayModeBar: false
            });

            // Access Forecast Chart
            const forecastYears = Array.from({length: 10}, (_, i) => 2021 + i);
            const forecastData = forecastYears.map(year => {
                return Math.min(100, coords.access + (year - 2021) * 1.2 + Math.random() * 1.5 - 0.75);
            });

            const forecastTrace = {
                x: forecastYears,
                y: forecastData,
                type: 'bar',
                marker: { 
                    color: '#27ae60',
                    opacity: 0.8,
                    line: { color: '#229954', width: 1 }
                },
                name: 'Forecast'
            };

            const forecastLayout = {
                title: {
                    text: `${countryName} - Access Forecast (2021-2030)`,
                    font: { size: 16, color: '#333' }
                },
                xaxis: { title: 'Year', gridcolor: '#f0f0f0' },
                yaxis: { title: 'Access (%)', gridcolor: '#f0f0f0', range: [0, 100] },
                plot_bgcolor: '#fafafa',
                paper_bgcolor: 'white',
                margin: { t: 50, r: 30, b: 50, l: 60 }
            };

            Plotly.newPlot('accessChart', [forecastTrace], forecastLayout, { 
                responsive: true, displayModeBar: false
            });

            // Renewable Energy Growth Chart
            const renewableYears = Array.from({length: 10}, (_, i) => 2021 + i);
            const renewableData = renewableYears.map(year => {
                const baseRenewable = Math.min(80, 20 + (coords.access * 0.3));
                return Math.min(95, baseRenewable + (year - 2021) * 2.5 + Math.random() * 2 - 1);
            });

            const renewableTrace = {
                x: renewableYears,
                y: renewableData,
                type: 'scatter',
                mode: 'lines+markers',
                name: 'Renewable Share',
                line: { color: '#e74c3c', width: 3, shape: 'spline' },
                marker: { color: '#e74c3c', size: 8 },
                fill: 'tonexty',
                fillcolor: 'rgba(231, 76, 60, 0.1)'
            };

            const baselineTrace = {
                x: renewableYears,
                y: renewableYears.map(() => 0),
                type: 'scatter',
                mode: 'lines',
                line: { color: 'transparent' },
                showlegend: false,
                hoverinfo: 'skip'
            };

            const renewableLayout = {
                title: {
                    text: `${countryName} - Renewable Energy Growth`,
                    font: { size: 16, color: '#333' }
                },
                xaxis: { title: 'Year', gridcolor: '#f0f0f0' },
                yaxis: { title: 'Renewable Share (%)', gridcolor: '#f0f0f0', range: [0, 100] },
                plot_bgcolor: '#fafafa',
                paper_bgcolor: 'white',
                margin: { t: 50, r: 30, b: 50, l: 60 }
            };

            Plotly.newPlot('renewableChart', [baselineTrace, renewableTrace], renewableLayout, { 
                responsive: true, displayModeBar: false
            });
        }'''
        
        # Find the existing renderCharts function and replace it
        old_render_start = content.find('function renderCharts(countryName, coords) {')
        if old_render_start != -1:
            # Find the end of the function
            brace_count = 0
            pos = old_render_start
            while pos < len(content):
                if content[pos] == '{':
                    brace_count += 1
                elif content[pos] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        break
                pos += 1
            
            # Replace the old function with new one that uses time period filtering
            new_render_function = '''function renderCharts(countryName, coords) {
            console.log(`📊 Rendering charts for ${countryName} with current time period: ${currentTimePeriod}`);
            renderChartsWithTimePeriod(countryName, coords, currentTimePeriod);
        }'''
            
            content = content[:old_render_start] + new_render_function + content[pos+1:]
            print("✅ Updated renderCharts function")
        
        # Add the filter functions before the closing script tag
        script_end = content.rfind('</script>')
        if script_end != -1:
            content = content[:script_end] + filter_functions + '\n    ' + content[script_end:]
            print("✅ Added time period filtering functions")
        
        # Update showResultsSection to show visualization controls
        old_show_results = 'resultSection.style.display = \'block\';'
        new_show_results = '''resultSection.style.display = 'block';
            
            // Show visualization controls
            const visualizationControls = document.getElementById('visualizationControls');
            if (visualizationControls) {
                visualizationControls.style.display = 'block';
            }'''
        
        if old_show_results in content:
            content = content.replace(old_show_results, new_show_results)
            print("✅ Updated showResultsSection to show controls")
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully added visualization controls!")
        return True
        
    except Exception as e:
        print(f"❌ Error adding controls: {e}")
        return False

def main():
    """Main function"""
    print("🔄 ADDING INTERACTIVE VISUALIZATION CONTROLS")
    print("=" * 60)
    print("   • All Years (2000-2030)")
    print("   • Historical (2000-2020)")
    print("   • Predictions (2021-2030)")
    print("   • Recent Trends (2015-2030)")
    print("=" * 60)
    
    success = add_visualization_controls()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ VISUALIZATION CONTROLS ADDED!")
        print("=" * 60)
        print("\n🎯 New Features:")
        print("   ✅ Interactive time period buttons")
        print("   ✅ Dynamic chart filtering")
        print("   ✅ Professional control panel")
        print("   ✅ Responsive design")
        
        print("\n📊 Time Period Options:")
        print("   • All Years (2000-2030) - Complete timeline")
        print("   • Historical (2000-2020) - Past data only")
        print("   • Predictions (2021-2030) - Future forecasts")
        print("   • Recent Trends (2015-2030) - Recent + future")
        
        print("\n🔄 User Flow:")
        print("   1. Search and select country")
        print("   2. Click 'Analyze Country'")
        print("   3. See visualization controls appear")
        print("   4. Click time period buttons")
        print("   5. Watch charts update dynamically")
        
        print("\n🚀 Ready to Test:")
        print("   1. Refresh browser (Ctrl+F5)")
        print("   2. Search for a country")
        print("   3. Click 'Analyze Country'")
        print("   4. Try different time period buttons")
        print("   5. See charts change based on selection")
        
        print("\n🎯 INTERACTIVE CONTROLS READY!")
        
    else:
        print("\n❌ Failed to add controls.")

if __name__ == "__main__":
    main()