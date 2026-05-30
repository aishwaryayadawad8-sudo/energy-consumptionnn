#!/usr/bin/env python3
"""
Test the new energy dataset integration
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from new_energy_adapter import NewEnergyDataAdapter

def test_new_dataset():
    """Test the new dataset functionality"""
    
    print("🧪 Testing New Energy Dataset Integration...")
    
    # Initialize adapter
    adapter = NewEnergyDataAdapter()
    
    # Test 1: Load data
    print("\n1️⃣ Testing data loading...")
    if adapter.load_data():
        print("✅ Data loaded successfully")
    else:
        print("❌ Failed to load data")
        return
    
    # Test 2: Get countries
    print("\n2️⃣ Testing country list...")
    countries = adapter.get_countries()
    print(f"✅ Found {len(countries)} countries: {', '.join(countries)}")
    
    # Test 3: Get country data
    print("\n3️⃣ Testing country data retrieval...")
    for country in countries[:2]:  # Test first 2 countries
        data = adapter.get_country_data(country)
        if data:
            print(f"✅ {country}: {len(data['years'])} years of data, latest access: {data['latest_access']}%")
        else:
            print(f"❌ No data for {country}")
    
    # Test 4: Get latest access rates
    print("\n4️⃣ Testing latest access rates...")
    latest_rates = adapter.get_latest_access_rates()
    for country, info in latest_rates.items():
        print(f"   {country}: {info['access_rate']}% in {info['year']}")
    
    # Test 5: Predictions
    print("\n5️⃣ Testing predictions...")
    predictions = adapter.predict_future_access(1)
    for pred in predictions:
        print(f"   {pred['country']} 2021: {pred['predicted_access']:.1f}%")
    
    # Test 6: Summary stats
    print("\n6️⃣ Testing summary statistics...")
    stats = adapter.get_summary_stats()
    for key, value in stats.items():
        print(f"   {key}: {value}")
    
    print("\n✅ All tests completed!")

if __name__ == "__main__":
    test_new_dataset()
