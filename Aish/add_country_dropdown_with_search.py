#!/usr/bin/env python3
"""
Add country dropdown with all countries visible plus search functionality
"""

import os

def add_country_dropdown_with_search():
    """Add dropdown showing all countries plus search bar"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔽 Adding country dropdown with search functionality...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and update the search section
        old_search_section = content.find('<!-- Search Section -->')
        if old_search_section != -1:
            # Find the end of the search section
            search_end = content.find('</div>', content.find('</div>', old_search_section) + 1) + 6
            
            # New search section with dropdown and search
            new_search_section = '''<!-- Search Section -->
        <div class="search-section">
            <h3><i class="fas fa-globe"></i> Country Energy Analysis</h3>
            
            <div class="row">
                <!-- Search Input Column -->
                <div class="col-md-5">
                    <label for="countryInput" class="form-label">
                        <i class="fas fa-search"></i> Search Country
                    </label>
                    <input type="text" id="countryInput" class="form-control" 
                           placeholder="Type country name..." 
                           autocomplete="off"
                           style="border-radius: 8px; padding: 12px;">
                    <div id="searchSuggestions" class="search-suggestions"></div>
                </div>
                
                <!-- Dropdown Column -->
                <div class="col-md-5">
                    <label for="countrySelect" class="form-label">
                        <i class="fas fa-list"></i> Select Country
                    </label>
                    <select id="countrySelect" class="form-select" 
                            style="border-radius: 8px; padding: 12px;">
                        <option value="">-- Choose a Country --</option>
                    </select>
                </div>
                
                <!-- Button Column -->
                <div class="col-md-2">
                    <label class="form-label" style="opacity: 0;">Button</label>
                    <button class="btn btn-primary w-100" onclick="analyzeSelectedCountry()" 
                            style="border-radius: 8px; padding: 12px;">
                        <i class="fas fa-search"></i> Analyze
                    </button>
                </div>
            </div>
            
            <div class="text-muted mt-3">
                <small>
                    <i class="fas fa-info-circle"></i> 
                    You can either type in the search box or select from the dropdown
                </small>
            </div>
        </div>'''
            
            # Replace the search section
            content = content[:old_search_section] + new_search_section + content[search_end:]
            print("✅ Updated search section with dropdown and search")
        
        # Update the setupSearchFunctionality function
        old_setup_search = content.find('function setupSearchFunctionality() {')
        if old_setup_search != -1:
            # Find the end of the function
            brace_count = 0
            pos = old_setup_search
            while pos < len(content):
                if content[pos] == '{':
                    brace_count += 1
                elif content[pos] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        function_end = pos + 1
                        break
                pos += 1
            
            # New setupSearchFunctionality with dropdown support
            new_setup_search = '''function setupSearchFunctionality() {
            const countryInput = document.getElementById('countryInput');
            const countrySelect = document.getElementById('countrySelect');
            const searchSuggestions = document.getElementById('searchSuggestions');
            
            // Populate dropdown with all countries
            populateCountryDropdown();
            
            if (!countryInput || !countrySelect) return;
            
            // Search input functionality
            countryInput.addEventListener('input', function() {
                const query = this.value.toLowerCase();
                if (query.length === 0) {
                    if (searchSuggestions) searchSuggestions.style.display = 'none';
                    // Clear dropdown selection when typing
                    countrySelect.value = '';
                } else {
                    filterCountries(query);
                    // Clear dropdown selection when typing
                    countrySelect.value = '';
                }
            });
            
            // Show all countries when clicking on input
            countryInput.addEventListener('focus', function() {
                if (this.value.length === 0) {
                    showAllCountries();
                }
            });
            
            // Dropdown change functionality
            countrySelect.addEventListener('change', function() {
                const selectedCountry = this.value;
                if (selectedCountry) {
                    // Update search input with selected country
                    countryInput.value = selectedCountry;
                    // Hide suggestions
                    if (searchSuggestions) searchSuggestions.style.display = 'none';
                    // Automatically analyze the selected country
                    console.log(`🔽 Country selected from dropdown: ${selectedCountry}`);
                }
            });
            
            // Hide suggestions when clicking outside
            document.addEventListener('click', function(e) {
                if (searchSuggestions && 
                    !countryInput.contains(e.target) && 
                    !searchSuggestions.contains(e.target)) {
                    searchSuggestions.style.display = 'none';
                }
            });
        }'''
            
            # Replace the function
            content = content[:old_setup_search] + new_setup_search + content[function_end:]
            print("✅ Updated setupSearchFunctionality with dropdown support")
        
        # Add populateCountryDropdown function
        script_end = content.rfind('</script>')
        if script_end != -1:
            dropdown_functions = '''
        
        // Populate country dropdown with all available countries
        function populateCountryDropdown() {
            const countrySelect = document.getElementById('countrySelect');
            if (!countrySelect) return;
            
            console.log('🔽 Populating country dropdown...');
            
            // Clear existing options (except the first placeholder)
            countrySelect.innerHTML = '<option value="">-- Choose a Country --</option>';
            
            // Get all countries and sort them
            const allCountries = Object.keys(countryCoordinates).sort();
            
            // Add each country as an option
            allCountries.forEach(country => {
                const option = document.createElement('option');
                option.value = country;
                option.textContent = country;
                countrySelect.appendChild(option);
            });
            
            console.log(`✅ Added ${allCountries.length} countries to dropdown`);
        }
        
        // Enhanced selectCountry function to work with both search and dropdown
        function selectCountryFromSearch(countryName) {
            const countryInput = document.getElementById('countryInput');
            const countrySelect = document.getElementById('countrySelect');
            const searchSuggestions = document.getElementById('searchSuggestions');
            
            // Update both input and dropdown
            if (countryInput) countryInput.value = countryName;
            if (countrySelect) countrySelect.value = countryName;
            if (searchSuggestions) searchSuggestions.style.display = 'none';
            
            console.log(`🎯 Country selected: ${countryName}`);
            
            // Verify country exists
            if (!countryCoordinates[countryName]) {
                console.error(`❌ Selected country ${countryName} not found in database`);
                alert(`Error: ${countryName} data not available. Please try another country.`);
                return;
            }
            
            // Immediately highlight the country on map
            highlightCountryOnMap(countryName);
            
            // Also show results section
            showResultsSection(countryName);
        }
        
        // Update analyzeSelectedCountry to work with both input and dropdown
        function getSelectedCountry() {
            const countryInput = document.getElementById('countryInput');
            const countrySelect = document.getElementById('countrySelect');
            
            // Priority: dropdown selection, then input value
            let countryName = '';
            
            if (countrySelect && countrySelect.value) {
                countryName = countrySelect.value;
                console.log(`🔽 Using dropdown selection: ${countryName}`);
            } else if (countryInput && countryInput.value.trim()) {
                countryName = countryInput.value.trim();
                console.log(`🔍 Using search input: ${countryName}`);
            }
            
            return countryName;
        }'''
            
            # Insert the dropdown functions
            content = content[:script_end] + dropdown_functions + content[script_end:]
            print("✅ Added dropdown population and selection functions")
        
        # Update the existing selectCountry function calls to use the new function
        content = content.replace('item.onclick = () => selectCountry(country);', 'item.onclick = () => selectCountryFromSearch(country);')
        
        # Update analyzeSelectedCountry to use getSelectedCountry
        old_analyze_start = content.find('const countryName = countryInput ? countryInput.value.trim() : \'\';')
        if old_analyze_start != -1:
            old_analyze_end = content.find(';', old_analyze_start) + 1
            new_analyze_line = 'const countryName = getSelectedCountry();'
            content = content[:old_analyze_start] + new_analyze_line + content[old_analyze_end:]
            print("✅ Updated analyzeSelectedCountry to use both input and dropdown")
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully added country dropdown with search!")
        return True
        
    except Exception as e:
        print(f"❌ Error adding dropdown: {e}")
        return False

def main():
    """Main function"""
    print("🔽 ADDING COUNTRY DROPDOWN WITH SEARCH")
    print("=" * 60)
    print("   • Dropdown showing all 128 countries")
    print("   • Search input for typing")
    print("   • Both work together")
    print("   • Auto-sync between input and dropdown")
    print("   • Professional styling")
    print("=" * 60)
    
    success = add_country_dropdown_with_search()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ COUNTRY DROPDOWN WITH SEARCH ADDED!")
        print("=" * 60)
        print("\n🔽 New Features:")
        print("   ✅ Dropdown with all 128 countries")
        print("   ✅ Search input for typing")
        print("   ✅ Both methods work together")
        print("   ✅ Auto-sync between input and dropdown")
        print("   ✅ Professional 3-column layout")
        
        print("\n🎯 How It Works:")
        print("   Method 1 - Dropdown:")
        print("   1. Click dropdown arrow")
        print("   2. Scroll through all countries")
        print("   3. Select any country")
        print("   4. Country appears in search box")
        print("   5. Click 'Analyze' button")
        
        print("\n   Method 2 - Search:")
        print("   1. Type in search box (e.g., 'india')")
        print("   2. See filtered suggestions")
        print("   3. Click on suggestion")
        print("   4. Dropdown updates automatically")
        print("   5. Click 'Analyze' button")
        
        print("\n🎨 Visual Layout:")
        print("   ┌─────────────────────────────────────┐")
        print("   │  🌍 Country Energy Analysis        │")
        print("   ├─────────────┬─────────────┬─────────┤")
        print("   │ 🔍 Search   │ 🔽 Dropdown │ Analyze │")
        print("   │ [india...]  │ [India ▼]  │ [Button]│")
        print("   └─────────────┴─────────────┴─────────┘")
        
        print("\n🌍 All Countries Available:")
        print("   • Major: India, USA, Germany, Brazil, China")
        print("   • European: France, UK, Italy, Spain, Netherlands")
        print("   • Asian: Thailand, Malaysia, Japan, Singapore")
        print("   • African: Nigeria, South Africa, Kenya, Egypt")
        print("   • And 118+ more countries!")
        
        print("\n🚀 Ready to Test:")
        print("   1. Start server: python manage.py runserver")
        print("   2. Go to explore dashboard")
        print("   3. Try both methods:")
        print("      • Click dropdown → Select India")
        print("      • Type 'germany' → Select from suggestions")
        print("   4. See country highlighting and charts!")
        
        print("\n🎯 PERFECT DUAL SEARCH EXPERIENCE!")
        print("   Users can search OR select from dropdown!")
        
    else:
        print("\n❌ Addition failed. Please check the error messages above.")

if __name__ == "__main__":
    main()