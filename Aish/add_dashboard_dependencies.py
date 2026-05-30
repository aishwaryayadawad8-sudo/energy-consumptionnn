#!/usr/bin/env python3
"""
Script to add required CSS and JavaScript dependencies for the embedded dashboard
"""

import os

def add_dashboard_dependencies():
    """Add required libraries for the embedded dashboard"""
    
    selector_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(selector_path):
        print(f"❌ File not found: {selector_path}")
        return False
    
    try:
        # Read the selector file
        with open(selector_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add required CSS libraries after the existing CSS links
        css_libraries = '''    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'''
        
        # Find where to insert CSS (after the existing font import)
        font_import = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">'
        
        if font_import in content and css_libraries not in content:
            content = content.replace(font_import, font_import + '\n' + css_libraries)
            print("✅ Added required CSS libraries")
        
        # Add required JavaScript libraries before the existing script
        js_libraries = '''    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js"></script>'''
        
        # Find where to insert JS (before the existing script section)
        script_start = '<script>\n// Handle Country Forecasts tab click'
        
        if script_start in content and js_libraries not in content:
            content = content.replace(script_start, js_libraries + '\n\n' + script_start)
            print("✅ Added required JavaScript libraries")
        
        # Write the file back
        with open(selector_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully updated {selector_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error adding dependencies: {e}")
        return False

def main():
    """Main function"""
    print("📚 Adding Dashboard Dependencies")
    print("="*40)
    
    success = add_dashboard_dependencies()
    
    if success:
        print("\n✅ SUCCESS! Dependencies added!")
        print("   • Bootstrap CSS & JS")
        print("   • Leaflet (for maps)")
        print("   • Chart.js (for charts)")
        print("   • Font Awesome (for icons)")
    else:
        print("\n❌ Failed to add dependencies.")

if __name__ == "__main__":
    main()