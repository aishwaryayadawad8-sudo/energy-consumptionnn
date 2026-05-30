#!/usr/bin/env python3
"""
Test comprehensive comparison page loading
"""

import requests
import time

def test_page_and_api():
    """Test both the page and API"""
    
    print("🧪 Testing Comprehensive Comparison Page")
    print("="*50)
    
    base_url = "http://127.0.0.1:8000"
    
    # Test 1: Check if page loads
    print("1️⃣ Testing page load...")
    try:
        response = requests.get(f"{base_url}/comprehensive-comparison/", timeout=10)
        print(f"   Page Status: {response.status_code}")
        
        if response.status_code == 200:
            content = response.text
            if "Comprehensive ML Model Comparison" in content:
                print("   ✅ Page loads with correct title")
            else:
                print("   ⚠️  Page loads but title missing")
                
            if "chart.js" in content:
                print("   ✅ Chart.js library included")
            else:
                print("   ❌ Chart.js library missing")
                
        else:
            print(f"   ❌ Page failed to load: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("   ❌ Connection failed - is Django server running?")
        print("   Run: python manage.py runserver")
        return
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return
    
    # Test 2: Check API endpoint
    print("\n2️⃣ Testing API endpoint...")
    try:
        response = requests.get(f"{base_url}/api/comprehensive-comparison/", timeout=30)
        print(f"   API Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('success'):
                print("   ✅ API returns success")
                
                objectives = data.get('objectives', [])
                results = data.get('results', {})
                
                print(f"   📊 Objectives: {len(objectives)}")
                print(f"   📈 Results: {len(results)}")
                
                # Check if all 8 objectives have 7 models
                missing_objectives = []
                for i in range(1, 9):
                    if str(i) not in results:
                        missing_objectives.append(i)
                    else:
                        models = list(results[str(i)].keys())
                        if len(models) != 7:
                            print(f"   ⚠️  Objective {i}: Only {len(models)} models")
                        else:
                            print(f"   ✅ Objective {i}: {len(models)} models")
                
                if missing_objectives:
                    print(f"   ❌ Missing objectives: {missing_objectives}")
                else:
                    print("   ✅ All 8 objectives present")
                    
            else:
                print("   ❌ API returns error:")
                print(f"      {data.get('error', 'Unknown error')}")
        else:
            print(f"   ❌ API failed: {response.status_code}")
            print(f"   Response: {response.text[:200]}...")
            
    except Exception as e:
        print(f"   ❌ API Error: {e}")
    
    # Test 3: Check if JavaScript can fetch data
    print("\n3️⃣ Simulating JavaScript fetch...")
    try:
        headers = {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
        }
        response = requests.get(f"{base_url}/api/comprehensive-comparison/", 
                              headers=headers, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print("   ✅ JavaScript-style request works")
                
                # Show sample data
                if '3' in data.get('results', {}):
                    obj3_models = list(data['results']['3'].keys())
                    print(f"   📋 Objective 3 models: {obj3_models}")
            else:
                print("   ❌ JavaScript-style request failed")
        else:
            print(f"   ❌ JavaScript-style request error: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ JavaScript simulation error: {e}")
    
    print("\n🔍 Troubleshooting Steps:")
    print("1. Make sure Django server is running: python manage.py runserver")
    print("2. Visit: http://127.0.0.1:8000/comprehensive-comparison/")
    print("3. Open browser developer tools (F12)")
    print("4. Check Console tab for JavaScript errors")
    print("5. Check Network tab to see if API calls are made")
    print("6. If page is blank, check if loading overlay is stuck")

if __name__ == "__main__":
    test_page_and_api()