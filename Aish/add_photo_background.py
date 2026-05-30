#!/usr/bin/env python3
"""
Script to add a photographic background image to the hero section
Instructions: Save your image as 'power-grid-bg.jpg' in sustainable_energy/static/images/
"""

import os

def add_photo_background():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    # Create images directory if it doesn't exist
    images_dir = "sustainable_energy/static/images"
    os.makedirs(images_dir, exist_ok=True)
    print(f"✅ Created/verified images directory: {images_dir}")
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the hero section with photo background
    old_hero_section_start = '''        /* Hero Section with Background */
        .hero-section {
            background: 
                linear-gradient(180deg, 
                    rgba(26, 35, 50, 0.95) 0%, 
                    rgba(36, 52, 71, 0.9) 50%, 
                    rgba(31, 49, 66, 0.95) 100%),
                radial-gradient(circle at 30% 40%, rgba(0, 212, 255, 0.1) 0%, transparent 70%),
                radial-gradient(circle at 70% 60%, rgba(0, 212, 255, 0.08) 0%, transparent 70%);
            position: relative;
            height: 400px;
            overflow: hidden;
        }
        
        .hero-bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('data:image/svg+xml,'''
    
    new_hero_section = '''        /* Hero Section with Background */
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
        }
        
        .hero-bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('data:image/svg+xml,'''
    
    if old_hero_section_start in content:
        content = content.replace(old_hero_section_start, new_hero_section)
        print("✅ Updated hero section to use photo background")
    else:
        print("⚠️ Could not find exact hero section pattern")
        print("Trying alternative approach...")
        
        # Try to find just the .hero-section CSS
        import re
        pattern = r'(\/\* Hero Section with Background \*\/\s+\.hero-section\s*\{[^}]+\})'
        match = re.search(pattern, content, re.DOTALL)
        
        if match:
            old_css = match.group(1)
            new_css = '''/* Hero Section with Background */
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
            content = content.replace(old_css, new_css)
            print("✅ Updated hero section using alternative method")
        else:
            print("❌ Could not find hero section CSS")
            return False
    
    # Write the updated content
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("📸 Adding Photographic Background Image")
    print("="*60)
    print()
    print("⚠️  IMPORTANT: Before running this script:")
    print("   1. Save your power grid image as 'power-grid-bg.jpg'")
    print("   2. Place it in: sustainable_energy/static/images/")
    print()
    print("Processing...")
    print()
    
    if add_photo_background():
        print("\n✅ SUCCESS! Photo background configured!")
        print("\n📋 Next Steps:")
        print("   1. Save your image as: sustainable_energy/static/images/power-grid-bg.jpg")
        print("   2. Run: python manage.py collectstatic (if in production)")
        print("   3. Refresh your browser")
        print("\n🎨 Background Features:")
        print("   • Real photographic image")
        print("   • Dark overlay for text readability")
        print("   • Full cover sizing")
        print("   • Centered positioning")
        print("   • Professional appearance")
        print("\n💡 Image Requirements:")
        print("   • Format: JPG, PNG, or WebP")
        print("   • Recommended size: 1920x400px or larger")
        print("   • File name: power-grid-bg.jpg")
        print("   • Location: sustainable_energy/static/images/")
        print("\n🔄 After adding the image file, refresh your browser!")
    else:
        print("\n❌ Failed to configure photo background")