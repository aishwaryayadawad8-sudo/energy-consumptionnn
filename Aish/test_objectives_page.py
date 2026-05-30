#!/usr/bin/env python3
"""
Test Objectives Page Navigation
"""

import requests

def test_objectives_page():
    """Test that the objectives page is working correctly"""
    
    BASE_URL = "http://127.0.0.1:8000"
    
    print("🧪 Testing Objectives Page Navigation")
    print("=" * 60)
    
    try:
        print("📡 Testing root page: /")
        response = requests.get(f"{BASE_URL}/", timeout=10)
        
        print(f"   Status Code: {response.status_code}")
        
        if response.status_code == 200:
            content = response.text
            
            # Check for objective selector specific content
            objective_checks = [
                ("Country Energy Forecasts", "Main title"),
                ("All Objectives", "Section title"),
                ("Total Energy Consumption", "Objective 1 title"),
                ("Electricity Access", "Objective 2 title"),
                ("Renewable Energy", "Objective 3 title"),
                ("CO2 Emissions", "Objective 4 title"),
                ("Country-Specific", "Objective 5 title"),
                ("Policy Impact", "Objective 6 title"),
                ("Investment Strategy", "Objective 7 title"),
                ("Admin Panel", "Objective 8 title"),
                ("View Analysis", "Analysis buttons")
            ]
            
            print("   🔍 Checking for objectives page content:")
            objectives_found = 0
            for check_text, description in objective_checks:
                if check_text in content:
                    print(f"      ✅ {description}: Found")
                    objectives_found += 1
                else:
                    print(f"      ❌ {description}: Missing")
            
            # Check if this looks like the explore dashboard instead
            explore_indicators = [
                "Explore Dashboard",
                "SDG 7 Energy Analytics", 
                "Energy Mix Chart",
                "Country Highlight"
            ]
            
            explore_found = 0
            for indicator in explore_indicators:
                if indicator in content:
                    explore_found += 1
            
            print(f"\n   📊 Analysis:")
            print(f"      Objectives content found: {objectives_found}/11")
            print(f"      Explore dashboard indicators: {explore_found}/4")
            
            if objectives_found >= 6:
                print("   ✅ This appears to be the OBJECTIVES page (correct)")
            elif explore_found >= 2:
                print("   ❌ This appears to be the EXPLORE dashboard (wrong)")
            else:
                print("   ⚠️  Unclear which page this is")
                
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("   ❌ Connection Error: Django server not running")
        print("   💡 Please start the Django server with: python manage.py runserver")
    except Exception as e:
        print(f"   ❌ Error: {e}")

def test_explore_page():
    """Test the explore dashboard page"""
    
    BASE_URL = "http://127.0.0.1:8000"
    
    print(f"\n📊 Testing Explore Dashboard: /explore/")
    
    try:
        response = requests.get(f"{BASE_URL}/explore/", timeout=10)
        
        print(f"   Status Code: {response.status_code}")
        
        if response.status_code == 200:
            content = response.text
            
            if "Explore Dashboard" in content or "SDG 7 Energy Analytics" in content:
                print("   ✅ Explore dashboard is accessible at /explore/")
            else:
                print("   ⚠️  /explore/ doesn't seem to be the explore dashboard")
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")

def show_navigation_summary():
    """Show the expected navigation flow"""
    
    print(f"\n" + "=" * 60)
    print("📋 EXPECTED NAVIGATION FLOW:")
    print("=" * 60)
    print("1. 🏠 Root page (/): Should show OBJECTIVES page with 8 cards")
    print("2. 🔍 Explore page (/explore/): Should show EXPLORE dashboard")
    print("3. 📊 Objective pages (/objective1/, etc.): Individual objectives")
    print("4. 🔙 'Back to Objectives' button: Should go to / (objectives page)")
    print("\n✅ If root page shows objectives, navigation is working correctly!")

if __name__ == "__main__":
    test_objectives_page()
    test_explore_page()
    show_navigation_summary()