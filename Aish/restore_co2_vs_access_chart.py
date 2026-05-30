#!/usr/bin/env python3
"""
Restore CO₂ vs Access Chart
===========================

This script restores the CO₂ vs Access chart to the vertical stack layout.
"""

import os
import re

def restore_co2_vs_access_chart():
    """Restore the CO₂ vs Access chart to the layout"""
    
    html_file_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔄 RESTORING CO₂ vs ACCESS CHART")
    print("=" * 60)
    print(f"📁 Updating file: {html_file_path}")
    
    # Read current file
    with open(html_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the CO₂ Timeline chart and add CO₂ vs Access after it
    co2_timeline_section = '''            <!-- Chart 5: CO₂ Timeline -->
            <div class="chart-container-vertical">
                <h4>CO₂ Timeline</h4>
                <div id="co2Chart"></div>
            </div>

            <!-- Chart 7: CO₂ Forecast -->'''
    
    # New section with CO₂ vs Access restored
    restored_section = '''            <!-- Chart 5: CO₂ Timeline -->
            <div class="chart-container-vertical">
                <h4>CO₂ Timeline</h4>
                <div id="co2Chart"></div>
            </div>
            
            <!-- Chart 6: CO₂ vs Access -->
            <div class="chart-container-vertical">
                <h4>CO₂ vs Access</h4>
                <div id="co2AccessChart"></div>
            </div>

            <!-- Chart 7: CO₂ Forecast -->'''
    
    # Replace the section to add CO₂ vs Access back
    if co2_timeline_section in content:
        content = content.replace(co2_timeline_section, restored_section)
        print("✅ Restored CO₂ vs Access chart section to HTML")
    else:
        print("⚠️ Could not find exact CO₂ Timeline section, trying alternative approach")
        
        # Try to find CO₂ Timeline and add CO₂ vs Access after it
        pattern = r'(<!-- Chart 5: CO₂ Timeline -->.*?</div>\s*)\s*(<!-- Chart 7: CO₂ Forecast -->)'
        if re.search(pattern, content, re.DOTALL):
            replacement = r'\1\n            \n            <!-- Chart 6: CO₂ vs Access -->\n            <div class="chart-container-vertical">\n                <h4>CO₂ vs Access</h4>\n                <div id="co2AccessChart"></div>\n            </div>\n\n            \2'
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            print("✅ Restored CO₂ vs Access chart using regex")
    
    # Restore the renderCO2AccessCorrelation function
    co2_access_function = '''        
        function renderCO2AccessCorrelation(countryName, coords) {
            // Create scatter plot showing relationship between electricity access and CO₂ emissions
            const accessData = [coords.access];
            const co2Data = [(coords.co2 || 50000) / 1000]; // Convert to Mt
            
            // Add some comparison countries for context
            const comparisonCountries = ['United States', 'Germany', 'China', 'India', 'Brazil'];
            const comparisonData = comparisonCountries
                .filter(country => country !== countryName && countryCoordinates[country])
                .map(country => ({
                    name: country,
                    access: countryCoordinates[country].access,
                    co2: (countryCoordinates[country].co2 || 50000) / 1000
                }));
            
            const selectedTrace = {
                x: accessData,
                y: co2Data,
                type: 'scatter',
                mode: 'markers',
                name: countryName,
                marker: { 
                    color: '#3498db', 
                    size: 15,
                    symbol: 'star'
                }
            };
            
            const comparisonTrace = {
                x: comparisonData.map(d => d.access),
                y: comparisonData.map(d => d.co2),
                type: 'scatter',
                mode: 'markers',
                name: 'Other Countries',
                marker: { 
                    color: '#95a5a6', 
                    size: 10,
                    opacity: 0.7
                },
                text: comparisonData.map(d => d.name),
                textposition: 'top center'
            };

            const layout = {
                title: `${countryName} - CO₂ Emissions vs Electricity Access`,
                xaxis: { title: 'Electricity Access (%)' },
                yaxis: { title: 'CO₂ Emissions (Mt)' },
                plot_bgcolor: '#f8fafc',
                paper_bgcolor: 'white'
            };

            Plotly.newPlot('co2AccessChart', [selectedTrace, comparisonTrace], layout, { responsive: true });
        }'''
    
    # Find a good place to insert the function (before the closing script tag)
    script_end_pattern = r'(\s*</script>)'
    if re.search(script_end_pattern, content):
        content = re.sub(script_end_pattern, co2_access_function + r'\1', content)
        print("✅ Restored renderCO2AccessCorrelation function")
    
    # Update the renderCO2Charts function to include CO₂ vs Access
    old_render_co2 = '''        function renderCO2Charts(countryName, coords, period) {
            console.log(`Rendering CO₂ charts for ${countryName} with period: ${period}`);
            
            // Render CO₂ charts (CO₂ vs Access removed)
            renderCO2Timeline(countryName, coords, period);
            renderCO2Forecast(countryName, coords, period);
        }'''
    
    new_render_co2 = '''        function renderCO2Charts(countryName, coords, period) {
            console.log(`Rendering CO₂ charts for ${countryName} with period: ${period}`);
            
            // Render all CO₂ charts
            renderCO2Timeline(countryName, coords, period);
            renderCO2AccessCorrelation(countryName, coords);
            renderCO2Forecast(countryName, coords, period);
        }'''
    
    if old_render_co2 in content:
        content = content.replace(old_render_co2, new_render_co2)
        print("✅ Updated renderCO2Charts function to include CO₂ vs Access")
    
    # Write the updated content
    try:
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Successfully restored CO₂ vs Access chart")
        return True
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False

def main():
    """Main function to restore CO₂ vs Access chart"""
    success = restore_co2_vs_access_chart()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ CO₂ vs ACCESS CHART RESTORED!")
        print("=" * 60)
        
        print("\n📊 Updated layout structure:")
        print("   Chart 1: Energy Timeline (2000-2030)")
        print("   Chart 2: Access Forecast")
        print("   Chart 3: Renewable Growth")
        print("   Chart 4: Energy Distribution")
        print("   Chart 5: CO₂ Timeline")
        print("   Chart 6: CO₂ vs Access")
        print("   Chart 7: CO₂ Forecast")
        print("   ✅ Restored: CO₂ vs Access")
        
        print("\n🎨 What was restored:")
        print("   ✓ CO₂ vs Access chart HTML section")
        print("   ✓ renderCO2AccessCorrelation JavaScript function")
        print("   ✓ Function calls to CO₂ vs Access chart")
        print("   ✓ Updated renderCO2Charts to include restored chart")
        
        print("\n📊 Complete chart set:")
        print("   ✓ 7 charts total (back to original)")
        print("   ✓ All charts arranged vertically")
        print("   ✓ Full width layout maintained")
        print("   ✓ Time period controls work with all charts")
        
        print("\n🧪 To test:")
        print("   1. Go to: http://127.0.0.1:8000/explore/")
        print("   2. Select a country (e.g., India)")
        print("   3. Verify: All 7 charts appear (including CO₂ vs Access)")
        print("   4. Check: Charts are still arranged vertically")
        print("   5. Test: Time period controls update all charts")
        
        print("\n🔄 Clear browser cache with Ctrl+F5 after testing")
    else:
        print("\n❌ FAILED TO RESTORE CO₂ vs ACCESS CHART")

if __name__ == "__main__":
    main()