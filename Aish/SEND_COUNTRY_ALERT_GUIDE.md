# Send Email Alert to Specific Country - Quick Guide

## Setup (One-Time)

### Step 1: Get Gmail App Password

1. Go to your Google Account: https://myaccount.google.com/
2. Click on **Security** (left sidebar)
3. Enable **2-Step Verification** if not already enabled
4. Go to **App Passwords**: https://myaccount.google.com/apppasswords
5. Select app: **Mail**
6. Select device: **Windows Computer** (or Other)
7. Click **Generate**
8. Copy the 16-character password (e.g., `abcd efgh ijkl mnop`)

### Step 2: Configure Email Settings

Open `sustainable_energy/email_config.py` and update:

```python
EMAIL_CONFIG = {
    'sender_email': 'electricity.prediction2000@gmail.com',
    'sender_password': 'your-16-char-app-password',  # Paste the App Password here
}

# When ready to send real emails:
ENABLE_ACTUAL_EMAIL_SENDING = True  # Change to True
```

## Usage

### Option 1: Interactive Mode (Recommended)

Run the script and follow the prompts:

```bash
python send_alert_to_country.py
```

You'll be asked:
1. **Country name**: Enter any country (e.g., India, Nigeria, Brazil)
2. **Email address**: Press Enter to use `electricity.prediction2000@gmail.com`
3. **Confirmation**: Type `yes` to send

### Option 2: Send to Multiple Countries

Use the existing script:

```bash
python send_country_alerts.py
```

This will:
- Analyze ALL countries
- Show a summary of their electricity access status
- Ask if you want to send alerts to countries that need attention

## Example Output

```
🌍 SDG 7 Country Alert System
============================================================

Enter country name (e.g., India, Nigeria, Brazil): Nigeria
Enter recipient email [electricity.prediction2000@gmail.com]: 

============================================================
Sending Alert to Nigeria
============================================================

📊 Loading data and analyzing country...
🔮 Predicting electricity access for Nigeria...

📊 Analysis Results:
   Country: Nigeria
   Predicted Access: 62.3%
   Year: 2021
   Status: ⚠️ NEEDS IMPROVEMENT
   Classification: Developing Country

📧 Email Preview:
------------------------------------------------------------
To: electricity.prediction2000@gmail.com
Subject: ⚠️ Action Required: Electricity Access Below Target for Nigeria
------------------------------------------------------------
Dear Energy Ministry of Nigeria,

SDG 7 Progress Alert

Our monitoring system shows Nigeria needs to accelerate electricity access improvements:

📊 Current Status:
- Electricity Access: 62.3%
- Classification: Developing Country
- Status: Below SDG 7 Target
...
------------------------------------------------------------

📤 Send this email? (yes/no): yes

📤 Sending email...
✅ Email sent successfully to electricity.prediction2000@gmail.com!
   Country: Nigeria
   Status: needs_improvement
   Access: 62.3%
```

## Country Status Categories

The system classifies countries into 4 categories:

1. **🚨 CRITICAL** (< 50% access)
   - Urgent action required
   - Emergency measures recommended

2. **⚠️ NEEDS IMPROVEMENT** (50-75% access)
   - Below SDG 7 target
   - Action plan provided

3. **👍 GOOD** (75-95% access)
   - On track
   - Encouragement to continue

4. **🎉 EXCELLENT** (> 95% access)
   - SDG 7 target achieved
   - Congratulations message

## Available Countries

Some example countries in the dataset:
- India
- Nigeria
- Brazil
- China
- United States
- Kenya
- Bangladesh
- Ethiopia
- South Africa
- Indonesia

Run the script with an invalid country name to see the full list!

## Troubleshooting

### Email not sending?

1. **Check email config**: Make sure `sender_password` is set in `email_config.py`
2. **Enable sending**: Set `ENABLE_ACTUAL_EMAIL_SENDING = True`
3. **Check Gmail settings**: Make sure 2FA is enabled and App Password is correct
4. **Check internet**: Make sure you're connected to the internet

### Country not found?

- Check spelling (case-sensitive)
- Run script with invalid name to see available countries
- Some countries may not be in the dataset

### Testing Mode

By default, `TESTING_MODE = True` means all emails go to your test email address.
- This is safe for testing
- Set to `False` when ready to send to actual country emails

## Next Steps

1. Set up your Gmail App Password
2. Update `email_config.py`
3. Run `python send_alert_to_country.py`
4. Enter a country name
5. Review the email preview
6. Type `yes` to send!

Your email `electricity.prediction2000@gmail.com` will receive the alert! 📧
