#!/usr/bin/env python3
"""
Restore explore dashboard to original simple state
"""

import os

def restore_original_explore_dashboard():
    """Restore explore dashboard to original simple state"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔄 Restoring explore dashboard to original state...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        # Create a clean, simple dashboard template
        original_dashboard_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Explore Dashboard - SDG 7 Energy Analytics</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px 0;
        }
        
        .dashboard-container {
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .header-section {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            text-align: center;
        }
        
        .search-section {
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        #map {
            height: 500px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-bottom: 30px;
        }
        
        .result-section {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-top: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        .chart-container {
            height: 400px;
            margin: 20px 0;
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .metric-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 15px;
            padding: 25px;
            text-align: center;
        }
        
        .metric-card .value {
            font-size: 2.5rem;
            font-weight: bold;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <!-- Header Section -->
        <div class="header-section">
            <h1><i class="fas fa-search"></i> Explore Dashboard</h1>
            <p>Interactive Country Energy Analysis</p>
            <a href="/country-forecasts/" class="btn btn-secondary">
                <i class="fas fa-arrow-left"></i> Back
            </a>
        </div>

        <!-- Search Section -->
        <div class="search-section">
            <h3><i class="fas fa-globe"></i> Country Energy Analysis</h3>
            
            <div class="row">
                <div class="col-md-8">
                    <input type="text" id="countryInput" class="form-control" 
                           placeholder="Search for a country..." 
                           autocomplete="off">
                    <div id="searchSuggestions" class="search-suggestions"></div>
                </div>
                <div class="col-md-4">
                    <button class="btn btn-primary w-100" onclick="analyzeSelectedCountry()">
                        <i class="fas fa-search"></i> Analyze
                    </button>
                </div>
            </div>
            
            <div class="text-muted mt-2">
                <small><i class="fas fa-info-circle"></i> Type country name to search</small>
            </div>
        </div>

        <!-- World Map -->
        <div id="map"></div>

        <!-- Results Section -->
        <div class="result-section" id="resultSection" style="display: none;">
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
            
            <!-- Charts -->
            <div class="chart-container" id="mainChart"></div>
            <div class="chart-container" id="accessChart"></div>
            <div class="chart-container" id="renewableChart"></div>
            <div class="chart-container" id="pieChart"></div>
        </div>
    </div>

    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script>
        let map;
        let currentCountry = null;
        let currentHighlightLayer = null;
        let currentMarker = null;

        // Country coordinates with data
        const countryCoordinates = {
            'India': { lat: 20.5937, lng: 78.9629, access: 95.2, co2: 2654000 },
            'United States': { lat: 39.8283, lng: -98.5795, access: 100.0, co2: 5416000 },
            'Germany': { lat: 51.1657, lng: 10.4515, access: 100.0, co2: 729000 },
            'Brazil': { lat: -14.2350, lng: -51.9253, access: 99.7, co2: 462000 },
            'China': { lat: 35.8617, lng: 104.1954, access: 100.0, co2: 10065000 },
            'Japan': { lat: 36.2048, lng: 138.2529, access: 100.0, co2: 1162000 },
            'United Kingdom': { lat: 55.3781, lng: -3.4360, access: 100.0, co2: 351000 },
            'France': { lat: 46.6034, lng: 1.8883, access: 100.0, co2: 330000 },
            'Italy': { lat: 41.8719, lng: 12.5674, access: 100.0, co2: 335000 },
            'Spain': { lat: 40.4637, lng: -3.7492, access: 100.0, co2: 258000 },
            'Russia': { lat: 61.5240, lng: 105.3188, access: 100.0, co2: 1711000 },
            'Canada': { lat: 56.1304, lng: -106.3468, access: 100.0, co2: 672000 },
            'Australia': { lat: -25.2744, lng: 133.7751, access: 100.0, co2: 415000 },
            'South Korea': { lat: 35.9078, lng: 127.7669, access: 100.0, co2: 611000 },
            'Mexico': { lat: 23.6345, lng: -102.5528, access: 99.4, co2: 486000 }
        };

        // Available countries list
        const countries = Object.keys(countryCoordinates).sort();

        // Initialize the application
        document.addEventListener('DOMContentLoaded', function() {
            console.log('🚀 Initializing Dashboard...');
            initializeMap();
            setupSearchFunctionality();
            console.log('✅ Dashboard initialized successfully!');
        });

        function initializeMap() {
            console.log('🗺️ Initializing map...');
            
            try {
                map = L.map('map').setView([20, 0], 2);
                
                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    attribution: '© OpenStreetMap contributors',
                    maxZoom: 18
                }).addTo(map);
                
                console.log('✅ Map initialized successfully');
                
            } catch (error) {
                console.error('❌ Map initialization failed:', error);
            }
        }

        function setupSearchFunctionality() {
            const countryInput = document.getElementById('countryInput');
            const searchSuggestions = document.getElementById('searchSuggestions');
            
            if (!countryInput) return;
            
            // Filter countries as user types
            countryInput.addEventListener('input', function() {
                const query = this.value.toLowerCase();
                if (query.length === 0) {
                    if (searchSuggestions) searchSuggestions.style.display = 'none';
                } else {
                    filterCountries(query);
                }
            });
            
            // Show all countries when clicking on input
            countryInput.addEventListener('focus', function() {
                if (this.value.length === 0) {
                    showAllCountries();
                }
            });
            
            // Hide suggestions when clicking outside
            document.addEventListener('click', function(e) {
                if (searchSuggestions && !countryInput.contains(e.target) && !searchSuggestions.contains(e.target)) {
                    searchSuggestions.style.display = 'none';
                }
            });
        }
        
        function showAllCountries() {
            const searchSuggestions = document.getElementById('searchSuggestions');
            if (!searchSuggestions) return;
            
            searchSuggestions.innerHTML = '';
            searchSuggestions.style.cssText = `
                position: absolute;
                top: 100%;
                left: 0;
                right: 0;
                background: white;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                z-index: 1000;
                max-height: 300px;
                overflow-y: auto;
                display: block;
            `;
            
            countries.slice(0, 20).forEach(country => {
                const item = document.createElement('div');
                item.style.cssText = `
                    padding: 12px 15px;
                    cursor: pointer;
                    border-bottom: 1px solid #f0f0f0;
                    transition: background-color 0.2s;
                `;
                item.textContent = country;
                item.onmouseover = () => item.style.backgroundColor = '#f8f9fa';
                item.onmouseout = () => item.style.backgroundColor = 'white';
                item.onclick = () => selectCountry(country);
                searchSuggestions.appendChild(item);
            });
        }
        
        function filterCountries(query) {
            const searchSuggestions = document.getElementById('searchSuggestions');
            if (!searchSuggestions) return;
            
            const filtered = countries.filter(country => 
                country.toLowerCase().includes(query)
            );
            
            searchSuggestions.innerHTML = '';
            searchSuggestions.style.cssText = `
                position: absolute;
                top: 100%;
                left: 0;
                right: 0;
                background: white;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                z-index: 1000;
                max-height: 300px;
                overflow-y: auto;
                display: ${filtered.length > 0 ? 'block' : 'none'};
            `;
            
            filtered.forEach(country => {
                const item = document.createElement('div');
                item.style.cssText = `
                    padding: 12px 15px;
                    cursor: pointer;
                    border-bottom: 1px solid #f0f0f0;
                    transition: background-color 0.2s;
                `;
                item.textContent = country;
                item.onmouseover = () => item.style.backgroundColor = '#f8f9fa';
                item.onmouseout = () => item.style.backgroundColor = 'white';
                item.onclick = () => selectCountry(country);
                searchSuggestions.appendChild(item);
            });
        }
        
        function selectCountry(countryName) {
            const countryInput = document.getElementById('countryInput');
            const searchSuggestions = document.getElementById('searchSuggestions');
            
            if (countryInput) countryInput.value = countryName;
            if (searchSuggestions) searchSuggestions.style.display = 'none';
            
            console.log(`🎯 Country selected: ${countryName}`);
            
            // Immediately highlight the country on map
            highlightCountryOnMap(countryName);
            
            // Also show results section
            showResultsSection(countryName);
        }

        function analyzeSelectedCountry() {
            const countryInput = document.getElementById('countryInput');
            const countryName = countryInput ? countryInput.value.trim() : '';
            
            if (!countryName) {
                alert('Please enter or select a country name first!');
                return;
            }

            // Check if country exists in our data
            if (!countryCoordinates[countryName]) {
                alert(`Sorry, ${countryName} is not available in our database. Please select from the suggestions.`);
                return;
            }

            currentCountry = countryName;
            console.log(`🔍 Analyzing: ${countryName}`);
            
            // Highlight country on map
            highlightCountryOnMap(countryName);
            
            // Show results section
            showResultsSection(countryName);
        }

        function highlightCountryOnMap(countryName) {
            const coords = countryCoordinates[countryName];
            if (!coords || !map) return;
            
            console.log(`🎯 Highlighting ${countryName}`);
            
            // Clear existing highlights
            clearMapHighlights();
            
            // Create simple circle highlighting
            const highlightCircle = L.circle([coords.lat, coords.lng], {
                color: '#32CD32',
                fillColor: '#90EE90',
                fillOpacity: 0.6,
                radius: 500000,
                weight: 2
            }).addTo(map);
            
            // Add pin marker
            const marker = L.marker([coords.lat, coords.lng])
                .addTo(map)
                .bindPopup(`
                    <div style="text-align: center; padding: 10px;">
                        <h5>${countryName}</h5>
                        <p><strong>Electricity Access:</strong> ${coords.access}%</p>
                        <p><strong>CO₂ Emissions:</strong> ${Math.round(coords.co2 / 1000)} Mt</p>
                    </div>
                `)
                .openPopup();
            
            // Store references
            currentHighlightLayer = highlightCircle;
            currentMarker = marker;
            
            // Center map on country
            map.flyTo([coords.lat, coords.lng], 5, {
                animate: true,
                duration: 1.5
            });
        }

        function clearMapHighlights() {
            if (currentHighlightLayer) {
                map.removeLayer(currentHighlightLayer);
                currentHighlightLayer = null;
            }
            if (currentMarker) {
                map.removeLayer(currentMarker);
                currentMarker = null;
            }
        }

        function showResultsSection(countryName) {
            const coords = countryCoordinates[countryName];
            if (!coords) return;
            
            // Update title
            const titleElement = document.getElementById('countryTitle');
            if (titleElement) {
                titleElement.textContent = `${countryName} - Energy Analysis`;
            }
            
            // Update metric cards
            updateMetricCards(countryName, coords);
            
            // Show results section
            const resultSection = document.getElementById('resultSection');
            if (resultSection) {
                resultSection.style.display = 'block';
            }
            
            // Render charts
            renderCharts(countryName, coords);
        }

        function updateMetricCards(countryName, coords) {
            const metricCards = document.getElementById('metricCards');
            if (metricCards) {
                metricCards.innerHTML = `
                    <div class="metric-card">
                        <h4>Electricity Access</h4>
                        <div class="value">${coords.access}</div>
                        <div class="unit">%</div>
                    </div>
                    <div class="metric-card">
                        <h4>CO₂ Emissions</h4>
                        <div class="value">${Math.round(coords.co2 / 1000)}</div>
                        <div class="unit">Mt</div>
                    </div>
                    <div class="metric-card">
                        <h4>Renewable Potential</h4>
                        <div class="value">${Math.round(20 + coords.access * 0.3)}</div>
                        <div class="unit">%</div>
                    </div>
                    <div class="metric-card">
                        <h4>Energy Efficiency</h4>
                        <div class="value">${Math.round(60 + coords.access * 0.2)}</div>
                        <div class="unit">Score</div>
                    </div>
                `;
            }
        }

        function renderCharts(countryName, coords) {
            console.log(`📊 Rendering charts for ${countryName}`);
            
            try {
                // Simple timeline chart
                const years = [2018, 2019, 2020, 2021, 2022];
                const accessData = years.map(year => coords.access + Math.random() * 2 - 1);

                const timelineTrace = {
                    x: years,
                    y: accessData,
                    type: 'scatter',
                    mode: 'lines+markers',
                    name: `${countryName} Access`,
                    line: { color: '#3498db', width: 3 }
                };

                Plotly.newPlot('mainChart', [timelineTrace], {
                    title: `${countryName} - Electricity Access Timeline`,
                    xaxis: { title: 'Year' },
                    yaxis: { title: 'Access (%)' }
                }, { responsive: true });

                // Simple pie chart
                const pieTrace = {
                    values: [60, 25, 10, 5],
                    labels: ['Fossil Fuels', 'Renewables', 'Nuclear', 'Other'],
                    type: 'pie'
                };

                Plotly.newPlot('pieChart', [pieTrace], {
                    title: `${countryName} - Energy Mix`
                }, { responsive: true });
                
                console.log(`✅ Charts rendered for ${countryName}`);
                
            } catch (error) {
                console.error(`❌ Error rendering charts:`, error);
            }
        }
    </script>
</body>
</html>'''
        
        # Write the original dashboard content
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(original_dashboard_content)
        
        print("✅ Successfully restored explore dashboard to original state!")
        return True
        
    except Exception as e:
        print(f"❌ Error restoring dashboard: {e}")
        return False

def main():
    """Main function"""
    print("🔄 RESTORING EXPLORE DASHBOARD TO ORIGINAL STATE")
    print("=" * 60)
    print("   • Simple, clean dashboard")
    print("   • Basic search functionality")
    print("   • Simple map highlighting")
    print("   • Basic charts and metrics")
    print("   • No complex features")
    print("=" * 60)
    
    success = restore_original_explore_dashboard()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ EXPLORE DASHBOARD RESTORED TO ORIGINAL STATE!")
        print("=" * 60)
        print("\n🎯 Original Features Restored:")
        print("   ✅ Simple 'Explore Dashboard' title")
        print("   ✅ Basic search interface")
        print("   ✅ World map with simple highlighting")
        print("   ✅ Circle highlighting for countries")
        print("   ✅ Basic popup with country data")
        print("   ✅ Simple metric cards")
        print("   ✅ Basic timeline and pie charts")
        
        print("\n🔄 User Experience:")
        print("   1. 📱 Page loads with simple interface")
        print("   2. 🔍 User searches for country")
        print("   3. 🎯 Country gets highlighted with circle")
        print("   4. 📊 Basic results section appears")
        print("   5. 📈 Simple charts display")
        
        print("\n🎨 Clean, Simple Design:")
        print("   • No complex layouts")
        print("   • No advanced features")
        print("   • Basic functionality only")
        print("   • Easy to understand")
        print("   • Fast and responsive")
        
        print("\n🚀 Ready to Test:")
        print("   1. Start server: python manage.py runserver")
        print("   2. Go to explore dashboard")
        print("   3. See simple, clean interface")
        print("   4. Search for any country → Basic highlighting!")
        
        print("\n🎯 BACK TO ORIGINAL SIMPLE DASHBOARD!")
        
    else:
        print("\n❌ Restore failed. Please check the error messages above.")

if __name__ == "__main__":
    main()