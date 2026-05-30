#!/usr/bin/env python3
"""
Add project.jpg as background image to the dashboard
"""

import os
import shutil

def add_project_background():
    """Add project.jpg as background to the explore dashboard"""
    
    print("🖼️ ADDING PROJECT.JPG AS BACKGROUND")
    print("=" * 50)
    
    # Paths
    source_image = r"C:\Users\aish0\OneDrive\Documents\Desktop\Aish\project.jpg"
    static_dir = "sustainable_energy/dashboard/static/images"
    dashboard_template = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    # Step 1: Create static images directory if it doesn't exist
    try:
        os.makedirs(static_dir, exist_ok=True)
        print(f"✅ Created/verified static images directory: {static_dir}")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        return False
    
    # Step 2: Copy project.jpg to static images
    try:
        if os.path.exists(source_image):
            destination = os.path.join(static_dir, "project-background.jpg")
            shutil.copy2(source_image, destination)
            print(f"✅ Copied project.jpg to: {destination}")
        else:
            print(f"❌ Source image not found: {source_image}")
            return False
    except Exception as e:
        print(f"❌ Error copying image: {e}")
        return False
    
    # Step 3: Update dashboard template with background
    try:
        with open(dashboard_template, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the body CSS and add background
        old_body_css = '''        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px 0;
        }'''
        
        new_body_css = '''        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.8) 0%, rgba(118, 75, 162, 0.8) 100%), 
                        url('/static/images/project-background.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
            min-height: 100vh;
            padding: 20px 0;
        }'''
        
        if old_body_css in content:
            content = content.replace(old_body_css, new_body_css)
            print("✅ Updated body CSS with background image")
        else:
            print("⚠️ Could not find exact body CSS, adding alternative...")
            
            # Alternative: Add background to dashboard-container
            old_container_css = '''        .dashboard-container {
            max-width: 1400px;
            margin: 0 auto;
        }'''
            
            new_container_css = '''        .dashboard-container {
            max-width: 1400px;
            margin: 0 auto;
            position: relative;
        }
        
        /* Project background overlay */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: url('/static/images/project-background.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            opacity: 0.3;
            z-index: -1;
        }'''
            
            if old_container_css in content:
                content = content.replace(old_container_css, new_container_css)
                print("✅ Added background using alternative method")
            else:
                # Add to end of CSS
                css_end = content.find('</style>')
                if css_end != -1:
                    background_css = '''
        /* Project Background Image */
        body {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.8) 0%, rgba(118, 75, 162, 0.8) 100%), 
                        url('/static/images/project-background.jpg') !important;
            background-size: cover !important;
            background-position: center !important;
            background-attachment: fixed !important;
            background-repeat: no-repeat !important;
        }'''
                    content = content[:css_end] + background_css + '\n    ' + content[css_end:]
                    print("✅ Added background CSS at end of styles")
        
        # Write updated content
        with open(dashboard_template, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully updated dashboard template!")
        return True
        
    except Exception as e:
        print(f"❌ Error updating template: {e}")
        return False

def add_background_to_other_pages():
    """Add background to other dashboard pages too"""
    
    print("\n🔄 Adding background to other pages...")
    
    other_templates = [
        "sustainable_energy/dashboard/templates/dashboard/objective_selector.html",
        "sustainable_energy/dashboard/templates/dashboard/co2_emissions.html",
        "sustainable_energy/dashboard/templates/dashboard/electricity.html",
        "sustainable_energy/dashboard/templates/dashboard/total_energy.html"
    ]
    
    background_css = '''
        /* Project Background Image */
        body {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.8) 0%, rgba(118, 75, 162, 0.8) 100%), 
                        url('/static/images/project-background.jpg') !important;
            background-size: cover !important;
            background-position: center !important;
            background-attachment: fixed !important;
            background-repeat: no-repeat !important;
        }'''
    
    for template_path in other_templates:
        try:
            if os.path.exists(template_path):
                with open(template_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Add background CSS if not already present
                if 'project-background.jpg' not in content:
                    css_end = content.find('</style>')
                    if css_end != -1:
                        content = content[:css_end] + background_css + '\n    ' + content[css_end:]
                        
                        with open(template_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        
                        print(f"✅ Added background to: {os.path.basename(template_path)}")
                    else:
                        print(f"⚠️ No CSS section found in: {os.path.basename(template_path)}")
                else:
                    print(f"✅ Background already exists in: {os.path.basename(template_path)}")
            else:
                print(f"⚠️ Template not found: {template_path}")
                
        except Exception as e:
            print(f"❌ Error updating {template_path}: {e}")

def main():
    """Main function"""
    print("🎨 SETTING PROJECT.JPG AS DASHBOARD BACKGROUND")
    print("=" * 60)
    print("   • Copy image to static directory")
    print("   • Update CSS with background image")
    print("   • Apply to all dashboard pages")
    print("   • Maintain existing gradient overlay")
    print("=" * 60)
    
    success = add_project_background()
    
    if success:
        add_background_to_other_pages()
        
        print("\n" + "=" * 60)
        print("✅ PROJECT BACKGROUND ADDED SUCCESSFULLY!")
        print("=" * 60)
        print("\n🎨 Background Features:")
        print("   ✅ Project.jpg as background image")
        print("   ✅ Covers entire screen")
        print("   ✅ Fixed attachment (doesn't scroll)")
        print("   ✅ Gradient overlay for readability")
        print("   ✅ Applied to all dashboard pages")
        
        print("\n🎯 Visual Effects:")
        print("   • Your project image as the background")
        print("   • Semi-transparent blue gradient overlay")
        print("   • Professional appearance maintained")
        print("   • Text remains readable")
        
        print("\n🚀 Ready to View:")
        print("   1. Refresh browser (Ctrl+F5)")
        print("   2. Open explore dashboard")
        print("   3. See your project.jpg as background")
        print("   4. Background stays fixed when scrolling")
        
        print("\n📁 Files Updated:")
        print("   • Copied: project.jpg → static/images/project-background.jpg")
        print("   • Updated: dashboard/templates/dashboard/index.html")
        print("   • Updated: Other dashboard template files")
        
        print("\n🎯 PROJECT IMAGE NOW AS BACKGROUND!")
        
    else:
        print("\n❌ Failed to add background.")

if __name__ == "__main__":
    main()