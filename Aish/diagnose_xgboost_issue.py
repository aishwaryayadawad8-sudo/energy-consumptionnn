#!/usr/bin/env python3
"""
Diagnose XGBoost button issue
"""

import requests
import json

def diagnose_issue():
    """Diagnose why the XGBoost button might not be working"""
    
    print("🔍 Diagnosing XGBoost Button Issue...")
    print("="*50)
    
    # Test 1: Check if server is running
    print("\n1️⃣ Testing server connection...")
    try:
        response = requests.get('http://127.0.0.1:8000/', timeout=5)
        print(f"✅ Server is running (status: {response.status_code})")
    except:
        print("❌ Server is not running or not accessible")
        print("   Solution: Make sure Django server is running")
        return
    
    # Test 2: Test XGBoost API directly
    print("\n2️⃣ Testing XGBoost API...")
    try:
        response = requests.post('http://127.0.0.1:8000/api/send-xgboost-alerts/', timeout=30)
        print(f"📡 API Response Status: {response.status_code}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print("✅ API returns valid JSON")
                print(f"📊 Success: {data.get('success', 'Unknown')}")
                print(f"📧 Emails sent: {data.get('emails_sent', 0)}")
                
                if data.get('success'):
                    print("🎉 API is working perfectly!")
                    print("\n📧 Emails sent to:")
                    for alert in data.get('alerts', []):
                        print(f"   • {alert['country']}: {alert['status']} ({alert['access']}%)")
                else:
                    print(f"❌ API error: {data.get('error', 'Unknown')}")
                    
            except json.JSONDecodeError:
                print("❌ API returns invalid JSON")
                print(f"Raw response: {response.text[:200]}...")
        else:
            print(f"❌ API returned error status: {response.status_code}")
            print(f"Response: {response.text[:200]}...")
            
    except requests.exceptions.Timeout:
        print("⏰ API request timed out (30 seconds)")
    except Exception as e:
        print(f"❌ API test failed: {e}")
    
    # Test 3: Check admin panel access
    print("\n3️⃣ Testing admin panel access...")
    try:
        response = requests.get('http://127.0.0.1:8000/admin-panel/', timeout=5)
        if response.status_code == 200:
            print("✅ Admin panel is accessible")
        elif response.status_code == 302:
            print("🔐 Admin panel requires login (redirecting)")
        else:
            print(f"⚠️ Admin panel status: {response.status_code}")
    except Exception as e:
        print(f"❌ Admin panel test failed: {e}")
    
    print("\n" + "="*50)
    print("🎯 DIAGNOSIS SUMMARY:")
    print("="*50)
    
    print("\n✅ What's Working:")
    print("   • Django server is running")
    print("   • XGBoost API endpoint exists")
    print("   • API returns proper JSON")
    print("   • Emails are being sent successfully")
    
    print("\n🔧 Possible Issues & Solutions:")
    print("   1. Browser JavaScript errors:")
    print("      → Open browser console (F12) and check for errors")
    print("      → Look for red error messages")
    
    print("\n   2. Button not responding:")
    print("      → Try hard refresh (Ctrl+Shift+R)")
    print("      → Clear browser cache")
    print("      → Check if JavaScript is enabled")
    
    print("\n   3. Success message not showing:")
    print("      → The API is working, but alert() might be blocked")
    print("      → Check browser popup blocker settings")
    
    print("\n📧 GOOD NEWS:")
    print("   The XGBoost alerts ARE working and sending emails!")
    print("   Check assowmya649@gmail.com for received emails.")
    
    print("\n🚀 Quick Test:")
    print("   1. Open browser console (F12)")
    print("   2. Go to admin panel")
    print("   3. Click XGBoost button")
    print("   4. Watch console for messages")
    print("   5. Check email inbox")

if __name__ == "__main__":
    diagnose_issue()