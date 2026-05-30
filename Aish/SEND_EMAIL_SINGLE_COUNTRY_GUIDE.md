# ✉️ Send Email to Single Country - User Guide

## Overview
A new dedicated page to send email alerts to one country at a time. This is perfect when you want to send an email to a specific country without selecting multiple countries.

## Access the Page

### Option 1: From Home Page
1. Go to: http://127.0.0.1:8000/
2. Look for the card: **"✉️ Send Email to Country"**
3. Click on it

### Option 2: Direct URL
```
http://127.0.0.1:8000/send-email-country/
```

## How to Use

### Step 1: Select Country
1. Open the page
2. Click on the dropdown menu
3. Select a country from the list
4. All countries are sorted alphabetically

### Step 2: View Country Information
Once you select a country, you'll see:
- **Country Name**: The selected country
- **Email Address**: Where the email will be sent
- **Predicted Access**: Electricity access percentage
- **Alert Type**: Critical/Needs Improvement/Good/Excellent

### Step 3: Send Email
1. Review the country information
2. Click the **"Send Email Alert"** button
3. Wait for confirmation
4. See success or error message

## Features

### 🎯 Single Country Focus
- Select one country at a time
- See detailed prediction before sending
- Instant feedback

### 📊 Real-Time Predictions
- Shows predicted electricity access
- Displays alert type with color coding
- Shows recipient email address

### ✅ Instant Confirmation
- Success message with details
- Error messages if something goes wrong
- Loading indicator while sending

### 🎨 Color-Coded Alert Types
- **🔴 Critical** - Access below 50%
- **🟡 Needs Improvement** - Access 50-75%
- **🔵 Good** - Access 75-95%
- **🟢 Excellent** - Access above 95%

## Page Layout

```
┌─────────────────────────────────────────────────────────┐
│ ← Back to Home                                          │
├─────────────────────────────────────────────────────────┤
│ 📧 Send Email Alert to Country                         │
│ Select a country and send electricity access alert      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ 🌍 Select Country                                       │
│ [Dropdown: Choose a Country ▼]                         │
│                                                         │
│ ┌─────────────────────────────────────────────────┐   │
│ │ Country Information                             │   │
│ │ Country: Albania                                │   │
│ │ Email: albania.energy@gov.al                    │   │
│ │ Predicted Access: 45.5%                         │   │
│ │ Alert Type: 🔴 Critical                         │   │
│ └─────────────────────────────────────────────────┘   │
│                                                         │
│ [✈️ Send Email Alert]                                  │
│                                                         │
├─────────────────────────────────────────────────────────┤
│ ℹ️ How It Works                                        │
│ 1. Select a Country                                    │
│ 2. View Prediction                                     │
│ 3. Send Email                                          │
│ 4. Get Confirmation                                    │
└─────────────────────────────────────────────────────────┘
```

## Example Usage

### Example 1: Sending to Albania
1. Select "Albania" from dropdown
2. See:
   - Email: albania.energy@gov.al
   - Access: 45.5%
   - Alert: 🔴 Critical
3. Click "Send Email Alert"
4. See: "✅ Email Sent Successfully!"

### Example 2: Sending to Kenya
1. Select "Kenya" from dropdown
2. See:
   - Email: kenya.energy@gov.ke
   - Access: 68.2%
   - Alert: 🟡 Needs Improvement
3. Click "Send Email Alert"
4. See: "✅ Email Sent Successfully!"

## Success Message

When email is sent successfully:
```
┌─────────────────────────────────────────────────────────┐
│ ✅ Email Sent Successfully!                             │
│                                                         │
│ Country: Albania                                        │
│ Total Alerts Sent: 1                                   │
│ The email has been sent to the country's energy        │
│ ministry.                                               │
└─────────────────────────────────────────────────────────┘
```

## Error Message

If something goes wrong:
```
┌─────────────────────────────────────────────────────────┐
│ ❌ Error Sending Email                                  │
│                                                         │
│ Failed to send email: Connection timeout               │
└─────────────────────────────────────────────────────────┘
```

## Differences from Objective 8

| Feature | Send Email to Country | Objective 8 (Multiple) |
|---------|----------------------|------------------------|
| Countries | One at a time | Multiple selection |
| Interface | Simple dropdown | Multi-select with checkboxes |
| Use Case | Quick single email | Bulk email sending |
| Login Required | No | Yes (Admin only) |
| Email Logs | Yes (automatic) | Yes (automatic) |

## When to Use This Page

### Use "Send Email to Country" when:
- ✅ You want to send to just one country
- ✅ You want a quick, simple interface
- ✅ You want to see prediction details first
- ✅ You don't need admin login

### Use "Objective 8" when:
- ✅ You want to send to multiple countries
- ✅ You need admin access control
- ✅ You want to send bulk emails
- ✅ You need advanced features

## Technical Details

### URL Route
```python
path('send-email-country/', views.send_email_single_country, name='send_email_single_country')
```

### View Function
```python
def send_email_single_country(request):
    """Page to send email to a single country"""
    return render(request, 'dashboard/send_email_single.html')
```

### Template
```
sustainable_energy/dashboard/templates/dashboard/send_email_single.html
```

### API Endpoints Used
- `/api/objective4/countries/` - Get list of countries
- `/api/objective4/predictions/` - Get predictions for country
- `/api/send-email-alerts-selected/` - Send email

## Email Logging

All emails sent from this page are automatically logged to the database:
- Country name
- Recipient email
- Status (success/failed)
- Timestamp
- Alert type
- Access percentage

View logs at: http://127.0.0.1:8000/email-logs/

## Troubleshooting

### Problem: Dropdown is empty
**Solution:**
- Make sure Django server is running
- Check browser console for errors
- Refresh the page

### Problem: "Send Email Alert" button is disabled
**Solution:**
- Select a country from the dropdown first
- The button enables automatically after selection

### Problem: Email sending fails
**Solution:**
- Check email configuration in `email_config.py`
- Verify SMTP settings
- Check server logs for errors

### Problem: No country information showing
**Solution:**
- Wait a moment after selecting country
- Check if predictions API is working
- Refresh the page and try again

## Quick Start

```bash
# 1. Make sure server is running
cd sustainable_energy
python manage.py runserver

# 2. Open browser
http://127.0.0.1:8000/send-email-country/

# 3. Select country and send!
```

## Tips

1. **Preview Before Sending**: Always check the country information before clicking send
2. **One at a Time**: This page is designed for single emails - use Objective 8 for bulk
3. **Check Logs**: View sent emails at `/email-logs/`
4. **Alert Types**: Pay attention to the color-coded alert types
5. **Error Messages**: Read error messages carefully for troubleshooting

## Benefits

✅ **Simple Interface**: Easy to use, no complex selections  
✅ **Quick Sending**: Send email in 3 clicks  
✅ **Preview Details**: See prediction before sending  
✅ **Instant Feedback**: Know immediately if email was sent  
✅ **No Login Required**: Open access for all users  
✅ **Automatic Logging**: All emails are logged automatically  

## Related Pages

- **Home Page**: http://127.0.0.1:8000/
- **Objective 8 (Multiple)**: http://127.0.0.1:8000/objective8/
- **Email Logs**: http://127.0.0.1:8000/email-logs/

---

**Status**: ✅ Ready to Use  
**URL**: http://127.0.0.1:8000/send-email-country/  
**Created**: December 2024
