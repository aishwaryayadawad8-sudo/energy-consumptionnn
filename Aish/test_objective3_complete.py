"""
Test script for Objective 4: SDG 7 Electricity Access Classification
"""

import sys
import os

# Add the sustainable_energy directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sustainable_energy'))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from ml_models.sdg7_access_classifier import SDG7AccessClassifier

def test_objective3():
    print("=" * 60)
    print("Testing Objective 3: SDG 7 Electricity Access Classification")
    print("=" * 60)
    
    csv_path = 'global-data-on-sustainable-energy.csv'
    
    # Initialize classifier
    print("\n1. Initializing classifier...")
    classifier = SDG7AccessClassifier(csv_path)
    
    # Load and clean data
    print("2. Loading and cleaning data...")
    classifier.load_and_clean_data()
    print(f"   ✓ Loaded {len(classifier.df)} records")
    print(f"   ✓ Access levels: {classifier.df['Access Level'].value_counts().to_dict()}")
    
    # Train and compare models
    print("\n3. Training and comparing models...")
    mse_scores = classifier.train_and_compare_models()
    print("   Model MSE Scores:")
    for model, mse in mse_scores.items():
        print(f"   - {model}: {mse:.4f}")
    print(f"   ✓ Best model: {classifier.best_model_name}")
    
    # Get all countries
    print("\n4. Getting all countries...")
    countries = classifier.get_all_countries()
    print(f"   ✓ Found {len(countries)} countries")
    print(f"   Sample countries: {countries[:5]}")
    
    # Test with India
    test_country = 'India'
    print(f"\n5. Testing with {test_country}...")
    
    # Get historical data
    print(f"   a) Historical data for {test_country}:")
    historical = classifier.get_historical_data(test_country)
    print(f"      ✓ {len(historical)} historical records")
    if historical:
        latest = historical[-1]
        print(f"      Latest: {latest['Year']} - {latest['Access to electricity (% of population)']}% ({latest['Access Level']})")
    
    # Get future predictions
    print(f"   b) Future predictions for {test_country}:")
    predictions = classifier.predict_future_access(10, test_country)
    if predictions:
        print(f"      ✓ {len(predictions)} predictions")
        print(f"      Sample: {predictions[0]['year']} - {predictions[0]['predicted_access_level']}")
        print(f"              {predictions[-1]['year']} - {predictions[-1]['predicted_access_level']}")
    
    # Get combined data
    print(f"   c) Combined historical + future data:")
    combined = classifier.get_combined_historical_future(test_country)
    print(f"      ✓ {len(combined)} total records")
    hist_count = len([d for d in combined if d['type'] == 'historical'])
    pred_count = len([d for d in combined if d['type'] == 'predicted'])
    print(f"      Historical: {hist_count}, Predicted: {pred_count}")
    
    # Get policy markers
    print(f"\n6. Testing policy markers for {test_country}...")
    policy_markers = classifier.get_policy_impact_data(test_country)
    if policy_markers:
        print(f"   ✓ Found {len(policy_markers)} policy markers")
        for marker in policy_markers:
            print(f"   - {marker['country']} ({marker['year']}): {marker['electricity_access']:.1f}% - {marker['access_level']}")
    else:
        print(f"   No policy markers for {test_country}")
    
    # Test with policy countries
    print("\n7. Testing all policy countries...")
    policy_countries = ['India', 'Bangladesh', 'Kenya', 'Nigeria', 'Brazil']
    all_markers = classifier.get_policy_impact_data()
    print(f"   ✓ Found {len(all_markers)} total policy markers")
    for marker in all_markers:
        print(f"   - {marker['country']} ({marker['year']}): {marker['electricity_access']:.1f}%")
    
    # Get access level distribution
    print(f"\n8. Testing access level distribution for {test_country}...")
    distribution = classifier.get_access_level_distribution(test_country)
    print(f"   ✓ {len(distribution)} distribution records")
    if distribution:
        print(f"   Sample: Year {distribution[0]['year']} - {distribution[0]['access_level']}: {distribution[0]['count']} records")
    
    print("\n" + "=" * 60)
    print("✓ All Objective 4 tests completed successfully!")
    print("=" * 60)
    
    return True

if __name__ == '__main__':
    try:
        test_objective3()
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
