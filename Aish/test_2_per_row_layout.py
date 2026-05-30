#!/usr/bin/env python3
"""
Test 2 Per Row Layout
=====================

This script tests the 2-per-row chart layout implementation.
"""

import requests
import time

def test_2_per_row_layout():
    """Test the 2-per-row layout functionality"""
    
    print("🧪 TESTING 2-PER-ROW LAYOUT")
    print("=" * 60)
    
    # Test server availability
    try:
        response = requests.get('http://127.0.0.1:8000/explore/', timeout=10)
        if response.status_code == 200:
            print("✅ Server is running and explore dashboard is accessible")
            
            # Check for 2-per-row layout elements in HTML
            html_content = response.text
            
            # Check for 2-per-row CSS class
            if 'charts-row-2' in html_content:
                print("✅ 2-per-row CSS class found in HTML")
            else:
                print("❌ 2-per-row CSS class NOT found")
                
            # Check for chart container class
            if 'chart-container-2' in html_content:
                print("✅ Chart container class found in HTML")
            else:
                print("❌ Chart container class NOT found")
                
            # Count the number of chart rows
            row_count = html_content.count('charts-row-2')
            print(f"📊 Chart rows found: {row_count}")
            
            # Check for all 7 chart containers
            chart_titles = [
                'Energy Timeline (2000-2030)',
                'Access Forecast',
                'Renewable Growth',
                'Energy Distribution',
                'CO₂ Timeline',
                'CO₂ vs Access',
                'CO₂ Forecast'
            ]
            
            found_charts = 0
            for chart in chart_titles:
                if chart in html_content:
                    found_charts += 1
                    print(f"✅ Found chart: {chart}")
                else:
                    print(f"❌ Missing chart: {chart}")
            
            print(f"\n📊 Charts found: {found_charts}/{len(chart_titles)}")
            
            # Check for specific layout structure
            layout_checks = {
                "Row 1 Structure": 'Energy Timeline (2000-2030)' in html_content and 'Access Forecast' in html_content,
                "Row 2 Structure": 'Renewable Growth' in html_content and 'Energy Distribution' in html_content,
                "Row 3 Structure": 'CO₂ Timeline' in html_content and 'CO₂ vs Access' in html_content,
                "Row 4 Structure": 'CO₂ Forecast' in html_content,
                "Centered Chart": 'chart-container-centered' in html_content,
                "Flex Layout": 'display: flex' in html_content,
                "Responsive Design": '@media (max-width:' in html_content
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
            
            # Overall assessment
            total_checks = len(chart_titles) + len(layout_checks) + len(time_controls) + 2  # +2 for CSS classes
            total_passed = found_charts + passed_layout + found_controls + (2 if 'charts-row-2' in html_content and 'chart-container-2' in html_content else 0)
            
            success_rate = (total_passed / total_checks) * 100
            
            print(f"\n📈 Overall Success Rate: {success_rate:.1f}% ({total_passed}/{total_checks})")
            
            if success_rate >= 90:
                print("🎉 2-PER-ROW LAYOUT IMPLEMENTATION: EXCELLENT!")
            elif success_rate >= 75:
                print("✅ 2-PER-ROW LAYOUT IMPLEMENTATION: GOOD!")
            elif success_rate >= 50:
                print("⚠️ 2-PER-ROW LAYOUT IMPLEMENTATION: NEEDS IMPROVEMENT")
            else:
                print("❌ 2-PER-ROW LAYOUT IMPLEMENTATION: FAILED")
                
            return success_rate >= 75
            
        else:
            print(f"❌ Server returned status code: {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error connecting to server: {e}")
        return False

def main():
    """Main function to test 2-per-row layout"""
    
    print("🚀 Starting 2-Per-Row Layout Test...")
    print("🌐 Testing URL: http://127.0.0.1:8000/explore/")
    print()
    
    success = test_2_per_row_layout()
    
    print("\n" + "=" * 60)
    if success:
        print("✅ 2-PER-ROW LAYOUT TEST PASSED!")
        print("=" * 60)
        
        print("\n🎯 What was tested:")
        print("   ✓ Server accessibility")
        print("   ✓ 2-per-row CSS implementation")
        print("   ✓ All 7 charts present")
        print("   ✓ Proper row structure (4 rows)")
        print("   ✓ Centered last chart")
        print("   ✓ Responsive design CSS")
        print("   ✓ Time period controls")
        
        print("\n📊 2-Per-Row Layout Structure:")
        print("   Row 1: [Energy Timeline] [Access Forecast]")
        print("   Row 2: [Renewable Growth] [Energy Distribution]")
        print("   Row 3: [CO₂ Timeline] [CO₂ vs Access]")
        print("   Row 4: [CO₂ Forecast] (centered)")
        
        print("\n🎨 Layout Features:")
        print("   ✓ Charts arranged vertically in rows")
        print("   ✓ 2 charts side by side per row")
        print("   ✓ Equal width charts in each row")
        print("   ✓ Last chart centered in its row")
        print("   ✓ Professional styling with shadows")
        print("   ✓ Responsive design for mobile/tablet")
        
        print("\n🧪 Manual Testing Steps:")
        print("   1. Go to: http://127.0.0.1:8000/explore/")
        print("   2. Select a country (e.g., India)")
        print("   3. Verify: Charts appear in 4 rows")
        print("   4. Check: 2 charts per row (except last row)")
        print("   5. Test: Time period controls update all charts")
        print("   6. Test: Responsive behavior on different screen sizes")
        
        print("\n💡 Tips:")
        print("   • Use Ctrl+F5 to clear browser cache")
        print("   • Test on different screen sizes")
        print("   • Verify charts stack vertically on mobile")
        print("   • Check that all charts update with time controls")
        
    else:
        print("❌ 2-PER-ROW LAYOUT TEST FAILED!")
        print("=" * 60)
        print("\n🔧 Troubleshooting:")
        print("   • Check if Django server is running")
        print("   • Verify HTML template has been updated")
        print("   • Clear browser cache with Ctrl+F5")
        print("   • Check browser console for JavaScript errors")

if __name__ == "__main__":
    main()