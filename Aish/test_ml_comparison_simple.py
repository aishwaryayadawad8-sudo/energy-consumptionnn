#!/usr/bin/env python3
"""
Simple test to verify ML comparison data structure
"""

def test_ml_comparison_data():
    """Test the ML comparison data structure"""
    
    print("🧪 Testing ML Comparison Data Structure")
    print("="*50)
    
    # This is the exact data structure from your code
    results = {
        1: {
            "Linear Regression": 0.5403,
            "Decision Tree": 0.0126,
            "KNN": 0.0284,
            "XGBoost": 0.0088,
            "LightGBM": 0.0176,
            "CatBoost": 0.0122,
            "Random Forest": 0.0120
        },
        2: {
            "Linear Regression": 0.0370,
            "Decision Tree": 0.0085,
            "KNN": 0.0089,
            "XGBoost": 0.0048,
            "LightGBM": 0.0349,
            "CatBoost": 0.0072,
            "Random Forest": 0.0074
        },
        3: {
            "Logistic Regression": 0.9425,
            "Decision Tree": 0.9562,
            "KNN": 0.9671,
            "XGBoost": 0.9781,
            "LightGBM": 0.9767,
            "CatBoost": 0.9808,
            "Random Forest": 0.9767
        },
        4: {
            "Linear Regression": 0.2276,
            "Decision Tree": 0.0251,
            "KNN": 0.0662,
            "XGBoost": 0.0142,
            "LightGBM": 0.0160,
            "CatBoost": 0.0096,
            "Random Forest": 0.0120
        },
        5: {
            "Linear Regression": 0.1902,
            "Decision Tree": 0.0209,
            "KNN": 0.0105,
            "XGBoost": 0.0078,
            "LightGBM": 0.0066,
            "CatBoost": 0.0047,
            "Random Forest": 0.0062
        },
        6: {
            "Logistic Regression": 0.8808,
            "Decision Tree": 0.9767,
            "KNN": 0.9671,
            "XGBoost": 0.9781,
            "LightGBM": 0.9808,
            "CatBoost": 0.9863,
            "Random Forest": 0.9877
        },
        7: {
            "Linear Regression": 0.5403,
            "Decision Tree": 0.0126,
            "KNN": 0.0284,
            "XGBoost": 0.0088,
            "LightGBM": 0.0176,
            "CatBoost": 0.0122,
            "Random Forest": 0.0120
        },
        8: {
            "Linear Regression": 0.1902,
            "Decision Tree": 0.0209,
            "KNN": 0.0105,
            "XGBoost": 0.0078,
            "LightGBM": 0.0066,
            "CatBoost": 0.0047,
            "Random Forest": 0.0062
        }
    }
    
    objectives = [
        {"sub_no": 1, "name": "Predict Energy Consumption", "task": "regression"},
        {"sub_no": 2, "name": "CO2 Emission Forecasting", "task": "regression"},
        {"sub_no": 3, "name": "Energy Access Classification", "task": "classification"},
        {"sub_no": 4, "name": "SDG 7 Monitoring", "task": "regression"},
        {"sub_no": 5, "name": "Energy Equity Analysis", "task": "regression"},
        {"sub_no": 6, "name": "Efficiency Optimization", "task": "classification"},
        {"sub_no": 7, "name": "Renewable Energy Potential", "task": "regression"},
        {"sub_no": 8, "name": "Investment Strategies", "task": "regression"}
    ]
    
    print(f"📊 Total Objectives: {len(objectives)}")
    print(f"📈 Total Result Sets: {len(results)}")
    
    # Check each objective
    print("\n🔍 Checking Model Coverage:")
    
    for obj in objectives:
        sub_no = obj["sub_no"]
        name = obj["name"]
        task = obj["task"]
        
        if sub_no in results:
            models = list(results[sub_no].keys())
            print(f"\n📋 Objective {sub_no}: {name} ({task})")
            print(f"   Models ({len(models)}): {', '.join(models)}")
            
            # Find best model
            scores = results[sub_no]
            if task == "classification":
                best_model = max(scores, key=scores.get)
                best_score = scores[best_model]
                metric = "Accuracy"
            else:
                best_model = min(scores, key=scores.get)
                best_score = scores[best_model]
                metric = "MSE"
            
            print(f"   🏆 Best: {best_model} ({metric}={best_score:.4f})")
        else:
            print(f"❌ Missing results for Objective {sub_no}")
    
    # Check for consistency
    print("\n🔧 Data Consistency Check:")
    
    # Check if all objectives have same number of models
    model_counts = [len(results[i]) for i in range(1, 9)]
    if len(set(model_counts)) == 1:
        print(f"✅ All objectives have {model_counts[0]} models")
    else:
        print(f"⚠️  Inconsistent model counts: {model_counts}")
    
    # Check for classification vs regression models
    print("\n📊 Model Type Check:")
    for obj in objectives:
        sub_no = obj["sub_no"]
        task = obj["task"]
        models = list(results[sub_no].keys())
        
        if task == "classification":
            if "Logistic Regression" in models:
                print(f"✅ Obj {sub_no}: Has Logistic Regression for classification")
            else:
                print(f"⚠️  Obj {sub_no}: Missing Logistic Regression for classification")
        else:
            if "Linear Regression" in models:
                print(f"✅ Obj {sub_no}: Has Linear Regression for regression")
            else:
                print(f"⚠️  Obj {sub_no}: Missing Linear Regression for regression")
    
    print("\n🎯 Summary:")
    print("- 8 objectives defined")
    print("- 7 ML models per objective")
    print("- 2 classification tasks (Obj 3, 6)")
    print("- 6 regression tasks (Obj 1, 2, 4, 5, 7, 8)")
    print("- Data structure is ready for web display")
    
    print("\n🚀 Next Steps:")
    print("1. Start Django server: python manage.py runserver")
    print("2. Visit: http://127.0.0.1:8000/comprehensive-comparison/")
    print("3. Check if all 7 models appear in each chart")
    print("4. Verify best models are highlighted in gold")

if __name__ == "__main__":
    test_ml_comparison_data()