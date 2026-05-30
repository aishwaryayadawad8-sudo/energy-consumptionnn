#!/usr/bin/env python3
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
    print("\n1️⃣ Loading new dataset...")
    adapter = NewEnergyDataAdapter()
    if not adapter.load_data():
        print("❌ Failed to load new dataset")
        return
    
    # Step 2: Get predictions
    print("\n2️⃣ Getting predictions...")
    predictions = adapter.predict_future_access(1)  # 2021 predictions
    if not predictions:
        print("❌ No predictions available")
        return
    
    print(f"✅ Got {len(predictions)} predictions:")
    for pred in predictions:
        print(f"   {pred['country']}: {pred['predicted_access']:.1f}% in {pred['year']}")
    
    # Step 3: Convert to DataFrame for email system
    print("\n3️⃣ Converting to DataFrame...")
    predictions_df = pd.DataFrame(predictions)
    print(f"✅ DataFrame shape: {predictions_df.shape}")
    print(predictions_df.head())
    
    # Step 4: Initialize email system
    print("\n4️⃣ Initializing email system...")
    email_system = SDG7EmailAlerts()
    
    # Step 5: Analyze which countries would get alerts
    print("\n5️⃣ Analyzing alert eligibility...")
    summary = email_system.get_alert_summary(predictions_df)
    
    for status, countries in summary.items():
        if countries:
            print(f"\n   {status.upper()}:")
            for country_info in countries:
                has_email = "✅" if country_info['has_email'] else "❌"
                print(f"     {has_email} {country_info['country']}: {country_info['access']:.1f}%")
    
    # Step 6: Send test alerts (simulation mode)
    print("\n6️⃣ Sending test alerts...")
    try:
        alerts_sent = email_system.analyze_and_send_alerts(predictions_df, log_to_db=False)
        print(f"✅ Would send {len(alerts_sent)} alerts:")
        for alert in alerts_sent:
            print(f"   📧 {alert['country']}: {alert['status']} ({alert['access']:.1f}%)")
    except Exception as e:
        print(f"❌ Error sending alerts: {e}")
    
    print("\n✅ Email test completed!")

if __name__ == "__main__":
    test_new_dataset_emails()
