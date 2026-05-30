#!/usr/bin/env python3
"""
Update the CO₂ Emissions navigation icon to link to the new CO₂ emissions dashboard
"""

def update_co2_navigation():
    print("🔧 Updating CO₂ Emissions navigation link...")
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    try:
        # Read the template file with proper encoding
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update the CO₂ emissions navigation link
        old_link = "{% url 'objective4_dashboard' %}"
        new_link = "{% url 'co2_emissions_dashboard' %}"
        
        if old_link in content and 'fas fa-smog' in content:
            # Replace the objective4_dashboard URL with co2_emissions_dashboard
            content = content.replace(old_link, new_link)
            
            # Write back the updated content
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ Updated CO₂ Emissions navigation link successfully!")
            print("🔗 CO₂ Emissions icon now links to: /co2-emissions/")
            return True
        else:
            print("⚠️ Could not find the CO₂ emissions navigation link to update")
            return False
        
    except Exception as e:
        print(f"❌ Error updating navigation: {e}")
        return False

if __name__ == "__main__":
    update_co2_navigation()