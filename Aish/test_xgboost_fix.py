#!/usr/bin/env python3
"""
Test the fixed XGBoost alerts
"""

import requests
import json

def test_xgboost_alerts():
    """Test the XGBoost alerts API"""
    
    print("🧪 Testing XGBoost Alerts API...")
    
    try:
        # Make request to the API
        url = 'http://127.0.0.1:8000/api/send-xgboost-alerts/'
        
        print(f"📡 Making POST request to: {url}")
        
        response = requests.post(url, timeout=30)
        
        print(f"📊 Response Status: {response.status_code}")
        print(f"📄 Response Headers: {dict(response.headers)}")
        
        # Check if response is JSON
        try:
            data = response.json()
            print("✅ Response is valid JSON")
            print(f"📋 Response Data:")
            print(json.dumps(data, indent=2))
            
            if data.get('success'):
                print(f"🎉 SUCCESS! Sent {data.get('emails_sent', 0)} emails")
                
                alerts = data.get('alerts', [])
                if alerts:
                    print(f"\n📧 Emails sent:")
                    for alert in alerts:
                        print(f"   {alert['country']}: {alert['status']} ({alert['access']:.1f}%) → {alert['email']}")
                else:
                    print("⚠️ No alerts in response")
            else:
                print(f"❌ API returned error: {data.get('error', 'Unknown error')}")
                
        except json.JSONDecodeError:
            print("❌ Response is not valid JSON")
            print(f"📄 Raw Response: {response.text[:500]}...")
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Is Django running?")
        print("   Start server with: cd sustainable_energy && python manage.py runserver")
        
    except requests.exceptions.Timeout:
        print("⏰ Request timed out (30 seconds)")
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    test_xgboost_alerts()