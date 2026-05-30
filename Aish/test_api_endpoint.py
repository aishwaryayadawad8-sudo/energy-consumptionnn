"""
Test the actual API endpoint to see what it returns
"""
import requests

# Test the predictions API
url = "http://127.0.0.1:8000/api/objective1/predictions/?country=India&years=10"

print("Testing Predictions API...")
print(f"URL: {url}")
print("=" * 60)

try:
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print("\n✅ API Response:")
        print(f"Success: {data.get('success')}")
        print(f"Country: {data.get('country')}")
        print(f"Years: {data.get('years')}")
        print(f"Predictions count: {len(data.get('predictions', []))}")
        
        if data.get('predictions'):
            print("\nFirst 3 predictions:")
            for pred in data['predictions'][:3]:
                print(f"  {pred}")
        else:
            print("\n❌ No predictions in response!")
    else:
        print(f"\n❌ Error: {response.status_code}")
        print(response.text)
        
except Exception as e:
    print(f"\n❌ Error: {str(e)}")
    print("\nMake sure your Django server is running!")
    print("Run: python manage.py runserver")
