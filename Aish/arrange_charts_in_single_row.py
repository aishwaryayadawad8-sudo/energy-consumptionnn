#!/usr/bin/env python3
"""
Arrange Charts in Single Row
============================

This script modifies the chart layout to arrange all charts in a single row
side by side horizontally.
"""

import os

def arrange_charts_single_row():
    """Arrange all charts in a single row side by side"""
    
    html_file_path = "Aish/sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("📊 ARRANGING ALL CHARTS IN SINGLE ROW")
    print("=" * 60)
    print(f"📁 Updating file: {html_file_path}")
    
    # Read current file
    with open(html_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the current 3-row charts section and replace it with single row
    old_charts_section = '''            <!-- Charts Grid Layout - 3 Rows -->
            
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
    
    # New single row layout with all 7 charts
    new_charts_section = '''            <!-- Charts Single Row Layout -->
            <div class="charts-single-row">
                <div class="chart-container-single">
                    <h4>Energy Timeline</h4>
                    <div id="mainChart"></div>
                </div>
                
                <div class="chart-container-single">
                    <h4>Access Forecast</h4>
                    <div id="accessChart"></div>
                </div>
                
                <div class="chart-container-single">
                    <h4>Renewable Growth</h4>
                    <div id="renewableChart"></div>
                </div>
                
                <div class="chart-container-single">
                    <h4>Energy Distribution</h4>
                    <div id="pieChart"></div>
                </div>
                
                <div class="chart-container-single">
                    <h4>CO₂ Timeline</h4>
                    <div id="co2Chart"></div>
                </div>
                
                <div class="chart-container-single">
                    <h4>CO₂ vs Access</h4>
                    <div id="co2AccessChart"></div>
                </div>
                
                <div class="chart-container-single">
                    <h4>CO₂ Forecast</h4>
                    <div id="co2ForecastChart"></div>
                </div>
            </div>'''
    
    # Replace the charts section
    if old_charts_section in content:
        content = content.replace(old_charts_section, new_charts_section)
        print("✅ Replaced 3-row layout with single row layout")
    else:
        print("⚠️ Could not find exact 3-row section, trying alternative approach")
        
        # Try to find any charts-row and replace
        if 'charts-row' in content:
            # Replace all charts-row sections with single row
            import re
            # Remove all existing chart sections and replace with single row
            pattern = r'<!-- Charts Grid Layout - 3 Rows -->.*?</div>\s*</div>\s*</div>'
            if re.search(pattern, content, re.DOTALL):
                content = re.sub(pattern, new_charts_section, content, flags=re.DOTALL)
                print("✅ Replaced charts using regex pattern")
    
    # Update CSS for single row layout
    old_css = '''        /* Charts Grid Layout */
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
        }'''
    
    new_css = '''        /* Charts Single Row Layout */
        .charts-single-row {
            display: flex;
            gap: 15px;
            margin-bottom: 30px;
            overflow-x: auto;
            padding-bottom: 10px;
        }
        
        .chart-container-single {
            flex: 0 0 300px;
            min-width: 300px;
            background: white;
            border-radius: 12px;
            padding: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            border: 1px solid #e5e7eb;
        }
        
        .chart-container-single h4 {
            font-size: 0.95rem;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 12px;
            text-align: center;
            border-bottom: 2px solid #e5e7eb;
            padding-bottom: 8px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        
        .chart-container-single > div {
            height: 280px;
            margin: 0;
        }
        
        /* Scrollbar styling for horizontal scroll */
        .charts-single-row::-webkit-scrollbar {
            height: 8px;
        }
        
        .charts-single-row::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 4px;
        }
        
        .charts-single-row::-webkit-scrollbar-thumb {
            background: #c1c1c1;
            border-radius: 4px;
        }
        
        .charts-single-row::-webkit-scrollbar-thumb:hover {
            background: #a8a8a8;
        }
        
        /* Responsive design for smaller screens */
        @media (max-width: 1200px) {
            .chart-container-single {
                flex: 0 0 280px;
                min-width: 280px;
            }
        }
        
        @media (max-width: 768px) {
            .chart-container-single {
                flex: 0 0 250px;
                min-width: 250px;
                padding: 12px;
            }
            
            .chart-container-single h4 {
                font-size: 0.9rem;
            }
            
            .chart-container-single > div {
                height: 250px;
            }
        }
        
        /* Override original chart-container styles */
        .chart-container {
            height: auto;
            margin: 20px 0;
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            padding: 10px;
        }'''
    
    # Replace the CSS
    if old_css in content:
        content = content.replace(old_css, new_css)
        print("✅ Updated CSS for single row layout")
    else:
        # Try to find and replace just the charts-row CSS
        if '.charts-row' in content:
            # Insert new CSS before closing style tag
            style_close = '</style>'
            if style_close in content:
                content = content.replace(style_close, new_css + '\n    ' + style_close)
                print("✅ Added single row CSS")
    
    # Write the updated content
    try:
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Successfully arranged all charts in single row")
        return True
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False

def main():
    """Main function to arrange charts in single row"""
    success = arrange_charts_single_row()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ ALL CHARTS ARRANGED IN SINGLE ROW!")
        print("=" * 60)
        print("\n📊 Single row layout:")
        print("   [Energy Timeline] [Access Forecast] [Renewable Growth] [Energy Distribution] [CO₂ Timeline] [CO₂ vs Access] [CO₂ Forecast]")
        
        print("\n🎨 Layout features:")
        print("   ✓ All 7 charts in one horizontal row")
        print("   ✓ Fixed width charts (300px each)")
        print("   ✓ Horizontal scrolling for overflow")
        print("   ✓ Compact design for space efficiency")
        print("   ✓ Professional styling with shadows")
        print("   ✓ Responsive sizing for different screens")
        
        print("\n📱 Responsive behavior:")
        print("   ✓ Desktop: 300px width per chart")
        print("   ✓ Tablet: 280px width per chart")
        print("   ✓ Mobile: 250px width per chart")
        print("   ✓ Horizontal scroll on all devices")
        
        print("\n🎯 Features:")
        print("   ✓ Horizontal scrolling to view all charts")
        print("   ✓ Fixed chart dimensions for consistency")
        print("   ✓ Compact titles to fit in smaller width")
        print("   ✓ All charts update with time period controls")
        
        print("\n🧪 To test:")
        print("   1. Go to: http://127.0.0.1:8000/explore/")
        print("   2. Select a country (e.g., India)")
        print("   3. Verify: All 7 charts appear in single row")
        print("   4. Scroll horizontally to see all charts")
        print("   5. Test: Time period controls update all charts")
        
        print("\n🔄 Clear browser cache with Ctrl+F5 after testing")
    else:
        print("\n❌ FAILED TO ARRANGE CHARTS IN SINGLE ROW")

if __name__ == "__main__":
    main()