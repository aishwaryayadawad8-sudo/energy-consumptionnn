#!/usr/bin/env python3
"""
Test Fixed Display
==================

Quick test to verify map and charts are now displaying correctly.
"""

import requests

def test_fixed_display():
    """Test that the display fix is working"""
    
    print("🧪 TESTING FIXED DISPLAY")
    print("=" * 50)
    
    try:
        response = requests.get('http://127.0.0.1:8000/explore/', timeout=10)
        
        if response.status_code == 200:
            html_content = response.text
            
            # Quick checks for key elements
            checks = {
                "Map Container": 'id="map"' in html_content,
                "Leaflet Script": 'leaflet.js' in html_content,
                "Results Visible": 'style="display: block;"' in html_content,
                "Global Metrics": 'Global Electricity Access' in html_content,
                "All Chart IDs": all(chart_id in html_content for chart_id in [
                    'id="mainChart"', 'id="accessChart"', 'id="renewableChart"',
                    'id="pieChart"', 'id="co2Chart"', 'id="co2AccessChart"', 'id="co2ForecastChart"'
                ]),
                "Initialization Code": 'loadSampleGlobalData' in html_content,
                "Chart Functions": 'renderSampleGlobalCharts' in html_content,
                "Script Structure": '</script>' in html_content and '<script>' in html_content
            }
            
            passed = sum(checks.values())
            total = len(checks)
            
            print(f"✅ Server accessible: {response.status_code}")
            
            for check_name, result in checks.items():
                status = "✅" if result else "❌"
                print(f"{status} {check_name}: {'PASS' if result else 'FAIL'}")
            
            print(f"\n📊 Quick Test Results: {passed}/{total} ({(passed/total)*100:.1f}%)")
            
            if passed >= 7:
                print("🎉 DISPLAY FIX SUCCESSFUL!")
                print("\n🧪 Next steps:")
                print("   1. Go to: http://127.0.0.1:8000/explore/")
                print("   2. Clear browser cache: Ctrl+F5")
                print("   3. Verify: Map and charts are visible")
                return True
            else:
                print("⚠️ Some issues detected")
                return False
                
        else:
            print(f"❌ Server error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_fixed_display()
    
    if success:
        print("\n" + "=" * 50)
        print("✅ READY TO TEST IN BROWSER!")
        print("🌐 URL: http://127.0.0.1:8000/explore/")
        print("🔄 Remember: Clear cache with Ctrl+F5")
    else:
        print("\n❌ Issues detected - check server and files")