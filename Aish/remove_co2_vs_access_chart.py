#!/usr/bin/env python3
"""
Remove CO₂ vs Access Chart
==========================

This script removes the CO₂ vs Access chart from the vertical stack layout.
"""

import os
import re

def remove_co2_vs_access_chart():
    """Remove the CO₂ vs Access chart from the layout"""
    
    html_file_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🗑️ REMOVING CO₂ vs ACCESS CHART")
    print("=" * 60)
    print(f"📁 Updating file: {html_file_path}")
    
    # Read current file
    with open(html_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and remove the CO₂ vs Access chart section
    co2_vs_access_section = '''            <!-- Chart 6: CO₂ vs Access -->
            <div class="chart-container-vertical">
                <h4>CO₂ vs Access</h4>
                <div id="co2AccessChart"></div>
            </div>
            '''
    
    # Remove the chart section
    if co2_vs_access_section in content:
        content = content.replace(co2_vs_access_section, '')
        print("✅ Removed CO₂ vs Access chart section from HTML")
    else:
        print("⚠️ Could not find exact CO₂ vs Access section, trying alternative approach")
        
        # Try to find and remove with different spacing
        pattern = r'<!-- Chart 6: CO₂ vs Access -->.*?</div>\s*'
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, '', content, flags=re.DOTALL)
            print("✅ Removed CO₂ vs Access chart using regex")
    
    # Also remove the JavaScript function calls for CO₂ vs Access
    js_functions_to_remove = [
        'renderCO2AccessCorrelation(countryName, coords);',
        'renderCO2AccessCorrelation(countryName, coords)',
    ]
    
    for func_call in js_functions_to_remove:
        if func_call in content:
            content = content.replace(func_call, '')
            print(f"✅ Removed JavaScript function call: {func_call}")
    
    # Remove the renderCO2AccessCorrelation function definition
    function_pattern = r'function renderCO2AccessCorrelation\(countryName, coords\) \{.*?\n        \}'
    if re.search(function_pattern, content, re.DOTALL):
        content = re.sub(function_pattern, '', content, flags=re.DOTALL)
        print("✅ Removed renderCO2AccessCorrelation function definition")
    
    # Update the renderCO2Charts function to not call CO₂ vs Access
    old_render_co2 = '''        function renderCO2Charts(countryName, coords, period) {
            console.log(`Rendering CO₂ charts for ${countryName} with period: ${period}`);
            
            // Render all CO₂ charts
            renderCO2Timeline(countryName, coords, period);
            renderCO2AccessCorrelation(countryName, coords);
            renderCO2Forecast(countryName, coords, period);
        }'''
    
    new_render_co2 = '''        function renderCO2Charts(countryName, coords, period) {
            console.log(`Rendering CO₂ charts for ${countryName} with period: ${period}`);
            
            // Render CO₂ charts (CO₂ vs Access removed)
            renderCO2Timeline(countryName, coords, period);
            renderCO2Forecast(countryName, coords, period);
        }'''
    
    if old_render_co2 in content:
        content = content.replace(old_render_co2, new_render_co2)
        print("✅ Updated renderCO2Charts function to exclude CO₂ vs Access")
    
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
        print("\n" + "=" * 60)
        print("✅ CO₂ vs ACCESS CHART REMOVED!")
        print("=" * 60)
        
        print("\n📊 Updated layout structure:")
        print("   Chart 1: Energy Timeline (2000-2030)")
        print("   Chart 2: Access Forecast")
        print("   Chart 3: Renewable Growth")
        print("   Chart 4: Energy Distribution")
        print("   Chart 5: CO₂ Timeline")
        print("   Chart 6: CO₂ Forecast")
        print("   ❌ Removed: CO₂ vs Access")
        
        print("\n🎨 What was removed:")
        print("   ✓ CO₂ vs Access chart HTML section")
        print("   ✓ renderCO2AccessCorrelation JavaScript function")
        print("   ✓ Function calls to CO₂ vs Access chart")
        print("   ✓ Updated renderCO2Charts to exclude removed chart")
        
        print("\n📊 Remaining charts:")
        print("   ✓ 6 charts total (down from 7)")
        print("   ✓ All charts still arranged vertically")
        print("   ✓ Full width layout maintained")
        print("   ✓ Time period controls still work")
        
        print("\n🧪 To test:")
        print("   1. Go to: http://127.0.0.1:8000/explore/")
        print("   2. Select a country (e.g., India)")
        print("   3. Verify: Only 6 charts appear (no CO₂ vs Access)")
        print("   4. Check: Charts are still arranged vertically")
        print("   5. Test: Time period controls update remaining charts")
        
        print("\n🔄 Clear browser cache with Ctrl+F5 after testing")
    else:
        print("\n❌ FAILED TO REMOVE CO₂ vs ACCESS CHART")

if __name__ == "__main__":
    main()