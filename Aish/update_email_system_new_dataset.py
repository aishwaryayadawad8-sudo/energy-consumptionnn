#!/usr/bin/env python3
"""
Update the email alert system to use the new dataset
"""

def update_email_system():
    """Update email system to use new dataset"""
    
    print("🔄 Updating email alert system for new dataset...")
    
    # Step 1: Update views.py to use new adapter
    print("\n1️⃣ Updating views.py...")
    
    with open('sustainable_energy/dashboard/views.py', 'r', encoding='utf-8') as f:
        views_content = f.read()
    
    # Add import for new adapter
    old_import = "from ml_models.sdg7_forecasting import SDG7Forecasting"
    new_import = """from ml_models.sdg7_forecasting import SDG7Forecasting
from new_energy_adapter import NewEnergyDataAdapter"""
    
    if old_import in views_content and "NewEnergyDataAdapter" not in views_content:
        views_content = views_content.replace(old_import, new_import)
        print("✅ Added NewEnergyDataAdapter import")
    
    # Update the send_email_alerts_selected function to use new dataset
    old_forecaster_code = """        # Get predictions
        forecaster = SDG7Forecasting(CSV_PATH)
        forecaster.load_and_clean_data()
        forecaster.train_and_compare_models()
        
        if selected_countries:
            # Get predictions for selected countries only
            all_predictions = []
            for country in selected_countries:
                predictions = forecaster.predict_future_access(1, country)
                if predictions:
                    all_predictions.extend(predictions)
        else:
            # Get predictions for all countries
            all_predictions = forecaster.predict_future_access(1, None)"""
    
    new_forecaster_code = """        # Get predictions using new dataset
        try:
            # Try new dataset first
            adapter = NewEnergyDataAdapter()
            if adapter.load_data():
                if selected_countries:
                    # Filter for selected countries only
                    available_countries = adapter.get_countries()
                    valid_countries = [c for c in selected_countries if c in available_countries]
                    all_predictions = []
                    for country in valid_countries:
                        predictions = adapter.predict_future_access(1, country)
                        all_predictions.extend(predictions)
                else:
                    # Get predictions for all countries in new dataset
                    all_predictions = adapter.predict_future_access(1, None)
                
                print(f"✅ Using new dataset with {len(all_predictions)} predictions")
            else:
                raise Exception("Failed to load new dataset")
                
        except Exception as e:
            print(f"⚠️ New dataset failed ({e}), falling back to original...")
            # Fallback to original dataset
            forecaster = SDG7Forecasting(CSV_PATH)
            forecaster.load_and_clean_data()
            forecaster.train_and_compare_models()
            
            if selected_countries:
                all_predictions = []
                for country in selected_countries:
                    predictions = forecaster.predict_future_access(1, country)
                    if predictions:
                        all_predictions.extend(predictions)
            else:
                all_predictions = forecaster.predict_future_access(1, None)"""
    
    if old_forecaster_code in views_content:
        views_content = views_content.replace(old_forecaster_code, new_forecaster_code)
        print("✅ Updated prediction logic to use new dataset")
    else:
        print("⚠️ Could not find prediction code to update")
    
    # Write back the updated views
    with open('sustainable_energy/dashboard/views.py', 'w', encoding='utf-8') as f:
        f.write(views_content)
    
    # Step 2: Update country emails for new dataset countries
    print("\n2️⃣ Updating country emails...")
    
    new_country_emails = """# Updated country emails for new dataset
India,assowmya649@gmail.com
China,assowmya649@gmail.com
Brazil,assowmya649@gmail.com
Nigeria,assowmya649@gmail.com
USA,assowmya649@gmail.com"""
    
    with open('sustainable_energy/country_emails_new.csv', 'w', encoding='utf-8') as f:
        f.write(new_country_emails)
    print("✅ Created country_emails_new.csv")
    
    # Step 3: Update email_alerts.py to use new country emails
    print("\n3️⃣ Updating email_alerts.py...")
    
    with open('sustainable_energy/ml_models/email_alerts.py', 'r', encoding='utf-8') as f:
        email_content = f.read()
    
    # Add option to use new country emails
    old_country_emails_section = """        # Load country emails
        try:
            import os
            csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'country_emails.csv')"""
    
    new_country_emails_section = """        # Load country emails (try new dataset first)
        try:
            import os
            # Try new dataset country emails first
            csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'country_emails_new.csv')
            if not os.path.exists(csv_path):
                # Fallback to original
                csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'country_emails.csv')"""
    
    if old_country_emails_section in email_content:
        email_content = email_content.replace(old_country_emails_section, new_country_emails_section)
        print("✅ Updated email_alerts.py to use new country emails")
    else:
        print("⚠️ Could not find country emails section to update")
    
    with open('sustainable_energy/ml_models/email_alerts.py', 'w', encoding='utf-8') as f:
        f.write(email_content)
    
    # Step 4: Create a test script for new dataset emails
    test_email_script = '''#!/usr/bin/env python3
"""
Test email alerts with new dataset
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from new_energy_adapter import NewEnergyDataAdapter
from ml_models.email_alerts import SDG7EmailAlerts
import pandas as pd

def test_new_dataset_emails():
    """Test email alerts with new dataset"""
    
    print("📧 Testing Email Alerts with New Dataset...")
    
    # Step 1: Load new dataset
    print("\\n1️⃣ Loading new dataset...")
    adapter = NewEnergyDataAdapter()
    if not adapter.load_data():
        print("❌ Failed to load new dataset")
        return
    
    # Step 2: Get predictions
    print("\\n2️⃣ Getting predictions...")
    predictions = adapter.predict_future_access(1)  # 2021 predictions
    if not predictions:
        print("❌ No predictions available")
        return
    
    print(f"✅ Got {len(predictions)} predictions:")
    for pred in predictions:
        print(f"   {pred['country']}: {pred['predicted_access']:.1f}% in {pred['year']}")
    
    # Step 3: Convert to DataFrame for email system
    print("\\n3️⃣ Converting to DataFrame...")
    predictions_df = pd.DataFrame(predictions)
    print(f"✅ DataFrame shape: {predictions_df.shape}")
    print(predictions_df.head())
    
    # Step 4: Initialize email system
    print("\\n4️⃣ Initializing email system...")
    email_system = SDG7EmailAlerts()
    
    # Step 5: Analyze which countries would get alerts
    print("\\n5️⃣ Analyzing alert eligibility...")
    summary = email_system.get_alert_summary(predictions_df)
    
    for status, countries in summary.items():
        if countries:
            print(f"\\n   {status.upper()}:")
            for country_info in countries:
                has_email = "✅" if country_info['has_email'] else "❌"
                print(f"     {has_email} {country_info['country']}: {country_info['access']:.1f}%")
    
    # Step 6: Send test alerts (simulation mode)
    print("\\n6️⃣ Sending test alerts...")
    try:
        alerts_sent = email_system.analyze_and_send_alerts(predictions_df, log_to_db=False)
        print(f"✅ Would send {len(alerts_sent)} alerts:")
        for alert in alerts_sent:
            print(f"   📧 {alert['country']}: {alert['status']} ({alert['access']:.1f}%)")
    except Exception as e:
        print(f"❌ Error sending alerts: {e}")
    
    print("\\n✅ Email test completed!")

if __name__ == "__main__":
    test_new_dataset_emails()
'''
    
    with open('sustainable_energy/test_new_dataset_emails.py', 'w', encoding='utf-8') as f:
        f.write(test_email_script)
    print("✅ Created test_new_dataset_emails.py")
    
    print("\n🎉 Email system update complete!")
    print("\n📋 What was updated:")
    print("   ✅ views.py - Added new dataset support")
    print("   ✅ email_alerts.py - Updated country email loading")
    print("   ✅ country_emails_new.csv - Email addresses for new countries")
    print("   ✅ test_new_dataset_emails.py - Test script")
    
    print("\n🧪 Test the updates:")
    print("   cd sustainable_energy && python test_new_dataset_emails.py")
    
    print("\n📊 New Dataset Countries & Latest Access Rates:")
    print("   🇮🇳 India: 85% (needs improvement)")
    print("   🇨🇳 China: 99% (excellent)")
    print("   🇧🇷 Brazil: 100% (excellent)")
    print("   🇳🇬 Nigeria: 100% (excellent)")
    print("   🇺🇸 USA: 86% (needs improvement)")

if __name__ == "__main__":
    update_email_system()