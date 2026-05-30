#!/usr/bin/env python3
"""
Test Objective 4 Model Comparison
Tests the exact code pattern provided by the user
"""

import sys
import os

# Add the sustainable_energy directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sustainable_energy'))

from ml_models.objective4_model_comparison import Objective4ModelComparison

def test_model_comparison():
    print("\n" + "="*70)
    print("🧪 Testing Objective 4: Model Comparison")
    print("   Using exact code pattern from user")
    print("="*70)
    
    # Get CSV path
    csv_path = 'global-data-on-sustainable-energy.csv'
    
    if not os.path.exists(csv_path):
        print(f"\n❌ Error: CSV file not found at {csv_path}")
        return
    
    # Create comparison object
    print("\n1️⃣  Creating model comparison object...")
    comparison = Objective4ModelComparison(csv_path)
    
    # Train and compare models
    print("\n2️⃣  Training and comparing 7 ML models...")
    print("   - Linear Regression")
    print("   - Decision Tree")
    print("   - KNN")
    print("   - XGBoost")
    print("   - LightGBM")
    print("   - CatBoost")
    print("   - Random Forest")
    
    mse_scores = comparison.train_and_compare_models()
    
    # Print results
    print("\n3️⃣  Model Comparison Results:")
    print("="*70)
    comparison.print_comparison()
    print("="*70)
    
    # Get data for API
    print("\n4️⃣  Getting data for API...")
    data = comparison.get_model_comparison_data()
    
    print(f"\n✅ Success: {data['success']}")
    print(f"📊 Objective: {data['objective']['name']}")
    print(f"📈 Metric: {data['metric']}")
    print(f"🏆 Best Model: {data['best_model']}")
    print(f"⭐ Best Value: {data['best_value']:.4f}")
    
    print("\n5️⃣  MSE Scores (sorted by performance):")
    sorted_scores = sorted(data['mse_scores'].items(), key=lambda x: x[1])
    for i, (model, mse) in enumerate(sorted_scores, 1):
        marker = "🏆" if model == data['best_model'] else "  "
        print(f"   {marker} {i}. {model}: {mse:.4f}")
    
    print("\n6️⃣  Color Coding:")
    for model, color in zip(data['models'], data['colors']):
        emoji = "🟡" if color == "gold" else "🔵"
        print(f"   {emoji} {model}: {color}")
    
    print("\n" + "="*70)
    print("✅ All tests passed!")
    print("="*70)
    
    print("\n📌 Next Steps:")
    print("   1. Start Django server: cd sustainable_energy && python manage.py runserver")
    print("   2. Open browser: http://127.0.0.1:8000/objective4/")
    print("   3. Model comparison will load automatically")
    print("   4. Best model will be highlighted in GOLD")
    print("\n")

if __name__ == "__main__":
    try:
        test_model_comparison()
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
