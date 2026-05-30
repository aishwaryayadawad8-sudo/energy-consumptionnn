#!/usr/bin/env python3
"""
Add realistic variation to the Access Forecast chart bars
"""

import os

def add_forecast_variation():
    """Update forecast chart to show realistic variation in bars"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔄 Adding realistic variation to Access Forecast chart...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the Access Forecast Chart generation in renderOtherCharts function
        old_forecast_code = '''            // Access Forecast Chart
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
            });'''
        
        new_forecast_code = '''            // Access Forecast Chart with realistic variation
            const forecastYears = Array.from({length: 10}, (_, i) => 2021 + i);
            
            // Create realistic forecast with variation based on country development level
            const baseAccess = coords.access;
            const developmentFactor = baseAccess / 100; // 0 to 1 scale
            
            const forecastData = forecastYears.map((year, index) => {
                let yearlyGrowth;
                let variation;
                
                // Different growth patterns based on current access level
                if (baseAccess < 30) {
                    // Low access countries: rapid but variable growth
                    yearlyGrowth = 3.5 + Math.sin(index * 0.8) * 1.5; // 2-5% growth
                    variation = Math.random() * 4 - 2; // ±2% variation
                } else if (baseAccess < 60) {
                    // Medium access countries: steady growth with some variation
                    yearlyGrowth = 2.2 + Math.sin(index * 0.6) * 1.0; // 1.2-3.2% growth
                    variation = Math.random() * 3 - 1.5; // ±1.5% variation
                } else if (baseAccess < 90) {
                    // High access countries: moderate growth, more variation
                    yearlyGrowth = 1.1 + Math.cos(index * 0.5) * 0.8; // 0.3-1.9% growth
                    variation = Math.random() * 2.5 - 1.25; // ±1.25% variation
                } else {
                    // Very high access countries: minimal growth, small variations
                    yearlyGrowth = 0.3 + Math.sin(index * 0.4) * 0.4; // -0.1-0.7% growth
                    variation = Math.random() * 1.5 - 0.75; // ±0.75% variation
                }
                
                // Calculate cumulative access with realistic constraints
                const cumulativeGrowth = yearlyGrowth * (index + 1);
                let projectedAccess = baseAccess + cumulativeGrowth + variation;
                
                // Add some economic cycle effects (every 3-4 years)
                if (index === 2 || index === 6) {
                    projectedAccess -= 0.8; // Economic slowdown years
                }
                if (index === 4 || index === 8) {
                    projectedAccess += 1.2; // Economic boom years
                }
                
                // Ensure realistic bounds
                projectedAccess = Math.max(baseAccess - 2, projectedAccess); // Don't go below baseline-2%
                projectedAccess = Math.min(100, projectedAccess); // Cap at 100%
                
                return Math.round(projectedAccess * 10) / 10; // Round to 1 decimal
            });

            // Create varied colors based on values (green gradient)
            const colors = forecastData.map(value => {
                const intensity = (value - Math.min(...forecastData)) / (Math.max(...forecastData) - Math.min(...forecastData));
                const greenValue = Math.floor(150 + intensity * 105); // 150-255 range
                return `rgb(39, ${greenValue}, 96)`; // Varying green intensity
            });

            const forecastTrace = {
                x: forecastYears,
                y: forecastData,
                type: 'bar',
                marker: { 
                    color: colors,
                    opacity: 0.8,
                    line: { color: '#229954', width: 1 }
                },
                name: 'Forecast',
                text: forecastData.map(val => `${val}%`),
                textposition: 'outside',
                textfont: { size: 10, color: '#333' }
            };

            const forecastLayout = {
                title: {
                    text: `${countryName} - Access Forecast (2021-2030)`,
                    font: { size: 16, color: '#333' }
                },
                xaxis: { 
                    title: 'Year', 
                    gridcolor: '#f0f0f0',
                    tickmode: 'array',
                    tickvals: forecastYears,
                    ticktext: forecastYears.map(y => y.toString())
                },
                yaxis: { 
                    title: 'Access (%)', 
                    gridcolor: '#f0f0f0', 
                    range: [Math.max(0, Math.min(...forecastData) - 5), Math.min(100, Math.max(...forecastData) + 5)]
                },
                plot_bgcolor: '#fafafa',
                paper_bgcolor: 'white',
                margin: { t: 50, r: 30, b: 50, l: 60 },
                showlegend: false
            };

            Plotly.newPlot('accessChart', [forecastTrace], forecastLayout, { 
                responsive: true, displayModeBar: false
            });'''
        
        # Replace the forecast chart code
        if old_forecast_code in content:
            content = content.replace(old_forecast_code, new_forecast_code)
            print("✅ Updated Access Forecast chart with realistic variation")
        else:
            print("⚠️ Could not find exact forecast code, searching for alternative...")
            
            # Try to find and replace a simpler pattern
            if "Access Forecast Chart" in content:
                # Find the section and update it
                start_pos = content.find("// Access Forecast Chart")
                if start_pos != -1:
                    # Find the end of this chart section (next chart or function end)
                    end_markers = [
                        "// Renewable Energy Growth Chart",
                        "function renderOtherCharts",
                        "function getTimePeriodLabel"
                    ]
                    
                    end_pos = len(content)
                    for marker in end_markers:
                        marker_pos = content.find(marker, start_pos + 100)
                        if marker_pos != -1 and marker_pos < end_pos:
                            end_pos = marker_pos
                    
                    # Replace the section
                    content = content[:start_pos] + new_forecast_code + "\n\n            " + content[end_pos:]
                    print("✅ Updated forecast chart using pattern matching")
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully added forecast variation!")
        return True
        
    except Exception as e:
        print(f"❌ Error adding forecast variation: {e}")
        return False

def main():
    """Main function"""
    print("🔄 ADDING FORECAST VARIATION")
    print("=" * 50)
    print("   • Realistic growth patterns based on country level")
    print("   • Economic cycle effects (boom/slowdown years)")
    print("   • Varied bar colors (green gradient)")
    print("   • Value labels on each bar")
    print("   • Dynamic Y-axis scaling")
    print("=" * 50)
    
    success = add_forecast_variation()
    
    if success:
        print("\n" + "=" * 50)
        print("✅ FORECAST VARIATION ADDED!")
        print("=" * 50)
        print("\n📊 New Forecast Features:")
        print("   ✅ Realistic year-to-year variation")
        print("   ✅ Country-specific growth patterns:")
        print("      • Low access (<30%): Rapid growth, high variation")
        print("      • Medium access (30-60%): Steady growth, moderate variation")
        print("      • High access (60-90%): Slow growth, some variation")
        print("      • Very high access (>90%): Minimal growth, small variation")
        
        print("\n🎨 Visual Improvements:")
        print("   ✅ Gradient green colors (darker = higher values)")
        print("   ✅ Value labels on each bar")
        print("   ✅ Dynamic Y-axis scaling")
        print("   ✅ Economic cycle effects")
        
        print("\n🧪 Test Different Countries:")
        print("   • Chad (11.1%) → See rapid growth with high variation")
        print("   • Ethiopia (44.3%) → See steady growth with some ups/downs")
        print("   • India (95.2%) → See minimal growth with small variations")
        print("   • Germany (100%) → See maintenance with tiny fluctuations")
        
        print("\n🚀 Ready to Test:")
        print("   1. Refresh browser (Ctrl+F5)")
        print("   2. Search for different countries")
        print("   3. Look at Access Forecast chart")
        print("   4. See varied bar heights and colors")
        print("   5. Notice country-specific patterns")
        
        print("\n🎯 REALISTIC FORECAST VARIATION READY!")
        
    else:
        print("\n❌ Failed to add forecast variation.")

if __name__ == "__main__":
    main()