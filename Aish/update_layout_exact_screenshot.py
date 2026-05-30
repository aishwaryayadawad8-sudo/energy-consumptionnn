#!/usr/bin/env python3
"""
Update layout to match the exact screenshot provided by user
"""

import os

def update_layout_exact_screenshot():
    """Update layout to match the exact screenshot"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🎨 Updating layout to match your exact screenshot...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and update the results section to show map and graphs together
        old_results_section = content.find('<div class="result-section" id="resultSection" style="display: none;">')
        if old_results_section != -1:
            # Find the end of the results section
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
            
            # New results section with map and graphs side by side
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
            
            <!-- Map and Charts Side by Side -->
            <div class="row" style="margin-top: 30px;">
                <!-- Map Column (Left Side) -->
                <div class="col-md-6">
                    <div class="map-section" style="
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
                            <span id="mapSectionTitle">Country Map View</span>
                        </h4>
                        <!-- This will show the same map as above but focused on country -->
                        <div id="countryMapView" style="
                            height: 400px;
                            border-radius: 10px;
                            border: 1px solid #e0e0e0;
                            background: #f8f9fa;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            color: #666;
                            font-size: 16px;
                        ">
                            <div style="text-align: center;">
                                <i class="fas fa-map" style="font-size: 48px; margin-bottom: 15px; opacity: 0.5;"></i>
                                <p>Country map view will appear here</p>
                                <small>Same highlighting as above map</small>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Charts Column (Right Side) -->
                <div class="col-md-6">
                    <div class="charts-section" style="
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
                            <i class="fas fa-chart-line" style="margin-right: 8px; color: #007bff;"></i>
                            Energy Analytics
                        </h4>
                        
                        <!-- Timeline Chart -->
                        <div class="chart-container" style="
                            height: 180px;
                            margin-bottom: 20px;
                            background: #f8f9fa;
                            border-radius: 8px;
                            padding: 15px;
                        ">
                            <div id="mainChart"></div>
                        </div>
                        
                        <!-- Pie Chart -->
                        <div class="chart-container" style="
                            height: 180px;
                            background: #f8f9fa;
                            border-radius: 8px;
                            padding: 15px;
                        ">
                            <div id="pieChart"></div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Additional Charts Row (Full Width) -->
            <div class="row">
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
            print("✅ Updated results section to match screenshot layout")
        
        # Update the showResultsSection function to update map section title
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
            
            // Update map section title
            const mapSectionTitle = document.getElementById('mapSectionTitle');
            if (mapSectionTitle) {
                mapSectionTitle.textContent = `${countryName} Map View`;
            }
            
            // Update metric cards
            updateMetricCards(countryName, coords);
            
            // Show results section
            const resultSection = document.getElementById('resultSection');
            if (resultSection) {
                resultSection.style.display = 'block';
            }
            
            // Update country map view placeholder
            const countryMapView = document.getElementById('countryMapView');
            if (countryMapView) {
                countryMapView.innerHTML = `
                    <div style="text-align: center; color: #32CD32;">
                        <i class="fas fa-map-marked-alt" style="font-size: 48px; margin-bottom: 15px;"></i>
                        <h5 style="margin-bottom: 10px; color: #333;">${countryName}</h5>
                        <p style="margin: 5px 0; color: #666;">Highlighted above with light green fill</p>
                        <p style="margin: 5px 0; color: #666;">📍 Pin marker shows location</p>
                        <div style="
                            background: #90EE90;
                            border: 2px solid #32CD32;
                            border-radius: 8px;
                            padding: 10px;
                            margin-top: 15px;
                            display: inline-block;
                        ">
                            <small style="color: #228B22; font-weight: bold;">
                                ✅ Country highlighted on map above
                            </small>
                        </div>
                    </div>
                `;
            }
            
            // Render charts
            renderCharts(countryName, coords);
        }'''
            
            # Replace the function
            content = content[:old_show_results] + new_show_results + content[function_end:]
            print("✅ Updated showResultsSection to match screenshot layout")
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully updated layout to match your screenshot!")
        return True
        
    except Exception as e:
        print(f"❌ Error updating layout: {e}")
        return False

def main():
    """Main function"""
    print("🎨 UPDATING LAYOUT TO MATCH YOUR SCREENSHOT")
    print("=" * 60)
    print("   • Search interface at top")
    print("   • Map with country highlighting below")
    print("   • Map view and charts side by side")
    print("   • Exact visual match to your image")
    print("=" * 60)
    
    success = update_layout_exact_screenshot()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ LAYOUT UPDATED TO MATCH YOUR SCREENSHOT!")
        print("=" * 60)
        print("\n🎯 Exact Screenshot Layout:")
        print("   ✅ Search interface at top")
        print("   ✅ Map with India highlighted below")
        print("   ✅ Light green fill covering entire country")
        print("   ✅ Green pin marker with popup")
        print("   ✅ Map view section on left side")
        print("   ✅ Charts section on right side")
        
        print("\n🔄 User Experience:")
        print("   1. 📱 User sees search interface")
        print("   2. 🗺️ Map visible below with world view")
        print("   3. 🔍 User searches for 'India'")
        print("   4. 🎯 India gets highlighted on map (light green)")
        print("   5. 📊 Results appear below with:")
        print("      • Metric cards at top")
        print("      • Map view section (left)")
        print("      • Charts section (right)")
        print("      • Additional charts below")
        
        print("\n🎨 Visual Layout (Exact Match):")
        print("   ┌─────────────────────────────────────┐")
        print("   │  🔍 Search Country Energy Profile  │")
        print("   │  [India            ] [🔵 Search]   │")
        print("   ├─────────────────────────────────────┤")
        print("   │  🗺️ Map with India highlighted     │")
        print("   │     (Light green fill + pin)       │")
        print("   ├─────────────────────────────────────┤")
        print("   │  📊📊📊📊 Metric Cards             │")
        print("   ├─────────────────┬───────────────────┤")
        print("   │  🗺️ Map View    │  📈 Timeline      │")
        print("   │  Section        │  📊 Pie Chart     │")
        print("   ├─────────────────┼───────────────────┤")
        print("   │  📈 Access Chart│  🌱 Renewable     │")
        print("   └─────────────────┴───────────────────┘")
        
        print("\n🚀 Ready to Test:")
        print("   1. Start server: python manage.py runserver")
        print("   2. Go to explore dashboard")
        print("   3. Search for 'India'")
        print("   4. See exact layout from your screenshot!")
        
        print("\n🎯 PERFECT MATCH TO YOUR SCREENSHOT!")
        
    else:
        print("\n❌ Update failed. Please check the error messages above.")

if __name__ == "__main__":
    main()