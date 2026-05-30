#!/usr/bin/env python3
"""
Update Objective 4 model comparison to use the exact data from the provided code
Sub-objective 4: SDG 7 Monitoring (regression task)
"""

# Read the views.py file
with open('sustainable_energy/dashboard/views.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the objective4_model_comparison function
function_start = content.find('def objective4_model_comparison(request):')
if function_start == -1:
    print("❌ Could not find objective4_model_comparison function")
    exit(1)

# Find the end of the function
function_end = content.find('\ndef ', function_start + 1)
if function_end == -1:
    function_end = len(content)

# Extract the current function
old_function = content[function_start:function_end]

# Create the new function with exact data from the code
new_function = '''def objective4_model_comparison(request):
    """API: Get model comparison MSE scores for SDG 7 Monitoring (Sub-objective 4)"""
    try:
        # Exact MSE scores from Sub-objective 4: SDG 7 Monitoring (regression)
        mse_scores = {
            "Linear Regression": 0.2276,
            "Decision Tree": 0.0251,
            "KNN": 0.0662,
            "XGBoost": 0.0142,
            "LightGBM": 0.0160,
            "CatBoost": 0.0096,  # Best model (lowest MSE)
            "Random Forest": 0.0120
        }
        
        # Best model is the one with lowest MSE (regression task)
        best_model = min(mse_scores, key=mse_scores.get)
        best_mse = mse_scores[best_model]
        
        return JsonResponse({
            'success': True,
            'mse_scores': mse_scores,
            'best_model': best_model,
            'best_mse': best_mse,
            'task_type': 'regression',
            'metric': 'MSE',
            'sub_objective': 4,
            'name': 'SDG 7 Monitoring'
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

'''

# Replace the function
content = content[:function_start] + new_function + content[function_end:]

# Write back the file
with open('sustainable_energy/dashboard/views.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Updated objective4_model_comparison function with exact data!")
print("\n📊 Model Comparison Data (Sub-objective 4: SDG 7 Monitoring):")
print("   - Linear Regression: MSE = 0.2276")
print("   - Decision Tree: MSE = 0.0251")
print("   - KNN: MSE = 0.0662")
print("   - XGBoost: MSE = 0.0142")
print("   - LightGBM: MSE = 0.0160")
print("   - CatBoost: MSE = 0.0096 ⭐ (Best Model)")
print("   - Random Forest: MSE = 0.0120")

print("\n🎯 Chart Features:")
print("   - Type: Bar chart")
print("   - Best Model: CatBoost (highlighted in gold)")
print("   - Metric: MSE (Lower is Better)")
print("   - Task: Regression")

print("\n🔄 Next steps:")
print("   1. Restart Django server: python manage.py runserver")
print("   2. Open http://localhost:8000/objective4/")
print("   3. The model comparison chart will auto-load")
print("   4. CatBoost bar will be highlighted in gold")
print("   5. All 7 algorithms will be displayed")

print("\n💡 The chart will show CatBoost as the best model with MSE=0.0096!")