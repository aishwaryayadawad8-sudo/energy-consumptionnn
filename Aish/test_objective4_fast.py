#!/usr/bin/env python3
"""
Test Objective 4 Fast Loading
Verifies that cached results load instantly
"""

import sys
import os
import time

# Add the sustainable_energy directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sustainable_energy'))

from ml_models.objective4_model_comparison import Objective4ModelComparison

def test_fast_loading():
    print("\n" + "="*70)
    print("⚡ Testing Objective 4: Fast Loading")
    print("="*70)
    
    csv_path = 'global-data-on-sustainable-energy.csv'
    
    if not os.path.exists(csv_path):
        print(f"\n❌ Error: CSV file not found at {csv_path}")
        return
    
    # Test 1: Cached Results (Fast)
    print("\n1️⃣  Testing CACHED results (should be instant)...")
    comparison = Objective4ModelComparison(csv_path)
    
    start_time = time.time()
    data = comparison.get_model_comparison_data(use_cached=True)
    end_time = time.time()
    
    cached_time = end_time - start_time
    
    print(f"   ⚡ Time taken: {cached_time:.3f} seconds")
    print(f"   ✅ Success: {data['success']}")
    print(f"   🏆 Best Model: {data['best_model']}")
    print(f"   📊 MSE Scores: {len(data['mse_scores'])} models")
    
    if cached_time < 1.0:
        print(f"   ✅ FAST! Loading time is excellent (< 1 second)")
    else:
        print(f"   ⚠️  Slower than expected (> 1 second)")
    
    # Test 2: Show all scores
    print("\n2️⃣  Model Comparison Results:")
    print("="*70)
    for model, mse in sorted(data['mse_scores'].items(), key=lambda x: x[1]):
        marker = "🏆" if model == data['best_model'] else "  "
        print(f"   {marker} {model}: MSE = {mse:.4f}")
    
    # Test 3: Performance Summary
    print("\n3️⃣  Performance Summary:")
    print("="*70)
    print(f"   Loading Method: Cached Results")
    print(f"   Time Taken: {cached_time:.3f} seconds")
    print(f"   Models Compared: 7")
    print(f"   Best Model: {data['best_model']}")
    print(f"   Best MSE: {data['best_value']:.4f}")
    
    if cached_time < 0.5:
        print(f"\n   ⚡⚡⚡ EXCELLENT! (< 0.5 seconds)")
    elif cached_time < 1.0:
        print(f"\n   ⚡⚡ VERY GOOD! (< 1 second)")
    elif cached_time < 2.0:
        print(f"\n   ⚡ GOOD! (< 2 seconds)")
    else:
        print(f"\n   ⚠️  Could be faster")
    
    print("\n" + "="*70)
    print("✅ Fast loading test complete!")
    print("="*70)
    
    print("\n📌 Next Steps:")
    print("   1. Restart Django server if running")
    print("   2. Open: http://127.0.0.1:8000/objective4/")
    print("   3. Page should load instantly now!")
    print("\n")

if __name__ == "__main__":
    try:
        test_fast_loading()
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
