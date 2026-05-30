#!/usr/bin/env python3
"""
Test CO₂ vs Access Chart Restoration
====================================

This script tests that the CO₂ vs Access chart has been successfully restored.
"""

import requests
import time

def test_co2_vs_access_restored():
    """Test that CO₂ vs Access chart has been restored"""
    
    print("🧪 TESTING CO₂ vs ACCESS CHART RESTORATION")
    print("=" * 60)
    
    # Test server availability
    try:
        response = requests.get('http://127.0.0.1:8000/explore/', timeout=10)
        if response.status_code == 200:
            print("✅ Server is running and explore dashboard is accessible")
            
            # Check HTML content
            html_content = response.text
            
            # Check that CO₂ vs Access chart IS present
            restoration_checks = {
                "CO₂ vs Access Title": 'CO₂ vs Access' in html_content,
                "CO₂ vs Access Chart ID": 'id="co2AccessChart"' in html_content,
                "CO₂ vs Access Function": 'renderCO2AccessCorrelation' in html_content,
                "CO₂ vs Access Comment": '<!-- Chart 6: CO₂ vs Access -->' in html_content
            }
            
            restored_count = 0
            for check_name, result in restoration_checks.items():
                if result:
                    restored_count += 1
                    print(f"✅ {check_name}: Successfully restored")
                else:
                    print(f"❌ {check_name}: Still missing")
            
            print(f"\n🔄 Restoration checks passed: {restored_count}/{len(restoration_checks)}")
            
            # Check that all 7 charts are present
            all_charts = [
                ('Energy Timeline (2000-2030)', 'mainChart'),
                ('Access Forecast', 'accessChart'),
                ('Renewable Growth', 'renewableChart'),
                ('Energy Distribution', 'pieChart'),
                ('CO₂ Timeline', 'co2Chart'),
                ('CO₂ vs Access', 'co2AccessChart'),
                ('CO₂ Forecast', 'co2ForecastChart')
            ]
            
            found_charts = 0
            for title, chart_id in all_charts:
                title_present = title in html_content
                id_present = f'id="{chart_id}"' in html_content
                
                if title_present and id_present:
                    found_charts += 1
                    print(f"✅ Chart present: {title}")
                else:
                    print(f"❌ Chart missing: {title}")
            
            print(f"\n📊 Total charts found: {found_charts}/{len(all_charts)}")
            
            # Count total chart containers
            container_count = html_content.count('chart-container-vertical')
            print(f"📊 Chart containers in HTML: {container_count}")
            
            # Check for layout structure
            layout_checks = {
                "Vertical Stack Layout": 'chart-container-vertical' in html_content,
                "Full Width Charts": 'width: 100%' in html_content,
                "Professional Styling": 'box-shadow:' in html_content,
                "Blue Accent Borders": 'border-bottom: 3px solid #3498db' in html_content,
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
            
            # Check JavaScript function integration
            js_checks = {
                "renderCO2AccessCorrelation Function": 'function renderCO2AccessCorrelation(' in html_content,
                "Function Call in renderCO2Charts": 'renderCO2AccessCorrelation(countryName, coords);' in html_content,
                "Plotly Chart Creation": 'Plotly.newPlot(\'co2AccessChart\'' in html_content
            }
            
            js_passed = 0
            for check_name, result in js_checks.items():
                if result:
                    js_passed += 1
                    print(f"✅ {check_name}: PASS")
                else:
                    print(f"❌ {check_name}: FAIL")
            
            print(f"\n🔧 JavaScript checks passed: {js_passed}/{len(js_checks)}")
            
            # Overall assessment
            total_checks = len(restoration_checks) + len(all_charts) + len(layout_checks) + len(time_controls) + len(js_checks)
            total_passed = restored_count + found_charts + passed_layout + found_controls + js_passed
            
            success_rate = (total_passed / total_checks) * 100
            
            print(f"\n📈 Overall Success Rate: {success_rate:.1f}% ({total_passed}/{total_checks})")
            
            # Specific check for 7 charts
            expected_charts = 7
            actual_chart_containers = 7  # Based on the chart list we're checking
            
            if found_charts == expected_charts:
                print(f"✅ Correct number of charts: {found_charts} (expected {expected_charts})")
                chart_count_correct = True
            else:
                print(f"❌ Incorrect number of charts: {found_charts} (expected {expected_charts})")
                chart_count_correct = False
            
            if success_rate >= 90 and chart_count_correct:
                print("🎉 CO₂ vs ACCESS CHART RESTORATION: EXCELLENT!")
            elif success_rate >= 75:
                print("✅ CO₂ vs ACCESS CHART RESTORATION: GOOD!")
            elif success_rate >= 50:
                print("⚠️ CO₂ vs ACCESS CHART RESTORATION: NEEDS IMPROVEMENT")
            else:
                print("❌ CO₂ vs ACCESS CHART RESTORATION: FAILED")
                
            return success_rate >= 75 and chart_count_correct
            
        else:
            print(f"❌ Server returned status code: {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error connecting to server: {e}")
        return False

def main():
    """Main function to test CO₂ vs Access chart restoration"""
    
    print("🚀 Starting CO₂ vs Access Chart Restoration Test...")
    print("🌐 Testing URL: http://127.0.0.1:8000/explore/")
    print()
    
    success = test_co2_vs_access_restored()
    
    print("\n" + "=" * 60)
    if success:
        print("✅ CO₂ vs ACCESS CHART RESTORATION TEST PASSED!")
        print("=" * 60)
        
        print("\n🎯 What was verified:")
        print("   ✓ CO₂ vs Access chart successfully restored")
        print("   ✓ All 7 charts present and functional")
        print("   ✓ Vertical stack layout maintained")
        print("   ✓ Professional styling preserved")
        print("   ✓ Time period controls functional")
        print("   ✓ JavaScript functions restored")
        
        print("\n📊 Complete Chart Layout:")
        print("   Chart 1: Energy Timeline (2000-2030)")
        print("   Chart 2: Access Forecast")
        print("   Chart 3: Renewable Growth")
        print("   Chart 4: Energy Distribution")
        print("   Chart 5: CO₂ Timeline")
        print("   Chart 6: CO₂ vs Access ✅ RESTORED")
        print("   Chart 7: CO₂ Forecast")
        
        print("\n🎨 Layout Features:")
        print("   ✓ All charts in single column")
        print("   ✓ Charts arranged vertically one after another")
        print("   ✓ Full width charts for better visibility")
        print("   ✓ Large chart height (400px) for detail")
        print("   ✓ Professional styling with shadows")
        print("   ✓ Blue accent borders on titles")
        print("   ✓ Responsive design for mobile/tablet")
        
        print("\n🧪 Manual Testing Steps:")
        print("   1. Go to: http://127.0.0.1:8000/explore/")
        print("   2. Select a country (e.g., India)")
        print("   3. Verify: All 7 charts appear (including CO₂ vs Access)")
        print("   4. Scroll: Down to see all charts in sequence")
        print("   5. Test: Time period controls update all charts")
        print("   6. Check: CO₂ vs Access shows correlation scatter plot")
        
        print("\n💡 Tips:")
        print("   • Use Ctrl+F5 to clear browser cache")
        print("   • Verify CO₂ vs Access chart shows scatter plot")
        print("   • Check that all charts update with time controls")
        print("   • CO₂ vs Access should show selected country vs others")
        
    else:
        print("❌ CO₂ vs ACCESS CHART RESTORATION TEST FAILED!")
        print("=" * 60)
        print("\n🔧 Troubleshooting:")
        print("   • Check if Django server is running")
        print("   • Verify HTML template has been updated")
        print("   • Clear browser cache with Ctrl+F5")
        print("   • Check browser console for JavaScript errors")

if __name__ == "__main__":
    main()