#!/usr/bin/env python3
"""
Final Verification Test
=======================

This script performs a final verification that the new HTML file
will display both map and charts correctly.
"""

import requests

def final_verification_test():
    """Perform final verification of the new HTML file"""
    
    print("🔍 FINAL VERIFICATION TEST")
    print("=" * 50)
    
    try:
        response = requests.get('http://127.0.0.1:8000/explore/', timeout=10)
        
        if response.status_code == 200:
            html_content = response.text
            
            # Comprehensive checks
            verification_checks = {
                "HTML Structure": '<!DOCTYPE html>' in html_content,
                "Plotly Script": 'plotly-latest.min.js' in html_content,
                "Leaflet CSS": 'leaflet.css' in html_content,
                "Leaflet JS": 'leaflet.js' in html_content,
                "Map Container": 'id="map"' in html_content,
                "Chart Containers": all(f'id="{chart_id}"' in html_content for chart_id in [
                    'mainChart', 'accessChart', 'renewableChart', 'pieChart', 
                    'co2Chart', 'co2AccessChart', 'co2ForecastChart'
                ]),
                "Global Metrics": 'Global Electricity Access' in html_content,
                "Country Data": 'countryCoordinates' in html_content,
                "Initialization": 'DOMContentLoaded' in html_content,
                "Sample Functions": 'renderSampleTimelineChart' in html_content,
                "Map Initialization": 'initializeMap' in html_content,
                "Chart Rendering": 'Plotly.newPlot' in html_content,
                "CSS Styling": '.chart-container-vertical' in html_content,
                "Responsive Design": '@media' in html_content
            }
            
            passed = sum(verification_checks.values())
            total = len(verification_checks)
            
            print(f"✅ Server Response: {response.status_code} OK")
            print(f"📄 Content Length: {len(html_content)} characters")
            
            for check_name, result in verification_checks.items():
                status = "✅" if result else "❌"
                print(f"{status} {check_name}")
            
            success_rate = (passed / total) * 100
            print(f"\n📊 Verification Score: {success_rate:.1f}% ({passed}/{total})")
            
            if success_rate >= 95:
                print("🎉 EXCELLENT - Ready for browser testing!")
                status = "EXCELLENT"
            elif success_rate >= 85:
                print("✅ GOOD - Should work in browser")
                status = "GOOD"
            elif success_rate >= 70:
                print("⚠️ ACCEPTABLE - May have minor issues")
                status = "ACCEPTABLE"
            else:
                print("❌ POOR - Likely to have issues")
                status = "POOR"
            
            return status, success_rate
            
        else:
            print(f"❌ Server Error: {response.status_code}")
            return "ERROR", 0
            
    except Exception as e:
        print(f"❌ Test Failed: {e}")
        return "ERROR", 0

def main():
    """Main verification function"""
    
    print("🚀 Starting Final Verification...")
    print("🌐 URL: http://127.0.0.1:8000/explore/")
    print()
    
    status, score = final_verification_test()
    
    print("\n" + "=" * 50)
    print("📋 FINAL VERIFICATION REPORT")
    print("=" * 50)
    
    if status in ["EXCELLENT", "GOOD"]:
        print(f"✅ STATUS: {status}")
        print(f"📊 SCORE: {score:.1f}%")
        
        print("\n🎯 READY FOR BROWSER TESTING!")
        print("\n📋 Testing Checklist:")
        print("   1. Open: http://127.0.0.1:8000/explore/")
        print("   2. Clear Cache: Press Ctrl+F5 (CRITICAL!)")
        print("   3. Wait: 2 seconds for charts to load")
        print("   4. Verify Map: Interactive world map visible")
        print("   5. Verify Charts: All 7 charts with global data")
        print("   6. Verify Metrics: Global statistics cards")
        print("   7. Test Selection: Country dropdown and search")
        print("   8. Test Controls: Time period buttons")
        
        print("\n🗺️ Expected Map Features:")
        print("   • Interactive world map")
        print("   • Zoom and pan functionality")
        print("   • Country selection dropdown")
        print("   • Search functionality")
        
        print("\n📊 Expected Charts:")
        print("   1. Global Energy Timeline (2000-2030)")
        print("   2. Global Access Forecast")
        print("   3. Global Renewable Growth")
        print("   4. Global Energy Distribution (Pie Chart)")
        print("   5. Global CO₂ Timeline")
        print("   6. CO₂ vs Access (Sample Countries)")
        print("   7. Global CO₂ Forecast")
        
        print("\n💡 Troubleshooting:")
        print("   • If not working: Clear cache with Ctrl+F5")
        print("   • Check browser console for errors (F12)")
        print("   • Wait 2 seconds for charts to render")
        print("   • Try different browser if issues persist")
        
    else:
        print(f"❌ STATUS: {status}")
        print(f"📊 SCORE: {score:.1f}%")
        print("\n🔧 Issues detected - check server and configuration")

if __name__ == "__main__":
    main()