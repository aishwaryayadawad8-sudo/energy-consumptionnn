# Send Email Alerts to Selected Countries - Complete Guide

## Overview

This system allows you to send electricity access alerts to specific countries using their official email addresses from `country_emails.csv`.

## Files Created

1. **country_emails.csv** - Contains 186 country email addresses
2. **send_email_by_country.py** - Script to send alerts to selected countries
3. **Updated email_alerts.py** - Now loads emails from CSV automatically

## Quick Start

### Step 1: Setup Email (One-Time)

1. Get Gmail App Password:
   - Visit: https://myaccount.google.com/apppasswords
   - Sign in with `electricity.prediction2000@gmail.com`
   - Generate App Password for "Mail"
   - Copy the 16-character code

2. Update `sustainable_energy/email_config.py`:
   ```python
   'sender_password': 'your-16-char-password',  # Line 8
   ENABLE_ACTUAL_EMAIL_SENDING = True  # Line 28
   ```

### Step 2: Send Alerts to Countries

Run the script:
```bash
python send_email_by_country.py
```

Enter countries (comma-separated):
```
Enter countries: India, Nigeria, Brazil, Kenya
```

Review the analysis and confirm to send!

## Usage Examples

### Example 1: Send to 3 Countries

```bash
python send_email_by_country.py
```

Input:
```
Enter countries: Nigeria, India, Bangladesh
```

Output:
```
🌍 SDG 7 Country Alert System
============================================================

✅ Loaded 186 country email addresses
📊 Loading data and training models...
🔮 Analyzing selected countries...

⚠️ Nigeria
   Access: 62.3%
   Status: NEEDS_IMPROVEMENT
   Email: nigeria@sdg7_alerts.org

👍 India
   Access: 84.5%
   Status: GOOD
   Email: india@sdg7_alerts.org

🚨 Bangladesh
   Access: 45.2%
   Status: CRITICAL
   Email: bangladesh@sdg7_alerts.org

============================================================
📋 Summary: 3 countries ready for alerts
============================================================

📤 Send email alerts to these countries? (yes/no): yes

📤 Sending emails...
✅ Email SIMULATED to nigeria@sdg7_alerts.org
✅ Email SIMULATED to india@sdg7_alerts.org
✅ Email SIMULATED to bangladesh@sdg7_alerts.org

============================================================
✅ Successfully sent 3/3 emails!
============================================================
```

### Example 2: Send to African Countries

```bash
python send_email_by_country.py
```

Input:
```
Enter countries: Nigeria, Kenya, Ethiopia, Ghana, South Africa
```

### Example 3: Send to Asian Countries

```bash
python send_email_by_country.py
```

Input:
```
Enter countries: India, China, Bangladesh, Pakistan, Indonesia
```

## Available Countries (186 Total)

The `country_emails.csv` file contains emails for:

**Africa**: Nigeria, Kenya, Ethiopia, Ghana, South Africa, Egypt, Morocco, etc.
**Asia**: India, China, Bangladesh, Pakistan, Indonesia, Thailand, etc.
**Europe**: Germany, France, United Kingdom, Italy, Spain, etc.
**Americas**: United States, Brazil, Canada, Mexico, Argentina, etc.
**Oceania**: Australia, New Zealand, Fiji, Papua New Guinea, etc.

## Email Format

All emails follow the pattern: `country@sdg7_alerts.org`

Examples:
- India → `india@sdg7_alerts.org`
- Nigeria → `nigeria@sdg7_alerts.org`
- United States → `united_states@sdg7_alerts.org`

## Alert Categories

The system automatically classifies countries and sends appropriate emails:

| Access % | Status | Email Type | Example Countries |
|----------|--------|------------|-------------------|
| < 50% | 🚨 CRITICAL | Urgent action plan | Chad, South Sudan, Burundi |
| 50-75% | ⚠️ NEEDS IMPROVEMENT | Recommendations | Nigeria, Kenya, Bangladesh |
| 75-95% | 👍 GOOD | Encouragement | India, Brazil, Indonesia |
| > 95% | 🎉 EXCELLENT | Congratulations | USA, Germany, Japan |

## Testing Mode

By default, emails are sent to your test email (`electricity.prediction2000@gmail.com`) instead of actual country emails.

To send to actual country emails:
1. Open `sustainable_energy/email_config.py`
2. Set `TESTING_MODE = False` (Line 26)
3. Set `ENABLE_ACTUAL_EMAIL_SENDING = True` (Line 28)

## Advanced Usage

### Send to All Countries

Use the existing script:
```bash
python send_country_alerts.py
```

This analyzes ALL countries and sends alerts to those needing attention.

### Send to Single Country

```bash
python send_alert_to_country.py
```

Then enter one country name when prompted.

### Custom Email List

To use different email addresses:
1. Edit `country_emails.csv`
2. Update the Email column with new addresses
3. Save the file
4. Run the script again

## Troubleshooting

### "Country not found in dataset"
- Check spelling (case-sensitive)
- Make sure country exists in `global-data-on-sustainable-energy.csv`
- Try variations: "United States" vs "USA"

### "No email address found"
- Check if country is in `country_emails.csv`
- Verify spelling matches exactly

### "Authentication Failed"
- Update `sender_password` in `email_config.py`
- Use App Password, not regular Gmail password
- Enable 2FA on Google account

### Emails not sending
- Set `ENABLE_ACTUAL_EMAIL_SENDING = True`
- Check internet connection
- Run `python test_email_setup.py` to diagnose

## Email Content Preview

### Critical Alert (< 50% access)
```
Subject: 🚨 URGENT: Critical Electricity Access Alert for Chad

Dear Energy Ministry of Chad,

CRITICAL ALERT: SDG 7 Monitoring System

Our AI-powered monitoring system has identified that Chad has 
critically low electricity access:

📊 Current Status:
- Electricity Access: 12.5%
- Classification: Developing Country
- Status: CRITICAL - Immediate Action Required

⚠️ IMMEDIATE ACTION PLAN:
1. Deploy mobile solar units to remote areas
2. Establish emergency power distribution centers
3. Partner with international energy organizations
...
```

### Needs Improvement (50-75% access)
```
Subject: ⚠️ Action Required: Electricity Access Below Target for Nigeria

Dear Energy Ministry of Nigeria,

SDG 7 Progress Alert

Our monitoring system shows Nigeria needs to accelerate 
electricity access improvements:

📊 Current Status:
- Electricity Access: 62.3%
- Status: Below SDG 7 Target

💡 RECOMMENDED ACTIONS:
1. Expand grid infrastructure to rural areas
2. Implement renewable energy projects
...
```

### Excellent (> 95% access)
```
Subject: 🎉 Congratulations: Germany Achieves Excellent Electricity Access!

Dear Energy Ministry of Germany,

CONGRATULATIONS! 🎉

We are pleased to inform you that Germany has achieved 
excellent electricity access:

📊 Current Status:
- Electricity Access: 100.0%
- Status: EXCELLENT - SDG 7 Target Achieved!
...
```

## Summary

You now have a complete system to:
1. ✅ Load 186 country email addresses from CSV
2. ✅ Select specific countries to send alerts to
3. ✅ Automatically analyze electricity access
4. ✅ Send customized emails based on country status
5. ✅ Test safely before sending real emails

Ready to send? Run:
```bash
python send_email_by_country.py
```
