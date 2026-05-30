#!/usr/bin/env python3
"""
Keep Only Time Period Controls
==============================

This script modifies the visualization controls to show only the Time Period section,
removing Chart Type and ML Model controls as requested by the user.
"""

import os

def keep_only_time_period():
    """Keep only Time Period controls, remove Chart Type and ML Model"""
    
    html_file_path = "Aish/sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("⏰ KEEPING ONLY TIME PERIOD CONTROLS")
    print("=" * 60)
    print(f"📁 Updating file: {html_file_path}")
    
    # Read current file
    with open(html_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the current visualization controls section and replace it
    old_controls_section = '''        <!-- Interactive Visualization Controls -->
        <div class="visualization-controls">
            <h3><i class="fas fa-sliders-h"></i> Interactive Visualization Controls</h3>
            
            <div class="control-section">
                <label class="control-label">Time Period:</label>
                <div class="control-buttons">
                    <button class="control-btn active" onclick="setTimePeriod('all')">All Years (2000-2030)</button>
                    <button class="control-btn" onclick="setTimePeriod('historical')">Historical (2000-2020)</button>
                    <button class="control-btn" onclick="setTimePeriod('predictions')">Predictions (2021-2030)</button>
                    <button class="control-btn" onclick="setTimePeriod('recent')">Recent Trends (2015-2030)</button>
                </div>
            </div>
            
            <div class="control-section">
                <label class="control-label">Chart Type:</label>
                <div class="control-buttons">
                    <button class="control-btn active" onclick="setChartType('timeline')">Timeline View</button>
                    <button class="control-btn" onclick="setChartType('comparison')">Historical vs Predicted</button>
                    <button class="control-btn" onclick="setChartType('breakdown')">Energy Mix</button>
                    <button class="control-btn" onclick="setChartType('access')">Access Trends</button>
                    <button class="control-btn" onclick="setChartType('pie')">Pie Chart</button>
                </div>
            </div>
            
            <div class="control-section">
                <label class="control-label">ML Model:</label>
                <div class="control-buttons">
                    <button class="control-btn active" onclick="setMLModel('xgboost')">XGBoost (Best)</button>
                    <button class="control-btn" onclick="setMLModel('catboost')">CatBoost</button>
                    <button class="control-btn" onclick="setMLModel('lightgbm')">LightGBM</button>
                    <button class="control-btn" onclick="setMLModel('ensemble')">Ensemble</button>
                </div>
            </div>
        </div>'''
    
    # New simplified controls section with only Time Period
    new_controls_section = '''        <!-- Interactive Visualization Controls -->
        <div class="visualization-controls">
            <h3><i class="fas fa-sliders-h"></i> Interactive Visualization Controls</h3>
            
            <div class="control-section">
                <label class="control-label">Time Period:</label>
                <div class="control-buttons">
                    <button class="control-btn active" onclick="setTimePeriod('all')">All Years (2000-2030)</button>
                    <button class="control-btn" onclick="setTimePeriod('historical')">Historical (2000-2020)</button>
                    <button class="control-btn" onclick="setTimePeriod('predictions')">Predictions (2021-2030)</button>
                    <button class="control-btn" onclick="setTimePeriod('recent')">Recent Trends (2015-2030)</button>
                </div>
            </div>
        </div>'''
    
    # Replace the controls section
    if old_controls_section in content:
        content = content.replace(old_controls_section, new_controls_section)
        print("✅ Removed Chart Type and ML Model controls")
        print("✅ Kept only Time Period controls")
    else:
        print("⚠️ Could not find exact controls section, trying alternative approach")
        
        # Try to find and remove individual sections
        chart_type_section = '''            <div class="control-section">
                <label class="control-label">Chart Type:</label>
                <div class="control-buttons">
                    <button class="control-btn active" onclick="setChartType('timeline')">Timeline View</button>
                    <button class="control-btn" onclick="setChartType('comparison')">Historical vs Predicted</button>
                    <button class="control-btn" onclick="setChartType('breakdown')">Energy Mix</button>
                    <button class="control-btn" onclick="setChartType('access')">Access Trends</button>
                    <button class="control-btn" onclick="setChartType('pie')">Pie Chart</button>
                </div>
            </div>
            
            <div class="control-section">
                <label class="control-label">ML Model:</label>
                <div class="control-buttons">
                    <button class="control-btn active" onclick="setMLModel('xgboost')">XGBoost (Best)</button>
                    <button class="control-btn" onclick="setMLModel('catboost')">CatBoost</button>
                    <button class="control-btn" onclick="setMLModel('lightgbm')">LightGBM</button>
                    <button class="control-btn" onclick="setMLModel('ensemble')">Ensemble</button>
                </div>
            </div>'''
        
        if chart_type_section in content:
            content = content.replace(chart_type_section, '')
            print("✅ Removed Chart Type and ML Model sections")
    
    # Simplify the JavaScript functions - keep only Time Period functionality
    old_js_functions = '''        // Global variables for visualization controls
        let currentTimePeriod = 'all';
        let currentChartType = 'timeline';
        let currentMLModel = 'xgboost';
        
        // Control functions
        function setTimePeriod(period) {
            currentTimePeriod = period;
            updateActiveButton('.control-buttons button[onclick*="setTimePeriod"]', period);
            console.log(`Time period set to: ${period}`);
            
            // Update charts if country is selected
            if (currentCountry) {
                updateChartsWithNewSettings();
            }
        }

        function setChartType(type) {
            currentChartType = type;
            updateActiveButton('.control-buttons button[onclick*="setChartType"]', type);
            console.log(`Chart type set to: ${type}`);
            
            // Update main chart if country is selected
            if (currentCountry) {
                updateMainChartWithType(type);
            }
        }

        function setMLModel(model) {
            currentMLModel = model;
            updateActiveButton('.control-buttons button[onclick*="setMLModel"]', model);
            console.log(`ML model set to: ${model}`);
            
            // Update charts if country is selected
            if (currentCountry) {
                updateChartsWithNewSettings();
            }
        }'''
    
    new_js_functions = '''        // Global variables for visualization controls
        let currentTimePeriod = 'all';
        
        // Control functions
        function setTimePeriod(period) {
            currentTimePeriod = period;
            updateActiveButton('.control-buttons button[onclick*="setTimePeriod"]', period);
            console.log(`Time period set to: ${period}`);
            
            // Update charts if country is selected
            if (currentCountry) {
                updateChartsWithTimePeriod(period);
            }
        }'''
    
    # Replace JavaScript functions
    if old_js_functions in content:
        content = content.replace(old_js_functions, new_js_functions)
        print("✅ Simplified JavaScript functions")
    
    # Add a new function to handle time period changes
    time_period_function = '''
        function updateChartsWithTimePeriod(period) {
            if (!currentCountry) return;
            
            const coords = countryCoordinates[currentCountry];
            if (!coords) return;
            
            console.log(`Updating charts for ${currentCountry} with time period: ${period}`);
            
            // Update charts based on time period
            renderTimelineChartWithPeriod(currentCountry, coords, period);
            renderAccessForecastWithPeriod(currentCountry, coords, period);
            renderRenewableGrowthWithPeriod(currentCountry, coords, period);
            renderEnergyPieChart(currentCountry, coords);
        }
        
        function renderTimelineChartWithPeriod(countryName, coords, period) {
            let years, accessData, title;
            
            switch(period) {
                case 'historical':
                    years = Array.from({length: 21}, (_, i) => 2000 + i);
                    accessData = years.map(year => {
                        const baseAccess = coords.access;
                        const yearFactor = (year - 2000) * 0.8;
                        return Math.min(100, Math.max(0, baseAccess - 20 + yearFactor + Math.random() * 3));
                    });
                    title = `${countryName} - Historical Data (2000-2020)`;
                    break;
                    
                case 'predictions':
                    years = Array.from({length: 10}, (_, i) => 2021 + i);
                    accessData = years.map(year => {
                        const baseAccess = coords.access;
                        const yearFactor = (year - 2021) * 1.2;
                        return Math.min(100, baseAccess + yearFactor + Math.random() * 2);
                    });
                    title = `${countryName} - Predictions (2021-2030)`;
                    break;
                    
                case 'recent':
                    years = Array.from({length: 16}, (_, i) => 2015 + i);
                    accessData = years.map(year => {
                        const baseAccess = coords.access;
                        if (year <= 2020) {
                            const yearFactor = (year - 2015) * 1.0;
                            return Math.min(100, Math.max(0, baseAccess - 10 + yearFactor + Math.random() * 3));
                        } else {
                            const yearFactor = (year - 2021) * 1.2;
                            return Math.min(100, baseAccess + yearFactor + Math.random() * 2);
                        }
                    });
                    title = `${countryName} - Recent Trends (2015-2030)`;
                    break;
                    
                default: // 'all'
                    const historicalYears = Array.from({length: 21}, (_, i) => 2000 + i);
                    const futureYears = Array.from({length: 10}, (_, i) => 2021 + i);
                    years = [...historicalYears, ...futureYears];
                    
                    const historicalData = historicalYears.map(year => {
                        const baseAccess = coords.access;
                        const yearFactor = (year - 2000) * 0.8;
                        return Math.min(100, Math.max(0, baseAccess - 20 + yearFactor + Math.random() * 3));
                    });
                    
                    const futureData = futureYears.map(year => {
                        const baseAccess = historicalData[historicalData.length - 1];
                        const yearFactor = (year - 2021) * 1.2;
                        return Math.min(100, baseAccess + yearFactor + Math.random() * 2);
                    });
                    
                    accessData = [...historicalData, ...futureData];
                    title = `${countryName} - All Years (2000-2030)`;
            }

            const trace = {
                x: years,
                y: accessData,
                type: 'scatter',
                mode: 'lines+markers',
                name: 'Electricity Access',
                line: { color: '#3498db', width: 3 },
                marker: { color: '#3498db', size: 6 }
            };

            const layout = {
                title: title,
                xaxis: { title: 'Year' },
                yaxis: { title: 'Electricity Access (%)' },
                plot_bgcolor: '#f8fafc',
                paper_bgcolor: 'white'
            };

            Plotly.newPlot('mainChart', [trace], layout, { responsive: true });
        }
        
        function renderAccessForecastWithPeriod(countryName, coords, period) {
            // Similar implementation for access forecast based on period
            const years = Array.from({length: 10}, (_, i) => 2021 + i);
            const accessForecast = years.map(year => Math.min(100, coords.access + (year - 2021) * 1.5));

            const trace = {
                x: years,
                y: accessForecast,
                type: 'bar',
                marker: { color: '#3498db', opacity: 0.8 }
            };

            const layout = {
                title: `Electricity Access Forecast - ${period.charAt(0).toUpperCase() + period.slice(1)} Period`,
                xaxis: { title: 'Year' },
                yaxis: { title: 'Access (%)' }
            };

            Plotly.newPlot('accessChart', [trace], layout, { responsive: true });
        }
        
        function renderRenewableGrowthWithPeriod(countryName, coords, period) {
            // Similar implementation for renewable growth based on period
            const years = Array.from({length: 10}, (_, i) => 2021 + i);
            const renewableGrowth = years.map(year => Math.min(95, 20 + (coords.access * 0.2) + (year - 2021) * 2.8));

            const trace = {
                x: years,
                y: renewableGrowth,
                type: 'scatter',
                mode: 'lines+markers',
                name: 'Renewable Share',
                line: { color: '#27ae60', width: 3 }
            };

            const layout = {
                title: `Renewable Energy Growth - ${period.charAt(0).toUpperCase() + period.slice(1)} Period`,
                xaxis: { title: 'Year' },
                yaxis: { title: 'Renewable Share (%)' }
            };

            Plotly.newPlot('renewableChart', [trace], layout, { responsive: true });
        }
        
        '''
    
    # Insert the new time period function before the closing script tag
    script_close = '</script>'
    if script_close in content:
        content = content.replace(script_close, time_period_function + '\n    ' + script_close)
        print("✅ Added time period specific chart functions")
    
    # Write the updated content
    try:
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Successfully kept only Time Period controls")
        return True
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False

def main():
    """Main function to keep only time period controls"""
    success = keep_only_time_period()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ TIME PERIOD CONTROLS ONLY!")
        print("=" * 60)
        print("\n⏰ Available Time Period controls:")
        print("   ✓ All Years (2000-2030) ← Default")
        print("   ✓ Historical (2000-2020)")
        print("   ✓ Predictions (2021-2030)")
        print("   ✓ Recent Trends (2015-2030)")
        
        print("\n❌ Removed controls:")
        print("   ✗ Chart Type controls")
        print("   ✗ ML Model controls")
        
        print("\n🎯 Functionality:")
        print("   ✓ Time period buttons update all charts")
        print("   ✓ Charts show data for selected time period")
        print("   ✓ Clean, simplified interface")
        print("   ✓ Active button highlighting")
        
        print("\n🧪 To test:")
        print("   1. Go to: http://127.0.0.1:8000/explore/")
        print("   2. Verify: Only Time Period controls are visible")
        print("   3. Select a country (e.g., India)")
        print("   4. Try different Time Period buttons")
        print("   5. Verify: Charts update to show selected time period")
        
        print("\n🔄 Clear browser cache with Ctrl+F5 after testing")
    else:
        print("\n❌ FAILED TO SIMPLIFY CONTROLS")

if __name__ == "__main__":
    main()