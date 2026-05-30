#!/usr/bin/env python3
"""
Speed test for Objective 5 Fast Analysis
"""

import time
import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from objective5_fast_analysis import (
    get_fast_model_comparison,
    get_fast_countries,
    get_fast_historical_data,
    get_fast_future_predictions,
    get_fast_combined_data
)

def time_function(func, *args, **kwargs):
    """Time a function execution"""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return result, execution_time

def test_speed():
    """Test the speed of all API endpoints"""
    print("⚡ Speed Test for Objective 5 Fast Analysis")
    print("=" * 50)
    
    # Test 1: Model Comparison
    print("📊 Testing Model Comparison...")
    result, time_ms = time_function(get_fast_model_comparison)
    print(f"✅ Model Comparison: {time_ms:.2f}ms")
    print(f"   Best Model: {result['best_model']} (MSE: {result['best_score']:.4f})")
    
    # Test 2: Countries List
    print("\n🌍 Testing Countries List...")
    result, time_ms = time_function(get_fast_countries)
    print(f"✅ Countries List: {time_ms:.2f}ms")
    print(f"   Countries Available: {len(result['countries'])}")
    
    # Test 3: Country Analysis (multiple countries)
    test_countries = ["United States", "China", "Germany", "Brazil", "India"]
    
    print(f"\n🔍 Testing Country Analysis for {len(test_countries)} countries...")
    
    total_time = 0
    for country in test_countries:
        print(f"\n📍 Testing {country}:")
        
        # Historical data
        result, time_ms = time_function(get_fast_historical_data, country)
        total_time += time_ms
        print(f"   📊 Historical: {time_ms:.2f}ms ({len(result['data'])} points)")
        
        # Future predictions
        result, time_ms = time_function(get_fast_future_predictions, country)
        total_time += time_ms
        print(f"   🔮 Predictions: {time_ms:.2f}ms ({len(result['predictions'])} points)")
        
        # Combined data
        result, time_ms = time_function(get_fast_combined_data, country)
        total_time += time_ms
        print(f"   📈 Combined: {time_ms:.2f}ms ({len(result['data'])} points)")
    
    print(f"\n⚡ SPEED SUMMARY:")
    print(f"   Total Analysis Time: {total_time:.2f}ms")
    print(f"   Average per Country: {total_time/len(test_countries):.2f}ms")
    print(f"   Average per API Call: {total_time/(len(test_countries)*3):.2f}ms")
    
    # Performance rating
    avg_time = total_time / (len(test_countries) * 3)
    if avg_time < 1:
        rating = "🚀 BLAZING FAST"
    elif avg_time < 5:
        rating = "⚡ VERY FAST"
    elif avg_time < 10:
        rating = "✅ FAST"
    elif avg_time < 50:
        rating = "⏱️ ACCEPTABLE"
    else:
        rating = "🐌 SLOW"
    
    print(f"\n🏆 Performance Rating: {rating}")
    print(f"📈 Expected User Experience: Charts load instantly!")

if __name__ == "__main__":
    test_speed()