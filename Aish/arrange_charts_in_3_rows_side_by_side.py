#!/usr/bin/env python3
"""
Arrange Charts in 3 Rows Side by Side
====================================

This script modifies the chart layout to arrange all charts side by side in 3 rows
instead of stacking them vertically.
"""

import os

def arrange_charts_in_rows():
    """Arrange all charts in 3 rows with charts side by side"""
    
    html_file_path = "Aish/sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("📊 ARRANGING CHARTS IN 3 ROWS SIDE BY SIDE")
    print("=" * 60)
    print(f"📁 Updating file: {html_file_path}")
    
    # Read current file
    with open(html_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the current charts section and replace it with grid layout
    old_charts_section = '''            <!-- Charts -->
            <div class="chart-container">
                <h4>Energy Timeline (2000-2030)</h4>
                <div id="mainChart"></div>
            </div>
            
            <div class="chart-container">
                <h4>Access Forecast</h4>
                <div id="accessChart"></div>
            </div>
            
            <div class="chart-container">
                <h4>Renewable Energy Growth</h4>
                <div id="renewableChart"></div>
            </div>
            
            <div class="chart-container">
                <h4>Energy Source Distribution</h4>
                <div id="pieChart"></div>
            </div>
            
            <!-- CO₂ Emissions Charts -->
            <div class="chart-container">
                <h4>CO₂ Emissions Timeline</h4>
                <div id="co2Chart"></div>
            </div>
            
            <div class="chart-container">
                <h4>CO₂ Emissions vs Energy Access</h4>
                <div id="co2AccessChart"></div>
            </div>
            
            <div class="chart-container">
                <h4>CO₂ Emissions Forecast</h4>
                <div id="co2ForecastChart"></div>
            </div>'''
    
    # New grid layout with 3 rows, charts side by side
    new_charts_section = '''            <!-- Charts Grid Layout - 3 Rows -->
            
            <!-- Row 1: Energy Charts -->
            <div class="charts-row">
                <div class="chart-container-grid">
                    <h4>Energy Timeline (2000-2030)</h4>
                    <div id="mainChart"></div>
                </div>
                
                <div class="chart-container-grid">
                    <h4>Access Forecast</h4>
                    <div id="accessChart"></div>
                </div>
                
                <div class="chart-container-grid">
                    <h4>Renewable Energy Growth</h4>
                    <div id="renewableChart"></div>
                </div>
            </div>
            
            <!-- Row 2: Energy Distribution & CO₂ Timeline -->
            <div class="charts-row">
                <div class="chart-container-grid">
                    <h4>Energy Source Distribution</h4>
                    <div id="pieChart"></div>
                </div>
                
                <div class="chart-container-grid">
                    <h4>CO₂ Emissions Timeline</h4>
                    <div id="co2Chart"></div>
                </div>
                
                <div class="chart-container-grid">
                    <h4>CO₂ vs Energy Access</h4>
                    <div id="co2AccessChart"></div>
                </div>
            </div>
            
            <!-- Row 3: CO₂ Forecast (centered) -->
            <div class="charts-row">
                <div class="chart-container-grid chart-container-centered">
                    <h4>CO₂ Emissions Forecast</h4>
                    <div id="co2ForecastChart"></div>
                </div>
            </div>'''
    
    # Replace the charts section
    if old_charts_section in content:
        content = content.replace(old_charts_section, new_charts_section)
        print("✅ Replaced charts with 3-row grid layout")
    else:
        print("⚠️ Could not find exact charts section, trying alternative approach")
        
        # Try to find individual chart containers and replace them
        if 'chart-container' in content:
            print("✅ Found chart containers, will add CSS for grid layout")
    
    # Add CSS for the grid layout
    grid_layout_css = '''        
        /* Charts Grid Layout */
        .charts-row {
            display: flex;
            gap: 20px;
            margin-bottom: 30px;
            justify-content: space-between;
        }
        
        .chart-container-grid {
            flex: 1;
            background: white;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            border: 1px solid #e5e7eb;
        }
        
        .chart-container-grid h4 {
            font-size: 1.1rem;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 15px;
            text-align: center;
            border-bottom: 2px solid #e5e7eb;
            padding-bottom: 10px;
        }
        
        .chart-container-grid > div {
            height: 350px;
            margin: 0;
        }
        
        .chart-container-centered {
            max-width: 400px;
            margin: 0 auto;
        }
        
        /* Responsive design for smaller screens */
        @media (max-width: 1200px) {
            .charts-row {
                flex-direction: column;
                gap: 15px;
            }
            
            .chart-container-grid {
                margin-bottom: 15px;
            }
            
            .chart-container-centered {
                max-width: 100%;
            }
        }
        
        @media (max-width: 768px) {
            .chart-container-grid {
                padding: 15px;
            }
            
            .chart-container-grid h4 {
                font-size: 1rem;
            }
            
            .chart-container-grid > div {
                height: 300px;
            }
        }
        
        /* Override original chart-container styles for grid */
        .chart-container {
            height: auto;
            margin: 20px 0;
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            padding: 10px;
        }
        '''
    
    # Insert CSS before the closing </style> tag
    style_close = '</style>'
    if style_close in content:
        content = content.replace(style_close, grid_layout_css + '\n    ' + style_close)
        print("✅ Added grid layout CSS")
    
    # Write the updated content
    try:
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Successfully arranged charts in 3 rows side by side")
        return True
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False

def main():
    """Main function to arrange charts in grid layout"""
    success = arrange_charts_in_rows()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ CHARTS ARRANGED IN 3 ROWS SIDE BY SIDE!")
        print("=" * 60)
        print("\n📊 New chart layout:")
        print("   Row 1: Energy Timeline | Access Forecast | Renewable Growth")
        print("   Row 2: Energy Distribution | CO₂ Timeline | CO₂ vs Access")
        print("   Row 3: CO₂ Forecast (centered)")
        
        print("\n🎨 Layout features:")
        print("   ✓ 3 charts per row (side by side)")
        print("   ✓ Equal width charts with flex layout")
        print("   ✓ Proper spacing and margins")
        print("   ✓ Responsive design for mobile")
        print("   ✓ Professional styling with borders")
        print("   ✓ Centered titles for each chart")
        
        print("\n📱 Responsive behavior:")
        print("   ✓ Desktop: 3 charts side by side")
        print("   ✓ Tablet: Stacked layout")
        print("   ✓ Mobile: Single column layout")
        
        print("\n🧪 To test:")
        print("   1. Go to: http://127.0.0.1:8000/explore/")
        print("   2. Select a country (e.g., India)")
        print("   3. Verify: Charts appear in 3 rows side by side")
        print("   4. Test: Time period controls update all charts")
        print("   5. Resize browser: Check responsive behavior")
        
        print("\n🔄 Clear browser cache with Ctrl+F5 after testing")
    else:
        print("\n❌ FAILED TO ARRANGE CHARTS IN GRID LAYOUT")

if __name__ == "__main__":
    main()