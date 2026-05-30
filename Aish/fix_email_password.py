"""
Quick Fix: Update Gmail App Password
Run this script to easily update your email password
"""

import os

print("\n" + "="*70)
print("🔧 FIX EMAIL PASSWORD - Quick Setup")
print("="*70)

print("\n📋 INSTRUCTIONS:")
print("1. Go to: https://myaccount.google.com/apppasswords")
print("2. Generate a new App Password (16 characters)")
print("3. Copy the password")
print("4. Paste it below")
print()

# Get password from user
app_password = input("Enter your Gmail App Password (16 characters): ").strip()

# Remove spaces if user included them
app_password = app_password.replace(" ", "")

# Validate
if len(app_password) != 16:
    print(f"\n❌ ERROR: Password should be 16 characters (you entered {len(app_password)})")
    print("   Example: abcdefghijklmnop")
    exit(1)

# Format with spaces for readability
formatted_password = f"{app_password[:4]} {app_password[4:8]} {app_password[8:12]} {app_password[12:16]}"

print(f"\n✅ Password validated: {formatted_password}")
print()

# Update config file
config_path = os.path.join('sustainable_energy', 'email_config.py')

try:
    with open(config_path, 'r') as f:
        content = f.read()
    
    # Find and replace the password line
    import re
    
    # Pattern to match the sender_password line
    pattern = r"'sender_password':\s*'[^']*'"
    replacement = f"'sender_password': '{formatted_password}'"
    
    new_content = re.sub(pattern, replacement, content)
    
    # Write back
    with open(config_path, 'w') as f:
        f.write(new_content)
    
    print("✅ Configuration file updated successfully!")
    print(f"   File: {config_path}")
    print()
    
    # Test the configuration
    print("🧪 Testing email configuration...")
    print()
    
    import sys
    sys.path.insert(0, 'sustainable_energy')
    from email_config import EMAIL_CONFIG, ENABLE_ACTUAL_EMAIL_SENDING
    
    import smtplib
    from email.mime.text import MIMEText
    
    try:
        # Try to connect
        server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.starttls()
        server.login(EMAIL_CONFIG['sender_email'], EMAIL_CONFIG['sender_password'])
        server.quit()
        
        print("✅ EMAIL AUTHENTICATION SUCCESSFUL!")
        print()
        print("="*70)
        print("🎉 ALL DONE! Your email system is now configured correctly.")
        print("="*70)
        print()
        print("Next steps:")
        print("1. Restart your Django server")
        print("2. Go to http://localhost:8000/email-logs/")
        print("3. Send test alerts - they should now show 'success' status!")
        print()
        
    except smtplib.SMTPAuthenticationError:
        print("❌ AUTHENTICATION FAILED!")
        print()
        print("The password you entered is incorrect.")
        print("Please:")
        print("1. Go to https://myaccount.google.com/apppasswords")
        print("2. Generate a NEW App Password")
        print("3. Run this script again")
        print()
        
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        print()

except FileNotFoundError:
    print(f"❌ ERROR: Could not find {config_path}")
    print("   Make sure you're running this from the project root directory")
    print()

except Exception as e:
    print(f"❌ ERROR: {str(e)}")
    print()
