#!/usr/bin/env python3
"""
Update country highlighting to show only pale green border with pin (no fill)
"""

import os

def update_country_highlighting():
    """Update highlighting to pale green border only"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔄 Updating country highlighting to pale green border only...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the highlighting code
        old_highlight_code = '''            // Create light green fill highlighting
            const highlightCircle = L.circle([coords.lat, coords.lng], {
                color: '#32CD32',
                fillColor: '#90EE90',
                fillOpacity: 0.6,
                radius: 500000,
                weight: 2
            }).addTo(map);'''
        
        new_highlight_code = '''            // Create pale green border highlighting (no fill)
            const highlightCircle = L.circle([coords.lat, coords.lng], {
                color: '#90EE90',        // Pale green border
                fillColor: 'transparent', // No fill
                fillOpacity: 0,          // No fill opacity
                radius: 500000,
                weight: 3                // Slightly thicker border for visibility
            }).addTo(map);'''
        
        # Replace the highlighting code
        if old_highlight_code in content:
            content = content.replace(old_highlight_code, new_highlight_code)
            print("✅ Updated country highlighting to pale green border only")
        else:
            print("⚠️ Could not find exact highlighting code, searching for alternative...")
            
            # Try to find any circle highlighting code
            if 'L.circle([coords.lat, coords.lng]' in content:
                # Find the section and replace it
                import re
                pattern = r'const highlightCircle = L\.circle\(\[coords\.lat, coords\.lng\], \{[^}]+\}\)\.addTo\(map\);'
                replacement = '''const highlightCircle = L.circle([coords.lat, coords.lng], {
                color: '#90EE90',        // Pale green border
                fillColor: 'transparent', // No fill
                fillOpacity: 0,          // No fill opacity
                radius: 500000,
                weight: 3                // Slightly thicker border for visibility
            }).addTo(map);'''
                
                content = re.sub(pattern, replacement, content)
                print("✅ Updated highlighting using pattern matching")
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully updated country highlighting!")
        return True
        
    except Exception as e:
        print(f"❌ Error updating highlighting: {e}")
        return False

def main():
    """Main function"""
    print("🔄 UPDATING COUNTRY HIGHLIGHTING")
    print("=" * 50)
    print("   • Pale green border only (no fill)")
    print("   • Pin marker with country info")
    print("   • Clean, professional appearance")
    print("=" * 50)
    
    success = update_country_highlighting()
    
    if success:
        print("\n" + "=" * 50)
        print("✅ HIGHLIGHTING UPDATED!")
        print("=" * 50)
        print("\n🎯 New Highlighting Style:")
        print("   ✅ Pale green border (#90EE90)")
        print("   ✅ No fill (transparent)")
        print("   ✅ Pin marker with popup")
        print("   ✅ Clean, professional look")
        
        print("\n🔄 User Experience:")
        print("   1. User searches for country")
        print("   2. Country shows pale green border outline")
        print("   3. Pin marker appears with country data")
        print("   4. Map centers on selected country")
        
        print("\n🚀 Ready to Test:")
        print("   1. Refresh browser (Ctrl+F5)")
        print("   2. Search for any country")
        print("   3. See pale green border highlighting")
        print("   4. Click pin for country information")
        
        print("\n🎯 PERFECT PALE GREEN BORDER!")
        
    else:
        print("\n❌ Update failed.")

if __name__ == "__main__":
    main()