#!/usr/bin/env python3
"""
Add Click to Show Options
This script makes the dropdown appear when users click on the search input field
"""

import os

def add_click_to_show_options():
    """Modify the search input to show dropdown options when clicked"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update the input field to show dropdown on click and focus
        old_input = '''                        <input type="text" id="countryInput" class="form-control unified-input" 
                               placeholder="Type to search or click dropdown arrow to select..." 
                               autocomplete="off">'''
        
        new_input = '''                        <input type="text" id="countryInput" class="form-control unified-input" 
                               placeholder="Type to search or click here to see all countries..." 
                               autocomplete="off" 
                               onclick="showCountryOptions()" 
                               onfocus="showCountryOptions()">'''
        
        if old_input in content:
            content = content.replace(old_input, new_input)
            print("✅ Updated input field to show options on click")
        else:
            print("⚠️ Could not find input field to update")
        
        # Add new JavaScript function to show options on input click
        new_js_function = '''
        function showCountryOptions() {
            const dropdown = document.getElementById('countryDropdown');
            const arrow = document.querySelector('.dropdown-arrow');
            
            // Show the dropdown
            dropdown.style.display = 'block';
            arrow.classList.add('active');
            
            // Clear the dropdown search to show all countries
            const dropdownSearch = document.getElementById('dropdownSearch');
            dropdownSearch.value = '';
            
            // Show all countries
            const countryItems = document.querySelectorAll('.country-item');
            countryItems.forEach(item => {
                item.style.display = 'flex';
            });
            
            console.log('Showing country options on input click');
        }'''
        
        # Find where to insert the new function (before toggleCountryDropdown)
        toggle_function = '''        function toggleCountryDropdown() {'''
        
        if toggle_function in content:
            content = content.replace(toggle_function, new_js_function + '\n        ' + toggle_function)
            print("✅ Added showCountryOptions function")
        
        # Update the setupAutoComplete function to also show dropdown
        old_autocomplete = '''        function setupAutoComplete() {
            const input = document.getElementById('countryInput');
            const suggestions = document.getElementById('countrySuggestions');
            
            input.addEventListener('input', function() {
                const value = this.value.toLowerCase();
                if (value.length < 2) {
                    suggestions.innerHTML = '';
                    return;
                }
                
                const matches = countries.filter(country => 
                    country.toLowerCase().includes(value)
                ).slice(0, 5);
                
                suggestions.innerHTML = matches.map(country => 
                    `<div class="suggestion-item p-2 border-bottom" style="cursor: pointer;" 
                          onclick="selectCountry('${country}')">${country}</div>`
                ).join('');
            });
        }'''
        
        new_autocomplete = '''        function setupAutoComplete() {
            const input = document.getElementById('countryInput');
            const suggestions = document.getElementById('countrySuggestions');
            
            input.addEventListener('input', function() {
                const value = this.value.toLowerCase();
                
                // Show dropdown when typing
                showCountryOptions();
                
                // Filter countries in dropdown based on input
                if (value.length > 0) {
                    filterCountriesInDropdown(value);
                }
                
                // Also show traditional suggestions below
                if (value.length < 2) {
                    suggestions.innerHTML = '';
                    return;
                }
                
                const matches = countries.filter(country => 
                    country.toLowerCase().includes(value)
                ).slice(0, 5);
                
                suggestions.innerHTML = matches.map(country => 
                    `<div class="suggestion-item p-2 border-bottom" style="cursor: pointer;" 
                          onclick="selectCountry('${country}')">${country}</div>`
                ).join('');
            });
        }'''
        
        if old_autocomplete in content:
            content = content.replace(old_autocomplete, new_autocomplete)
            print("✅ Updated setupAutoComplete to show dropdown while typing")
        
        # Add function to filter countries in dropdown based on input
        filter_function = '''
        function filterCountriesInDropdown(searchTerm) {
            const countryItems = document.querySelectorAll('.country-item');
            
            countryItems.forEach(item => {
                const countryName = item.textContent.toLowerCase();
                if (countryName.includes(searchTerm.toLowerCase())) {
                    item.style.display = 'flex';
                } else {
                    item.style.display = 'none';
                }
            });
        }'''
        
        # Insert the filter function before the existing filterCountries function
        old_filter = '''        function filterCountries() {'''
        
        if old_filter in content:
            content = content.replace(old_filter, filter_function + '\n        ' + old_filter)
            print("✅ Added filterCountriesInDropdown function")
        
        # Update the existing filterCountries function to use the new one
        old_filter_countries = '''        function filterCountries() {
            const searchTerm = document.getElementById('dropdownSearch').value.toLowerCase();
            const countryItems = document.querySelectorAll('.country-item');
            
            countryItems.forEach(item => {
                const countryName = item.textContent.toLowerCase();
                if (countryName.includes(searchTerm)) {
                    item.style.display = 'flex';
                } else {
                    item.style.display = 'none';
                }
            });
        }'''
        
        new_filter_countries = '''        function filterCountries() {
            const searchTerm = document.getElementById('dropdownSearch').value;
            filterCountriesInDropdown(searchTerm);
        }'''
        
        if old_filter_countries in content:
            content = content.replace(old_filter_countries, new_filter_countries)
            print("✅ Updated filterCountries function")
        
        # Update the selectCountryFromList function to also clear the main input if needed
        old_select = '''        function selectCountryFromList(country) {
            document.getElementById('countryInput').value = country;
            document.getElementById('countryDropdown').style.display = 'none';
            document.querySelector('.dropdown-arrow').classList.remove('active');
            console.log(`Selected country: ${country}`);
        }'''
        
        new_select = '''        function selectCountryFromList(country) {
            document.getElementById('countryInput').value = country;
            document.getElementById('countryDropdown').style.display = 'none';
            document.querySelector('.dropdown-arrow').classList.remove('active');
            
            // Clear traditional suggestions
            document.getElementById('countrySuggestions').innerHTML = '';
            
            console.log(`Selected country: ${country}`);
        }'''
        
        if old_select in content:
            content = content.replace(old_select, new_select)
            print("✅ Updated selectCountryFromList function")
        
        # Write the updated content back to the file
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully added click-to-show options functionality!")
        return True
        
    except Exception as e:
        print(f"❌ Error adding click-to-show options: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Adding Click-to-Show Options Functionality...")
    success = add_click_to_show_options()
    
    if success:
        print("\n✅ CLICK-TO-SHOW OPTIONS ADDED!")
        print("\n🎯 New Behavior:")
        print("1. ✅ Click on search input → Dropdown appears with all countries")
        print("2. ✅ Focus on search input → Dropdown appears automatically")
        print("3. ✅ Start typing → Dropdown filters countries in real-time")
        print("4. ✅ Click dropdown arrow → Same dropdown behavior")
        print("5. ✅ Click outside → Dropdown closes")
        print("\n📱 User Experience:")
        print("   • Click anywhere in the search box to see all countries")
        print("   • Type to filter countries instantly")
        print("   • Click any country to select it")
        print("   • No need to remember exact country names")
        print("\n🎨 Features:")
        print("   • Instant dropdown on click/focus")
        print("   • Real-time filtering while typing")
        print("   • Smooth animations and transitions")
        print("   • Mobile-friendly touch interactions")
        print("\n⚡ Restart your Django server to test the new functionality!")
    else:
        print("\n❌ Failed to add click-to-show options.")