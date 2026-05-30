#!/usr/bin/env python3
"""
Update dashboard to show country map alongside graphs/charts
"""

import os

def add_map_with_graphs_layout():
    """Add layout to show map with graphs side by side"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🗺️ Adding map with graphs layout...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the results section and update its layout
        old_results_section = content.find('<div class="result-section" id="resultSection" style="display: none;">')
        if old_results_section != -1:
            # Find the end of the results section
            # Look for the closing div of the result-section
            pos = old_results_section
            div_count = 0
            while pos < len(content):
                if content[pos:pos+5] == '<div ':
                    div_count += 1
                elif content[pos:pos+6] == '</div>':
                    div_count -= 1
                    if div_count == 0:
                        section_end = pos + 6
                        break
                pos += 1
            
            # New results section with map and graphs layout
            new_results_section = '''<div class="result-section" id="resultSection" style="display: none;">
            <h2 id="countryTitle">Country Analysis</h2>
            
            <!-- Metric Cards -->
            <div class="metric-cards" id="metricCards">
                <div class="metric-card">
                    <h4>Electricity Access</h4>
                    <div class="value">--</div>
                    <div class="unit">%</div>
                </div>
                <div class="metric-card">
                    <h4>CO₂ Emissions</h4>
                    <div class="value">--</div>
                    <div class="unit">Mt</div>
                </div>
                <div class="metric-card">
                    <h4>Renewable Potential</h4>
                    <div class="value">--</div>
                    <div class="unit">%</div>
                </div>
                <div class="metric-card">
                    <h4>Energy Efficiency</h4>
                    <div class="value">--</div>
                    <div class="unit">Score</div>
                </div>
            </div>
            
            <!-- Map and Charts Layout -->
            <div class="row" style="margin-top: 30px;">
                <!-- Country Map Column -->
                <div class="col-md-6">
                    <div class="map-container" style="
                        background: white;
                        border-radius: 15px;
                        padding: 20px;
                        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                        margin-bottom: 30px;
                    ">
                        <h4 style="
                            color: #333;
                            margin-bottom: 20px;
                            text-align: center;
                            font-weight: 600;
                        ">
                            <i class="fas fa-map-marked-alt" style="margin-right: 8px; color: #32CD32;"></i>
                            <span id="mapTitle">Country Location</span>
                        </h4>
                        <div id="countryMap" style="
                            height: 400px;
                            border-radius: 10px;
                            border: 1px solid #e0e0e0;
                        "></div>
                    </div>
                </div>
                
                <!-- Charts Column -->
                <div class="col-md-6">
                    <div class="charts-container">
                        <!-- Main Timeline Chart -->
                        <div class="chart-container" style="
                            height: 200px;
                            margin-bottom: 20px;
                            background: white;
                            border-radius: 10px;
                            padding: 15px;
                            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                        ">
                            <div id="mainChart"></div>
                        </div>
                        
                        <!-- Energy Mix Pie Chart -->
                        <div class="chart-container" style="
                            height: 200px;
                            margin-bottom: 20px;
                            background: white;
                            border-radius: 10px;
                            padding: 15px;
                            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                        ">
                            <div id="pieChart"></div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Additional Charts Row -->
            <div class="row" style="margin-top: 20px;">
                <div class="col-md-6">
                    <div class="chart-container" style="
                        height: 300px;
                        margin-bottom: 20px;
                        background: white;
                        border-radius: 10px;
                        padding: 20px;
                        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                    ">
                        <div id="accessChart"></div>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="chart-container" style="
                        height: 300px;
                        margin-bottom: 20px;
                        background: white;
                        border-radius: 10px;
                        padding: 20px;
                        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                    ">
                        <div id="renewableChart"></div>
                    </div>
                </div>
            </div>
        </div>'''
            
            # Replace the results section
            content = content[:old_results_section] + new_results_section + content[section_end:]
            print("✅ Updated results section with map and graphs layout")
        
        # Add function to initialize country-specific map
        # Find where to insert the new function (before the last script tag)
        script_end = content.rfind('</script>')
        if script_end != -1:
            country_map_function = '''
        
        // Initialize country-specific map
        let countryMap;
        let countryMapInitialized = false;
        
        function initializeCountryMap(countryName, coords) {
            console.log(`🗺️ Initializing country map for ${countryName}...`);
            
            try {
                // Clear existing map if any
                if (countryMap) {
                    countryMap.remove();
                }
                
                // Initialize new map focused on country
                countryMap = L.map('countryMap').setView([coords.lat, coords.lng], 6);
                
                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    attribution: '© OpenStreetMap contributors',
                    maxZoom: 18
                }).addTo(countryMap);
                
                // Update map title
                const mapTitle = document.getElementById('mapTitle');
                if (mapTitle) {
                    mapTitle.textContent = `${countryName} Location`;
                }
                
                // Add country highlighting to the country map
                highlightCountryOnCountryMap(countryName, coords);
                
                countryMapInitialized = true;
                console.log(`✅ Country map initialized for ${countryName}`);
                
            } catch (error) {
                console.error(`❌ Country map initialization failed for ${countryName}:`, error);
            }
        }
        
        function highlightCountryOnCountryMap(countryName, coords) {
            if (!countryMap) return;
            
            // Check if we have local GeoJSON data for this country
            if (localCountryBoundaries[countryName]) {
                console.log(`✅ Using local GeoJSON data for ${countryName} on country map`);
                
                // Create GeoJSON layer for country map
                const geoJsonLayer = L.geoJSON(localCountryBoundaries[countryName], {
                    style: {
                        fillColor: '#90EE90',      // Light green fill
                        weight: 2,                 // Border width
                        opacity: 1,                // Border opacity
                        color: '#32CD32',          // Border color
                        fillOpacity: 0.6           // Fill opacity
                    }
                }).addTo(countryMap);
                
                // Fit map to country boundaries
                countryMap.fitBounds(geoJsonLayer.getBounds(), {
                    padding: [20, 20]
                });
                
            } else {
                // Fallback: create circle highlighting
                const highlightCircle = L.circle([coords.lat, coords.lng], {
                    color: '#32CD32',
                    fillColor: '#90EE90',
                    fillOpacity: 0.6,
                    radius: getCountryRadius(countryName) / 2,
                    weight: 2
                }).addTo(countryMap);
            }
            
            // Add pin marker
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
            
            L.marker([coords.lat, coords.lng], { icon: customIcon })
                .addTo(countryMap)
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
                `)
                .openPopup();
        }'''
            
            # Insert the function before the closing script tag
            content = content[:script_end] + country_map_function + content[script_end:]
            print("✅ Added country map initialization functions")
        
        # Update the showResultsSection function to initialize country map
        old_show_results = content.find('function showResultsSection(countryName) {')
        if old_show_results != -1:
            # Find the end of the function
            brace_count = 0
            pos = old_show_results
            while pos < len(content):
                if content[pos] == '{':
                    brace_count += 1
                elif content[pos] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        function_end = pos + 1
                        break
                pos += 1
            
            # Updated showResultsSection function
            new_show_results = '''function showResultsSection(countryName) {
            const coords = countryCoordinates[countryName];
            if (!coords) return;
            
            // Update title
            const titleElement = document.getElementById('countryTitle');
            if (titleElement) {
                titleElement.textContent = `${countryName} - Energy Analysis Dashboard`;
            }
            
            // Update metric cards
            updateMetricCards(countryName, coords);
            
            // Show results section
            const resultSection = document.getElementById('resultSection');
            if (resultSection) {
                resultSection.style.display = 'block';
            }
            
            // Initialize country-specific map
            setTimeout(() => {
                initializeCountryMap(countryName, coords);
            }, 100);
            
            // Render charts
            renderCharts(countryName, coords);
        }'''
            
            # Replace the function
            content = content[:old_show_results] + new_show_results + content[function_end:]
            print("✅ Updated showResultsSection to initialize country map")
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully added map with graphs layout!")
        return True
        
    except Exception as e:
        print(f"❌ Error adding map with graphs layout: {e}")
        return False

def main():
    """Main function"""
    print("🗺️ ADDING MAP WITH GRAPHS LAYOUT")
    print("=" * 60)
    print("   • Country map alongside charts")
    print("   • Side-by-side layout")
    print("   • Country highlighting on both maps")
    print("   • Professional dashboard design")
    print("=" * 60)
    
    success = add_map_with_graphs_layout()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ MAP WITH GRAPHS LAYOUT ADDED!")
        print("=" * 60)
        print("\n🎯 New Layout Features:")
        print("   ✅ World map at top (for country search)")
        print("   ✅ Country-specific map on left side")
        print("   ✅ Charts and graphs on right side")
        print("   ✅ Metric cards at top of results")
        print("   ✅ Additional charts below")
        
        print("\n🔄 User Experience:")
        print("   1. 📱 User sees search interface + world map")
        print("   2. 🔍 User searches for country (e.g., 'India')")
        print("   3. 🗺️ Country gets highlighted on world map")
        print("   4. 📊 Results section appears with:")
        print("      • Metric cards showing key stats")
        print("      • Country map (left) - focused on selected country")
        print("      • Charts (right) - timeline and pie chart")
        print("      • Additional charts below")
        
        print("\n🎨 Visual Layout:")
        print("   ┌─────────────────────────────────────┐")
        print("   │  🔍 Search + 🗺️ World Map          │")
        print("   ├─────────────────────────────────────┤")
        print("   │  📊 Metric Cards (4 cards)         │")
        print("   ├─────────────────┬───────────────────┤")
        print("   │  🗺️ Country Map │  📈 Timeline      │")
        print("   │  (India focus)  │  📊 Pie Chart     │")
        print("   ├─────────────────┼───────────────────┤")
        print("   │  📈 Access Chart│  🌱 Renewable     │")
        print("   │                 │     Chart         │")
        print("   └─────────────────┴───────────────────┘")
        
        print("\n🌍 Map Features:")
        print("   • World map: Shows country in global context")
        print("   • Country map: Focused view with highlighting")
        print("   • Both maps: Light green fill + pin markers")
        print("   • Consistent styling and popups")
        
        print("\n📊 Chart Features:")
        print("   • Timeline chart: Electricity access trends")
        print("   • Pie chart: Energy source distribution")
        print("   • Access chart: Future forecasts")
        print("   • Renewable chart: Growth projections")
        
        print("\n🚀 Ready to Test:")
        print("   1. Start server: python manage.py runserver")
        print("   2. Go to explore dashboard")
        print("   3. Search for 'India'")
        print("   4. See country map + graphs together!")
        
        print("\n🎯 PERFECT MAP + GRAPHS EXPERIENCE!")
        
    else:
        print("\n❌ Update failed. Please check the error messages above.")

if __name__ == "__main__":
    main()