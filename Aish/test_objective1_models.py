"""
Test script to verify Objective 1 model comparison with all 7 models
"""
import sys
import os

# Add the sustainable_energy directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sustainable_energy'))

from ml_models.energy_consumption_predictor import EnergyConsumptionPredictor

# Path to CSV
CSV_PATH = 'global-data-on-sustainable-energy.csv'

print("=" * 60)
print("Testing Objective 1: Energy Consumption Prediction")
print("=" * 60)

# Initialize predictor
predictor = EnergyConsumptionPredictor(CSV_PATH)

# Load data
print("\n1. Loading and cleaning data...")
predictor.load_and_clean_data()
print(f"   ✓ Loaded {len(predictor.df)} rows")

# Train and compare models
print("\n2. Training and comparing models...")
mse_scores = predictor.train_and_compare_models()

print("\n3. Model Comparison Results (MSE):")
print("-" * 60)
for model_name, mse in sorted(mse_scores.items(), key=lambda x: x[1]):
    print(f"   {model_name:20s}: {mse:.4f}")

print("\n4. Best Model:")
print(f"   ✓ {predictor.best_model_name} (MSE: {mse_scores[predictor.best_model_name]:.4f})")

print("\n" + "=" * 60)
print("Test completed successfully!")
print("=" * 60)
