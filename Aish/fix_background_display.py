#!/usr/bin/env python3
"""
Script to fix the background display and remove SVG overlay
"""

import os

def fix_background_display():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and completely replace the hero section to remove SVG overlay
    # Look for the hero-bg section that contains the SVG
    hero_bg_start = content.find('.hero-bg {')
    if hero_bg_start != -1:
        # Find the end of the hero-bg CSS block
        brace_count = 0
        pos = hero_bg_start
        while pos < len(content):
            if content[pos] == '{':
                brace_count += 1
            elif content[pos] == '}':
                brace_count -= 1
                if brace_count == 0:
                    hero_bg_end = pos + 1
                    break
            pos += 1
        
        if brace_count == 0:
            # Replace the entire hero-bg section
            new_hero_bg = '''        .hero-bg {
            display: none;
        }'''
            
            content = content[:hero_bg_start] + new_hero_bg + content[hero_bg_end:]
            print("✅ Removed SVG overlay from hero-bg")
        else:
            print("⚠️ Could not find complete hero-bg CSS block")
    
    # Also ensure the hero-section has the correct background
    hero_section_pattern = '''        /* Hero Section with Background */
        .hero-section {
            background: 
                linear-gradient(180deg, 
                    rgba(26, 35, 50, 0.4) 0%, 
                    rgba(36, 52, 71, 0.5) 50%, 
                    rgba(31, 49, 66, 0.6) 100%),
                url('{% static "images/power-grid-bg.jpg" %}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            position: relative;
            height: 400px;
            overflow: hidden;
        }'''
    
    # Check if we need to update the hero section
    if "url('{% static \"images/power-grid-bg.jpg\" %}')" not in content:
        # Find and replace the hero section
        import re
        pattern = r'(\/\* Hero Section with Background \*\/\s+\.hero-section\s*\{[^}]+\})'
        match = re.search(pattern, content, re.DOTALL)
        
        if match:
            content = content.replace(match.group(1), hero_section_pattern)
            print("✅ Updated hero section background")
        else:
            print("⚠️ Could not find hero section to update")
    
    # Write the updated content
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def check_image_file():
    """Check if the background image file exists"""
    image_path = "sustainable_energy/static/images/power-grid-bg.jpg"
    if os.path.exists(image_path):
        print(f"✅ Background image found: {image_path}")
        return True
    else:
        print(f"❌ Background image NOT found: {image_path}")
        print("   Please save your power grid image to this location")
        return False

if __name__ == "__main__":
    print("🔧 Fixing Background Display")
    print("="*60)
    print()
    
    # Check if image file exists
    image_exists = check_image_file()
    
    if fix_background_display():
        print("\n✅ SUCCESS! Background display fixed!")
        print("\n🔧 Changes Made:")
        print("   • Removed SVG overlay that was covering the photo")
        print("   • Ensured photo background is properly configured")
        print("   • Set correct static file path")
        
        if not image_exists:
            print("\n⚠️  IMPORTANT:")
            print("   • Save your power grid image as: sustainable_energy/static/images/power-grid-bg.jpg")
            print("   • The image should be the one with transmission towers and city lights")
            print("   • Recommended size: 1920x400px or larger")
        
        print("\n🔄 Next Steps:")
        if not image_exists:
            print("   1. Save the power grid image to: sustainable_energy/static/images/power-grid-bg.jpg")
            print("   2. Refresh your browser")
        else:
            print("   1. Refresh your browser (Ctrl+F5 for hard refresh)")
            print("   2. Clear browser cache if needed")
        
        print("\n💡 If still showing SVG pattern:")
        print("   • Try hard refresh (Ctrl+F5)")
        print("   • Check browser developer tools for any 404 errors")
        print("   • Ensure image file name is exactly: power-grid-bg.jpg")
        
    else:
        print("\n❌ Failed to fix background display")