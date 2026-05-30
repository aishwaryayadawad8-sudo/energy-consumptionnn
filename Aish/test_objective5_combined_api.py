#!/usr/bin/env python3
"""
Test the new combined endpoint
"""
import requests

BASE_URL = "http://localhost:8000"

print("=" * 60)
print("Testing Objective 5 Combined API Endpoint")
print("=" * 60)

# Test combined endpoint for Bahrain
print("\nTesting /api/objective5/combined/?country=Bahrain")
try:
    response = requests.get(f"{BASE_URL}/api/objective5/combined/?country=Bahrain")
    print(f"Status: {response.status_code}")
    data = response.json()
    
    if data.get('success'):
        print(f"✓ Success!")
        print(f"  Total data points: {len(data['data'])}")
        
        historical = [d for d in data['data'] if d['type'] == 'historical']
        predicted = [d for d in data['data'] if d['type'] == 'predicted']
        
        print(f"  Historical: {len(historical)} points")
        print(f"  Predicted: {len(predicted)} points")
        
        if historical:
            print(f"\n  Sample historical:")
            print(f"    Year: {historical[0]['year']}")
            print(f"    Access: {historical[0]['access']}%")
            print(f"    Level: {historical[0]['access_level']}")
        
        if predicted:
            print(f"\n  Sample predicted:")
            print(f"    Year: {predicted[0]['year']}")
            print(f"    Access: {predicted[0]['access']}%")
            print(f"    Level: {predicted[0]['access_level']}")
    else:
        print(f"✗ Error: {data.get('message', data.get('error', 'Unknown'))}")
        
except Exception as e:
    print(f"✗ Exception: {e}")

print("\n" + "=" * 60)
