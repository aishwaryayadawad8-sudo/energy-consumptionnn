"""
Test the Comprehensive ML Comparison System
"""

import sys
import os

# Add the sustainable_energy directory to path
sys.path.insert(0, 'sustainable_energy')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sustainable_energy.settings')

import django
django.setup()

from ml_models.comprehensive_ml_comparison import ComprehensiveMLComparison

print("\n" + "="*70)
print("🧪 Testing Comprehensive ML Comparison System")
print("="*70)

# Initialize
csv_path = 'global-data-on-sustainable-energy.csv'
comparison = ComprehensiveMLComparison(csv_path)

# Run comparison
print("\n🚀 Running comparison across all 8 objectives...")
results = comparison.compare_all_objectives()

# Get summary
summary = comparison.get_summary()

print("\n" + "="*70)
print("📊 SUMMARY OF BEST MODELS")
print("="*70)

for sub_no in sorted(summary.keys()):
    obj = summary[sub_no]
    print(f"\nSub-objective {sub_no}: {obj['name']}")
    print(f"   Task: {obj['task']}")
    print(f"   Best Model: {obj['best_model']}")
    print(f"   Score: {obj['best_score']:.4f}")

print("\n" + "="*70)
print("✅ Test Complete!")
print("="*70)
print("\n📌 Next Steps:")
print("   1. Start Django server: python sustainable_energy/manage.py runserver")
print("   2. Visit: http://localhost:8000/comprehensive-comparison/")
print("   3. Click 'Run Comprehensive Analysis'")
print()
