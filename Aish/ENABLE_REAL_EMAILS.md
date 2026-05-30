# 📧 Enable Real Email Sending to Your Email

## ✅ Current Setup

Your email `assowmya649@gmail.com` is now configured for:
- ✅ Albania alerts
- ✅ Afghanistan alerts
- ✅ Testing mode (all emails go to your address)

---

## 🔧 To Receive REAL Emails (Not Simulated)

Currently, emails are **SIMULATED** (not actually sent). To receive real emails:

### Step 1: Get Gmail App Password

1. Go to: https://myaccount.google.com/
2. Click **Security** (left sidebar)
3. Enable **2-Step Verification** (if not already enabled)
4. Go to: https://myaccount.google.com/apppasswords
5. Select **Mail** and **Other (Custom name)**
6. Type: "SDG7 Alert System"
7. Click **Generate**
8. Copy the **16-character password** (example: `abcd efgh ijkl mnop`)

### Step 2: Update Email Configuration

Edit `sustainable_energy/email_config.py`:

```python
# SMTP Configuration
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'sender_email': 'assowmya649@gmail.com',
    'sender_password': 'abcd efgh ijkl mnop',  # ← Paste your App Password here
    'sender_name': 'SDG 7 Monitoring System'
}

# Enable actual email sending
ENABLE_ACTUAL_EMAIL_SENDING = True  # ← Change to True
SIMULATION_MODE = False  # ← Change to False
```

### Step 3: Test It

```bash
python send_xgboost_alert_to_country.py Albania
```

You should receive a real email at `assowmya649@gmail.com`!

---

## 🎯 Current Configuration

**File: `country_emails.csv`**
```
Albania,assowmya649@gmail.com  ✅ Updated
Afghanistan,assowmya649@gmail.com  ✅ Already set
```

**File: `sustainable_energy/email_config.py`**
```
TESTING_MODE = True  ✅ All emails go to assowmya649@gmail.com
DUMMY_EMAIL = 'assowmya649@gmail.com'  ✅ Your email
ENABLE_ACTUAL_EMAIL_SENDING = False  ⚠️ Change to True to send real emails
SIMULATION_MODE = True  ⚠️ Change to False to send real emails
```

---

## 🚀 Quick Test (Simulation Mode)

Right now, you can test without real emails:

```bash
python send_xgboost_alert_to_country.py Albania
```

**Output:**
```
✅ Email SIMULATED (not actually sent) to assowmya649@gmail.com
   Subject: 📊 Status Update: Electricity Access Progress in Albania
```

This shows the email **would be sent** to your address, but it's simulated.

---

## 📧 To Send Real Emails

1. **Get Gmail App Password** (Step 1 above)
2. **Update `email_config.py`:**
   ```python
   'sender_password': 'your-16-char-password',  # Paste here
   ENABLE_ACTUAL_EMAIL_SENDING = True
   SIMULATION_MODE = False
   ```
3. **Run:**
   ```bash
   python send_xgboost_alert_to_country.py Albania
   ```
4. **Check your inbox:** `assowmya649@gmail.com`

---

## ⚠️ Important Notes

### Gmail App Password (Not Regular Password!)
- ❌ Don't use your regular Gmail password
- ✅ Use the 16-character App Password from Google

### Security
- Keep your App Password secret
- Don't share `email_config.py` with others
- Add `email_config.py` to `.gitignore`

### Testing Mode
- `TESTING_MODE = True` → All emails go to `DUMMY_EMAIL`
- `TESTING_MODE = False` → Emails go to addresses in `country_emails.csv`

---

## 🎯 Summary

**Current Status:**
- ✅ Albania email updated to `assowmya649@gmail.com`
- ✅ Testing mode enabled (all emails to your address)
- ⚠️ Simulation mode (emails not actually sent)

**To receive real emails:**
1. Get Gmail App Password
2. Update `email_config.py` with password
3. Set `ENABLE_ACTUAL_EMAIL_SENDING = True`
4. Set `SIMULATION_MODE = False`
5. Run the script

**Test command:**
```bash
python send_xgboost_alert_to_country.py Albania
```

---

## 📞 Need Help?

If you have issues:
1. Make sure 2-Step Verification is enabled in Gmail
2. Use App Password (not regular password)
3. Check spam folder for emails
4. Verify email address is correct in `country_emails.csv`

---

**Your email is now configured! Follow the steps above to enable real email sending.** 📧✅
