#!/usr/bin/env python3
"""
Test script for Objective 5 Model Comparison
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from objective5_model_comparison import get_objective5_model_comparison, get_all_objectives_summary

def test_objective5_comparison():
    """Test the Objective 5 model comparison function"""
    print("Testing Objective 5 Model Comparison...")
    
    result = get_objective5_model_comparison()
    
    if result:
        print(f"\n✅ Objective: {result['objective_name']}")
        print(f"📊 Task Type: {result['task_type']}")
        print(f"📈 Metric: {result['metric']}")
        print(f"🏆 Best Model: {result['best_model']} ({result['best_score']:.4f})")
        
        print(f"\n📋 All Model Scores:")
        for model, score in result['scores'].items():
            star = "⭐" if model == result['best_model'] else "  "
            print(f"{star} {model}: {score:.4f}")
        
        return True
    else:
        print("❌ No data available for Objective 5")
        return False

def test_all_objectives_summary():
    """Test the all objectives summary function"""
    print("\n" + "="*50)
    print("Testing All Objectives Summary...")
    
    summary = get_all_objectives_summary()
    
    print(f"\n📊 Summary of Best Models per Objective:")
    for obj_no, data in summary.items():
        print(f"Objective {obj_no}: {data['name']}")
        print(f"  🏆 Best Model: {data['best_model']}")
        print(f"  📈 {data['metric']}: {data['best_score']:.4f}")
        print(f"  🔧 Task: {data['task']}")
        print()

if __name__ == "__main__":
    print("🚀 Starting Objective 5 Model Comparison Tests")
    print("="*50)
    
    # Test Objective 5 specifically
    success = test_objective5_comparison()
    
    if success:
        # Test all objectives summary
        test_all_objectives_summary()
        print("✅ All tests completed successfully!")
    else:
        print("❌ Tests failed!")