#!/usr/bin/env python3
"""
Test Objective 7 API
"""
import requests

def test_objective7_api():
    """Test Objective 7 API endpoints"""
    base_url = "http://127.0.0.1:8000"
    
    print("🚀 Testing Objective 7 API...")
    print("=" * 50)
    
    # Test model comparison API
    print("\n📊 Testing Model Comparison API...")
    try:
        response = requests.get(f"{base_url}/api/objective7/model-comparison/", timeout=5)
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
    
    print("\n" + "=" * 50)
    print("🏁 API Testing Complete!")

if __name__ == "__main__":
    test_objective7_api()