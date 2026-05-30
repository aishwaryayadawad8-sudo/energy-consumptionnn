#!/usr/bin/env python3
"""
Hide map initially and show it only after country search
"""

import os

def hide_map_until_search():
    """Hide map initially and show only after search"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🗺️ Hiding map until country search...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the map div and hide it initially
        old_map_div = content.find('<div id="map"></div>')
        if old_map_div != -1:
            # Replace with hidden map
            new_map_div = '<div id="map" style="display: none; height: 500px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); margin-bottom: 30px;"></div>'
            content = content[:old_map_div] + new_map_div + content[old_map_div + len('<div id="map"></div>'):]
            print("✅ Map div hidden initially")
        
        # Update the CSS to remove the map styling since it's now inline
        old_map_css = content.find('#map {')
        if old_map_css != -1:
            # Find the end of the CSS rule
            css_end = content.find('}', old_map_css) + 1
            # Remove the CSS rule since we're using inline styles
            content = content[:old_map_css] + content[css_end:]
            print("✅ Removed old map CSS")
        
        # Add a placeholder message where map will appear
        map_placeholder = '''
        <!-- Map Placeholder -->
        <div id="mapPlaceholder" style="
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border: 2px dashed #dee2e6;
            border-radius: 15px;
            padding: 60px 20px;
            text-align: center;
            margin-bottom: 30px;
            color: #6c757d;
        ">
            <i class="fas fa-search" style="font-size: 48px; margin-bottom: 20px; opacity: 0.5;"></i>
            <h4 style="margin-bottom: 10px; color: #495057;">Search for a Country</h4>
            <p style="margin: 0; font-size: 16px;">Enter a country name above to view its location and energy profile on the interactive map</p>
        </div>'''
        
        # Insert placeholder before the map
        map_div_pos = content.find('<div id="map"')
        content = content[:map_div_pos] + map_placeholder + '\n        ' + content[map_div_pos:]
        print("✅ Added map placeholder")
        
        # Update the highlightCountryOnMap function to show the map
        old_highlight_function = content.find('function highlightCountryOnMap(countryName) {')
        if old_highlight_function != -1:
            # Find the start of the function body
            function_start = content.find('{', old_highlight_function) + 1
            
            # Add code to show map and hide placeholder
            show_map_code = '''
            
            // Show map and hide placeholder
            const mapElement = document.getElementById('map');
            const placeholderElement = document.getElementById('mapPlaceholder');
            
            if (mapElement && placeholderElement) {
                mapElement.style.display = 'block';
                placeholderElement.style.display = 'none';
                
                // Initialize map if not already done
                if (!map) {
                    console.log('🗺️ Initializing map for first time...');
                    initializeMap();
                }
            }
            '''
            
            # Insert the code at the beginning of the function
            content = content[:function_start] + show_map_code + content[function_start:]
            print("✅ Updated highlightCountryOnMap to show map")
        
        # Update the initializeMap function to handle delayed initialization
        old_init_function = content.find('function initializeMap() {')
        if old_init_function != -1:
            # Find the function body
            function_start = content.find('{', old_init_function) + 1
            function_end = content.find('function ', old_init_function + 1)
            if function_end == -1:
                function_end = len(content)
            
            # Find the end of the initializeMap function
            brace_count = 0
            pos = function_start
            while pos < function_end:
                if content[pos] == '{':
                    brace_count += 1
                elif content[pos] == '}':
                    brace_count -= 1
                    if brace_count == -1:  # Found the closing brace of the function
                        function_end = pos
                        break
                pos += 1
            
            # New initializeMap function with delayed initialization
            new_init_function = '''function initializeMap() {
            console.log('🗺️ Initializing map...');
            
            try {
                // Only initialize if map element is visible
                const mapElement = document.getElementById('map');
                if (!mapElement || mapElement.style.display === 'none') {
                    console.log('⏳ Map element not visible, skipping initialization');
                    return;
                }
                
                map = L.map('map').setView([20, 0], 2);
                
                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    attribution: '© OpenStreetMap contributors',
                    maxZoom: 18
                }).addTo(map);
                
                console.log('✅ Map initialized successfully');
                
                // Force map to resize after showing
                setTimeout(() => {
                    if (map) {
                        map.invalidateSize();
                    }
                }, 100);
                
            } catch (error) {
                console.error('❌ Map initialization failed:', error);
            }
        }'''
            
            # Replace the function
            content = content[:old_init_function] + new_init_function + content[function_end + 1:]
            print("✅ Updated initializeMap for delayed initialization")
        
        # Update the DOMContentLoaded event to not initialize map immediately
        old_dom_ready = content.find("document.addEventListener('DOMContentLoaded', function() {")
        if old_dom_ready != -1:
            # Find the function body
            function_start = content.find('{', old_dom_ready) + 1
            
            # Find the end of the function
            brace_count = 0
            pos = function_start
            while pos < len(content):
                if content[pos] == '{':
                    brace_count += 1
                elif content[pos] == '}':
                    brace_count -= 1
                    if brace_count == -1:
                        function_end = pos
                        break
                pos += 1
            
            # New DOM ready function without immediate map initialization
            new_dom_ready = '''document.addEventListener('DOMContentLoaded', function() {
            console.log('🚀 Initializing Dashboard...');
            // Don't initialize map immediately - wait for search
            setupSearchFunctionality();
            console.log('✅ Dashboard initialized successfully! Map will load after search.');
        });'''
            
            # Replace the function
            content = content[:old_dom_ready] + new_dom_ready + content[function_end + 1:]
            print("✅ Updated DOM ready to skip initial map loading")
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully updated dashboard to hide map until search!")
        return True
        
    except Exception as e:
        print(f"❌ Error updating dashboard: {e}")
        return False

def main():
    """Main function"""
    print("🗺️ HIDING MAP UNTIL COUNTRY SEARCH")
    print("=" * 60)
    print("   • Map hidden initially")
    print("   • Search placeholder shown instead")
    print("   • Map appears only after country search")
    print("   • Smooth transition and proper initialization")
    print("=" * 60)
    
    success = hide_map_until_search()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ MAP HIDDEN UNTIL SEARCH - COMPLETE!")
        print("=" * 60)
        print("\n🎯 New Behavior:")
        print("   ✅ Page loads with search interface only")
        print("   ✅ Map is hidden initially")
        print("   ✅ Placeholder message shows where map will appear")
        print("   ✅ Map appears when user searches for a country")
        print("   ✅ Country gets highlighted immediately")
        
        print("\n🔄 User Flow:")
        print("   1. 📱 User sees search interface")
        print("   2. 🔍 User types country name (e.g., 'India')")
        print("   3. 🗺️ Map appears with country highlighted")
        print("   4. 📍 Pin marker and popup show country data")
        print("   5. 📊 Charts and metrics display below")
        
        print("\n🎨 Visual Experience:")
        print("   • Clean, focused search interface initially")
        print("   • No overwhelming map on page load")
        print("   • Smooth transition when map appears")
        print("   • Immediate country highlighting after search")
        print("   • Professional, user-friendly workflow")
        
        print("\n🚀 Ready to Test:")
        print("   1. Start server: python manage.py runserver")
        print("   2. Go to explore dashboard")
        print("   3. See clean search interface (no map)")
        print("   4. Search for 'India' → Map appears with highlighting!")
        
        print("\n🎯 PERFECT SEARCH-FIRST EXPERIENCE!")
        
    else:
        print("\n❌ Update failed. Please check the error messages above.")

if __name__ == "__main__":
    main()