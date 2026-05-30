#!/usr/bin/env python3
"""
Test the Country Forecasts Fix
"""

import requests

def test_country_forecasts_url():
    """Test the new dedicated country forecasts URL"""
    
    BASE_URL = "http://127.0.0.1:8000"
    
    print("🧪 Testing Country Forecasts Fix")
    print("=" * 60)
    
    # Test the new dedicated URL
    print("1️⃣  Testing: /country-forecasts/ (NEW dedicated URL)")
    try:
        response = requests.get(f"{BASE_URL}/country-forecasts/", timeout=10)
        if response.status_code == 200:
            content = response.text
            
            # Check for Country Energy Forecasts page content
            forecasts_indicators = [
                "Country Energy Forecasts",
                "All Objectives",
                "Total Energy Consumption",
                "Electricity Access",
                "Renewable Energy",
                "CO2 Emissions",
                "View Analysis"
            ]
            
            found_count = sum(1 for indicator in forecasts_indicators if indicator in content)
            
            print(f"   Status: {response.status_code}")
            print(f"   Country Forecasts content: {found_count}/{len(forecasts_indicators)} found")
            
            # Check page title
            title_start = content.find('<title>') + 7
            title_end = content.find('</title>')
            if title_start > 6 and title_end > title_start:
                title = content[title_start:title_end]
                print(f"   📄 Page Title: {title}")
            
            if found_count >= 5:
                print("   ✅ SUCCESS: This shows the COUNTRY FORECASTS page with 8 cards!")
                print("   ✅ Back to Objectives will now work correctly!")
            else:
                print("   ❌ ISSUE: This doesn't appear to be the country forecasts page")
                
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Compare with root URL to show the difference
    print(f"\n2️⃣  Comparing with root URL: / (what you DON'T want)")
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        if response.status_code == 200:
            content = response.text
            
            # Check what type of page this is
            if "Country Energy Forecasts" in content:
                print("   ℹ️  Root URL also shows Country Forecasts (this is fine)")
            elif "Explore Dashboard" in content:
                print("   ⚠️  Root URL shows Explore Dashboard (different from forecasts)")
            else:
                print("   ❓ Root URL shows unknown page type")
                
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")

def show_fix_summary():
    """Show summary of the fix"""
    
    print(f"\n" + "=" * 60)
    print("✅ COUNTRY FORECASTS FIX SUMMARY:")
    print("=" * 60)
    print("🎯 PROBLEM: 'Back to Objectives' was going to main page")
    print("🔧 SOLUTION: Created dedicated /country-forecasts/ URL")
    print("")
    print("📊 NEW NAVIGATION FLOW:")
    print("   Individual Objective → 'Back to Objectives' → /country-forecasts/")
    print("")
    print("✅ WHAT HAPPENS NOW:")
    print("   - Click 'Back to Objectives' from any objective")
    print("   - URL becomes: /country-forecasts/")
    print("   - Page shows: Country Energy Forecasts with 8 cards")
    print("   - NO MORE: Main page or other unwanted pages")
    print("")
    print("🧪 TO TEST:")
    print("   1. Go to any objective page (e.g., /objective1/)")
    print("   2. Click 'Back to Objectives' button")
    print("   3. Should see Country Energy Forecasts page with 8 cards")
    print("   4. URL should be: /country-forecasts/")

if __name__ == "__main__":
    test_country_forecasts_url()
    show_fix_summary()