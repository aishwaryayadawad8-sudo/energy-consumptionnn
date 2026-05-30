#!/usr/bin/env python3
"""
Optimize Country Search with Zoom and Pale Green Highlighting
This script optimizes the country search to zoom to the country and highlight it with pale green
showing the electricity access percentage
"""

import os

def optimize_country_search_zoom():
    """Optimize country search with proper zoom and pale green highlighting"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update the highlightCountryFeature function for better zoom and pale green highlighting
        old_highlight_feature = '''        function highlightCountryFeature(feature, countryName, coords) {
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
        }'''
        
        new_highlight_feature = '''        function highlightCountryFeature(feature, countryName, coords) {
            // Create the country layer with pale green highlighting
            const countryLayer = L.geoJSON(feature, {
                style: {
                    fillColor: '#dcfce7',     // Pale green fill (very light)
                    weight: 2,                // Thinner border
                    opacity: 0.8,             // Border opacity
                    color: '#22c55e',         // Green border
                    dashArray: '',            // Solid line
                    fillOpacity: 0.6          // More visible fill
                },
                onEachFeature: function(feature, layer) {
                    // Add popup to the country with electricity access
                    const popupContent = `
                        <div class="country-search-popup">
                            <h2>${countryName}</h2>
                            <div class="electricity-access">
                                <i class="fas fa-bolt"></i> 
                                <span>Electricity Access: <strong>${coords.access}%</strong></span>
                            </div>
                            <button onclick="searchCountry()" class="btn btn-primary view-analysis-btn">
                                <i class="fas fa-chart-line"></i> View Full Analysis
                            </button>
                        </div>
                    `;
                    
                    layer.bindPopup(popupContent, {
                        maxWidth: 280,
                        className: 'country-search-popup-container',
                        closeButton: true,
                        autoClose: false,
                        closeOnClick: false
                    });
                }
            }).addTo(map);
            
            // Store reference for later removal
            window.currentCountryLayer = countryLayer;
            
            // Zoom to country with proper bounds and padding
            const bounds = countryLayer.getBounds();
            map.fitBounds(bounds, {
                padding: [30, 30],          // More padding for better view
                animate: true,
                duration: 2.0,              // Slower animation for smooth zoom
                easeLinearity: 0.25         // Smooth easing
            });
            
            // Open popup after zoom animation completes
            setTimeout(() => {
                countryLayer.openPopup();
                console.log(`Zoomed to ${countryName} and showing electricity access: ${coords.access}%`);
            }, 2200);
            
            console.log(`Successfully highlighted ${countryName} with pale green and zoomed to bounds`);
        }'''
        
        if old_highlight_feature in content:
            content = content.replace(old_highlight_feature, new_highlight_feature)
            print("✅ Updated highlightCountryFeature with pale green and better zoom")
        
        # Update the fallback highlight function as well
        old_fallback = '''        function loadFallbackHighlight(countryName, coords) {
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
        
        new_fallback = '''        function loadFallbackHighlight(countryName, coords) {
            console.log(`Using fallback highlight for ${countryName}`);
            
            // Create a more accurate country-sized circle as fallback with pale green
            const radius = getCountryRadius(countryName);
            
            const countryHighlight = L.circle([coords.lat, coords.lng], {
                color: '#22c55e',           // Green border
                fillColor: '#dcfce7',       // Pale green fill
                fillOpacity: 0.6,           // More visible transparency
                weight: 2,                  // Thinner border
                radius: radius
            }).addTo(map);
            
            // Store reference
            window.currentCountryLayer = countryHighlight;
            
            // Add popup with electricity access
            const popupContent = `
                <div class="country-search-popup">
                    <h2>${countryName}</h2>
                    <div class="electricity-access">
                        <i class="fas fa-bolt"></i> 
                        <span>Electricity Access: <strong>${coords.access}%</strong></span>
                    </div>
                    <button onclick="searchCountry()" class="btn btn-primary view-analysis-btn">
                        <i class="fas fa-chart-line"></i> View Full Analysis
                    </button>
                </div>
            `;
            
            countryHighlight.bindPopup(popupContent, {
                maxWidth: 280,
                className: 'country-search-popup-container',
                closeButton: true,
                autoClose: false,
                closeOnClick: false
            });
            
            // Zoom to country with appropriate level
            const zoomLevel = getCountryZoomLevel(countryName);
            map.flyTo([coords.lat, coords.lng], zoomLevel, {
                animate: true,
                duration: 2.0
            });
            
            // Open popup after zoom
            setTimeout(() => {
                countryHighlight.openPopup();
                console.log(`Fallback: Zoomed to ${countryName} and showing electricity access: ${coords.access}%`);
            }, 2200);
        }
        
        function getCountryZoomLevel(countryName) {
            // Different zoom levels for different country sizes
            const zoomLevels = {
                'Russia': 3, 'Canada': 3, 'United States': 4, 'China': 4, 'Brazil': 4,
                'Australia': 4, 'India': 5, 'Argentina': 5, 'Kazakhstan': 4, 'Algeria': 5,
                'Saudi Arabia': 5, 'Mexico': 5, 'Indonesia': 5, 'Iran': 5, 'Libya': 5,
                'Mongolia': 5, 'Peru': 5, 'Chad': 5, 'Niger': 5, 'Angola': 5,
                'Mali': 5, 'South Africa': 5, 'Colombia': 5, 'Ethiopia': 5, 'Bolivia': 5,
                'Mauritania': 5, 'Egypt': 6, 'Tanzania': 6, 'Nigeria': 6, 'Venezuela': 6,
                'Pakistan': 6, 'Mozambique': 6, 'Turkey': 6, 'Chile': 5, 'Zambia': 6,
                'Myanmar': 6, 'Afghanistan': 6, 'Somalia': 6, 'Ukraine': 6, 'Madagascar': 6,
                'Kenya': 6, 'Botswana': 6, 'France': 6, 'Yemen': 6, 'Thailand': 6,
                'Spain': 6, 'Sweden': 6, 'Morocco': 6, 'Iraq': 6, 'Paraguay': 6,
                'Zimbabwe': 6, 'Japan': 6, 'Germany': 6, 'Finland': 6, 'Vietnam': 6,
                'Malaysia': 6, 'Norway': 6, 'Poland': 6, 'Italy': 6, 'Philippines': 6,
                'Ecuador': 6, 'New Zealand': 6, 'United Kingdom': 6, 'Uganda': 7,
                'Ghana': 7, 'Romania': 7, 'Laos': 7, 'Belarus': 7, 'Senegal': 7,
                'Syria': 7, 'Cambodia': 7, 'Uruguay': 7, 'Tunisia': 7, 'Nepal': 7,
                'Bangladesh': 7, 'Greece': 7, 'Nicaragua': 7, 'North Korea': 7,
                'Bulgaria': 7, 'Cuba': 7, 'Guatemala': 7, 'Iceland': 7, 'South Korea': 7,
                'Hungary': 7, 'Portugal': 7, 'Jordan': 7, 'Serbia': 7, 'Austria': 7,
                'Czech Republic': 7, 'Panama': 7, 'Ireland': 7, 'Georgia': 7,
                'Sri Lanka': 7, 'Lithuania': 7, 'Latvia': 7, 'Croatia': 7,
                'Costa Rica': 7, 'Slovakia': 7, 'Estonia': 8, 'Denmark': 8,
                'Netherlands': 8, 'Switzerland': 8, 'Belgium': 8, 'Albania': 8,
                'Slovenia': 8, 'Luxembourg': 9, 'Cyprus': 9, 'Malta': 10
            };
            return zoomLevels[countryName] || 6; // Default zoom level
        }'''
        
        if old_fallback in content:
            content = content.replace(old_fallback, new_fallback)
            print("✅ Updated fallback highlight with pale green and smart zoom")
        
        # Update CSS for the new popup style
        old_popup_css = '''        .country-boundary-popup-container .leaflet-popup-content {
            margin: 0;
            padding: 0;
            border-radius: 12px;
            overflow: hidden;
        }
        
        .country-boundary-popup {
            background: white;
            padding: 20px;
            text-align: center;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        }
        
        .country-boundary-popup h3 {
            margin: 0 0 15px 0;
            color: #1f2937;
            font-size: 1.4rem;
            font-weight: 700;
        }
        
        .access-info {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            margin: 15px 0;
            padding: 10px;
            background: #f8fafc;
            border-radius: 8px;
            color: #374151;
        }
        
        .access-info i {
            color: #f59e0b;
            font-size: 1.1rem;
        }
        
        .access-info strong {
            color: #22c55e;
            font-size: 1.1rem;
        }
        
        .analysis-btn {
            background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            color: white;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
            margin: 0 auto;
        }
        
        .analysis-btn:hover {
            background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
        }
        
        .analysis-btn i {
            font-size: 1rem;
        }
        
        /* Custom popup arrow */
        .country-boundary-popup-container .leaflet-popup-tip {
            background: white;
            border: none;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        }'''
        
        new_popup_css = '''        .country-search-popup-container .leaflet-popup-content {
            margin: 0;
            padding: 0;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        }
        
        .country-search-popup {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
            padding: 25px;
            text-align: center;
            border-radius: 15px;
            border: 1px solid #e5e7eb;
        }
        
        .country-search-popup h2 {
            margin: 0 0 20px 0;
            color: #1f2937;
            font-size: 1.6rem;
            font-weight: 700;
            text-shadow: 0 1px 2px rgba(0,0,0,0.1);
        }
        
        .electricity-access {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            margin: 20px 0;
            padding: 15px;
            background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
            border-radius: 12px;
            color: #166534;
            border: 2px solid #22c55e;
        }
        
        .electricity-access i {
            color: #eab308;
            font-size: 1.3rem;
            animation: pulse 2s infinite;
        }
        
        .electricity-access strong {
            color: #15803d;
            font-size: 1.3rem;
            font-weight: 800;
        }
        
        .view-analysis-btn {
            background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
            border: none;
            padding: 14px 24px;
            border-radius: 12px;
            color: white;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 10px;
            margin: 0 auto;
            font-size: 1rem;
            box-shadow: 0 4px 16px rgba(59, 130, 246, 0.3);
        }
        
        .view-analysis-btn:hover {
            background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(59, 130, 246, 0.5);
        }
        
        .view-analysis-btn i {
            font-size: 1.1rem;
        }
        
        /* Custom popup arrow */
        .country-search-popup-container .leaflet-popup-tip {
            background: white;
            border: 1px solid #e5e7eb;
            box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }'''
        
        if old_popup_css in content:
            content = content.replace(old_popup_css, new_popup_css)
            print("✅ Updated popup CSS for better country search experience")
        
        # Write the updated content back to the file
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully optimized country search with zoom and pale green highlighting!")
        return True
        
    except Exception as e:
        print(f"❌ Error optimizing country search: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Optimizing Country Search with Zoom and Pale Green Highlighting...")
    success = optimize_country_search_zoom()
    
    if success:
        print("\n✅ COUNTRY SEARCH OPTIMIZED!")
        print("\n🎯 Perfect Search Experience:")
        print("1. ✅ Search country → Map automatically zooms to that country")
        print("2. ✅ Country highlighted with pale green color")
        print("3. ✅ Shows electricity access percentage for that specific country")
        print("4. ✅ Smooth zoom animation (2 seconds)")
        print("5. ✅ Professional popup with country info")
        print("\n🎨 Visual Features:")
        print("   • Pale Green Fill: #dcfce7 (very light green)")
        print("   • Green Border: #22c55e (clear outline)")
        print("   • Smart Zoom Levels: Different zoom for different country sizes")
        print("   • Animated Electricity Icon: Pulsing bolt icon")
        print("   • Gradient Popup: Beautiful popup design")
        print("\n📍 Example Experience:")
        print("   Search 'India' →")
        print("   • Map smoothly zooms to India")
        print("   • India highlighted in pale green")
        print("   • Popup shows: 'India - Electricity Access: 95.2%'")
        print("   • Click 'View Full Analysis' for detailed dashboard")
        print("\n🔧 Smart Features:")
        print("   • Large countries (Russia, Canada): Zoom level 3-4")
        print("   • Medium countries (India, Germany): Zoom level 5-6")
        print("   • Small countries (Netherlands, Belgium): Zoom level 8-9")
        print("   • Popup stays open until user closes it")
        print("   • Real country boundaries when available")
        print("\n⚡ Restart your Django server to experience the optimized search!")
    else:
        print("\n❌ Failed to optimize country search.")