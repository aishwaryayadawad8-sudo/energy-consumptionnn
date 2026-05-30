#!/usr/bin/env python3
"""
Script to add real country boundary highlighting like in the screenshot
"""

import os

def add_real_country_boundaries():
    """Add real country boundary highlighting using GeoJSON"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🗺️ Adding real country boundary highlighting...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the highlightCountryOnMap function and replace it
        old_function_start = content.find('function highlightCountryOnMap(countryName) {')
        if old_function_start == -1:
            print("❌ Could not find highlightCountryOnMap function")
            return False
        
        # Find the end of the function
        brace_count = 0
        pos = old_function_start
        while pos < len(content):
            if content[pos] == '{':
                brace_count += 1
            elif content[pos] == '}':
                brace_count -= 1
                if brace_count == 0:
                    old_function_end = pos + 1
                    break
            pos += 1
        
        # New function with real country boundary highlighting
        new_function = '''function highlightCountryOnMap(countryName) {
            const coords = countryCoordinates[countryName];
            if (!coords || !map) return;
            
            console.log(`🎯 Highlighting ${countryName} with real country boundaries`);
            
            // Clear existing highlights
            clearMapHighlights();
            
            // Try to load real country boundaries from external API
            loadCountryBoundaries(countryName, coords);
        }
        
        async function loadCountryBoundaries(countryName, coords) {
            try {
                // Use REST Countries API to get country boundaries
                const response = await fetch(`https://restcountries.com/v3.1/name/${encodeURIComponent(countryName)}?fields=name,cca2,cca3`);
                
                if (response.ok) {
                    const countryData = await response.json();
                    const countryCode = countryData[0]?.cca2 || countryData[0]?.cca3;
                    
                    if (countryCode) {
                        // Try to load GeoJSON from multiple sources
                        await loadGeoJSONBoundaries(countryName, countryCode, coords);
                    } else {
                        fallbackHighlighting(countryName, coords);
                    }
                } else {
                    fallbackHighlighting(countryName, coords);
                }
            } catch (error) {
                console.log(`⚠️ API failed for ${countryName}, using fallback`);
                fallbackHighlighting(countryName, coords);
            }
        }
        
        async function loadGeoJSONBoundaries(countryName, countryCode, coords) {
            const geoJsonSources = [
                `https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson`,
                `https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson`
            ];
            
            for (const source of geoJsonSources) {
                try {
                    const response = await fetch(source);
                    if (response.ok) {
                        const geoData = await response.json();
                        
                        // Find the country in the GeoJSON data
                        const countryFeature = geoData.features.find(feature => {
                            const props = feature.properties;
                            return props.NAME === countryName || 
                                   props.NAME_EN === countryName ||
                                   props.ADMIN === countryName ||
                                   props.NAME_LONG === countryName ||
                                   props.ISO_A2 === countryCode ||
                                   props.ISO_A3 === countryCode;
                        });
                        
                        if (countryFeature) {
                            highlightCountryWithGeoJSON(countryName, countryFeature, coords);
                            return;
                        }
                    }
                } catch (error) {
                    console.log(`Failed to load from ${source}`);
                    continue;
                }
            }
            
            // If no GeoJSON found, use fallback
            fallbackHighlighting(countryName, coords);
        }
        
        function highlightCountryWithGeoJSON(countryName, countryFeature, coords) {
            console.log(`✅ Found GeoJSON boundaries for ${countryName}`);
            
            // Create GeoJSON layer with green highlighting
            const geoJsonLayer = L.geoJSON(countryFeature, {
                style: {
                    fillColor: '#90EE90',
                    weight: 3,
                    opacity: 1,
                    color: '#32CD32',
                    fillOpacity: 0.6
                },
                onEachFeature: function(feature, layer) {
                    layer.bindPopup(`
                        <div style="text-align: center; padding: 15px; border: 2px solid #32CD32; border-radius: 10px; background: linear-gradient(135deg, #f0fff0 0%, #e6ffe6 100%);">
                            <h5 style="margin: 0 0 10px 0; color: #228B22; font-weight: bold;">${countryName}</h5>
                            <div style="border-bottom: 1px solid #90EE90; margin: 10px 0;"></div>
                            <p style="margin: 5px 0; color: #2c3e50;"><strong>🔌 Electricity Access:</strong> ${coords.access}%</p>
                            <p style="margin: 5px 0; color: #2c3e50;"><strong>🌍 CO₂ Emissions:</strong> ${Math.round(coords.co2 / 1000)} Mt</p>
                            <p style="margin: 5px 0; color: #2c3e50;"><strong>🌱 Renewable Potential:</strong> ${Math.round(20 + coords.access * 0.3)}%</p>
                            <div style="margin-top: 10px; padding: 5px; background: rgba(50, 205, 50, 0.2); border-radius: 5px;">
                                <small style="color: #228B22; font-weight: bold;">🗺️ Real Country Boundaries</small>
                            </div>
                        </div>
                    `);
                }
            }).addTo(map);
            
            // Add pin marker at country center
            const marker = L.marker([coords.lat, coords.lng])
                .addTo(map)
                .bindPopup(`
                    <div style="text-align: center; padding: 15px; border: 2px solid #32CD32; border-radius: 10px; background: linear-gradient(135deg, #f0fff0 0%, #e6ffe6 100%);">
                        <h5 style="margin: 0 0 10px 0; color: #228B22; font-weight: bold;">${countryName}</h5>
                        <div style="border-bottom: 1px solid #90EE90; margin: 10px 0;"></div>
                        <p style="margin: 5px 0; color: #2c3e50;"><strong>🔌 Electricity Access:</strong> ${coords.access}%</p>
                        <p style="margin: 5px 0; color: #2c3e50;"><strong>🌍 CO₂ Emissions:</strong> ${Math.round(coords.co2 / 1000)} Mt</p>
                        <p style="margin: 5px 0; color: #2c3e50;"><strong>🌱 Renewable Potential:</strong> ${Math.round(20 + coords.access * 0.3)}%</p>
                        <div style="margin-top: 10px; padding: 5px; background: rgba(50, 205, 50, 0.2); border-radius: 5px;">
                            <small style="color: #228B22; font-weight: bold;">📍 Country Center</small>
                        </div>
                    </div>
                `)
                .openPopup();
            
            // Store references
            currentHighlightLayer = geoJsonLayer;
            currentMarker = marker;
            
            // Fit map to country boundaries
            map.fitBounds(geoJsonLayer.getBounds(), {
                padding: [20, 20],
                maxZoom: 6
            });
            
            console.log(`✅ Successfully highlighted ${countryName} with real boundaries`);
        }
        
        function fallbackHighlighting(countryName, coords) {
            console.log(`🔄 Using fallback highlighting for ${countryName}`);
            
            // Create enhanced circular highlight as fallback
            const highlightCircle = L.circle([coords.lat, coords.lng], {
                color: '#32CD32',
                fillColor: '#90EE90',
                fillOpacity: 0.6,
                radius: getCountryRadius(countryName),
                weight: 4
            }).addTo(map);
            
            // Add pin marker
            const marker = L.marker([coords.lat, coords.lng])
                .addTo(map)
                .bindPopup(`
                    <div style="text-align: center; padding: 15px; border: 2px solid #32CD32; border-radius: 10px; background: linear-gradient(135deg, #f0fff0 0%, #e6ffe6 100%);">
                        <h5 style="margin: 0 0 10px 0; color: #228B22; font-weight: bold;">${countryName}</h5>
                        <div style="border-bottom: 1px solid #90EE90; margin: 10px 0;"></div>
                        <p style="margin: 5px 0; color: #2c3e50;"><strong>🔌 Electricity Access:</strong> ${coords.access}%</p>
                        <p style="margin: 5px 0; color: #2c3e50;"><strong>🌍 CO₂ Emissions:</strong> ${Math.round(coords.co2 / 1000)} Mt</p>
                        <p style="margin: 5px 0; color: #2c3e50;"><strong>🌱 Renewable Potential:</strong> ${Math.round(20 + coords.access * 0.3)}%</p>
                        <div style="margin-top: 10px; padding: 5px; background: rgba(50, 205, 50, 0.2); border-radius: 5px;">
                            <small style="color: #228B22; font-weight: bold;">🎯 Country Area Highlighted</small>
                        </div>
                    </div>
                `)
                .openPopup();
            
            // Store references
            currentHighlightLayer = highlightCircle;
            currentMarker = marker;
            
            // Center map on country
            const zoom = getCountryZoom(countryName);
            map.flyTo([coords.lat, coords.lng], zoom, {
                animate: true,
                duration: 1.5
            });
            
            console.log(`✅ Fallback highlighting applied for ${countryName}`);
        }'''
        
        # Replace the old function with the new one
        content = content[:old_function_start] + new_function + content[old_function_end:]
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully added real country boundary highlighting")
        return True
        
    except Exception as e:
        print(f"❌ Error adding real country boundaries: {e}")
        return False

def main():
    """Main function"""
    print("🗺️ ADDING REAL COUNTRY BOUNDARY HIGHLIGHTING")
    print("=" * 60)
    print("   • Real country shapes highlighted in green")
    print("   • Using GeoJSON data from external APIs")
    print("   • Fallback to enhanced circles if GeoJSON fails")
    print("   • Pin markers at country centers")
    print("=" * 60)
    
    success = add_real_country_boundaries()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ REAL COUNTRY BOUNDARY HIGHLIGHTING ADDED!")
        print("=" * 60)
        print("\n🗺️ New Features:")
        print("   ✅ Real country shapes highlighted in green")
        print("   ✅ GeoJSON data from REST Countries API")
        print("   ✅ Automatic boundary detection")
        print("   ✅ Enhanced popups with country details")
        print("   ✅ Pin markers at country centers")
        print("   ✅ Fallback to enhanced circles")
        print("   ✅ Auto-fit map to country boundaries")
        
        print("\n🎯 How it works:")
        print("   1. Search for a country (e.g., 'India')")
        print("   2. System fetches real country boundaries")
        print("   3. Country shape gets highlighted in green")
        print("   4. Pin marker appears at country center")
        print("   5. Map auto-fits to show full country")
        
        print("\n🌍 Supported:")
        print("   • All major countries with GeoJSON data")
        print("   • Automatic fallback for unsupported countries")
        print("   • Real-time boundary fetching")
        print("   • Enhanced visual feedback")
        
        print("\n🔄 Next Steps:")
        print("   1. Refresh your browser (Ctrl+F5)")
        print("   2. Search for 'India' or any country")
        print("   3. See the real country shape highlighted!")
        print("   4. Try different countries to see boundaries")
        
    else:
        print("\n❌ Enhancement failed. Please check the error messages above.")

if __name__ == "__main__":
    main()