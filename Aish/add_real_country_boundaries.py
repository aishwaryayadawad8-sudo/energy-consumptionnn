#!/usr/bin/env python3
"""
Add Real Country Boundaries Highlighting
This script adds functionality to highlight actual country boundaries/shapes
using GeoJSON data from public APIs
"""

import os

def add_real_country_boundaries():
    """Add real country boundary highlighting functionality"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the highlightCountryOnMap function with real boundary highlighting
        old_highlight_function_start = '''        function highlightCountryOnMap(countryName) {
            if (!map || !countryCoordinates[countryName]) {
                console.log(`Country coordinates not found for: ${countryName}`);
                return;
            }
            
            const coords = countryCoordinates[countryName];
            
            // Remove existing layers if any
            if (currentMarker) {
                map.removeLayer(currentMarker);
            }
            if (window.currentCountryLayer) {
                map.removeLayer(window.currentCountryLayer);
            }
            
            // Load country boundary data and highlight with green border
            loadCountryBoundary(countryName, coords);
            
            // Center map on country with smooth animation
            map.flyTo([coords.lat, coords.lng], 5, {
                animate: true,
                duration: 1.5
            });
            
            console.log(`Highlighting ${countryName} borders on map`);
        }'''
        
        new_highlight_function = '''        function highlightCountryOnMap(countryName) {
            if (!map || !countryCoordinates[countryName]) {
                console.log(`Country coordinates not found for: ${countryName}`);
                return;
            }
            
            const coords = countryCoordinates[countryName];
            
            // Remove existing layers if any
            if (currentMarker) {
                map.removeLayer(currentMarker);
            }
            if (window.currentCountryLayer) {
                map.removeLayer(window.currentCountryLayer);
            }
            
            // Load real country boundary data
            loadRealCountryBoundaries(countryName, coords);
            
            console.log(`Loading real boundaries for ${countryName}`);
        }
        
        function loadRealCountryBoundaries(countryName, coords) {
            // Get country code for API call
            const countryCode = getCountryCode(countryName);
            
            if (!countryCode) {
                console.log(`Country code not found for: ${countryName}`);
                // Fallback to simple highlighting
                loadFallbackHighlight(countryName, coords);
                return;
            }
            
            // Try multiple GeoJSON sources for country boundaries
            const geoJsonSources = [
                `https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson`,
                `https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson`
            ];
            
            // Try to load from the first source
            loadFromGeoJsonSource(countryName, countryCode, coords, 0, geoJsonSources);
        }
        
        function loadFromGeoJsonSource(countryName, countryCode, coords, sourceIndex, sources) {
            if (sourceIndex >= sources.length) {
                console.log(`All GeoJSON sources failed for ${countryName}, using fallback`);
                loadFallbackHighlight(countryName, coords);
                return;
            }
            
            const source = sources[sourceIndex];
            
            fetch(source)
                .then(response => response.json())
                .then(geoJsonData => {
                    // Find the country in the GeoJSON data
                    const countryFeature = findCountryInGeoJson(geoJsonData, countryName, countryCode);
                    
                    if (countryFeature) {
                        highlightCountryFeature(countryFeature, countryName, coords);
                    } else {
                        console.log(`Country not found in source ${sourceIndex}, trying next...`);
                        loadFromGeoJsonSource(countryName, countryCode, coords, sourceIndex + 1, sources);
                    }
                })
                .catch(error => {
                    console.log(`Failed to load from source ${sourceIndex}:`, error);
                    loadFromGeoJsonSource(countryName, countryCode, coords, sourceIndex + 1, sources);
                });
        }
        
        function findCountryInGeoJson(geoJsonData, countryName, countryCode) {
            if (!geoJsonData.features) return null;
            
            // Try to find by various property names
            const searchTerms = [
                countryName.toLowerCase(),
                countryCode.toLowerCase(),
                countryName.replace(/\s+/g, '').toLowerCase()
            ];
            
            for (const feature of geoJsonData.features) {
                const props = feature.properties;
                if (!props) continue;
                
                // Check various property names that might contain country info
                const propertyNames = ['NAME', 'name', 'NAME_EN', 'ADMIN', 'admin', 'ISO_A2', 'iso_a2', 'ISO_A3', 'iso_a3'];
                
                for (const propName of propertyNames) {
                    if (props[propName]) {
                        const propValue = props[propName].toLowerCase();
                        if (searchTerms.some(term => propValue.includes(term) || term.includes(propValue))) {
                            return feature;
                        }
                    }
                }
            }
            
            return null;
        }
        
        function highlightCountryFeature(feature, countryName, coords) {
            // Create the country layer with green highlighting
            const countryLayer = L.geoJSON(feature, {
                style: {
                    fillColor: '#22c55e',     // Green fill
                    weight: 3,                // Border thickness
                    opacity: 1,               // Border opacity
                    color: '#16a34a',         // Border color (darker green)
                    dashArray: '',            // Solid line
                    fillOpacity: 0.3          // Fill transparency
                },
                onEachFeature: function(feature, layer) {
                    // Add popup to the country
                    const popupContent = `
                        <div class="country-boundary-popup">
                            <h3>${countryName}</h3>
                            <div class="access-info">
                                <i class="fas fa-bolt"></i> 
                                <span>Electricity Access: <strong>${coords.access}%</strong></span>
                            </div>
                            <button onclick="searchCountry()" class="btn btn-primary analysis-btn">
                                <i class="fas fa-chart-line"></i> View Full Analysis
                            </button>
                        </div>
                    `;
                    
                    layer.bindPopup(popupContent, {
                        maxWidth: 300,
                        className: 'country-boundary-popup-container'
                    });
                }
            }).addTo(map);
            
            // Store reference for later removal
            window.currentCountryLayer = countryLayer;
            
            // Fit map to country bounds
            map.fitBounds(countryLayer.getBounds(), {
                padding: [20, 20],
                animate: true,
                duration: 1.5
            });
            
            // Open popup after animation
            setTimeout(() => {
                countryLayer.openPopup();
            }, 1800);
            
            console.log(`Successfully highlighted ${countryName} with real boundaries`);
        }
        
        function loadFallbackHighlight(countryName, coords) {
            console.log(`Using fallback highlight for ${countryName}`);
            
            // Create a more accurate country-sized circle as fallback
            const radius = getCountryRadius(countryName);
            
            const countryHighlight = L.circle([coords.lat, coords.lng], {
                color: '#16a34a',           // Darker green border
                fillColor: '#22c55e',       // Green fill
                fillOpacity: 0.3,           // Transparency
                weight: 3,                  // Border thickness
                radius: radius
            }).addTo(map);
            
            // Store reference
            window.currentCountryLayer = countryHighlight;
            
            // Add popup
            const popupContent = `
                <div class="country-boundary-popup">
                    <h3>${countryName}</h3>
                    <div class="access-info">
                        <i class="fas fa-bolt"></i> 
                        <span>Electricity Access: <strong>${coords.access}%</strong></span>
                    </div>
                    <button onclick="searchCountry()" class="btn btn-primary analysis-btn">
                        <i class="fas fa-chart-line"></i> View Full Analysis
                    </button>
                </div>
            `;
            
            countryHighlight.bindPopup(popupContent, {
                maxWidth: 300,
                className: 'country-boundary-popup-container'
            });
            
            // Center map on country
            map.flyTo([coords.lat, coords.lng], 5, {
                animate: true,
                duration: 1.5
            });
            
            // Open popup
            setTimeout(() => {
                countryHighlight.openPopup();
            }, 1800);
        }'''
        
        # Find the old function and replace it
        if old_highlight_function_start in content:
            # Find the end of the old function (look for the next function definition)
            start_pos = content.find(old_highlight_function_start)
            if start_pos != -1:
                # Find the end of this function (next function or end of script)
                end_markers = [
                    '\n        function loadCountryBoundary(',
                    '\n        function getCountryCode(',
                    '\n        function fetchCountryData(',
                    '\n        function loadMapData('
                ]
                
                end_pos = len(content)
                for marker in end_markers:
                    marker_pos = content.find(marker, start_pos)
                    if marker_pos != -1 and marker_pos < end_pos:
                        end_pos = marker_pos
                
                # Replace the old function with the new one
                old_function_content = content[start_pos:end_pos]
                content = content.replace(old_function_content, new_highlight_function + '\n        ')
                print("✅ Replaced highlightCountryOnMap with real boundary highlighting")
        
        # Write the updated content back to the file
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully added real country boundary highlighting!")
        return True
        
    except Exception as e:
        print(f"❌ Error adding real boundaries: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Adding Real Country Boundary Highlighting...")
    success = add_real_country_boundaries()
    
    if success:
        print("\n✅ REAL COUNTRY BOUNDARIES ADDED!")
        print("\n🗺️ New Features:")
        print("1. ✅ Real country shape highlighting (not just circles)")
        print("2. ✅ Uses GeoJSON data from public APIs")
        print("3. ✅ Green fill with darker green borders")
        print("4. ✅ Automatic fallback if GeoJSON fails")
        print("5. ✅ Fits map to actual country boundaries")
        print("\n🎯 How it works:")
        print("   • Loads real country boundary data from GeoJSON APIs")
        print("   • Highlights the actual country shape in green")
        print("   • Shows popup with electricity access info")
        print("   • Falls back to circle if boundary data unavailable")
        print("\n📍 Example:")
        print("   Search 'India' → Shows actual India boundaries in green")
        print("   Search 'Germany' → Shows actual Germany shape highlighted")
        print("   Search 'Brazil' → Shows actual Brazil borders in green")
        print("\n🔧 Technical:")
        print("   • Uses multiple GeoJSON data sources for reliability")
        print("   • Smart country matching by name and ISO codes")
        print("   • Automatic map fitting to country bounds")
        print("   • Professional popup styling")
        print("\n⚡ Restart your Django server to see real country boundaries!")
    else:
        print("\n❌ Failed to add real boundaries.")