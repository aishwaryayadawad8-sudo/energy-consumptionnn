#!/usr/bin/env python3
"""
Test the comprehensive comparison API
"""

import requests
import json

def test_comprehensive_api():
    """Test the comprehensive comparison API endpoint"""
    
    print("🧪 Testing Comprehensive Comparison API...")
    print("="*50)
    
    try:
        # Test the API endpoint
        url = "http://127.0.0.1:8000/api/comprehensive-comparison/"
        
        print(f"📡 Making request to: {url}")
        response = requests.get(url, timeout=30)
        
        print(f"📊 Response Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('success'):
                print("✅ API Response: SUCCESS")
                print(f"📈 Objectives: {len(data.get('objectives', []))}")
                print(f"📊 Results: {len(data.get('results', {}))}")
                print(f"🏆 Summary: {len(data.get('summary', {}))}")
                
                # Show sample results
                print("\n📋 Sample Results:")
                for obj_num, scores in list(data.get('results', {}).items())[:2]:
                    print(f"  Objective {obj_num}:")
                    for model, score in scores.items():
                        print(f"    {model}: {score:.4f}")
                
                print("\n🎯 Best Models Summary:")
                for obj_num, summary in data.get('summary', {}).items():
                    print(f"  Obj {obj_num}: {summary['best_model']} ({summary['best_score']:.4f})")
                
            else:
                print("❌ API Response: FAILED")
                print(f"Error: {data.get('error', 'Unknown error')}")
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            print(f"Response: {response.text[:200]}...")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Make sure Django server is running")
        print("   Run: python manage.py runserver")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("="*50)

if __name__ == "__main__":
    test_comprehensive_api()