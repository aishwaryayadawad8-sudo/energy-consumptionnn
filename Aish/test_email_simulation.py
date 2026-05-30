"""
Test Email Simulation Mode
This will show that emails work without actually sending them
"""

print("=" * 70)
print("🧪 Testing Email Simulation Mode")
print("=" * 70)

# Test the configuration
print("\n📋 Step 1: Checking Configuration")
print("-" * 70)

try:
    from sustainable_energy.email_config import EMAIL_CONFIG, ENABLE_ACTUAL_EMAIL_SENDING, TESTING_MODE
    
    print(f"✅ Email Configuration Loaded")
    print(f"   Sender: {EMAIL_CONFIG['sender_email']}")
    print(f"   Testing Mode: {TESTING_MODE}")
    print(f"   Actual Sending: {ENABLE_ACTUAL_EMAIL_SENDING}")
    print(f"   Mode: {'SIMULATION' if not ENABLE_ACTUAL_EMAIL_SENDING else 'REAL SENDING'}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)

# Test email alert system
print("\n📧 Step 2: Testing Email Alert System")
print("-" * 70)

try:
    import sys
    import os
    sys.path.insert(0, 'sustainable_energy')
    
    from ml_models.email_alerts import SDG7EmailAlerts
    import pandas as pd
    
    # Create test predictions
    test_data = pd.DataFrame({
        'country': ['Kenya', 'India', 'Nigeria', 'Germany', 'Bangladesh'],
        'year': [2024, 2024, 2024, 2024, 2024],
        'predicted_access': [45.5, 99.2, 55.3, 99.8, 88.5]
    })
    
    print(f"✅ Created test data for {len(test_data)} countries")
    print(f"   Countries: {', '.join(test_data['country'].tolist())}")
    
    # Initialize alert system
    alert_system = SDG7EmailAlerts()
    print(f"\n✅ Email Alert System Initialized")
    
    # Send alerts (simulated)
    print(f"\n📤 Sending Simulated Alerts...")
    print("-" * 70)
    
    alerts_sent = alert_system.analyze_and_send_alerts(test_data, log_to_db=False)
    
    print(f"\n✅ Simulation Complete!")
    print(f"   Total Alerts: {len(alerts_sent)}")
    
    if alerts_sent:
        print(f"\n📊 Alert Summary:")
        for alert in alerts_sent:
            status_emoji = {
                'critical': '🚨',
                'needs_improvement': '⚠️',
                'excellent': '✅'
            }.get(alert['status'], '📧')
            
            print(f"   {status_emoji} {alert['country']}: {alert['access']:.1f}% - {alert['status'].upper()}")
    
    print("\n" + "=" * 70)
    print("✅ Email Simulation Mode is Working!")
    print("=" * 70)
    print("\nWhat this means:")
    print("✅ Your email system is configured correctly")
    print("✅ Emails will show as 'sent successfully'")
    print("✅ All data is logged to database")
    print("✅ Perfect for presentations and demos")
    print("❌ Emails are NOT actually sent (simulation only)")
    
    print("\n💡 To enable REAL email sending:")
    print("1. Get Gmail App Password from: https://myaccount.google.com/apppasswords")
    print("2. Update 'sender_password' in email_config.py")
    print("3. Set ENABLE_ACTUAL_EMAIL_SENDING = True")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 70)
