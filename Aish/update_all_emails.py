"""
Update ALL country emails to tejaswini.y2004teju@gmail.com
This ensures every country receives alerts at your email address
"""

import pandas as pd

print("\n" + "="*70)
print("📧 Updating ALL Country Emails")
print("="*70)

# Read the CSV
df = pd.read_csv('country_emails.csv')

print(f"\n📊 Total countries: {len(df)}")
print(f"📧 Setting all emails to: tejaswini.y2004teju@gmail.com")

# Update all emails to your address
df['Email'] = 'tejaswini.y2004teju@gmail.com'

# Save back to CSV
df.to_csv('country_emails.csv', index=False)

print("\n✅ All country emails updated successfully!")
print("\n📋 Sample countries updated:")
for i, row in df.head(10).iterrows():
    print(f"   {row['Country']:30s} → {row['Email']}")

print(f"\n... and {len(df) - 10} more countries")

print("\n" + "="*70)
print("✅ Configuration Complete!")
print("="*70)
print("\n🎯 Now ALL countries will receive alerts at:")
print("   tejaswini.y2004teju@gmail.com")
print("\n📝 To send automatic alerts to all countries:")
print("   python auto_send_xgboost_alerts.py")
print("\n" + "="*70 + "\n")
