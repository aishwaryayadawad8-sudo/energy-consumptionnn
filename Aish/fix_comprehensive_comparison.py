#!/usr/bin/env python3
"""
Fix Comprehensive ML Comparison - Ensure all 7 models show up
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sustainable_energy.settings')
sys.path.append('sustainable_energy')
django.setup()

from django.test import Client
from django.urls import reverse
import json

def test_comprehensive_comparison():
    """Test the comprehensive comparison functionality"""
    
    print("🔧 Testing Comprehensive ML Comparison")
    print("="*60)
    
    # Create test client
    client = Client()
    
    try:
        # Test the API endpoint
        print("📡 Testing API endpoint...")
        response = client.get('/api/comprehensive-comparison/')
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = json.loads(response.content)
            
            if data.get('success'):
                print("✅ API Working Successfully!")
                
                objectives = data.get('objectives', [])
                results = data.get('results', {})
                summary = data.get('summary', {})
                
                print(f"\n📊 Found {len(objectives)} objectives")
                print(f"📈 Found {len(results)} result sets")
                print(f"🏆 Found {len(summary)} summaries")
                
                # Check each objective has 7 models
                print("\n🔍 Checking Model Coverage:")
                expected_models = [
                    "Linear Regression", "Decision Tree", "KNN", 
                    "XGBoost", "LightGBM", "CatBoost", "Random Forest"
                ]
                
                all_good = True
                for obj_num, scores in results.items():
                    models_found = list(scores.keys())
                    print(f"  Objective {obj_num}: {len(models_found)} models")
                    
                    missing_models = set(expected_models) - set(models_found)
                    if missing_models:
                        print(f"    ❌ Missing: {missing_models}")
                        all_good = False
                    else:
                        print(f"    ✅ All 7 models present")
                
                if all_good:
                    print("\n🎉 SUCCESS: All objectives have all 7 models!")
                else:
                    print("\n⚠️  WARNING: Some models are missing")
                
                # Show sample results
                print("\n📋 Sample Results (Objective 3 - Classification):")
                if '3' in results:
                    for model, score in results['3'].items():
                        print(f"  {model}: {score:.4f}")
                
            else:
                print("❌ API returned error:")
                print(f"  Error: {data.get('error', 'Unknown')}")
        else:
            print(f"❌ HTTP Error {response.status_code}")
            print(f"Response: {response.content.decode()[:200]}...")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    print("="*60)

def test_page_load():
    """Test the comprehensive comparison page loads"""
    
    print("\n🌐 Testing Page Load...")
    client = Client()
    
    try:
        response = client.get('/comprehensive-comparison/')
        print(f"Page Status: {response.status_code}")
        
        if response.status_code == 200:
            content = response.content.decode()
            if "Comprehensive ML Model Comparison" in content:
                print("✅ Page loads successfully")
            else:
                print("⚠️  Page loads but content may be wrong")
        else:
            print(f"❌ Page load failed: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Page load error: {e}")

if __name__ == "__main__":
    test_comprehensive_comparison()
    test_page_load()
    
    print("\n🚀 To fix any issues:")
    print("1. Make sure Django server is running: python manage.py runserver")
    print("2. Visit: http://127.0.0.1:8000/comprehensive-comparison/")
    print("3. Check browser console for JavaScript errors")
    print("4. All 7 models should appear in charts for each objective")