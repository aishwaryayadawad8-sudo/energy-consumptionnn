#!/usr/bin/env python3
"""
Speed test for Objective 6 Fast Analysis
"""

import time
import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from objective6_fast_analysis import (
    get_fast_obj6_model_comparison,
    get_fast_obj6_countries,
    get_fast_obj6_historical_data,
    get_fast_obj6_future_predictions,
    get_fast_obj6_combined_data
)

def time_function(func, *args, **kwargs):
    """Time a function execution"""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return result, execution_time

def test_objective6_speed():
    """Test the speed of Objective 6 API endpoints"""
    print("⚡ Speed Test for Objective 6: Efficiency Optimization Identification")
    print("=" * 70)
    
    # Test 1: Model Comparison (Classification)
    print("📊 Testing Model Comparison (Classification)...")
    result, time_ms = time_function(get_fast_obj6_model_comparison)
    print(f"✅ Model Comparison: {time_ms:.2f}ms")
    print(f"   Best Model: {result['best_model']} (Accuracy: {result['best_score']:.4f})")
    print(f"   Task Type: {result['task_type']} | Metric: {result['metric']}")
    
    # Test 2: Countries List
    print("\n🌍 Testing Countries List...")
    result, time_ms = time_function(get_fast_obj6_countries)
    print(f"✅ Countries List: {time_ms:.2f}ms")
    print(f"   Countries Available: {len(result['countries'])}")
    
    # Test 3: Country Analysis (multiple countries)
    test_countries = ["United States", "Germany", "China", "India", "Brazil"]
    
    print(f"\n🔍 Testing Efficiency Analysis for {len(test_countries)} countries...")
    
    total_time = 0
    for country in test_countries:
        print(f"\n📍 Testing {country}:")
        
        # Historical efficiency data
        result, time_ms = time_function(get_fast_obj6_historical_data, country)
        total_time += time_ms
        if result['success']:
            print(f"   📊 Historical: {time_ms:.2f}ms ({len(result['data'])} points)")
            # Show efficiency levels
            efficiency_levels = [d['Efficiency_Level'] for d in result['data']]
            latest_level = efficiency_levels[-1] if efficiency_levels else "Unknown"
            print(f"       Latest Efficiency: {latest_level}")
        else:
            print(f"   📊 Historical: {time_ms:.2f}ms (No data)")
        
        # Future efficiency predictions
        result, time_ms = time_function(get_fast_obj6_future_predictions, country)
        total_time += time_ms
        if result['success']:
            print(f"   🔮 Predictions: {time_ms:.2f}ms ({len(result['predictions'])} points)")
            # Show predicted efficiency
            pred_levels = [d['Efficiency_Level'] for d in result['predictions']]
            future_level = pred_levels[-1] if pred_levels else "Unknown"
            print(f"       Predicted 2030: {future_level}")
        else:
            print(f"   🔮 Predictions: {time_ms:.2f}ms (No data)")
        
        # Combined efficiency data
        result, time_ms = time_function(get_fast_obj6_combined_data, country)
        total_time += time_ms
        if result['success']:
            print(f"   📈 Combined: {time_ms:.2f}ms ({len(result['data'])} points)")
        else:
            print(f"   📈 Combined: {time_ms:.2f}ms (No data)")
    
    print(f"\n⚡ OBJECTIVE 6 SPEED SUMMARY:")
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
    print(f"📈 Expected User Experience: Efficiency charts load instantly!")
    
    # Show model comparison details
    print(f"\n📊 MODEL COMPARISON DETAILS:")
    comp_result = get_fast_obj6_model_comparison()
    for model, accuracy in comp_result['mse_scores'].items():
        star = "⭐" if model == comp_result['best_model'] else "  "
        print(f"{star} {model}: {accuracy:.4f}")

if __name__ == "__main__":
    test_objective6_speed()