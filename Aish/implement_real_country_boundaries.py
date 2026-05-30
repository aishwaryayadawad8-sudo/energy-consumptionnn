#!/usr/bin/env python3
"""
REAL COUNTRY BOUNDARIES IMPLEMENTATION
=====================================

This script implements real country boundary highlighting using GeoJSON data.
Instead of circular highlights, countries will be highlighted with their actual borders.
"""

import os
import json

def implement_real_country_boundaries():
    """Implement real country boundary highlighting"""
    
    html_file_path = "Aish/sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🗺️ Implementing real country boundaries...")
    print(f"📁 Updating file: {html_file_path}")
    
    # Read the current file
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False
    
    # Find the createScreenshotStyleHighlight function and replace it
    old_function_start = "function createScreenshotStyleHighlight(countryName, coords) {"
    old_function_end = "console.log(`✅ Created pale green highlight for ${countryName}`);\n        }"
    
    start_pos = content.find(old_function_start)
    if start_pos == -1:
        print("❌ Could not find createScreenshotStyleHighlight function")
        return False
    
    end_pos = content.find(old_function_end, start_pos)
    if end_pos == -1:
        print("❌ Could not find end of createScreenshotStyleHighlight function")
        return False
    
    end_pos += len(old_function_end)
    
    # New function that loads real country boundaries
    new_function = '''function createScreenshotStyleHighlight(countryName, coords) {
            // Try to load real country boundaries first
            loadRealCountryBoundaries(countryName, coords);
        }
        
        function loadRealCountryBoundaries(countryName, coords) {
            console.log(`🗺️ Loading real boundaries for ${countryName}...`);
            
            // Try multiple GeoJSON sources for country boundaries
            const geoJsonSources = [
                'https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson',
                'https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson',
                'https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json'
            ];
            
            // Try to load from the first available source
            loadFromGeoJsonSource(countryName, coords, 0, geoJsonSources);
        }
        
        function loadFromGeoJsonSource(countryName, coords, sourceIndex, sources) {
            if (sourceIndex >= sources.length) {
                console.log(`⚠️ All GeoJSON sources failed for ${countryName}, using fallback circle`);
                createFallbackCircleHighlight(countryName, coords);
                return;
            }
            
            const source = sources[sourceIndex];
            console.log(`📡 Trying GeoJSON source ${sourceIndex + 1}/${sources.length}...`);
            
            fetch(source)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP ${response.status}`);
                    }
                    return response.json();
                })
                .then(geoJsonData => {
                    console.log(`✅ Loaded GeoJSON data, searching for ${countryName}...`);
                    
                    // Find the country in the GeoJSON data
                    const countryFeature = findCountryInGeoJson(geoJsonData, countryName);
                    
                    if (countryFeature) {
                        console.log(`✅ Found ${countryName} in GeoJSON data!`);
                        highlightCountryWithRealBoundaries(countryFeature, countryName, coords);
                    } else {
                        console.log(`❌ ${countryName} not found in source ${sourceIndex + 1}, trying next...`);
                        loadFromGeoJsonSource(countryName, coords, sourceIndex + 1, sources);
                    }
                })
                .catch(error => {
                    console.log(`❌ Failed to load from source ${sourceIndex + 1}: ${error.message}`);
                    loadFromGeoJsonSource(countryName, coords, sourceIndex + 1, sources);
                });
        }
        
        function findCountryInGeoJson(geoJsonData, countryName) {
            if (!geoJsonData.features) {
                console.log('❌ No features found in GeoJSON data');
                return null;
            }
            
            console.log(`🔍 Searching through ${geoJsonData.features.length} features...`);
            
            // Create search terms for the country
            const searchTerms = [
                countryName.toLowerCase(),
                countryName.replace(/\s+/g, '').toLowerCase(),
                getCountryAlternativeNames(countryName)
            ].flat();
            
            console.log(`🔍 Search terms: ${searchTerms.join(', ')}`);
            
            for (const feature of geoJsonData.features) {
                const props = feature.properties;
                if (!props) continue;
                
                // Check various property names that might contain country info
                const propertyNames = [
                    'NAME', 'name', 'NAME_EN', 'name_en', 'ADMIN', 'admin', 
                    'NAME_LONG', 'name_long', 'SOVEREIGNT', 'sovereignt',
                    'ISO_A2', 'iso_a2', 'ISO_A3', 'iso_a3', 'ADM0_A3', 'adm0_a3'
                ];
                
                for (const propName of propertyNames) {
                    if (props[propName]) {
                        const propValue = props[propName].toLowerCase();
                        
                        // Check if any search term matches
                        for (const term of searchTerms) {
                            if (propValue === term || propValue.includes(term) || term.includes(propValue)) {
                                console.log(`✅ Found match: ${propName} = "${props[propName]}" matches "${term}"`);
                                return feature;
                            }
                        }
                    }
                }
            }
            
            console.log(`❌ No match found for ${countryName}`);
            return null;
        }
        
        function getCountryAlternativeNames(countryName) {
            // Alternative names for countries that might appear differently in GeoJSON
            const alternatives = {
                'United States': ['usa', 'united states of america', 'us', 'america'],
                'United Kingdom': ['uk', 'great britain', 'britain', 'england'],
                'Russia': ['russian federation', 'ussr'],
                'China': ['peoples republic of china', 'prc'],
                'South Korea': ['korea', 'republic of korea'],
                'North Korea': ['korea', 'democratic peoples republic of korea'],
                'Iran': ['islamic republic of iran'],
                'Syria': ['syrian arab republic'],
                'Venezuela': ['bolivarian republic of venezuela'],
                'Bolivia': ['plurinational state of bolivia'],
                'Tanzania': ['united republic of tanzania'],
                'Congo': ['democratic republic of the congo', 'congo-kinshasa'],
                'Ivory Coast': ['cote divoire'],
                'Myanmar': ['burma'],
                'Czech Republic': ['czechia'],
                'Macedonia': ['north macedonia'],
                'Swaziland': ['eswatini']
            };
            
            return alternatives[countryName] || [countryName.toLowerCase()];
        }
        
        function highlightCountryWithRealBoundaries(feature, countryName, coords) {
            console.log(`🎨 Highlighting ${countryName} with real boundaries...`);
            
            // Create the country layer with green highlighting (like screenshot)
            const countryLayer = L.geoJSON(feature, {
                style: {
                    fillColor: '#dcfce7',     // Pale green fill (like screenshot)
                    weight: 3,                // Border thickness
                    opacity: 1,               // Border opacity
                    color: '#22c55e',         // Green border (like screenshot)
                    dashArray: '',            // Solid line
                    fillOpacity: 0.6          // Fill transparency
                },
                onEachFeature: function(feature, layer) {
                    // Add hover effects
                    layer.on({
                        mouseover: function(e) {
                            const layer = e.target;
                            layer.setStyle({
                                weight: 4,
                                color: '#16a34a',
                                fillOpacity: 0.7
                            });
                        },
                        mouseout: function(e) {
                            countryLayer.resetStyle(e.target);
                        }
                    });
                }
            }).addTo(map);
            
            // Store reference for later removal
            window.currentCountryLayer = countryLayer;
            
            // Zoom to country bounds with padding
            const bounds = countryLayer.getBounds();
            map.fitBounds(bounds, {
                padding: [20, 20],          // Padding around country
                animate: true,
                duration: 2.0,              // Smooth animation
                easeLinearity: 0.25         // Smooth easing
            });
            
            console.log(`✅ Successfully highlighted ${countryName} with real boundaries!`);
        }
        
        function createFallbackCircleHighlight(countryName, coords) {
            console.log(`🔄 Using fallback circle highlight for ${countryName}`);
            
            // Create a circle as fallback when GeoJSON fails
            const radius = getCountryRadius(countryName);
            
            const countryHighlight = L.circle([coords.lat, coords.lng], {
                color: '#22c55e',           // Green border
                fillColor: '#dcfce7',       // Pale green fill
                fillOpacity: 0.6,           // Transparency
                weight: 3,                  // Border thickness
                radius: radius,
                interactive: false
            }).addTo(map);
            
            // Store reference for later removal
            window.currentCountryLayer = countryHighlight;
            
            // Zoom to country
            const zoomLevel = getCountryZoomLevel(countryName);
            map.setView([coords.lat, coords.lng], zoomLevel, {
                animate: true,
                duration: 1.5
            });
            
            console.log(`✅ Created fallback circle highlight for ${countryName}`);
        }'''
    
    # Replace the function
    new_content = content[:start_pos] + new_function + content[end_pos:]
    
    # Write the updated content back to the file
    try:
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ Successfully updated index.html with real country boundaries")
        return True
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False

def add_cors_headers_note():
    """Add note about CORS for GeoJSON loading"""
    print("\n📝 IMPORTANT NOTES:")
    print("=" * 50)
    print("🌐 GeoJSON Loading:")
    print("   - Uses multiple public GeoJSON sources")
    print("   - Falls back to circle if GeoJSON fails")
    print("   - Handles CORS automatically")
    print("\n🗺️ Country Boundary Features:")
    print("   ✓ Real country shapes and borders")
    print("   ✓ Green fill with green border (like screenshot)")
    print("   ✓ Hover effects for interactivity")
    print("   ✓ Smart country name matching")
    print("   ✓ Automatic zoom to country bounds")
    print("\n🔄 Fallback System:")
    print("   - If GeoJSON fails → Circle highlight")
    print("   - Multiple GeoJSON sources for reliability")
    print("   - Alternative country names for better matching")

def main():
    """Main function to implement real country boundaries"""
    print("🗺️ IMPLEMENTING REAL COUNTRY BOUNDARIES")
    print("=" * 60)
    
    success = implement_real_country_boundaries()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ REAL COUNTRY BOUNDARIES IMPLEMENTED!")
        print("=" * 60)
        print("\n🎯 Features implemented:")
        print("   ✓ Real country shapes using GeoJSON data")
        print("   ✓ Green border and pale green fill (like screenshot)")
        print("   ✓ Multiple GeoJSON sources for reliability")
        print("   ✓ Smart country name matching")
        print("   ✓ Automatic zoom to country bounds")
        print("   ✓ Hover effects for interactivity")
        print("   ✓ Fallback to circle if GeoJSON fails")
        
        add_cors_headers_note()
        
        print("\n🧪 To test:")
        print("   1. Start Django server: python manage.py runserver")
        print("   2. Go to: http://127.0.0.1:8000/explore/")
        print("   3. Search for 'India' - should show real India borders")
        print("   4. Try other countries like 'Germany', 'Brazil', 'Japan'")
        print("   5. Should see actual country shapes, not circles")
        print("\n🔄 Clear browser cache with Ctrl+F5 after testing")
    else:
        print("\n❌ IMPLEMENTATION FAILED")
        print("Please check the error messages above")

if __name__ == "__main__":
    main()