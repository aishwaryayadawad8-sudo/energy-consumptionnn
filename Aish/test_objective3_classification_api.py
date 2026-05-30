#!/usr/bin/env python3
"""
Test the Objective 3 classification API endpoint
"""

import requests
import json

def test_objective3_api():
    """Test the Objective 3 combined API endpoint"""
    print("🔍 Testing Objective 3 Classification API...")
    
    try:
        # Test with Belarus
        url = "http://localhost:8000/api/objective3/combined/?country=Belarus"
        print(f"📡 Calling: {url}")
        
        response = requests.get(url, timeout=10)
        print(f"📊 Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("📋 Response structure:")
            print(f"   Success: {data.get('success')}")
            
            if data.get('success') and data.get('data'):
                sample_data = data['data']
                print(f"   Data points: {len(sample_data)}")
                
                # Analyze data structure
                historical = [d for d in sample_data if d.get('type') == 'historical']
                predicted = [d for d in sample_data if d.get('type') == 'predicted']
                
                print(f"   Historical points: {len(historical)}")
                print(f"   Predicted points: {len(predicted)}")
                
                if historical:
                    print(f"   Sample historical: {historical[0]}")
                if predicted:
                    print(f"   Sample predicted: {predicted[0]}")
                
                # Check access levels
                access_levels = set()
                for point in sample_data:
                    if 'access_level' in point:
                        access_levels.add(point['access_level'])
                
                print(f"   Access levels: {list(access_levels)}")
                
                if access_levels:
                    print("✅ Objective 3 API works for classification chart!")
                    return True
                else:
                    print("❌ Missing access_level field")
                    return False
            else:
                print(f"❌ API failed: {data.get('error', 'Unknown')}")
                return False
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("🚀 Testing Objective 3 Classification Chart")
    print("=" * 50)
    
    api_works = test_objective3_api()
    
    print("\n" + "=" * 50)
    print("📋 Summary:")
    print(f"   Objective 3 API: {'✅' if api_works else '❌'}")
    
    if api_works:
        print(f"\n🎉 Ready to test!")
        print(f"   1. Restart Django server: python manage.py runserver")
        print(f"   2. Open http://localhost:8000/objective3/")
        print(f"   3. Select a country and click 'Analyze Country'")
        print(f"   4. Look for the stepped line chart!")
        print(f"   5. Check console for [OBJ3-CLASSIFICATION] messages")
    else:
        print(f"\n❌ API needs to be fixed first")

if __name__ == "__main__":
    main()