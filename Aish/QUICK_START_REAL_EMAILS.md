# 🚀 Quick Start: Send Real Emails to Your Address

## ✅ Configuration Complete!

Your system is configured to send **REAL emails** to `assowmya649@gmail.com` for:
- ✅ Albania
- ✅ Afghanistan

---

## 📧 Setup Gmail (One Time - 5 Minutes)

### Step 1: Get App Password

1. Visit: **https://myaccount.google.com/apppasswords**
2. Sign in with: `assowmya649@gmail.com`
3. Generate App Password for "Mail"
4. Copy the 16-character password

### Step 2: Configure Password

Run this command and paste your App Password:
```bash
python setup_gmail_password.py
```

**OR** manually edit `sustainable_energy/email_config.py`:
```python
'sender_password': 'your-16-char-password',  # Paste here
```

---

## 🎯 Send Real Emails

### Test with Albania:
```bash
python send_xgboost_alert_to_country.py Albania
```

### Test with Afghanistan:
```bash
python send_xgboost_alert_to_country.py Afghanistan
```

### Send Automatic Alerts:
```bash
python auto_send_xgboost_alerts.py
```

---

## 📬 Check Your Inbox

After running the command, check:
- **Email:** `assowmya649@gmail.com`
- **Subject:** "📊 Status Update: Electricity Access Progress in [Country]"
- **From:** SDG 7 Monitoring System

**If not in inbox, check spam folder!**

---

## ✅ Current Configuration

```
✅ Albania → assowmya649@gmail.com
✅ Afghanistan → assowmya649@gmail.com
✅ Real Email Mode: ENABLED
✅ Simulation Mode: DISABLED
⚠️ Gmail Password: NEEDS SETUP (run setup_gmail_password.py)
```

---

## 🎯 Quick Commands

```bash
# 1. Setup Gmail password (one time)
python setup_gmail_password.py

# 2. Send to Albania
python send_xgboost_alert_to_country.py Albania

# 3. Send to Afghanistan  
python send_xgboost_alert_to_country.py Afghanistan

# 4. Send automatic alerts (both countries)
python auto_send_xgboost_alerts.py
```

---

## 📧 What You'll Receive

**Real email with:**
- XGBoost ML predictions (99.16% accuracy)
- Current electricity access percentage
- Status classification
- Detailed recommendations
- Professional formatting

**No test messages, no simulation - REAL emails only!** ✅

---

**Ready to send? Just configure your Gmail App Password and run the commands!** 🚀
