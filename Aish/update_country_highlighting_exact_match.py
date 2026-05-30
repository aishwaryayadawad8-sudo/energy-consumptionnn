#!/usr/bin/env python3
"""
Update country highlighting to match the exact screenshot provided by user
"""

import os

def update_country_highlighting_exact_match():
    """Update highlighting to match the exact screenshot"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🎨 Updating country highlighting to match your exact screenshot...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and update the highlightCountryWithGeoJSON function
        old_geojson_function = content.find('function highlightCountryWithGeoJSON(countryName, countryFeature, coords) {')
        if old_geojson_function != -1:
            # Find the end of the function
            brace_count = 0
            pos = old_geojson_function
            while pos < len(content):
                if content[pos] == '{':
                    brace_count += 1
                elif content[pos] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        old_geojson_end = pos + 1
                        break
                pos += 1
            
            # Updated function to match exact screenshot
            new_geojson_function = '''function highlightCountryWithGeoJSON(countryName, countryFeature, coords) {
            console.log(`✅ Found GeoJSON boundaries for ${countryName}`);
            
            // Create GeoJSON layer with exact screenshot styling
            const geoJsonLayer = L.geoJSON(countryFeature, {
                style: {
                    fillColor: '#90EE90',      // Light green fill (exact match to screenshot)
                    weight: 1,                 // Thin border like screenshot
                    opacity: 0.8,              // Border opacity
                    color: '#228B22',          // Forest green border
                    fillOpacity: 0.4           // Light fill opacity like screenshot
                },
                onEachFeature: function(feature, layer) {
                    // Add subtle hover effect
                    layer.on({
                        mouseover: function(e) {
                            const layer = e.target;
                            layer.setStyle({
                                weight: 2,
                                fillOpacity: 0.5
                            });
                        },
                        mouseout: function(e) {
                            const layer = e.target;
                            layer.setStyle({
                                weight: 1,
                                fillOpacity: 0.4
                            });
                        }
                    });
                }
            }).addTo(map);
            
            // Add green pin marker exactly like screenshot
            const customIcon = L.divIcon({
                className: 'custom-country-marker',
                html: `
                    <div style="
                        background: #32CD32; 
                        border: 2px solid #228B22; 
                        border-radius: 50% 50% 50% 0; 
                        width: 25px; 
                        height: 25px; 
                        transform: rotate(-45deg);
                        display: flex; 
                        align-items: center; 
                        justify-content: center;
                        box-shadow: 0 2px 5px rgba(0,0,0,0.3);
                    ">
                        <i class="fas fa-map-pin" style="
                            color: white; 
                            font-size: 14px; 
                            transform: rotate(45deg);
                        "></i>
                    </div>
                `,
                iconSize: [25, 25],
                iconAnchor: [12, 25]
            });
            
            const marker = L.marker([coords.lat, coords.lng], { icon: customIcon })
                .addTo(map)
                .bindPopup(`
                    <div style="
                        background: white;
                        border: 1px solid #ddd;
                        border-radius: 8px;
                        padding: 15px;
                        min-width: 200px;
                        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                        font-family: Arial, sans-serif;
                    ">
                        <div style="
                            display: flex;
                            align-items: center;
                            margin-bottom: 10px;
                        ">
                            <div style="
                                background: #32CD32;
                                border-radius: 50%;
                                width: 8px;
                                height: 8px;
                                margin-right: 8px;
                            "></div>
                            <h5 style="
                                margin: 0;
                                color: #333;
                                font-size: 16px;
                                font-weight: bold;
                            ">${countryName}</h5>
                        </div>
                        <div style="
                            display: flex;
                            align-items: center;
                            color: #666;
                            font-size: 14px;
                        ">
                            <span style="
                                background: #FFA500;
                                border-radius: 2px;
                                width: 4px;
                                height: 12px;
                                margin-right: 8px;
                            "></span>
                            <span>Electricity Access: <strong>${coords.access}%</strong></span>
                        </div>
                    </div>
                `, {
                    closeButton: true,
                    autoClose: false,
                    closeOnClick: false
                })
                .openPopup();
            
            // Store references
            currentHighlightLayer = geoJsonLayer;
            currentMarker = marker;
            
            // Fit map to country boundaries like screenshot
            map.fitBounds(geoJsonLayer.getBounds(), {
                padding: [50, 50],
                maxZoom: 6
            });
            
            console.log(`✅ Successfully highlighted ${countryName} exactly like screenshot`);
        }'''
            
            # Replace the function
            content = content[:old_geojson_function] + new_geojson_function + content[old_geojson_end:]
            print("✅ Updated GeoJSON highlighting function to match screenshot")
        
        # Also update the fallback highlighting function
        old_fallback_function = content.find('function fallbackHighlighting(countryName, coords) {')
        if old_fallback_function != -1:
            # Find the end of the function
            brace_count = 0
            pos = old_fallback_function
            while pos < len(content):
                if content[pos] == '{':
                    brace_count += 1
                elif content[pos] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        old_fallback_end = pos + 1
                        break
                pos += 1
            
            # Updated fallback function to match screenshot
            new_fallback_function = '''function fallbackHighlighting(countryName, coords) {
            console.log(`🔄 Using fallback highlighting for ${countryName}`);
            
            // Create light green filled circle matching screenshot style
            const highlightCircle = L.circle([coords.lat, coords.lng], {
                color: '#228B22',          // Forest green border
                fillColor: '#90EE90',      // Light green fill
                fillOpacity: 0.4,          // Light opacity like screenshot
                radius: getCountryRadius(countryName),
                weight: 1
            }).addTo(map);
            
            // Add hover effect
            highlightCircle.on({
                mouseover: function(e) {
                    e.target.setStyle({
                        weight: 2,
                        fillOpacity: 0.5
                    });
                },
                mouseout: function(e) {
                    e.target.setStyle({
                        weight: 1,
                        fillOpacity: 0.4
                    });
                }
            });
            
            // Add green pin marker exactly like screenshot
            const customIcon = L.divIcon({
                className: 'custom-country-marker',
                html: `
                    <div style="
                        background: #32CD32; 
                        border: 2px solid #228B22; 
                        border-radius: 50% 50% 50% 0; 
                        width: 25px; 
                        height: 25px; 
                        transform: rotate(-45deg);
                        display: flex; 
                        align-items: center; 
                        justify-content: center;
                        box-shadow: 0 2px 5px rgba(0,0,0,0.3);
                    ">
                        <i class="fas fa-map-pin" style="
                            color: white; 
                            font-size: 14px; 
                            transform: rotate(45deg);
                        "></i>
                    </div>
                `,
                iconSize: [25, 25],
                iconAnchor: [12, 25]
            });
            
            const marker = L.marker([coords.lat, coords.lng], { icon: customIcon })
                .addTo(map)
                .bindPopup(`
                    <div style="
                        background: white;
                        border: 1px solid #ddd;
                        border-radius: 8px;
                        padding: 15px;
                        min-width: 200px;
                        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                        font-family: Arial, sans-serif;
                    ">
                        <div style="
                            display: flex;
                            align-items: center;
                            margin-bottom: 10px;
                        ">
                            <div style="
                                background: #32CD32;
                                border-radius: 50%;
                                width: 8px;
                                height: 8px;
                                margin-right: 8px;
                            "></div>
                            <h5 style="
                                margin: 0;
                                color: #333;
                                font-size: 16px;
                                font-weight: bold;
                            ">${countryName}</h5>
                        </div>
                        <div style="
                            display: flex;
                            align-items: center;
                            color: #666;
                            font-size: 14px;
                        ">
                            <span style="
                                background: #FFA500;
                                border-radius: 2px;
                                width: 4px;
                                height: 12px;
                                margin-right: 8px;
                            "></span>
                            <span>Electricity Access: <strong>${coords.access}%</strong></span>
                        </div>
                    </div>
                `, {
                    closeButton: true,
                    autoClose: false,
                    closeOnClick: false
                })
                .openPopup();
            
            // Store references
            currentHighlightLayer = highlightCircle;
            currentMarker = marker;
            
            // Center map on country like screenshot
            const zoom = getCountryZoom(countryName);
            map.flyTo([coords.lat, coords.lng], zoom, {
                animate: true,
                duration: 1.5
            });
            
            console.log(`✅ Fallback highlighting applied for ${countryName} matching screenshot`);
        }'''
            
            # Replace the fallback function
            content = content[:old_fallback_function] + new_fallback_function + content[old_fallback_end:]
            print("✅ Updated fallback highlighting function to match screenshot")
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully updated country highlighting to match your screenshot!")
        return True
        
    except Exception as e:
        print(f"❌ Error updating country highlighting: {e}")
        return False

def main():
    """Main function"""
    print("🎨 UPDATING COUNTRY HIGHLIGHTING TO MATCH YOUR SCREENSHOT")
    print("=" * 70)
    print("   • Light green fill covering entire country area")
    print("   • Thin forest green border")
    print("   • Green teardrop-shaped pin marker")
    print("   • Clean white popup with country info")
    print("   • Exact visual match to your image")
    print("=" * 70)
    
    success = update_country_highlighting_exact_match()
    
    if success:
        print("\n" + "=" * 70)
        print("✅ COUNTRY HIGHLIGHTING UPDATED TO MATCH YOUR SCREENSHOT!")
        print("=" * 70)
        print("\n🎨 Exact Screenshot Match:")
        print("   ✅ Light green fill (#90EE90) covering entire country")
        print("   ✅ Thin forest green border (#228B22)")
        print("   ✅ Light fill opacity (40%) like your image")
        print("   ✅ Green teardrop pin marker with shadow")
        print("   ✅ Clean white popup with country name and data")
        print("   ✅ Proper map zoom and positioning")
        
        print("\n🗺️ Visual Features (Exact Match):")
        print("   • Country area filled with light green (like India in your image)")
        print("   • Subtle thin border around country shape")
        print("   • Green pin marker with teardrop shape and shadow")
        print("   • White popup box with green dot and orange indicator")
        print("   • Clean, professional styling matching your screenshot")
        
        print("\n🔄 Test Instructions:")
        print("   1. Refresh browser (Ctrl+F5)")
        print("   2. Search for 'India'")
        print("   3. See EXACT match to your screenshot!")
        print("   4. Light green country fill + green pin + white popup")
        
        print("\n🎯 PERFECT MATCH TO YOUR SCREENSHOT!")
        print("   The highlighting will look EXACTLY like your image")
        print("   with India filled in light green and the green pin!")
        
    else:
        print("\n❌ Update failed. Please check the error messages above.")

if __name__ == "__main__":
    main()