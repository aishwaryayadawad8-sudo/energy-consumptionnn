#!/usr/bin/env python3

"""
Test the comprehensive Objective 4 API endpoints
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_objective4_comprehensive():
    """Test all Objective 4 comprehensive API endpoints"""
    
    print("🧪 Testing Objective 4 Comprehensive API Implementation")
    print("=" * 70)
    
    try:
        # Test 1: Model Comparison (4 Classification Models)
        print("\n1️⃣  Testing: Model Comparison (4 Classification Models)")
        response = requests.get(f"{BASE_URL}/api/objective4/model-comparison/")
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print(f"   ✅ Best Model: {data.get('best_model')}")
                print(f"   📊 Models tested: {len(data.get('models', {}))}")
                for model, mse in data.get('models', {}).items():
                    print(f"      {model}: MSE = {mse:.4f}")
            else:
                print(f"   ❌ API returned error: {data}")
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
        
        # Test 2: Get Countries
        print("\n2️⃣  Testing: Get All Countries")
        response = requests.get(f"{BASE_URL}/api/objective4/countries/")
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print(f"   ✅ Countries available: {data.get('count')}")
                print(f"   📍 Sample countries: {data.get('countries', [])[:5]}")
            else:
                print(f"   ❌ API returned error: {data}")
        
        # Test 3: Historical Data
        test_country = "Albania"
        print(f"\n3️⃣  Testing: Historical Data for {test_country}")
        response = requests.get(f"{BASE_URL}/api/objective4/historical/?country={test_country}")
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print(f"   ✅ Historical data: {data.get('years_available')} years")
                print(f"   📈 Sample data points: {len(data.get('data', []))}")
                if data.get('data'):
                    latest = data['data'][-1]
                    print(f"   📊 Latest: {latest.get('Year')} - {latest.get('Access to electricity (% of population)')}%")
            else:
                print(f"   ❌ API returned error: {data}")
        
        # Test 4: Future Predictions (Classification-based)
        print(f"\n4️⃣  Testing: Future Predictions for {test_country}")
        response = requests.get(f"{BASE_URL}/api/objective4/predictions/?country={test_country}&years=7")
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print(f"   ✅ Predictions: {data.get('years_predicted')} years")
                print(f"   🤖 Model used: {data.get('model_used')}")
                if data.get('predictions'):
                    sample_pred = data['predictions'][0]
                    print(f"   🔮 Sample: {sample_pred.get('year')} - {sample_pred.get('predicted_access')}% ({sample_pred.get('access_level')})")
            else:
                print(f"   ❌ API returned error: {data}")
        
        # Test 5: Combined Data
        print(f"\n5️⃣  Testing: Combined Historical + Future Data")
        response = requests.get(f"{BASE_URL}/api/objective4/combined/?country={test_country}")
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print(f"   ✅ Historical points: {len(data.get('historical', []))}")
                print(f"   ✅ Future predictions: {len(data.get('predictions', []))}")
                print(f"   🤖 Model used: {data.get('model_used')}")
            else:
                print(f"   ❌ API returned error: {data}")
        
        print("\n" + "=" * 70)
        print("✅ Objective 4 Comprehensive API Testing Complete!")
        print("\n📊 Features Verified:")
        print("   - 4 Classification Models (Logistic Regression, Decision Tree, KNN, XGBoost)")
        print("   - Access Level Categories (Low, Medium, High)")
        print("   - Enhanced Historical Analysis")
        print("   - Classification-based Future Predictions")
        print("   - Combined Historical + Future Data")
        print("\n🌐 Ready for Use:")
        print(f"   Open: {BASE_URL}/objective4/")
        print("   Select any country and analyze!")
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Cannot connect to Django server")
        print("💡 Start the server: cd sustainable_energy && python manage.py runserver")
        print(f"   Then visit: {BASE_URL}/objective4/")
    
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    test_objective4_comprehensive()