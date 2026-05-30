# Quick Email Alert Setup Guide

Send electricity access alerts to any country using your email: `electricity.prediction2000@gmail.com`

## 🚀 Quick Start (3 Steps)

### Step 1: Get Gmail App Password (2 minutes)

1. Visit: https://myaccount.google.com/apppasswords
2. Sign in with `electricity.prediction2000@gmail.com`
3. Click **"Select app"** → Choose **"Mail"**
4. Click **"Select device"** → Choose **"Windows Computer"**
5. Click **"Generate"**
6. Copy the 16-character password (looks like: `abcd efgh ijkl mnop`)

**Note**: You need 2-Factor Authentication enabled. If not enabled:
- Go to https://myaccount.google.com/security
- Enable 2-Step Verification first

### Step 2: Configure Email (30 seconds)

Open `sustainable_energy/email_config.py` and update line 8:

```python
'sender_password': 'abcd efgh ijkl mnop',  # Paste your App Password here
```

Then change line 28 to enable sending:

```python
ENABLE_ACTUAL_EMAIL_SENDING = True  # Change False to True
```

### Step 3: Test & Send (1 minute)

Test your setup:
```bash
python test_email_setup.py
```

Send alert to a country:
```bash
python send_alert_to_country.py
```

## 📧 Usage Examples

### Example 1: Send Alert to Nigeria

```bash
python send_alert_to_country.py
```

When prompted:
- Country: `Nigeria`
- Email: Press Enter (uses your email)
- Confirm: `yes`

### Example 2: Send Alert to India

```bash
python send_alert_to_country.py
```

When prompted:
- Country: `India`
- Email: Press Enter
- Confirm: `yes`

### Example 3: Send Alerts to All Countries

```bash
python send_country_alerts.py
```

This will:
- Analyze all countries
- Show which ones need alerts
- Ask for confirmation before sending

## 📊 What Gets Sent?

The system analyzes each country's electricity access and sends appropriate alerts:

| Access Level | Status | Email Type |
|-------------|--------|------------|
| < 50% | 🚨 CRITICAL | Urgent action plan |
| 50-75% | ⚠️ NEEDS IMPROVEMENT | Recommendations |
| 75-95% | 👍 GOOD | Encouragement |
| > 95% | 🎉 EXCELLENT | Congratulations |

## 🔧 Files You Created

1. **send_alert_to_country.py** - Send alert to specific country
2. **test_email_setup.py** - Test your email configuration
3. **SEND_COUNTRY_ALERT_GUIDE.md** - Detailed guide
4. **QUICK_EMAIL_SETUP.md** - This file

## ⚠️ Troubleshooting

### "Authentication Failed"
- Make sure you're using the App Password, not your regular Gmail password
- Check that 2FA is enabled on your Google account

### "Password not configured"
- Update `sender_password` in `sustainable_energy/email_config.py`
- Don't use `'your-app-password'` - use the actual 16-character code

### "Country not found"
- Check spelling (case-sensitive)
- Try: India, Nigeria, Brazil, China, Kenya, Bangladesh

### Email not sending
- Make sure `ENABLE_ACTUAL_EMAIL_SENDING = True`
- Run `python test_email_setup.py` to diagnose

## 📝 Summary

You now have 3 ways to send alerts:

1. **Single Country** (Recommended for testing)
   ```bash
   python send_alert_to_country.py
   ```

2. **Test Email Setup**
   ```bash
   python test_email_setup.py
   ```

3. **All Countries**
   ```bash
   python send_country_alerts.py
   ```

All emails will be sent from and to: `electricity.prediction2000@gmail.com`

Ready to send your first alert? Run:
```bash
python send_alert_to_country.py
```
