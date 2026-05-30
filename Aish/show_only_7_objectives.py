#!/usr/bin/env python3
"""
Script to show only 7 objectives (excluding Explore Dashboard) in the Country Energy Forecasts section
"""

import os

def remove_explore_dashboard_from_objectives():
    """Remove the 8th objective (Explore Dashboard) from the objectives grid"""
    
    selector_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(selector_path):
        print(f"❌ File not found: {selector_path}")
        return False
    
    try:
        # Read the selector file
        with open(selector_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update the section title to show only 7 objectives
        old_title = '<h2 class="section-title">Country Energy Forecasts - All 8 Objectives</h2>'
        new_title = '<h2 class="section-title">Country Energy Forecasts - All Objectives</h2>'
        
        if old_title in content:
            content = content.replace(old_title, new_title)
            print("✅ Updated section title to remove '8 Objectives'")
        
        # Find and remove the 8th objective (Explore Dashboard)
        obj8_start = content.find('            <!-- Objective 8: Explore Dashboard -->')
        
        if obj8_start != -1:
            # Find the end of the objective card
            obj8_end = content.find('            </div>\n        </div>\n    </div>\n</section>', obj8_start)
            
            if obj8_end != -1:
                # Remove the entire 8th objective
                content = content[:obj8_start] + content[obj8_end:]
                print("✅ Removed Explore Dashboard from objectives grid")
            else:
                # Alternative approach - find the next objective or end of grid
                obj8_end = content.find('            \n            </div>', obj8_start)
                if obj8_end != -1:
                    content = content[:obj8_start] + content[obj8_end:]
                    print("✅ Removed Explore Dashboard from objectives grid (alternative)")
        else:
            print("⚠️ Explore Dashboard objective not found in grid")
        
        # Write the file back
        with open(selector_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully updated {selector_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error removing Explore Dashboard: {e}")
        return False

def main():
    """Main function"""
    print("🎯 Showing Only 7 Objectives in Country Energy Forecasts")
    print("="*70)
    print("   • Removing Explore Dashboard from objectives grid")
    print("   • Keeping Explore Dashboard button on main page")
    print("   • Country Energy Forecasts shows only 7 objectives")
    print()
    
    success = remove_explore_dashboard_from_objectives()
    
    if success:
        print("\n✅ SUCCESS! Country Energy Forecasts now shows 7 objectives!")
        print("\n📋 Objectives in Country Energy Forecasts section:")
        print("   01. Total Energy Consumption")
        print("   02. Electricity Access & Generation")
        print("   03. Renewable Energy Sources")
        print("   04. CO Emissions Analysis")
        print("   05. Country-Specific Forecasts")
        print("   06. Policy Impact Analysis")
        print("   07. Investment Strategy Optimization")
        print("\n🎯 Perfect separation:")
        print("   • Main page: Explore Dashboard button (prominent)")
        print("   • Country Forecasts: 7 specialized objectives")
        print("   • Clean organization and clear purpose")
        print("\n🔄 Refresh browser and test the Country Energy Forecasts!")
    else:
        print("\n❌ Failed to update objectives section.")

if __name__ == "__main__":
    main()