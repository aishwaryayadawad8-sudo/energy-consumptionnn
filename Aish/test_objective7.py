"""
Test script for Objective 7: Renewable Energy Investment Potential
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_objective7():
    print("=" * 60)
    print("Testing Objective 7: Renewable Energy Investment Potential")
    print("=" * 60)
    
    # Test 1: Model Comparison
    print("\n1. Testing Model Comparison API...")
    response = requests.get(f"{BASE_URL}/api/objective7/model-comparison/")
    if response.status_code == 200:
        data = response.json()
        print("✓ Model Comparison API working!")
        print(f"  Best Model: {data.get('best_model')}")
        print(f"  MSE Scores: {json.dumps(data.get('mse_scores'), indent=2)}")
    else:
        print(f"✗ Model Comparison API failed: {response.status_code}")
    
    # Test 2: Countries List
    print("\n2. Testing Countries API...")
    response = requests.get(f"{BASE_URL}/api/objective7/countries/")
    if response.status_code == 200:
        data = response.json()
        countries = data.get('countries', [])
        print(f"✓ Countries API working! Found {len(countries)} countries")
        print(f"  Sample countries: {countries[:5]}")
    else:
        print(f"✗ Countries API failed: {response.status_code}")
    
    # Test 3: Historical Data
    print("\n3. Testing Historical Data API...")
    test_country = "United States"
    response = requests.get(f"{BASE_URL}/api/objective7/historical/?country={test_country}")
    if response.status_code == 200:
        data = response.json()
        historical = data.get('data', [])
        print(f"✓ Historical Data API working!")
        print(f"  Country: {test_country}")
        print(f"  Data points: {len(historical)}")
        if historical:
            print(f"  Sample: Year {historical[0]['Year']}, Capacity: {historical[0]['Renewable_Capacity']:.2f}")
    else:
        print(f"✗ Historical Data API failed: {response.status_code}")
    
    # Test 4: Future Predictions
    print("\n4. Testing Future Predictions API...")
    response = requests.get(f"{BASE_URL}/api/objective7/predictions/?country={test_country}&years=5")
    if response.status_code == 200:
        data = response.json()
        predictions = data.get('predictions', [])
        print(f"✓ Future Predictions API working!")
        print(f"  Country: {test_country}")
        print(f"  Predictions: {len(predictions)}")
        if predictions:
            print(f"  Sample: Year {predictions[0]['year']}, Potential: {predictions[0]['predicted_potential_level']}")
    else:
        print(f"✗ Future Predictions API failed: {response.status_code}")
    
    # Test 5: Combined Data
    print("\n5. Testing Combined Data API...")
    response = requests.get(f"{BASE_URL}/api/objective7/combined/?country={test_country}")
    if response.status_code == 200:
        data = response.json()
        combined = data.get('data', [])
        print(f"✓ Combined Data API working!")
        print(f"  Total data points: {len(combined)}")
        historical_count = sum(1 for d in combined if d.get('type') == 'historical')
        predicted_count = sum(1 for d in combined if d.get('type') == 'predicted')
        print(f"  Historical: {historical_count}, Predicted: {predicted_count}")
    else:
        print(f"✗ Combined Data API failed: {response.status_code}")
    
    # Test 6: Dashboard Page
    print("\n6. Testing Dashboard Page...")
    response = requests.get(f"{BASE_URL}/objective7/")
    if response.status_code == 200:
        print("✓ Dashboard page accessible!")
        print(f"  URL: {BASE_URL}/objective7/")
    else:
        print(f"✗ Dashboard page failed: {response.status_code}")
    
    print("\n" + "=" * 60)
    print("Objective 7 Testing Complete!")
    print("=" * 60)
    print(f"\n🌐 Access Objective 7 at: {BASE_URL}/objective7/")
    print(f"🏠 Return to selector at: {BASE_URL}/")

if __name__ == "__main__":
    try:
        test_objective7()
    except Exception as e:
        print(f"\n❌ Error during testing: {str(e)}")
        import traceback
        traceback.print_exc()
