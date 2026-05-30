"""
Test Email Configuration
Quick test to verify your email setup is working
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def test_email_config():
    """Test if email configuration is working"""
    print("=" * 60)
    print("Testing Email Configuration")
    print("=" * 60)
    print()
    
    # Load config
    try:
        from sustainable_energy.email_config import EMAIL_CONFIG, ENABLE_ACTUAL_EMAIL_SENDING
        
        sender_email = EMAIL_CONFIG['sender_email']
        sender_password = EMAIL_CONFIG['sender_password']
        smtp_server = EMAIL_CONFIG['smtp_server']
        smtp_port = EMAIL_CONFIG['smtp_port']
        
        print(f"📧 Sender Email: {sender_email}")
        print(f"🔐 Password: {'*' * len(sender_password)}")
        print(f"🌐 SMTP Server: {smtp_server}:{smtp_port}")
        print(f"✉️  Sending Enabled: {ENABLE_ACTUAL_EMAIL_SENDING}")
        print()
        
        # Check if password is set
        if sender_password == 'your-app-password':
            print("❌ ERROR: Email password not configured!")
            print()
            print("To fix this:")
            print("1. Go to https://myaccount.google.com/apppasswords")
            print("2. Create an App Password for Mail")
            print("3. Update 'sender_password' in sustainable_energy/email_config.py")
            return False
        
        # Create test email
        recipient = sender_email  # Send to yourself
        subject = "🧪 Test Email from SDG 7 Alert System"
        body = """
Hello!

This is a test email from your SDG 7 Alert System.

If you're reading this, your email configuration is working correctly! ✅

You can now send alerts to countries using:
- python send_alert_to_country.py (for specific countries)
- python send_country_alerts.py (for all countries)

Best regards,
SDG 7 Monitoring System
"""
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Try to send
        if ENABLE_ACTUAL_EMAIL_SENDING:
            print("📤 Attempting to send test email...")
            try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
                server.quit()
                
                print("✅ SUCCESS! Test email sent!")
                print(f"📬 Check your inbox at {recipient}")
                print()
                print("Your email configuration is working correctly!")
                return True
                
            except smtplib.SMTPAuthenticationError:
                print("❌ AUTHENTICATION FAILED!")
                print()
                print("Possible issues:")
                print("1. Incorrect App Password")
                print("2. 2-Factor Authentication not enabled")
                print("3. App Password not generated")
                print()
                print("Fix:")
                print("1. Go to https://myaccount.google.com/apppasswords")
                print("2. Generate a new App Password")
                print("3. Update sustainable_energy/email_config.py")
                return False
                
            except Exception as e:
                print(f"❌ ERROR: {str(e)}")
                return False
        else:
            print("⚠️  Email sending is DISABLED")
            print()
            print("To enable:")
            print("1. Open sustainable_energy/email_config.py")
            print("2. Set ENABLE_ACTUAL_EMAIL_SENDING = True")
            print()
            print("Email preview:")
            print("-" * 60)
            print(f"To: {recipient}")
            print(f"Subject: {subject}")
            print(body)
            print("-" * 60)
            return False
            
    except ImportError as e:
        print(f"❌ ERROR: Could not load email configuration")
        print(f"   {str(e)}")
        return False

if __name__ == '__main__':
    print()
    test_email_config()
    print()
    print("=" * 60)
