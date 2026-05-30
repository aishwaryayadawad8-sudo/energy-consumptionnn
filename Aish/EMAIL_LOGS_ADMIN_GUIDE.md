# 📧 Email Logs Admin Dashboard - Complete Guide

## Overview
A separate admin page to track all email alerts sent to countries, showing success/failure status, timestamps, and detailed information.

## Features

### 1. **Email Logs Dashboard** (`/email-logs/`)
- View all sent emails in a table format
- Real-time status tracking (Success/Failed/Pending)
- Filter by status, alert type, and country
- Statistics dashboard showing:
  - Total emails sent
  - Successful emails
  - Failed emails
  - Success rate percentage
- Auto-refresh every 30 seconds

### 2. **Database Logging**
All emails are automatically logged to the database with:
- Country name
- Recipient email address
- Email subject
- Status (success/failed/pending)
- Alert type (critical/needs_improvement/excellent/good)
- Electricity access percentage
- Year
- Timestamp
- Error message (if failed)
- Sent by (admin username)

### 3. **Admin Access**
- Only accessible to logged-in admin users
- Requires staff permissions
- Integrated with existing admin login system

## Setup Instructions

### Step 1: Create Database Table
```bash
python create_email_logs_table.py
```

This will:
- Create migrations for the EmailLog model
- Apply migrations to create the database table

### Step 2: Start Django Server
```bash
cd sustainable_energy
python manage.py runserver
```

### Step 3: Login as Admin
1. Go to: http://127.0.0.1:8000/admin-login/
2. Login with your admin credentials
3. You'll be redirected to the Email Alert System

## How to Use

### Accessing Email Logs

**Option 1: From Email Alert System**
1. Login at `/admin-login/`
2. Go to Objective 8 (Email Alert System)
3. Click "View Email Logs" button in the top bar

**Option 2: Direct URL**
- Navigate to: http://127.0.0.1:8000/email-logs/

### Viewing Email History

The dashboard shows:
- **Date & Time**: When the email was sent
- **Country**: Recipient country
- **Email**: Recipient email address
- **Alert Type**: Critical/Needs Improvement/Excellent/Good
- **Access %**: Electricity access percentage
- **Year**: Prediction year
- **Status**: Success/Failed/Pending
- **Sent By**: Admin username who sent the email
- **Subject**: Email subject line
- **Error Message**: If failed, shows the error

### Filtering Logs

**By Status:**
- All
- Success
- Failed
- Pending

**By Alert Type:**
- All
- Critical
- Needs Improvement
- Excellent
- Good

**By Country:**
- Type country name in search box
- Real-time filtering

### Statistics Dashboard

Top of the page shows:
- **Total Emails**: All emails sent
- **Successful**: Successfully delivered emails
- **Failed**: Failed email attempts
- **Success Rate**: Percentage of successful emails

## Color Coding

### Status Badges
- 🟢 **Success**: Green badge
- 🔴 **Failed**: Red badge
- 🟡 **Pending**: Yellow badge

### Alert Type Badges
- 🔴 **Critical**: Red (< 50% access)
- 🟡 **Needs Improvement**: Yellow (50-75% access)
- 🔵 **Good**: Blue (75-95% access)
- 🟢 **Excellent**: Green (> 95% access)

## API Endpoints

### Get Email Logs
```
GET /api/email-logs/
```

**Response:**
```json
{
  "success": true,
  "logs": [
    {
      "id": 1,
      "country": "Albania",
      "recipient_email": "albania.energy@gov.al",
      "subject": "🚨 URGENT: Critical Electricity Access Alert",
      "status": "success",
      "alert_type": "critical",
      "electricity_access": 45.5,
      "year": 2024,
      "sent_at": "2024-12-02T10:30:00Z",
      "error_message": null,
      "sent_by": "admin"
    }
  ],
  "total": 1
}
```

## Database Schema

### EmailLog Model
```python
class EmailLog(models.Model):
    country = CharField(max_length=100)
    recipient_email = EmailField()
    subject = CharField(max_length=500)
    status = CharField(choices=['success', 'failed', 'pending'])
    alert_type = CharField(choices=['critical', 'needs_improvement', 'good', 'excellent'])
    electricity_access = FloatField()
    year = IntegerField()
    sent_at = DateTimeField(auto_now_add=True)
    error_message = TextField(blank=True, null=True)
    sent_by = CharField(max_length=100, blank=True, null=True)
```

## Automatic Logging

Emails are automatically logged when sent from:
1. **Objective 8 Dashboard** (`/objective8/`)
   - When you select countries and click "Send Alerts"
   - User info is captured automatically

2. **API Endpoint** (`/api/send-email-alerts-selected/`)
   - All API calls log emails automatically

## Troubleshooting

### No Logs Showing
1. Check if database table exists:
   ```bash
   python manage.py dbshell
   .tables  # Should show dashboard_emaillog
   ```

2. Send a test email from Objective 8
3. Refresh the logs page

### Permission Denied
- Make sure you're logged in as admin
- Check if user has `is_staff` permission

### Database Errors
```bash
# Reset migrations if needed
python manage.py migrate dashboard zero
python manage.py makemigrations dashboard
python manage.py migrate dashboard
```

## Features in Detail

### Auto-Refresh
- Page automatically refreshes every 30 seconds
- Manual refresh button available
- No need to reload page

### Responsive Design
- Works on desktop, tablet, and mobile
- Table scrolls horizontally on small screens
- Touch-friendly interface

### Real-Time Statistics
- Updates when filters are applied
- Shows filtered statistics
- Percentage calculations

## Integration with Email System

The email logs are integrated with:
1. **Email Alert System** (`email_alerts.py`)
   - Modified `send_email()` method to log attempts
   - Modified `analyze_and_send_alerts()` to pass user info

2. **Views** (`views.py`)
   - `send_email_alerts_selected()` passes user object
   - `get_email_logs()` retrieves logs from database

3. **URLs** (`urls.py`)
   - `/email-logs/` - Dashboard page
   - `/api/email-logs/` - API endpoint

## Security

- Admin-only access (requires login)
- Staff permission required
- CSRF protection enabled
- SQL injection prevention (Django ORM)

## Future Enhancements

Possible additions:
- Export logs to CSV/Excel
- Email retry functionality
- Bulk delete old logs
- Email templates preview
- Delivery confirmation tracking
- Email open tracking
- Click tracking in emails

## Quick Reference

| Action | URL |
|--------|-----|
| Admin Login | `/admin-login/` |
| Email Logs Dashboard | `/email-logs/` |
| Send Email Alerts | `/objective8/` |
| API - Get Logs | `/api/email-logs/` |
| API - Send Alerts | `/api/send-email-alerts-selected/` |

## Support

If you encounter issues:
1. Check Django server logs
2. Check browser console for JavaScript errors
3. Verify database migrations are applied
4. Ensure admin user has staff permissions

---

**Created**: December 2024  
**Version**: 1.0  
**Status**: ✅ Ready to Use
