#!/usr/bin/env python3
"""
Quick API Test for Objective 6 Model Comparison
"""
import requests
import json

def test_objective6_api():
    """Test Objective 6 API endpoints"""
    base_url = "http://127.0.0.1:8000"
    
    print("🚀 Testing Objective 6 API Endpoints...")
    print("=" * 50)
    
    # Test model comparison API
    print("\n📊 Testing Model Comparison API...")
    try:
        response = requests.get(f"{base_url}/api/objective6/model-comparison/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Model Comparison API: SUCCESS")
            print(f"   Best Model: {data.get('best_model', 'N/A')}")
            print(f"   Best Score: {data.get('best_score', 'N/A')}")
            print(f"   Task Type: {data.get('task_type', 'N/A')}")
            print(f"   Models Available: {len(data.get('mse_scores', {}))}")
            
            # Print all model scores
            if 'mse_scores' in data:
                print("\n   📈 All Model Scores:")
                for model, score in data['mse_scores'].items():
                    marker = "⭐" if model == data.get('best_model') else "  "
                    print(f"   {marker} {model}: {score:.4f}")
        else:
            print(f"❌ Model Comparison API: FAILED (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Model Comparison API: ERROR - {e}")
    
    # Test countries API
    print("\n🌍 Testing Countries API...")
    try:
        response = requests.get(f"{base_url}/api/objective6/countries/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Countries API: SUCCESS")
            print(f"   Countries Available: {len(data.get('countries', []))}")
            print(f"   Sample Countries: {data.get('countries', [])[:5]}")
        else:
            print(f"❌ Countries API: FAILED (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Countries API: ERROR - {e}")
    
    # Test historical data API
    print("\n📊 Testing Historical Data API...")
    try:
        response = requests.get(f"{base_url}/api/objective6/historical/?country=United States", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Historical Data API: SUCCESS")
            print(f"   Data Points: {len(data.get('data', []))}")
            print(f"   Country: {data.get('country', 'N/A')}")
        else:
            print(f"❌ Historical Data API: FAILED (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Historical Data API: ERROR - {e}")
    
    print("\n" + "=" * 50)
    print("🏁 API Testing Complete!")

if __name__ == "__main__":
    test_objective6_api()