# Email Alert System - Quick Reference

## 🚀 Quick Commands

### List All Countries
```bash
python list_countries.py
```
Shows all 186 countries with their email addresses.

### Send to Selected Countries
```bash
python send_email_by_country.py
```
Enter countries like: `India, Nigeria, Brazil`

### Send to Single Country
```bash
python send_alert_to_country.py
```
Enter one country when prompted.

### Send to All Countries
```bash
python send_country_alerts.py
```
Analyzes and sends to all countries needing alerts.

### Test Email Setup
```bash
python test_email_setup.py
```
Verifies your email configuration works.

## ⚙️ Configuration Files

### Email Settings
**File**: `sustainable_energy/email_config.py`

**Line 8** - Your Gmail App Password:
```python
'sender_password': 'your-16-char-password',
```

**Line 26** - Testing Mode (sends to your email):
```python
TESTING_MODE = True  # False to send to actual country emails
```

**Line 28** - Enable Sending:
```python
ENABLE_ACTUAL_EMAIL_SENDING = True  # False to simulate only
```

### Country Emails
**File**: `country_emails.csv`

Format:
```csv
Country,Email
India,india@sdg7_alerts.org
Nigeria,nigeria@sdg7_alerts.org
```

## 📧 Email Addresses

**Your Email**: `electricity.prediction2000@gmail.com`

**Country Emails**: All follow pattern `country@sdg7_alerts.org`
- India → india@sdg7_alerts.org
- Nigeria → nigeria@sdg7_alerts.org
- United States → united_states@sdg7_alerts.org

## 🎯 Alert Types

| Access % | Status | Icon |
|----------|--------|------|
| < 50% | CRITICAL | 🚨 |
| 50-75% | NEEDS IMPROVEMENT | ⚠️ |
| 75-95% | GOOD | 👍 |
| > 95% | EXCELLENT | 🎉 |

## 📝 Example Usage

### Send to 3 Countries
```bash
python send_email_by_country.py
```
Input: `Nigeria, India, Kenya`

### Send to Region
```bash
python send_email_by_country.py
```
Input: `Nigeria, Ghana, Kenya, Ethiopia, South Africa`

## 🔧 Setup Steps

1. **Get App Password** (2 min)
   - https://myaccount.google.com/apppasswords
   - Generate for "Mail"
   - Copy 16-character code

2. **Update Config** (30 sec)
   - Edit `sustainable_energy/email_config.py`
   - Paste password on line 8
   - Set `ENABLE_ACTUAL_EMAIL_SENDING = True` on line 28

3. **Test** (1 min)
   ```bash
   python test_email_setup.py
   ```

4. **Send** (1 min)
   ```bash
   python send_email_by_country.py
   ```

## ⚠️ Common Issues

**"Authentication Failed"**
→ Update `sender_password` with App Password

**"Country not found"**
→ Check spelling, run `python list_countries.py`

**"No email address"**
→ Country not in `country_emails.csv`

**Emails not sending**
→ Set `ENABLE_ACTUAL_EMAIL_SENDING = True`

## 📚 Documentation

- **SEND_EMAIL_TO_COUNTRIES_GUIDE.md** - Complete guide
- **QUICK_EMAIL_SETUP.md** - Setup instructions
- **SEND_COUNTRY_ALERT_GUIDE.md** - Detailed documentation

## 🎓 Example Countries

**High Access (> 95%)**:
- United States, Germany, Japan, France, United Kingdom

**Good (75-95%)**:
- India, Brazil, China, Indonesia, Mexico

**Needs Improvement (50-75%)**:
- Nigeria, Kenya, Bangladesh, Pakistan, Ghana

**Critical (< 50%)**:
- Chad, South Sudan, Burundi, Central African Republic

## 💡 Tips

1. **Test First**: Use `TESTING_MODE = True` to send to your email
2. **Start Small**: Test with 1-2 countries first
3. **Check Spelling**: Country names are case-sensitive
4. **View List**: Run `python list_countries.py` to see all options
5. **Verify Setup**: Run `python test_email_setup.py` before sending

## 📞 Quick Help

**See all countries**:
```bash
python list_countries.py
```

**Test email**:
```bash
python test_email_setup.py
```

**Send to countries**:
```bash
python send_email_by_country.py
```

That's it! You're ready to send electricity access alerts to any country! 🌍⚡
