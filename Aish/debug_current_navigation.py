#!/usr/bin/env python3
"""
Debug Current Navigation Issue
"""

import requests

def debug_navigation():
    """Debug what's actually happening with navigation"""
    
    BASE_URL = "http://127.0.0.1:8000"
    
    print("🔍 Debugging Navigation Issue")
    print("=" * 60)
    
    # Test what's actually at the root URL
    print("1️⃣  Checking what's at root URL (/):")
    try:
        response = requests.get(f"{BASE_URL}/", timeout=10)
        if response.status_code == 200:
            content = response.text
            
            # Check for different page indicators
            indicators = {
                "Objectives Page": [
                    "Country Energy Forecasts",
                    "All Objectives", 
                    "Total Energy Consumption",
                    "Electricity Access",
                    "View Analysis"
                ],
                "Explore Dashboard": [
                    "Explore Dashboard",
                    "SDG 7 Energy Analytics",
                    "Energy Mix Chart",
                    "Country Highlight"
                ],
                "Other Page": [
                    "Django",
                    "Welcome",
                    "Error"
                ]
            }
            
            for page_type, checks in indicators.items():
                found = sum(1 for check in checks if check in content)
                print(f"   {page_type}: {found}/{len(checks)} indicators found")
                if found >= len(checks) // 2:
                    print(f"   🎯 This appears to be: {page_type}")
            
            # Show first 500 characters of the page
            print(f"\n   📄 First 500 characters of page:")
            print(f"   {content[:500]}...")
            
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test the back button URL specifically
    print(f"\n2️⃣  Testing back button behavior:")
    print(f"   Current back button should use: window.location.href='/'")
    print(f"   This should take you to: Root page with objectives")
    
    # Check if there are any redirects
    print(f"\n3️⃣  Checking for redirects:")
    try:
        response = requests.get(f"{BASE_URL}/", allow_redirects=False, timeout=5)
        if response.status_code in [301, 302, 303, 307, 308]:
            print(f"   ⚠️  Root URL redirects to: {response.headers.get('Location', 'Unknown')}")
        else:
            print(f"   ✅ No redirects, serves content directly")
    except Exception as e:
        print(f"   ❌ Error checking redirects: {e}")

def show_troubleshooting_steps():
    """Show troubleshooting steps"""
    
    print(f"\n" + "=" * 60)
    print("🛠️  TROUBLESHOOTING STEPS:")
    print("=" * 60)
    print("1. 🔄 Try hard refresh: Ctrl+F5 or Ctrl+Shift+R")
    print("2. 🧹 Clear browser cache and cookies")
    print("3. 🔍 Check browser developer tools (F12) for errors")
    print("4. 🌐 Try in incognito/private browsing mode")
    print("5. 🔄 Restart Django server: python manage.py runserver")
    print("\n📋 What to look for:")
    print("   - Root page (/) should show 8 objective cards")
    print("   - Title should be 'Country Energy Forecasts - All Objectives'")
    print("   - Each card should have 'View Analysis' button")

if __name__ == "__main__":
    debug_navigation()
    show_troubleshooting_steps()