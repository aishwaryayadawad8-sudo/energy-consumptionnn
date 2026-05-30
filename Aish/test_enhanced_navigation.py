#!/usr/bin/env python3
"""
Test Enhanced Navigation
"""

import requests

def test_enhanced_navigation():
    """Test the enhanced navigation with objectives parameter"""
    
    BASE_URL = "http://127.0.0.1:8000"
    
    print("🧪 Testing Enhanced Back to Objectives Navigation")
    print("=" * 60)
    
    # Test the enhanced URL
    print("1️⃣  Testing: /?objectives=true")
    try:
        response = requests.get(f"{BASE_URL}/?objectives=true", timeout=10)
        if response.status_code == 200:
            content = response.text
            
            # Check for objectives page content
            objectives_checks = [
                "Country Energy Forecasts",
                "All Objectives",
                "Total Energy Consumption",
                "Electricity Access",
                "Renewable Energy",
                "CO2 Emissions",
                "View Analysis"
            ]
            
            found_count = sum(1 for check in objectives_checks if check in content)
            
            print(f"   Status: {response.status_code}")
            print(f"   Objectives content: {found_count}/{len(objectives_checks)} found")
            
            if found_count >= 5:
                print("   ✅ SUCCESS: This shows the OBJECTIVES PAGE with 8 cards")
            else:
                print("   ❌ ISSUE: This doesn't appear to be the objectives page")
                
            # Check cache headers
            cache_control = response.headers.get('Cache-Control', 'Not set')
            print(f"   Cache-Control: {cache_control}")
            
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test regular root URL for comparison
    print(f"\n2️⃣  Testing: / (for comparison)")
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        if response.status_code == 200:
            content = response.text
            objectives_found = sum(1 for check in ["Country Energy Forecasts", "All Objectives", "View Analysis"] if check in content)
            print(f"   Status: {response.status_code}")
            print(f"   Objectives content: {objectives_found}/3 key indicators found")
            
            if objectives_found >= 2:
                print("   ✅ This also shows the objectives page")
            else:
                print("   ❌ This shows a different page")
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")

def show_final_instructions():
    """Show final testing instructions"""
    
    print(f"\n" + "=" * 60)
    print("📋 FINAL TESTING INSTRUCTIONS:")
    print("=" * 60)
    print("The 'Back to Objectives' button now uses enhanced navigation.")
    print("")
    print("🔄 To test:")
    print("1. 🌐 Go to: http://127.0.0.1:8000/objective1/")
    print("2. 🔙 Click: 'Back to Objectives' button")
    print("3. ✅ Expected: Page with 8 objective cards")
    print("   - Title: 'Energy & emissions projections 2050'")
    print("   - Cards: Total Energy, Electricity Access, Renewable Energy, etc.")
    print("")
    print("🛠️  If it still doesn't work:")
    print("1. 🔄 Hard refresh: Ctrl+F5")
    print("2. 🧹 Clear browser cache completely")
    print("3. 🕵️ Try incognito/private mode")
    print("4. 🌐 Open: back_to_objectives_test.html (created in current folder)")
    print("")
    print("🎯 The enhanced navigation now:")
    print("   - Uses /?objectives=true parameter")
    print("   - Forces no-cache headers")
    print("   - Should bypass any caching issues")

if __name__ == "__main__":
    test_enhanced_navigation()
    show_final_instructions()