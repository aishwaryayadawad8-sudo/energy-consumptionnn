"""
Verify Email Addresses Configuration
Shows which emails will be used for each country
"""

print("=" * 70)
print("📧 Email Address Verification")
print("=" * 70)

# Check configuration
print("\n📋 Step 1: Checking Configuration")
print("-" * 70)

try:
    from sustainable_energy.email_config import TESTING_MODE, DUMMY_EMAIL
    
    print(f"TESTING_MODE: {TESTING_MODE}")
    print(f"DUMMY_EMAIL: {DUMMY_EMAIL}")
    
    if TESTING_MODE:
        print(f"\n⚠️  WARNING: TESTING_MODE is ON")
        print(f"   ALL emails will go to: {DUMMY_EMAIL}")
        print(f"   CSV emails will be IGNORED")
    else:
        print(f"\n✅ TESTING_MODE is OFF")
        print(f"   Emails will use addresses from country_emails.csv")
        
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)

# Load CSV emails
print("\n📧 Step 2: Loading Email Addresses from CSV")
print("-" * 70)

try:
    import pandas as pd
    df = pd.read_csv('country_emails.csv')
    
    print(f"✅ Loaded {len(df)} countries from CSV")
    print(f"\nSample emails from CSV:")
    
    for i, row in df.head(10).iterrows():
        print(f"  {row['Country']:30s} → {row['Email']}")
    
    # Check for your specific email
    your_email = 'assowmya649@gmail.com'
    countries_with_your_email = df[df['Email'] == your_email]
    
    if len(countries_with_your_email) > 0:
        print(f"\n✅ Found your email ({your_email}) for:")
        for _, row in countries_with_your_email.iterrows():
            print(f"  - {row['Country']}")
    
except Exception as e:
    print(f"❌ Error loading CSV: {e}")

# Show what will actually be used
print("\n🎯 Step 3: What Will Actually Be Used")
print("-" * 70)

try:
    from sustainable_energy.ml_models.email_alerts import SDG7EmailAlerts
    
    alert_system = SDG7EmailAlerts()
    
    # Check a few countries
    test_countries = ['Afghanistan', 'Albania', 'India', 'Kenya']
    
    print(f"Email addresses that will be used:")
    for country in test_countries:
        if country in alert_system.COUNTRY_EMAILS:
            email = alert_system.COUNTRY_EMAILS[country]
            
            if TESTING_MODE:
                actual_email = DUMMY_EMAIL
                print(f"  {country:20s} → {email:40s} (REDIRECTED TO: {actual_email})")
            else:
                print(f"  {country:20s} → {email}")
        else:
            print(f"  {country:20s} → NOT FOUND")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

# Summary
print("\n" + "=" * 70)
print("📊 Summary")
print("=" * 70)

if TESTING_MODE:
    print(f"\n⚠️  TESTING MODE IS ON")
    print(f"   Current behavior:")
    print(f"   - ALL emails go to: {DUMMY_EMAIL}")
    print(f"   - CSV emails are ignored")
    print(f"\n   To use CSV emails:")
    print(f"   1. Open: sustainable_energy/email_config.py")
    print(f"   2. Change: TESTING_MODE = False")
    print(f"   3. Restart server")
else:
    print(f"\n✅ TESTING MODE IS OFF")
    print(f"   Current behavior:")
    print(f"   - Emails use addresses from country_emails.csv")
    print(f"   - Afghanistan → assowmya649@gmail.com")
    print(f"   - Albania → electricity.prediction2000@gmail.com")
    print(f"   - Other countries → their CSV emails")

print("\n" + "=" * 70)
