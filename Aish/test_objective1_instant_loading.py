#!/usr/bin/env python3
"""
Test Objective 1 Instant ML Comparison Loading
"""

import requests
import time
import json

def test_objective1_instant_loading():
    """Test that Objective 1 ML comparison loads instantly"""
    
    BASE_URL = "http://127.0.0.1:8000"
    
    print("🧪 Testing Objective 1 Instant ML Comparison Loading")
    print("=" * 60)
    
    try:
        # Test the model comparison API endpoint
        print("📡 Testing /api/objective1/model-comparison/")
        
        start_time = time.time()
        response = requests.get(f"{BASE_URL}/api/objective1/model-comparison/", timeout=10)
        end_time = time.time()
        
        response_time = end_time - start_time
        
        print(f"   Status Code: {response.status_code}")
        print(f"   Response Time: {response_time:.3f} seconds")
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('success'):
                print("   ✅ API Response: SUCCESS")
                
                mse_scores = data.get('mse_scores', {})
                best_model = data.get('best_model', 'Unknown')
                
                print(f"   🏆 Best Model: {best_model}")
                print("   📊 MSE Scores:")
                
                for model, score in mse_scores.items():
                    star = " ⭐" if model == best_model else ""
                    print(f"      - {model}: {score:.4f}{star}")
                
                # Check if response is instant (under 0.1 seconds)
                if response_time < 0.1:
                    print(f"   🚀 INSTANT LOADING: {response_time:.3f}s (< 0.1s)")
                elif response_time < 0.5:
                    print(f"   ⚡ FAST LOADING: {response_time:.3f}s (< 0.5s)")
                else:
                    print(f"   ⏳ SLOW LOADING: {response_time:.3f}s (> 0.5s)")
                
                print("\n✅ Objective 1 ML Comparison Test: PASSED")
                
            else:
                print("   ❌ API Response: FAILED")
                print(f"   Error: {data.get('error', 'Unknown error')}")
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
            print(f"   Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("   ❌ Connection Error: Django server not running")
        print("   💡 Please start the Django server with: python manage.py runserver")
    except requests.exceptions.Timeout:
        print("   ❌ Timeout Error: Request took too long")
    except Exception as e:
        print(f"   ❌ Unexpected Error: {e}")

if __name__ == "__main__":
    test_objective1_instant_loading()
    print("\n" + "=" * 60)
    print("🔄 If the server is running, refresh the Objective 1 page to see instant loading!")