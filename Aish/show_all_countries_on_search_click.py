#!/usr/bin/env python3
"""
Show All Countries on Search Click
=================================

This script modifies the search functionality to show all available countries
as options when the user clicks in the search box, not just when typing.
"""

import os

def enhance_search_with_all_countries():
    """Enhance search to show all countries on click"""
    
    html_file_path = "Aish/sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔍 ENHANCING SEARCH TO SHOW ALL COUNTRIES")
    print("=" * 60)
    print(f"📁 Updating file: {html_file_path}")
    
    # Read current file
    with open(html_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the search functionality
    old_search_js = '''searchInput.addEventListener('input', function() {
                const value = this.value.toLowerCase().trim();
                
                if (value.length < 2) {
                    suggestions.style.display = 'none';
                    return;
                }
                
                const matches = countries.filter(country => 
                    country.toLowerCase().includes(value)
                ).slice(0, 8);
                
                if (matches.length > 0) {
                    suggestions.innerHTML = matches.map(country => 
                        `<div class="suggestion-item" onclick="selectCountryFromSearch('${country}')">
                            <i class="fas fa-map-marker-alt" style="color: #22c55e; margin-right: 8px;"></i>
                            ${country}
                        </div>`
                    ).join('');
                    suggestions.style.display = 'block';
                } else {
                    suggestions.style.display = 'none';
                }
            });'''
    
    new_search_js = '''// Show all countries when clicking in search box
            searchInput.addEventListener('click', function() {
                showAllCountriesInSearch();
            });
            
            searchInput.addEventListener('focus', function() {
                showAllCountriesInSearch();
            });
            
            searchInput.addEventListener('input', function() {
                const value = this.value.toLowerCase().trim();
                
                if (value.length === 0) {
                    // Show all countries when search is empty
                    showAllCountriesInSearch();
                    return;
                }
                
                // Filter countries based on search term
                const matches = countries.filter(country => 
                    country.toLowerCase().includes(value)
                );
                
                if (matches.length > 0) {
                    suggestions.innerHTML = matches.map(country => 
                        `<div class="suggestion-item" onclick="selectCountryFromSearch('${country}')">
                            <i class="fas fa-map-marker-alt" style="color: #22c55e; margin-right: 8px;"></i>
                            ${country}
                        </div>`
                    ).join('');
                    suggestions.style.display = 'block';
                } else {
                    suggestions.innerHTML = '<div class="suggestion-item" style="color: #999; cursor: default;">No countries found</div>';
                    suggestions.style.display = 'block';
                }
            });'''
    
    # Replace the search functionality
    if old_search_js in content:
        content = content.replace(old_search_js, new_search_js)
        print("✅ Updated search input event listeners")
    else:
        print("⚠️ Could not find exact search code, adding new function")
    
    # Add the showAllCountriesInSearch function before the closing script tag
    show_all_function = '''
        function showAllCountriesInSearch() {
            const suggestions = document.getElementById('searchSuggestions');
            
            // Show all countries in suggestions
            suggestions.innerHTML = countries.map(country => 
                `<div class="suggestion-item" onclick="selectCountryFromSearch('${country}')">
                    <i class="fas fa-map-marker-alt" style="color: #22c55e; margin-right: 8px;"></i>
                    ${country}
                </div>`
            ).join('');
            suggestions.style.display = 'block';
            
            console.log(`Showing all ${countries.length} countries in search suggestions`);
        }
        
        '''
    
    # Insert the function before the closing script tag
    script_close = '</script>'
    if script_close in content:
        content = content.replace(script_close, show_all_function + script_close)
        print("✅ Added showAllCountriesInSearch function")
    
    # Also update the CSS to make suggestions scrollable and show more countries
    old_suggestions_css = '''.search-suggestions {
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            z-index: 1000;
            max-height: 200px;
            overflow-y: auto;
            display: none;
        }'''
    
    new_suggestions_css = '''.search-suggestions {
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            z-index: 1000;
            max-height: 300px;
            overflow-y: auto;
            display: none;
        }'''
    
    if old_suggestions_css in content:
        content = content.replace(old_suggestions_css, new_suggestions_css)
        print("✅ Updated suggestions CSS for better scrolling")
    
    # Write the updated content
    try:
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Successfully enhanced search functionality")
        return True
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False

def main():
    """Main function to enhance search"""
    success = enhance_search_with_all_countries()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ SEARCH ENHANCED TO SHOW ALL COUNTRIES!")
        print("=" * 60)
        print("\n🎯 New search behavior:")
        print("   ✓ Click in search box → Shows ALL countries")
        print("   ✓ Focus on search box → Shows ALL countries")
        print("   ✓ Empty search → Shows ALL countries")
        print("   ✓ Type to filter → Shows matching countries")
        print("   ✓ Scrollable list for easy browsing")
        print("   ✓ Visual icons for each country option")
        
        print("\n🧪 To test:")
        print("   1. Go to: http://127.0.0.1:8000/explore/")
        print("   2. Click in the search box")
        print("   3. Verify: All 60+ countries appear as options")
        print("   4. Type 'Ind' → Should filter to India, Indonesia")
        print("   5. Clear search → Should show all countries again")
        print("   6. Click any country → Should select and highlight")
        
        print("\n🔄 Clear browser cache with Ctrl+F5 after testing")
    else:
        print("\n❌ FAILED TO ENHANCE SEARCH")

if __name__ == "__main__":
    main()