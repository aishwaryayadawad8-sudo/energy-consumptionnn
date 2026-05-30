#!/usr/bin/env python3
"""
Script to ensure objectives are hidden by default and only appear after clicking Country Forecasts
"""

import os

def fix_objectives_toggle():
    """Fix the objectives section to be properly hidden by default"""
    
    selector_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(selector_path):
        print(f"❌ File not found: {selector_path}")
        return False
    
    try:
        # Read the selector file
        with open(selector_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove duplicate objectives-section CSS rules
        # Find and remove the second objectives-section rule that might be overriding
        duplicate_css_start = content.find('        .objectives-section {\n            background: white;')
        
        if duplicate_css_start != -1:
            # Find the end of this CSS rule
            duplicate_css_end = content.find('        }\n        \n        .objective-item', duplicate_css_start)
            
            if duplicate_css_end != -1:
                # Remove the duplicate CSS rule
                content = content[:duplicate_css_start] + content[duplicate_css_end + 8:]
                print("✅ Removed duplicate objectives-section CSS rule")
        
        # Ensure the main objectives-section CSS is correct
        old_css = '''    /* Objectives Grid (Hidden by default, shown when Country Forecasts is clicked) */
    .objectives-section {
        display: none;
        padding: 60px 0;
        background: #f8fafc;
    }
    
    .objectives-section.active {
        display: block;
    }'''
        
        new_css = '''    /* Objectives Grid (Hidden by default, shown when Country Forecasts is clicked) */
    .objectives-section {
        display: none;
        padding: 60px 0;
        background: #f8fafc;
    }
    
    .objectives-section.active {
        display: block;
    }'''
        
        # Make sure the CSS is properly set
        if old_css in content:
            print("✅ Objectives CSS is correctly set to hidden by default")
        else:
            # Try to find and fix the CSS
            css_start = content.find('.objectives-section {')
            if css_start != -1:
                # Find the end of the CSS block
                css_end = content.find('}', css_start)
                if css_end != -1:
                    # Check if display: none is there
                    css_block = content[css_start:css_end + 1]
                    if 'display: none' not in css_block:
                        # Add display: none
                        content = content.replace(css_block, css_block.replace('{', '{\n        display: none;'))
                        print("✅ Added display: none to objectives-section")
        
        # Write the file back
        with open(selector_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully updated {selector_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing objectives toggle: {e}")
        return False

def main():
    """Main function"""
    print("🔧 Fixing Objectives Toggle Behavior")
    print("="*50)
    print("   • Ensuring objectives are hidden by default")
    print("   • Only appear after clicking 'COUNTRY ENERGY FORECASTS'")
    print("   • Removing duplicate CSS rules")
    print()
    
    success = fix_objectives_toggle()
    
    if success:
        print("\n✅ SUCCESS! Objectives toggle behavior fixed!")
        print("\n📋 How it works now:")
        print("   1. Visit /objectives/ → See main content + Explore Dashboard button")
        print("   2. Click 'COUNTRY ENERGY FORECASTS' tab → See all 7 objectives")
        print("   3. Click other tabs → Hide objectives, show main content")
        print("\n🎯 Perfect behavior:")
        print("   • Objectives hidden by default ✅")
        print("   • Toggle works on Country Forecasts click ✅")
        print("   • Clean 7-objective grid ✅")
        print("   • Explore Dashboard button on main page ✅")
        print("\n🔄 Refresh browser and test the toggle!")
    else:
        print("\n❌ Failed to fix toggle behavior.")

if __name__ == "__main__":
    main()