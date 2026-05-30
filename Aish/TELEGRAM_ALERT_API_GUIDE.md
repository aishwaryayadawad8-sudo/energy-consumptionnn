# 📱 Telegram Bot API - Best Choice for Your Project

## 🎯 Why Telegram Bot API?

### Advantages
- ✅ **100% FREE** - No limits, no costs
- ✅ **Instant delivery** - Real-time alerts
- ✅ **Easy setup** - 10 minutes to implement
- ✅ **Rich formatting** - Markdown, buttons, images
- ✅ **Group support** - Multiple officials per country
- ✅ **No phone numbers needed** - Users subscribe via username
- ✅ **Reliable** - 99.9% uptime
- ✅ **Global** - Works in all countries

### Perfect For Your SDG 7 Project
- Send instant energy alerts to countries
- Countries subscribe to your bot
- Automated threshold-based notifications
- Share charts and reports
- Create country-specific channels

---

## 🚀 Quick Setup (5 Steps)

### Step 1: Create Your Bot (2 minutes)

1. Open Telegram and search for **@BotFather**
2. Send: `/newbot`
3. Choose name: `SDG7 Energy Alert Bot`
4. Choose username: `sdg7_energy_bot` (must end with 'bot')
5. **Copy your bot token** (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### Step 2: Install Python Library
```bash
pip install python-telegram-bot requests
```

### Step 3: Create Telegram Config File
```python
# sustainable_energy/telegram_config.py

TELEGRAM_BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'

# Country chat IDs (users will get these by messaging your bot)
COUNTRY_CHAT_IDS = {
    'India': '123456789',
    'Kenya': '987654321',
    'Germany': '456789123',
    # Add more as countries subscribe
}
```

### Step 4: Create Alert Function
```python
# sustainable_energy/ml_models/telegram_alerts.py

import requests
from telegram_config import TELEGRAM_BOT_TOKEN, COUNTRY_CHAT_IDS

def send_telegram_alert(country, electricity_access, status, recommendations):
    """Send energy alert via Telegram"""
    
    chat_id = COUNTRY_CHAT_IDS.get(country)
    if not chat_id:
        print(f"No Telegram chat ID for {country}")
        return False
    
    # Format message with Markdown
    if status == 'critical':
        emoji = '🚨'
        status_text = '*CRITICAL*'
    elif status == 'needs_improvement':
        emoji = '⚠️'
        status_text = '*NEEDS IMPROVEMENT*'
    else:
        emoji = '✅'
        status_text = '*EXCELLENT*'
    
    message = f"""
{emoji} *ENERGY ALERT: {country}*

📊 *Electricity Access:* {electricity_access:.1f}%
🎯 *Status:* {status_text}

*Recommendations:*
{recommendations}

_Automated alert from SDG 7 Dashboard_
_Powered by ML predictions_
    """
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    try:
        response = requests.post(url, data={
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'Markdown'
        })
        
        if response.status_code == 200:
            print(f"✅ Telegram alert sent to {country}")
            return True
        else:
            print(f"❌ Failed to send to {country}: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error sending Telegram alert: {e}")
        return False


def send_telegram_alerts_to_all():
    """Send alerts to all countries based on thresholds"""
    import pandas as pd
    
    # Load your data
    df = pd.read_csv('global-data-on-sustainable-energy.csv')
    latest_data = df.groupby('Entity').last().reset_index()
    
    alerts_sent = []
    
    for _, row in latest_data.iterrows():
        country = row['Entity']
        access = row.get('Access to electricity (% of population)', 0)
        
        # Determine status and recommendations
        if access < 50:
            status = 'critical'
            recommendations = """
• Immediate infrastructure investment needed
• Partner with international energy organizations
• Focus on renewable energy solutions
• Implement rural electrification programs
            """
        elif access < 80:
            status = 'needs_improvement'
            recommendations = """
• Expand grid coverage to rural areas
• Invest in renewable energy capacity
• Improve energy efficiency programs
• Strengthen policy frameworks
            """
        else:
            status = 'excellent'
            recommendations = """
• Maintain current infrastructure
• Continue renewable energy expansion
• Share best practices with other nations
• Focus on sustainability goals
            """
        
        # Send alert
        success = send_telegram_alert(country, access, status, recommendations)
        
        if success:
            alerts_sent.append({
                'country': country,
                'access': access,
                'status': status
            })
    
    return alerts_sent
```

### Step 5: Add to Your Django Views
```python
# sustainable_energy/dashboard/views.py

from ml_models.telegram_alerts import send_telegram_alert, send_telegram_alerts_to_all

def send_telegram_alerts_view(request):
    """API endpoint to send Telegram alerts"""
    if request.method == 'POST':
        alerts_sent = send_telegram_alerts_to_all()
        
        return JsonResponse({
            'success': True,
            'total_alerts': len(alerts_sent),
            'alerts': alerts_sent
        })
    
    return JsonResponse({'error': 'POST method required'}, status=400)
```

---

## 📱 How Countries Subscribe

### For Country Officials:

1. **Open Telegram** and search for your bot: `@sdg7_energy_bot`
2. **Click Start** or send `/start`
3. **Get Chat ID**: Bot replies with their chat ID
4. **Register**: Send chat ID to your admin
5. **Receive Alerts**: Automatic notifications!

### Bot Commands:
```
/start - Subscribe to alerts
/status - Check current energy status
/help - Get help
/unsubscribe - Stop receiving alerts
```

---

## 🎨 Advanced Features

### 1. Send Charts via Telegram
```python
import matplotlib.pyplot as plt
import io

def send_chart_to_telegram(country, chat_id):
    # Create chart
    plt.figure(figsize=(10, 6))
    # ... your chart code ...
    
    # Save to bytes
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    # Send via Telegram
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
    files = {'photo': buf}
    data = {'chat_id': chat_id, 'caption': f'Energy trends for {country}'}
    
    requests.post(url, files=files, data=data)
```

### 2. Interactive Buttons
```python
def send_alert_with_buttons(country, chat_id):
    keyboard = {
        'inline_keyboard': [[
            {'text': '📊 View Dashboard', 'url': 'http://your-dashboard.com'},
            {'text': '📧 Email Report', 'callback_data': 'email_report'}
        ]]
    }
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        'chat_id': chat_id,
        'text': f'Energy alert for {country}',
        'reply_markup': keyboard
    })
```

### 3. Create Country Channels
```python
# Create a channel for each country
# Officials can join and get all updates
# Example: @sdg7_india, @sdg7_kenya, etc.
```

---

## 🔄 Integration with Your Existing System

### Update Your Email Alert System
```python
# In sustainable_energy/ml_models/email_alerts.py

from telegram_alerts import send_telegram_alert

def send_alert(country, access, status):
    # Send email (existing)
    send_email_alert(country, access, status)
    
    # Also send Telegram (new!)
    send_telegram_alert(country, access, status)
    
    # Best of both worlds!
```

---

## 💰 Cost Comparison

| API | Free Tier | Cost After | Best For |
|-----|-----------|------------|----------|
| **Telegram** | ✅ Unlimited FREE | FREE | ⭐ Your project |
| SendGrid | 100/day | $19.95/mo | Email backup |
| Twilio SMS | $15 credit | $0.0075/SMS | Urgent alerts |
| WhatsApp | Limited | $0.005/msg | Business use |
| Slack | Limited | $7.25/user | Organizations |

---

## 🎯 Recommended Setup for Your Project

### Primary: Telegram Bot
- Instant alerts
- Free forever
- Rich formatting
- Easy subscription

### Backup: Email (You already have this!)
- Detailed reports
- Professional documentation
- Works everywhere

### Optional: SMS (Twilio) for Critical Alerts
- Only for emergencies
- When electricity access < 30%
- Direct to ministers

---

## 📝 Next Steps

1. **Create bot** with @BotFather (2 min)
2. **Install library**: `pip install python-telegram-bot`
3. **Copy the code** above
4. **Test with your account** first
5. **Share bot** with country officials
6. **Automate** with your ML predictions

---

## 🔗 Resources

- Telegram Bot API Docs: https://core.telegram.org/bots/api
- Python Library: https://python-telegram-bot.org/
- Bot Examples: https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples

---

## ✅ Why This is Perfect for SDG 7

1. **Free** - No budget needed
2. **Global** - Works in all countries
3. **Instant** - Real-time alerts
4. **Professional** - Rich formatting
5. **Scalable** - Unlimited messages
6. **Easy** - 10 minutes to setup
7. **Reliable** - 99.9% uptime

**Start with Telegram, keep your email system as backup, and you have a perfect alert system!** 📱⚡
