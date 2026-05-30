#!/usr/bin/env python
"""Quick API test"""
import requests
import json

print("Testing Objective 4 API...")
print("=" * 60)

try:
    # Test the API endpoint
    url = "http://127.0.0.1:8000/api/objective3/model-comparison/"
    print(f"\nCalling: {url}")
    
    response = requests.get(url, timeout=60)
    
    print(f"Status Code: {response.status_code}")
    print(f"Content-Type: {response.headers.get('Content-Type')}")
    
    if response.status_code == 200:
        data = response.json()
        print("\n✅ SUCCESS! Response:")
        print(json.dumps(data, indent=2))
    else:
        print(f"\n❌ ERROR: {response.status_code}")
        print(response.text)
        
except requests.exceptions.ConnectionError:
    print("\n❌ ERROR: Cannot connect to server")
    print("Make sure Django server is running:")
    print("  cd sustainable_energy")
    print("  python manage.py runserver")
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")
