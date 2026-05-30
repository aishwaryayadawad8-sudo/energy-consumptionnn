"""
Send Test Email to Albania
Simple script to test real email sending
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print("\n" + "="*70)
print("📧 Sending Test Email to Albania (tejaswini.y2004teju@gmail.com)")
print("="*70)

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'tejaswini.y2004teju@gmail.com'
sender_password = 'unbkroqmxrlzhpxb'  # Your App Password (spaces removed)
recipient_email = 'tejaswini.y2004teju@gmail.com'

# Email content
subject = "🎉 Test: XGBoost Alert System for Albania"
body = """
Dear Energy Ministry of Albania,

This is a TEST email from the XGBoost Alert System.

If you receive this email, the system is working correctly!

📊 Albania Status:
- Country: Albania
- Email: assowmya649@gmail.com
- System: XGBoost ML Model (99.16% accuracy)
- Status: READY TO SEND REAL ALERTS

✅ Next Steps:
1. This confirms email delivery is working
2. You can now receive automatic alerts
3. Run: python send_xgboost_alert_to_country.py Albania

Best regards,
SDG 7 Monitoring System
"""

try:
    print("\n1️⃣ Creating email message...")
    msg = MIMEMultipart()
    msg['From'] = f"SDG 7 Monitoring System <{sender_email}>"
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    print("✅ Email message created")
    
    print("\n2️⃣ Connecting to Gmail SMTP server...")
    server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
    print("✅ Connected to Gmail")
    
    print("\n3️⃣ Starting TLS encryption...")
    server.starttls()
    print("✅ TLS started")
    
    print("\n4️⃣ Logging in with App Password...")
    server.login(sender_email, sender_password)
    print("✅ Login successful")
    
    print("\n5️⃣ Sending email...")
    server.send_message(msg)
    print("✅ Email sent successfully!")
    
    print("\n6️⃣ Closing connection...")
    server.quit()
    print("✅ Connection closed")
    
    print("\n" + "="*70)
    print("🎉 SUCCESS! Email sent to tejaswini.y2004teju@gmail.com")
    print("="*70)
    print("\n📧 Check your inbox:")
    print("   Email: tejaswini.y2004teju@gmail.com")
    print("   Subject: 🎉 Test: XGBoost Alert System for Albania")
    print("\n⚠️  If not in inbox, check SPAM folder!")
    print("="*70 + "\n")
    
except smtplib.SMTPAuthenticationError as e:
    print("\n❌ Authentication Error!")
    print(f"   Error: {e}")
    print("\n🔧 Possible solutions:")
    print("   1. Check if App Password is correct: unbk roqm xrlz hpxb")
    print("   2. Make sure 2-Step Verification is enabled")
    print("   3. Try generating a new App Password")
    print("   4. Visit: https://myaccount.google.com/apppasswords")
    
except smtplib.SMTPException as e:
    print("\n❌ SMTP Error!")
    print(f"   Error: {e}")
    print("\n🔧 Possible solutions:")
    print("   1. Check internet connection")
    print("   2. Check if Gmail is blocking the connection")
    print("   3. Try again in a few minutes")
    
except Exception as e:
    print("\n❌ Unexpected Error!")
    print(f"   Error: {e}")
    import traceback
    traceback.print_exc()
