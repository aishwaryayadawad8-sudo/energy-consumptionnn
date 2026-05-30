"""
Generate country_emails.csv with all countries from dataset
All emails will be set to your personal email address
"""

import pandas as pd

# Your personal email address
YOUR_EMAIL = "assowmya649@gmail.com"

# Load the dataset to get all countries
df = pd.read_csv('global-data-on-sustainable-energy.csv')

# Get unique countries and sort them
countries = sorted(df['Entity'].dropna().unique())

print(f"\n{'='*70}")
print(f"📧 Generating country_emails.csv for {len(countries)} countries")
print(f"{'='*70}\n")

# Create CSV data
csv_data = []
csv_data.append("Country,Email")

for country in countries:
    csv_data.append(f"{country},{YOUR_EMAIL}")

# Write to file
with open('country_emails.csv', 'w', encoding='utf-8') as f:
    f.write('\n'.join(csv_data))

print(f"✅ Created country_emails.csv with {len(countries)} countries")
print(f"✅ All emails set to: {YOUR_EMAIL}")
print()

# Show first 10 and last 10 countries
print("📋 First 10 countries:")
for i, country in enumerate(countries[:10], 1):
    print(f"   {i}. {country} → {YOUR_EMAIL}")

print()
print("📋 Last 10 countries:")
for i, country in enumerate(countries[-10:], len(countries)-9):
    print(f"   {i}. {country} → {YOUR_EMAIL}")

print()
print(f"{'='*70}")
print(f"✅ COMPLETE! All {len(countries)} countries configured")
print(f"{'='*70}\n")

# Verify the file
df_verify = pd.read_csv('country_emails.csv')
print(f"✅ Verification: CSV file has {len(df_verify)} rows")
print(f"✅ All emails point to: {YOUR_EMAIL}")
print()
print("🚀 Next steps:")
print("   1. Configure Gmail App Password: python fix_email_password.py")
print("   2. Test email: python test_email_setup.py")
print("   3. Send alerts: python auto_send_xgboost_alerts.py")
print()
