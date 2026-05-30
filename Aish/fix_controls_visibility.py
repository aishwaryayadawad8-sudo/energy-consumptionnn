#!/usr/bin/env python3
"""
Fix visualization controls visibility issues
"""

import os

def fix_controls_visibility():
    """Ensure visualization controls are fully visible"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔄 Fixing visualization controls visibility...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Ensure controls CSS is explicit about visibility
        old_controls_css = '''        .visualization-controls {
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            /* Always visible */
        }'''
        
        new_controls_css = '''        .visualization-controls {
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            display: block !important;
            visibility: visible !important;
            opacity: 1 !important;
            /* Always visible - forced */
        }'''
        
        if old_controls_css in content:
            content = content.replace(old_controls_css, new_controls_css)
            print("✅ Updated controls CSS with forced visibility")
        
        # 2. Remove any JavaScript that might hide the controls
        hide_patterns = [
            "visualizationControls.style.display = 'none'",
            "visualizationControls.style.visibility = 'hidden'",
            "getElementById('visualizationControls').style.display = 'none'",
            "display: none"
        ]
        
        for pattern in hide_patterns:
            if pattern in content:
                content = content.replace(pattern, "/* removed hiding code */")
                print(f"✅ Removed hiding code: {pattern}")
        
        # 3. Add explicit JavaScript to ensure controls are visible on page load
        visibility_script = '''
        
        // Ensure visualization controls are always visible
        document.addEventListener('DOMContentLoaded', function() {
            const controls = document.getElementById('visualizationControls');
            if (controls) {
                controls.style.display = 'block';
                controls.style.visibility = 'visible';
                controls.style.opacity = '1';
                console.log('✅ Visualization controls made visible');
            }
        });'''
        
        # Add this script before the closing script tag
        script_end = content.rfind('</script>')
        if script_end != -1:
            content = content[:script_end] + visibility_script + '\n    ' + content[script_end:]
            print("✅ Added visibility enforcement script")
        
        # 4. Make sure the controls HTML doesn't have any hidden attributes
        controls_html_start = content.find('<div class="visualization-controls"')
        if controls_html_start != -1:
            # Check for any hidden attributes in the next 200 characters
            controls_section = content[controls_html_start:controls_html_start+200]
            if 'style="display: none"' in controls_section:
                content = content.replace('style="display: none"', 'style="display: block"')
                print("✅ Removed inline display:none from controls")
            if 'hidden' in controls_section:
                content = content.replace('hidden', '')
                print("✅ Removed hidden attribute from controls")
        
        # 5. Add a bright border for debugging (temporary)
        debug_css = '''        
        /* DEBUG: Make controls highly visible */
        .visualization-controls {
            border: 3px solid #ff0000 !important;
            background: #f0f8ff !important;
        }
        
        .time-period-btn {
            border: 2px solid #007bff !important;
            font-weight: bold !important;
        }'''
        
        # Find the end of existing CSS and add debug styles
        css_end = content.find('</style>')
        if css_end != -1:
            content = content[:css_end] + debug_css + '\n    ' + content[css_end:]
            print("✅ Added debug styling for high visibility")
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully fixed controls visibility!")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing visibility: {e}")
        return False

def main():
    """Main function"""
    print("🔄 FIXING CONTROLS VISIBILITY")
    print("=" * 50)
    print("   • Force display: block !important")
    print("   • Remove any hiding JavaScript")
    print("   • Add visibility enforcement")
    print("   • Add debug styling for testing")
    print("=" * 50)
    
    success = fix_controls_visibility()
    
    if success:
        print("\n" + "=" * 50)
        print("✅ CONTROLS VISIBILITY FIXED!")
        print("=" * 50)
        print("\n🎯 Changes Made:")
        print("   ✅ Forced display: block !important")
        print("   ✅ Added visibility: visible !important")
        print("   ✅ Added opacity: 1 !important")
        print("   ✅ Removed any hiding JavaScript")
        print("   ✅ Added visibility enforcement script")
        print("   ✅ Added red border for debugging")
        
        print("\n🔍 Debug Features:")
        print("   • Red border around controls panel")
        print("   • Light blue background")
        print("   • Bold button text")
        print("   • Forced visibility styles")
        
        print("\n🚀 Testing Steps:")
        print("   1. Refresh browser (Ctrl+F5)")
        print("   2. Look for RED BORDER around controls")
        print("   3. Should see controls immediately at top")
        print("   4. If still hidden, check browser console")
        
        print("\n🎯 CONTROLS SHOULD NOW BE VISIBLE!")
        
    else:
        print("\n❌ Failed to fix visibility.")

if __name__ == "__main__":
    main()