"""
Setup Gmail App Password for Real Email Sending
Run this script to configure your Gmail App Password
"""

import os

print("\n" + "="*70)
print("📧 Gmail App Password Setup")
print("="*70)

print("\n🔐 To send REAL emails, you need a Gmail App Password")
print("\n📝 Steps to get your Gmail App Password:")
print("   1. Go to: https://myaccount.google.com/apppasswords")
print("   2. Sign in with: assowmya649@gmail.com")
print("   3. If you see 'App passwords', click it")
print("   4. If not, enable 2-Step Verification first:")
print("      → https://myaccount.google.com/security")
print("   5. Select 'Mail' and 'Other (Custom name)'")
print("   6. Type: 'SDG7 Alert System'")
print("   7. Click 'Generate'")
print("   8. Copy the 16-character password (e.g., 'abcd efgh ijkl mnop')")

print("\n" + "="*70)
app_password = input("\n📋 Paste your 16-character App Password here: ").strip()

if not app_password or app_password == 'your-app-password':
    print("\n❌ No password entered. Please run this script again with your App Password.")
    exit(1)

# Remove spaces from password
app_password = app_password.replace(' ', '')

# Update email_config.py
config_path = 'sustainable_energy/email_config.py'

try:
    with open(config_path, 'r') as f:
        content = f.read()
    
    # Replace the password
    content = content.replace(
        "'sender_password': 'your-app-password'",
        f"'sender_password': '{app_password}'"
    )
    
    with open(config_path, 'w') as f:
        f.write(content)
    
    print("\n✅ Gmail App Password configured successfully!")
    print("\n📧 Email Configuration:")
    print(f"   Sender: assowmya649@gmail.com")
    print(f"   Password: {'*' * len(app_password)} (hidden)")
    print(f"   Mode: REAL EMAIL SENDING ENABLED")
    
    print("\n🎯 Ready to send real emails!")
    print("\n📝 Test it now:")
    print("   python send_xgboost_alert_to_country.py Albania")
    
    print("\n✅ You will receive a REAL email at: assowmya649@gmail.com")
    print("="*70 + "\n")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nPlease manually edit: sustainable_energy/email_config.py")
    print(f"Replace 'your-app-password' with: {app_password}")
