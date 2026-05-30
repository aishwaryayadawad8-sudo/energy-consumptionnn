#!/usr/bin/env python3
"""
Test script to check if objectives 2 and 3 are working
"""

import requests
import sys

def test_objectives():
    base_url = "http://127.0.0.1:8000"
    
    print("🔍 Testing Objectives 2 and 3...")
    
    objectives = [
        ("Objective 2", f"{base_url}/objective2/"),
        ("Objective 3", f"{base_url}/objective3/")
    ]
    
    for name, url in objectives:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"✅ {name}: Working ({response.status_code})")
            else:
                print(f"❌ {name}: Error {response.status_code}")
                if response.status_code == 404:
                    print(f"   URL not found: {url}")
                elif response.status_code == 500:
                    print(f"   Server error - check template or view function")
        except requests.exceptions.ConnectionError:
            print("❌ Server not running! Please start the Django server first:")
            print("   cd Aish/sustainable_energy")
            print("   python manage.py runserver")
            return False
        except Exception as e:
            print(f"❌ {name}: Error - {e}")
    
    return True

if __name__ == "__main__":
    test_objectives()