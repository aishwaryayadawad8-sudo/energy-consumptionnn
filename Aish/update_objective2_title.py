#!/usr/bin/env python3
"""
Update Objective 2 title to use proper CO₂ symbol
"""

def update_objective2_title():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Updating Objective 2 title...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the old title with new one
        old_title = "COâ‚‚ Emission Forecasting"
        new_title = "CO₂ Emission Forecasting"
        
        if old_title in content:
            content = content.replace(old_title, new_title)
            
            # Also update the description if it contains the old format
            old_desc = "forecast future COâ‚‚ emission levels"
            new_desc = "forecast future CO₂ emission levels"
            content = content.replace(old_desc, new_desc)
            
            # Update other CO2 references
            content = content.replace("COâ‚‚ emission trend analysis", "CO₂ emission trend analysis")
            content = content.replace("COâ‚‚: ${country.co2_emissions", "CO₂: ${country.co2_emissions")
            content = content.replace("COâ‚‚ Emissions (kt)", "CO₂ Emissions (kt)")
            
            # Write back the updated content
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ Objective 2 title updated successfully!")
            print(f"📝 Changed from: {old_title}")
            print(f"📝 Changed to: {new_title}")
            print("🔄 Please refresh your browser to see changes")
            
        else:
            print(f"❌ Could not find title '{old_title}' in template")
            
    except FileNotFoundError:
        print(f"❌ Template file not found: {template_path}")
    except Exception as e:
        print(f"❌ Error updating title: {e}")

if __name__ == "__main__":
    update_objective2_title()