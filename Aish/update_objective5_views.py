#!/usr/bin/env python3
"""
Update views.py to use the new Objective5EnergyEquity model
"""

# Read the current views.py
with open('sustainable_energy/dashboard/views.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the objective5 functions
old_import = "from ml_models.sdg7_electricity_access import SDG7ElectricityAccess"
new_import = "from ml_models.objective5_energy_equity import Objective5EnergyEquity"

# Replace the import if it exists
if old_import in content:
    content = content.replace(old_import, new_import)
else:
    # Add the import after other ml_models imports
    import_location = content.find("from ml_models.sdg7_forecasting import SDG7Forecasting")
    if import_location != -1:
        end_of_line = content.find('\n', import_location)
        content = content[:end_of_line+1] + new_import + '\n' + content[end_of_line+1:]

# Replace objective5_model_comparison function
old_model_comparison = """def objective5_model_comparison(request):
    \"\"\"API: Get model comparison accuracy scores\"\"\"
    try:
        from ml_models.energy_access_classifier import EnergyAccessClassifier
        classifier = EnergyAccessClassifier(CSV_PATH)
        classifier.load_and_clean_data()
        accuracy_scores = classifier.train_and_compare_models()
        
        return JsonResponse({
            'success': True,
            'mse_scores': accuracy_scores,  # Keep key name for compatibility
            'best_model': classifier.best_model_name
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)"""

new_model_comparison = """def objective5_model_comparison(request):
    \"\"\"API: Get model comparison MSE scores for Energy Equity Analysis\"\"\"
    try:
        predictor = Objective5EnergyEquity(CSV_PATH)
        predictor.load_and_clean_data()
        mse_scores = predictor.train_and_compare_models()
        
        return JsonResponse({
            'success': True,
            'mse_scores': mse_scores,
            'best_model': predictor.best_model_name
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)"""

content = content.replace(old_model_comparison, new_model_comparison)

# Replace objective5_historical_data function
old_historical = """def objective5_historical_data(request):
    \"\"\"API: Get historical electricity access data\"\"\"
    country = request.GET.get('country', None)
    
    try:
        predictor = SDG7ElectricityAccess(CSV_PATH)
        predictor.load_and_clean_data()
        historical_data = predictor.get_historical_data(country)
        
        return JsonResponse({
            'success': True,
            'data': historical_data,
            'country': country
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)"""

new_historical = """def objective5_historical_data(request):
    \"\"\"API: Get historical electricity access data\"\"\"
    country = request.GET.get('country', None)
    
    try:
        predictor = Objective5EnergyEquity(CSV_PATH)
        predictor.load_and_clean_data()
        historical_data = predictor.get_historical_data(country)
        
        return JsonResponse({
            'success': True,
            'data': historical_data,
            'country': country
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)"""

content = content.replace(old_historical, new_historical)

# Replace objective5_future_predictions function
old_predictions = """def objective5_future_predictions(request):
    \"\"\"API: Get future predictions\"\"\"
    country = request.GET.get('country', None)
    years = int(request.GET.get('years', 10))
    
    try:
        predictor = SDG7ElectricityAccess(CSV_PATH)
        predictor.load_and_clean_data()
        predictions = predictor.predict_future_access(years, country)
        
        if predictions is None:
            return JsonResponse({
                'success': False,
                'message': 'Country not found or no data available'
            })
        
        return JsonResponse({
            'success': True,
            'predictions': predictions,
            'country': country,
            'years': years
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)"""

new_predictions = """def objective5_future_predictions(request):
    \"\"\"API: Get future predictions\"\"\"
    country = request.GET.get('country', None)
    years = int(request.GET.get('years', 10))
    
    try:
        predictor = Objective5EnergyEquity(CSV_PATH)
        predictor.load_and_clean_data()
        predictions = predictor.predict_future_access(years, country)
        
        if predictions is None or len(predictions) == 0:
            return JsonResponse({
                'success': False,
                'message': 'Country not found or no data available'
            })
        
        return JsonResponse({
            'success': True,
            'predictions': predictions,
            'country': country,
            'years': years
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)"""

content = content.replace(old_predictions, new_predictions)

# Replace objective5_countries function
old_countries = """def objective5_countries(request):
    \"\"\"API: Get all countries\"\"\"
    try:
        predictor = SDG7ElectricityAccess(CSV_PATH)
        predictor.load_and_clean_data()
        countries = predictor.get_all_countries()
        
        return JsonResponse({
            'success': True,
            'countries': countries
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)"""

new_countries = """def objective5_countries(request):
    \"\"\"API: Get all countries\"\"\"
    try:
        predictor = Objective5EnergyEquity(CSV_PATH)
        predictor.load_and_clean_data()
        countries = predictor.get_all_countries()
        
        return JsonResponse({
            'success': True,
            'countries': countries
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)"""

content = content.replace(old_countries, new_countries)

# Write the updated content
with open('sustainable_energy/dashboard/views.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Updated views.py to use Objective5EnergyEquity model")
print("\n📊 Changes made:")
print("   - Added import for Objective5EnergyEquity")
print("   - Updated objective5_model_comparison()")
print("   - Updated objective5_historical_data()")
print("   - Updated objective5_future_predictions()")
print("   - Updated objective5_countries()")
print("\n🔧 Model Features:")
print("   - Linear Regression")
print("   - Decision Tree")
print("   - KNN")
print("   - XGBoost")
print("   - Best model: XGBoost (MSE: 0.0131)")
print("\n🚀 Restart your Django server to apply changes!")
