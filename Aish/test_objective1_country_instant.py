#!/usr/bin/env python3
"""
Test Objective 1 Country Analysis Instant Loading
"""

import requests
import time

def test_country_apis():
    """Test the country analysis APIs for speed"""
    
    BASE_URL = "http://127.0.0.1:8000"
    
    print("🧪 Testing Objective 1 Country Analysis APIs")
    print("=" * 60)
    
    # Test countries endpoint
    try:
        print("📡 Testing /api/objective1/countries/")
        start_time = time.time()
        response = requests.get(f"{BASE_URL}/api/objective1/countries/", timeout=10)
        end_time = time.time()
        
        print(f"   Status: {response.status_code}")
        print(f"   Response Time: {end_time - start_time:.3f}s")
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                countries = data.get('countries', [])
                print(f"   ✅ Found {len(countries)} countries")
                
                # Test with a sample country
                if countries:
                    test_country = countries[0]
                    print(f"\n📊 Testing with country: {test_country}")
                    
                    # Test historical data
                    print("   📈 Testing historical data...")
                    start_time = time.time()
                    hist_response = requests.get(
                        f"{BASE_URL}/api/objective1/historical/?country={test_country}", 
                        timeout=10
                    )
                    end_time = time.time()
                    
                    print(f"      Status: {hist_response.status_code}")
                    print(f"      Response Time: {end_time - start_time:.3f}s")
                    
                    if hist_response.status_code == 200:
                        hist_data = hist_response.json()
                        if hist_data.get('success'):
                            data_points = len(hist_data.get('data', []))
                            print(f"      ✅ Historical data: {data_points} data points")
                        else:
                            print(f"      ❌ Historical data failed: {hist_data.get('error', 'Unknown')}")
                    
                    # Test predictions
                    print("   🔮 Testing predictions...")
                    start_time = time.time()
                    pred_response = requests.get(
                        f"{BASE_URL}/api/objective1/predictions/?country={test_country}&years=10", 
                        timeout=10
                    )
                    end_time = time.time()
                    
                    print(f"      Status: {pred_response.status_code}")
                    print(f"      Response Time: {end_time - start_time:.3f}s")
                    
                    if pred_response.status_code == 200:
                        pred_data = pred_response.json()
                        if pred_data.get('success'):
                            predictions = len(pred_data.get('predictions', []))
                            print(f"      ✅ Predictions: {predictions} data points")
                        else:
                            print(f"      ❌ Predictions failed: {pred_data.get('error', 'Unknown')}")
            else:
                print(f"   ❌ Countries API failed: {data.get('error', 'Unknown')}")
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("   ❌ Connection Error: Django server not running")
        print("   💡 Please start the Django server with: python manage.py runserver")
    except Exception as e:
        print(f"   ❌ Error: {e}")

def show_usage_instructions():
    """Show instructions for testing the instant loading"""
    
    print("\n" + "=" * 60)
    print("📋 HOW TO TEST INSTANT COUNTRY ANALYSIS:")
    print("=" * 60)
    print("1. 🌐 Open: http://127.0.0.1:8000/objective1/")
    print("2. 📊 The ML comparison chart should load instantly")
    print("3. 🌍 Select any country from the dropdown")
    print("4. 🖱️  Click 'Analyze Country' button")
    print("5. ⚡ Charts should appear INSTANTLY with sample data")
    print("6. 🔄 Real data will load in background and update charts")
    print("\n✨ Expected Behavior:")
    print("   - No more 'loadCountryData function called!' alert")
    print("   - Charts appear immediately (not after API calls)")
    print("   - Sample data shows first, then updates with real data")
    print("   - Smooth, professional user experience")

if __name__ == "__main__":
    test_country_apis()
    show_usage_instructions()