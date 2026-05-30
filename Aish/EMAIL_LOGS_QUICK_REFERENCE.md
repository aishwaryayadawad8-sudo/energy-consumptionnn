# 📧 Email Logs - Quick Reference Card

## URLs
```
Login:       http://127.0.0.1:8000/admin-login/
Send Emails: http://127.0.0.1:8000/objective8/
View Logs:   http://127.0.0.1:8000/email-logs/
API:         http://127.0.0.1:8000/api/email-logs/
```

## Quick Start
```bash
# 1. Start server
cd sustainable_energy
python manage.py runserver

# 2. Open browser
http://127.0.0.1:8000/admin-login/

# 3. Login → Send Email → View Logs
```

## What Gets Logged
- ✅ Country name
- ✅ Recipient email
- ✅ Email subject
- ✅ Status (success/failed)
- ✅ Alert type
- ✅ Access percentage
- ✅ Timestamp
- ✅ Admin username
- ✅ Error message (if failed)

## Dashboard Features
- 📊 Statistics (Total, Success, Failed, Rate)
- 📋 Email history table
- 🔍 Filters (Status, Alert Type, Country)
- 🔄 Auto-refresh (30 seconds)
- 📱 Mobile responsive

## Status Colors
- 🟢 Success - Green
- 🔴 Failed - Red
- 🟡 Pending - Yellow

## Alert Types
- 🔴 Critical (< 50%)
- 🟡 Needs Improvement (50-75%)
- 🔵 Good (75-95%)
- 🟢 Excellent (> 95%)

## Common Tasks

### Send Email
1. Go to `/objective8/`
2. Select countries
3. Click "Send Alerts"

### View Logs
1. Click "View Email Logs" button
2. Or go to `/email-logs/`

### Filter Logs
- Status dropdown → Select status
- Alert Type dropdown → Select type
- Country search → Type country name

### Check Success Rate
- Look at statistics cards at top
- Green number = successful emails
- Red number = failed emails
- Blue percentage = success rate

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Can't access logs | Login as admin first |
| No logs showing | Send test email first |
| Permission denied | Check `is_staff = True` |
| Table not found | Run `python create_email_logs_table.py` |

## Files Location
```
sustainable_energy/
├── dashboard/
│   ├── models.py              # EmailLog model
│   ├── views.py               # email_logs_dashboard
│   ├── urls.py                # /email-logs/ route
│   └── templates/
│       └── dashboard/
│           └── email_logs.html
└── ml_models/
    └── email_alerts.py        # Logging logic
```

## API Response
```json
{
  "success": true,
  "logs": [
    {
      "country": "Albania",
      "recipient_email": "albania@gov.al",
      "status": "success",
      "alert_type": "critical",
      "electricity_access": 45.5,
      "year": 2024,
      "sent_at": "2024-12-02T10:30:00Z",
      "sent_by": "admin"
    }
  ],
  "total": 1
}
```

## Keyboard Shortcuts
- `Ctrl + R` - Refresh page
- `Ctrl + F` - Find in page
- `Tab` - Navigate filters

## Best Practices
- ✅ Check logs regularly
- ✅ Monitor success rate
- ✅ Filter failed emails to debug
- ✅ Use search for specific countries
- ✅ Keep success rate above 80%

## Documentation
- `SETUP_EMAIL_LOGS.md` - Setup guide
- `EMAIL_LOGS_ADMIN_GUIDE.md` - Full docs
- `EMAIL_LOGS_DEMO.md` - Visual demo
- `EMAIL_LOGS_READY.md` - Getting started

---
**Quick Help**: See `EMAIL_LOGS_ADMIN_GUIDE.md` for details
