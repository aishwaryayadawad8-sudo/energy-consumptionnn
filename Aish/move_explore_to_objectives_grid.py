#!/usr/bin/env python3
"""
Script to remove Explore Dashboard from navigation tabs and add it as 8th objective in the grid
"""

import os

def remove_explore_from_nav():
    """Remove EXPLORE DASHBOARD from navigation tabs"""
    
    selector_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(selector_path):
        print(f"❌ File not found: {selector_path}")
        return False
    
    try:
        # Read the selector file
        with open(selector_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove the entire EXPLORE DASHBOARD tab
        explore_tab = '''        <a href="/" class="nav-tab">
            <div class="nav-icon"><i class="fas fa-chart-line"></i></div>
            <span>EXPLORE DASHBOARD</span>
        </a>'''
        
        if explore_tab in content:
            content = content.replace(explore_tab, '')
            print("✅ Removed EXPLORE DASHBOARD from navigation tabs")
        else:
            print("⚠️ EXPLORE DASHBOARD tab not found in expected format")
        
        # Write the file back
        with open(selector_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully updated {selector_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating selector: {e}")
        return False

def add_explore_to_objectives_grid():
    """Add Explore Dashboard as 8th objective card in the objectives grid"""
    
    selector_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(selector_path):
        print(f"❌ File not found: {selector_path}")
        return False
    
    try:
        # Read the selector file
        with open(selector_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the end of the objectives grid (before the closing </div>)
        grid_end = content.find('            </div>\n        </div>\n    </div>\n</section>')
        
        if grid_end != -1:
            # Add the 8th objective card for Explore Dashboard
            explore_card = '''            
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
                    Interactive country energy analysis with search functionality, world map visualization, and comprehensive energy profiles for 128+ countries.
                </p>
                <a href="/" class="objective-btn">
                    View Analysis
                </a>
            </div>
'''
            
            # Insert the new card before the closing div
            content = content[:grid_end] + explore_card + content[grid_end:]
            print("✅ Added Explore Dashboard as 8th objective card")
        else:
            print("⚠️ Could not find objectives grid end position")
        
        # Write the file back
        with open(selector_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully updated {selector_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error adding explore card: {e}")
        return False

def main():
    """Main function"""
    print("🔄 Moving Explore Dashboard to Objectives Grid")
    print("="*60)
    print("   • Removing from navigation tabs")
    print("   • Adding as 8th objective card")
    print()
    
    success1 = remove_explore_from_nav()
    success2 = add_explore_to_objectives_grid()
    
    if success1 and success2:
        print("\n✅ SUCCESS! Explore Dashboard moved to objectives grid!")
        print("\n📋 New Structure:")
        print("   • Navigation tabs: 5 tabs (Total Energy, Electricity, etc.)")
        print("   • Objectives grid: 8 cards including Explore Dashboard")
        print("   • Explore Dashboard: Available as objective #8")
        print("\n🎯 User Flow:")
        print("   1. Visit /objectives/ (objective selector)")
        print("   2. Click 'COUNTRY ENERGY FORECASTS' tab")
        print("   3. See all 8 objectives including Explore Dashboard")
        print("   4. Click 'View Analysis' on Explore Dashboard card")
        print("\n🔄 Refresh your browser to see the changes!")
    else:
        print("\n❌ Some updates failed. Please check the files manually.")

if __name__ == "__main__":
    main()