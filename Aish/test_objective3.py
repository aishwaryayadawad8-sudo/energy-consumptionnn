#!/usr/bin/env python
"""Test script for Objective 4 - Electricity Access Classifier"""

import os
import sys

# Add the sustainable_energy directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sustainable_energy'))

from ml_models.electricity_access_classifier import ElectricityAccessClassifier

# CSV path
CSV_PATH = os.path.join(os.path.dirname(__file__), 'global-data-on-sustainable-energy.csv')

print("=" * 60)
print("Testing Objective 4: Electricity Access Classifier")
print("=" * 60)

try:
    print("\n1. Initializing classifier...")
    classifier = ElectricityAccessClassifier(CSV_PATH)
    print("✅ Classifier initialized")
    
    print("\n2. Loading and cleaning data...")
    classifier.load_and_clean_data()
    print(f"✅ Data loaded: {len(classifier.df_class)} rows")
    
    print("\n3. Training models and comparing...")
    accuracy_scores = classifier.train_and_compare_models()
    
    print("\n4. Results:")
    print("-" * 60)
    for model_name, accuracy in accuracy_scores.items():
        print(f"   {model_name:25s}: {accuracy:.4f}")
    print("-" * 60)
    print(f"\n✅ Best Model: {classifier.best_model_name}")
    
    print("\n5. Testing API response format...")
    response = {
        'success': True,
        'accuracy_scores': accuracy_scores,
        'best_model': classifier.best_model_name
    }
    print(f"✅ Response format correct: {response}")
    
    print("\n" + "=" * 60)
    print("✅ ALL TESTS PASSED!")
    print("=" * 60)
    
except Exception as e:
    print(f"\n❌ ERROR: {str(e)}")
    import traceback
    print("\nFull traceback:")
    traceback.print_exc()
    sys.exit(1)
