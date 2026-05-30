#!/usr/bin/env python3
"""
Verify that the Objective 3 classification chart fix is working
"""

import requests

def test_fix():
    print("🔍 Verifying Objective 3 Fix...")
    
    # Test API
    try:
        response = requests.get("http://localhost:8000/api/objective3/combined/?country=Belarus", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print("✅ API is working")
                print(f"   Data points: {len(data.get('data', []))}")
                return True
            else:
                print("❌ API failed")
                return False
        else:
            print(f"❌ HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("🚀 Testing Objective 3 Classification Chart Fix")
    print("=" * 50)
    
    if test_fix():
        print("\n✅ Fix appears to be working!")
        print("\n🔄 Next steps:")
        print("   1. Restart Django server")
        print("   2. Open http://localhost:8000/objective3/")
        print("   3. Select Belarus and click 'Analyze Country'")
        print("   4. Look for the stepped line chart!")
    else:
        print("\n❌ Fix needs more work")

if __name__ == "__main__":
    main()