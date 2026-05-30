"""
Automated Demo: Email Alert System
Shows how the system works with example countries
"""
import pandas as pd

# Configuration
DEMO_COUNTRIES = ["India", "Nigeria", "Kenya", "Chad", "Brazil"]

def load_country_emails():
    """Load country email addresses"""
    df = pd.read_csv('country_emails.csv')
    return dict(zip(df['Country'], df['Email']))

def analyze_country(country_name):
    """Analyze electricity access for a country"""
    df = pd.read_csv('global-data-on-sustainable-energy.csv')
    
    # Try case-insensitive match
    country_data = df[df['Entity'].str.lower() == country_name.lower()].copy()
    
    if country_data.empty:
        return None
    
    # Get correct country name
    country_name = country_data.iloc[0]['Entity']
    
    # Get most recent data
    country_data = country_data.sort_values('Year', ascending=False)
    latest = country_data.iloc[0]
    
    access = latest.get('Access to electricity (% of population)', 0)
    year = latest.get('Year', 2020)
    
    return {
        'country': country_name,
        'access': float(access),
        'year': int(year)
    }

def classify_status(access):
    """Classify country status"""
    if access < 50:
        return 'CRITICAL', '🚨'
    elif access < 75:
        return 'NEEDS IMPROVEMENT', '⚠️'
    elif access < 95:
        return 'GOOD', '👍'
    else:
        return 'EXCELLENT', '🎉'

def main():
    print("\n" + "=" * 70)
    print("🌍 SDG 7 Email Alert System - DEMO")
    print("=" * 70)
    print()
    
    # Load emails
    print("📧 Loading country email addresses...")
    country_emails = load_country_emails()
    print(f"✅ Loaded {len(country_emails)} country emails")
    print()
    
    print("=" * 70)
    print(f"Analyzing {len(DEMO_COUNTRIES)} Countries")
    print("=" * 70)
    print()
    
    results = []
    
    for country in DEMO_COUNTRIES:
        result = analyze_country(country)
        
        if not result:
            print(f"⚠️  {country}: Not found in dataset")
            continue
        
        email = country_emails.get(result['country'])
        status, emoji = classify_status(result['access'])
        
        print(f"{emoji} {result['country']}")
        print(f"   Electricity Access: {result['access']:.1f}%")
        print(f"   Status: {status}")
        print(f"   Year: {result['year']}")
        print(f"   Email: {email}")
        print()
        
        results.append({
            'country': result['country'],
            'access': result['access'],
            'status': status,
            'emoji': emoji,
            'email': email
        })
    
    print("=" * 70)
    print("📊 Summary")
    print("=" * 70)
    print()
    
    # Group by status
    critical = [r for r in results if 'CRITICAL' in r['status']]
    needs_improvement = [r for r in results if 'NEEDS IMPROVEMENT' in r['status']]
    good = [r for r in results if 'GOOD' in r['status']]
    excellent = [r for r in results if 'EXCELLENT' in r['status']]
    
    if critical:
        print(f"🚨 CRITICAL ({len(critical)} countries):")
        for r in critical:
            print(f"   - {r['country']}: {r['access']:.1f}%")
        print()
    
    if needs_improvement:
        print(f"⚠️  NEEDS IMPROVEMENT ({len(needs_improvement)} countries):")
        for r in needs_improvement:
            print(f"   - {r['country']}: {r['access']:.1f}%")
        print()
    
    if good:
        print(f"👍 GOOD ({len(good)} countries):")
        for r in good:
            print(f"   - {r['country']}: {r['access']:.1f}%")
        print()
    
    if excellent:
        print(f"🎉 EXCELLENT ({len(excellent)} countries):")
        for r in excellent:
            print(f"   - {r['country']}: {r['access']:.1f}%")
        print()
    
    print("=" * 70)
    print("📧 Email Alert Preview")
    print("=" * 70)
    print()
    
    # Show example email for first country
    if results:
        example = results[0]
        print(f"Example email for {example['country']}:")
        print("-" * 70)
        
        if 'CRITICAL' in example['status']:
            subject = f"🚨 URGENT: Critical Electricity Access Alert for {example['country']}"
        elif 'NEEDS IMPROVEMENT' in example['status']:
            subject = f"⚠️ Action Required: Electricity Access Below Target for {example['country']}"
        elif 'EXCELLENT' in example['status']:
            subject = f"🎉 Congratulations: {example['country']} Achieves Excellent Electricity Access!"
        else:
            subject = f"✅ Good Progress: {example['country']} on Track for SDG 7"
        
        print(f"To: {example['email']}")
        print(f"Subject: {subject}")
        print(f"Status: {example['status']} ({example['access']:.1f}% access)")
        print("-" * 70)
    
    print()
    print("=" * 70)
    print("✅ Demo Complete!")
    print("=" * 70)
    print()
    print("To send real alerts, run:")
    print("  python send_email_simple.py")
    print()
    print("Then enter countries like: India, Nigeria, Brazil")
    print()
    print("Note: Currently in SIMULATION mode (no actual emails sent)")
    print("To enable real sending:")
    print("  1. Get Gmail App Password from https://myaccount.google.com/apppasswords")
    print("  2. Edit send_email_simple.py and update SENDER_PASSWORD")
    print("  3. Set ENABLE_SENDING = True")
    print()

if __name__ == '__main__':
    main()
