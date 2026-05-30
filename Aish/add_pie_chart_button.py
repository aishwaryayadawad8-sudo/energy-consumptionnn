#!/usr/bin/env python3
"""
Add Pie Chart Button to Chart Type Controls
"""

import os

def add_pie_chart_button():
    """Add pie chart button to the chart type controls"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if pie chart button already exists
        if "onclick=\"setChartType('pie')\"" in content:
            print("✅ Pie chart button already exists")
            return True
        
        # Add pie chart button to chart type controls
        old_buttons = '''                    <button class="control-btn" onclick="setChartType('access')">Access Trends</button>
                </div>'''
        
        new_buttons = '''                    <button class="control-btn" onclick="setChartType('access')">Access Trends</button>
                    <button class="control-btn" onclick="setChartType('pie')">Pie Chart</button>
                </div>'''
        
        if old_buttons in content:
            content = content.replace(old_buttons, new_buttons)
            print("✅ Added pie chart button to controls")
        else:
            print("⚠️ Could not find chart type controls to update")
        
        # Update the chart type handling in JavaScript
        # Find the updateCharts function and add pie chart case
        update_charts_pattern = '''                case 'access':
                    renderAccessChart(countryData, predictions);
                    break;
            }'''
        
        new_update_charts = '''                case 'access':
                    renderAccessChart(countryData, predictions);
                    break;
                case 'pie':
                    renderEnergySourcePieChart(countryData, predictions);
                    break;
            }'''
        
        if update_charts_pattern in content:
            content = content.replace(update_charts_pattern, new_update_charts)
            print("✅ Added pie chart case to updateCharts function")
        
        # Update the getChartTitle function
        chart_titles = '''            const titles = {
                'timeline': 'Energy Timeline (2000-2030)',
                'comparison': 'Historical vs Predicted Comparison',
                'breakdown': 'Energy Mix Breakdown',
                'access': 'Access Trends Analysis'
            };'''
        
        new_chart_titles = '''            const titles = {
                'timeline': 'Energy Timeline (2000-2030)',
                'comparison': 'Historical vs Predicted Comparison',
                'breakdown': 'Energy Mix Breakdown',
                'access': 'Access Trends Analysis',
                'pie': 'Energy Source Distribution'
            };'''
        
        if chart_titles in content:
            content = content.replace(chart_titles, new_chart_titles)
            print("✅ Added pie chart title to getChartTitle function")
        
        # Write the updated content back to the file
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully added pie chart button and functionality!")
        return True
        
    except Exception as e:
        print(f"❌ Error adding pie chart button: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Adding Pie Chart Button to Controls...")
    success = add_pie_chart_button()
    
    if success:
        print("\n✅ PIE CHART BUTTON ADDED SUCCESSFULLY!")
        print("\n📋 Now users can:")
        print("1. Click the 'Pie Chart' button in Chart Type controls")
        print("2. View the energy source distribution as a pie chart")
        print("3. See interactive hover details")
        print("4. Switch between different chart types easily")
    else:
        print("\n❌ Failed to add pie chart button.")