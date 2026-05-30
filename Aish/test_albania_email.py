"""
Test Albania Email Configuration
This script verifies that Albania's email is correctly set to assowmya649@gmail.com
"""

import pandas as pd
import sys
import os

print("\n" + "="*70)
print("🔍 Testing Albania Email Configuration")
print("="*70)

# Test 1: Check country_emails.csv
print("\n1️⃣ Checking country_emails.csv...")
try:
    df = pd.read_csv('country_emails.csv')
    albania_row = df[df['Country'] == 'Albania']
    
    if not albania_row.empty:
        albania_email = albania_row['Email'].values[0]
        print(f"✅ Albania email in CSV: {albania_email}")
        
        if albania_email == 'assowmya649@gmail.com':
            print("✅ CORRECT! Albania email is set to assowmya649@gmail.com")
        else:
            print(f"❌ WRONG! Albania email is {albania_email}, should be assowmya649@gmail.com")
    else:
        print("❌ Albania not found in CSV!")
except Exception as e:
    print(f"❌ Error reading CSV: {e}")

# Test 2: Check email_alerts.py loading
print("\n2️⃣ Testing email_alerts.py loading...")
try:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sustainable_energy'))
    from ml_models.email_alerts import SDG7EmailAlerts
    
    alert_system = SDG7EmailAlerts()
    
    if 'Albania' in alert_system.COUNTRY_EMAILS:
        loaded_email = alert_system.COUNTRY_EMAILS['Albania']
        print(f"✅ Albania email loaded: {loaded_email}")
        
        if loaded_email == 'assowmya649@gmail.com':
            print("✅ CORRECT! Email system is using assowmya649@gmail.com")
        else:
            print(f"❌ WRONG! Email system is using {loaded_email}")
            print("   This means CSV is not being loaded correctly!")
    else:
        print("❌ Albania not found in email system!")
        
except Exception as e:
    print(f"❌ Error loading email system: {e}")
    import traceback
    traceback.print_exc()

# Test 3: Check email_config.py
print("\n3️⃣ Checking email_config.py...")
try:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sustainable_energy'))
    from email_config import EMAIL_CONFIG, ENABLE_ACTUAL_EMAIL_SENDING, SIMULATION_MODE, TESTING_MODE
    
    print(f"✅ Sender email: {EMAIL_CONFIG['sender_email']}")
    print(f"✅ ENABLE_ACTUAL_EMAIL_SENDING: {ENABLE_ACTUAL_EMAIL_SENDING}")
    print(f"✅ SIMULATION_MODE: {SIMULATION_MODE}")
    print(f"✅ TESTING_MODE: {TESTING_MODE}")
    
    if EMAIL_CONFIG['sender_email'] == 'assowmya649@gmail.com':
        print("✅ CORRECT! Sender email is assowmya649@gmail.com")
    else:
        print(f"⚠️  Sender email is {EMAIL_CONFIG['sender_email']}")
    
    if ENABLE_ACTUAL_EMAIL_SENDING:
        print("✅ Real email sending is ENABLED")
    else:
        print("⚠️  Real email sending is DISABLED (simulation mode)")
        
except Exception as e:
    print(f"❌ Error loading email config: {e}")

# Test 4: Simulate sending to Albania
print("\n4️⃣ Simulating email send to Albania...")
try:
    from ml_models.email_alerts import SDG7EmailAlerts
    
    alert_system = SDG7EmailAlerts()
    
    if 'Albania' in alert_system.COUNTRY_EMAILS:
        email = alert_system.COUNTRY_EMAILS['Albania']
        print(f"✅ Would send email to: {email}")
        
        if email == 'assowmya649@gmail.com':
            print("✅ SUCCESS! Email would be sent to assowmya649@gmail.com")
        else:
            print(f"❌ FAIL! Email would be sent to {email} instead of assowmya649@gmail.com")
    
except Exception as e:
    print(f"❌ Error: {e}")

print("\n" + "="*70)
print("📊 SUMMARY")
print("="*70)

print("\n✅ If all tests show 'assowmya649@gmail.com', the configuration is correct!")
print("⚠️  If any test shows a different email, there's a configuration issue.")

print("\n📝 To fix issues:")
print("   1. Make sure country_emails.csv has: Albania,assowmya649@gmail.com")
print("   2. Make sure email_config.py has TESTING_MODE = False")
print("   3. Restart any running Django servers")
print("   4. Run: python send_xgboost_alert_to_country.py Albania")

print("\n" + "="*70 + "\n")
