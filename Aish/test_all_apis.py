"""
Quick API Test Script
Run this to verify all your APIs are working
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"

print("=" * 70)
print("🧪 Testing SDG 7 Dashboard APIs")
print("=" * 70)

# Test 1: Get All Countries
print("\n📋 Test 1: Get All Countries")
print("-" * 70)
try:
    response = requests.get(f"{BASE_URL}/api/countries/", timeout=5)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ SUCCESS - Status: {response.status_code}")
        print(f"   Found {len(data.get('countries', []))} countries")
        print(f"   First 5: {data.get('countries', [])[:5]}")
    else:
        print(f"❌ FAILED - Status: {response.status_code}")
except Exception as e:
    print(f"❌ ERROR: {e}")

# Test 2: Search India
print("\n🔍 Test 2: Search Country - India")
print("-" * 70)
try:
    response = requests.get(f"{BASE_URL}/api/search/", params={'country': 'India'}, timeout=5)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ SUCCESS - Status: {response.status_code}")
        print(f"   Country: {data.get('country')}")
        print(f"   Electricity Access: {data.get('electricity_access')}%")
        print(f"   Latest Year: {data.get('latest_year')}")
    else:
        print(f"❌ FAILED - Status: {response.status_code}")
except Exception as e:
    print(f"❌ ERROR: {e}")

# Test 3: Search Kenya
print("\n🔍 Test 3: Search Country - Kenya")
print("-" * 70)
try:
    response = requests.get(f"{BASE_URL}/api/search/", params={'country': 'Kenya'}, timeout=5)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ SUCCESS - Status: {response.status_code}")
        print(f"   Country: {data.get('country')}")
        print(f"   Electricity Access: {data.get('electricity_access')}%")
        print(f"   Status: {data.get('status', {}).get('status')}")
    else:
        print(f"❌ FAILED - Status: {response.status_code}")
except Exception as e:
    print(f"❌ ERROR: {e}")

# Test 4: Predict Future
print("\n🔮 Test 4: Predict Future - Kenya (5 years)")
print("-" * 70)
try:
    response = requests.get(f"{BASE_URL}/api/predict/", 
                          params={'country': 'Kenya', 'years': 5}, 
                          timeout=5)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ SUCCESS - Status: {response.status_code}")
        print(f"   Country: {data.get('country')}")
        print(f"   Model: {data.get('model_used')}")
        predictions = data.get('predictions', [])
        if predictions:
            print(f"   Predictions: {len(predictions)} years")
            print(f"   First prediction: Year {predictions[0].get('year')} - {predictions[0].get('predicted_access')}%")
    else:
        print(f"❌ FAILED - Status: {response.status_code}")
except Exception as e:
    print(f"❌ ERROR: {e}")

# Test 5: Get Map Data
print("\n🗺️  Test 5: Get Map Data")
print("-" * 70)
try:
    response = requests.get(f"{BASE_URL}/api/map-data/", timeout=5)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ SUCCESS - Status: {response.status_code}")
        map_data = data.get('map_data', [])
        print(f"   Countries on map: {len(map_data)}")
        if map_data:
            print(f"   Sample: {map_data[0].get('country')} at ({map_data[0].get('lat')}, {map_data[0].get('lon')})")
    else:
        print(f"❌ FAILED - Status: {response.status_code}")
except Exception as e:
    print(f"❌ ERROR: {e}")

# Test 6: Objective 1 - Model Comparison
print("\n⚡ Test 6: Objective 1 - Model Comparison")
print("-" * 70)
try:
    response = requests.get(f"{BASE_URL}/api/objective1/model-comparison/", timeout=5)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ SUCCESS - Status: {response.status_code}")
        print(f"   Best Model: {data.get('best_model')}")
        models = data.get('models', {})
        for model, score in models.items():
            print(f"   {model}: {score}")
    else:
        print(f"❌ FAILED - Status: {response.status_code}")
except Exception as e:
    print(f"❌ ERROR: {e}")

# Test 7: Objective 2 - Model Comparison
print("\n💨 Test 7: Objective 2 - Model Comparison")
print("-" * 70)
try:
    response = requests.get(f"{BASE_URL}/api/objective2/model-comparison/", timeout=5)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ SUCCESS - Status: {response.status_code}")
        print(f"   Best Model: {data.get('best_model')}")
    else:
        print(f"❌ FAILED - Status: {response.status_code}")
except Exception as e:
    print(f"❌ ERROR: {e}")

# Test 8: Objective 3 - Model Comparison
print("\n🔌 Test 8: Objective 3 - Model Comparison")
print("-" * 70)
try:
    response = requests.get(f"{BASE_URL}/api/objective3/model-comparison/", timeout=5)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ SUCCESS - Status: {response.status_code}")
        print(f"   Best Model: {data.get('best_model')}")
    else:
        print(f"❌ FAILED - Status: {response.status_code}")
except Exception as e:
    print(f"❌ ERROR: {e}")

# Summary
print("\n" + "=" * 70)
print("📊 Test Summary")
print("=" * 70)
print("✅ If all tests show SUCCESS, your APIs are working perfectly!")
print("❌ If any test shows FAILED or ERROR, check:")
print("   1. Django server is running (python manage.py runserver)")
print("   2. Server is at http://127.0.0.1:8000/")
print("   3. No errors in Django console")
print("\n🎉 Ready to test in Postman!")
print("=" * 70)
