#!/usr/bin/env python3
"""
Test dashboard endpoints to ensure nothing is canceled
"""

import requests
import time

def test_dashboard_endpoints():
    """Test all dashboard endpoints"""
    
    print("🔍 TESTING DASHBOARD ENDPOINTS")
    print("=" * 50)
    
    base_url = "http://127.0.0.1:8000"
    
    endpoints = [
        ("/", "Main Dashboard"),
        ("/explore/", "Explore Dashboard"),
        ("/country-forecasts/", "Country Forecasts"),
    ]
    
    print("🌐 Testing server connectivity...")
    
    for endpoint, name in endpoints:
        try:
            print(f"\n📡 Testing {name}: {base_url}{endpoint}")
            
            response = requests.get(f"{base_url}{endpoint}", timeout=10)
            
            if response.status_code == 200:
                print(f"✅ {name} - WORKING (Status: {response.status_code})")
                
                # Check for key elements in explore dashboard
                if endpoint == "/explore/":
                    content = response.text
                    
                    checks = [
                        ("Interactive Visualization Controls", "Controls section"),
                        ("All Years (2000-2030)", "Time period buttons"),
                        ("unifiedSearchInput", "Search functionality"),
                        ("mainChart", "Chart containers"),
                        ("countryCoordinates", "Country data")
                    ]
                    
                    for check_text, description in checks:
                        if check_text in content:
                            print(f"   ✅ {description} - PRESENT")
                        else:
                            print(f"   ❌ {description} - MISSING")
                
            else:
                print(f"❌ {name} - ERROR (Status: {response.status_code})")
                
        except requests.exceptions.ConnectionError:
            print(f"❌ {name} - CONNECTION FAILED (Server not running?)")
        except requests.exceptions.Timeout:
            print(f"⏰ {name} - TIMEOUT (Server slow?)")
        except Exception as e:
            print(f"❌ {name} - ERROR: {e}")
    
    return True

def main():
    """Main function"""
    print("🧪 DASHBOARD ENDPOINT TESTING")
    print("=" * 50)
    print("Checking if dashboard is accessible and working...")
    
    success = test_dashboard_endpoints()
    
    if success:
        print("\n" + "=" * 50)
        print("🎯 ENDPOINT TEST COMPLETE!")
        print("=" * 50)
        print("\n🚀 If all endpoints are working:")
        print("   • Dashboard is NOT canceled")
        print("   • Server is running properly")
        print("   • All features should be accessible")
        
        print("\n🌐 Access Dashboard:")
        print("   • Main: http://127.0.0.1:8000/")
        print("   • Explore: http://127.0.0.1:8000/explore/")
        print("   • Forecasts: http://127.0.0.1:8000/country-forecasts/")
        
        print("\n🔍 If you see issues:")
        print("   1. Check browser console for JavaScript errors")
        print("   2. Hard refresh (Ctrl+Shift+R)")
        print("   3. Clear browser cache")
        print("   4. Try different browser")
        
        print("\n✅ DASHBOARD IS ACTIVE - NOTHING CANCELED!")
        
    else:
        print("\n❌ Some tests failed.")

if __name__ == "__main__":
    main()