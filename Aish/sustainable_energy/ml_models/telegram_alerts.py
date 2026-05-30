"""
Telegram Alert System for SDG 7 Energy Dashboard
Send instant alerts to countries via Telegram Bot
"""

import requests
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from telegram_config import TELEGRAM_BOT_TOKEN, COUNTRY_CHAT_IDS, ENABLE_TELEGRAM_ALERTS
except ImportError:
    print("⚠️  telegram_config.py not found. Please create it first.")
    TELEGRAM_BOT_TOKEN = None
    COUNTRY_CHAT_IDS = {}
    ENABLE_TELEGRAM_ALERTS = False


def send_telegram_alert(country, electricity_access, status, recommendations):
    """
    Send energy alert to a specific country via Telegram
    
    Args:
        country (str): Country name
        electricity_access (float): Electricity access percentage
        status (str): 'critical', 'needs_improvement', or 'excellent'
        recommendations (str): Action recommendations
    
    Returns:
        bool: True if sent successfully, False otherwise
    """
    
    if not ENABLE_TELEGRAM_ALERTS:
        print("ℹ️  Telegram alerts are disabled. Enable in telegram_config.py")
        return False
    
    if not TELEGRAM_BOT_TOKEN or TELEGRAM_BOT_TOKEN == 'YOUR_BOT_TOKEN_HERE':
        print("❌ Please configure TELEGRAM_BOT_TOKEN in telegram_config.py")
        return False
    
    chat_id = COUNTRY_CHAT_IDS.get(country)
    if not chat_id:
        print(f"⚠️  No Telegram chat ID configured for {country}")
        return False
    
    # Format message based on status
    if status == 'critical':
        emoji = '🚨'
        status_text = '*CRITICAL ALERT*'
        urgency = '⚠️ IMMEDIATE ACTION REQUIRED'
    elif status == 'needs_improvement':
        emoji = '⚠️'
        status_text = '*NEEDS IMPROVEMENT*'
        urgency = '📋 Action Recommended'
    else:
        emoji = '✅'
        status_text = '*EXCELLENT PROGRESS*'
        urgency = '🎉 Keep up the good work!'
    
    # Create formatted message
    message = f"""
{emoji} *ENERGY ALERT: {country}*

{urgency}

📊 *Current Status*
• Electricity Access: *{electricity_access:.1f}%*
• Classification: {status_text}

💡 *Recommendations:*
{recommendations}

━━━━━━━━━━━━━━━━━━━━
_Automated alert from SDG 7 Dashboard_
_Powered by Machine Learning predictions_
    """
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    try:
        response = requests.post(url, data={
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'Markdown'
        }, timeout=10)
        
        if response.status_code == 200:
            print(f"✅ Telegram alert sent to {country}")
            return True
        else:
            print(f"❌ Failed to send to {country}: {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        print(f"❌ Timeout sending alert to {country}")
        return False
    except Exception as e:
        print(f"❌ Error sending Telegram alert to {country}: {e}")
        return False


def get_recommendations(country, access, renewable_share=None, co2_emissions=None):
    """Generate recommendations based on country metrics"""
    
    if access < 50:
        return """
• 🏗️ Immediate infrastructure investment needed
• 🤝 Partner with international energy organizations
• ♻️ Focus on renewable energy solutions
• 🌍 Implement rural electrification programs
• 💰 Seek funding from World Bank/UN programs
        """
    elif access < 80:
        return """
• 📈 Expand grid coverage to rural areas
• ⚡ Invest in renewable energy capacity
• 💡 Improve energy efficiency programs
• 📋 Strengthen policy frameworks
• 🔋 Develop energy storage solutions
        """
    else:
        return """
• ✅ Maintain current infrastructure
• 🌱 Continue renewable energy expansion
• 🌍 Share best practices with other nations
• 🎯 Focus on sustainability goals
• 📊 Monitor and optimize energy distribution
        """


def send_telegram_alerts_to_all():
    """
    Send alerts to all countries based on electricity access thresholds
    
    Returns:
        dict: Summary of alerts sent
    """
    
    if not ENABLE_TELEGRAM_ALERTS:
        return {
            'success': False,
            'message': 'Telegram alerts are disabled',
            'alerts_sent': []
        }
    
    import pandas as pd
    
    try:
        # Load data
        csv_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'global-data-on-sustainable-energy.csv'
        )
        df = pd.read_csv(csv_path)
        
        # Get latest data for each country
        latest_data = df.groupby('Entity').last().reset_index()
        
        alerts_sent = []
        alerts_failed = []
        
        for _, row in latest_data.iterrows():
            country = row['Entity']
            
            # Skip if no chat ID configured
            if country not in COUNTRY_CHAT_IDS or not COUNTRY_CHAT_IDS[country]:
                continue
            
            access = row.get('Access to electricity (% of population)', 0)
            renewable = row.get('Renewable energy share in the total final energy consumption (%)', 0)
            co2 = row.get('Value_co2_emissions_kt_by_country', 0)
            
            # Determine status
            if access < 50:
                status = 'critical'
            elif access < 80:
                status = 'needs_improvement'
            else:
                status = 'excellent'
            
            # Get recommendations
            recommendations = get_recommendations(country, access, renewable, co2)
            
            # Send alert
            success = send_telegram_alert(country, access, status, recommendations)
            
            if success:
                alerts_sent.append({
                    'country': country,
                    'access': float(access),
                    'status': status
                })
            else:
                alerts_failed.append(country)
        
        return {
            'success': True,
            'total_alerts': len(alerts_sent),
            'alerts_sent': alerts_sent,
            'failed': alerts_failed
        }
        
    except FileNotFoundError:
        return {
            'success': False,
            'message': 'CSV file not found',
            'alerts_sent': []
        }
    except Exception as e:
        return {
            'success': False,
            'message': str(e),
            'alerts_sent': []
        }


def send_telegram_alert_to_country(country_name):
    """
    Send alert to a specific country
    
    Args:
        country_name (str): Name of the country
    
    Returns:
        dict: Result of the operation
    """
    
    if not ENABLE_TELEGRAM_ALERTS:
        return {'success': False, 'message': 'Telegram alerts are disabled'}
    
    import pandas as pd
    
    try:
        csv_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'global-data-on-sustainable-energy.csv'
        )
        df = pd.read_csv(csv_path)
        
        # Get country data
        country_data = df[df['Entity'] == country_name]
        
        if country_data.empty:
            return {'success': False, 'message': f'Country {country_name} not found'}
        
        latest = country_data.iloc[-1]
        access = latest.get('Access to electricity (% of population)', 0)
        
        # Determine status
        if access < 50:
            status = 'critical'
        elif access < 80:
            status = 'needs_improvement'
        else:
            status = 'excellent'
        
        recommendations = get_recommendations(country_name, access)
        
        success = send_telegram_alert(country_name, access, status, recommendations)
        
        return {
            'success': success,
            'country': country_name,
            'access': float(access),
            'status': status
        }
        
    except Exception as e:
        return {'success': False, 'message': str(e)}


if __name__ == '__main__':
    # Test the system
    print("=" * 60)
    print("Testing Telegram Alert System")
    print("=" * 60)
    
    if not ENABLE_TELEGRAM_ALERTS:
        print("\n⚠️  Telegram alerts are DISABLED")
        print("To enable:")
        print("1. Get bot token from @BotFather")
        print("2. Update telegram_config.py")
        print("3. Set ENABLE_TELEGRAM_ALERTS = True")
    else:
        print("\n✅ Telegram alerts are ENABLED")
        print(f"Bot Token: {TELEGRAM_BOT_TOKEN[:10]}...")
        print(f"Configured countries: {len([c for c in COUNTRY_CHAT_IDS.values() if c])}")
        
        # Test sending to all
        print("\nSending test alerts...")
        result = send_telegram_alerts_to_all()
        print(f"\nResults: {result}")
