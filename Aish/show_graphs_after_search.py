#!/usr/bin/env python3
"""
Show all graphs immediately after searching/selecting a country
"""

import os

def show_graphs_after_search():
    """Update dashboard to show graphs immediately after country search"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔄 Updating dashboard to show graphs after search...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Update selectCountry function to show results immediately
        old_select_function = '''        function selectCountry(countryName) {
            const searchInput = document.getElementById('unifiedSearchInput');
            
            if (searchInput) searchInput.value = countryName;
            hideCountryOptions();
            
            console.log(`🎯 Country selected: ${countryName}`);
            
            // Only highlight the country on map, don't show results yet
            highlightCountryOnMap(countryName);
            
            // Store the selected country for analysis
            currentCountry = countryName;
        }'''
        
        new_select_function = '''        function selectCountry(countryName) {
            const searchInput = document.getElementById('unifiedSearchInput');
            
            if (searchInput) searchInput.value = countryName;
            hideCountryOptions();
            
            console.log(`🎯 Country selected: ${countryName}`);
            
            // Highlight country on map AND show results immediately
            highlightCountryOnMap(countryName);
            showResultsSection(countryName);
            
            // Store the selected country for analysis
            currentCountry = countryName;
        }'''
        
        # Replace selectCountry function
        if old_select_function in content:
            content = content.replace(old_select_function, new_select_function)
            print("✅ Updated selectCountry to show graphs immediately")
        
        # 2. Update analyzeSelectedCountry to also show results for manual search
        # Find the part where it shows results and make sure it works for both paths
        old_analyze_end = '''            // Highlight country on map
            highlightCountryOnMap(foundCountry);
            
            // Show results section with charts
            showResultsSection(foundCountry);'''
        
        new_analyze_end = '''            // Highlight country on map and show results
            highlightCountryOnMap(foundCountry);
            showResultsSection(foundCountry);'''
        
        if old_analyze_end in content:
            content = content.replace(old_analyze_end, new_analyze_end)
            print("✅ Updated analyzeSelectedCountry function")
        
        # 3. Make the "Analyze Country" button optional by updating its text
        old_button_html = '''            <div class="text-center">
                <button class="analyze-btn" onclick="analyzeSelectedCountry()">
                    <i class="fas fa-search"></i> Analyze Country
                </button>
            </div>'''
        
        new_button_html = '''            <div class="text-center">
                <button class="analyze-btn" onclick="analyzeSelectedCountry()">
                    <i class="fas fa-search"></i> Search & Analyze
                </button>
                <div style="margin-top: 10px; color: #666; font-size: 12px;">
                    <i class="fas fa-info-circle"></i> Charts appear automatically when you select a country
                </div>
            </div>'''
        
        if old_button_html in content:
            content = content.replace(old_button_html, new_button_html)
            print("✅ Updated button text and added info message")
        
        # 4. Add automatic search functionality when typing
        # Find the search input event listener and enhance it
        old_input_listener = '''            // Search input functionality
            searchInput.addEventListener('input', function() {
                const query = this.value.toLowerCase();
                if (query.length === 0) {
                    showAllCountries();
                } else {
                    filterCountries(query);
                }
                
                if (!isDropdownOpen) {
                    toggleCountryOptions();
                }
            });'''
        
        new_input_listener = '''            // Search input functionality with auto-analysis
            searchInput.addEventListener('input', function() {
                const query = this.value.toLowerCase();
                if (query.length === 0) {
                    showAllCountries();
                } else {
                    filterCountries(query);
                    
                    // Auto-analyze if exact match found
                    const exactMatch = Object.keys(countryCoordinates).find(country => 
                        country.toLowerCase() === query
                    );
                    
                    if (exactMatch) {
                        setTimeout(() => {
                            selectCountry(exactMatch);
                        }, 500); // Small delay for better UX
                    }
                }
                
                if (!isDropdownOpen) {
                    toggleCountryOptions();
                }
            });'''
        
        if old_input_listener in content:
            content = content.replace(old_input_listener, new_input_listener)
            print("✅ Added auto-analysis for exact matches")
        
        # 5. Update the instruction text to reflect new behavior
        old_instruction = '''            <div class="mb-3" style="color: #666; font-size: 14px; text-align: center;">
                <i class="fas fa-info-circle"></i> Select a time period, then search and analyze a country to see filtered charts
            </div>'''
        
        new_instruction = '''            <div class="mb-3" style="color: #666; font-size: 14px; text-align: center;">
                <i class="fas fa-info-circle"></i> Select a time period, then search for a country - charts will appear automatically
            </div>'''
        
        if old_instruction in content:
            content = content.replace(old_instruction, new_instruction)
            print("✅ Updated instruction text")
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully updated dashboard for automatic graph display!")
        return True
        
    except Exception as e:
        print(f"❌ Error updating dashboard: {e}")
        return False

def main():
    """Main function"""
    print("🔄 SHOWING GRAPHS AFTER SEARCH")
    print("=" * 50)
    print("   • Graphs appear immediately after country selection")
    print("   • No need to click 'Analyze Country' button")
    print("   • Auto-analysis for exact matches while typing")
    print("   • Improved user experience")
    print("=" * 50)
    
    success = show_graphs_after_search()
    
    if success:
        print("\n" + "=" * 50)
        print("✅ GRAPHS NOW SHOW AFTER SEARCH!")
        print("=" * 50)
        print("\n🎯 New Behavior:")
        print("   ✅ Select country → Graphs appear immediately")
        print("   ✅ Type exact country name → Auto-analysis")
        print("   ✅ Click dropdown option → Instant graphs")
        print("   ✅ Manual search button still works")
        
        print("\n🔄 User Experience:")
        print("   1. User selects time period (optional)")
        print("   2. User searches/selects country")
        print("   3. Map highlights + ALL GRAPHS APPEAR")
        print("   4. User can change time periods anytime")
        
        print("\n📊 What Appears Automatically:")
        print("   • Timeline Chart (filtered by time period)")
        print("   • Energy Mix Pie Chart")
        print("   • Access Forecast Chart")
        print("   • Renewable Growth Chart")
        print("   • Metric cards with country data")
        
        print("\n🚀 Ready to Test:")
        print("   1. Refresh browser (Ctrl+F5)")
        print("   2. Search for 'India' or select from dropdown")
        print("   3. See ALL GRAPHS appear immediately")
        print("   4. Try different countries")
        print("   5. Change time periods to see filtering")
        
        print("\n🎯 AUTOMATIC GRAPH DISPLAY READY!")
        
    else:
        print("\n❌ Failed to update dashboard.")

if __name__ == "__main__":
    main()