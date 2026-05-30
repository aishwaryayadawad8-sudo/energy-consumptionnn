#!/usr/bin/env python3
"""
Add Country Dropdown Selector to Explore Dashboard
This script adds a dropdown/select option for countries alongside the search functionality
"""

import os

def add_country_dropdown():
    """Add country dropdown selector to the explore dashboard"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if dropdown already exists
        if 'id="countrySelect"' in content:
            print("✅ Country dropdown already exists")
            return True
        
        # Find the search section and add dropdown
        old_search_section = '''        <!-- Search Section -->
        <div class="search-section">
            <h3><i class="fas fa-globe"></i> Country Energy Analysis</h3>
            <div class="row">
                <div class="col-md-8">
                    <div class="search-box">
                        <input type="text" id="countryInput" class="form-control" 
                               placeholder="Enter country name (e.g., United States, China, India...)" 
                               autocomplete="off">
                    </div>
                </div>
                <div class="col-md-4">
                    <button class="btn btn-primary w-100" onclick="searchCountry()">
                        <i class="fas fa-search"></i> Analyze Country
                    </button>
                </div>
            </div>
            <div id="countrySuggestions" class="mt-2"></div>
        </div>'''
        
        new_search_section = '''        <!-- Search Section -->
        <div class="search-section">
            <h3><i class="fas fa-globe"></i> Country Energy Analysis</h3>
            
            <!-- Search Input Row -->
            <div class="row mb-3">
                <div class="col-md-8">
                    <div class="search-box">
                        <input type="text" id="countryInput" class="form-control" 
                               placeholder="Enter country name (e.g., United States, China, India...)" 
                               autocomplete="off">
                    </div>
                </div>
                <div class="col-md-4">
                    <button class="btn btn-primary w-100" onclick="searchCountry()">
                        <i class="fas fa-search"></i> Analyze Country
                    </button>
                </div>
            </div>
            
            <!-- OR Divider -->
            <div class="text-center mb-3">
                <span class="or-divider">OR</span>
            </div>
            
            <!-- Country Dropdown Row -->
            <div class="row">
                <div class="col-md-8">
                    <select id="countrySelect" class="form-select" onchange="selectCountryFromDropdown()">
                        <option value="">Select a country from the list...</option>
                    </select>
                </div>
                <div class="col-md-4">
                    <button class="btn btn-success w-100" onclick="analyzeSelectedCountry()">
                        <i class="fas fa-chart-line"></i> Analyze Selected
                    </button>
                </div>
            </div>
            
            <div id="countrySuggestions" class="mt-2"></div>
        </div>'''
        
        if old_search_section in content:
            content = content.replace(old_search_section, new_search_section)
            print("✅ Added country dropdown to search section")
        else:
            print("⚠️ Could not find search section to update")
            return False
        
        # Add CSS styles for the new elements
        css_styles = '''        .or-divider {
            background: white;
            padding: 0 15px;
            color: #6b7280;
            font-weight: 500;
            position: relative;
        }
        
        .or-divider::before {
            content: '';
            position: absolute;
            top: 50%;
            left: -100px;
            right: calc(100% + 15px);
            height: 1px;
            background: #e5e7eb;
        }
        
        .or-divider::after {
            content: '';
            position: absolute;
            top: 50%;
            right: -100px;
            left: calc(100% + 15px);
            height: 1px;
            background: #e5e7eb;
        }
        
        .form-select {
            border-radius: 50px;
            padding: 15px 25px;
            border: 2px solid #e0e0e0;
            font-size: 1.1rem;
            background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%23343a40' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='m1 6 7 7 7-7'/%3e%3c/svg%3e");
        }
        
        .form-select:focus {
            border-color: var(--secondary-color);
            box-shadow: 0 0 0 0.2rem rgba(52, 152, 219, 0.25);
        }
        
        .btn-success {
            border-radius: 50px;
            padding: 12px 30px;
            font-weight: bold;
            background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
            border: none;
        }
        
        .btn-success:hover {
            background: linear-gradient(135deg, #229954 0%, #27ae60 100%);
            transform: translateY(-1px);
        }'''
        
        # Find the end of the existing CSS and add new styles
        css_end = '''        @media (max-width: 768px) {
            .metric-cards {
                grid-template-columns: 1fr;
            }
            
            .control-buttons {
                justify-content: center;
            }
            
            .country-header {
                flex-direction: column;
                text-align: center;
                gap: 10px;
            }
        }
    </style>'''
        
        new_css_end = '''        @media (max-width: 768px) {
            .metric-cards {
                grid-template-columns: 1fr;
            }
            
            .control-buttons {
                justify-content: center;
            }
            
            .country-header {
                flex-direction: column;
                text-align: center;
                gap: 10px;
            }
            
            .or-divider::before,
            .or-divider::after {
                display: none;
            }
        }
    </style>'''
        
        if css_end in content:
            content = content.replace(css_end, css_styles + '\n        ' + new_css_end)
            print("✅ Added CSS styles for dropdown")
        
        # Add JavaScript functions for dropdown functionality
        js_functions = '''
        function populateCountryDropdown() {
            const select = document.getElementById('countrySelect');
            
            // Clear existing options except the first one
            while (select.children.length > 1) {
                select.removeChild(select.lastChild);
            }
            
            // Add countries to dropdown
            countries.forEach(country => {
                const option = document.createElement('option');
                option.value = country;
                option.textContent = country;
                select.appendChild(option);
            });
            
            console.log(`Populated dropdown with ${countries.length} countries`);
        }
        
        function selectCountryFromDropdown() {
            const select = document.getElementById('countrySelect');
            const selectedCountry = select.value;
            
            if (selectedCountry) {
                // Update the search input to show selected country
                document.getElementById('countryInput').value = selectedCountry;
                console.log(`Selected country from dropdown: ${selectedCountry}`);
            }
        }
        
        function analyzeSelectedCountry() {
            const select = document.getElementById('countrySelect');
            const selectedCountry = select.value;
            
            if (!selectedCountry) {
                alert('Please select a country from the dropdown first.');
                return;
            }
            
            // Update the search input and trigger search
            document.getElementById('countryInput').value = selectedCountry;
            searchCountry();
        }'''
        
        # Find the loadCountries function and update it to populate dropdown
        old_load_countries = '''        function loadCountries() {
            fetch('/api/countries/')
                .then(response => response.json())
                .then(data => {
                    countries = data.countries || [];
                })
                .catch(error => console.error('Error loading countries:', error));
        }'''
        
        new_load_countries = '''        function loadCountries() {
            fetch('/api/countries/')
                .then(response => response.json())
                .then(data => {
                    countries = data.countries || [];
                    // Populate the dropdown after loading countries
                    populateCountryDropdown();
                })
                .catch(error => console.error('Error loading countries:', error));
        }'''
        
        if old_load_countries in content:
            content = content.replace(old_load_countries, new_load_countries)
            print("✅ Updated loadCountries function to populate dropdown")
        
        # Add the new JavaScript functions before the cleanup section
        cleanup_section = '''        // Cleanup on page unload
        window.addEventListener('beforeunload', () => {
            if (realTimeInterval) {
                clearInterval(realTimeInterval);
            }
        });'''
        
        if cleanup_section in content:
            content = content.replace(cleanup_section, js_functions + '\n        ' + cleanup_section)
            print("✅ Added JavaScript functions for dropdown functionality")
        
        # Write the updated content back to the file
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully added country dropdown selector!")
        return True
        
    except Exception as e:
        print(f"❌ Error adding country dropdown: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Adding Country Dropdown Selector...")
    success = add_country_dropdown()
    
    if success:
        print("\n✅ COUNTRY DROPDOWN ADDED SUCCESSFULLY!")
        print("\n📋 Features added:")
        print("1. ✅ Country dropdown/select with all available countries")
        print("2. ✅ 'OR' divider between search and dropdown options")
        print("3. ✅ 'Analyze Selected' button for dropdown selection")
        print("4. ✅ Auto-sync between search input and dropdown selection")
        print("5. ✅ Professional styling with rounded corners and gradients")
        print("6. ✅ Responsive design for mobile devices")
        print("\n🎯 How it works:")
        print("   • Users can either type in the search box OR select from dropdown")
        print("   • Dropdown is populated automatically with all countries")
        print("   • Selecting from dropdown updates the search input")
        print("   • Both methods trigger the same analysis functionality")
        print("\n⚡ Restart your Django server to see the new dropdown!")
    else:
        print("\n❌ Failed to add country dropdown.")