# Custom Email Message Feature - Complete Guide

## ✅ What's New

The Email Alert System now supports **custom email messages**! You can type your own message and it will be sent to the selected countries.

## 🎯 How to Use

### Step 1: Access Admin Panel
1. Go to http://127.0.0.1:8000/
2. Click on **"🔐 Admin Panel - Email Alert System"**
3. Login with admin credentials

### Step 2: Navigate to Email Alert System
1. From the Admin Panel, click **"Send Alerts"**
2. You'll see the Email Alert System page

### Step 3: Customize Your Message

#### Option A: Use Quick Templates
- Click one of the template buttons:
  - **⚠️ Urgent Alert** - For critical situations
  - **⏰ Reminder** - For follow-up messages
  - **✅ Congratulations** - For positive updates
  - **📊 Status Update** - For general updates

#### Option B: Write Custom Message
1. **Email Subject** (optional):
   - Type your custom subject line
   - Leave empty to use automatic subject based on country status
   
2. **Alert Message** (required):
   - Type your custom message in the text area
   - This message will be sent to ALL selected countries
   - Leave empty to use automatic message based on electricity access status

### Step 4: Select Countries
- Check the countries you want to send the email to
- Or click **"Send to All Countries"** to send to everyone

### Step 5: Send
- Click **"📧 Send Alerts to Selected Countries"**
- Your custom message will be sent!

## 📧 Example Custom Messages

### Example 1: Urgent Alert
```
Subject: Urgent: Electricity Access Crisis

Message:
Dear Energy Ministry,

We have detected a critical decline in electricity access in your country.
Current situation requires urgent intervention.

Key Points:
• Current situation requires urgent intervention
• Immediate policy review recommended
• Technical assistance available upon request

Please contact us at your earliest convenience to discuss action plans.

Best regards,
SDG 7 Monitoring Team
```

### Example 2: Congratulations
```
Subject: Congratulations on Energy Progress!

Message:
Dear Energy Ministry,

Congratulations! Your country has made excellent progress in electricity access.

We commend your efforts and would like to:
• Share your success story with other nations
• Provide additional support for continued growth
• Discuss best practices

Keep up the great work!

Best regards,
SDG 7 Monitoring Team
```

### Example 3: Status Update
```
Subject: Monthly Energy Access Report

Message:
Dear Energy Ministry,

This is your monthly electricity access status update.

Current Status: [Automatically determined]
Access Rate: [Automatically calculated]

We recommend:
1. Continue current policies
2. Monitor progress monthly
3. Report any significant changes

For questions, please contact our support team.

Best regards,
SDG 7 Monitoring Team
```

## 🔧 Technical Details

### How It Works
1. **Frontend**: User types message in the form
2. **JavaScript**: Captures the custom subject and message
3. **API**: Sends data to `/api/send-email-alerts-selected/`
4. **Backend**: 
   - If custom message provided → Uses custom message
   - If empty → Generates automatic message based on country status
5. **Email**: Sends to selected countries

### API Request Format
```json
{
  "countries": ["Albania", "Kenya", "India"],
  "custom_subject": "Your Custom Subject",
  "custom_message": "Your custom message here..."
}
```

### Automatic vs Custom Messages

| Field | If Empty | If Provided |
|-------|----------|-------------|
| Subject | Auto-generated based on status | Uses your custom subject |
| Message | Auto-generated with country data | Uses your custom message |

## 🎨 Features

✅ **Custom Subject Line** - Write your own email subject
✅ **Custom Message Body** - Full control over email content
✅ **Quick Templates** - Pre-written templates for common scenarios
✅ **Character Counter** - Track subject line length (max 200)
✅ **Multi-Country Support** - Send same message to multiple countries
✅ **Fallback to Auto** - Leave empty to use automatic messages
✅ **Email Logging** - All sent emails are logged in the database

## 📊 Admin Panel Features

The new Admin Panel provides:
- **Email Alert System** - Send custom alerts
- **Email Logs** - View history of sent emails
- **Single Country Alert** - Send to one country
- **Custom Alert** - Create custom alerts
- **XGBoost Alerts** - AI-powered automatic alerts

## 🔐 Access Control

- Admin Panel requires login
- Only staff users can access
- Login at: http://127.0.0.1:8000/admin-login/
- Logout redirects to login page

## 🚀 Quick Start

1. **Start Server**:
   ```bash
   cd sustainable_energy
   python manage.py runserver
   ```

2. **Access Dashboard**:
   - Go to http://127.0.0.1:8000/

3. **Login to Admin**:
   - Click "Admin Panel"
   - Enter credentials

4. **Send Custom Email**:
   - Click "Send Alerts"
   - Type your message
   - Select countries
   - Click "Send"

## ✨ Summary

Now you have complete control over email content! Type whatever message you want in the "Alert Message" field, and it will be sent to the selected countries. The system is flexible - use custom messages when needed, or leave it empty for automatic messages based on country data.

**Dashboard URL**: http://127.0.0.1:8000/
**Admin Panel**: http://127.0.0.1:8000/admin-panel/
**Email Alerts**: http://127.0.0.1:8000/objective8/
