#!/usr/bin/env python3
"""
Combine search input and dropdown into one unified search bar
"""

import os

def combine_search_into_one_bar():
    """Combine search and dropdown into one unified search bar"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔄 Combining search and dropdown into one bar...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the search section
        old_search_section = content.find('<!-- Search Section -->')
        if old_search_section != -1:
            # Find the end of the search section
            search_end = content.find('</div>', content.find('</div>', old_search_section) + 1) + 6
            
            # New unified search section
            new_search_section = '''<!-- Search Section -->
        <div class="search-section">
            <h3><i class="fas fa-globe"></i> Country Energy Analysis</h3>
            
            <div class="row">
                <!-- Unified Search Bar -->
                <div class="col-md-10">
                    <div class="search-container" style="position: relative;">
                        <input type="text" id="countryInput" class="form-control" 
                               placeholder="Search or select a country..." 
                               autocomplete="off"
                               style="
                                   border-radius: 25px; 
                                   padding: 15px 20px; 
                                   font-size: 16px;
                                   border: 2px solid #e0e0e0;
                                   background: white;
                                   box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                               ">
                        
                        <!-- Dropdown Arrow -->
                        <div class="dropdown-arrow" onclick="toggleCountryDropdown()" style="
                            position: absolute;
                            right: 15px;
                            top: 50%;
                            transform: translateY(-50%);
                            cursor: pointer;
                            color: #666;
                            font-size: 18px;
                            padding: 5px;
                        ">
                            <i class="fas fa-chevron-down" id="dropdownIcon"></i>
                        </div>
                        
                        <!-- Search Suggestions / Country List -->
                        <div id="searchSuggestions" class="search-suggestions" style="
                            position: absolute;
                            top: 100%;
                            left: 0;
                            right: 0;
                            background: white;
                            border: 1px solid #e0e0e0;
                            border-radius: 15px;
                            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
                            z-index: 1000;
                            max-height: 300px;
                            overflow-y: auto;
                            display: none;
                            margin-top: 5px;
                        "></div>
                    </div>
                </div>
                
                <!-- Analyze Button -->
                <div class="col-md-2">
                    <button class="btn btn-primary w-100" onclick="analyzeSelectedCountry()" 
                            style="
                                border-radius: 25px; 
                                padding: 15px 20px; 
                                font-size: 16px;
                                font-weight: 600;
                                background: #007bff;
                                border: none;
                                box-shadow: 0 2px 10px rgba(0,123,255,0.3);
                            ">
                        <i class="fas fa-search"></i> Analyze
                    </button>
                </div>
            </div>
        </div>'''
            
            # Replace the search section
            content = content[:old_search_section] + new_search_section + content[search_end:]
            print("✅ Updated search section with unified search bar")
        
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
            
            # New unified search functionality
            new_setup_search = '''function setupSearchFunctionality() {
            const countryInput = document.getElementById('countryInput');
            const searchSuggestions = document.getElementById('searchSuggestions');
            
            if (!countryInput || !searchSuggestions) return;
            
            // Search input functionality
            countryInput.addEventListener('input', function() {
                const query = this.value.toLowerCase();
                if (query.length === 0) {
                    searchSuggestions.style.display = 'none';
                } else {
                    filterCountries(query);
                }
            });
            
            // Show all countries when clicking on input
            countryInput.addEventListener('focus', function() {
                if (this.value.length === 0) {
                    showAllCountries();
                }
            });
            
            // Hide suggestions when clicking outside
            document.addEventListener('click', function(e) {
                if (!countryInput.contains(e.target) && 
                    !searchSuggestions.contains(e.target) &&
                    !e.target.closest('.dropdown-arrow')) {
                    searchSuggestions.style.display = 'none';
                    updateDropdownIcon(false);
                }
            });
        }'''
            
            # Replace the function
            content = content[:old_setup_search] + new_setup_search + content[function_end:]
            print("✅ Updated setupSearchFunctionality for unified search")
        
        # Add new functions for unified search
        script_end = content.rfind('</script>')
        if script_end != -1:
            unified_search_functions = '''
        
        // Toggle country dropdown
        function toggleCountryDropdown() {
            const searchSuggestions = document.getElementById('searchSuggestions');
            const countryInput = document.getElementById('countryInput');
            
            if (searchSuggestions.style.display === 'none' || !searchSuggestions.style.display) {
                // Show all countries
                showAllCountries();
                countryInput.focus();
                updateDropdownIcon(true);
            } else {
                // Hide suggestions
                searchSuggestions.style.display = 'none';
                updateDropdownIcon(false);
            }
        }
        
        // Update dropdown icon
        function updateDropdownIcon(isOpen) {
            const icon = document.getElementById('dropdownIcon');
            if (icon) {
                icon.className = isOpen ? 'fas fa-chevron-up' : 'fas fa-chevron-down';
            }
        }
        
        // Enhanced showAllCountries for unified search
        function showAllCountries() {
            const searchSuggestions = document.getElementById('searchSuggestions');
            if (!searchSuggestions) return;
            
            searchSuggestions.innerHTML = '';
            searchSuggestions.style.display = 'block';
            updateDropdownIcon(true);
            
            // Add header
            const header = document.createElement('div');
            header.style.cssText = `
                padding: 12px 20px;
                background: #f8f9fa;
                border-bottom: 1px solid #e0e0e0;
                font-weight: 600;
                color: #495057;
                font-size: 14px;
            `;
            header.innerHTML = '<i class="fas fa-globe"></i> Select a Country';
            searchSuggestions.appendChild(header);
            
            // Add countries
            const allCountries = Object.keys(countryCoordinates).sort();
            allCountries.forEach(country => {
                const item = document.createElement('div');
                item.style.cssText = `
                    padding: 12px 20px;
                    cursor: pointer;
                    border-bottom: 1px solid #f0f0f0;
                    transition: all 0.2s ease;
                    display: flex;
                    align-items: center;
                `;
                
                const coords = countryCoordinates[country];
                item.innerHTML = `
                    <div style="flex: 1;">
                        <div style="font-weight: 500; color: #333;">${country}</div>
                        <div style="font-size: 12px; color: #666; margin-top: 2px;">
                            Electricity Access: ${coords.access}%
                        </div>
                    </div>
                `;
                
                item.onmouseover = () => {
                    item.style.backgroundColor = '#f8f9fa';
                    item.style.borderLeft = '4px solid #007bff';
                };
                item.onmouseout = () => {
                    item.style.backgroundColor = 'white';
                    item.style.borderLeft = 'none';
                };
                item.onclick = () => selectCountryFromUnifiedSearch(country);
                searchSuggestions.appendChild(item);
            });
        }
        
        // Enhanced filterCountries for unified search
        function filterCountries(query) {
            const searchSuggestions = document.getElementById('searchSuggestions');
            if (!searchSuggestions) return;
            
            const filtered = Object.keys(countryCoordinates).filter(country => 
                country.toLowerCase().includes(query)
            ).sort();
            
            searchSuggestions.innerHTML = '';
            searchSuggestions.style.display = filtered.length > 0 ? 'block' : 'none';
            updateDropdownIcon(filtered.length > 0);
            
            if (filtered.length > 0) {
                // Add header
                const header = document.createElement('div');
                header.style.cssText = `
                    padding: 12px 20px;
                    background: #f8f9fa;
                    border-bottom: 1px solid #e0e0e0;
                    font-weight: 600;
                    color: #495057;
                    font-size: 14px;
                `;
                header.innerHTML = `<i class="fas fa-search"></i> Found ${filtered.length} countries`;
                searchSuggestions.appendChild(header);
                
                // Add filtered countries
                filtered.forEach(country => {
                    const item = document.createElement('div');
                    item.style.cssText = `
                        padding: 12px 20px;
                        cursor: pointer;
                        border-bottom: 1px solid #f0f0f0;
                        transition: all 0.2s ease;
                        display: flex;
                        align-items: center;
                    `;
                    
                    const coords = countryCoordinates[country];
                    item.innerHTML = `
                        <div style="flex: 1;">
                            <div style="font-weight: 500; color: #333;">${country}</div>
                            <div style="font-size: 12px; color: #666; margin-top: 2px;">
                                Electricity Access: ${coords.access}%
                            </div>
                        </div>
                    `;
                    
                    item.onmouseover = () => {
                        item.style.backgroundColor = '#f8f9fa';
                        item.style.borderLeft = '4px solid #007bff';
                    };
                    item.onmouseout = () => {
                        item.style.backgroundColor = 'white';
                        item.style.borderLeft = 'none';
                    };
                    item.onclick = () => selectCountryFromUnifiedSearch(country);
                    searchSuggestions.appendChild(item);
                });
            }
        }
        
        // Select country from unified search
        function selectCountryFromUnifiedSearch(countryName) {
            const countryInput = document.getElementById('countryInput');
            const searchSuggestions = document.getElementById('searchSuggestions');
            
            if (countryInput) countryInput.value = countryName;
            if (searchSuggestions) {
                searchSuggestions.style.display = 'none';
                updateDropdownIcon(false);
            }
            
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
        }'''
            
            # Insert the unified search functions
            content = content[:script_end] + unified_search_functions + content[script_end:]
            print("✅ Added unified search functions")
        
        # Update existing selectCountry calls to use the new function
        content = content.replace('selectCountryFromSearch(country)', 'selectCountryFromUnifiedSearch(country)')
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully combined search into one unified bar!")
        return True
        
    except Exception as e:
        print(f"❌ Error combining search: {e}")
        return False

def main():
    """Main function"""
    print("🔄 COMBINING SEARCH INTO ONE UNIFIED BAR")
    print("=" * 60)
    print("   • Single search input with dropdown arrow")
    print("   • Type to search or click arrow to browse")
    print("   • Enhanced suggestions with country data")
    print("   • Professional unified design")
    print("=" * 60)
    
    success = combine_search_into_one_bar()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ UNIFIED SEARCH BAR CREATED!")
        print("=" * 60)
        print("\n🎯 New Unified Experience:")
        print("   ✅ Single search input field")
        print("   ✅ Dropdown arrow on the right")
        print("   ✅ Type to search OR click arrow to browse")
        print("   ✅ Enhanced suggestions with country data")
        print("   ✅ Professional rounded design")
        
        print("\n🔄 How It Works:")
        print("   Method 1 - Type to Search:")
        print("   1. Click in search bar")
        print("   2. Type 'india' or any country")
        print("   3. See filtered suggestions with data")
        print("   4. Click on country to select")
        
        print("\n   Method 2 - Browse All Countries:")
        print("   1. Click dropdown arrow (▼)")
        print("   2. See all 128 countries listed")
        print("   3. Scroll through alphabetical list")
        print("   4. Click on any country to select")
        
        print("\n🎨 Visual Design:")
        print("   ┌─────────────────────────────────────┐")
        print("   │  🌍 Country Energy Analysis        │")
        print("   ├─────────────────────────┬───────────┤")
        print("   │ [Search or select...  ▼] │ Analyze │")
        print("   └─────────────────────────┴───────────┘")
        
        print("\n✨ Enhanced Features:")
        print("   • Rounded search bar with shadow")
        print("   • Dropdown arrow that rotates")
        print("   • Country suggestions show electricity data")
        print("   • Header shows number of results")
        print("   • Hover effects with blue accent")
        print("   • Professional typography")
        
        print("\n🚀 Ready to Test:")
        print("   1. Refresh browser (Ctrl+F5)")
        print("   2. See unified search bar")
        print("   3. Try typing 'india'")
        print("   4. Try clicking dropdown arrow")
        print("   5. Select country and analyze!")
        
        print("\n🎯 PERFECT UNIFIED SEARCH EXPERIENCE!")
        
    else:
        print("\n❌ Combination failed. Please check the error messages above.")

if __name__ == "__main__":
    main()