#!/usr/bin/env python3
"""
Script to enhance country highlighting in explore dashboard with pale green border and pin
"""

import os

def enhance_country_highlighting():
    """Enhance country highlighting with pale green border and pin marker"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🎯 Enhancing country highlighting with pale green border...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Enhanced CSS for country highlighting
        enhanced_css = '''
        /* Enhanced Country Highlighting Styles */
        .country-highlight-circle {
            border: 3px solid #90EE90 !important;
            border-radius: 50% !important;
            background-color: rgba(144, 238, 144, 0.2) !important;
            box-shadow: 0 0 20px rgba(144, 238, 144, 0.6) !important;
            animation: pulseGreen 2s infinite !important;
        }
        
        @keyframes pulseGreen {
            0% {
                box-shadow: 0 0 20px rgba(144, 238, 144, 0.6);
                transform: scale(1);
            }
            50% {
                box-shadow: 0 0 30px rgba(144, 238, 144, 0.8);
                transform: scale(1.05);
            }
            100% {
                box-shadow: 0 0 20px rgba(144, 238, 144, 0.6);
                transform: scale(1);
            }
        }
        
        .country-pin-marker {
            background-color: #32CD32 !important;
            border: 2px solid #228B22 !important;
            border-radius: 50% !important;
            width: 20px !important;
            height: 20px !important;
            box-shadow: 0 0 15px rgba(50, 205, 50, 0.7) !important;
        }
        
        .country-search-highlight {
            background-color: rgba(144, 238, 144, 0.3) !important;
            border: 2px solid #90EE90 !important;
            border-radius: 8px !important;
            animation: highlightPulse 1.5s ease-in-out !important;
        }
        
        @keyframes highlightPulse {
            0% {
                background-color: rgba(144, 238, 144, 0.1);
                border-color: #90EE90;
            }
            50% {
                background-color: rgba(144, 238, 144, 0.4);
                border-color: #32CD32;
            }
            100% {
                background-color: rgba(144, 238, 144, 0.3);
                border-color: #90EE90;
            }
        }'''
        
        # Find the closing </style> tag and insert enhanced CSS before it
        style_end = content.find('</style>')
        if style_end != -1:
            content = content[:style_end] + enhanced_css + '\n        ' + content[style_end:]
            print("✅ Added enhanced CSS for country highlighting")
        
        # Enhanced JavaScript for country highlighting
        enhanced_js = '''
        
        // Enhanced country highlighting with pale green border and pin
        let currentHighlightLayer = null;
        let currentMarker = null;
        
        function highlightCountryOnMap(countryName) {
            const coords = countryCoordinates[countryName];
            if (!coords || !map) return;
            
            console.log(`🎯 Highlighting ${countryName} with pale green border and pin`);
            
            // Clear existing highlights and markers
            clearMapHighlights();
            
            // Create pale green circle highlight around country
            const highlightCircle = L.circle([coords.lat, coords.lng], {
                color: '#90EE90',
                fillColor: '#90EE90',
                fillOpacity: 0.2,
                radius: 200000, // 200km radius
                weight: 3,
                className: 'country-highlight-circle'
            }).addTo(map);
            
            // Create custom pin marker with pale green styling
            const customIcon = L.divIcon({
                className: 'country-pin-marker',
                html: '<i class="fas fa-map-pin" style="color: #228B22; font-size: 16px; margin-top: 2px;"></i>',
                iconSize: [20, 20],
                iconAnchor: [10, 10]
            });
            
            // Add enhanced marker for selected country
            const marker = L.marker([coords.lat, coords.lng], { icon: customIcon })
                .addTo(map)
                .bindPopup(`
                    <div style="text-align: center; padding: 15px; border: 2px solid #90EE90; border-radius: 10px; background: linear-gradient(135deg, #f0fff0 0%, #e6ffe6 100%);">
                        <h5 style="margin: 0 0 10px 0; color: #228B22; font-weight: bold;">${countryName}</h5>
                        <div style="border-bottom: 1px solid #90EE90; margin: 10px 0;"></div>
                        <p style="margin: 5px 0; color: #2c3e50;"><strong>🔌 Electricity Access:</strong> ${coords.access}%</p>
                        <p style="margin: 5px 0; color: #2c3e50;"><strong>🌍 CO₂ Emissions:</strong> ${Math.round(coords.co2 / 1000)} Mt</p>
                        <p style="margin: 5px 0; color: #2c3e50;"><strong>🌱 Renewable Potential:</strong> ${Math.round(20 + coords.access * 0.3)}%</p>
                        <div style="margin-top: 10px; padding: 5px; background: rgba(144, 238, 144, 0.2); border-radius: 5px;">
                            <small style="color: #228B22; font-weight: bold;">✅ Country Selected & Highlighted</small>
                        </div>
                    </div>
                `)
                .openPopup();
            
            // Store references for cleanup
            currentHighlightLayer = highlightCircle;
            currentMarker = marker;
            
            // Center map on country with smooth animation
            map.flyTo([coords.lat, coords.lng], 5, {
                animate: true,
                duration: 1.5
            });
            
            // Highlight the country in search suggestions if visible
            highlightCountryInSearch(countryName);
            
            console.log(`✅ Successfully highlighted ${countryName} with pale green border and pin`);
        }
        
        function clearMapHighlights() {
            // Remove existing highlight circle
            if (currentHighlightLayer) {
                map.removeLayer(currentHighlightLayer);
                currentHighlightLayer = null;
            }
            
            // Remove existing marker
            if (currentMarker) {
                map.removeLayer(currentMarker);
                currentMarker = null;
            }
            
            // Clear all other markers and circles
            map.eachLayer(layer => {
                if (layer instanceof L.Marker || layer instanceof L.Circle) {
                    if (layer !== currentHighlightLayer && layer !== currentMarker) {
                        map.removeLayer(layer);
                    }
                }
            });
        }
        
        function highlightCountryInSearch(countryName) {
            // Highlight the country in search dropdown if visible
            const searchSuggestions = document.getElementById('searchSuggestions');
            if (searchSuggestions && searchSuggestions.style.display !== 'none') {
                const suggestionItems = searchSuggestions.querySelectorAll('.suggestion-item');
                suggestionItems.forEach(item => {
                    item.classList.remove('country-search-highlight');
                    if (item.textContent === countryName) {
                        item.classList.add('country-search-highlight');
                        // Scroll to highlighted item
                        item.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                    }
                });
            }
            
            // Also highlight in dropdown if it matches
            const countryDropdown = document.getElementById('countryDropdown');
            if (countryDropdown && countryDropdown.value === countryName) {
                countryDropdown.style.border = '2px solid #90EE90';
                countryDropdown.style.backgroundColor = 'rgba(144, 238, 144, 0.1)';
                setTimeout(() => {
                    countryDropdown.style.border = '2px solid #e0e0e0';
                    countryDropdown.style.backgroundColor = 'white';
                }, 3000);
            }
        }
        
        // Enhanced country selection with immediate highlighting
        function selectCountry(countryName) {
            const countryInput = document.getElementById('countryInput');
            const countryDropdown = document.getElementById('countryDropdown');
            const searchSuggestions = document.getElementById('searchSuggestions');
            
            if (countryInput) countryInput.value = countryName;
            if (countryDropdown) countryDropdown.value = countryName;
            if (searchSuggestions) searchSuggestions.style.display = 'none';
            
            // Immediately highlight the country on map when selected
            highlightCountryOnMap(countryName);
            
            console.log(`🎯 Country selected and highlighted: ${countryName}`);
        }'''
        
        # Find the existing highlightCountryOnMap function and replace it
        old_highlight_start = content.find('function highlightCountryOnMap(countryName) {')
        if old_highlight_start != -1:
            # Find the end of the function
            brace_count = 0
            pos = old_highlight_start
            while pos < len(content):
                if content[pos] == '{':
                    brace_count += 1
                elif content[pos] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        old_highlight_end = pos + 1
                        break
                pos += 1
            
            # Replace the old function with enhanced version
            content = content[:old_highlight_start] + enhanced_js + content[old_highlight_end:]
            print("✅ Enhanced highlightCountryOnMap function with pale green border and pin")
        else:
            # If function not found, add it before the closing script tag
            script_end = content.rfind('</script>')
            if script_end != -1:
                content = content[:script_end] + enhanced_js + '\n    ' + content[script_end:]
                print("✅ Added enhanced country highlighting functions")
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully enhanced country highlighting with pale green border and pin")
        return True
        
    except Exception as e:
        print(f"❌ Error enhancing country highlighting: {e}")
        return False

def main():
    """Main function"""
    print("🎯 ENHANCING COUNTRY HIGHLIGHTING WITH PALE GREEN BORDER")
    print("=" * 60)
    print("   • Adding pale green circular border around selected country")
    print("   • Enhanced pin marker with green styling")
    print("   • Smooth animations and visual feedback")
    print("   • Improved popup design with country details")
    print("=" * 60)
    
    success = enhance_country_highlighting()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ COUNTRY HIGHLIGHTING ENHANCED!")
        print("=" * 60)
        print("\n🎯 New Features:")
        print("   ✅ Pale green circular border around selected country")
        print("   ✅ Custom green pin marker with icon")
        print("   ✅ Pulsing animation effect for visibility")
        print("   ✅ Enhanced popup with country details")
        print("   ✅ Smooth map animation when country selected")
        print("   ✅ Search highlighting in dropdown")
        print("   ✅ Automatic highlighting when country selected from search")
        
        print("\n🔧 How it works:")
        print("   1. Search for a country in the search box")
        print("   2. Select country from dropdown or suggestions")
        print("   3. Country gets highlighted with pale green border")
        print("   4. Green pin marker appears at country location")
        print("   5. Map smoothly animates to country location")
        print("   6. Enhanced popup shows country details")
        
        print("\n🎨 Visual Features:")
        print("   • Pale green (#90EE90) circular border")
        print("   • 200km radius highlight circle")
        print("   • Pulsing animation effect")
        print("   • Custom green pin marker")
        print("   • Enhanced popup with gradient background")
        print("   • Search result highlighting")
        
        print("\n🔄 Next Steps:")
        print("   1. Restart your Django server")
        print("   2. Visit the explore dashboard")
        print("   3. Search for any country")
        print("   4. See the pale green border and pin highlighting")
        
    else:
        print("\n❌ Enhancement failed. Please check the error messages above.")

if __name__ == "__main__":
    main()