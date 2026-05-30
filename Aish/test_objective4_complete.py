#!/usr/bin/env python3
"""
Test Objective 4: SDG 7 Monitoring with Model Comparison
Tests the complete flow with 7 ML algorithms
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_objective4():
    print("\n" + "="*70)
    print("🧪 Testing Objective 4: SDG 7 Monitoring")
    print("="*70)
    
    # Test 1: Get all countries
    print("\n1️⃣  Testing: Get all countries")
    response = requests.get(f"{BASE_URL}/api/objective4/countries/")
    data = response.json()
    
    if data['success']:
        print(f"   ✅ Found {len(data['countries'])} countries")
        print(f"   📋 Sample countries: {data['countries'][:5]}")
    else:
        print(f"   ❌ Failed to get countries")
        return
    
    # Test 2: Model Comparison (7 algorithms)
    print("\n2️⃣  Testing: Model Comparison (7 Algorithms)")
    response = requests.get(f"{BASE_URL}/api/objective4/model-comparison/")
    data = response.json()
    
    if data['success']:
        print(f"   ✅ Model comparison complete")
        print(f"   🏆 Best Model: {data['best_model']}")
        print(f"   📊 MSE Scores:")
        for model, mse in data['mse_scores'].items():
            print(f"      - {model}: {mse:.4f}")
    else:
        print(f"   ❌ Failed to get model comparison")
        return
    
    # Test 3: Historical data for a country
    test_country = "Albania"
    print(f"\n3️⃣  Testing: Historical data for {test_country}")
    response = requests.get(f"{BASE_URL}/api/objective4/historical/?country={test_country}")
    data = response.json()
    
    if data['success']:
        print(f"   ✅ Found {len(data['data'])} historical records")
        if data['data']:
            latest = data['data'][-1]
            print(f"   📅 Latest year: {latest['Year']}")
            print(f"   ⚡ Access: {latest['Access to electricity (% of population)']}%")
    else:
        print(f"   ❌ Failed to get historical data")
        return
    
    # Test 4: Future predictions
    print(f"\n4️⃣  Testing: Future predictions for {test_country}")
    response = requests.get(f"{BASE_URL}/api/objective4/predictions/?country={test_country}&years=7")
    data = response.json()
    
    if data['success']:
        print(f"   ✅ Generated {len(data['predictions'])} predictions")
        print(f"   🔮 Predictions:")
        for pred in data['predictions'][:3]:
            print(f"      - Year {pred['year']}: {pred['predicted_access']:.2f}%")
    else:
        print(f"   ❌ Failed to get predictions")
        return
    
    # Test 5: Combined data
    print(f"\n5️⃣  Testing: Combined historical + future data")
    response = requests.get(f"{BASE_URL}/api/objective4/combined/?country={test_country}")
    data = response.json()
    
    if data['success']:
        historical = [d for d in data['data'] if d['type'] == 'historical']
        predicted = [d for d in data['data'] if d['type'] == 'predicted']
        print(f"   ✅ Combined data ready")
        print(f"   📊 Historical records: {len(historical)}")
        print(f"   🔮 Predicted records: {len(predicted)}")
    else:
        print(f"   ❌ Failed to get combined data")
        return
    
    print("\n" + "="*70)
    print("✅ All Objective 4 tests passed!")
    print("="*70)
    print("\n📌 Next Steps:")
    print("   1. Open browser: http://127.0.0.1:8000/objective4/")
    print("   2. Select a country from the dropdown")
    print("   3. Click 'Analyze Country'")
    print("   4. View:")
    print("      - Model Comparison (7 algorithms)")
    print("      - Historical electricity access data")
    print("      - Future predictions (next 7 years)")
    print("\n")

if __name__ == "__main__":
    try:
        test_objective4()
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Cannot connect to Django server")
        print("   Please start the server first:")
        print("   cd sustainable_energy")
        print("   python manage.py runserver")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
