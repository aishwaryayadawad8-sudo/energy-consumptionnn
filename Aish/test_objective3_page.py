"""
Test if Objective 4 page loads correctly
"""

import sys
import os

# Add the sustainable_energy directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sustainable_energy'))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from django.test import Client
from django.urls import reverse

def test_objective3_page():
    print("=" * 60)
    print("Testing Objective 3 Page Load")
    print("=" * 60)
    
    client = Client()
    
    # Test 1: Check if URL resolves
    print("\n1. Testing URL resolution...")
    try:
        url = reverse('objective3_dashboard')
        print(f"   ✓ URL resolved: {url}")
    except Exception as e:
        print(f"   ✗ URL resolution failed: {e}")
        return False
    
    # Test 2: Check if page loads
    print("\n2. Testing page load...")
    try:
        response = client.get('/objective3/')
        print(f"   Status code: {response.status_code}")
        
        if response.status_code == 200:
            print("   ✓ Page loaded successfully")
            print(f"   Content length: {len(response.content)} bytes")
            
            # Check if it's not empty
            if len(response.content) < 100:
                print("   ⚠ Warning: Page content is very small")
                print(f"   Content: {response.content[:200]}")
            else:
                print("   ✓ Page has content")
                
        else:
            print(f"   ✗ Page load failed with status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"   ✗ Page load error: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Test 3: Check API endpoints
    print("\n3. Testing API endpoints...")
    
    endpoints = [
        '/api/objective3/countries/',
        '/api/objective3/model-comparison/',
    ]
    
    for endpoint in endpoints:
        try:
            response = client.get(endpoint)
            if response.status_code == 200:
                print(f"   ✓ {endpoint} - OK")
            else:
                print(f"   ✗ {endpoint} - Status {response.status_code}")
        except Exception as e:
            print(f"   ✗ {endpoint} - Error: {e}")
    
    print("\n" + "=" * 60)
    print("✓ Objective 4 page test completed")
    print("=" * 60)
    
    return True

if __name__ == '__main__':
    try:
        test_objective3_page()
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
