#!/usr/bin/env python3
"""Add country highlighting on map when selected"""

# Read the file
with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a variable to store the highlight marker at the top of the script section
old_script_start = '''    <script>
        let map;
        let charts = {};'''

new_script_start = '''    <script>
        let map;
        let charts = {};
        let highlightMarker = null;  // Store the highlighted country marker'''

content = content.replace(old_script_start, new_script_start)

# Add a function to highlight country on map
highlight_function = '''
        
        // Highlight selected country on map
        function highlightCountryOnMap(countryName, lat, lon, electricityAccess) {
            // Remove previous highlight if exists
            if (highlightMarker) {
                map.removeLayer(highlightMarker);
            }
            
            // Create a larger, highlighted marker
            highlightMarker = L.circleMarker([lat, lon], {
                radius: 15,
                fillColor: '#FFD700',  // Gold color for highlight
                color: '#FF4500',      // Orange-red border
                weight: 3,
                opacity: 1,
                fillOpacity: 0.9
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

# Find where to insert the highlight function (after loadMapData function)
insert_marker = '''        // Load countries list
        function loadCountries() {'''

content = content.replace(insert_marker, highlight_function + '\n        ' + insert_marker)

# Now update the searchCountry function to call highlightCountryOnMap
old_search_function = '''            fetch(`/api/search/?country=${encodeURIComponent(country)}`)
                .then(response => response.json())
                .then(data => {
                    loadingSpinner.style.display = 'none';
                    
                    if (!data.found) {
                        notFoundMessage.style.display = 'block';
                        document.getElementById('notFoundText').textContent = data.message;
                        return;
                    }
                    
                    displayCountryData(data);
                    loadPredictions(country);
                })'''

new_search_function = '''            fetch(`/api/search/?country=${encodeURIComponent(country)}`)
                .then(response => response.json())
                .then(data => {
                    loadingSpinner.style.display = 'none';
                    
                    if (!data.found) {
                        notFoundMessage.style.display = 'block';
                        document.getElementById('notFoundText').textContent = data.message;
                        return;
                    }
                    
                    displayCountryData(data);
                    loadPredictions(country);
                    
                    // Highlight country on map if coordinates are available
                    if (data.lat && data.lon) {
                        highlightCountryOnMap(data.country, data.lat, data.lon, data.electricity_access || 0);
                    }
                })'''

content = content.replace(old_search_function, new_search_function)

# Add CSS for the country highlight label
css_addition = '''        
        .country-highlight-label {
            background-color: #FFD700;
            border: 2px solid #FF4500;
            border-radius: 5px;
            padding: 5px 10px;
            font-weight: bold;
            font-size: 14px;
            color: #2c3e50;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }'''

# Find the style section and add the CSS
style_marker = '''    </style>
</head>'''

content = content.replace(style_marker, css_addition + '\n    ' + style_marker)

# Write back
with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Country highlighting feature added!")
print("🗺️  Features added:")
print("   • Selected country highlighted with gold marker")
print("   • Country name label displayed on map")
print("   • Map zooms to selected country")
print("   • Popup shows electricity access details")
print("   • Previous highlight removed when new country selected")
