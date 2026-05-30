#!/usr/bin/env python3
"""
Remove the info text from the search section
"""

import os

def remove_info_text():
    """Remove the info text below the search section"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🗑️ Removing info text from search section...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and remove the info text div
        info_text_start = content.find('<div class="text-muted mt-3">')
        if info_text_start != -1:
            # Find the end of the info text div
            info_text_end = content.find('</div>', info_text_start) + 6
            
            # Remove the entire info text section
            content = content[:info_text_start] + content[info_text_end:]
            print("✅ Removed info text section")
        else:
            print("ℹ️ Info text not found (might already be removed)")
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully removed info text!")
        return True
        
    except Exception as e:
        print(f"❌ Error removing info text: {e}")
        return False

def main():
    """Main function"""
    print("🗑️ REMOVING INFO TEXT")
    print("=" * 40)
    print("   • Removing instructional text")
    print("   • Cleaner interface")
    print("   • Less clutter")
    print("=" * 40)
    
    success = remove_info_text()
    
    if success:
        print("\n" + "=" * 40)
        print("✅ INFO TEXT REMOVED!")
        print("=" * 40)
        print("\n🎨 Cleaner Interface:")
        print("   ✅ No more instructional text")
        print("   ✅ Cleaner, simpler look")
        print("   ✅ Less visual clutter")
        print("   ✅ More professional appearance")
        
        print("\n🔄 What's Left:")
        print("   • Search input box")
        print("   • Country dropdown")
        print("   • Analyze button")
        print("   • Clean 3-column layout")
        
        print("\n🚀 Ready to Test:")
        print("   1. Refresh browser (Ctrl+F5)")
        print("   2. See cleaner interface")
        print("   3. No more info text below")
        
        print("\n🎯 CLEANER INTERFACE ACHIEVED!")
        
    else:
        print("\n❌ Removal failed. Please check the error messages above.")

if __name__ == "__main__":
    main()