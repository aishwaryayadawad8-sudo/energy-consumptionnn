"""
Send XGBoost Alert to a Specific Country
This script sends an automatic alert to a selected country using XGBoost predictions
"""

import sys
import os

# Add the sustainable_energy directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sustainable_energy'))

from ml_models.xgboost_alert_system import XGBoostAlertSystem
from ml_models.email_alerts import SDG7EmailAlerts
from ml_models.email_templates import EmailTemplates
import pandas as pd


def send_alert_to_country(country_name):
    """
    Send XGBoost-based alert to a specific country
    
    Args:
        country_name: Name of the country (e.g., 'Albania')
    """
    print("\n" + "="*70)
    print(f"📧 Sending XGBoost Alert to {country_name}")
    print("="*70)
    
    try:
        # Step 1: Initialize XGBoost system
        print("\n1️⃣ Initializing XGBoost system...")
        csv_path = 'global-data-on-sustainable-energy.csv'
        xgboost_system = XGBoostAlertSystem(csv_path)
        
        # Step 2: Train model
        print("\n2️⃣ Training XGBoost model...")
        xgboost_system.train_xgboost_model()
        
        # Step 3: Get prediction for the country
        print(f"\n3️⃣ Getting prediction for {country_name}...")
        prediction = xgboost_system.predict_country_access(country_name)
        
        if not prediction['found']:
            print(f"❌ Country '{country_name}' not found in dataset")
            print(f"   {prediction['message']}")
            return False
        
        print(f"✅ Prediction generated:")
        print(f"   Current Access: {prediction['current_access']:.2f}%")
        print(f"   Predicted Access: {prediction['predicted_access']:.2f}%")
        print(f"   Change: {prediction['change']:+.2f}%")
        print(f"   Status: {prediction['status']}")
        print(f"   Alert Type: {prediction['alert_type']}")
        
        # Step 4: Check if country has email
        print(f"\n4️⃣ Checking email address for {country_name}...")
        emails_df = pd.read_csv('country_emails.csv')
        country_email_row = emails_df[emails_df['Country'] == country_name]
        
        if country_email_row.empty:
            print(f"❌ No email address found for {country_name}")
            print(f"   Please add email to country_emails.csv")
            return False
        
        email_address = country_email_row['Email'].values[0]
        print(f"✅ Email found: {email_address}")
        
        # Step 5: Generate email content
        print(f"\n5️⃣ Generating email content...")
        subject, body = EmailTemplates.get_template_by_type(
            prediction['alert_type'],
            country_name,
            prediction['predicted_access'],
            prediction['year']
        )
        
        print(f"✅ Email content generated:")
        print(f"   Template: {prediction['alert_type']}")
        print(f"   Subject: {subject[:60]}...")
        print(f"   Body length: {len(body)} characters")
        
        # Step 6: Send email
        print(f"\n6️⃣ Sending email to {country_name}...")
        email_system = SDG7EmailAlerts()
        
        success = email_system.send_email(
            to_email=email_address,
            subject=subject,
            body=body,
            country_name=country_name,
            log_to_db=False  # Set to True if you want to log to database
        )
        
        if success:
            print(f"✅ Email sent successfully to {email_address}")
            print(f"\n📧 Email Details:")
            print(f"   To: {email_address}")
            print(f"   Subject: {subject}")
            print(f"   Status: {prediction['status']}")
            print(f"   Access: {prediction['predicted_access']:.2f}%")
            print(f"   Model: XGBoost (Accuracy: {prediction['model_accuracy']:.2f}%)")
        else:
            print(f"❌ Failed to send email")
            return False
        
        print("\n" + "="*70)
        print(f"✅ Alert sent successfully to {country_name}!")
        print("="*70)
        
        return True
        
    except Exception as e:
        print("\n" + "="*70)
        print("❌ ERROR:")
        print("="*70)
        import traceback
        print(traceback.format_exc())
        print("="*70)
        return False


def list_available_countries():
    """List all available countries"""
    try:
        emails_df = pd.read_csv('country_emails.csv')
        countries = sorted(emails_df['Country'].tolist())
        
        print("\n" + "="*70)
        print(f"📋 Available Countries ({len(countries)} total)")
        print("="*70)
        
        # Print in columns
        for i in range(0, len(countries), 3):
            row = countries[i:i+3]
            print("   " + "".join(f"{c:25s}" for c in row))
        
        print("="*70)
        
    except Exception as e:
        print(f"❌ Error loading countries: {e}")


if __name__ == '__main__':
    print("\n" + "="*70)
    print("🚀 XGBoost Alert System - Send Alert to Specific Country")
    print("="*70)
    
    # Check if country name is provided
    if len(sys.argv) > 1:
        country_name = ' '.join(sys.argv[1:])
        send_alert_to_country(country_name)
    else:
        print("\n📝 Usage:")
        print("   python send_xgboost_alert_to_country.py <Country Name>")
        print("\n📝 Examples:")
        print("   python send_xgboost_alert_to_country.py Albania")
        print("   python send_xgboost_alert_to_country.py Kenya")
        print("   python send_xgboost_alert_to_country.py \"South Africa\"")
        
        # Ask user for country name
        print("\n" + "="*70)
        choice = input("\nWould you like to see available countries? (y/n): ").strip().lower()
        
        if choice == 'y':
            list_available_countries()
        
        print("\n" + "="*70)
        country_name = input("\nEnter country name (or press Enter to exit): ").strip()
        
        if country_name:
            send_alert_to_country(country_name)
        else:
            print("\n👋 Goodbye!")
