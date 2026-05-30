#!/usr/bin/env python3
"""
Script to clean up the objectives section - remove embedded dashboard and keep only 7 objectives
"""

import os

def clean_objectives_section():
    """Remove the embedded dashboard from objectives and keep only 7 objective cards"""
    
    selector_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(selector_path):
        print(f"❌ File not found: {selector_path}")
        return False
    
    try:
        # Read the selector file
        with open(selector_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update the section title back to 7 objectives
        old_title = '<h2 class="section-title">Country Energy Forecasts - All 8 Objectives</h2>'
        new_title = '<h2 class="section-title">Country Energy Forecasts - All Objectives</h2>'
        
        if old_title in content:
            content = content.replace(old_title, new_title)
            print("✅ Updated section title")
        
        # Find and remove the 8th objective (embedded dashboard)
        # Look for the start of objective 8
        obj8_start = content.find('<!-- Objective 8: Full Explore Dashboard -->')
        
        if obj8_start != -1:
            # Find the end of the objective card (look for the next closing div or end of grid)
            obj8_end = content.find('            </div>\n        </div>\n    </div>\n</section>', obj8_start)
            
            if obj8_end != -1:
                # Remove the entire 8th objective
                content = content[:obj8_start] + content[obj8_end:]
                print("✅ Removed embedded dashboard from objectives")
            else:
                print("⚠️ Could not find end of objective 8")
        else:
            print("⚠️ Objective 8 not found")
        
        # Write the file back
        with open(selector_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully updated {selector_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error cleaning objectives: {e}")
        return False

def main():
    """Main function"""
    print("🧹 Cleaning Objectives Section")
    print("="*40)
    print("   • Removing embedded dashboard")
    print("   • Keeping only 7 objective cards")
    print("   • Dashboard accessible via button")
    print()
    
    success = clean_objectives_section()
    
    if success:
        print("\n✅ SUCCESS! Objectives section cleaned!")
        print("\n📋 What's changed:")
        print("   • Removed embedded dashboard from objectives")
        print("   • Now shows only 7 objective cards")
        print("   • Clean, organized objectives grid")
        print("   • Dashboard accessible via 'Launch Explore Dashboard' button")
        print("\n🎯 Perfect structure:")
        print("   • Main page: Explore Dashboard button")
        print("   • Objectives: Clean 7-card grid")
        print("   • Dashboard: Full functionality at /")
    else:
        print("\n❌ Failed to clean objectives section.")

if __name__ == "__main__":
    main()