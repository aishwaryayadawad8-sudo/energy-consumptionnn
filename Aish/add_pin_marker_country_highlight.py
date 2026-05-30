#!/usr/bin/env python3
"""Replace circle with pin marker and add country boundary highlighting"""

# Read the file
with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the circleMarker with a custom pin icon marker
old_highlight_function = '''        // Highlight selected country on map
        function highlightCountryOnMap(countryName, lat, lon, electricityAccess) {
            // Remove previous highlight if exists
            if (highlightMarker) {
                map.removeLayer(highlightMarker);
            }
            
            // Create a larger, highlighted marker with vibrant colors
            highlightMarker = L.circleMarker([lat, lon], {
                radius: 20,              // Larger size
                fillColor: '#FF1493',    // Deep Pink - very distinct!
                color: '#FFFF00',        // Bright Yellow border
                weight: 4,               // Thicker border
                opacity: 1,
                fillOpacity: 1           // Fully opaque
            }).addTo(map);
            
            // Add a permanent label with country name
            highlightMarker.bindTooltip(countryName, {
                permanent: true,
                direction: 'top',
                className: 'country-highlight-label',
                offset: [0, -15]
            }).openTooltip();
            
            // Add popup with details
            highlightMarker.bindPopup(`
                <div style="text-align: center;">
                    <strong style="font-size: 16px; color: #2c3e50;">${countryName}</strong><br>
                    <span style="font-size: 14px;">⚡ Electricity Access: ${electricityAccess.toFixed(1)}%</span>
                </div>
            `).openPopup();
            
            // Zoom to the country
            map.setView([lat, lon], 5, {
                animate: true,
                duration: 1
            });
        }'''

new_highlight_function = '''        // Highlight selected country on map
        function highlightCountryOnMap(countryName, lat, lon, electricityAccess) {
            // Remove previous highlight if exists
            if (highlightMarker) {
                map.removeLayer(highlightMarker);
            }
            
            // Create custom pin icon
            const pinIcon = L.divIcon({
                className: 'custom-pin-marker',
                html: `
                    <div style="position: relative;">
                        <svg width="50" height="70" viewBox="0 0 50 70" xmlns="http://www.w3.org/2000/svg">
                            <!-- Pin shadow -->
                            <ellipse cx="25" cy="65" rx="8" ry="3" fill="rgba(0,0,0,0.3)"/>
                            <!-- Pin body -->
                            <path d="M25 0 C15 0 7 8 7 18 C7 28 25 50 25 50 C25 50 43 28 43 18 C43 8 35 0 25 0 Z" 
                                  fill="#FF1493" stroke="#FFFF00" stroke-width="3"/>
                            <!-- Pin center circle -->
                            <circle cx="25" cy="18" r="8" fill="#FFFFFF"/>
                            <!-- Pin inner dot -->
                            <circle cx="25" cy="18" r="4" fill="#FF1493"/>
                        </svg>
                        <div style="position: absolute; top: -30px; left: 50%; transform: translateX(-50%); 
                                    background: #FF1493; color: white; padding: 5px 12px; border-radius: 5px; 
                                    border: 2px solid #FFFF00; white-space: nowrap; font-weight: bold; 
                                    box-shadow: 0 2px 8px rgba(0,0,0,0.3); font-size: 14px;">
                            ${countryName}
                        </div>
                    </div>
                `,
                iconSize: [50, 70],
                iconAnchor: [25, 50],
                popupAnchor: [0, -50]
            });
            
            // Create marker with pin icon
            highlightMarker = L.marker([lat, lon], {
                icon: pinIcon,
                zIndexOffset: 1000  // Ensure it's on top
            }).addTo(map);
            
            // Add popup with details
            highlightMarker.bindPopup(`
                <div style="text-align: center; padding: 10px;">
                    <strong style="font-size: 18px; color: #FF1493;">📍 ${countryName}</strong><br>
                    <hr style="margin: 8px 0; border-color: #FF1493;">
                    <span style="font-size: 16px;">⚡ Electricity Access: <strong>${electricityAccess.toFixed(1)}%</strong></span>
                </div>
            `).openPopup();
            
            // Zoom to the country
            map.setView([lat, lon], 6, {
                animate: true,
                duration: 1
            });
            
            // Try to highlight country boundary using Nominatim API
            fetch(`https://nominatim.openstreetmap.org/search?country=${encodeURIComponent(countryName)}&polygon_geojson=1&format=json`)
                .then(response => response.json())
                .then(data => {
                    if (data && data.length > 0 && data[0].geojson) {
                        // Add country boundary highlight
                        const boundaryLayer = L.geoJSON(data[0].geojson, {
                            style: {
                                color: '#FF1493',      // Pink border
                                weight: 4,
                                opacity: 0.8,
                                fillColor: '#FF1493',  // Pink fill
                                fillOpacity: 0.2       // Semi-transparent
                            }
                        }).addTo(map);
                        
                        // Store boundary layer to remove later
                        if (!highlightMarker.boundaryLayer) {
                            highlightMarker.boundaryLayer = boundaryLayer;
                        }
                        
                        // Fit map to country bounds
                        map.fitBounds(boundaryLayer.getBounds(), {
                            padding: [50, 50],
                            animate: true
                        });
                    }
                })
                .catch(error => {
                    console.log('Could not load country boundary:', error);
                    // Fallback to just pin marker if boundary fails
                });
        }'''

content = content.replace(old_highlight_function, new_highlight_function)

# Update the removal logic to also remove boundary
old_removal = '''            // Remove previous highlight if exists
            if (highlightMarker) {
                map.removeLayer(highlightMarker);
            }'''

new_removal = '''            // Remove previous highlight if exists
            if (highlightMarker) {
                map.removeLayer(highlightMarker);
                // Also remove boundary layer if exists
                if (highlightMarker.boundaryLayer) {
                    map.removeLayer(highlightMarker.boundaryLayer);
                }
            }'''

content = content.replace(old_removal, new_removal)

# Update CSS for the pin marker
old_label_css = '''        .country-highlight-label {
            background-color: #FF1493;  /* Deep Pink */
            border: 3px solid #FFFF00;  /* Bright Yellow border */
            border-radius: 8px;
            padding: 8px 15px;
            font-weight: bold;
            font-size: 16px;
            color: #FFFFFF;             /* White text */
            box-shadow: 0 4px 15px rgba(255, 20, 147, 0.6);
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        }'''

new_label_css = '''        .custom-pin-marker {
            background: transparent;
            border: none;
        }
        
        .custom-pin-marker svg {
            filter: drop-shadow(0 4px 8px rgba(0,0,0,0.4));
        }'''

content = content.replace(old_label_css, new_label_css)

# Write back
with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Added location pin marker with country boundary highlighting!")
print("📍 Features:")
print("   • Custom pink pin icon with yellow border")
print("   • Country name label above pin")
print("   • Country boundary highlighted in pink")
print("   • Semi-transparent pink fill over country")
print("   • Map auto-fits to country boundaries")
print("   • Fallback to pin only if boundary data unavailable")
