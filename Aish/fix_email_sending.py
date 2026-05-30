"""
Script to fix email sending configuration
Run this to enable email alerts
"""

print("=" * 70)
print("🔧 Email Configuration Fix Script")
print("=" * 70)

# Step 1: Check current configuration
print("\n📋 Step 1: Checking current configuration...")
print("-" * 70)

try:
    from sustainable_energy.email_config import EMAIL_CONFIG, ENABLE_ACTUAL_EMAIL_SENDING, TESTING_MODE
    
    print(f"✅ Configuration file found")
    print(f"   Sender Email: {EMAIL_CONFIG['sender_email']}")
    print(f"   Password Set: {'Yes' if EMAIL_CONFIG['sender_password'] != 'your-app-password' else 'NO - NEEDS FIXING'}")
    print(f"   Email Sending Enabled: {'Yes' if ENABLE_ACTUAL_EMAIL_SENDING else 'NO - NEEDS FIXING'}")
    print(f"   Testing Mode: {'Yes' if TESTING_MODE else 'No'}")
    
    needs_fixing = []
    
    if EMAIL_CONFIG['sender_password'] == 'your-app-password':
        needs_fixing.append("Password not configured")
    
    if not ENABLE_ACTUAL_EMAIL_SENDING:
        needs_fixing.append("Email sending is disabled")
    
    if needs_fixing:
        print(f"\n⚠️  Issues found: {len(needs_fixing)}")
        for issue in needs_fixing:
            print(f"   - {issue}")
    else:
        print(f"\n✅ Configuration looks good!")
        
except Exception as e:
    print(f"❌ Error loading configuration: {e}")
    exit(1)

# Step 2: Check country emails
print("\n📧 Step 2: Checking country emails...")
print("-" * 70)

try:
    import pandas as pd
    df = pd.read_csv('country_emails.csv')
    print(f"✅ Found {len(df)} countries with email addresses")
    print(f"   Sample countries: {', '.join(df['Country'].head(5).tolist())}")
except Exception as e:
    print(f"⚠️  Warning: Could not load country_emails.csv: {e}")

# Step 3: Provide fix instructions
print("\n🔧 Step 3: How to Fix")
print("-" * 70)

if needs_fixing:
    print("\nTo fix the issues:")
    print("\n1. Open: sustainable_energy/email_config.py")
    print("\n2. Make these changes:")
    
    if "Password not configured" in needs_fixing:
        print("\n   a) Get Gmail App Password:")
        print("      - Go to: https://myaccount.google.com/apppasswords")
        print("      - Create new App Password for 'Mail'")
        print("      - Copy the 16-character password")
        print("\n   b) Update this line:")
        print("      'sender_password': 'your-app-password',")
        print("      Change to:")
        print("      'sender_password': 'YOUR_ACTUAL_PASSWORD',")
    
    if "Email sending is disabled" in needs_fixing:
        print("\n   c) Enable email sending:")
        print("      ENABLE_ACTUAL_EMAIL_SENDING = False")
        print("      Change to:")
        print("      ENABLE_ACTUAL_EMAIL_SENDING = True")
    
    print("\n3. Save the file")
    print("\n4. Restart Django server:")
    print("   cd sustainable_energy")
    print("   python manage.py runserver")
    
    print("\n5. Test by visiting:")
    print("   http://127.0.0.1:8000/objective8/")
    print("   Click 'Send Email Alerts'")
else:
    print("\n✅ No fixes needed! Your configuration is ready.")
    print("\nTo test:")
    print("1. Make sure Django server is running")
    print("2. Visit: http://127.0.0.1:8000/objective8/")
    print("3. Click 'Send Email Alerts'")
    print("4. Check your email inbox!")

# Step 4: Test email connection (optional)
print("\n🧪 Step 4: Test Email Connection (Optional)")
print("-" * 70)

test = input("\nDo you want to test email connection now? (y/n): ").lower()

if test == 'y':
    if EMAIL_CONFIG['sender_password'] == 'your-app-password':
        print("❌ Cannot test - password not configured")
        print("   Please set up your Gmail App Password first")
    elif not ENABLE_ACTUAL_EMAIL_SENDING:
        print("⚠️  Email sending is disabled")
        print("   Emails will be simulated (not actually sent)")
        print("   Set ENABLE_ACTUAL_EMAIL_SENDING = True to send real emails")
    else:
        print("\n📤 Testing email connection...")
        try:
            import smtplib
            server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
            server.starttls()
            server.login(EMAIL_CONFIG['sender_email'], EMAIL_CONFIG['sender_password'])
            server.quit()
            print("✅ Email connection successful!")
            print("   Your email configuration is working!")
        except Exception as e:
            print(f"❌ Email connection failed: {e}")
            print("\nTroubleshooting:")
            print("1. Check your Gmail App Password is correct")
            print("2. Make sure 2-Factor Authentication is enabled")
            print("3. Try generating a new App Password")

print("\n" + "=" * 70)
print("✅ Configuration check complete!")
print("=" * 70)
print("\nFor detailed instructions, see: FIX_EMAIL_ZERO_SENT.md")
