"""
Diagnose Email Failure - Show exactly why emails are failing
"""

import sys
import os

sys.path.insert(0, 'sustainable_energy')

print("\n" + "="*70)
print("🔍 EMAIL FAILURE DIAGNOSIS")
print("="*70)

try:
    from email_config import EMAIL_CONFIG, ENABLE_ACTUAL_EMAIL_SENDING, TESTING_MODE, SIMULATION_MODE
    
    print("\n📋 CURRENT CONFIGURATION:")
    print(f"   Sender Email: {EMAIL_CONFIG['sender_email']}")
    print(f"   SMTP Server: {EMAIL_CONFIG['smtp_server']}:{EMAIL_CONFIG['smtp_port']}")
    
    # Check password
    password = EMAIL_CONFIG['sender_password']
    if password == 'your-app-password':
        print(f"   Password: ❌ NOT CONFIGURED (still using placeholder)")
        print()
        print("🚨 PROBLEM FOUND: Gmail App Password Not Set")
        print()
        print("This is why all your emails show 'failed' status!")
        print()
    else:
        # Mask password for security
        masked = password[:4] + "*" * (len(password) - 8) + password[-4:]
        print(f"   Password: ✅ Configured ({masked})")
        print()
        
        # Test authentication
        print("🧪 Testing Gmail authentication...")
        import smtplib
        
        try:
            server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
            server.starttls()
            server.login(EMAIL_CONFIG['sender_email'], password)
            server.quit()
            print("   ✅ Authentication successful!")
            print()
            print("✅ EMAIL SYSTEM IS WORKING CORRECTLY")
            print()
            print("If you're still seeing 'failed' status:")
            print("1. Restart your Django server")
            print("2. Clear your browser cache")
            print("3. Try sending a new alert")
            print()
            
        except smtplib.SMTPAuthenticationError:
            print("   ❌ Authentication failed!")
            print()
            print("🚨 PROBLEM FOUND: Invalid Gmail App Password")
            print()
            print("The password is set but incorrect.")
            print()
        except Exception as e:
            print(f"   ❌ Connection error: {str(e)}")
            print()
    
    print("📊 EMAIL SETTINGS:")
    print(f"   Email Sending: {'✅ ENABLED' if ENABLE_ACTUAL_EMAIL_SENDING else '❌ DISABLED'}")
    print(f"   Testing Mode: {'✅ ON (sends to dummy email)' if TESTING_MODE else '❌ OFF (sends to real emails)'}")
    print(f"   Simulation Mode: {'✅ ON (no actual sending)' if SIMULATION_MODE else '❌ OFF (real sending)'}")
    print()
    
    # Check database logs
    print("📝 CHECKING EMAIL LOGS...")
    try:
        import django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sustainable_energy.settings')
        django.setup()
        
        from dashboard.models import EmailLog
        
        total_logs = EmailLog.objects.count()
        failed_logs = EmailLog.objects.filter(status='failed').count()
        success_logs = EmailLog.objects.filter(status='success').count()
        
        print(f"   Total Emails: {total_logs}")
        print(f"   ✅ Success: {success_logs}")
        print(f"   ❌ Failed: {failed_logs}")
        print()
        
        if failed_logs > 0:
            # Get last failed email
            last_failed = EmailLog.objects.filter(status='failed').order_by('-sent_at').first()
            if last_failed:
                print(f"   Last Failed Email:")
                print(f"      Country: {last_failed.country}")
                print(f"      Email: {last_failed.recipient_email}")
                print(f"      Time: {last_failed.sent_at}")
                if last_failed.error_message:
                    print(f"      Error: {last_failed.error_message}")
                print()
        
    except Exception as db_error:
        print(f"   ⚠️  Could not check database: {str(db_error)}")
        print()
    
    print("="*70)
    print("🔧 HOW TO FIX:")
    print("="*70)
    print()
    
    if password == 'your-app-password':
        print("STEP 1: Generate Gmail App Password")
        print("   → Go to: https://myaccount.google.com/apppasswords")
        print("   → Generate a new App Password")
        print()
        print("STEP 2: Update Configuration")
        print("   → Run: python fix_email_password.py")
        print("   → Or manually edit: sustainable_energy/email_config.py")
        print()
        print("STEP 3: Restart Server")
        print("   → Stop Django server (Ctrl+C)")
        print("   → Start again: python sustainable_energy/manage.py runserver")
        print()
        print("STEP 4: Test")
        print("   → Go to: http://localhost:8000/objective8/")
        print("   → Send a test alert")
        print("   → Check status in Email Logs")
        print()
    else:
        print("Your password is configured but authentication failed.")
        print()
        print("Try these steps:")
        print("1. Generate a NEW App Password at:")
        print("   https://myaccount.google.com/apppasswords")
        print()
        print("2. Update it by running:")
        print("   python fix_email_password.py")
        print()
        print("3. Make sure 2-Factor Authentication is enabled")
        print()

except ImportError as e:
    print(f"\n❌ ERROR: Could not import email_config")
    print(f"   {str(e)}")
    print()
    print("Make sure you're running this from the project root directory")
    print()

except Exception as e:
    print(f"\n❌ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    print()

print("="*70)
print()
