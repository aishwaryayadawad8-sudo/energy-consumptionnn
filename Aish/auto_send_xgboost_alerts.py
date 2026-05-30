"""
Automatic XGBoost Alert System
Sends alerts automatically to all countries based on XGBoost predictions
Run this script and it will automatically send alerts without any manual input
"""

import sys
import os
import time
from datetime import datetime

# Add the sustainable_energy directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sustainable_energy'))

from ml_models.xgboost_alert_system import XGBoostAlertSystem
from ml_models.email_alerts import SDG7EmailAlerts
from ml_models.email_templates import EmailTemplates
import pandas as pd


def send_automatic_alerts():
    """
    Automatically send XGBoost alerts to all countries
    No user input required - fully automatic
    """
    print("\n" + "="*70)
    print("🤖 AUTOMATIC XGBoost Alert System")
    print("="*70)
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    
    try:
        # Step 1: Initialize XGBoost system
        print("\n1️⃣ Initializing XGBoost system...")
        csv_path = 'global-data-on-sustainable-energy.csv'
        
        if not os.path.exists(csv_path):
            print(f"❌ CSV file not found: {csv_path}")
            return False
        
        xgboost_system = XGBoostAlertSystem(csv_path)
        print("✅ System initialized")
        
        # Step 2: Train XGBoost model
        print("\n2️⃣ Training XGBoost model automatically...")
        xgboost_system.train_xgboost_model()
        
        model_info = xgboost_system.get_model_info()
        print(f"✅ Model trained with {model_info['accuracy']:.2f}% accuracy")
        
        # Step 3: Get predictions for all countries
        print("\n3️⃣ Generating predictions for all countries...")
        predictions = xgboost_system.predict_all_countries()
        print(f"✅ Generated {len(predictions)} predictions")
        
        # Step 4: Load country emails
        print("\n4️⃣ Loading country email addresses...")
        emails_df = pd.read_csv('country_emails.csv')
        country_emails = dict(zip(emails_df['Country'], emails_df['Email']))
        print(f"✅ Loaded {len(country_emails)} email addresses")
        
        # Step 5: Initialize email system
        print("\n5️⃣ Initializing email system...")
        email_system = SDG7EmailAlerts()
        print("✅ Email system ready")
        
        # Step 6: Automatically send alerts
        print("\n6️⃣ Automatically sending alerts...")
        print("="*70)
        
        alerts_sent = []
        alerts_by_type = {
            'critical': 0,
            'needs_improvement': 0,
            'good': 0,
            'excellent': 0
        }
        
        for i, pred in enumerate(predictions, 1):
            country = pred['country']
            access = pred['predicted_access']
            status = pred['status']
            alert_type = pred['alert_type']
            year = pred['year']
            
            # Count by type
            alerts_by_type[status] += 1
            
            # Check if we have email for this country
            if country not in country_emails:
                print(f"   ⚠️  [{i}/{len(predictions)}] {country:25s} - No email address")
                continue
            
            # Only send for critical, needs_improvement, or excellent
            if status in ['critical', 'needs_improvement', 'excellent']:
                email_address = country_emails[country]
                
                # Generate email content
                subject, body = EmailTemplates.get_template_by_type(
                    alert_type, country, access, year
                )
                
                # Send email automatically
                success = email_system.send_email(
                    to_email=email_address,
                    subject=subject,
                    body=body,
                    country_name=country,
                    log_to_db=False
                )
                
                if success:
                    status_icon = {
                        'critical': '🚨',
                        'needs_improvement': '⚠️',
                        'excellent': '🎉'
                    }.get(status, '📊')
                    
                    print(f"   ✅ [{i}/{len(predictions)}] {status_icon} {country:25s} - Alert sent ({status})")
                    
                    alerts_sent.append({
                        'country': country,
                        'email': email_address,
                        'status': status,
                        'alert_type': alert_type,
                        'access': float(access),
                        'year': year,
                        'subject': subject
                    })
                else:
                    print(f"   ❌ [{i}/{len(predictions)}] {country:25s} - Failed to send")
            else:
                # Good status - optional alert
                print(f"   ℹ️  [{i}/{len(predictions)}] {country:25s} - Good status (no alert needed)")
        
        # Step 7: Summary
        print("\n" + "="*70)
        print("📊 AUTOMATIC ALERT SUMMARY")
        print("="*70)
        print(f"\n✅ Alerts sent successfully: {len(alerts_sent)}")
        print(f"\n📊 Alert Distribution:")
        print(f"   🚨 Critical:          {alerts_by_type['critical']:3d} countries")
        print(f"   ⚠️  Needs Improvement: {alerts_by_type['needs_improvement']:3d} countries")
        print(f"   ✅ Good:              {alerts_by_type['good']:3d} countries")
        print(f"   🎉 Excellent:         {alerts_by_type['excellent']:3d} countries")
        
        print(f"\n🎯 Model Performance:")
        print(f"   Accuracy: {model_info['accuracy']:.2f}%")
        print(f"   MSE: {model_info['mse']:.2f}")
        print(f"   Features: {model_info['n_features']}")
        
        print(f"\n⏰ Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*70)
        
        # Show sample alerts sent
        if alerts_sent:
            print(f"\n📧 Sample Alerts Sent (First 10):")
            for i, alert in enumerate(alerts_sent[:10], 1):
                status_icon = {
                    'critical': '🚨',
                    'needs_improvement': '⚠️',
                    'excellent': '🎉'
                }.get(alert['status'], '📊')
                print(f"   {i:2d}. {status_icon} {alert['country']:25s} - {alert['access']:5.1f}% ({alert['status']})")
            
            if len(alerts_sent) > 10:
                print(f"   ... and {len(alerts_sent) - 10} more alerts")
        
        print("\n✅ Automatic alert system completed successfully!")
        print("="*70 + "\n")
        
        return True
        
    except Exception as e:
        print("\n" + "="*70)
        print("❌ ERROR in automatic alert system:")
        print("="*70)
        import traceback
        print(traceback.format_exc())
        print("="*70)
        return False


if __name__ == '__main__':
    print("\n" + "="*70)
    print("🚀 Starting Automatic XGBoost Alert System")
    print("="*70)
    print("\n⚡ This script will automatically:")
    print("   1. Train XGBoost model")
    print("   2. Predict electricity access for all countries")
    print("   3. Send alerts automatically (no user input needed)")
    print("   4. Show summary of alerts sent")
    print("\n⏳ Please wait while the system runs automatically...")
    print("="*70)
    
    # Wait 2 seconds to let user read the message
    time.sleep(2)
    
    # Run automatic alert system
    success = send_automatic_alerts()
    
    if success:
        print("\n🎉 SUCCESS! All alerts have been sent automatically.")
        print("\n📝 Next Steps:")
        print("   • Check your email inbox for sent alerts")
        print("   • View logs at: http://localhost:8000/email-logs/")
        print("   • Run this script again anytime to send new alerts")
    else:
        print("\n❌ Automatic alert system encountered an error.")
        print("   Please check the error message above.")
    
    sys.exit(0 if success else 1)
