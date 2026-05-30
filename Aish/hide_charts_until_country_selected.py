#!/usr/bin/env python3
"""
Hide Charts Until Country Selected
==================================

This script modifies the dashboard so that all charts are hidden initially
and only appear after a user searches/selects a country.
"""

import os

def hide_charts_until_country_selected():
    """Modify dashboard to show charts only after country selection"""
    
    html_file_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("👁️ HIDING CHARTS UNTIL COUNTRY SELECTED")
    print("=" * 50)
    print(f"📁 Updating file: {html_file_path}")
    
    # Read current file
    with open(html_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add CSS to hide charts initially
    css_addition = '''        
        .charts-hidden {
            display: none;
        }
        
        .charts-visible {
            display: block;
        }
        
        .no-country-message {
            text-align: center;
            padding: 60px 20px;
            background: white;
            border-radius: 15px;
            margin-top: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        .no-country-message h3 {
            color: #6c757d;
            margin-bottom: 20px;
        }
        
        .no-country-message p {
            color: #6c757d;
            font-size: 1.1rem;
        }
        
        .no-country-message i {
            font-size: 4rem;
            color: #dee2e6;
            margin-bottom: 20px;
        }'''
    
    # Insert the CSS before the closing </style> tag
    style_end = "</style>"
    if style_end in content:
        content = content.replace(style_end, css_addition + "\n    " + style_end)
        print("✅ Added CSS for hiding/showing charts")
    
    # Modify the results section to be hidden initially
    old_result_section = '''        <!-- Results Section - Always Visible -->
        <div class="result-section" id="resultSection">'''
    
    new_result_section = '''        <!-- Results Section - Hidden Until Country Selected -->
        <div class="result-section charts-hidden" id="resultSection">'''
    
    if old_result_section in content:
        content = content.replace(old_result_section, new_result_section)
        print("✅ Modified results section to be hidden initially")
    
    # Add a message to show when no country is selected
    map_div = '''        <!-- World Map -->
        <div id="map"></div>'''
    
    map_with_message = '''        <!-- World Map -->
        <div id="map"></div>

        <!-- No Country Selected Message -->
        <div class="no-country-message" id="noCountryMessage">
            <i class="fas fa-search"></i>
            <h3>Select a Country to View Analysis</h3>
            <p>Use the search box or dropdown above to select a country and view detailed energy analysis charts.</p>
            <p><strong>Available:</strong> 60+ countries with comprehensive energy data (2000-2030)</p>
        </div>'''
    
    if map_div in content:
        content = content.replace(map_div, map_with_message)
        print("✅ Added no country selected message")
    
    # Remove the automatic sample data loading
    old_load_sample = '''                // Load sample data after a short delay
                setTimeout(() => {
                    console.log('📊 Loading sample data...');
                    loadSampleData();
                }, 1000);'''
    
    new_load_sample = '''                // Charts will be loaded when country is selected
                console.log('📊 Charts ready - waiting for country selection...');'''
    
    if old_load_sample in content:
        content = content.replace(old_load_sample, new_load_sample)
        print("✅ Removed automatic sample data loading")
    
    # Update the analyzeSelectedCountry function to show charts
    old_analyze_function_start = '''        // FIXED COUNTRY ANALYSIS FUNCTION
        function analyzeSelectedCountry() {
            const countryInput = document.getElementById('countryInput');
            const countryDropdown = document.getElementById('countryDropdown');
            
            // Get country name from either input or dropdown
            let countryName = '';
            if (countryInput && countryInput.value.trim()) {
                countryName = countryInput.value.trim();
            } else if (countryDropdown && countryDropdown.value) {
                countryName = countryDropdown.value;
            }
            
            if (!countryName) {
                alert('Please select or search for a country first!');
                return;
            }

            // Check if country exists in our data
            if (!countryCoordinates[countryName]) {
                alert(`Sorry, ${countryName} is not available in our database. Please select from the dropdown.`);
                return;
            }

            currentCountry = countryName;
            console.log(`🔍 Analyzing: ${countryName}`);
            
            // Update title
            const titleElement = document.getElementById('countryTitle');
            if (titleElement) {
                titleElement.textContent = `${countryName} - Energy Analysis Dashboard`;
            }
            
            // Update metric cards with country data
            updateMetricCards(countryName);
            
            // Render country-specific charts
            renderCountryCharts(countryName);
            
            // Highlight country on map
            highlightCountryOnMap(countryName);
            
            // Success message
            console.log(`✅ Successfully loaded analysis for ${countryName}`);
        }'''
    
    new_analyze_function_start = '''        // FIXED COUNTRY ANALYSIS FUNCTION
        function analyzeSelectedCountry() {
            const countryInput = document.getElementById('countryInput');
            const countryDropdown = document.getElementById('countryDropdown');
            
            // Get country name from either input or dropdown
            let countryName = '';
            if (countryInput && countryInput.value.trim()) {
                countryName = countryInput.value.trim();
            } else if (countryDropdown && countryDropdown.value) {
                countryName = countryDropdown.value;
            }
            
            if (!countryName) {
                alert('Please select or search for a country first!');
                return;
            }

            // Check if country exists in our data
            if (!countryCoordinates[countryName]) {
                alert(`Sorry, ${countryName} is not available in our database. Please select from the dropdown.`);
                return;
            }

            currentCountry = countryName;
            console.log(`🔍 Analyzing: ${countryName}`);
            
            // Show the charts section and hide the no-country message
            showChartsSection();
            
            // Update title
            const titleElement = document.getElementById('countryTitle');
            if (titleElement) {
                titleElement.textContent = `${countryName} - Energy Analysis Dashboard`;
            }
            
            // Update metric cards with country data
            updateMetricCards(countryName);
            
            // Render country-specific charts
            renderCountryCharts(countryName);
            
            // Highlight country on map
            highlightCountryOnMap(countryName);
            
            // Success message
            console.log(`✅ Successfully loaded analysis for ${countryName}`);
        }'''
    
    if old_analyze_function_start in content:
        content = content.replace(old_analyze_function_start, new_analyze_function_start)
        print("✅ Updated analyzeSelectedCountry function to show charts")
    
    # Add the showChartsSection function
    show_charts_function = '''        
        function showChartsSection() {
            const resultSection = document.getElementById('resultSection');
            const noCountryMessage = document.getElementById('noCountryMessage');
            
            if (resultSection) {
                resultSection.classList.remove('charts-hidden');
                resultSection.classList.add('charts-visible');
            }
            
            if (noCountryMessage) {
                noCountryMessage.style.display = 'none';
            }
            
            console.log('📊 Charts section is now visible');
        }
        
        function hideChartsSection() {
            const resultSection = document.getElementById('resultSection');
            const noCountryMessage = document.getElementById('noCountryMessage');
            
            if (resultSection) {
                resultSection.classList.remove('charts-visible');
                resultSection.classList.add('charts-hidden');
            }
            
            if (noCountryMessage) {
                noCountryMessage.style.display = 'block';
            }
            
            console.log('📊 Charts section is now hidden');
        }'''
    
    # Insert the function before the setTimePeriod function
    set_time_period_function = "        function setTimePeriod(period) {"
    if set_time_period_function in content:
        content = content.replace(set_time_period_function, show_charts_function + "\n\n" + set_time_period_function)
        print("✅ Added showChartsSection and hideChartsSection functions")
    
    # Write the updated content
    try:
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Successfully modified dashboard to hide charts initially")
        return True
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False

def main():
    """Main function to hide charts until country selected"""
    success = hide_charts_until_country_selected()
    
    if success:
        print("\n" + "=" * 50)
        print("✅ CHARTS NOW HIDDEN UNTIL COUNTRY SELECTED!")
        print("=" * 50)
        
        print("\n👁️ What was changed:")
        print("   ✓ Charts are hidden on initial page load")
        print("   ✓ Added 'Select a Country' message")
        print("   ✓ Charts appear only after country selection")
        print("   ✓ Removed automatic sample data loading")
        print("   ✓ Added show/hide chart functions")
        
        print("\n📊 New behavior:")
        print("   1. Page loads with map and search controls")
        print("   2. Shows 'Select a Country to View Analysis' message")
        print("   3. All 6 charts are hidden initially")
        print("   4. Charts appear when user selects a country")
        print("   5. Charts show country-specific data")
        
        print("\n🧪 To test:")
        print("   1. Go to: http://127.0.0.1:8000/explore/")
        print("   2. Clear cache: Ctrl+F5")
        print("   3. Verify: No charts visible initially")
        print("   4. Verify: Shows 'Select a Country' message")
        print("   5. Select a country (e.g., 'Germany')")
        print("   6. Click 'Analyze' button")
        print("   7. Verify: All 6 charts appear with country data")
        
        print("\n🔄 Clear browser cache with Ctrl+F5")
    else:
        print("\n❌ FAILED TO HIDE CHARTS")

if __name__ == "__main__":
    main()