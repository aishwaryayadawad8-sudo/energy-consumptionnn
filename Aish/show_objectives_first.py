#!/usr/bin/env python3
"""
Script to show objectives first and hide the main content section
"""

import os

def show_objectives_first():
    """Hide main content and show objectives prominently"""
    
    file_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return False
    
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Hide the main content section by default
        old_content_section = '<!-- Content Section -->\n<section class="content-section" id="main-content">'
        new_content_section = '<!-- Content Section (Hidden by default) -->\n<section class="content-section" id="main-content" style="display: none;">'
        
        if old_content_section in content:
            content = content.replace(old_content_section, new_content_section)
            print("✅ Hidden main content section by default")
        else:
            print("⚠️ Content section pattern not found")
        
        # Write the file back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully updated {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating file: {e}")
        return False

def main():
    """Main function"""
    print("🎯 Showing Objectives First")
    print("="*40)
    
    success = show_objectives_first()
    
    if success:
        print("\n✅ SUCCESS!")
        print("   • Objectives section is now shown first")
        print("   • Main content section is hidden")
        print("   • Full board is prominently displayed")
    else:
        print("\n❌ Failed to update.")

if __name__ == "__main__":
    main()