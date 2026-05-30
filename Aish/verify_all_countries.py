"""
Verify that all countries are configured correctly
"""

import pandas as pd

print("\n" + "="*70)
print("🔍 VERIFYING COUNTRY EMAIL CONFIGURATION")
print("="*70 + "\n")

# Load country emails
df_emails = pd.read_csv('country_emails.csv')

# Load dataset countries
df_data = pd.read_csv('global-data-on-sustainable-energy.csv')
dataset_countries = sorted(df_data['Entity'].dropna().unique())

print(f"📊 STATISTICS:")
print(f"   Countries in CSV: {len(df_emails)}")
print(f"   Countries in Dataset: {len(dataset_countries)}")
print(f"   Match: {'✅ YES' if len(df_emails) == len(dataset_countries) else '❌ NO'}")
print()

# Check email addresses
unique_emails = df_emails['Email'].unique()
print(f"📧 EMAIL ADDRESSES:")
for email in unique_emails:
    count = len(df_emails[df_emails['Email'] == email])
    print(f"   {email}: {count} countries")
print()

# Check for missing countries
csv_countries = set(df_emails['Country'].tolist())
data_countries = set(dataset_countries)

missing_in_csv = data_countries - csv_countries
missing_in_data = csv_countries - data_countries

if missing_in_csv:
    print(f"⚠️  MISSING IN CSV ({len(missing_in_csv)}):")
    for country in sorted(missing_in_csv):
        print(f"   - {country}")
    print()
else:
    print("✅ All dataset countries are in CSV")
    print()

if missing_in_data:
    print(f"⚠️  EXTRA IN CSV ({len(missing_in_data)}):")
    for country in sorted(missing_in_data):
        print(f"   - {country}")
    print()
else:
    print("✅ No extra countries in CSV")
    print()

# Show sample countries
print("📋 SAMPLE COUNTRIES (First 10):")
for i, row in df_emails.head(10).iterrows():
    print(f"   {i+1}. {row['Country']} → {row['Email']}")
print()

print("📋 SAMPLE COUNTRIES (Last 10):")
for i, row in df_emails.tail(10).iterrows():
    print(f"   {i+1}. {row['Country']} → {row['Email']}")
print()

# Final status
print("="*70)
if len(df_emails) == len(dataset_countries) and not missing_in_csv:
    print("✅ VERIFICATION PASSED!")
    print(f"   All {len(df_emails)} countries are correctly configured")
    print(f"   All emails point to: {df_emails['Email'].iloc[0]}")
else:
    print("⚠️  VERIFICATION ISSUES FOUND")
    print("   Please review the warnings above")
print("="*70 + "\n")

# Next steps
print("🚀 NEXT STEPS:")
print("   1. Setup Gmail App Password: python fix_email_password.py")
print("   2. Test email: python test_email_setup.py")
print("   3. Send test alert: python send_xgboost_alert_to_country.py Albania")
print("   4. Send to all: python auto_send_xgboost_alerts.py")
print()
