#!/usr/bin/env python3
"""
Arrange Charts Vertical Stack
=============================

This script modifies the chart layout to arrange all charts vertically
one after another in a single column.
"""

import os

def arrange_charts_vertical_stack():
    """Arrange all charts vertically one after another"""
    
    html_file_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("📊 ARRANGING CHARTS: VERTICAL STACK (ONE AFTER ANOTHER)")
    print("=" * 60)
    print(f"📁 Updating file: {html_file_path}")
    
    # Read current file
    with open(html_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the current 2-per-row charts section and replace it
    old_charts_section = '''            <!-- Charts Layout: 2 Per Row -->
            
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
    
    # New vertical stack layout - all charts one after another
    new_charts_section = '''            <!-- Charts Vertical Stack: One After Another -->
            
            <!-- Chart 1: Energy Timeline -->
            <div class="chart-container-vertical">
                <h4>Energy Timeline (2000-2030)</h4>
                <div id="mainChart"></div>
            </div>
            
            <!-- Chart 2: Access Forecast -->
            <div class="chart-container-vertical">
                <h4>Access Forecast</h4>
                <div id="accessChart"></div>
            </div>
            
            <!-- Chart 3: Renewable Growth -->
            <div class="chart-container-vertical">
                <h4>Renewable Growth</h4>
                <div id="renewableChart"></div>
            </div>
            
            <!-- Chart 4: Energy Distribution -->
            <div class="chart-container-vertical">
                <h4>Energy Distribution</h4>
                <div id="pieChart"></div>
            </div>
            
            <!-- Chart 5: CO₂ Timeline -->
            <div class="chart-container-vertical">
                <h4>CO₂ Timeline</h4>
                <div id="co2Chart"></div>
            </div>
            
            <!-- Chart 6: CO₂ vs Access -->
            <div class="chart-container-vertical">
                <h4>CO₂ vs Access</h4>
                <div id="co2AccessChart"></div>
            </div>
            
            <!-- Chart 7: CO₂ Forecast -->
            <div class="chart-container-vertical">
                <h4>CO₂ Forecast</h4>
                <div id="co2ForecastChart"></div>
            </div>'''
    
    # Replace the charts section
    if old_charts_section in content:
        content = content.replace(old_charts_section, new_charts_section)
        print("✅ Replaced 2-per-row layout with vertical stack layout")
    else:
        print("⚠️ Could not find exact 2-per-row section, trying alternative approach")
        
        # Try to find any charts-row-2 and replace
        if 'charts-row-2' in content:
            # Replace all charts-row-2 sections with vertical stack
            import re
            # Remove all existing chart sections and replace with vertical stack
            pattern = r'<!-- Charts Layout: 2 Per Row -->.*?</div>\s*</div>'
            if re.search(pattern, content, re.DOTALL):
                content = re.sub(pattern, new_charts_section, content, flags=re.DOTALL)
                print("✅ Replaced charts using regex pattern")
    
    # Update CSS for vertical stack layout
    old_css = '''        /* Charts Layout: 2 Per Row */
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
    
    new_css = '''        /* Charts Vertical Stack: One After Another */
        .chart-container-vertical {
            width: 100%;
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            border: 1px solid #e5e7eb;
        }
        
        .chart-container-vertical h4 {
            font-size: 1.3rem;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 20px;
            text-align: center;
            border-bottom: 3px solid #3498db;
            padding-bottom: 12px;
        }
        
        .chart-container-vertical > div {
            height: 400px;
            margin: 0;
        }
        
        /* Responsive design for smaller screens */
        @media (max-width: 1200px) {
            .chart-container-vertical {
                padding: 20px;
                margin-bottom: 25px;
            }
            
            .chart-container-vertical h4 {
                font-size: 1.2rem;
            }
            
            .chart-container-vertical > div {
                height: 350px;
            }
        }
        
        @media (max-width: 768px) {
            .chart-container-vertical {
                padding: 15px;
                margin-bottom: 20px;
            }
            
            .chart-container-vertical h4 {
                font-size: 1.1rem;
                margin-bottom: 15px;
            }
            
            .chart-container-vertical > div {
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
        print("✅ Updated CSS for vertical stack layout")
    else:
        # Try to find and replace just the charts-row-2 CSS
        if '.charts-row-2' in content:
            # Insert new CSS before closing style tag
            style_close = '</style>'
            if style_close in content:
                content = content.replace(style_close, new_css + '\n    ' + style_close)
                print("✅ Added vertical stack CSS")
    
    # Write the updated content
    try:
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Successfully arranged charts in vertical stack")
        return True
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False

def main():
    """Main function to arrange charts in vertical stack"""
    success = arrange_charts_vertical_stack()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ CHARTS ARRANGED: VERTICAL STACK!")
        print("=" * 60)
        
        print("\n📊 Layout structure:")
        print("   Chart 1: Energy Timeline (2000-2030)")
        print("   Chart 2: Access Forecast")
        print("   Chart 3: Renewable Growth")
        print("   Chart 4: Energy Distribution")
        print("   Chart 5: CO₂ Timeline")
        print("   Chart 6: CO₂ vs Access")
        print("   Chart 7: CO₂ Forecast")
        
        print("\n🎨 Layout features:")
        print("   ✓ All charts in single column")
        print("   ✓ Charts arranged vertically one after another")
        print("   ✓ Full width charts for better visibility")
        print("   ✓ Larger chart height (400px) for detail")
        print("   ✓ Professional styling with shadows")
        print("   ✓ Blue accent borders on titles")
        print("   ✓ Responsive design for different screens")
        
        print("\n📱 Responsive behavior:")
        print("   ✓ Desktop: 400px height, full width")
        print("   ✓ Tablet: 350px height, optimized padding")
        print("   ✓ Mobile: 300px height, compact spacing")
        
        print("\n🎯 Features:")
        print("   ✓ Clear visual separation between charts")
        print("   ✓ Consistent full-width layout")
        print("   ✓ All charts update with time period controls")
        print("   ✓ Professional rounded corners and shadows")
        print("   ✓ Easy scrolling through all charts")
        
        print("\n🧪 To test:")
        print("   1. Go to: http://127.0.0.1:8000/explore/")
        print("   2. Select a country (e.g., India)")
        print("   3. Verify: All 7 charts appear one after another vertically")
        print("   4. Scroll: Down to see all charts in sequence")
        print("   5. Test: Time period controls update all charts")
        
        print("\n🔄 Clear browser cache with Ctrl+F5 after testing")
    else:
        print("\n❌ FAILED TO ARRANGE CHARTS IN VERTICAL STACK")

if __name__ == "__main__":
    main()