"""
Simple Email Alert System - No Django Required
Send electricity access alerts to selected countries
"""
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Email Configuration
SENDER_EMAIL = 'electricity.prediction2000@gmail.com'
SENDER_PASSWORD = 'your-app-password'  # Replace with your Gmail App Password
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Settings
TESTING_MODE = True  # Sends to your email instead of country emails
ENABLE_SENDING = False  # Set to True to actually send emails

def load_country_emails():
    """Load country email addresses from CSV"""
    try:
        df = pd.read_csv('country_emails.csv')
        emails = dict(zip(df['Country'], df['Email']))
        print(f"✅ Loaded {len(emails)} country email addresses")
        return emails
    except Exception as e:
        print(f"❌ Error loading country_emails.csv: {e}")
        return {}

def predict_electricity_access(country_name):
    """Predict electricity access for a country"""
    try:
        # Load data
        df = pd.read_csv('global-data-on-sustainable-energy.csv')
        
        # Try exact match first
        country_data = df[df['Entity'] == country_name].copy()
        
        # If not found, try case-insensitive match
        if country_data.empty:
            country_data = df[df['Entity'].str.lower() == country_name.lower()].copy()
            if not country_data.empty:
                country_name = country_data.iloc[0]['Entity']  # Use correct case
        
        if country_data.empty:
            return None
        
        # Get the most recent access percentage
        country_data = country_data.sort_values('Year', ascending=False)
        latest = country_data.iloc[0]
        
        access = latest.get('Access to electricity (% of population)', 0)
        year = latest.get('Year', 2020)
        
        return {
            'country': country_name,
            'access': float(access),
            'year': int(year)
        }
        
    except Exception as e:
        print(f"❌ Error analyzing {country_name}: {e}")
        return None

def classify_status(access):
    """Classify country status based on electricity access"""
    if access < 50:
        return 'critical', 'Developing'
    elif access < 75:
        return 'needs_improvement', 'Developing'
    elif access < 95:
        return 'good', 'Developing'
    else:
        return 'excellent', 'Developed'

def generate_email_content(country, access, status, country_type, year):
    """Generate email content based on country status"""
    
    if status == 'critical':
        subject = f"🚨 URGENT: Critical Electricity Access Alert for {country}"
        body = f"""Dear Energy Ministry of {country},

CRITICAL ALERT: SDG 7 Monitoring System

Our AI-powered monitoring system has identified that {country} has critically low electricity access:

📊 Current Status:
- Electricity Access: {access:.1f}%
- Classification: {country_type} Country
- Status: CRITICAL - Immediate Action Required
- Year: {year}

⚠️ IMMEDIATE ACTION PLAN:

1. EMERGENCY MEASURES:
   - Deploy mobile solar units to remote areas
   - Establish emergency power distribution centers
   - Partner with international energy organizations

2. SHORT-TERM (0-2 years):
   - Accelerate grid expansion to underserved regions
   - Implement off-grid solar solutions
   - Provide subsidies for household solar systems

3. MEDIUM-TERM (2-5 years):
   - Invest in renewable energy infrastructure
   - Build mini-grid systems for rural communities
   - Train local technicians for maintenance

Best regards,
SDG 7 Global Monitoring System
"""
    
    elif status == 'needs_improvement':
        subject = f"⚠️ Action Required: Electricity Access Below Target for {country}"
        body = f"""Dear Energy Ministry of {country},

SDG 7 Progress Alert

Our monitoring system shows {country} needs to accelerate electricity access improvements:

📊 Current Status:
- Electricity Access: {access:.1f}%
- Classification: {country_type} Country
- Status: Below SDG 7 Target
- Year: {year}

💡 RECOMMENDED ACTIONS:

1. Expand grid infrastructure to rural areas
2. Implement renewable energy projects (solar, wind)
3. Provide financing for household connections
4. Partner with private sector for last-mile connectivity

📈 Target: Achieve 95%+ access by 2030

Best regards,
SDG 7 Global Monitoring System
"""
    
    elif status == 'excellent':
        subject = f"🎉 Congratulations: {country} Achieves Excellent Electricity Access!"
        body = f"""Dear Energy Ministry of {country},

CONGRATULATIONS! 🎉

We are pleased to inform you that {country} has achieved excellent electricity access:

📊 Current Status:
- Electricity Access: {access:.1f}%
- Classification: {country_type} Country
- Status: EXCELLENT - SDG 7 Target Achieved!
- Year: {year}

🌟 ACHIEVEMENTS:
- Universal electricity access achieved
- SDG 7 target met ahead of schedule
- Model for other countries to follow

Best regards,
SDG 7 Global Monitoring System
"""
    
    else:  # good
        subject = f"✅ Good Progress: {country} on Track for SDG 7"
        body = f"""Dear Energy Ministry of {country},

SDG 7 Progress Update

{country} is making good progress toward universal electricity access:

📊 Current Status:
- Electricity Access: {access:.1f}%
- Classification: {country_type} Country
- Status: Good Progress
- Year: {year}

👍 Keep up the excellent work! Continue current efforts to reach 100% access.

Best regards,
SDG 7 Global Monitoring System
"""
    
    return subject, body

def send_email(to_email, subject, body, country_name):
    """Send email alert"""
    try:
        # In testing mode, send to your email
        actual_recipient = to_email
        if TESTING_MODE:
            to_email = SENDER_EMAIL
            subject = f"[TEST - For: {country_name}] {subject}"
            body = f"ORIGINAL RECIPIENT: {actual_recipient}\nCOUNTRY: {country_name}\n\n{'='*60}\n\n{body}"
        
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email (only if enabled)
        if ENABLE_SENDING:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            server.quit()
            print(f"✅ Email SENT to {to_email}")
        else:
            print(f"✅ Email SIMULATED to {to_email}")
        
        print(f"   Subject: {subject}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send email: {str(e)}")
        return False

def main():
    print("\n🌍 SDG 7 Country Alert System")
    print("=" * 60)
    print()
    
    # Load country emails
    country_emails = load_country_emails()
    if not country_emails:
        print("❌ Cannot proceed without country emails")
        return
    
    print()
    print("Send electricity access alerts to selected countries")
    print()
    print("Example: India, Nigeria, Brazil")
    print()
    
    # Get countries from user
    countries_input = input("Enter countries (comma-separated): ").strip()
    
    if not countries_input:
        print("❌ No countries entered")
        return
    
    # Parse countries
    country_list = [c.strip() for c in countries_input.split(',') if c.strip()]
    
    if not country_list:
        print("❌ No valid countries entered")
        return
    
    print()
    print("=" * 60)
    print("Analyzing Countries")
    print("=" * 60)
    print()
    
    alerts_to_send = []
    
    for country in country_list:
        # Analyze country
        result = predict_electricity_access(country)
        
        if not result:
            print(f"⚠️  {country}: Not found in dataset")
            continue
        
        # Get email
        email = country_emails.get(result['country'])
        if not email:
            print(f"⚠️  {result['country']}: No email address found")
            continue
        
        # Classify
        status, country_type = classify_status(result['access'])
        
        status_emoji = {
            'critical': '🚨',
            'needs_improvement': '⚠️',
            'good': '👍',
            'excellent': '🎉'
        }
        
        print(f"{status_emoji.get(status, '📧')} {result['country']}")
        print(f"   Access: {result['access']:.1f}%")
        print(f"   Status: {status.upper()}")
        print(f"   Email: {email}")
        print()
        
        alerts_to_send.append({
            'country': result['country'],
            'email': email,
            'access': result['access'],
            'status': status,
            'country_type': country_type,
            'year': result['year']
        })
    
    if not alerts_to_send:
        print("❌ No valid countries to send alerts to")
        return
    
    print("=" * 60)
    print(f"📋 Summary: {len(alerts_to_send)} countries ready for alerts")
    print("=" * 60)
    print()
    
    if not ENABLE_SENDING:
        print("⚠️  NOTE: Email sending is DISABLED (simulation mode)")
        print("   To enable: Edit this script and set ENABLE_SENDING = True")
        print()
    
    if TESTING_MODE:
        print("⚠️  NOTE: TESTING MODE - All emails will go to your email")
        print(f"   ({SENDER_EMAIL})")
        print()
    
    # Ask for confirmation
    response = input("📤 Send email alerts? (yes/no): ").strip().lower()
    
    if response in ['yes', 'y']:
        print("\n📤 Sending emails...")
        print()
        
        sent_count = 0
        for alert in alerts_to_send:
            subject, body = generate_email_content(
                alert['country'],
                alert['access'],
                alert['status'],
                alert['country_type'],
                alert['year']
            )
            
            success = send_email(
                alert['email'],
                subject,
                body,
                alert['country']
            )
            
            if success:
                sent_count += 1
        
        print()
        print("=" * 60)
        print(f"✅ Successfully processed {sent_count}/{len(alerts_to_send)} emails!")
        print("=" * 60)
    else:
        print("\n❌ Email sending cancelled")
    
    print()

if __name__ == '__main__':
    main()
