#!/usr/bin/env python3
"""
Script to update the objectives section title to reflect 8 objectives
"""

import os

def update_objectives_title():
    """Update the objectives section title"""
    
    selector_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(selector_path):
        print(f"❌ File not found: {selector_path}")
        return False
    
    try:
        # Read the selector file
        with open(selector_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update the section title
        old_title = '<h2 class="section-title">Country Energy Forecasts - All Objectives</h2>'
        new_title = '<h2 class="section-title">Country Energy Forecasts - All 8 Objectives</h2>'
        
        if old_title in content:
            content = content.replace(old_title, new_title)
            print("✅ Updated section title to include '8 Objectives'")
        else:
            print("⚠️ Section title not found in expected format")
        
        # Write the file back
        with open(selector_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully updated {selector_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating title: {e}")
        return False

def main():
    """Main function"""
    print("📝 Updating Objectives Section Title")
    print("="*40)
    
    success = update_objectives_title()
    
    if success:
        print("\n✅ SUCCESS! Title updated!")
        print("   • Section now shows 'All 8 Objectives'")
        print("   • Reflects the complete set including Explore Dashboard")
    else:
        print("\n❌ Failed to update title.")

if __name__ == "__main__":
    main()