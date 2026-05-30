#!/usr/bin/env python3
"""
Verify that Objective 3 shows exactly 8 models in model comparison
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(__file__))

def test_objective3_models():
    """Test that Objective 3 returns exactly 8 models"""
    print("🧪 Testing Objective 3 Model Count...")
    
    try:
        from objective3_real_analysis import get_real_obj3_model_comparison
        
        result = get_real_obj3_model_comparison()
        
        if result['success']:
            models = result['mse_scores']
            model_count = len(models)
            best_model = result['best_model']
            best_score = result['best_score']
            
            print(f"📊 Found {model_count} models:")
            for i, (model, score) in enumerate(models.items(), 1):
                status = "🏆" if model == best_model else "📈"
                print(f"  {i}. {status} {model}: {score:.4f}")
            
            print(f"\n🏆 Best Model: {best_model} (Accuracy: {best_score:.4f})")
            
            if model_count == 8:
                print("✅ SUCCESS: Objective 3 correctly shows 8 models!")
                return True
            else:
                print(f"❌ FAIL: Expected 8 models, found {model_count}")
                return False
        else:
            print("❌ FAIL: API returned error")
            return False
            
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def main():
    """Main test function"""
    print("🎯 Objective 3 Model Count Verification")
    print("=" * 40)
    
    success = test_objective3_models()
    
    print("\n" + "=" * 40)
    if success:
        print("🎉 Objective 3 is ready with 8 models!")
    else:
        print("⚠️  Objective 3 needs attention")

if __name__ == "__main__":
    main()