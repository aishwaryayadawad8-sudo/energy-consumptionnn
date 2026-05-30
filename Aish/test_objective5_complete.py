"""
Test script for Objective 5: SDG 7 Electricity Access Forecasting
"""

import sys
import os

# Add the sustainable_energy directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sustainable_energy'))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from ml_models.sdg7_forecasting import SDG7Forecasting

def test_objective5():
    print("=" * 60)
    print("Testing Objective 5: SDG 7 Electricity Access Forecasting")
    print("=" * 60)
    
    csv_path = 'global-data-on-sustainable-energy.csv'
    
    # Initialize forecaster
    print("\n1. Initializing forecaster...")
    forecaster = SDG7Forecasting(csv_path)
    
    # Load and clean data
    print("2. Loading and cleaning data...")
    forecaster.load_and_clean_data()
    print(f"   ✓ Loaded {len(forecaster.df)} records")
    print(f"   ✓ SDG7 dataset: {len(forecaster.df_sdg7)} records")
    
    # Train and compare models
    print("\n3. Training and comparing models...")
    mse_scores = forecaster.train_and_compare_models()
    print("   Model MSE Scores:")
    for model, mse in mse_scores.items():
        print(f"   - {model}: {mse:.4f}")
    print(f"   ✓ Best model: {forecaster.best_model_name}")
    
    # Get all countries
    print("\n4. Getting all countries...")
    countries = forecaster.get_all_countries()
    print(f"   ✓ Found {len(countries)} countries")
    print(f"   Sample countries: {countries[:5]}")
    
    # Test with United States
    test_country = 'United States'
    print(f"\n5. Testing with {test_country}...")
    
    # Get historical data
    print(f"   a) Historical data for {test_country}:")
    historical = forecaster.get_historical_data(test_country)
    print(f"      ✓ {len(historical)} historical records")
    if historical:
        latest = historical[-1]
        print(f"      Latest: {latest['Year']} - {latest['Access to electricity (% of population)']}%")
    
    # Get future predictions
    print(f"   b) Future predictions for {test_country}:")
    predictions = forecaster.predict_future_access(7, test_country)
    if predictions:
        print(f"      ✓ {len(predictions)} predictions")
        print(f"      Sample: {predictions[0]['year']} - {predictions[0]['predicted_access']:.1f}%")
        print(f"              {predictions[-1]['year']} - {predictions[-1]['predicted_access']:.1f}%")
    
    # Get combined data
    print(f"   c) Combined historical + future data:")
    combined = forecaster.get_combined_historical_future(test_country)
    print(f"      ✓ {len(combined)} total records")
    hist_count = len([d for d in combined if d['type'] == 'historical'])
    pred_count = len([d for d in combined if d['type'] == 'predicted'])
    print(f"      Historical: {hist_count}, Predicted: {pred_count}")
    
    # Get country statistics
    print(f"\n6. Testing country statistics for {test_country}...")
    stats = forecaster.get_country_statistics(test_country)
    if stats:
        print(f"   ✓ Latest access: {stats['latest_access']:.1f}% ({stats['latest_year']})")
        print(f"   ✓ Improvement: {stats['improvement']:.1f}% over {stats['years_tracked']} years")
        print(f"   ✓ Data points: {stats['data_points']}")
    
    # Get global statistics
    print("\n7. Testing global statistics...")
    global_stats = forecaster.get_global_statistics()
    print(f"   ✓ Global average: {global_stats['global_average']:.1f}%")
    print(f"   ✓ Countries tracked: {global_stats['countries_tracked']}")
    print(f"   ✓ Countries at 100%: {global_stats['countries_100_percent']}")
    print(f"   ✓ Countries below 50%: {global_stats['countries_below_50']}")
    
    print("\n" + "=" * 60)
    print("✓ All Objective 5 tests completed successfully!")
    print("=" * 60)
    
    return True

if __name__ == '__main__':
    try:
        test_objective5()
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
