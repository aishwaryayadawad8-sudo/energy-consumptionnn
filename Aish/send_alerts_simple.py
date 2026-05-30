"""
Simple Email Alert Script - No Django Required
Sends email alerts to countries based on electricity access
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sustainable_energy'))

import pandas as pd
from ml_models.email_alerts import SDG7EmailAlerts
from ml_models.sdg7_forecasting import SDG7Forecasting

def main():
    print("=" * 70)
    print("SDG 7 EMAIL ALERT SYSTEM")
    print("=" * 70)
    print()
    
    # Path to CSV
    csv_path = 'global-data-on-sustainable-energy.csv'
    
    if not os.path.exists(csv_path):
        print(f"❌ Error: CSV file not found at {csv_path}")
        return
    
    print("📊 Loading data and training models...")
    try:
        forecaster = SDG7Forecasting(csv_path)
        forecaster.load_and_clean_data()
        forecaster.train_and_compare_models()
        print("✅ Models trained successfully!")
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return
    
    print("\n🔮 Predicting electricity access for all countries...")
    try:
        all_predictions = forecaster.predict_future_access(1, None)
        
        if not all_predictions:
            print("❌ No predictions available")
            return
        
        # Convert to DataFrame
        predictions_df = pd.DataFrame(all_predictions)
        predictions_df.columns = ['year', 'country', 'predicted_access']
        
        print(f"✅ Analyzed {len(predictions_df['country'].unique())} countries")
    except Exception as e:
        print(f"❌ Error making predictions: {e}")
        return
    
    print()
    
    # Initialize email alert system
    alert_system = SDG7EmailAlerts()
    
    # Get summary
    print("📋 COUNTRY STATUS SUMMARY")
    print("=" * 70)
    summary = alert_system.get_alert_summary(predictions_df)
    
    # Critical countries
    print(f"\n🚨 CRITICAL (< 50% access): {len(summary['critical'])} countries")
    if summary['critical']:
        print("   Top countries:")
        for c in summary['critical'][:10]:
            email_status = "✉️" if c['has_email'] else "❌"
            print(f"   {email_status} {c['country']}: {c['access']:.1f}%")
        if len(summary['critical']) > 10:
            print(f"   ... and {len(summary['critical']) - 10} more")
    
    # Needs improvement
    print(f"\n⚠️  NEEDS IMPROVEMENT (50-75%): {len(summary['needs_improvement'])} countries")
    if summary['needs_improvement']:
        print("   Top countries:")
        for c in summary['needs_improvement'][:10]:
            email_status = "✉️" if c['has_email'] else "❌"
            print(f"   {email_status} {c['country']}: {c['access']:.1f}%")
        if len(summary['needs_improvement']) > 10:
            print(f"   ... and {len(summary['needs_improvement']) - 10} more")
    
    # Good
    print(f"\n👍 GOOD (75-95%): {len(summary['good'])} countries")
    if summary['good']:
        print("   Sample countries:")
        for c in summary['good'][:5]:
            email_status = "✉️" if c['has_email'] else "❌"
            print(f"   {email_status} {c['country']}: {c['access']:.1f}%")
        if len(summary['good']) > 5:
            print(f"   ... and {len(summary['good']) - 5} more")
    
    # Excellent
    print(f"\n🎉 EXCELLENT (> 95%): {len(summary['excellent'])} countries")
    if summary['excellent']:
        print("   Sample countries:")
        for c in summary['excellent'][:10]:
            email_status = "✉️" if c['has_email'] else "❌"
            print(f"   {email_status} {c['country']}: {c['access']:.1f}%")
        if len(summary['excellent']) > 10:
            print(f"   ... and {len(summary['excellent']) - 10} more")
    
    print("\n" + "=" * 70)
    print(f"📧 Total countries with email configured: {len(alert_system.COUNTRY_EMAILS)}")
    print("=" * 70)
    
    # Send emails
    print("\n📤 SENDING EMAIL ALERTS...")
    print("-" * 70)
    
    try:
        alerts_sent = alert_system.analyze_and_send_alerts(predictions_df)
        
        print(f"\n✅ Successfully processed {len(alerts_sent)} email alerts!")
        print("\n📧 EMAILS SENT TO:")
        print("=" * 70)
        
        # Group by status
        critical_sent = [a for a in alerts_sent if a['status'] == 'critical']
        needs_improvement_sent = [a for a in alerts_sent if a['status'] == 'needs_improvement']
        excellent_sent = [a for a in alerts_sent if a['status'] == 'excellent']
        
        if critical_sent:
            print(f"\n🚨 CRITICAL ALERTS ({len(critical_sent)}):")
            for alert in critical_sent:
                print(f"   → {alert['country']}: {alert['access']:.1f}% → {alert['email']}")
        
        if needs_improvement_sent:
            print(f"\n⚠️  NEEDS IMPROVEMENT ALERTS ({len(needs_improvement_sent)}):")
            for alert in needs_improvement_sent:
                print(f"   → {alert['country']}: {alert['access']:.1f}% → {alert['email']}")
        
        if excellent_sent:
            print(f"\n🎉 EXCELLENT ALERTS ({len(excellent_sent)}):")
            for alert in excellent_sent:
                print(f"   → {alert['country']}: {alert['access']:.1f}% → {alert['email']}")
        
        print("\n" + "=" * 70)
        print("✅ EMAIL ALERT PROCESS COMPLETE!")
        print("=" * 70)
        
        # Summary
        print(f"\n📊 SUMMARY:")
        print(f"   • Total countries analyzed: {len(predictions_df['country'].unique())}")
        print(f"   • Countries with emails: {len(alert_system.COUNTRY_EMAILS)}")
        print(f"   • Alerts sent: {len(alerts_sent)}")
        print(f"   • Critical: {len(critical_sent)}")
        print(f"   • Needs Improvement: {len(needs_improvement_sent)}")
        print(f"   • Excellent: {len(excellent_sent)}")
        
    except Exception as e:
        print(f"\n❌ Error sending emails: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
