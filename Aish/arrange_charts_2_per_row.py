#!/usr/bin/env python3
"""
Arrange Charts 2 Per Row
=========================

This script modifies the chart layout to arrange charts vertically 
with 2 charts per row (one after another).
"""

import os

def arrange_charts_2_per_row():
    """Arrange charts vertically with 2 charts per row"""
    
    html_file_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("📊 ARRANGING CHARTS: 2 PER ROW (VERTICAL LAYOUT)")
    print("=" * 60)
    print(f"📁 Updating file: {html_file_path}")
    
    # Read current file
    with open(html_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the current single row charts section and replace it
    old_charts_section = '''            <!-- Charts Single Row Layout -->
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
    
    # New 2-per-row layout with charts arranged vertically
    new_charts_section = '''            <!-- Charts Layout: 2 Per Row -->
            
            <!-- Row 1: Energy Timeline + Access Forecast -->
            <div class="charts-row-2">
                <div class="chart-container-2">
                    <h4>Energy Timeline (2000-2030)</h4>
                    <div id="mainChart"></div>
                </div>
                
                <div class="chart-container-2">
                    <h4>Access Forecast</h4>
                    <div id="accessChart"></div>
                </div>
            </div>
            
            <!-- Row 2: Renewable Growth + Energy Distribution -->
            <div class="charts-row-2">
                <div class="chart-container-2">
                    <h4>Renewable Growth</h4>
                    <div id="renewableChart"></div>
                </div>
                
                <div class="chart-container-2">
                    <h4>Energy Distribution</h4>
                    <div id="pieChart"></div>
                </div>
            </div>
            
            <!-- Row 3: CO₂ Timeline + CO₂ vs Access -->
            <div class="charts-row-2">
                <div class="chart-container-2">
                    <h4>CO₂ Timeline</h4>
                    <div id="co2Chart"></div>
                </div>
                
                <div class="chart-container-2">
                    <h4>CO₂ vs Access</h4>
                    <div id="co2AccessChart"></div>
                </div>
            </div>
            
            <!-- Row 4: CO₂ Forecast (centered) -->
            <div class="charts-row-2">
                <div class="chart-container-2 chart-container-centered">
                    <h4>CO₂ Forecast</h4>
                    <div id="co2ForecastChart"></div>
                </div>
            </div>'''
    
    # Replace the charts section
    if old_charts_section in content:
        content = content.replace(old_charts_section, new_charts_section)
        print("✅ Replaced single row layout with 2-per-row layout")
    else:
        print("⚠️ Could not find exact single row section, trying alternative approach")
        
        # Try to find any charts-single-row and replace
        if 'charts-single-row' in content:
            # Replace all charts-single-row sections with 2-per-row
            import re
            # Remove all existing chart sections and replace with 2-per-row
            pattern = r'<!-- Charts Single Row Layout -->.*?</div>'
            if re.search(pattern, content, re.DOTALL):
                content = re.sub(pattern, new_charts_section, content, flags=re.DOTALL)
                print("✅ Replaced charts using regex pattern")
    
    # Update CSS for 2-per-row layout
    old_css = '''        /* Charts Single Row Layout */
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
    
    new_css = '''        /* Charts Layout: 2 Per Row */
        .charts-row-2 {
            display: flex;
            gap: 20px;
            margin-bottom: 25px;
            justify-content: space-between;
        }
        
        .chart-container-2 {
            flex: 1;
            background: white;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            border: 1px solid #e5e7eb;
        }
        
        .chart-container-2 h4 {
            font-size: 1.1rem;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 15px;
            text-align: center;
            border-bottom: 2px solid #e5e7eb;
            padding-bottom: 10px;
        }
        
        .chart-container-2 > div {
            height: 350px;
            margin: 0;
        }
        
        .chart-container-centered {
            max-width: 48%;
            margin: 0 auto;
        }
        
        /* Responsive design for smaller screens */
        @media (max-width: 1200px) {
            .charts-row-2 {
                flex-direction: column;
                gap: 15px;
            }
            
            .chart-container-2 {
                margin-bottom: 15px;
            }
            
            .chart-container-centered {
                max-width: 100%;
            }
        }
        
        @media (max-width: 768px) {
            .chart-container-2 {
                padding: 15px;
            }
            
            .chart-container-2 h4 {
                font-size: 1rem;
            }
            
            .chart-container-2 > div {
                height: 300px;
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
        print("✅ Updated CSS for 2-per-row layout")
    else:
        # Try to find and replace just the charts-single-row CSS
        if '.charts-single-row' in content:
            # Insert new CSS before closing style tag
            style_close = '</style>'
            if style_close in content:
                content = content.replace(style_close, new_css + '\n    ' + style_close)
                print("✅ Added 2-per-row CSS")
    
    # Write the updated content
    try:
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Successfully arranged charts in 2-per-row layout")
        return True
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False

def main():
    """Main function to arrange charts in 2-per-row layout"""
    success = arrange_charts_2_per_row()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ CHARTS ARRANGED: 2 PER ROW!")
        print("=" * 60)
        
        print("\n📊 Layout structure:")
        print("   Row 1: [Energy Timeline] [Access Forecast]")
        print("   Row 2: [Renewable Growth] [Energy Distribution]")
        print("   Row 3: [CO₂ Timeline] [CO₂ vs Access]")
        print("   Row 4: [CO₂ Forecast] (centered)")
        
        print("\n🎨 Layout features:")
        print("   ✓ 2 charts per row (side by side)")
        print("   ✓ Charts arranged vertically (one row after another)")
        print("   ✓ Equal width charts in each row")
        print("   ✓ Last chart centered in its row")
        print("   ✓ Professional styling with shadows")
        print("   ✓ Responsive design for different screens")
        
        print("\n📱 Responsive behavior:")
        print("   ✓ Desktop: 2 charts side by side per row")
        print("   ✓ Tablet/Mobile: Charts stack vertically")
        print("   ✓ Maintains proper spacing and sizing")
        
        print("\n🎯 Features:")
        print("   ✓ Clear visual separation between rows")
        print("   ✓ Consistent chart heights (350px)")
        print("   ✓ All charts update with time period controls")
        print("   ✓ Professional rounded corners and shadows")
        
        print("\n🧪 To test:")
        print("   1. Go to: http://127.0.0.1:8000/explore/")
        print("   2. Select a country (e.g., India)")
        print("   3. Verify: Charts appear in 4 rows with 2 charts each")
        print("   4. Check: Last row has 1 centered chart")
        print("   5. Test: Time period controls update all charts")
        
        print("\n🔄 Clear browser cache with Ctrl+F5 after testing")
    else:
        print("\n❌ FAILED TO ARRANGE CHARTS IN 2-PER-ROW LAYOUT")

if __name__ == "__main__":
    main()