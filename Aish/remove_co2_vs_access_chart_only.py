#!/usr/bin/env python3
"""
Remove CO₂ vs Access Chart Only
===============================

This script removes only the CO₂ vs Access chart from the explore dashboard
while keeping all other charts intact.
"""

import os

def remove_co2_vs_access_chart():
    """Remove the CO₂ vs Access chart from the dashboard"""
    
    html_file_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🗑️ REMOVING CO₂ VS ACCESS CHART")
    print("=" * 50)
    print(f"📁 Updating file: {html_file_path}")
    
    # Read current file
    with open(html_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the CO₂ vs Access chart container
    chart_container = '''            <!-- Chart 6: CO₂ vs Access -->
            <div class="chart-container-vertical">
                <h4>CO₂ vs Access</h4>
                <div id="co2AccessChart"></div>
            </div>'''
    
    if chart_container in content:
        content = content.replace(chart_container, '')
        print("✅ Removed CO₂ vs Access chart container")
    else:
        print("⚠️ Chart container not found, trying alternative format")
        # Try alternative format
        alt_container = '''            <!-- Chart 6: CO₂ vs Access -->
            <div class="chart-container-vertical">
                <h4>CO₂ vs Access</h4>
                <div id="co2AccessChart"></div>
            </div>

'''
        if alt_container in content:
            content = content.replace(alt_container, '')
            print("✅ Removed CO₂ vs Access chart container (alternative format)")
    
    # Remove the sample rendering function call
    sample_function_call = "                renderSampleCO2AccessCorrelation();"
    if sample_function_call in content:
        content = content.replace(sample_function_call, '')
        print("✅ Removed sample CO₂ vs Access function call")
    
    # Remove the country-specific rendering function call
    country_function_call = "                renderCountryCO2AccessCorrelation(countryName, coords);"
    if country_function_call in content:
        content = content.replace(country_function_call, '')
        print("✅ Removed country CO₂ vs Access function call")
    
    # Remove the sample rendering function
    sample_function_start = "        function renderSampleCO2AccessCorrelation() {"
    sample_function_end = "            Plotly.newPlot('co2AccessChart', [trace], layout, { responsive: true });\n        }"
    
    start_index = content.find(sample_function_start)
    if start_index != -1:
        end_index = content.find(sample_function_end, start_index)
        if end_index != -1:
            end_index += len(sample_function_end)
            content = content[:start_index] + content[end_index:]
            print("✅ Removed sample CO₂ vs Access function")
    
    # Remove the country-specific rendering function
    country_function_start = "        function renderCountryCO2AccessCorrelation(countryName, coords) {"
    country_function_end = "            Plotly.newPlot('co2AccessChart', [selectedTrace, comparisonTrace], layout, { responsive: true });\n        }"
    
    start_index = content.find(country_function_start)
    if start_index != -1:
        end_index = content.find(country_function_end, start_index)
        if end_index != -1:
            end_index += len(country_function_end)
            content = content[:start_index] + content[end_index:]
            print("✅ Removed country CO₂ vs Access function")
    
    # Clean up any extra blank lines
    content = content.replace('\n\n\n', '\n\n')
    
    # Write the updated content
    try:
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Successfully removed CO₂ vs Access chart")
        return True
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False

def main():
    """Main function to remove CO₂ vs Access chart"""
    success = remove_co2_vs_access_chart()
    
    if success:
        print("\n" + "=" * 50)
        print("✅ CO₂ VS ACCESS CHART REMOVED!")
        print("=" * 50)
        
        print("\n🗑️ What was removed:")
        print("   ✓ CO₂ vs Access chart container")
        print("   ✓ Sample CO₂ vs Access function")
        print("   ✓ Country CO₂ vs Access function")
        print("   ✓ Function calls for CO₂ vs Access")
        
        print("\n📊 Remaining charts:")
        print("   ✓ Energy Timeline (2000-2030)")
        print("   ✓ Access Forecast")
        print("   ✓ Renewable Growth")
        print("   ✓ Energy Distribution")
        print("   ✓ CO₂ Timeline")
        print("   ✓ CO₂ Forecast")
        print("   ❌ CO₂ vs Access (REMOVED)")
        
        print("\n🧪 To test:")
        print("   1. Go to: http://127.0.0.1:8000/explore/")
        print("   2. Clear cache: Ctrl+F5")
        print("   3. Verify: CO₂ vs Access chart is gone")
        print("   4. Verify: All other 6 charts still work")
        print("   5. Test country selection still works")
        
        print("\n🔄 Clear browser cache with Ctrl+F5")
    else:
        print("\n❌ FAILED TO REMOVE CO₂ VS ACCESS CHART")

if __name__ == "__main__":
    main()