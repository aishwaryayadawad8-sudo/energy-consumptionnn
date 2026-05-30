#!/usr/bin/env python3
"""
Test admin login functionality
"""

import requests
import sys

def test_admin_login():
    base_url = "http://127.0.0.1:8000"
    
    print("🔍 Testing Admin Login...")
    
    # Create a session
    session = requests.Session()
    
    try:
        # Step 1: Get login page and CSRF token
        login_page = session.get(f"{base_url}/admin-login/")
        if login_page.status_code != 200:
            print(f"❌ Cannot access login page: {login_page.status_code}")
            return False
        
        print("✅ Login page accessible")
        
        # Extract CSRF token
        csrf_token = None
        for line in login_page.text.split('\n'):
            if 'csrfmiddlewaretoken' in line:
                start = line.find('value="') + 7
                end = line.find('"', start)
                csrf_token = line[start:end]
                break
        
        if not csrf_token:
            print("❌ Could not find CSRF token")
            return False
        
        print("✅ CSRF token found")
        
        # Step 2: Attempt login
        login_data = {
            'username': 'admin',
            'password': 'admin123',
            'csrfmiddlewaretoken': csrf_token
        }
        
        login_response = session.post(f"{base_url}/admin-login/", data=login_data, allow_redirects=False)
        
        if login_response.status_code == 302:
            print("✅ Login successful - redirected to admin panel")
            
            # Step 3: Access admin panel
            admin_panel = session.get(f"{base_url}/admin-panel/")
            if admin_panel.status_code == 200:
                print("✅ Admin panel accessible after login")
                return True
            else:
                print(f"❌ Admin panel not accessible: {admin_panel.status_code}")
                return False
        else:
            print(f"❌ Login failed: {login_response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Server not running! Please start the Django server first:")
        print("   cd Aish/sustainable_energy")
        print("   python manage.py runserver")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = test_admin_login()
    if success:
        print("\n🎉 Admin Panel is working!")
        print("\n📋 How to access:")
        print("1. Go to: http://127.0.0.1:8000/admin-login/")
        print("2. Username: admin")
        print("3. Password: admin123")
        print("4. Click Login")
        print("5. You'll be redirected to the admin panel")
    else:
        print("\n❌ Admin Panel test failed")
        sys.exit(1)