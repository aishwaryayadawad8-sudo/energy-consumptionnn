#!/usr/bin/env python3
"""
Update all objectives to use the exact model comparison results from the provided code
"""

def update_all_objectives_with_exact_results():
    views_path = "sustainable_energy/dashboard/views.py"
    
    print("🔧 Updating all objectives with exact model comparison results...")
    
    # Exact results from the provided code
    exact_results = {
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
    
    # Define task types for each objective
    task_types = {
        1: "regression",
        2: "regression", 
        3: "classification",
        4: "regression",
        5: "regression",
        6: "classification",
        7: "regression",
        8: "regression"
    }
    
    objective_names = {
        1: "Energy Consumption Prediction",
        2: "CO₂ Emission Forecasting",
        3: "Energy Access Classification", 
        4: "SDG-7 Progress Monitoring",
        5: "Energy Equity Analysis",
        6: "Efficiency Optimization Identification",
        7: "Renewable Energy Potential Assessment",
        8: "Sustainable Investment Strategy Support"
    }
    
    try:
        # Read the current views file
        with open(views_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update each objective's model comparison function
        for obj_num in range(1, 9):
            results = exact_results[obj_num]
            task_type = task_types[obj_num]
            obj_name = objective_names[obj_num]
            
            # Determine best model and metric
            if task_type == "classification":
                best_model = max(results, key=results.get)
                metric = "Accuracy"
            else:
                best_model = min(results, key=results.get)
                metric = "MSE"
            
            best_score = results[best_model]
            
            # Create the new function content
            new_function = f'''def objective{obj_num}_model_comparison(request):
    """API: Get model comparison for {obj_name} - Using exact provided results"""
    try:
        # Exact results from provided code for Objective {obj_num}
        results = {results}
        
        # For {task_type} task, best model has {"highest" if task_type == "classification" else "lowest"} {metric}
        best_model = {"max" if task_type == "classification" else "min"}(results, key=results.get)
        best_score = results[best_model]
        
        return JsonResponse({{
            'success': True,
            'objective_name': '{obj_name}',
            'task_type': '{task_type}',
            'metric': '{metric}',
            '{"accuracy_scores" if task_type == "classification" else "mse_scores"}': results,
            'best_model': best_model,
            'best_score': best_score
        }})
    except Exception as e:
        return JsonResponse({{'error': str(e)}}, status=500)'''
            
            # Find and replace the existing function
            import re
            pattern = rf'def objective{obj_num}_model_comparison\(request\):.*?(?=def|\Z)'
            
            if re.search(pattern, content, re.DOTALL):
                content = re.sub(pattern, new_function + '\n\n', content, flags=re.DOTALL)
                print(f"✅ Updated Objective {obj_num} model comparison")
            else:
                print(f"⚠️  Could not find Objective {obj_num} model comparison function")
        
        # Write back the updated content
        with open(views_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ All objectives updated with exact model comparison results!")
        print("📝 Summary:")
        for obj_num in range(1, 9):
            results = exact_results[obj_num]
            task_type = task_types[obj_num]
            if task_type == "classification":
                best_model = max(results, key=results.get)
                metric = "Accuracy"
            else:
                best_model = min(results, key=results.get)
                metric = "MSE"
            best_score = results[best_model]
            print(f"   Objective {obj_num}: {best_model} ({metric}={best_score:.4f})")
        
        print("🔄 Please restart Django server to apply changes")
        
    except FileNotFoundError:
        print(f"❌ Views file not found: {views_path}")
    except Exception as e:
        print(f"❌ Error updating views: {e}")

if __name__ == "__main__":
    update_all_objectives_with_exact_results()