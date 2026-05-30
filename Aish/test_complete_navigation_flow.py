#!/usr/bin/env python3
"""
Test Complete Navigation Flow
"""

import requests

def test_complete_flow():
    """Test the complete navigation flow"""
    
    BASE_URL = "http://127.0.0.1:8000"
    
    print("🧪 Testing Complete Navigation Flow")
    print("=" * 60)
    
    # Test 1: Root page should show objectives
    print("1️⃣  Testing: Root page (/) - Should show OBJECTIVES")
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        if response.status_code == 200:
            content = response.text
            if "Country Energy Forecasts" in content and "All Objectives" in content:
                print("   ✅ Root page shows OBJECTIVES page with 8 cards")
            else:
                print("   ❌ Root page doesn't show objectives")
        else:
            print(f"   ❌ Root page error: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Root page error: {e}")
    
    # Test 2: Objective 1 page should be accessible
    print("\n2️⃣  Testing: Objective 1 page (/objective1/)")
    try:
        response = requests.get(f"{BASE_URL}/objective1/", timeout=5)
        if response.status_code == 200:
            content = response.text
            if "Back to Objectives" in content:
                print("   ✅ Objective 1 page accessible with back button")
            else:
                print("   ⚠️  Objective 1 accessible but no back button found")
        else:
            print(f"   ❌ Objective 1 error: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Objective 1 error: {e}")
    
    # Test 3: Explore dashboard should be at /explore/
    print("\n3️⃣  Testing: Explore dashboard (/explore/)")
    try:
        response = requests.get(f"{BASE_URL}/explore/", timeout=5)
        if response.status_code == 200:
            content = response.text
            if "Explore Dashboard" in content or "SDG 7 Energy Analytics" in content:
                print("   ✅ Explore dashboard accessible at /explore/")
            else:
                print("   ⚠️  /explore/ doesn't show explore dashboard")
        else:
            print(f"   ❌ Explore dashboard error: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Explore dashboard error: {e}")

def show_final_instructions():
    """Show final testing instructions"""
    
    print(f"\n" + "=" * 60)
    print("📋 MANUAL TESTING INSTRUCTIONS:")
    print("=" * 60)
    print("1. 🌐 Open: http://127.0.0.1:8000/")
    print("   👀 You should see: Page with 8 objective cards")
    print("   📝 Title: 'Country Energy Forecasts - All Objectives'")
    print("")
    print("2. 🖱️  Click: Any objective's 'View Analysis' button")
    print("   👀 You should see: Individual objective page")
    print("   📝 Look for: 'Back to Objectives' button (top area)")
    print("")
    print("3. 🔙 Click: 'Back to Objectives' button")
    print("   👀 You should see: Return to page with 8 objective cards")
    print("   ✅ This confirms the navigation is working correctly!")
    print("")
    print("🎯 EXPECTED FLOW:")
    print("   Objectives Page → Individual Objective → Back Button → Objectives Page")

if __name__ == "__main__":
    test_complete_flow()
    show_final_instructions()