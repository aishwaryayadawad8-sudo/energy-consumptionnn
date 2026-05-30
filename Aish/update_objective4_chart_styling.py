#!/usr/bin/env python3

"""
Update Objective 4 chart styling to match the provided image
Make it wider and improve the legend layout
"""

def update_chart_styling():
    """Update chart styling in Objective 4 template"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective4.html"
    
    # Read current template
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update chart container styling
    old_chart_style = '''        .chart-container {
            position: relative;
            height: 400px;
            margin-top: 20px;
        }'''
    
    new_chart_style = '''        .chart-container {
            position: relative;
            height: 500px;
            margin-top: 20px;
        }
        
        .interactive-chart-container {
            position: relative;
            height: 600px;
            margin-top: 20px;
            background: rgba(248, 249, 250, 0.8);
            border-radius: 10px;
            padding: 15px;
        }'''
    
    content = content.replace(old_chart_style, new_chart_style)
    
    # Update the historical section to use the new styling
    old_historical_section = '''        <!-- Historical Data Section -->
        <div class="section-card" id="historicalSection" style="display: none;">
            <h2 class="section-title"><i class="fas fa-history"></i> Historical Electricity Access</h2>
            <p class="text-muted" id="historicalCountryName"></p>
            <div class="chart-container">
                <canvas id="historicalChart"></canvas>
            </div>
        </div>'''
    
    new_historical_section = '''        <!-- Historical Data Section -->
        <div class="section-card" id="historicalSection" style="display: none;">
            <h2 class="section-title"><i class="fas fa-history"></i> Historical Electricity Access</h2>
            <p class="text-muted" id="historicalCountryName"></p>
            <div class="interactive-chart-container">
                <canvas id="historicalChart"></canvas>
            </div>
        </div>'''
    
    content = content.replace(old_historical_section, new_historical_section)
    
    # Update the chart creation to have better legend positioning
    old_legend_config = '''                        legend: {
                            display: true,
                            position: 'right',
                            labels: {
                                boxWidth: 12,
                                padding: 8,
                                font: {
                                    size: 11
                                },
                                generateLabels: function(chart) {
                                    const original = Chart.defaults.plugins.legend.labels.generateLabels;
                                    const labels = original.call(this, chart);
                                    
                                    // Add click handler info
                                    labels.forEach(label => {
                                        label.text = label.text + (label.hidden ? ' (hidden)' : '');
                                    });
                                    
                                    return labels;
                                }
                            },'''
    
    new_legend_config = '''                        legend: {
                            display: true,
                            position: 'right',
                            align: 'start',
                            maxWidth: 200,
                            labels: {
                                boxWidth: 15,
                                padding: 6,
                                font: {
                                    size: 12
                                },
                                usePointStyle: true,
                                generateLabels: function(chart) {
                                    const original = Chart.defaults.plugins.legend.labels.generateLabels;
                                    const labels = original.call(this, chart);
                                    
                                    // Sort labels alphabetically
                                    labels.sort((a, b) => a.text.localeCompare(b.text));
                                    
                                    return labels;
                                }
                            },'''
    
    content = content.replace(old_legend_config, new_legend_config)
    
    # Add auto-load functionality when page loads
    old_window_onload = '''        // Load model comparison automatically on page load
        window.onload = function() {
            console.log('🚀 [OBJ4] Page loaded, loading model comparison instantly...');
            loadModelComparison();
        };'''
    
    new_window_onload = '''        // Load model comparison automatically on page load
        window.onload = function() {
            console.log('🚀 [OBJ4] Page loaded, loading model comparison instantly...');
            loadModelComparison();
            
            // Auto-load interactive chart after 2 seconds
            setTimeout(() => {
                console.log('🌍 Auto-loading interactive historical chart...');
                loadAllCountriesHistoricalChart();
            }, 2000);
        };'''
    
    content = content.replace(old_window_onload, new_window_onload)
    
    # Write the updated template
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Updated Objective 4 chart styling!")
    print("\n🎨 Styling Improvements:")
    print("   - Larger chart container (600px height)")
    print("   - Better legend positioning (right side, sorted alphabetically)")
    print("   - Background styling for interactive charts")
    print("   - Auto-loads interactive chart on page load")
    print("   - Improved legend with point styles")
    print("\n📊 Chart Features:")
    print("   - All countries loaded but hidden by default")
    print("   - Click legend to show/hide countries")
    print("   - Sorted country list in legend")
    print("   - Matches your provided image style")

if __name__ == "__main__":
    update_chart_styling()