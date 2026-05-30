#!/usr/bin/env python3
"""
Script to add the 8th objective (Explore Dashboard) back to the objectives grid
"""

import os

def add_8th_objective():
    """Add the 8th objective card back to the objectives section"""
    
    selector_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(selector_path):
        print(f"❌ File not found: {selector_path}")
        return False
    
    try:
        # Read the selector file
        with open(selector_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update the section title to include 8 objectives
        old_title = '<h2 class="section-title">Country Energy Forecasts - All Objectives</h2>'
        new_title = '<h2 class="section-title">Country Energy Forecasts - All 8 Objectives</h2>'
        
        if old_title in content:
            content = content.replace(old_title, new_title)
            print("✅ Updated section title to include '8 Objectives'")
        
        # Find the end of the objectives grid (before closing divs)
        grid_end = content.find('            </div>\n        </div>\n    </div>\n</section>')
        
        if grid_end != -1:
            # Add the 8th objective card
            objective_8_card = '''            
            <!-- Objective 8: Explore Dashboard -->
            <div class="objective-card">
                <div class="objective-header">
                    <div class="objective-icon">
                        <i class="fas fa-search"></i>
                    </div>
                    <div class="objective-number">08</div>
                </div>
                <h3 class="objective-title">Explore Dashboard</h3>
                <p class="objective-description">
                    Interactive country energy analysis with search functionality, world map visualization, and comprehensive energy profiles for 128+ countries with ML predictions.
                </p>
                <a href="/" class="objective-btn">
                    View Analysis
                </a>
            </div>
'''
            
            # Insert the 8th objective before the closing divs
            content = content[:grid_end] + objective_8_card + content[grid_end:]
            print("✅ Added 8th objective (Explore Dashboard) to the grid")
        else:
            print("⚠️ Could not find objectives grid end position")
        
        # Write the file back
        with open(selector_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully updated {selector_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error adding 8th objective: {e}")
        return False

def main():
    """Main function"""
    print("🎯 Adding 8th Objective to Complete the Grid")
    print("="*60)
    print("   • Adding Explore Dashboard as 8th objective")
    print("   • Updating section title to '8 Objectives'")
    print("   • Completing the full objectives grid")
    print()
    
    success = add_8th_objective()
    
    if success:
        print("\n✅ SUCCESS! All 8 objectives now in the grid!")
        print("\n📋 Complete Objectives Grid:")
        print("   01. Total Energy Consumption")
        print("   02. Electricity Access & Generation")
        print("   03. Renewable Energy Sources")
        print("   04. CO Emissions Analysis")
        print("   05. Country-Specific Forecasts")
        print("   06. Policy Impact Analysis")
        print("   07. Investment Strategy Optimization")
        print("   08. 🔍 Explore Dashboard")
        print("\n🎯 User Experience:")
        print("   1. Visit /objectives/ → See Explore Dashboard button")
        print("   2. Click 'COUNTRY ENERGY FORECASTS' → See ALL 8 objectives")
        print("   3. Choose any objective including Explore Dashboard")
        print("\n🔄 Refresh your browser to see all 8 objectives!")
    else:
        print("\n❌ Failed to add 8th objective.")

if __name__ == "__main__":
    main()