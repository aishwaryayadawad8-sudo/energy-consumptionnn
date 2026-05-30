#!/usr/bin/env python3
"""
Quick test of Objective 5 API endpoints
"""

import requests
import json

base_url = "http://localhost:8000"

def test_api_endpoint(endpoint, description):
    """Test an API endpoint and return the result"""
    try:
        print(f"\n🔍 Testing {description}...")
        print(f"   URL: {base_url}{endpoint}")
        
        response = requests.get(f"{base_url}{endpoint}", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print(f"   ✅ SUCCESS: {description}")
                return True, data
            else:
                print(f"   ❌ FAILED: {description} - API returned success=false")
                print(f"   Error: {data.get('error', 'Unknown error')}")
                return False, data
        else:
            print(f"   ❌ FAILED: {description} - HTTP {response.status_code}")
            return False, None
            
    except requests.exceptions.ConnectionError:
        print(f"   ❌ FAILED: {description} - Server not running")
        return False, None
    except Exception as e:
        print(f"   ❌ FAILED: {description} - {str(e)}")
        return False, None

def main():
    print("🚀 Testing Objective 5 API Endpoints")
    print("=" * 50)
    
    # Test countries endpoint
    success, data = test_api_endpoint("/api/objective5/countries/", "Countries List")
    if success:
        print(f"   📊 Found {len(data.get('countries', []))} countries")
        countries = data.get('countries', [])
        if countries:
            test_country = countries[0]  # Use first country for testing
            print(f"   🎯 Using '{test_country}' for further tests")
            
            # Test predictions endpoint
            success, pred_data = test_api_endpoint(
                f"/api/objective5/predictions/?country={test_country}&years=10", 
                f"Predictions for {test_country}"
            )
            if success:
                predictions = pred_data.get('predictions', [])
                print(f"   📈 Found {len(predictions)} prediction points")
                if predictions:
                    print(f"   📅 Years: {predictions[0]['year']} to {predictions[-1]['year']}")
                    print(f"   📊 Sample prediction: {predictions[0]['predicted_access']:.1f}%")
            
            # Test historical endpoint
            success, hist_data = test_api_endpoint(
                f"/api/objective5/historical/?country={test_country}", 
                f"Historical data for {test_country}"
            )
            if success:
                historical = hist_data.get('data', [])
                print(f"   📈 Found {len(historical)} historical points")
    
    # Test model comparison
    success, model_data = test_api_endpoint("/api/objective5/model-comparison/", "Model Comparison")
    if success:
        models = model_data.get('mse_scores', {})
        print(f"   🏆 Best model: {model_data.get('best_model', 'Unknown')}")
        print(f"   📊 Models tested: {list(models.keys())}")
    
    print("\n" + "=" * 50)
    print("✅ API testing complete!")
    print("\n💡 If all tests passed, the predictions chart should now work.")
    print("   Open http://localhost:8000/objective5/ to test the frontend.")

if __name__ == "__main__":
    main()