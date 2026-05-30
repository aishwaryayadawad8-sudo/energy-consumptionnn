"""
Test XGBoost Alert System
This script tests the XGBoost alert system to identify any errors
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sustainable_energy.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from sustainable_energy.ml_models.xgboost_alert_system import XGBoostAlertSystem
from sustainable_energy.ml_models.email_alerts import SDG7EmailAlerts
from sustainable_energy.ml_models.email_templates import EmailTemplates

def test_xgboost_system():
    """Test the XGBoost alert system"""
    print("\n" + "="*70)
    print("🧪 Testing XGBoost Alert System")
    print("="*70)
    
    try:
        # Step 1: Initialize system
        print("\n1️⃣ Initializing XGBoost system...")
        csv_path = 'global-data-on-sustainable-energy.csv'
        xgboost_system = XGBoostAlertSystem(csv_path)
        print("✅ System initialized")
        
        # Step 2: Train model
        print("\n2️⃣ Training XGBoost model...")
        xgboost_system.train_xgboost_model()
        print("✅ Model trained successfully")
        
        # Step 3: Test prediction for a specific country
        print("\n3️⃣ Testing prediction for Albania...")
        result = xgboost_system.predict_country_access('Albania')
        
        if result['found']:
            print(f"✅ Prediction successful:")
            print(f"   Country: {result['country']}")
            print(f"   Current Access: {result['current_access']:.2f}%")
            print(f"   Predicted Access: {result['predicted_access']:.2f}%")
            print(f"   Status: {result['status']}")
            print(f"   Alert Type: {result['alert_type']}")
        else:
            print(f"❌ Country not found: {result['message']}")
        
        # Step 4: Get predictions for all countries
        print("\n4️⃣ Getting predictions for all countries...")
        predictions = xgboost_system.predict_all_countries()
        print(f"✅ Generated {len(predictions)} predictions")
        
        # Show sample predictions
        print("\n📊 Sample Predictions:")
        for pred in predictions[:5]:
            print(f"   {pred['country']:20s} - {pred['predicted_access']:5.1f}% ({pred['status']})")
        
        # Step 5: Test email template generation
        print("\n5️⃣ Testing email template generation...")
        subject, body = EmailTemplates.get_template_by_type(
            'urgent', 'Albania', 85.5, 2024
        )
        print(f"✅ Template generated:")
        print(f"   Subject: {subject[:60]}...")
        
        # Step 6: Check email system
        print("\n6️⃣ Checking email system...")
        email_system = SDG7EmailAlerts()
        print(f"✅ Email system initialized")
        print(f"   SMTP Server: {email_system.smtp_server}")
        print(f"   Sender Email: {email_system.sender_email}")
        print(f"   Countries with emails: {len(email_system.COUNTRY_EMAILS)}")
        
        # Check if Albania has an email
        if 'Albania' in email_system.COUNTRY_EMAILS:
            print(f"   Albania email: {email_system.COUNTRY_EMAILS['Albania']}")
        else:
            print(f"   ⚠️  Albania email not found in country_emails.csv")
        
        # Step 7: Count how many countries would receive alerts
        print("\n7️⃣ Analyzing alert distribution...")
        alert_counts = {
            'critical': 0,
            'needs_improvement': 0,
            'good': 0,
            'excellent': 0
        }
        
        countries_with_emails = 0
        countries_to_alert = []
        
        for pred in predictions:
            status = pred['status']
            alert_counts[status] += 1
            
            country = pred['country']
            if country in email_system.COUNTRY_EMAILS:
                countries_with_emails += 1
                if status in ['critical', 'needs_improvement', 'excellent']:
                    countries_to_alert.append({
                        'country': country,
                        'status': status,
                        'access': pred['predicted_access']
                    })
        
        print(f"\n📊 Alert Distribution:")
        print(f"   Critical: {alert_counts['critical']}")
        print(f"   Needs Improvement: {alert_counts['needs_improvement']}")
        print(f"   Good: {alert_counts['good']}")
        print(f"   Excellent: {alert_counts['excellent']}")
        print(f"\n📧 Email Coverage:")
        print(f"   Total countries: {len(predictions)}")
        print(f"   Countries with emails: {countries_with_emails}")
        print(f"   Countries to receive alerts: {len(countries_to_alert)}")
        
        # Show countries that will receive alerts
        print(f"\n📬 Countries that will receive alerts:")
        for item in countries_to_alert[:10]:
            print(f"   {item['country']:20s} - {item['access']:5.1f}% ({item['status']})")
        if len(countries_to_alert) > 10:
            print(f"   ... and {len(countries_to_alert) - 10} more")
        
        print("\n" + "="*70)
        print("✅ All tests passed! XGBoost Alert System is working correctly.")
        print("="*70)
        
        return True
        
    except Exception as e:
        print("\n" + "="*70)
        print("❌ ERROR DETECTED:")
        print("="*70)
        import traceback
        print(traceback.format_exc())
        print("="*70)
        return False


if __name__ == '__main__':
    success = test_xgboost_system()
    
    if success:
        print("\n✅ You can now use the XGBoost alert system!")
        print("\n📝 To send alerts to a specific country:")
        print("   Visit: http://localhost:8000/send-custom-alert/")
        print("\n📝 To send automatic XGBoost alerts:")
        print("   Make a POST request to: http://localhost:8000/api/send-xgboost-alerts/")
    else:
        print("\n❌ Please fix the errors above before using the system.")
