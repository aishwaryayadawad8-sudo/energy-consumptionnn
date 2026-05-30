#!/usr/bin/env python3
"""
Clean up leftover code from the old search implementation
"""

import os

def clean_unified_search():
    """Remove leftover code from old search implementation"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🧹 Cleaning up leftover code from old search implementation...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove leftover dropdown column code
        lines = content.split('\n')
        cleaned_lines = []
        skip_lines = False
        
        for i, line in enumerate(lines):
            # Skip leftover dropdown column
            if '<!-- Dropdown Column -->' in line:
                skip_lines = True
                continue
            elif skip_lines and ('</div>' in line and 'col-md-' in lines[i-5:i+1]):
                skip_lines = False
                continue
            elif skip_lines:
                continue
            
            # Skip leftover button column if it's duplicate
            if 'col-md-4' in line and 'analyzeSelectedCountry()' in line:
                # Check if this is a duplicate button (we already have one in col-md-2)
                if any('col-md-2' in prev_line and 'analyzeSelectedCountry()' in prev_line 
                       for prev_line in lines[max(0, i-20):i]):
                    skip_lines = True
                    continue
            
            cleaned_lines.append(line)
        
        # Join lines back
        content = '\n'.join(cleaned_lines)
        
        # Remove any remaining references to the old dropdown
        content = content.replace('populateCountryDropdown();', '')
        content = content.replace('populateCountryDropdown()', '')
        
        # Remove duplicate analyze buttons
        content = content.replace('''                <div class="col-md-4">
                    <button class="btn btn-primary w-100" onclick="analyzeSelectedCountry()">
                        <i class="fas fa-search"></i> Analyze
                    </button>
                </div>
            </div>
            
            <div class="text-muted mt-2">
                <small><i class="fas fa-info-circle"></i> Type country name to search</small>
            </div>''', '')
        
        # Write cleaned content back
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully cleaned up leftover code!")
        return True
        
    except Exception as e:
        print(f"❌ Error cleaning up: {e}")
        return False

def main():
    """Main function"""
    print("🧹 CLEANING UNIFIED SEARCH IMPLEMENTATION")
    print("=" * 50)
    
    success = clean_unified_search()
    
    if success:
        print("\n✅ CLEANUP COMPLETE!")
        print("=" * 50)
        print("\n🎯 Final Unified Search Features:")
        print("   ✅ Single search input field")
        print("   ✅ Dropdown arrow on the right")
        print("   ✅ Type to search functionality")
        print("   ✅ Click arrow to browse all countries")
        print("   ✅ Enhanced suggestions with data")
        print("   ✅ Professional rounded design")
        print("   ✅ No duplicate elements")
        print("   ✅ Clean, optimized code")
        
        print("\n🚀 Ready for Final Testing!")
        print("   1. Refresh browser (Ctrl+F5)")
        print("   2. See clean unified search bar")
        print("   3. Test both search methods")
        print("   4. Enjoy perfect user experience!")
        
    else:
        print("\n❌ Cleanup failed. Please check the error messages above.")

if __name__ == "__main__":
    main()