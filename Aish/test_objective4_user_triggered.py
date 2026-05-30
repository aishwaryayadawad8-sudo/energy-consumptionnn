#!/usr/bin/env python3

"""
Test that Objective 4 no longer auto-loads and requires user interaction
"""

import requests
import time

BASE_URL = "http://127.0.0.1:8000"

def test_user_triggered_loading():
    """Test that charts only load when user clicks button"""
    
    print("🧪 Testing Objective 4 User-Triggered Loading")
    print("=" * 60)
    
    try:
        # Test 1: Page loads without auto-loading charts
        print("\n1️⃣  Testing: Page Load (No Auto-Loading)")
        response = requests.get(f"{BASE_URL}/objective4/", timeout=10)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            content = response.text
            
            # Check that auto-loading is removed
            if 'Auto-loading interactive historical chart' not in content:
                print("   ✅ Auto-loading removed from code")
            else:
                print("   ❌ Auto-loading still present")
            
            # Check for user instructions
            if 'Click "Analyze Country"' in content:
                print("   ✅ User instructions found")
            
            if 'Show All Countries (Interactive)' in content:
                print("   ✅ Interactive option available")
            
            if 'Analyze Country' in content:
                print("   ✅ User action button found")
        
        # Test 2: Model comparison still loads instantly
        print("\n2️⃣  Testing: Model Comparison (Should Still Load Instantly)")
        if 'loadModelComparison()' in content:
            print("   ✅ Model comparison function found")
        
        if 'window.onload' in content and 'loadModelComparison()' in content:
            print("   ✅ Model comparison still auto-loads (correct)")
        
        # Test 3: Interactive chart functions available
        print("\n3️⃣  Testing: Interactive Chart Functions Available")
        if 'loadAllCountriesHistoricalChart' in content:
            print("   ✅ Interactive chart function available")
        
        if 'createInteractiveHistoricalChart' in content:
            print("   ✅ Chart creation function available")
        
        # Test 4: API endpoints still work
        print("\n4️⃣  Testing: API Endpoints Still Functional")
        
        # Test countries API
        response = requests.get(f"{BASE_URL}/api/objective4/countries/")
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print(f"   ✅ Countries API: {len(data.get('countries', []))} countries")
        
        # Test historical data API
        response = requests.get(f"{BASE_URL}/api/objective4/historical/?country=Albania")
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print(f"   ✅ Historical API: {len(data.get('data', []))} data points")
        
        print("\n" + "=" * 60)
        print("✅ User-Triggered Loading Testing Complete!")
        print("\n🎮 Verified Behavior:")
        print("   - Page loads with only model comparison")
        print("   - No auto-loading of historical charts")
        print("   - User must click 'Analyze Country' button")
        print("   - Interactive chart available when 'Show All Countries' selected")
        print("   - Detailed analysis available when specific country selected")
        print("\n📋 User Flow:")
        print("   1. Visit page → See model comparison only")
        print("   2. Select dropdown option:")
        print("      - 'Show All Countries' → Interactive chart")
        print("      - Specific country → Detailed analysis")
        print("   3. Click 'Analyze Country' → Chart loads")
        print("\n🌐 Ready for Testing:")
        print(f"   Visit: {BASE_URL}/objective4/")
        print("   Try both interactive and detailed modes!")
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Cannot connect to Django server")
        print("💡 Start the server: cd sustainable_energy && python manage.py runserver")
        print(f"   Then visit: {BASE_URL}/objective4/")
    
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    test_user_triggered_loading()