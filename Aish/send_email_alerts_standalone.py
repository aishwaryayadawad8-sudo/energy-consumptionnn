"""
Standalone Email Alert Script
Sends email alerts to countries based on electricity access
No Django required - Pure Python
"""
import sys
import os

# Add the sustainable_energy directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sustainable_energy'))

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Email alert thresholds
CRITICAL_THRESHOLD = 50
LOW_THRESHOLD = 75
GOOD_THRESHOLD = 95

# Country emails
COUNTRY_EMAILS = {
    'Afghanistan': 'afghanistan.energy@gov.af',
    'Bangladesh': 'bangladesh.energy@gov.bd',
    'India': 'india.energy@gov.in',
    'Kenya': 'kenya.energy@gov.ke',
    'Nigeria': 'nigeria.energy@gov.ng',
    'Brazil': 'brazil.energy@gov.br',
    'China': 'china.energy@gov.cn',
    'United States': 'usa.energy@gov.us',
    'Germany': 'germany.energy@gov.de',
    'Japan': 'japan.energy@gov.jp',
}

def classify_country_status(access_percentage):
    """Classify country based on electricity access"""
    if access_percentage < CRITICAL_THRESHOLD:
        return 'critical', 'Underdeveloped'
    elif access_percentage < LOW_THRESHOLD:
        return 'needs_improvement', 'Developing'
    elif access_percentage < GOOD_THRESHOLD:
        return 'good', 'Developing'
    else:
        return 'excellent', 'Developed'

def generate_email_content(country, access_percentage, status, country_type, year):
    """Generate email content based on country status"""
    
    if status == 'critical':
        subject = f"🚨 URGENT: Critical Electricity Access Alert for {country}"
        body = f"""
Dear Energy Ministry of {country},

CRITICAL ALERT: SDG 7 Monitoring System

Our AI-powered monitoring system has identified that {country} has critically low electricity access:

📊 Current Status:
- Electricity Access: {access_percentage:.1f}%
- Classification: {country_type} Country
- Status: CRITICAL - Immediate Action Required
- Year: {year}

⚠️ IMMEDIATE ACTION PLAN:
1. Deploy mobile solar units to remote areas
2. Establish emergency power distribution centers
3. Partner with international energy organizations
4. Accelerate grid expansion to underserved regions

Best regards,
SDG 7 Global Monitoring System
"""
    
    elif status == 'needs_improvement':
        subject = f"⚠️ Action Required: Electricity Access Below Target for {country}"
        body = f"""
Dear Energy Ministry of {country},

SDG 7 Progress Alert

Our monitoring system shows {country} needs to accelerate electricity access improvements:

📊 Current Status:
- Electricity Access: {access_percentage:.1f}%
- Classification: {country_type} Country
- Status: Below SDG 7 Target
- Year: {year}

💡 RECOMMENDED ACTIONS:
1. Expand grid infrastructure to rural areas
2. Implement renewable energy projects (solar, wind)
3. Provide financing for household connections

Best regards,
SDG 7 Global Monitoring System
"""
    
    elif status == 'excellent':
        subject = f"🎉 Congratulations: {country} Achieves Excellent Electricity Access!"
        body = f"""
Dear Energy Ministry of {country},

CONGRATULATIONS! 🎉

We are pleased to inform you that {country} has achieved excellent electricity access:

📊 Current Status:
- Electricity Access: {access_percentage:.1f}%
- Classification: {country_type} Country
- Status: EXCELLENT - SDG 7 Target Achieved!
- Year: {year}

🌟 Your success story will be featured in our global SDG 7 report!

Best regards,
SDG 7 Global Monitoring System
"""
    
    else:  # good
        subject = f"✅ Good Progress: {country} on Track for SDG 7"
        body = f"""
Dear Energy Ministry of {country},

SDG 7 Progress Update

{country} is making good progress toward universal electricity access:

📊 Current Status:
- Electricity Access: {access_percentage:.1f}%
- Classification: {country_type} Country
- Status: Good Progress
- Year: {year}

👍 Keep up the excellent work!

Best regards,
SDG 7 Global Monitoring System
"""
    
    return subject, body

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
    
    print("📊 Loading data...")
    try:
        df = pd.read_csv(csv_path)
        df.columns = df.columns.str.strip().str.replace('\n', ' ').str.replace(r'\s+', ' ', regex=True)
        print(f"✅ Loaded data with {len(df)} rows")
    except Exception as e:
        print(f"❌ Error loading CSV: {e}")
        return
    
    # Get latest data for each country
    print("\n🔮 Analyzing electricity access for all countries...")
    
    latest_data = df.groupby('Entity').apply(lambda x: x.nlargest(1, 'Year')).reset_index(drop=True)
    latest_data = latest_data[['Entity', 'Year', 'Access to electricity (% of population)']].dropna()
    
    print(f"✅ Analyzed {len(latest_data)} countries")
    print()
    
    # Classify countries
    results = []
    for _, row in latest_data.iterrows():
        country = row['Entity']
        access = row['Access to electricity (% of population)']
        year = int(row['Year'])
        
        status, country_type = classify_country_status(access)
        
        results.append({
            'country': country,
            'access': access,
            'status': status,
            'type': country_type,
            'year': year,
            'has_email': country in COUNTRY_EMAILS
        })
    
    # Group by status
    critical = [r for r in results if r['status'] == 'critical']
    needs_improvement = [r for r in results if r['status'] == 'needs_improvement']
    good = [r for r in results if r['status'] == 'good']
    excellent = [r for r in results if r['status'] == 'excellent']
    
    # Print summary
    print("📋 COUNTRY STATUS SUMMARY")
    print("=" * 70)
    
    print(f"\n🚨 CRITICAL (< 50% access): {len(critical)} countries")
    if critical:
        for c in critical[:10]:
            email_status = "✉️" if c['has_email'] else "❌"
            print(f"   {email_status} {c['country']}: {c['access']:.1f}%")
        if len(critical) > 10:
            print(f"   ... and {len(critical) - 10} more")
    
    print(f"\n⚠️  NEEDS IMPROVEMENT (50-75%): {len(needs_improvement)} countries")
    if needs_improvement:
        for c in needs_improvement[:10]:
            email_status = "✉️" if c['has_email'] else "❌"
            print(f"   {email_status} {c['country']}: {c['access']:.1f}%")
        if len(needs_improvement) > 10:
            print(f"   ... and {len(needs_improvement) - 10} more")
    
    print(f"\n👍 GOOD (75-95%): {len(good)} countries")
    if good:
        for c in good[:5]:
            email_status = "✉️" if c['has_email'] else "❌"
            print(f"   {email_status} {c['country']}: {c['access']:.1f}%")
        if len(good) > 5:
            print(f"   ... and {len(good) - 5} more")
    
    print(f"\n🎉 EXCELLENT (> 95%): {len(excellent)} countries")
    if excellent:
        for c in excellent[:10]:
            email_status = "✉️" if c['has_email'] else "❌"
            print(f"   {email_status} {c['country']}: {c['access']:.1f}%")
        if len(excellent) > 10:
            print(f"   ... and {len(excellent) - 10} more")
    
    print("\n" + "=" * 70)
    print(f"📧 Total countries with email configured: {len(COUNTRY_EMAILS)}")
    print("=" * 70)
    
    # Send emails (simulated)
    print("\n📤 SENDING EMAIL ALERTS...")
    print("-" * 70)
    
    alerts_sent = []
    
    for result in results:
        country = result['country']
        
        # Only send to countries with emails and specific statuses
        if country in COUNTRY_EMAILS and result['status'] in ['critical', 'needs_improvement', 'excellent']:
            subject, body = generate_email_content(
                country, 
                result['access'], 
                result['status'], 
                result['type'], 
                result['year']
            )
            
            # Simulate sending (print instead of actual email)
            print(f"✅ Email sent to {country} ({COUNTRY_EMAILS[country]})")
            print(f"   Subject: {subject}")
            print()
            
            alerts_sent.append({
                'country': country,
                'email': COUNTRY_EMAILS[country],
                'status': result['status'],
                'access': result['access']
            })
    
    # Summary
    print("\n" + "=" * 70)
    print("✅ EMAIL ALERT PROCESS COMPLETE!")
    print("=" * 70)
    
    critical_sent = [a for a in alerts_sent if a['status'] == 'critical']
    needs_improvement_sent = [a for a in alerts_sent if a['status'] == 'needs_improvement']
    excellent_sent = [a for a in alerts_sent if a['status'] == 'excellent']
    
    print(f"\n📊 SUMMARY:")
    print(f"   • Total countries analyzed: {len(results)}")
    print(f"   • Countries with emails: {len(COUNTRY_EMAILS)}")
    print(f"   • Alerts sent: {len(alerts_sent)}")
    print(f"   • Critical: {len(critical_sent)}")
    print(f"   • Needs Improvement: {len(needs_improvement_sent)}")
    print(f"   • Excellent: {len(excellent_sent)}")
    
    if alerts_sent:
        print(f"\n📧 EMAILS SENT TO:")
        for alert in alerts_sent:
            status_emoji = {'critical': '🚨', 'needs_improvement': '⚠️', 'excellent': '🎉'}.get(alert['status'], '📧')
            print(f"   {status_emoji} {alert['country']}: {alert['access']:.1f}% → {alert['email']}")

if __name__ == '__main__':
    main()
