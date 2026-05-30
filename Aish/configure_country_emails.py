"""
Configure Country Emails - Interactive Setup
Choose which countries should receive alerts at your email address
"""

import pandas as pd

print("\n" + "="*70)
print("📧 Configure Country Email Alerts")
print("="*70)

# Read current configuration
df = pd.read_csv('country_emails.csv')
countries = sorted(df['Country'].tolist())

print(f"\n📊 Total Countries Available: {len(countries)}")
print("\n" + "="*70)
print("ALL COUNTRIES LIST:")
print("="*70)

# Display all countries in columns
for i in range(0, len(countries), 3):
    row = countries[i:i+3]
    print("   " + "".join(f"{c:30s}" for c in row))

print("\n" + "="*70)
print("📝 CONFIGURATION OPTIONS:")
print("="*70)
print("\n1. Set ALL countries to your email")
print("2. Set SPECIFIC countries to your email")
print("3. View current configuration")
print("4. Exit")

choice = input("\nEnter your choice (1-4): ").strip()

if choice == "1":
    # Set all countries to user email
    print("\n" + "="*70)
    email = input("Enter your email address: ").strip()
    
    if email and '@' in email:
        df['Email'] = email
        df.to_csv('country_emails.csv', index=False)
        print(f"\n✅ ALL {len(countries)} countries set to: {email}")
        print("\n📝 To send alerts, run:")
        print("   python auto_send_xgboost_alerts.py")
    else:
        print("\n❌ Invalid email address!")

elif choice == "2":
    # Set specific countries
    print("\n" + "="*70)
    print("Enter country names separated by commas")
    print("Example: Albania, Kenya, India, Brazil")
    print("="*70)
    
    selected = input("\nCountries: ").strip()
    email = input("Your email address: ").strip()
    
    if selected and email and '@' in email:
        selected_countries = [c.strip() for c in selected.split(',')]
        updated = 0
        
        for country in selected_countries:
            if country in df['Country'].values:
                df.loc[df['Country'] == country, 'Email'] = email
                updated += 1
                print(f"   ✅ {country} → {email}")
            else:
                print(f"   ⚠️  {country} not found")
        
        if updated > 0:
            df.to_csv('country_emails.csv', index=False)
            print(f"\n✅ Updated {updated} countries")
            print("\n📝 To send alerts, run:")
            print(f"   python send_xgboost_alert_to_country.py {selected_countries[0]}")
    else:
        print("\n❌ Invalid input!")

elif choice == "3":
    # View current configuration
    print("\n" + "="*70)
    print("CURRENT CONFIGURATION:")
    print("="*70)
    
    # Group by email
    email_groups = df.groupby('Email')['Country'].apply(list).to_dict()
    
    for email, country_list in email_groups.items():
        print(f"\n📧 {email}")
        print(f"   Countries ({len(country_list)}):")
        for i in range(0, len(country_list), 3):
            row = country_list[i:i+3]
            print("   " + ", ".join(row))

else:
    print("\n👋 Goodbye!")

print("\n" + "="*70)
print("✅ Configuration Complete!")
print("="*70)
print("\n📝 Next Steps:")
print("   1. Send alerts: python auto_send_xgboost_alerts.py")
print("   2. View logs: http://localhost:8000/email-logs/")
print("   3. Admin page: http://localhost:8000/admin-login/")
print("\n" + "="*70 + "\n")
