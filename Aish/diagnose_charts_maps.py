#!/usr/bin/env python3
"""
Diagnose Charts and Maps Issues
===============================

This script creates a diagnostic HTML file to test charts and maps functionality.
"""

def create_diagnostic_test():
    """Create a diagnostic test HTML file"""
    
    diagnostic_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Charts and Maps Diagnostic Test</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .test-section { margin: 20px 0; padding: 20px; border: 2px solid #ccc; border-radius: 10px; }
        .test-button { background: #3498db; color: white; padding: 10px 20px; border: none; border-radius: 5px; margin: 5px; cursor: pointer; }
        .test-button:hover { background: #2980b9; }
        #map { height: 300px; width: 100%; border: 2px solid #ccc; margin: 10px 0; }
        #chart { height: 300px; width: 100%; border: 2px solid #ccc; margin: 10px 0; }
        .log { background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0; font-family: monospace; font-size: 12px; max-height: 200px; overflow-y: auto; }
        .success { color: green; font-weight: bold; }
        .error { color: red; font-weight: bold; }
    </style>
</head>
<body>
    <h1>🔧 Charts and Maps Diagnostic Test</h1>
    
    <div class="test-section">
        <h2>📊 Chart Library Test</h2>
        <button class="test-button" onclick="testPlotly()">Test Plotly.js</button>
        <button class="test-button" onclick="testTimelineChart()">Test Timeline Chart</button>
        <button class="test-button" onclick="testPieChart()">Test Pie Chart</button>
        <div id="chart"></div>
    </div>
    
    <div class="test-section">
        <h2>🗺️ Map Library Test</h2>
        <button class="test-button" onclick="testLeaflet()">Test Leaflet.js</button>
        <button class="test-button" onclick="testMapMarkers()">Test Map Markers</button>
        <button class="test-button" onclick="testCountryHighlight()">Test Country Highlight</button>
        <div id="map"></div>
    </div>
    
    <div class="test-section">
        <h2>🌐 API Test</h2>
        <button class="test-button" onclick="testCountryAPI()">Test Country Search API</button>
        <button class="test-button" onclick="testMapDataAPI()">Test Map Data API</button>
    </div>
    
    <div class="log" id="log">
        <strong>Diagnostic Log:</strong><br>
        Click test buttons to diagnose issues...
    </div>

    <script>
        let map;
        
        function log(message, type = 'info') {
            const logDiv = document.getElementById('log');
            const timestamp = new Date().toLocaleTimeString();
            const className = type === 'success' ? 'success' : type === 'error' ? 'error' : '';
            logDiv.innerHTML += `<br><span class="${className}">${timestamp}: ${message}</span>`;
            logDiv.scrollTop = logDiv.scrollHeight;
        }
        
        function testPlotly() {
            log('Testing Plotly.js library...');
            
            if (typeof Plotly === 'undefined') {
                log('❌ Plotly.js is NOT loaded!', 'error');
                return;
            }
            
            log('✅ Plotly.js is loaded successfully', 'success');
            log(`Plotly version: ${Plotly.version || 'unknown'}`);
        }
        
        function testTimelineChart() {
            log('Testing timeline chart rendering...');
            
            if (typeof Plotly === 'undefined') {
                log('❌ Plotly.js not available', 'error');
                return;
            }
            
            try {
                const trace = {
                    x: [2020, 2021, 2022, 2023, 2024, 2025],
                    y: [85, 87, 89, 91, 93, 95],
                    type: 'scatter',
                    mode: 'lines+markers',
                    name: 'Test Data',
                    line: { color: '#3498db', width: 3 }
                };
                
                const layout = {
                    title: 'Test Timeline Chart',
                    xaxis: { title: 'Year' },
                    yaxis: { title: 'Value (%)' }
                };
                
                Plotly.newPlot('chart', [trace], layout, { responsive: true });
                log('✅ Timeline chart rendered successfully', 'success');
            } catch (error) {
                log(`❌ Timeline chart error: ${error.message}`, 'error');
            }
        }
        
        function testPieChart() {
            log('Testing pie chart rendering...');
            
            if (typeof Plotly === 'undefined') {
                log('❌ Plotly.js not available', 'error');
                return;
            }
            
            try {
                const trace = {
                    values: [45, 30, 15, 10],
                    labels: ['Fossil Fuels', 'Renewables', 'Nuclear', 'Other'],
                    type: 'pie',
                    marker: { colors: ['#e74c3c', '#27ae60', '#3498db', '#9b59b6'] }
                };
                
                const layout = {
                    title: 'Test Pie Chart'
                };
                
                Plotly.newPlot('chart', [trace], layout, { responsive: true });
                log('✅ Pie chart rendered successfully', 'success');
            } catch (error) {
                log(`❌ Pie chart error: ${error.message}`, 'error');
            }
        }
        
        function testLeaflet() {
            log('Testing Leaflet.js library...');
            
            if (typeof L === 'undefined') {
                log('❌ Leaflet.js is NOT loaded!', 'error');
                return;
            }
            
            log('✅ Leaflet.js is loaded successfully', 'success');
            log(`Leaflet version: ${L.version || 'unknown'}`);
            
            try {
                if (map) {
                    map.remove();
                }
                
                map = L.map('map').setView([20, 0], 2);
                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    attribution: '© OpenStreetMap contributors'
                }).addTo(map);
                
                log('✅ Map initialized successfully', 'success');
            } catch (error) {
                log(`❌ Map initialization error: ${error.message}`, 'error');
            }
        }
        
        function testMapMarkers() {
            log('Testing map markers...');
            
            if (!map) {
                log('❌ Map not initialized. Run Leaflet test first.', 'error');
                return;
            }
            
            try {
                // Add test markers
                const testLocations = [
                    { name: 'India', lat: 20.5937, lng: 78.9629 },
                    { name: 'USA', lat: 39.8283, lng: -98.5795 },
                    { name: 'Germany', lat: 51.1657, lng: 10.4515 }
                ];
                
                testLocations.forEach(location => {
                    L.marker([location.lat, location.lng])
                        .addTo(map)
                        .bindPopup(`<strong>${location.name}</strong><br>Test marker`);
                });
                
                log('✅ Map markers added successfully', 'success');
            } catch (error) {
                log(`❌ Map markers error: ${error.message}`, 'error');
            }
        }
        
        function testCountryHighlight() {
            log('Testing country highlighting...');
            
            if (!map) {
                log('❌ Map not initialized. Run Leaflet test first.', 'error');
                return;
            }
            
            try {
                // Add a test circle highlight
                const circle = L.circle([20.5937, 78.9629], {
                    color: '#22c55e',
                    fillColor: '#dcfce7',
                    fillOpacity: 0.6,
                    radius: 500000
                }).addTo(map);
                
                circle.bindPopup('<strong>India</strong><br>Test highlight').openPopup();
                map.setView([20.5937, 78.9629], 5);
                
                log('✅ Country highlighting test successful', 'success');
            } catch (error) {
                log(`❌ Country highlighting error: ${error.message}`, 'error');
            }
        }
        
        function testCountryAPI() {
            log('Testing country search API...');
            
            fetch('/api/search/?country=India')
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.found) {
                        log('✅ Country API working - India found', 'success');
                        log(`India electricity access: ${data.electricity_access}%`);
                    } else {
                        log('⚠️ Country API working but India not found', 'error');
                    }
                })
                .catch(error => {
                    log(`❌ Country API error: ${error.message}`, 'error');
                });
        }
        
        function testMapDataAPI() {
            log('Testing map data API...');
            
            fetch('/api/map-data/')
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.map_data && data.map_data.length > 0) {
                        log(`✅ Map data API working - ${data.map_data.length} countries loaded`, 'success');
                    } else {
                        log('⚠️ Map data API working but no data returned', 'error');
                    }
                })
                .catch(error => {
                    log(`❌ Map data API error: ${error.message}`, 'error');
                });
        }
        
        // Auto-run basic tests on page load
        window.onload = function() {
            log('🔧 Starting diagnostic tests...');
            setTimeout(() => {
                testPlotly();
                testLeaflet();
            }, 1000);
        };
    </script>
</body>
</html>'''
    
    with open('Aish/diagnose_charts_maps.html', 'w', encoding='utf-8') as f:
        f.write(diagnostic_html)
    
    print("📄 Created diagnostic test file: Aish/diagnose_charts_maps.html")

def main():
    """Main function"""
    print("🔧 CREATING CHARTS AND MAPS DIAGNOSTIC TEST")
    print("=" * 60)
    
    create_diagnostic_test()
    
    print("\n✅ DIAGNOSTIC TEST CREATED!")
    print("=" * 60)
    print("\n🧪 How to use:")
    print("   1. Open Aish/diagnose_charts_maps.html in your browser")
    print("   2. Click test buttons to diagnose issues")
    print("   3. Check the log for success/error messages")
    print("   4. Use results to identify specific problems")
    
    print("\n🎯 Tests available:")
    print("   • Plotly.js library loading")
    print("   • Chart rendering (timeline, pie)")
    print("   • Leaflet.js library loading")
    print("   • Map initialization and markers")
    print("   • Country highlighting")
    print("   • API endpoints (/api/search/, /api/map-data/)")
    
    print("\n💡 If tests fail:")
    print("   • Check browser console (F12) for errors")
    print("   • Ensure Django server is running")
    print("   • Clear browser cache (Ctrl+F5)")
    print("   • Check network connectivity")

if __name__ == "__main__":
    main()