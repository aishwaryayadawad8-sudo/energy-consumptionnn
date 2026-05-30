# 🔐 Administrator Email Alert Setup Guide

## Overview

The email alert system is now **administrator-only**. Only logged-in admin users can send email alerts to countries.

## Step 1: Create Administrator Account

Run this command to create an admin account:

```bash
python create_admin.py
```

You'll be prompted to enter:
- Username (e.g., "admin")
- Email (your email address)
- Password (choose a strong password)

## Step 2: Configure Your Email

Edit the file: `sustainable_energy/email_config.py`

Replace these values:
```python
'sender_email': 'your-actual-email@gmail.com',
'sender_password': 'your-16-char-app-password',
```

### For Gmail Users:

1. **Enable 2-Factor Authentication**
   - Go to: https://myaccount.google.com/security
   - Enable 2-Step Verification

2. **Create App Password**
   - Go to: https://myaccount.google.com/apppasswords
   - Select "Mail" and your device
   - Copy the 16-character password
   - Paste it in `email_config.py`

3. **Update sender_email**
   - Replace with your Gmail address

### For Other Email Providers:

**Outlook/Hotmail:**
```python
'smtp_server': 'smtp.office365.com',
'smtp_port': 587,
```

**Yahoo:**
```python
'smtp_server': 'smtp.mail.yahoo.com',
'smtp_port': 587,
```

## Step 3: Login as Administrator

1. **Start the Django server** (if not running):
   ```bash
   cd sustainable_energy
   python manage.py runserver
   ```

2. **Login to Django Admin**:
   - Go to: http://127.0.0.1:8000/admin/
   - Enter your admin username and password
   - You're now logged in as administrator

3. **Access the Dashboard**:
   - Go to: http://127.0.0.1:8000/dashboard/
   - You'll see the "Send Email Alerts" section (admin only)

## Step 4: Send Email Alerts

1. **On the dashboard**, you'll see:
   - "Send Email Alerts to Countries" section with **Admin Only** badge
   - Your username displayed
   - "Send Email Alerts to All Countries" button

2. **Click the button**:
   - Confirm the action
   - System analyzes all countries
   - Sends personalized emails based on electricity access
   - Shows popup with results

## Security Features

✅ **Authentication Required** - Must be logged in
✅ **Admin Only** - Only staff/superuser can send emails
✅ **Confirmation Dialog** - Prevents accidental sends
✅ **Audit Trail** - All actions logged

## Email Alert Categories

The system sends different emails based on electricity access:

- **🚨 Critical** (< 50%) → Urgent action plan
- **⚠️ Needs Improvement** (50-75%) → Recommendations
- **👍 Good** (75-95%) → Encouragement
- **🎉 Excellent** (> 95%) → Congratulations

## Testing Without Sending Real Emails

By default, emails are **simulated** (not actually sent). To enable real sending:

1. Edit `sustainable_energy/email_config.py`
2. Set: `ENABLE_ACTUAL_EMAIL_SENDING = True`
3. Make sure your email credentials are correct

## Troubleshooting

### "Authentication required" error
- You're not logged in
- Solution: Login at http://127.0.0.1:8000/admin/

### "Access denied" error
- Your account is not an administrator
- Solution: Run `python create_admin.py` to make your account admin

### Email not sending
- Check `email_config.py` settings
- Verify Gmail App Password is correct
- Check if 2FA is enabled on Gmail
- Check `ENABLE_ACTUAL_EMAIL_SENDING` is True

### Button not visible
- You're not logged in as admin
- Solution: Login at /admin/ first

## Non-Admin Users

Regular users (non-admin) will **NOT see** the email alert section. It's completely hidden from them for security.

## Summary

1. ✅ Create admin account: `python create_admin.py`
2. ✅ Configure email in `email_config.py`
3. ✅ Login at http://127.0.0.1:8000/admin/
4. ✅ Access dashboard at http://127.0.0.1:8000/dashboard/
5. ✅ Send emails (admin only)

Your email alert system is now secure and administrator-only!
