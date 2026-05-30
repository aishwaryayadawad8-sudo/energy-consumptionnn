#!/usr/bin/env python3
"""
Add combined historical + future endpoint for Objective 5
"""

# Read views.py
with open('sustainable_energy/dashboard/views.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find where to add the new endpoint (after objective5_countries)
insert_marker = "def objective5_countries(request):"
insert_pos = content.find(insert_marker)

if insert_pos == -1:
    print("❌ Could not find objective5_countries function")
    exit(1)

# Find the end of objective5_countries function
next_def_pos = content.find("\ndef ", insert_pos + 10)

# New endpoint code
new_endpoint = """

def objective5_combined_data(request):
    \"\"\"API: Get combined historical and future data with access level classification\"\"\"
    country = request.GET.get('country', None)
    
    if not country:
        return JsonResponse({
            'success': False,
            'message': 'Country parameter required'
        })
    
    try:
        predictor = Objective5EnergyEquity(CSV_PATH)
        predictor.load_and_clean_data()
        
        # Get historical data
        historical = predictor.get_historical_data(country)
        
        # Get future predictions
        predictions = predictor.predict_future_access(10, country)
        
        if not historical or not predictions:
            return JsonResponse({
                'success': False,
                'message': 'Country not found or no data available'
            })
        
        # Combine data
        combined = []
        
        # Add historical data
        for item in historical:
            combined.append({
                'year': int(item['Year']),
                'access': float(item['Access to electricity (% of population)']),
                'access_level': item['access_level'],
                'type': 'historical'
            })
        
        # Add future predictions
        for item in predictions:
            combined.append({
                'year': int(item['year']),
                'access': float(item['predicted_access']),
                'access_level': item['access_level'],
                'type': 'predicted'
            })
        
        return JsonResponse({
            'success': True,
            'data': combined,
            'country': country
        })
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return JsonResponse({'error': str(e)}, status=500)
"""

# Insert the new endpoint
content = content[:next_def_pos] + new_endpoint + content[next_def_pos:]

# Write back
with open('sustainable_energy/dashboard/views.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Added objective5_combined_data endpoint to views.py")
print("\n📝 New endpoint:")
print("   /api/objective5/combined/?country=X")
print("\n📊 Returns:")
print("   - Historical data with access_level (High/Medium/Low)")
print("   - Future predictions with access_level")
print("   - Combined in single response")
print("\n🔧 Next: Add URL pattern to urls.py")
