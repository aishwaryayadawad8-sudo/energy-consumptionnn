#!/usr/bin/env python3
"""
Script to remove the Navigation section from the Explore Dashboard
"""

import os

def remove_navigation_section():
    template_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and remove the Navigation section
    nav_section_start = content.find('        <!-- Navigation to Objectives -->')
    if nav_section_start != -1:
        # Find the end of this section (the closing </div> after the button)
        nav_section_end = content.find('        </div>\n        \n        \n        <!-- Project Objectives -->', nav_section_start)
        if nav_section_end != -1:
            nav_section_end += len('        </div>\n        \n        ')
            # Remove the navigation section
            content = content[:nav_section_start] + content[nav_section_end:]
            print("✅ Removed Navigation section from Explore Dashboard")
        else:
            print("⚠️ Could not find end of navigation section")
    else:
        print("⚠️ Navigation section not found")
    
    # Write the updated content
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("🗑️  Removing Navigation Section from Explore Dashboard")
    print("="*60)
    print("   • Removing 'Navigation' header section")
    print("   • Removing 'View All Objectives' button")
    print("   • Cleaning up the layout")
    print()
    
    if remove_navigation_section():
        print("\n✅ SUCCESS! Navigation section removed!")
        print("\n📋 What was removed:")
        print("   • Navigation header with compass icon")
        print("   • Description text")
        print("   • 'View All Objectives' button")
        print("\n🎯 Explore Dashboard now shows:")
        print("   • Header with title")
        print("   • Project Objectives section")
        print("   • Search functionality")
        print("   • World map")
        print("   • Country analysis results")
        print("\n🔄 Refresh your browser to see the cleaner layout!")
    else:
        print("\n❌ Failed to remove navigation section")