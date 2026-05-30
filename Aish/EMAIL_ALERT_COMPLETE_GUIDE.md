# 📧 Complete Email Alert System Guide

## ✅ What's Been Implemented

Your email alert system is now complete with:

1. **Admin-Only Access** - Only administrators can send emails
2. **Dummy Email Testing** - All emails go to your test email
3. **Detailed Reports** - See which countries received what emails
4. **Email Configuration** - Easy setup with your Gmail

## 🚀 Quick Setup (3 Steps)

### Step 1: Configure Your Email

Edit `sustainable_energy/email_config.py`:

```python
EMAIL_CONFIG = {
    'sender_email': 'your-actual-email@gmail.com',  # Your Gmail
    'sender_password': 'your-16-char-app-password',  # Gmail App Password
}

TESTING_MODE = True  # Keep this True for testing
DUMMY_EMAIL = 'your-test-email@gmail.com'  # Your dummy/test email
ENABLE_ACTUAL_EMAIL_SENDING = True  # Set to True to actually send
```

**Get Gmail App Password:**
1. Go to https://myaccount.google.com/apppasswords
2. Create password for "Mail"
3. Copy the 16-character code
4. Paste in `sender_password`

### Step 2: Create Admin Account

```bash
python create_admin.py
```

Enter:
- Username: `admin`
- Email: your email
- Password: choose a strong password

### Step 3: Login and Test

1. **Login as admin:**
   - Go to: http://127.0.0.1:8000/admin/
   - Enter username and password

2. **Access dashboard:**
   - Go to: http://127.0.0.1:8000/dashboard/
   - You'll see "Send Email Alerts" section

3. **Send test emails:**
   - Click "Send Email Alerts to All Countries"
   - Confirm
   - Check your dummy email inbox!

## 📧 How It Works

### Testing Mode (Current Setup)

When `TESTING_MODE = True`:
- **ALL emails go to your dummy email**
- Each email shows which country it's for
- Subject line includes: `[TEST - For: CountryName]`
- Body includes original recipient info

**Example email you'll receive:**
```
Subject: [TEST - For: Kenya] ⚠️ Action Required: Electricity Access Below Target for Kenya

ORIGINAL RECIPIENT: kenya.energy@gov.ke
COUNTRY: Kenya

============================================================

Dear Energy Ministry of Kenya,
[rest of email content]
```

### Production Mode

When `TESTING_MODE = False`:
- Emails go to actual country addresses
- No test prefixes
- Real deployment

## 📊 Email Categories

The system sends different emails based on electricity access:

| Status | Access % | Email Type | Icon |
|--------|----------|------------|------|
| Critical | < 50% | Urgent action plan | 🚨 |
| Needs Improvement | 50-75% | Recommendations | ⚠️ |
| Good | 75-95% | Encouragement | 👍 |
| Excellent | > 95% | Congratulations | 🎉 |

## 📋 Countries That Will Receive Emails

Based on the latest data, these countries will receive emails:

**🎉 Excellent (7 countries):**
- Afghanistan (97.7%)
- Bangladesh (96.2%)
- Brazil (100%)
- China (100%)
- Germany (100%)
- India (99%)
- Japan (100%)

**⚠️ Needs Improvement (2 countries):**
- Kenya (71.4%)
- Nigeria (55.4%)

**Total: 9 emails** will be sent to your dummy email address!

## 🔍 What You'll See

### In Dashboard:
1. Confirmation dialog
2. Loading spinner
3. Success popup with:
   - Total alerts sent
   - Countries by status (Critical/Needs Improvement/Excellent)
   - Email addresses
   - Access percentages

### In Your Dummy Email Inbox:
- 9 separate emails
- Each labeled with country name
- Full email content as it would be sent
- Original recipient information

## 🛠️ Troubleshooting

### "Authentication required" Error
**Problem:** Not logged in  
**Solution:** Login at http://127.0.0.1:8000/admin/

### "Access denied" Error
**Problem:** Not an administrator  
**Solution:** Run `python create_admin.py` to create/update admin account

### Email Button Not Visible
**Problem:** Not logged in as admin  
**Solution:** Login at /admin/ first, then go to /dashboard/

### Emails Not Sending
**Problem:** Email configuration  
**Solutions:**
1. Check `ENABLE_ACTUAL_EMAIL_SENDING = True`
2. Verify Gmail App Password is correct
3. Check sender_email is your Gmail
4. Ensure 2FA is enabled on Gmail

### No Emails in Inbox
**Problem:** Wrong dummy email or not sending  
**Solutions:**
1. Check `DUMMY_EMAIL` in email_config.py
2. Check spam folder
3. Verify `ENABLE_ACTUAL_EMAIL_SENDING = True`

## 📝 Testing Checklist

- [ ] Configure email_config.py with your Gmail
- [ ] Set DUMMY_EMAIL to your test email
- [ ] Set ENABLE_ACTUAL_EMAIL_SENDING = True
- [ ] Create admin account with create_admin.py
- [ ] Login at /admin/
- [ ] Go to /dashboard/
- [ ] See "Send Email Alerts" section
- [ ] Click button and confirm
- [ ] Check dummy email inbox
- [ ] Verify 9 emails received

## 🎯 Summary

Your system is ready! Here's what happens:

1. **Admin logs in** → Can access email feature
2. **Clicks "Send Alerts"** → System analyzes 127 countries
3. **Sends 9 emails** → All to your dummy email
4. **Shows report** → Which countries received what
5. **You check inbox** → See all 9 test emails

**Current Status:**
- ✅ Admin authentication working
- ✅ Email system configured
- ✅ Testing mode enabled
- ✅ 9 countries will receive emails
- ✅ All emails go to your dummy address
- ✅ Detailed reports in dashboard

Ready to test! 🚀
