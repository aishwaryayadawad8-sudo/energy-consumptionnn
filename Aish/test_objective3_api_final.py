#!/usr/bin/env python3
"""
Test Objective 3 API endpoints to ensure they work correctly
"""

import requests
import json

def test_api_endpoint(url, description):
    """Test a single API endpoint"""
    print(f"\n🧪 Testing: {description}")
    print(f"📡 URL: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        print(f"📊 Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success: {data.get('success', 'N/A')}")
            
            # Print relevant data info
            if 'mse_scores' in data:
                print(f"📈 Models: {len(data['mse_scores'])} found")
                print(f"🏆 Best: {data.get('best_model', 'N/A')} ({data.get('best_score', 'N/A'):.4f})")
            elif 'countries' in data:
                print(f"🌍 Countries: {len(data['countries'])} available")
            elif 'data' in data:
                print(f"📊 Data points: {len(data['data'])}")
            elif 'predictions' in data:
                print(f"🔮 Predictions: {len(data['predictions'])}")
                
            return True
        else:
            print(f"❌ Failed: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Test all Objective 3 API endpoints"""
    print("🚀 Testing Objective 3 API Endpoints")
    print("=" * 50)
    
    base_url = "http://127.0.0.1:8000"
    test_country = "Australia"
    
    endpoints = [
        (f"{base_url}/api/objective3/model-comparison/", "Model Comparison"),
        (f"{base_url}/api/objective3/countries/", "Countries List"),
        (f"{base_url}/api/objective3/historical/?country={test_country}", f"Historical Data - {test_country}"),
        (f"{base_url}/api/objective3/predictions/?country={test_country}", f"Future Predictions - {test_country}"),
        (f"{base_url}/api/objective3/combined/?country={test_country}", f"Combined Data - {test_country}"),
    ]
    
    results = []
    for url, description in endpoints:
        success = test_api_endpoint(url, description)
        results.append((description, success))
    
    print("\n" + "=" * 50)
    print("📋 SUMMARY:")
    
    passed = 0
    for description, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {description}")
        if success:
            passed += 1
    
    print(f"\n🎯 Results: {passed}/{len(results)} endpoints working")
    
    if passed == len(results):
        print("🎉 All Objective 3 APIs are working perfectly!")
    else:
        print("⚠️  Some endpoints need attention")

if __name__ == "__main__":
    main()