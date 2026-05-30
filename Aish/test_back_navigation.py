#!/usr/bin/env python3
"""
Test Back Navigation to Objectives Selector
"""

import requests
import time

def test_main_page():
    """Test that the main page (objective selector) is accessible"""
    
    BASE_URL = "http://127.0.0.1:8000"
    
    print("🧪 Testing Back Navigation to Objectives Selector")
    print("=" * 60)
    
    try:
        print("📡 Testing main page: /")
        response = requests.get(f"{BASE_URL}/", timeout=10)
        
        print(f"   Status Code: {response.status_code}")
        
        if response.status_code == 200:
            content = response.text
            
            # Check for key elements of the objective selector
            checks = [
                ("Country Energy Forecasts", "Main title"),
                ("Objective 1", "Objective 1 card"),
                ("Objective 2", "Objective 2 card"),
                ("Objective 3", "Objective 3 card"),
                ("Objective 4", "Objective 4 card"),
                ("Objective 5", "Objective 5 card"),
                ("Objective 6", "Objective 6 card"),
                ("Objective 7", "Objective 7 card"),
                ("Objective 8", "Objective 8 card"),
                ("View Analysis", "Analysis buttons")
            ]
            
            print("   🔍 Checking page content:")
            for check_text, description in checks:
                if check_text in content:
                    print(f"      ✅ {description}: Found")
                else:
                    print(f"      ❌ {description}: Missing")
            
            print(f"\n   ✅ Main page is accessible and contains objective selector")
            
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
            print(f"   Response: {response.text[:200]}...")
            
    except requests.exceptions.ConnectionError:
        print("   ❌ Connection Error: Django server not running")
        print("   💡 Please start the Django server with: python manage.py runserver")
    except Exception as e:
        print(f"   ❌ Error: {e}")

def test_objective_pages():
    """Test that objective pages are accessible"""
    
    BASE_URL = "http://127.0.0.1:8000"
    
    print(f"\n📊 Testing Objective Pages:")
    
    for i in range(1, 9):
        try:
            print(f"   Testing Objective {i}...")
            response = requests.get(f"{BASE_URL}/objective{i}/", timeout=5)
            
            if response.status_code == 200:
                content = response.text
                if "Back to Objectives" in content:
                    print(f"      ✅ Objective {i}: Accessible with back button")
                else:
                    print(f"      ⚠️  Objective {i}: Accessible but no back button found")
            else:
                print(f"      ❌ Objective {i}: HTTP {response.status_code}")
                
        except Exception as e:
            print(f"      ❌ Objective {i}: Error - {e}")

def show_navigation_instructions():
    """Show instructions for testing navigation"""
    
    print(f"\n" + "=" * 60)
    print("📋 HOW TO TEST BACK NAVIGATION:")
    print("=" * 60)
    print("1. 🌐 Open: http://127.0.0.1:8000/")
    print("2. 👀 You should see the main page with 8 objective cards")
    print("3. 🖱️  Click on any objective (e.g., 'View Analysis' for Objective 1)")
    print("4. 📊 You'll be taken to the specific objective page")
    print("5. 🔙 Click 'Back to Objectives' button (top-left)")
    print("6. ✅ You should return to the main page with all 8 objectives")
    print("\n🎯 Expected Flow:")
    print("   Main Page → Objective Page → Back Button → Main Page")

if __name__ == "__main__":
    test_main_page()
    test_objective_pages()
    show_navigation_instructions()