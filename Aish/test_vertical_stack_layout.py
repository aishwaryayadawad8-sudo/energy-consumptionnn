#!/usr/bin/env python3
"""
Test Vertical Stack Layout
===========================

This script tests the vertical stack chart layout implementation.
"""

import requests
import time

def test_vertical_stack_layout():
    """Test the vertical stack layout functionality"""
    
    print("🧪 TESTING VERTICAL STACK LAYOUT")
    print("=" * 60)
    
    # Test server availability
    try:
        response = requests.get('http://127.0.0.1:8000/explore/', timeout=10)
        if response.status_code == 200:
            print("✅ Server is running and explore dashboard is accessible")
            
            # Check for vertical stack layout elements in HTML
            html_content = response.text
            
            # Check for vertical stack CSS class
            if 'chart-container-vertical' in html_content:
                print("✅ Vertical stack CSS class found in HTML")
            else:
                print("❌ Vertical stack CSS class NOT found")
                
            # Count the number of vertical chart containers
            container_count = html_content.count('chart-container-vertical')
            print(f"📊 Vertical chart containers found: {container_count}")
            
            # Check for all 7 chart containers in order
            chart_sequence = [
                ('Energy Timeline (2000-2030)', 'mainChart'),
                ('Access Forecast', 'accessChart'),
                ('Renewable Growth', 'renewableChart'),
                ('Energy Distribution', 'pieChart'),
                ('CO₂ Timeline', 'co2Chart'),
                ('CO₂ vs Access', 'co2AccessChart'),
                ('CO₂ Forecast', 'co2ForecastChart')
            ]
            
            found_charts = 0
            chart_positions = []
            
            for i, (title, chart_id) in enumerate(chart_sequence, 1):
                title_pos = html_content.find(title)
                id_pos = html_content.find(f'id="{chart_id}"')
                
                if title_pos != -1 and id_pos != -1:
                    found_charts += 1
                    chart_positions.append((i, title, title_pos))
                    print(f"✅ Chart {i}: {title} found at position {title_pos}")
                else:
                    print(f"❌ Chart {i}: {title} NOT found")
            
            print(f"\n📊 Charts found: {found_charts}/{len(chart_sequence)}")
            
            # Verify charts are in correct order (positions should be increasing)
            if len(chart_positions) >= 2:
                correct_order = all(chart_positions[i][2] < chart_positions[i+1][2] 
                                  for i in range(len(chart_positions)-1))
                if correct_order:
                    print("✅ Charts are in correct vertical order")
                else:
                    print("❌ Charts are NOT in correct vertical order")
            
            # Check for layout structure
            layout_checks = {
                "Single Column Layout": 'width: 100%' in html_content,
                "Full Width Charts": 'chart-container-vertical' in html_content,
                "Proper Spacing": 'margin-bottom: 30px' in html_content,
                "Professional Styling": 'box-shadow:' in html_content,
                "Blue Accent Borders": 'border-bottom: 3px solid #3498db' in html_content,
                "Responsive Design": '@media (max-width:' in html_content,
                "Large Chart Height": 'height: 400px' in html_content
            }
            
            passed_layout = 0
            for check_name, result in layout_checks.items():
                if result:
                    passed_layout += 1
                    print(f"✅ {check_name}: PASS")
                else:
                    print(f"❌ {check_name}: FAIL")
            
            print(f"\n🏗️ Layout checks passed: {passed_layout}/{len(layout_checks)}")
            
            # Check for time period controls
            time_controls = [
                'All Years (2000-2030)',
                'Historical (2000-2020)', 
                'Predictions (2021-2030)',
                'Recent Trends (2015-2030)'
            ]
            
            found_controls = 0
            for control in time_controls:
                if control in html_content:
                    found_controls += 1
                    print(f"✅ Time control found: {control}")
                else:
                    print(f"❌ Time control missing: {control}")
            
            print(f"\n⏰ Time controls found: {found_controls}/{len(time_controls)}")
            
            # Check that old layout classes are removed
            old_classes_removed = {
                "No Single Row": 'charts-single-row' not in html_content,
                "No 2-Per-Row": 'charts-row-2' not in html_content,
                "No Old Containers": 'chart-container-single' not in html_content and 'chart-container-2' not in html_content
            }
            
            removed_count = sum(old_classes_removed.values())
            print(f"\n🧹 Old layout classes removed: {removed_count}/{len(old_classes_removed)}")
            for check_name, result in old_classes_removed.items():
                status = "✅" if result else "❌"
                print(f"   {status} {check_name}")
            
            # Overall assessment
            total_checks = len(chart_sequence) + len(layout_checks) + len(time_controls) + len(old_classes_removed) + 2  # +2 for CSS class and order
            total_passed = found_charts + passed_layout + found_controls + removed_count + (2 if 'chart-container-vertical' in html_content and correct_order else 1 if 'chart-container-vertical' in html_content else 0)
            
            success_rate = (total_passed / total_checks) * 100
            
            print(f"\n📈 Overall Success Rate: {success_rate:.1f}% ({total_passed}/{total_checks})")
            
            if success_rate >= 90:
                print("🎉 VERTICAL STACK LAYOUT IMPLEMENTATION: EXCELLENT!")
            elif success_rate >= 75:
                print("✅ VERTICAL STACK LAYOUT IMPLEMENTATION: GOOD!")
            elif success_rate >= 50:
                print("⚠️ VERTICAL STACK LAYOUT IMPLEMENTATION: NEEDS IMPROVEMENT")
            else:
                print("❌ VERTICAL STACK LAYOUT IMPLEMENTATION: FAILED")
                
            return success_rate >= 75
            
        else:
            print(f"❌ Server returned status code: {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error connecting to server: {e}")
        return False

def main():
    """Main function to test vertical stack layout"""
    
    print("🚀 Starting Vertical Stack Layout Test...")
    print("🌐 Testing URL: http://127.0.0.1:8000/explore/")
    print()
    
    success = test_vertical_stack_layout()
    
    print("\n" + "=" * 60)
    if success:
        print("✅ VERTICAL STACK LAYOUT TEST PASSED!")
        print("=" * 60)
        
        print("\n🎯 What was tested:")
        print("   ✓ Server accessibility")
        print("   ✓ Vertical stack CSS implementation")
        print("   ✓ All 7 charts present in correct order")
        print("   ✓ Single column layout structure")
        print("   ✓ Full width chart containers")
        print("   ✓ Professional styling and spacing")
        print("   ✓ Time period controls")
        print("   ✓ Old layout classes removed")
        
        print("\n📊 Vertical Stack Layout Structure:")
        print("   Chart 1: Energy Timeline (2000-2030)")
        print("   Chart 2: Access Forecast")
        print("   Chart 3: Renewable Growth")
        print("   Chart 4: Energy Distribution")
        print("   Chart 5: CO₂ Timeline")
        print("   Chart 6: CO₂ vs Access")
        print("   Chart 7: CO₂ Forecast")
        
        print("\n🎨 Layout Features:")
        print("   ✓ All charts in single column")
        print("   ✓ Charts arranged vertically one after another")
        print("   ✓ Full width charts for better visibility")
        print("   ✓ Larger chart height (400px) for detail")
        print("   ✓ Professional styling with shadows")
        print("   ✓ Blue accent borders on titles")
        print("   ✓ Responsive design for mobile/tablet")
        
        print("\n🧪 Manual Testing Steps:")
        print("   1. Go to: http://127.0.0.1:8000/explore/")
        print("   2. Select a country (e.g., India)")
        print("   3. Verify: All 7 charts appear vertically one after another")
        print("   4. Scroll: Down to see all charts in sequence")
        print("   5. Test: Time period controls update all charts")
        print("   6. Test: Responsive behavior on different screen sizes")
        
        print("\n💡 Tips:")
        print("   • Use Ctrl+F5 to clear browser cache")
        print("   • Scroll down to see all charts")
        print("   • Charts are now full width for better visibility")
        print("   • All charts update with time controls")
        
    else:
        print("❌ VERTICAL STACK LAYOUT TEST FAILED!")
        print("=" * 60)
        print("\n🔧 Troubleshooting:")
        print("   • Check if Django server is running")
        print("   • Verify HTML template has been updated")
        print("   • Clear browser cache with Ctrl+F5")
        print("   • Check browser console for JavaScript errors")

if __name__ == "__main__":
    main()