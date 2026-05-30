#!/usr/bin/env python3

"""
Update the dropdown text to reflect the SDG 7 chart functionality
"""

def update_sdg7_dropdown():
    """Update dropdown and instructions for SDG 7 chart"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective4.html"
    
    # Read current template
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update the dropdown option text
    old_dropdown = '''                    <select id="countrySelect" class="form-select country-select">
                        <option value="">-- Show All Countries (Interactive) --</option>
                    </select>'''
    
    new_dropdown = '''                    <select id="countrySelect" class="form-select country-select">
                        <option value="">-- SDG 7: All Countries Chart --</option>
                    </select>'''
    
    content = content.replace(old_dropdown, new_dropdown)
    
    # Update the instructions
    old_instructions = '''                    <small class="text-muted">
                        💡 <strong>Instructions:</strong> Select "Show All Countries" for interactive chart, or choose specific country for detailed analysis, then click "Analyze Country"
                    </small>'''
    
    new_instructions = '''                    <small class="text-muted">
                        💡 <strong>Instructions:</strong> Select "SDG 7: All Countries Chart" for interactive visualization, or choose specific country for detailed analysis, then click "Analyze Country"
                    </small>'''
    
    content = content.replace(old_instructions, new_instructions)
    
    # Update the section description
    old_section_desc = '''            <p class="text-muted">Click "Analyze Country" to load interactive chart with all countries OR detailed analysis for specific country</p>'''
    new_section_desc = '''            <p class="text-muted">Load the SDG 7 interactive chart with all countries OR get detailed analysis for a specific country</p>'''
    
    content = content.replace(old_section_desc, new_section_desc)
    
    # Update the loadAllCountriesHistoricalChart function name display
    old_console_log = '''            console.log('🌍 Loading interactive historical chart for ALL countries...');'''
    new_console_log = '''            console.log('🌍 Loading SDG 7: Access to Electricity Over Time chart...');'''
    
    content = content.replace(old_console_log, new_console_log)
    
    # Update the historical country name text
    old_country_name = '''                'SDG 7: Access to Electricity Over Time (Click legend to show/hide countries)';'''
    new_country_name = '''                'SDG 7: Access to Electricity Over Time - Click legend to show/hide countries';'''
    
    content = content.replace(old_country_name, new_country_name)
    
    # Write the updated template
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Updated dropdown and instructions for SDG 7 chart!")
    print("\n📝 Changes Made:")
    print("   - Dropdown: 'SDG 7: All Countries Chart'")
    print("   - Clear instructions about SDG 7 functionality")
    print("   - Updated console logging messages")
    print("   - Improved user guidance text")
    print("\n🎮 User Experience:")
    print("   1. Select 'SDG 7: All Countries Chart' from dropdown")
    print("   2. Click 'Analyze Country' button")
    print("   3. See the exact chart from your image")
    print("   4. Afghanistan visible by default")
    print("   5. Click legend to show/hide other countries")

if __name__ == "__main__":
    update_sdg7_dropdown()