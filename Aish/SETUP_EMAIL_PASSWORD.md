# 🔧 FIX EMAIL ALERTS - Setup Gmail App Password

## ❌ PROBLEM: All Emails Showing "Failed" Status

Your emails are failing because the Gmail App Password is not configured correctly.

## ✅ SOLUTION: Generate Gmail App Password

### Step 1: Enable 2-Factor Authentication
1. Go to: https://myaccount.google.com/security
2. Click "2-Step Verification"
3. Follow the steps to enable it (if not already enabled)

### Step 2: Generate App Password
1. Go to: https://myaccount.google.com/apppasswords
2. Sign in with your Gmail account: `assowmya649@gmail.com`
3. In "Select app" dropdown, choose "Mail"
4. In "Select device" dropdown, choose "Windows Computer"
5. Click "Generate"
6. **COPY THE 16-CHARACTER PASSWORD** (it will look like: `abcd efgh ijkl mnop`)

### Step 3: Update Configuration
1. Open file: `sustainable_energy/email_config.py`
2. Find this line:
   ```python
   'sender_password': 'qlxk ufqo qqxe iqxe',
   ```
3. Replace with your actual 16-character App Password:
   ```python
   'sender_password': 'your-actual-app-password-here',
   ```

### Step 4: Test Email Setup
Run this command to verify:
```bash
python test_email_setup.py
```

You should see:
```
✅ Email sent successfully!
```

### Step 5: Restart Django Server
```bash
# Stop the server (Ctrl+C)
# Then restart:
python sustainable_energy/manage.py runserver
```

### Step 6: Test Sending Alerts
1. Go to: http://localhost:8000/objective8/
2. Select a country (e.g., Albania)
3. Click "Send Alerts"
4. Check Email Logs - status should now show "success" ✅

---

## 🔍 Why This Happens

Gmail requires an "App Password" for third-party applications. Regular Gmail passwords don't work for security reasons.

The error occurs because:
1. The placeholder password `'your-app-password'` is not valid
2. Gmail rejects authentication attempts
3. All emails fail with authentication error

---

## 📝 Quick Reference

**Your Email:** assowmya649@gmail.com  
**SMTP Server:** smtp.gmail.com  
**Port:** 587  
**App Password:** (Generate from link above)

---

## ⚠️ Important Notes

1. **Never share your App Password** - treat it like a regular password
2. **Keep 2FA enabled** - required for App Passwords
3. **Use App Password, not regular password** - regular Gmail password won't work
4. **Remove spaces** - App Password can be entered with or without spaces

---

## 🆘 Still Having Issues?

If emails still fail after setup:

1. **Check if 2FA is enabled:**
   - Go to: https://myaccount.google.com/security
   - Look for "2-Step Verification" - should be ON

2. **Regenerate App Password:**
   - Delete old App Password
   - Generate a new one
   - Update config file

3. **Check Gmail settings:**
   - Go to Gmail Settings → Forwarding and POP/IMAP
   - Enable IMAP access

4. **Test with simple script:**
   ```bash
   python send_email_simple.py
   ```

---

## ✅ After Setup

Once configured correctly, you'll see:
- ✅ Status: "success" in Email Logs
- 📧 Actual emails delivered to recipients
- 🎉 No more "failed" status!
