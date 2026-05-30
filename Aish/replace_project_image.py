#!/usr/bin/env python3
"""
Helper script to replace project.jpg image
"""

import os
import shutil
from pathlib import Path

def replace_project_image():
    """Guide user to replace project.jpg image"""
    
    project_image_path = r"C:\Users\aish0\OneDrive\Documents\Desktop\Aish\project.jpg"
    
    print("🖼️ PROJECT IMAGE REPLACEMENT GUIDE")
    print("=" * 50)
    
    # Check if the current image exists
    if os.path.exists(project_image_path):
        print(f"✅ Current image found at: {project_image_path}")
        
        # Get file info
        file_size = os.path.getsize(project_image_path)
        file_size_kb = file_size / 1024
        
        print(f"📊 Current image info:")
        print(f"   • Size: {file_size_kb:.1f} KB")
        print(f"   • Path: {project_image_path}")
        
    else:
        print(f"❌ No image found at: {project_image_path}")
    
    print(f"\n🔄 How to replace the image:")
    print("=" * 30)
    print("1. 📁 Navigate to: C:\\Users\\aish0\\OneDrive\\Documents\\Desktop\\Aish\\")
    print("2. 🖼️ Find your new image file")
    print("3. ✏️ Rename your new image to: project.jpg")
    print("4. 📋 Copy the new project.jpg")
    print("5. 📂 Paste it in the Aish folder")
    print("6. ✅ Choose 'Replace' when prompted")
    
    print(f"\n💡 Alternative method:")
    print("=" * 20)
    print("1. 🖱️ Right-click on the old project.jpg")
    print("2. 🗑️ Delete it")
    print("3. 📋 Copy your new image to the folder")
    print("4. ✏️ Rename it to: project.jpg")
    
    print(f"\n📋 Image requirements:")
    print("=" * 25)
    print("• 📏 Format: JPG/JPEG")
    print("• 📐 Size: Any size (will be displayed as-is)")
    print("• 📝 Name: Must be exactly 'project.jpg'")
    print("• 📍 Location: Must be in Aish folder")
    
    print(f"\n🎯 If you want to use it in the dashboard:")
    print("=" * 45)
    print("We can help you add it to the web interface!")
    print("Just let us know where you want it to appear.")
    
    return True

def check_image_formats():
    """Check what image files are in the directory"""
    
    aish_folder = r"C:\Users\aish0\OneDrive\Documents\Desktop\Aish"
    
    print(f"\n🔍 Checking for images in Aish folder:")
    print("=" * 40)
    
    image_extensions = ['.jpg', '.jpeg', '.png', '.webp', '.gif', '.bmp']
    found_images = []
    
    try:
        for file in os.listdir(aish_folder):
            file_path = os.path.join(aish_folder, file)
            if os.path.isfile(file_path):
                _, ext = os.path.splitext(file.lower())
                if ext in image_extensions:
                    file_size = os.path.getsize(file_path)
                    file_size_kb = file_size / 1024
                    found_images.append((file, file_size_kb))
        
        if found_images:
            print("📸 Found these images:")
            for img_name, size_kb in found_images:
                print(f"   • {img_name} ({size_kb:.1f} KB)")
        else:
            print("❌ No image files found")
            
    except Exception as e:
        print(f"❌ Error checking folder: {e}")
    
    return found_images

def main():
    """Main function"""
    replace_project_image()
    check_image_formats()
    
    print(f"\n" + "🎯" * 20)
    print("🎯 READY TO REPLACE PROJECT IMAGE! 🎯")
    print("🎯" * 20)
    
    print(f"\n✅ Next steps:")
    print("1. Find your new image")
    print("2. Rename it to 'project.jpg'")
    print("3. Copy it to the Aish folder")
    print("4. Replace the old one")
    
    print(f"\n💬 Need help adding it to the dashboard?")
    print("Just tell us where you want it to appear!")

if __name__ == "__main__":
    main()