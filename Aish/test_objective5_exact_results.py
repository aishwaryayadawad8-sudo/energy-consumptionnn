#!/usr/bin/env python3
"""
Test Objective 5 model comparison to verify it uses exact results from provided code
"""

import requests
import json

def test_objective5_exact_results():
    print("🔍 Testing Objective 5 Model Comparison with Exact Results")
    print("=" * 60)
    
    # Expected results from your provided code for Objective 5
    expected_results = {
        "Linear Regression": 0.1902,
        "Decision Tree": 0.0209,
        "KNN": 0.0105,
        "XGBoost": 0.0078,
        "LightGBM": 0.0066,
        "CatBoost": 0.0047,
        "Random Forest": 0.0062
    }
    
    # Expected best model (lowest MSE for regression)
    expected_best_model = "CatBoost"
    expected_best_score = 0.0047
    
    try:
        # Test the API endpoint
        url = "http://127.0.0.1:8000/api/objective5/model-comparison/"
        print(f"📡 Testing API: {url}")
        
        response = requests.get(url)
        print(f"📊 Response Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API Response: Success")
            
            # Verify the structure
            if data.get('success'):
                print(f"✅ Success Flag: True")
                
                # Check objective name
                obj_name = data.get('objective_name')
                print(f"📝 Objective Name: {obj_name}")
                
                # Check task type
                task_type = data.get('task_type')
                print(f"📝 Task Type: {task_type}")
                
                # Check metric
                metric = data.get('metric')
                print(f"📝 Metric: {metric}")
                
                # Check model results
                mse_scores = data.get('mse_scores', {})
                print(f"📊 Model Results:")
                
                all_correct = True
                for model, expected_score in expected_results.items():
                    actual_score = mse_scores.get(model)
                    if actual_score == expected_score:
                        print(f"   ✅ {model}: {actual_score} (Expected: {expected_score})")
                    else:
                        print(f"   ❌ {model}: {actual_score} (Expected: {expected_score})")
                        all_correct = False
                
                # Check best model
                best_model = data.get('best_model')
                best_score = data.get('best_score')
                
                if best_model == expected_best_model and best_score == expected_best_score:
                    print(f"✅ Best Model: {best_model} (MSE: {best_score})")
                else:
                    print(f"❌ Best Model: {best_model} (MSE: {best_score})")
                    print(f"   Expected: {expected_best_model} (MSE: {expected_best_score})")
                    all_correct = False
                
                if all_correct:
                    print("\n🎉 SUCCESS: All results match your provided code exactly!")
                    print("✅ Objective 5 is correctly implemented")
                else:
                    print("\n❌ MISMATCH: Some results don't match your provided code")
                    
            else:
                print(f"❌ API returned success=false: {data}")
                
        else:
            print(f"❌ API Error: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Django server not running")
        print("Please start the server with: python manage.py runserver")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print("🔧 NEXT STEPS:")
    print("1. If successful, visit: http://127.0.0.1:8000/objective5/")
    print("2. Verify the chart loads instantly with CatBoost highlighted")
    print("3. Check that all 7 models show the exact values above")

if __name__ == "__main__":
    test_objective5_exact_results()