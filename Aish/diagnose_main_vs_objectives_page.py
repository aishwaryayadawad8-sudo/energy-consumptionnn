#!/usr/bin/env python3
"""
Diagnose Main Page vs Objectives Page Issue
"""

import requests

def check_different_urls():
    """Check what's served at different URLs"""
    
    BASE_URL = "http://127.0.0.1:8000"
    
    print("🔍 Checking Different URLs")
    print("=" * 60)
    
    urls_to_check = [
        ("/", "Root URL"),
        ("/explore/", "Explore Dashboard"),
        ("/dashboard/", "Dashboard Redirect"),
    ]
    
    for url, description in urls_to_check:
        print(f"\n📡 Testing: {url} ({description})")
        try:
            response = requests.get(f"{BASE_URL}{url}", timeout=5)
            if response.status_code == 200:
                content = response.text
                
                # Check for objectives page indicators
                objectives_indicators = [
                    "Country Energy Forecasts",
                    "All Objectives",
                    "Total Energy Consumption",
                    "View Analysis"
                ]
                
                # Check for explore dashboard indicators
                explore_indicators = [
                    "Explore Dashboard",
                    "SDG 7 Energy Analytics",
                    "Energy Mix Chart"
                ]
                
                objectives_found = sum(1 for indicator in objectives_indicators if indicator in content)
                explore_found = sum(1 for indicator in explore_indicators if indicator in content)
                
                print(f"   Status: {response.status_code}")
                print(f"   Objectives indicators: {objectives_found}/{len(objectives_indicators)}")
                print(f"   Explore indicators: {explore_found}/{len(explore_indicators)}")
                
                if objectives_found >= 3:
                    print(f"   🎯 This appears to be: OBJECTIVES PAGE (8 cards)")
                elif explore_found >= 2:
                    print(f"   🎯 This appears to be: EXPLORE DASHBOARD")
                else:
                    print(f"   🎯 This appears to be: UNKNOWN PAGE")
                    
                # Show title
                title_start = content.find('<title>') + 7
                title_end = content.find('</title>')
                if title_start > 6 and title_end > title_start:
                    title = content[title_start:title_end]
                    print(f"   📄 Page title: {title}")
                    
            else:
                print(f"   ❌ HTTP Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")

def show_current_back_button_behavior():
    """Show what the back buttons currently do"""
    
    print(f"\n" + "=" * 60)
    print("🔙 CURRENT BACK BUTTON BEHAVIOR:")
    print("=" * 60)
    print("All back buttons currently use: window.location.href='/?t=timestamp'")
    print("This should take you to: Root URL (/)")
    print("")
    print("📋 DIAGNOSIS:")
    print("If the root URL (/) is showing the wrong page, we need to:")
    print("1. Check if there's a redirect happening")
    print("2. Check if the wrong template is being served")
    print("3. Possibly change the back button to go to a different URL")

if __name__ == "__main__":
    check_different_urls()
    show_current_back_button_behavior()