"""
Simple XGBoost Alert System Test (No Django)
Tests the core XGBoost functionality
"""

import sys
import os

# Add the sustainable_energy directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sustainable_energy'))

from ml_models.xgboost_alert_system import XGBoostAlertSystem
from ml_models.email_templates import EmailTemplates

def test_xgboost_system():
    """Test the XGBoost alert system"""
    print("\n" + "="*70)
    print("🧪 Testing XGBoost Alert System (Simple Test)")
    print("="*70)
    
    try:
        # Step 1: Initialize system
        print("\n1️⃣ Initializing XGBoost system...")
        csv_path = 'global-data-on-sustainable-energy.csv'
        
        if not os.path.exists(csv_path):
            print(f"❌ CSV file not found: {csv_path}")
            return False
        
        xgboost_system = XGBoostAlertSystem(csv_path)
        print("✅ System initialized")
        
        # Step 2: Train model
        print("\n2️⃣ Training XGBoost model...")
        xgboost_system.train_xgboost_model()
        print("✅ Model trained successfully")
        
        # Step 3: Get model info
        model_info = xgboost_system.get_model_info()
        print(f"\n📊 Model Information:")
        print(f"   Model Type: {model_info['model_type']}")
        print(f"   Features: {model_info['n_features']}")
        print(f"   Accuracy: {model_info['accuracy']:.2f}%")
        print(f"   MSE: {model_info['mse']:.4f}")
        
        # Step 4: Test prediction for Albania
        print("\n3️⃣ Testing prediction for Albania...")
        result = xgboost_system.predict_country_access('Albania')
        
        if result['found']:
            print(f"✅ Prediction successful:")
            print(f"   Country: {result['country']}")
            print(f"   Current Access: {result['current_access']:.2f}%")
            print(f"   Predicted Access: {result['predicted_access']:.2f}%")
            print(f"   Change: {result['change']:+.2f}%")
            print(f"   Status: {result['status']}")
            print(f"   Alert Type: {result['alert_type']}")
        else:
            print(f"❌ Country not found: {result['message']}")
            return False
        
        # Step 5: Get predictions for all countries
        print("\n4️⃣ Getting predictions for all countries...")
        predictions = xgboost_system.predict_all_countries()
        print(f"✅ Generated {len(predictions)} predictions")
        
        # Show sample predictions
        print("\n📊 Sample Predictions (First 10):")
        for i, pred in enumerate(predictions[:10], 1):
            print(f"   {i:2d}. {pred['country']:25s} - {pred['predicted_access']:5.1f}% ({pred['status']})")
        
        # Step 6: Analyze alert distribution
        print("\n5️⃣ Analyzing alert distribution...")
        alert_counts = {
            'critical': 0,
            'needs_improvement': 0,
            'good': 0,
            'excellent': 0
        }
        
        for pred in predictions:
            status = pred['status']
            alert_counts[status] += 1
        
        print(f"\n📊 Alert Distribution:")
        print(f"   🚨 Critical: {alert_counts['critical']}")
        print(f"   ⚠️  Needs Improvement: {alert_counts['needs_improvement']}")
        print(f"   ✅ Good: {alert_counts['good']}")
        print(f"   🎉 Excellent: {alert_counts['excellent']}")
        
        # Step 7: Test email template generation
        print("\n6️⃣ Testing email template generation...")
        
        # Test urgent template
        subject, body = EmailTemplates.get_template_by_type(
            'urgent', 'Albania', result['predicted_access'], 2024
        )
        print(f"✅ Urgent template generated:")
        print(f"   Subject: {subject[:60]}...")
        print(f"   Body length: {len(body)} characters")
        
        # Test all template types
        template_types = ['urgent', 'reminder', 'congratulations', 'status_update']
        print(f"\n📧 Testing all template types:")
        for template_type in template_types:
            subject, body = EmailTemplates.get_template_by_type(
                template_type, 'Albania', 85.5, 2024
            )
            print(f"   ✅ {template_type:20s} - {len(body):4d} chars")
        
        # Step 8: Check country emails
        print("\n7️⃣ Checking country emails...")
        import pandas as pd
        
        try:
            emails_df = pd.read_csv('country_emails.csv')
            print(f"✅ Country emails loaded: {len(emails_df)} countries")
            
            # Check if Albania has an email
            albania_email = emails_df[emails_df['Country'] == 'Albania']
            if not albania_email.empty:
                print(f"   Albania email: {albania_email['Email'].values[0]}")
            else:
                print(f"   ⚠️  Albania email not found")
            
            # Count how many predicted countries have emails
            countries_with_emails = 0
            for pred in predictions:
                country_email = emails_df[emails_df['Country'] == pred['country']]
                if not country_email.empty:
                    countries_with_emails += 1
            
            print(f"\n📧 Email Coverage:")
            print(f"   Total predictions: {len(predictions)}")
            print(f"   Countries with emails: {countries_with_emails}")
            print(f"   Coverage: {countries_with_emails/len(predictions)*100:.1f}%")
            
        except Exception as e:
            print(f"⚠️  Could not load country emails: {e}")
        
        print("\n" + "="*70)
        print("✅ ALL TESTS PASSED! XGBoost Alert System is working correctly.")
        print("="*70)
        
        print("\n📝 Next Steps:")
        print("   1. Start Django server: python sustainable_energy/manage.py runserver")
        print("   2. Send XGBoost alerts via API: POST to /api/send-xgboost-alerts/")
        print("   3. Or use the web interface at: http://localhost:8000/objective8/")
        
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
    
    if not success:
        print("\n❌ Please fix the errors above before using the system.")
        sys.exit(1)
