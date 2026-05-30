#!/usr/bin/env python3

"""
Update Objective 4 views.py to use the comprehensive ML implementation
"""

import os

def update_objective4_views():
    """Update views.py with comprehensive Objective 4 implementation"""
    
    views_path = "sustainable_energy/dashboard/views.py"
    
    # Read current views.py
    with open(views_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add import for the new comprehensive ML class
    import_line = "from ml_models.objective4_comprehensive_ml import Objective4ComprehensiveML"
    
    if import_line not in content:
        # Find the imports section and add our import
        import_section_end = content.find("CSV_PATH = ")
        if import_section_end != -1:
            content = content[:import_section_end] + import_line + "\n" + content[import_section_end:]
    
    # Update the objective4_historical_data function
    old_historical_function = '''def objective4_historical_data(request):
    """API: Get historical electricity access data"""
    country = request.GET.get('country', None)
    
    try:
        forecaster = SDG7Forecasting(CSV_PATH)
        forecaster.load_and_clean_data()
        historical_data = forecaster.get_historical_data(country)
        
        return JsonResponse({
            'success': True,
            'data': historical_data,
            'country': country
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)'''
    
    new_historical_function = '''def objective4_historical_data(request):
    """API: Get historical electricity access data using comprehensive ML"""
    country = request.GET.get('country', None)
    
    try:
        ml = Objective4ComprehensiveML(CSV_PATH)
        result = ml.get_historical_data(country)
        
        if result['success']:
            return JsonResponse(result)
        else:
            return JsonResponse(result, status=400)
            
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)'''
    
    # Update the objective4_future_predictions function
    old_predictions_function = '''def objective4_future_predictions(request):
    """API: Get future predictions"""
    country = request.GET.get('country', None)
    years = int(request.GET.get('years', 7))
    
    try:
        forecaster = SDG7Forecasting(CSV_PATH)
        forecaster.load_and_clean_data()
        predictions = forecaster.predict_future_access(years, country)
        
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
        return JsonResponse({'error': str(e)}, status=500)'''
    
    new_predictions_function = '''def objective4_future_predictions(request):
    """API: Get future predictions using comprehensive ML classification"""
    country = request.GET.get('country', None)
    years = int(request.GET.get('years', 7))
    
    try:
        ml = Objective4ComprehensiveML(CSV_PATH)
        result = ml.predict_future_access(country, years)
        
        if result['success']:
            return JsonResponse(result)
        else:
            return JsonResponse(result, status=400)
            
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)'''
    
    # Update the objective4_countries function
    old_countries_function = '''def objective4_countries(request):
    """API: Get all countries"""
    try:
        forecaster = SDG7Forecasting(CSV_PATH)
        forecaster.load_and_clean_data()
        countries = forecaster.get_countries()
        
        return JsonResponse({
            'success': True,
            'countries': countries
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)'''
    
    new_countries_function = '''def objective4_countries(request):
    """API: Get all countries using comprehensive ML"""
    try:
        ml = Objective4ComprehensiveML(CSV_PATH)
        result = ml.get_countries()
        
        return JsonResponse(result)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)'''
    
    # Update the objective4_model_comparison function to use comprehensive ML
    old_model_function_start = content.find('def objective4_model_comparison(request):')
    old_model_function_end = content.find('def objective4_historical_data(request):')
    
    new_model_function = '''def objective4_model_comparison(request):
    """API: Get comprehensive model comparison using 4 classification algorithms"""
    try:
        ml = Objective4ComprehensiveML(CSV_PATH)
        result = ml.get_model_comparison()
        
        return JsonResponse(result)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

'''
    
    # Add new comprehensive stats function
    new_stats_function = '''def objective4_comprehensive_stats(request):
    """API: Get comprehensive country statistics"""
    country = request.GET.get('country', None)
    
    try:
        ml = Objective4ComprehensiveML(CSV_PATH)
        result = ml.get_country_stats(country)
        
        if result['success']:
            return JsonResponse(result)
        else:
            return JsonResponse(result, status=400)
            
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def objective4_combined_comprehensive(request):
    """API: Get combined historical and future data using comprehensive ML"""
    country = request.GET.get('country', None)
    
    try:
        ml = Objective4ComprehensiveML(CSV_PATH)
        result = ml.get_combined_data(country)
        
        if result['success']:
            return JsonResponse(result)
        else:
            return JsonResponse(result, status=400)
            
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

'''
    
    # Replace functions
    if old_model_function_start != -1 and old_model_function_end != -1:
        content = content[:old_model_function_start] + new_model_function + content[old_model_function_end:]
    
    content = content.replace(old_historical_function, new_historical_function)
    content = content.replace(old_predictions_function, new_predictions_function)
    content = content.replace(old_countries_function, new_countries_function)
    
    # Add new functions before the OBJECTIVE 5 section
    objective5_start = content.find('# ===== OBJECTIVE 5:')
    if objective5_start != -1:
        content = content[:objective5_start] + new_stats_function + content[objective5_start:]
    
    # Write updated views.py
    with open(views_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Updated Objective 4 views.py with comprehensive ML implementation!")
    print("\n📊 New Features Added:")
    print("   - 4 Classification Models: Logistic Regression, Decision Tree, KNN, XGBoost")
    print("   - Access Level Categories: Low (0-50%), Medium (50-90%), High (90-100%)")
    print("   - Enhanced Historical Data Analysis")
    print("   - Intelligent Future Predictions based on classification")
    print("   - Comprehensive Country Statistics")
    print("   - Combined Historical + Future Data")
    print("\n🔄 API Endpoints Updated:")
    print("   - /api/objective4/model-comparison/ - Now uses 4 classification models")
    print("   - /api/objective4/historical/ - Enhanced historical analysis")
    print("   - /api/objective4/predictions/ - Classification-based predictions")
    print("   - /api/objective4/countries/ - Improved country listing")
    print("   - NEW: /api/objective4/stats/ - Comprehensive country stats")

if __name__ == "__main__":
    update_objective4_views()