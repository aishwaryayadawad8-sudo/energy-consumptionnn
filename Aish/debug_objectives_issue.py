#!/usr/bin/env python3
"""
Debug script to identify why objectives 2 and 3 buttons might not be working
"""

import requests
import sys

def test_objective_pages():
    base_url = "http://127.0.0.1:8000"
    
    print("🔍 Debugging Objectives 2 and 3 Button Issues")
    print("=" * 60)
    
    # Test main page
    try:
        main_response = requests.get(f"{base_url}/country-forecasts/")
        print(f"✅ Main page: {main_response.status_code}")
    except Exception as e:
        print(f"❌ Main page error: {e}")
        return False
    
    # Test objectives
    objectives = [
        ("Objective 2", f"{base_url}/objective2/"),
        ("Objective 3", f"{base_url}/objective3/")
    ]
    
    for name, url in objectives:
        try:
            response = requests.get(url)
            print(f"✅ {name}: {response.status_code}")
            
            # Check if response contains expected content
            content = response.text
            if "CO₂ Emission Forecasting" in content and "objective2" in url:
                print(f"   ✓ Contains expected CO₂ content")
            elif "Energy Access Classification" in content and "objective3" in url:
                print(f"   ✓ Contains expected Energy Access content")
            else:
                print(f"   ⚠️  Content might be incorrect")
                
        except Exception as e:
            print(f"❌ {name}: Error - {e}")
    
    print("\n" + "=" * 60)
    print("🔧 TROUBLESHOOTING RECOMMENDATIONS:")
    print("=" * 60)
    
    print("1. CLEAR BROWSER CACHE:")
    print("   - Press Ctrl+Shift+Delete")
    print("   - Or press Ctrl+F5 for hard refresh")
    
    print("\n2. CHECK BROWSER CONSOLE:")
    print("   - Press F12 to open Developer Tools")
    print("   - Look for JavaScript errors in Console tab")
    print("   - Look for failed network requests in Network tab")
    
    print("\n3. TEST DIRECT NAVIGATION:")
    print("   - Copy these URLs directly into browser:")
    print(f"   - {base_url}/objective2/")
    print(f"   - {base_url}/objective3/")
    
    print("\n4. CHECK BUTTON ELEMENTS:")
    print("   - Right-click on the button")
    print("   - Select 'Inspect Element'")
    print("   - Verify the href attribute is correct")
    
    print("\n5. POSSIBLE CAUSES:")
    print("   - CSS z-index issues (button behind overlay)")
    print("   - JavaScript preventing default click behavior")
    print("   - Browser cache serving old version")
    print("   - CSS pointer-events: none on button")
    
    print("\n6. QUICK FIXES TO TRY:")
    print("   - Restart Django server")
    print("   - Try different browser")
    print("   - Disable browser extensions")
    print("   - Test in incognito/private mode")
    
    return True

if __name__ == "__main__":
    test_objective_pages()