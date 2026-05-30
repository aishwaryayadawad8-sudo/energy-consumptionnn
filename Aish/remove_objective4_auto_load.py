#!/usr/bin/env python3

"""
Remove auto-loading from Objective 4 - chart should only load when user clicks button
"""

def remove_auto_load():
    """Remove auto-loading functionality from Objective 4"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective4.html"
    
    # Read current template
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the auto-load functionality from window.onload
    old_window_onload = '''        // Load model comparison automatically on page load
        window.onload = function() {
            console.log('🚀 [OBJ4] Page loaded, loading model comparison instantly...');
            loadModelComparison();
            
            // Auto-load interactive chart after 2 seconds
            setTimeout(() => {
                console.log('🌍 Auto-loading interactive historical chart...');
                loadAllCountriesHistoricalChart();
            }, 2000);
        };'''
    
    new_window_onload = '''        // Load model comparison automatically on page load
        window.onload = function() {
            console.log('🚀 [OBJ4] Page loaded, loading model comparison instantly...');
            loadModelComparison();
        };'''
    
    content = content.replace(old_window_onload, new_window_onload)
    
    # Update the country selection section to be clearer about user action required
    old_country_section = '''            <div class="row">
                <div class="col-md-8">
                    <select id="countrySelect" class="form-select country-select">
                        <option value="">-- Show All Countries (Interactive) --</option>
                    </select>
                </div>
                <div class="col-md-4">
                    <button class="btn btn-load w-100" onclick="loadCountryData()">
                        <i class="fas fa-chart-line"></i> Load Chart
                    </button>
                </div>
            </div>
            <div class="row mt-2">
                <div class="col-12">
                    <small class="text-muted">
                        💡 <strong>Tip:</strong> Select "Show All Countries" to see interactive chart, or choose specific country for detailed analysis
                    </small>
                </div>
            </div>'''
    
    new_country_section = '''            <div class="row">
                <div class="col-md-8">
                    <select id="countrySelect" class="form-select country-select">
                        <option value="">-- Show All Countries (Interactive) --</option>
                    </select>
                </div>
                <div class="col-md-4">
                    <button class="btn btn-load w-100" onclick="loadCountryData()">
                        <i class="fas fa-chart-line"></i> Analyze Country
                    </button>
                </div>
            </div>
            <div class="row mt-2">
                <div class="col-12">
                    <small class="text-muted">
                        💡 <strong>Instructions:</strong> Select "Show All Countries" for interactive chart, or choose specific country for detailed analysis, then click "Analyze Country"
                    </small>
                </div>
            </div>'''
    
    content = content.replace(old_country_section, new_country_section)
    
    # Update the section description to make it clear user needs to take action
    old_description = '''            <p class="text-muted">Interactive chart with all countries OR detailed analysis for specific country</p>'''
    new_description = '''            <p class="text-muted">Click "Analyze Country" to load interactive chart with all countries OR detailed analysis for specific country</p>'''
    
    content = content.replace(old_description, new_description)
    
    # Write the updated template
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Removed auto-loading from Objective 4!")
    print("\n🎮 New User Flow:")
    print("   1. Page loads → Only model comparison appears")
    print("   2. User selects option from dropdown:")
    print("      - 'Show All Countries' = Interactive chart")
    print("      - Specific country = Detailed analysis")
    print("   3. User clicks 'Analyze Country' button")
    print("   4. Chart loads based on selection")
    print("\n📊 Chart Loading:")
    print("   - No auto-loading")
    print("   - User-triggered only")
    print("   - Clear instructions provided")
    print("   - Interactive chart loads when 'Show All Countries' selected")
    print("   - Detailed analysis loads when specific country selected")

if __name__ == "__main__":
    remove_auto_load()