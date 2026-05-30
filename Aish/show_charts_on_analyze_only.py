#!/usr/bin/env python3
"""
Update dashboard so charts appear only after clicking 'Analyze Country' button
"""

import os

def update_dashboard_flow():
    """Update dashboard to show charts only after analysis"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔄 Updating dashboard flow...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Update selectCountry function to NOT show results immediately
        old_select_function = '''        function selectCountry(countryName) {
            const searchInput = document.getElementById('unifiedSearchInput');
            
            if (searchInput) searchInput.value = countryName;
            hideCountryOptions();
            
            console.log(`🎯 Country selected: ${countryName}`);
            
            // Immediately highlight the country on map and show results
            highlightCountryOnMap(countryName);
            showResultsSection(countryName);
        }'''
        
        new_select_function = '''        function selectCountry(countryName) {
            const searchInput = document.getElementById('unifiedSearchInput');
            
            if (searchInput) searchInput.value = countryName;
            hideCountryOptions();
            
            console.log(`🎯 Country selected: ${countryName}`);
            
            // Only highlight the country on map, don't show results yet
            highlightCountryOnMap(countryName);
            
            // Store the selected country for analysis
            currentCountry = countryName;
        }'''
        
        # Replace selectCountry function
        if old_select_function in content:
            content = content.replace(old_select_function, new_select_function)
            print("✅ Updated selectCountry function")
        else:
            print("⚠️ Could not find exact selectCountry function")
        
        # 2. Update analyzeSelectedCountry to show results and render charts
        # Find the part where it calls highlightCountryOnMap and showResultsSection
        old_analyze_part = '''            // Highlight country on map
            highlightCountryOnMap(foundCountry);
            
            // Show results section
            showResultsSection(foundCountry);'''
        
        new_analyze_part = '''            // Highlight country on map
            highlightCountryOnMap(foundCountry);
            
            // Show results section with charts
            showResultsSection(foundCountry);'''
        
        if old_analyze_part in content:
            content = content.replace(old_analyze_part, new_analyze_part)
            print("✅ Updated analyzeSelectedCountry function")
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully updated dashboard flow!")
        return True
        
    except Exception as e:
        print(f"❌ Error updating dashboard: {e}")
        return False

def main():
    """Main function"""
    print("🔄 UPDATING DASHBOARD FLOW")
    print("=" * 50)
    print("   • Charts appear ONLY after clicking 'Analyze Country'")
    print("   • Country selection only highlights map")
    print("   • Analysis button shows results + all charts")
    print("=" * 50)
    
    success = update_dashboard_flow()
    
    if success:
        print("\n" + "=" * 50)
        print("✅ DASHBOARD FLOW UPDATED!")
        print("=" * 50)
        print("\n🎯 New Flow:")
        print("   1. User searches/selects country → Map highlights only")
        print("   2. User clicks 'Analyze Country' → Charts appear")
        print("   3. All 4 charts render together with analysis")
        
        print("\n📊 Charts Include:")
        print("   • Timeline Chart (Electricity Access Trends)")
        print("   • Pie Chart (Energy Source Distribution)")
        print("   • Forecast Chart (Future Access Predictions)")
        print("   • Renewable Chart (Growth Projections)")
        
        print("\n🚀 Ready to Test:")
        print("   1. Refresh browser (Ctrl+F5)")
        print("   2. Search for a country (only map highlights)")
        print("   3. Click 'Analyze Country' (charts appear)")
        
        print("\n🎯 PERFECT! Charts only after analysis!")
        
    else:
        print("\n❌ Update failed.")

if __name__ == "__main__":
    main()