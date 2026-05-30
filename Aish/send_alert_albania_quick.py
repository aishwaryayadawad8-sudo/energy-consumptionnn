"""
Quick Script to Send Alert to Albania
Works WITHOUT Django - Run this if Django server has issues
"""
import pandas as pd

print("\n" + "="*60)
print("🚀 Quick Email Alert to Albania")
print("="*60)
print()

try:
    # Load data
    print("📊 Loading data...")
    df = pd.read_csv('global-data-on-sustainable-energy.csv')
    
    # Get Albania data
    albania_data = df[df['Entity'] == 'Albania'].copy()
    
    if albania_data.empty:
        print("❌ Albania not found in dataset")
    else:
        # Get latest data
        albania_data = albania_data.sort_values('Year', ascending=False)
        latest = albania_data.iloc[0]
        
        access = latest.get('Access to electricity (% of population)', 0)
        year = latest.get('Year', 2020)
        
        print(f"✅ Albania Data Found!")
        print(f"   Year: {year}")
        print(f"   Electricity Access: {access}%")
        print()
        
        # Classify status
        if access < 50:
            status = "🚨 CRITICAL"
            message = "Urgent action needed"
        elif access < 75:
            status = "⚠️ NEEDS IMPROVEMENT"
            message = "Below SDG 7 target"
        elif access < 95:
            status = "👍 GOOD"
            message = "On track for SDG 7"
        else:
            status = "🎉 EXCELLENT"
            message = "SDG 7 target achieved!"
        
        print(f"Status: {status}")
        print(f"Message: {message}")
        print()
        
        # Email details
        email = "albania@sdg7_alerts.org"
        print(f"📧 Email would be sent to: {email}")
        print()
        
        # Email content
        if "EXCELLENT" in status or "GOOD" in status:
            subject = f"✅ Good Progress: Albania on Track for SDG 7"
            body = f"""
Dear Energy Ministry of Albania,

SDG 7 Progress Update

Albania is making good progress toward universal electricity access:

📊 Current Status:
- Electricity Access: {access}%
- Status: {message}
- Year: {year}

👍 Keep up the excellent work! Continue current efforts to reach 100% access.

Best regards,
SDG 7 Global Monitoring System
"""
        else:
            subject = f"⚠️ Action Required: Electricity Access Alert for Albania"
            body = f"""
Dear Energy Ministry of Albania,

SDG 7 Alert

Our monitoring system shows Albania needs attention:

📊 Current Status:
- Electricity Access: {access}%
- Status: {message}
- Year: {year}

💡 RECOMMENDED ACTIONS:
1. Expand grid infrastructure
2. Implement renewable energy projects
3. Provide financing for connections

Best regards,
SDG 7 Global Monitoring System
"""
        
        print("="*60)
        print("📧 EMAIL PREVIEW")
        print("="*60)
        print(f"To: {email}")
        print(f"Subject: {subject}")
        print()
        print(body)
        print("="*60)
        print()
        print("✅ SUCCESS! Email alert prepared for Albania")
        print()
        print("NOTE: Currently in SIMULATION mode")
        print("To actually send emails, configure email_config.py")
        
except FileNotFoundError:
    print("❌ Error: global-data-on-sustainable-energy.csv not found")
    print("   Make sure you're in the correct directory")
except Exception as e:
    print(f"❌ Error: {e}")

print()
print("="*60)
print("Done!")
print("="*60)
