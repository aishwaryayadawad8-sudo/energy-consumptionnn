#!/usr/bin/env python3
"""
Create Unified Country Selector
This script combines search and dropdown into one unified interface
"""

import os

def create_unified_country_selector():
    """Replace the dual interface with a single unified country selector"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the entire search section with a unified interface
        old_search_section = '''        <!-- Search Section -->
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
        
        new_search_section = '''        <!-- Search Section -->
        <div class="search-section">
            <h3><i class="fas fa-globe"></i> Country Energy Analysis</h3>
            
            <!-- Unified Country Selector -->
            <div class="row">
                <div class="col-md-8">
                    <div class="unified-selector">
                        <input type="text" id="countryInput" class="form-control unified-input" 
                               placeholder="Type to search or click dropdown arrow to select..." 
                               autocomplete="off">
                        <div class="dropdown-arrow" onclick="toggleCountryDropdown()">
                            <i class="fas fa-chevron-down"></i>
                        </div>
                        <div id="countryDropdown" class="country-dropdown" style="display: none;">
                            <div class="dropdown-search">
                                <input type="text" id="dropdownSearch" class="form-control" 
                                       placeholder="Search countries..." onkeyup="filterCountries()">
                            </div>
                            <div id="countryList" class="country-list">
                                <!-- Countries will be populated here -->
                            </div>
                        </div>
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
        
        if old_search_section in content:
            content = content.replace(old_search_section, new_search_section)
            print("✅ Replaced dual interface with unified country selector")
        else:
            print("⚠️ Could not find search section to replace")
            return False
        
        # Update CSS styles for the unified interface
        old_css = '''        .or-divider {
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
        
        new_css = '''        .unified-selector {
            position: relative;
        }
        
        .unified-input {
            border-radius: 50px;
            padding: 15px 50px 15px 25px;
            border: 2px solid #e0e0e0;
            font-size: 1.1rem;
            background: white;
        }
        
        .unified-input:focus {
            border-color: var(--secondary-color);
            box-shadow: 0 0 0 0.2rem rgba(52, 152, 219, 0.25);
        }
        
        .dropdown-arrow {
            position: absolute;
            right: 15px;
            top: 50%;
            transform: translateY(-50%);
            cursor: pointer;
            color: #6b7280;
            font-size: 1.2rem;
            padding: 5px;
            border-radius: 50%;
            transition: all 0.3s ease;
        }
        
        .dropdown-arrow:hover {
            background: #f3f4f6;
            color: var(--secondary-color);
        }
        
        .dropdown-arrow.active {
            transform: translateY(-50%) rotate(180deg);
            color: var(--secondary-color);
        }
        
        .country-dropdown {
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            border: 2px solid #e0e0e0;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            z-index: 1000;
            max-height: 300px;
            overflow: hidden;
            margin-top: 5px;
        }
        
        .dropdown-search {
            padding: 15px;
            border-bottom: 1px solid #e5e7eb;
        }
        
        .dropdown-search input {
            border-radius: 25px;
            padding: 10px 15px;
            border: 1px solid #e0e0e0;
            font-size: 0.9rem;
        }
        
        .country-list {
            max-height: 200px;
            overflow-y: auto;
        }
        
        .country-item {
            padding: 12px 20px;
            cursor: pointer;
            border-bottom: 1px solid #f3f4f6;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .country-item:hover {
            background: #f8fafc;
            color: var(--secondary-color);
        }
        
        .country-item:last-child {
            border-bottom: none;
        }
        
        .country-flag {
            font-size: 1.2rem;
        }'''
        
        if old_css in content:
            content = content.replace(old_css, new_css)
            print("✅ Updated CSS for unified interface")
        
        # Update JavaScript functions
        old_js_functions = '''
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
        
        new_js_functions = '''
        function populateCountryDropdown() {
            const countryList = document.getElementById('countryList');
            countryList.innerHTML = '';
            
            // Add countries to dropdown list
            countries.forEach(country => {
                const countryItem = document.createElement('div');
                countryItem.className = 'country-item';
                countryItem.innerHTML = `
                    <span class="country-flag">🌍</span>
                    <span>${country}</span>
                `;
                countryItem.onclick = () => selectCountryFromList(country);
                countryList.appendChild(countryItem);
            });
            
            console.log(`Populated dropdown with ${countries.length} countries`);
        }
        
        function toggleCountryDropdown() {
            const dropdown = document.getElementById('countryDropdown');
            const arrow = document.querySelector('.dropdown-arrow');
            
            if (dropdown.style.display === 'none' || dropdown.style.display === '') {
                dropdown.style.display = 'block';
                arrow.classList.add('active');
                // Focus on dropdown search
                document.getElementById('dropdownSearch').focus();
            } else {
                dropdown.style.display = 'none';
                arrow.classList.remove('active');
            }
        }
        
        function selectCountryFromList(country) {
            document.getElementById('countryInput').value = country;
            document.getElementById('countryDropdown').style.display = 'none';
            document.querySelector('.dropdown-arrow').classList.remove('active');
            console.log(`Selected country: ${country}`);
        }
        
        function filterCountries() {
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
        }
        
        // Close dropdown when clicking outside
        document.addEventListener('click', function(event) {
            const selector = document.querySelector('.unified-selector');
            const dropdown = document.getElementById('countryDropdown');
            
            if (selector && !selector.contains(event.target)) {
                dropdown.style.display = 'none';
                document.querySelector('.dropdown-arrow').classList.remove('active');
            }
        });'''
        
        if old_js_functions in content:
            content = content.replace(old_js_functions, new_js_functions)
            print("✅ Updated JavaScript for unified interface")
        
        # Update the mobile CSS
        old_mobile_css = '''            .or-divider::before,
            .or-divider::after {
                display: none;
            }'''
        
        new_mobile_css = '''            .unified-input {
                padding: 12px 40px 12px 20px;
                font-size: 1rem;
            }
            
            .dropdown-arrow {
                right: 12px;
                font-size: 1rem;
            }'''
        
        if old_mobile_css in content:
            content = content.replace(old_mobile_css, new_mobile_css)
            print("✅ Updated mobile CSS")
        
        # Write the updated content back to the file
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully created unified country selector!")
        return True
        
    except Exception as e:
        print(f"❌ Error creating unified selector: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Creating Unified Country Selector...")
    success = create_unified_country_selector()
    
    if success:
        print("\n✅ UNIFIED COUNTRY SELECTOR CREATED!")
        print("\n🎯 New Interface Features:")
        print("1. ✅ Single input field with dual functionality")
        print("2. ✅ Type to search (with autocomplete)")
        print("3. ✅ Click dropdown arrow to see all countries")
        print("4. ✅ Search within dropdown for easy filtering")
        print("5. ✅ Click outside to close dropdown")
        print("6. ✅ Professional design with smooth animations")
        print("\n📱 How to use:")
        print("   • Type country name directly in the input")
        print("   • OR click the dropdown arrow (▼) to see all countries")
        print("   • Search within dropdown to filter countries")
        print("   • Click any country to select it")
        print("   • Click 'Analyze Country' to start analysis")
        print("\n⚡ Restart your Django server to see the unified interface!")
    else:
        print("\n❌ Failed to create unified selector.")