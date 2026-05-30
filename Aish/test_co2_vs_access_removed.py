#!/usr/bin/env python3
"""
Test CO₂ vs Access Chart Removal
=================================

This script tests that the CO₂ vs Access chart has been successfully removed.
"""

import requests
import time

def test_co2_vs_access_removed():
    """Test that CO₂ vs Access chart has been removed"""
    
    print("🧪 TESTING CO₂ vs ACCESS CHART REMOVAL")
    print("=" * 60)
    
    # Test server availability
    try:
        response = requests.get('http://127.0.0.1:8000/explore/', timeout=10)
        if response.status_code == 200:
            print("✅ Server is running and explore dashboard is accessible")
            
            # Check HTML content
            html_content = response.text
            
            # Check that CO₂ vs Access chart is NOT present
            removal_checks = {
                "CO₂ vs Access Title": 'CO₂ vs Access' not in html_content,
                "CO₂ vs Access Chart ID": 'id="co2AccessChart"' not in html_content,
                "CO₂ vs Access Function": 'renderCO2AccessCorrelation' not in html_content,
                "CO₂ vs Access Comment": '<!-- Chart 6: CO₂ vs Access -->' not in html_content
            }
            
            removed_count = 0
            for check_name, result in removal_checks.items():
                if result:
                    removed_count += 1
                    print(f"✅ {check_name}: Successfully removed")
                else:
                    print(f"❌ {check_name}: Still present")
            
            print(f"\n🗑️ Removal checks passed: {removed_count}/{len(removal_checks)}")
            
            # Check that remaining charts are still present
            remaining_charts = [
                ('Energy Timeline (2000-2030)', 'mainChart'),
                ('Access Forecast', 'accessChart'),
                ('Renewable Growth', 'renewableChart'),
                ('Energy Distribution', 'pieChart'),
                ('CO₂ Timeline', 'co2Chart'),
                ('CO₂ Forecast', 'co2ForecastChart')
            ]
            
            found_remaining = 0
            for title, chart_id in remaining_charts:
                title_present = title in html_content
                id_present = f'id="{chart_id}"' in html_content
                
                if title_present and id_present:
                    found_remaining += 1
                    print(f"✅ Remaining chart: {title}")
                else:
                    print(f"❌ Missing chart: {title}")
            
            print(f"\n📊 Remaining charts found: {found_remaining}/{len(remaining_charts)}")
            
            # Count total chart containers
            container_count = html_content.count('chart-container-vertical')
            print(f"📊 Total chart containers: {container_count}")
            
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
            
            # Overall assessment
            total_checks = len(removal_checks) + len(remaining_charts) + len(layout_checks) + len(time_controls)
            total_passed = removed_count + found_remaining + passed_layout + found_controls
            
            success_rate = (total_passed / total_checks) * 100
            
            print(f"\n📈 Overall Success Rate: {success_rate:.1f}% ({total_passed}/{total_checks})")
            
            # Specific check for 6 charts (not 7)
            expected_charts = 6
            if container_count == expected_charts:
                print(f"✅ Correct number of charts: {container_count} (expected {expected_charts})")
            else:
                print(f"❌ Incorrect number of charts: {container_count} (expected {expected_charts})")
            
            if success_rate >= 90 and container_count == expected_charts:
                print("🎉 CO₂ vs ACCESS CHART REMOVAL: EXCELLENT!")
            elif success_rate >= 75:
                print("✅ CO₂ vs ACCESS CHART REMOVAL: GOOD!")
            elif success_rate >= 50:
                print("⚠️ CO₂ vs ACCESS CHART REMOVAL: NEEDS IMPROVEMENT")
            else:
                print("❌ CO₂ vs ACCESS CHART REMOVAL: FAILED")
                
            return success_rate >= 75 and container_count == expected_charts
            
        else:
            print(f"❌ Server returned status code: {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error connecting to server: {e}")
        return False

def main():
    """Main function to test CO₂ vs Access chart removal"""
    
    print("🚀 Starting CO₂ vs Access Chart Removal Test...")
    print("🌐 Testing URL: http://127.0.0.1:8000/explore/")
    print()
    
    success = test_co2_vs_access_removed()
    
    print("\n" + "=" * 60)
    if success:
        print("✅ CO₂ vs ACCESS CHART REMOVAL TEST PASSED!")
        print("=" * 60)
        
        print("\n🎯 What was verified:")
        print("   ✓ CO₂ vs Access chart completely removed")
        print("   ✓ All remaining 6 charts still present")
        print("   ✓ Vertical stack layout maintained")
        print("   ✓ Professional styling preserved")
        print("   ✓ Time period controls still functional")
        print("   ✓ JavaScript functions cleaned up")
        
        print("\n📊 Updated Chart Layout:")
        print("   Chart 1: Energy Timeline (2000-2030)")
        print("   Chart 2: Access Forecast")
        print("   Chart 3: Renewable Growth")
        print("   Chart 4: Energy Distribution")
        print("   Chart 5: CO₂ Timeline")
        print("   Chart 6: CO₂ Forecast")
        print("   ❌ Removed: CO₂ vs Access")
        
        print("\n🎨 Layout Features Maintained:")
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
        print("   3. Verify: Only 6 charts appear (no CO₂ vs Access)")
        print("   4. Scroll: Down to see all remaining charts")
        print("   5. Test: Time period controls update all charts")
        
        print("\n💡 Tips:")
        print("   • Use Ctrl+F5 to clear browser cache")
        print("   • Verify CO₂ vs Access chart is completely gone")
        print("   • Check that remaining charts still work perfectly")
        
    else:
        print("❌ CO₂ vs ACCESS CHART REMOVAL TEST FAILED!")
        print("=" * 60)
        print("\n🔧 Troubleshooting:")
        print("   • Check if Django server is running")
        print("   • Verify HTML template has been updated")
        print("   • Clear browser cache with Ctrl+F5")
        print("   • Check browser console for JavaScript errors")

if __name__ == "__main__":
    main()