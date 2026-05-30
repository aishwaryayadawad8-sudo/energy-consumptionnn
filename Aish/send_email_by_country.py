"""
Send Email Alerts to Selected Countries
Uses the country_emails.csv file for official country email addresses
"""
import os
import sys
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sustainable_energy.config.settings')
django.setup()

import pandas as pd
from sustainable_energy.ml_models.email_alerts import SDG7EmailAlerts
from sustainable_energy.ml_models.sdg7_forecasting import SDG7Forecasting

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

def send_alerts_to_countries(country_list):
    """
    Send alerts to specific countries
    
    Args:
        country_list: List of country names to send alerts to
    """
    print("=" * 60)
    print("SDG 7 Email Alert System - Selected Countries")
    print("=" * 60)
    print()
    
    # Load country emails
    country_emails = load_country_emails()
    if not country_emails:
        print("❌ No country emails loaded. Please check country_emails.csv")
        return
    
    # Path to CSV
    csv_path = 'global-data-on-sustainable-energy.csv'
    
    print("📊 Loading data and training models...")
    forecaster = SDG7Forecasting(csv_path)
    forecaster.load_and_clean_data()
    forecaster.train_and_compare_models()
    
    print("🔮 Analyzing selected countries...")
    print()
    
    # Initialize email alert system
    alert_system = SDG7EmailAlerts()
    
    alerts_to_send = []
    
    for country in country_list:
        # Get prediction for this country
        predictions = forecaster.predict_future_access(1, country)
        
        if not predictions:
            print(f"⚠️  {country}: Not found in dataset")
            continue
        
        # Get the prediction
        year, country_name, predicted_access = predictions[0]
        
        # Get email address
        email = country_emails.get(country_name)
        if not email:
            print(f"⚠️  {country_name}: No email address found")
            continue
        
        # Classify status
        status, country_type = alert_system.classify_country_status(predicted_access)
        
        status_emoji = {
            'critical': '🚨',
            'needs_improvement': '⚠️',
            'good': '👍',
            'excellent': '🎉'
        }
        
        print(f"{status_emoji.get(status, '📧')} {country_name}")
        print(f"   Access: {predicted_access:.1f}%")
        print(f"   Status: {status.upper()}")
        print(f"   Email: {email}")
        print()
        
        alerts_to_send.append({
            'country': country_name,
            'email': email,
            'access': predicted_access,
            'status': status,
            'country_type': country_type,
            'year': year
        })
    
    if not alerts_to_send:
        print("❌ No valid countries to send alerts to")
        return
    
    print("=" * 60)
    print(f"📋 Summary: {len(alerts_to_send)} countries ready for alerts")
    print("=" * 60)
    print()
    
    # Ask for confirmation
    response = input("📤 Send email alerts to these countries? (yes/no): ").strip().lower()
    
    if response in ['yes', 'y']:
        print("\n📤 Sending emails...")
        print()
        
        sent_count = 0
        for alert in alerts_to_send:
            subject, body = alert_system.generate_email_content(
                alert['country'],
                alert['access'],
                alert['status'],
                alert['country_type'],
                alert['year']
            )
            
            success = alert_system.send_email(
                alert['email'],
                subject,
                body,
                country_name=alert['country']
            )
            
            if success:
                sent_count += 1
        
        print()
        print("=" * 60)
        print(f"✅ Successfully sent {sent_count}/{len(alerts_to_send)} emails!")
        print("=" * 60)
    else:
        print("\n❌ Email sending cancelled")
    
    print()

def main():
    print("\n🌍 SDG 7 Country Alert System")
    print("=" * 60)
    print()
    print("Send electricity access alerts to selected countries")
    print()
    
    # Option 1: Enter countries manually
    print("Option 1: Enter country names (comma-separated)")
    print("Example: India, Nigeria, Brazil")
    print()
    countries_input = input("Enter countries: ").strip()
    
    if countries_input:
        # Split by comma and clean up
        country_list = [c.strip() for c in countries_input.split(',') if c.strip()]
        
        if country_list:
            print()
            send_alerts_to_countries(country_list)
        else:
            print("❌ No countries entered")
    else:
        print("❌ No countries entered")

if __name__ == '__main__':
    main()
