"""
Test the predictions API to see if it's returning data
"""
import sys
import os
import django

# Setup Django
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sustainable_energy'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sustainable_energy.settings')
django.setup()

from ml_models.energy_consumption_predictor import EnergyConsumptionPredictor

# Test with a sample country
CSV_PATH = 'global-data-on-sustainable-energy.csv'

print("Testing Energy Consumption Predictor...")
print("=" * 60)

try:
    predictor = EnergyConsumptionPredictor(CSV_PATH)
    predictor.load_and_clean_data()
    
    # Test getting countries
    countries = predictor.get_all_countries()
    print(f"\n✅ Found {len(countries)} countries")
    print(f"Sample countries: {countries[:5]}")
    
    # Test with a specific country
    test_country = "India"
    print(f"\n📊 Testing predictions for: {test_country}")
    
    # Get historical data
    historical = predictor.get_historical_data(test_country)
    print(f"✅ Historical data points: {len(historical)}")
    if historical:
        print(f"   Sample: {historical[0]}")
    
    # Get predictions
    predictions = predictor.predict_future_consumption(years_ahead=10, country_name=test_country)
    print(f"✅ Prediction data points: {len(predictions) if predictions else 0}")
    if predictions:
        print(f"   Sample: {predictions[0]}")
        print(f"   Years: {[p['year'] for p in predictions[:3]]}")
    else:
        print("   ❌ No predictions returned!")
    
    print("\n" + "=" * 60)
    print("✅ API test completed successfully!")
    
except Exception as e:
    print(f"\n❌ Error: {str(e)}")
    import traceback
    traceback.print_exc()
