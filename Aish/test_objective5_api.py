#!/usr/bin/env python3
"""
Test Objective 5 API endpoints directly
"""

import requests
import json

def test_objective5_apis():
    """Test all Objective 5 API endpoints"""
    base_url = "http://127.0.0.1:8000"
    
    print("🧪 Testing Objective 5 API Endpoints")
    print("=" * 50)
    
    # Test 1: Model Comparison
    print("📊 Testing Model Comparison API...")
    try:
        response = requests.get(f"{base_url}/api/objective5/model-comparison/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Model Comparison: {response.status_code}")
            print(f"   Best Model: {data.get('best_model', 'Unknown')}")
            print(f"   Success: {data.get('success', False)}")
        else:
            print(f"❌ Model Comparison: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Model Comparison: Connection error - {e}")
    
    # Test 2: Countries List
    print("\n🌍 Testing Countries API...")
    try:
        response = requests.get(f"{base_url}/api/objective5/countries/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Countries: {response.status_code}")
            print(f"   Countries Count: {len(data.get('countries', []))}")
            print(f"   Success: {data.get('success', False)}")
            if data.get('countries'):
                print(f"   First 5: {data['countries'][:5]}")
        else:
            print(f"❌ Countries: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Countries: Connection error - {e}")
    
    # Test 3: Historical Data
    print("\n📊 Testing Historical Data API...")
    try:
        response = requests.get(f"{base_url}/api/objective5/historical/?country=United States", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Historical Data: {response.status_code}")
            print(f"   Data Points: {len(data.get('data', []))}")
            print(f"   Success: {data.get('success', False)}")
        else:
            print(f"❌ Historical Data: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Historical Data: Connection error - {e}")
    
    # Test 4: Future Predictions
    print("\n🔮 Testing Future Predictions API...")
    try:
        response = requests.get(f"{base_url}/api/objective5/predictions/?country=United States", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Future Predictions: {response.status_code}")
            print(f"   Predictions Count: {len(data.get('predictions', []))}")
            print(f"   Success: {data.get('success', False)}")
        else:
            print(f"❌ Future Predictions: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Future Predictions: Connection error - {e}")
    
    print("\n" + "=" * 50)
    print("🎯 API Test Complete!")

if __name__ == "__main__":
    test_objective5_apis()