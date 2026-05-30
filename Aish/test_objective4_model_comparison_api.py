#!/usr/bin/env python3
"""
Test the updated Objective 4 model comparison API
"""

import requests
import json

def test_objective4_model_comparison():
    """Test the Objective 4 model comparison API"""
    print("🔍 Testing Objective 4 Model Comparison API...")
    
    try:
        url = "http://localhost:8000/api/objective4/model-comparison/"
        print(f"📡 Calling: {url}")
        
        response = requests.get(url, timeout=10)
        print(f"📊 Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("📋 Response:")
            print(json.dumps(data, indent=2))
            
            if data.get('success'):
                mse_scores = data.get('mse_scores', {})
                best_model = data.get('best_model')
                best_mse = data.get('best_mse')
                
                print(f"\n✅ API Success!")
                print(f"   Models: {len(mse_scores)}")
                print(f"   Best Model: {best_model}")
                print(f"   Best MSE: {best_mse}")
                
                print(f"\n📊 All Model Scores:")
                for model, mse in mse_scores.items():
                    marker = " ⭐" if model == best_model else ""
                    print(f"   {model}: {mse}{marker}")
                
                # Verify the data matches the expected values
                expected_best = "CatBoost"
                expected_mse = 0.0096
                
                if best_model == expected_best and abs(best_mse - expected_mse) < 0.0001:
                    print(f"\n✅ Data matches expected values!")
                    return True
                else:
                    print(f"\n⚠️  Data doesn't match expected values")
                    print(f"   Expected: {expected_best} with MSE {expected_mse}")
                    print(f"   Got: {best_model} with MSE {best_mse}")
                    return False
            else:
                print(f"❌ API failed: {data.get('error', 'Unknown error')}")
                return False
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("🚀 Testing Objective 4 Model Comparison Update")
    print("=" * 50)
    
    success = test_objective4_model_comparison()
    
    print("\n" + "=" * 50)
    if success:
        print("✅ Model comparison API is working correctly!")
        print("\n🎯 Expected Chart Behavior:")
        print("   - 7 bars showing all algorithms")
        print("   - CatBoost bar highlighted in GOLD")
        print("   - All other bars in blue")
        print("   - Title: 'Model Performance Comparison (Lower is Better)'")
        print("   - Y-axis: MSE Score")
        
        print("\n🔄 Next Steps:")
        print("   1. Restart Django server: python manage.py runserver")
        print("   2. Open http://localhost:8000/objective4/")
        print("   3. The chart should auto-load with CatBoost highlighted")
        print("   4. Verify all 7 algorithms are displayed")
    else:
        print("❌ API needs to be fixed")

if __name__ == "__main__":
    main()