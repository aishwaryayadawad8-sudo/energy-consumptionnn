#!/usr/bin/env python3
"""
Add Country Map Identification
This script adds functionality to identify and highlight searched countries on the map
with markers and popups showing country information
"""

import os

def add_country_map_identification():
    """Add map identification functionality for searched countries"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add country coordinates data (major countries)
        country_coordinates = '''
        // Country coordinates for map identification
        const countryCoordinates = {
            'Afghanistan': { lat: 33.9391, lng: 67.7100, access: 97.7 },
            'Albania': { lat: 41.1533, lng: 20.1683, access: 100.0 },
            'Algeria': { lat: 28.0339, lng: 1.6596, access: 99.4 },
            'Argentina': { lat: -38.4161, lng: -63.6167, access: 99.2 },
            'Australia': { lat: -25.2744, lng: 133.7751, access: 100.0 },
            'Austria': { lat: 47.5162, lng: 14.5501, access: 100.0 },
            'Bangladesh': { lat: 23.6850, lng: 90.3563, access: 92.2 },
            'Belgium': { lat: 50.5039, lng: 4.4699, access: 100.0 },
            'Brazil': { lat: -14.2350, lng: -51.9253, access: 99.7 },
            'Canada': { lat: 56.1304, lng: -106.3468, access: 100.0 },
            'Chad': { lat: 15.4542, lng: 18.7322, access: 11.1 },
            'Chile': { lat: -35.6751, lng: -71.5430, access: 99.8 },
            'China': { lat: 35.8617, lng: 104.1954, access: 100.0 },
            'Colombia': { lat: 4.5709, lng: -74.2973, access: 97.4 },
            'Costa Rica': { lat: 9.7489, lng: -83.7534, access: 99.7 },
            'Denmark': { lat: 56.2639, lng: 9.5018, access: 100.0 },
            'Egypt': { lat: 26.8206, lng: 30.8025, access: 99.6 },
            'Ethiopia': { lat: 9.1450, lng: 40.4897, access: 44.3 },
            'Finland': { lat: 61.9241, lng: 25.7482, access: 100.0 },
            'France': { lat: 46.6034, lng: 1.8883, access: 100.0 },
            'Germany': { lat: 51.1657, lng: 10.4515, access: 100.0 },
            'Ghana': { lat: 7.9465, lng: -1.0232, access: 85.0 },
            'Greece': { lat: 39.0742, lng: 21.8243, access: 100.0 },
            'Iceland': { lat: 64.9631, lng: -19.0208, access: 100.0 },
            'India': { lat: 20.5937, lng: 78.9629, access: 95.2 },
            'Indonesia': { lat: -0.7893, lng: 113.9213, access: 97.8 },
            'Iran': { lat: 32.4279, lng: 53.6880, access: 100.0 },
            'Iraq': { lat: 33.2232, lng: 43.6793, access: 100.0 },
            'Ireland': { lat: 53.4129, lng: -8.2439, access: 100.0 },
            'Italy': { lat: 41.8719, lng: 12.5674, access: 100.0 },
            'Japan': { lat: 36.2048, lng: 138.2529, access: 100.0 },
            'Kenya': { lat: -0.0236, lng: 37.9062, access: 71.4 },
            'Madagascar': { lat: -18.7669, lng: 46.8691, access: 26.6 },
            'Malaysia': { lat: 4.2105, lng: 101.9758, access: 99.8 },
            'Mexico': { lat: 23.6345, lng: -102.5528, access: 99.4 },
            'Morocco': { lat: 31.7917, lng: -7.0926, access: 99.4 },
            'Myanmar': { lat: 21.9162, lng: 95.9560, access: 70.1 },
            'Nepal': { lat: 28.3949, lng: 84.1240, access: 90.7 },
            'Netherlands': { lat: 52.1326, lng: 5.2913, access: 100.0 },
            'New Zealand': { lat: -40.9006, lng: 174.8860, access: 100.0 },
            'Nigeria': { lat: 9.0820, lng: 8.6753, access: 62.0 },
            'Norway': { lat: 60.4720, lng: 8.4689, access: 100.0 },
            'Pakistan': { lat: 30.3753, lng: 69.3451, access: 73.1 },
            'Philippines': { lat: 12.8797, lng: 121.7740, access: 94.8 },
            'Poland': { lat: 51.9194, lng: 19.1451, access: 100.0 },
            'Portugal': { lat: 39.3999, lng: -8.2245, access: 100.0 },
            'Russia': { lat: 61.5240, lng: 105.3188, access: 100.0 },
            'Saudi Arabia': { lat: 23.8859, lng: 45.0792, access: 100.0 },
            'South Africa': { lat: -30.5595, lng: 22.9375, access: 84.2 },
            'South Korea': { lat: 35.9078, lng: 127.7669, access: 100.0 },
            'Spain': { lat: 40.4637, lng: -3.7492, access: 100.0 },
            'Sweden': { lat: 60.1282, lng: 18.6435, access: 100.0 },
            'Switzerland': { lat: 46.8182, lng: 8.2275, access: 100.0 },
            'Tanzania': { lat: -6.3690, lng: 34.8888, access: 38.8 },
            'Thailand': { lat: 15.8700, lng: 100.9925, access: 99.8 },
            'Turkey': { lat: 38.9637, lng: 35.2433, access: 100.0 },
            'Uganda': { lat: 1.3733, lng: 32.2903, access: 57.3 },
            'Ukraine': { lat: 48.3794, lng: 31.1656, access: 100.0 },
            'United Kingdom': { lat: 55.3781, lng: -3.4360, access: 100.0 },
            'United States': { lat: 37.0902, lng: -95.7129, access: 100.0 },
            'Uruguay': { lat: -32.5228, lng: -55.7658, access: 99.7 },
            'Venezuela': { lat: 6.4238, lng: -66.5897, access: 99.0 },
            'Vietnam': { lat: 14.0583, lng: 108.2772, access: 99.0 }
        };'''
        
        # Find where to insert the coordinates (after ML model configurations)
        ml_models_end = '''        };

        // Initialize the application'''
        
        if ml_models_end in content:
            content = content.replace(ml_models_end, '        };\n' + country_coordinates + '\n        // Initialize the application')
            print("✅ Added country coordinates data")
        
        # Add map marker management variables
        map_variables = '''        // Global variables
        let map;
        let currentCountry = null;
        let currentTimePeriod = 'all';
        let currentChartType = 'timeline';
        let currentMLModel = 'xgboost';
        let countries = [];
        let realTimeInterval;
        let currentMarker = null; // Track current country marker'''
        
        old_variables = '''        // Global variables
        let map;
        let currentCountry = null;
        let currentTimePeriod = 'all';
        let currentChartType = 'timeline';
        let currentMLModel = 'xgboost';
        let countries = [];
        let realTimeInterval;'''
        
        if old_variables in content:
            content = content.replace(old_variables, map_variables)
            print("✅ Added currentMarker variable")
        
        # Add function to highlight country on map
        highlight_function = '''
        function highlightCountryOnMap(countryName) {
            if (!map || !countryCoordinates[countryName]) {
                console.log(`Country coordinates not found for: ${countryName}`);
                return;
            }
            
            const coords = countryCoordinates[countryName];
            
            // Remove existing marker if any
            if (currentMarker) {
                map.removeLayer(currentMarker);
            }
            
            // Create custom icon for the country marker
            const countryIcon = L.divIcon({
                className: 'country-marker',
                html: `
                    <div class="marker-pin">
                        <div class="marker-icon">📍</div>
                    </div>
                    <div class="marker-popup">
                        <strong>${countryName}</strong><br>
                        Electricity Access: ${coords.access}%
                    </div>
                `,
                iconSize: [40, 60],
                iconAnchor: [20, 60],
                popupAnchor: [0, -60]
            });
            
            // Add marker to map
            currentMarker = L.marker([coords.lat, coords.lng], { icon: countryIcon })
                .addTo(map)
                .bindPopup(`
                    <div class="country-popup">
                        <h4><strong>${countryName}</strong></h4>
                        <p><i class="fas fa-bolt"></i> Electricity Access: <strong>${coords.access}%</strong></p>
                        <button onclick="searchCountry()" class="btn btn-sm btn-primary">
                            <i class="fas fa-chart-line"></i> View Full Analysis
                        </button>
                    </div>
                `, {
                    maxWidth: 250,
                    className: 'custom-popup'
                });
            
            // Center map on country with smooth animation
            map.flyTo([coords.lat, coords.lng], 5, {
                animate: true,
                duration: 1.5
            });
            
            // Open popup after animation
            setTimeout(() => {
                currentMarker.openPopup();
            }, 1600);
            
            console.log(`Highlighted ${countryName} on map`);
        }'''
        
        # Insert the highlight function before the existing functions
        before_load_map = '''        function loadMapData() {'''
        
        if before_load_map in content:
            content = content.replace(before_load_map, highlight_function + '\n        ' + before_load_map)
            print("✅ Added highlightCountryOnMap function")
        
        # Add CSS styles for the custom markers and popups
        marker_css = '''        .country-marker {
            background: transparent;
            border: none;
        }
        
        .marker-pin {
            position: relative;
            text-align: center;
        }
        
        .marker-icon {
            font-size: 2rem;
            filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.3));
            animation: bounce 2s infinite;
        }
        
        .marker-popup {
            position: absolute;
            top: -80px;
            left: 50%;
            transform: translateX(-50%);
            background: white;
            padding: 8px 12px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            font-size: 0.8rem;
            white-space: nowrap;
            border: 2px solid var(--secondary-color);
            z-index: 1000;
        }
        
        .marker-popup::after {
            content: '';
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translateX(-50%);
            border: 8px solid transparent;
            border-top-color: var(--secondary-color);
        }
        
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {
                transform: translateY(0);
            }
            40% {
                transform: translateY(-10px);
            }
            60% {
                transform: translateY(-5px);
            }
        }
        
        .custom-popup .leaflet-popup-content {
            margin: 15px;
        }
        
        .country-popup h4 {
            margin: 0 0 10px 0;
            color: var(--primary-color);
        }
        
        .country-popup p {
            margin: 5px 0;
            color: #666;
        }
        
        .country-popup .btn {
            margin-top: 10px;
        }'''
        
        # Find where to insert the CSS (before the media queries)
        before_media = '''        @media (max-width: 768px) {'''
        
        if before_media in content:
            content = content.replace(before_media, marker_css + '\n        ' + before_media)
            print("✅ Added marker CSS styles")
        
        # Update the searchCountry function to highlight the country on map
        old_search_country = '''        function searchCountry() {
            const countryName = document.getElementById('countryInput').value.trim();
            if (!countryName) return;

            currentCountry = countryName;
            showLoading(true);
            
            // Update ML model info
            updateMLModelInfo();
            
            // Fetch country data with predictions
            Promise.all([
                fetchCountryData(countryName),
                fetchPredictions(countryName),
                fetchEnergyMix(countryName)
            ]).then(([countryData, predictions, energyMix]) => {
                showLoading(false);
                displayResults(countryData, predictions, energyMix);
                updateCharts(countryData, predictions, energyMix);
            }).catch(error => {
                showLoading(false);
                showError('Country not found or data unavailable');
                console.error('Error:', error);
            });
        }'''
        
        new_search_country = '''        function searchCountry() {
            const countryName = document.getElementById('countryInput').value.trim();
            if (!countryName) return;

            currentCountry = countryName;
            showLoading(true);
            
            // Highlight country on map
            highlightCountryOnMap(countryName);
            
            // Update ML model info
            updateMLModelInfo();
            
            // Fetch country data with predictions
            Promise.all([
                fetchCountryData(countryName),
                fetchPredictions(countryName),
                fetchEnergyMix(countryName)
            ]).then(([countryData, predictions, energyMix]) => {
                showLoading(false);
                displayResults(countryData, predictions, energyMix);
                updateCharts(countryData, predictions, energyMix);
            }).catch(error => {
                showLoading(false);
                showError('Country not found or data unavailable');
                console.error('Error:', error);
            });
        }'''
        
        if old_search_country in content:
            content = content.replace(old_search_country, new_search_country)
            print("✅ Updated searchCountry function to highlight map")
        
        # Update the selectCountryFromList function to also highlight on map
        old_select_from_list = '''        function selectCountryFromList(country) {
            document.getElementById('countryInput').value = country;
            document.getElementById('countryDropdown').style.display = 'none';
            document.querySelector('.dropdown-arrow').classList.remove('active');
            
            // Clear traditional suggestions
            document.getElementById('countrySuggestions').innerHTML = '';
            
            console.log(`Selected country: ${country}`);
        }'''
        
        new_select_from_list = '''        function selectCountryFromList(country) {
            document.getElementById('countryInput').value = country;
            document.getElementById('countryDropdown').style.display = 'none';
            document.querySelector('.dropdown-arrow').classList.remove('active');
            
            // Clear traditional suggestions
            document.getElementById('countrySuggestions').innerHTML = '';
            
            // Highlight on map immediately
            highlightCountryOnMap(country);
            
            console.log(`Selected country: ${country}`);
        }'''
        
        if old_select_from_list in content:
            content = content.replace(old_select_from_list, new_select_from_list)
            print("✅ Updated selectCountryFromList to highlight map")
        
        # Write the updated content back to the file
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully added country map identification!")
        return True
        
    except Exception as e:
        print(f"❌ Error adding map identification: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Adding Country Map Identification...")
    success = add_country_map_identification()
    
    if success:
        print("\n✅ COUNTRY MAP IDENTIFICATION ADDED!")
        print("\n🗺️ Map Features:")
        print("1. ✅ Auto-highlight searched countries with animated markers")
        print("2. ✅ Custom popup showing country name and electricity access")
        print("3. ✅ Smooth map animation to center on selected country")
        print("4. ✅ Bouncing pin animation for visual appeal")
        print("5. ✅ 'View Full Analysis' button in popup")
        print("\n📍 Supported Countries:")
        print("   • 50+ major countries with exact coordinates")
        print("   • Includes: USA, India, China, Germany, Brazil, etc.")
        print("   • Real electricity access percentages")
        print("\n🎯 User Experience:")
        print("   • Search 'India' → Map centers on India with marker")
        print("   • Click marker → Shows popup with country info")
        print("   • Select from dropdown → Instantly highlights on map")
        print("   • Smooth animations and professional styling")
        print("\n⚡ Restart your Django server to see the map identification!")
    else:
        print("\n❌ Failed to add map identification.")