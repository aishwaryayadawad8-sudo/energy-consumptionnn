"""
Send Email Alerts to Countries Based on Electricity Access
Run this script to automatically send emails to countries
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

def main():
    print("=" * 60)
    print("SDG 7 Email Alert System")
    print("=" * 60)
    print()
    
    # Path to CSV
    csv_path = 'global-data-on-sustainable-energy.csv'
    
    print("📊 Loading data and training models...")
    forecaster = SDG7Forecasting(csv_path)
    forecaster.load_and_clean_data()
    forecaster.train_and_compare_models()
    
    print("🔮 Predicting electricity access for all countries...")
    all_predictions = forecaster.predict_future_access(1, None)
    
    if not all_predictions:
        print("❌ No predictions available")
        return
    
    # Convert to DataFrame
    predictions_df = pd.DataFrame(all_predictions)
    predictions_df.columns = ['year', 'country', 'predicted_access']
    
    print(f"✅ Analyzed {len(predictions_df['country'].unique())} countries")
    print()
    
    # Initialize email alert system
    alert_system = SDG7EmailAlerts()
    
    # Get summary first
    print("📋 Country Status Summary:")
    print("-" * 60)
    summary = alert_system.get_alert_summary(predictions_df)
    
    print(f"🚨 Critical (< 50% access): {len(summary['critical'])} countries")
    if summary['critical']:
        for c in summary['critical'][:5]:
            print(f"   - {c['country']}: {c['access']:.1f}%")
        if len(summary['critical']) > 5:
            print(f"   ... and {len(summary['critical']) - 5} more")
    
    print(f"\n⚠️  Needs Improvement (50-75%): {len(summary['needs_improvement'])} countries")
    if summary['needs_improvement']:
        for c in summary['needs_improvement'][:5]:
            print(f"   - {c['country']}: {c['access']:.1f}%")
        if len(summary['needs_improvement']) > 5:
            print(f"   ... and {len(summary['needs_improvement']) - 5} more")
    
    print(f"\n👍 Good (75-95%): {len(summary['good'])} countries")
    if summary['good']:
        for c in summary['good'][:5]:
            print(f"   - {c['country']}: {c['access']:.1f}%")
        if len(summary['good']) > 5:
            print(f"   ... and {len(summary['good']) - 5} more")
    
    print(f"\n🎉 Excellent (> 95%): {len(summary['excellent'])} countries")
    if summary['excellent']:
        for c in summary['excellent'][:5]:
            print(f"   - {c['country']}: {c['access']:.1f}%")
        if len(summary['excellent']) > 5:
            print(f"   ... and {len(summary['excellent']) - 5} more")
    
    print()
    print("=" * 60)
    
    # Ask user if they want to send emails
    response = input("\n📧 Do you want to send email alerts? (yes/no): ").strip().lower()
    
    if response in ['yes', 'y']:
        print("\n📤 Sending email alerts...")
        alerts_sent = alert_system.analyze_and_send_alerts(predictions_df)
        
        print(f"\n✅ Successfully sent {len(alerts_sent)} email alerts!")
        print("\nEmails sent to:")
        for alert in alerts_sent:
            status_emoji = {
                'critical': '🚨',
                'needs_improvement': '⚠️',
                'excellent': '🎉'
            }.get(alert['status'], '📧')
            
            print(f"{status_emoji} {alert['country']} ({alert['access']:.1f}% access) → {alert['email']}")
    else:
        print("\n❌ Email sending cancelled")
    
    print("\n" + "=" * 60)
    print("Done!")

if __name__ == '__main__':
    main()
