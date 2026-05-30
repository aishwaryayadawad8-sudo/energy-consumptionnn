"""
Send Email Alert to a Specific Country
Simple script to send electricity access alerts to any country
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

def send_alert_to_country(country_name, recipient_email):
    """
    Send an alert email to a specific country
    
    Args:
        country_name: Name of the country (e.g., 'India', 'Nigeria')
        recipient_email: Email address to send the alert to
    """
    print("=" * 60)
    print(f"Sending Alert to {country_name}")
    print("=" * 60)
    print()
    
    # Path to CSV
    csv_path = 'global-data-on-sustainable-energy.csv'
    
    print("📊 Loading data and analyzing country...")
    forecaster = SDG7Forecasting(csv_path)
    forecaster.load_and_clean_data()
    forecaster.train_and_compare_models()
    
    # Get prediction for the specific country
    print(f"🔮 Predicting electricity access for {country_name}...")
    predictions = forecaster.predict_future_access(1, country_name)
    
    if not predictions:
        print(f"❌ Country '{country_name}' not found in dataset")
        print("\nAvailable countries:")
        df = pd.read_csv(csv_path)
        countries = sorted(df['Entity'].unique())
        for i, c in enumerate(countries[:20], 1):
            print(f"  {i}. {c}")
        if len(countries) > 20:
            print(f"  ... and {len(countries) - 20} more")
        return
    
    # Get the prediction
    year, country, predicted_access = predictions[0]
    
    print(f"\n📊 Analysis Results:")
    print(f"   Country: {country}")
    print(f"   Predicted Access: {predicted_access:.1f}%")
    print(f"   Year: {year}")
    
    # Classify status
    alert_system = SDG7EmailAlerts()
    status, country_type = alert_system.classify_country_status(predicted_access)
    
    status_emoji = {
        'critical': '🚨 CRITICAL',
        'needs_improvement': '⚠️ NEEDS IMPROVEMENT',
        'good': '👍 GOOD',
        'excellent': '🎉 EXCELLENT'
    }
    
    print(f"   Status: {status_emoji.get(status, status.upper())}")
    print(f"   Classification: {country_type} Country")
    print()
    
    # Generate email content
    subject, body = alert_system.generate_email_content(
        country, predicted_access, status, country_type, year
    )
    
    print("📧 Email Preview:")
    print("-" * 60)
    print(f"To: {recipient_email}")
    print(f"Subject: {subject}")
    print("-" * 60)
    print(body[:500] + "..." if len(body) > 500 else body)
    print("-" * 60)
    print()
    
    # Ask for confirmation
    response = input("📤 Send this email? (yes/no): ").strip().lower()
    
    if response in ['yes', 'y']:
        print("\n📤 Sending email...")
        success = alert_system.send_email(recipient_email, subject, body, country_name=country)
        
        if success:
            print(f"\n✅ Email sent successfully to {recipient_email}!")
            print(f"   Country: {country}")
            print(f"   Status: {status}")
            print(f"   Access: {predicted_access:.1f}%")
        else:
            print(f"\n❌ Failed to send email")
            print("\nTroubleshooting:")
            print("1. Check your email configuration in sustainable_energy/email_config.py")
            print("2. Make sure ENABLE_ACTUAL_EMAIL_SENDING = True")
            print("3. Verify your Gmail App Password is correct")
    else:
        print("\n❌ Email sending cancelled")
    
    print("\n" + "=" * 60)

def main():
    print("\n🌍 SDG 7 Country Alert System")
    print("=" * 60)
    print()
    
    # Get country name
    country = input("Enter country name (e.g., India, Nigeria, Brazil): ").strip()
    
    if not country:
        print("❌ Country name is required")
        return
    
    # Get email address (default to your email)
    default_email = "electricity.prediction2000@gmail.com"
    email = input(f"Enter recipient email [{default_email}]: ").strip()
    
    if not email:
        email = default_email
    
    print()
    send_alert_to_country(country, email)

if __name__ == '__main__':
    main()
