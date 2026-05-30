# 📧 Email Logs Admin Dashboard - Visual Demo

## What You'll See

### 1. Login Page (`/admin-login/`)
```
┌─────────────────────────────────────────┐
│   🔐 Admin Login                        │
│                                         │
│   Username: [admin____________]         │
│   Password: [••••••••••••••••]         │
│                                         │
│   [Login Button]                        │
└─────────────────────────────────────────┘
```

### 2. Email Alert System (`/objective8/`)
```
┌─────────────────────────────────────────────────────────┐
│ 👤 Logged in as Admin: admin                            │
│ [View Email Logs] [Logout]                              │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ 📧 Email Alert System - SDG 7 Monitoring               │
│                                                         │
│ Select Countries:                                       │
│ [Albania ▼] [Kenya ▼] [Nigeria ▼]                     │
│                                                         │
│ [Send Alerts to Selected Countries]                    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 3. Email Logs Dashboard (`/email-logs/`)

#### Top Section - Header & Stats
```
┌─────────────────────────────────────────────────────────────────┐
│ 📧 Email Logs Dashboard                                         │
│ Track all email alerts sent to countries                        │
│                                                                 │
│ 👤 Logged in as: admin                                          │
│ [← Back to Email Alerts] [Logout]                              │
└─────────────────────────────────────────────────────────────────┘

┌──────────────┬──────────────┬──────────────┬──────────────┐
│ Total Emails │  Successful  │    Failed    │ Success Rate │
│      25      │      22      │      3       │    88.0%     │
│   (Purple)   │   (Green)    │    (Red)     │   (Blue)     │
└──────────────┴──────────────┴──────────────┴──────────────┘
```

#### Filter Controls
```
┌─────────────────────────────────────────────────────────────────┐
│ Status: [All ▼]  Alert Type: [All ▼]  Country: [Search...]     │
│ [🔄 Refresh]                                                    │
└─────────────────────────────────────────────────────────────────┘
```

#### Email History Table
```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Date & Time        │ Country  │ Email              │ Alert Type          │ Access % │ Year │ Status    │ Sent By │
├────────────────────┼──────────┼────────────────────┼─────────────────────┼──────────┼──────┼───────────┼─────────┤
│ 2024-12-02 10:30  │ Albania  │ albania@gov.al     │ 🔴 Critical         │ 45.5%    │ 2024 │ ✅ Success│ admin   │
│ 2024-12-02 10:31  │ Kenya    │ kenya@gov.ke       │ 🟡 Needs Improve    │ 68.2%    │ 2024 │ ✅ Success│ admin   │
│ 2024-12-02 10:32  │ Nigeria  │ nigeria@gov.ng     │ 🟢 Excellent        │ 98.5%    │ 2024 │ ✅ Success│ admin   │
│ 2024-12-02 10:33  │ Chad     │ chad@gov.td        │ 🔴 Critical         │ 12.3%    │ 2024 │ ❌ Failed │ admin   │
│ 2024-12-02 10:34  │ India    │ india@gov.in       │ 🔵 Good             │ 85.0%    │ 2024 │ ✅ Success│ admin   │
└────────────────────┴──────────┴────────────────────┴─────────────────────┴──────────┴──────┴───────────┴─────────┘
```

## Real Example Data

### Example 1: Successful Email
```json
{
  "country": "Albania",
  "recipient_email": "albania.energy@gov.al",
  "subject": "🚨 URGENT: Critical Electricity Access Alert for Albania",
  "status": "success",
  "alert_type": "critical",
  "electricity_access": 45.5,
  "year": 2024,
  "sent_at": "2024-12-02T10:30:00Z",
  "error_message": null,
  "sent_by": "admin"
}
```

**How it appears in table:**
```
┌────────────────────────────────────────────────────────────────────────────┐
│ 2024-12-02 10:30 │ Albania │ albania.energy@gov.al │ 🔴 Critical │ 45.5% │
│ 2024 │ ✅ Success │ admin │                                                │
│ Subject: 🚨 URGENT: Critical Electricity Access Alert for Albania          │
└────────────────────────────────────────────────────────────────────────────┘
```

### Example 2: Failed Email
```json
{
  "country": "Chad",
  "recipient_email": "chad.energy@gov.td",
  "subject": "🚨 URGENT: Critical Electricity Access Alert for Chad",
  "status": "failed",
  "alert_type": "critical",
  "electricity_access": 12.3,
  "year": 2024,
  "sent_at": "2024-12-02T10:33:00Z",
  "error_message": "SMTP connection timeout",
  "sent_by": "admin"
}
```

**How it appears in table:**
```
┌────────────────────────────────────────────────────────────────────────────┐
│ 2024-12-02 10:33 │ Chad │ chad.energy@gov.td │ 🔴 Critical │ 12.3% │      │
│ 2024 │ ❌ Failed │ admin │                                                 │
│ Subject: 🚨 URGENT: Critical Electricity Access Alert for Chad             │
│ Error: SMTP connection timeout                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

## Color Coding Guide

### Status Badges
- **✅ Success** - Green background, dark green text
- **❌ Failed** - Red background, dark red text
- **⏳ Pending** - Yellow background, dark yellow text

### Alert Type Badges
- **🔴 Critical** - Red badge (< 50% access)
- **🟡 Needs Improvement** - Orange badge (50-75% access)
- **🔵 Good** - Blue badge (75-95% access)
- **🟢 Excellent** - Green badge (> 95% access)

## Filter Examples

### Filter by Status: "Failed"
```
┌────────────────────────────────────────────────────────────────────────────┐
│ Status: [Failed ▼]  Alert Type: [All ▼]  Country: [_______]              │
└────────────────────────────────────────────────────────────────────────────┘

Statistics Update:
┌──────────────┬──────────────┬──────────────┬──────────────┐
│ Total Emails │  Successful  │    Failed    │ Success Rate │
│      3       │      0       │      3       │    0.0%      │
└──────────────┴──────────────┴──────────────┴──────────────┘

Shows only failed emails in table
```

### Filter by Alert Type: "Critical"
```
┌────────────────────────────────────────────────────────────────────────────┐
│ Status: [All ▼]  Alert Type: [Critical ▼]  Country: [_______]            │
└────────────────────────────────────────────────────────────────────────────┘

Shows only critical alerts (countries with < 50% access)
```

### Search by Country: "Kenya"
```
┌────────────────────────────────────────────────────────────────────────────┐
│ Status: [All ▼]  Alert Type: [All ▼]  Country: [Kenya____]               │
└────────────────────────────────────────────────────────────────────────────┘

Shows only emails sent to Kenya
```

## Mobile View

On mobile devices, the table becomes scrollable:

```
┌─────────────────────────┐
│ 📧 Email Logs Dashboard │
│                         │
│ ← Swipe to see more →  │
│                         │
│ ┌─────────────────────┐ │
│ │ Date    │ Country   │ │
│ │ 12/02   │ Albania   │ │
│ │ 10:30   │           │ │
│ └─────────────────────┘ │
│                         │
│ Total: 25  Success: 22  │
│ Failed: 3  Rate: 88%    │
└─────────────────────────┘
```

## Auto-Refresh Indicator

Every 30 seconds, you'll see:
```
┌─────────────────────────────────────┐
│ 🔄 Refreshing...                    │
└─────────────────────────────────────┘
```

Then updates to:
```
┌─────────────────────────────────────┐
│ ✅ Updated (Last: 10:35:42)         │
└─────────────────────────────────────┘
```

## Empty State

When no emails have been sent yet:
```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│                    📭 No email logs found                       │
│                                                                 │
│         Send your first email from the Email Alert System       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Error State

If there's a database error:
```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│              ❌ Error loading logs: Database error              │
│                                                                 │
│                    Please try again later                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## User Flow

### Complete User Journey:

1. **Login** → `/admin-login/`
   - Enter credentials
   - Click "Login"

2. **Send Emails** → `/objective8/`
   - Select countries
   - Click "Send Alerts"
   - See success message

3. **View Logs** → `/email-logs/`
   - Click "View Email Logs" button
   - See all sent emails
   - Filter/search as needed

4. **Monitor** → Stay on `/email-logs/`
   - Page auto-refreshes
   - See new emails appear
   - Check success rate

## Quick Actions

From Email Logs Dashboard:
- **Back to Email Alerts** → Returns to Objective 8
- **Logout** → Logs out and returns to login page
- **Refresh** → Manually refresh logs
- **Filter** → Apply filters to narrow results
- **Search** → Find specific country

## Statistics Interpretation

### Example Statistics:
```
Total: 100 | Success: 85 | Failed: 15 | Rate: 85%
```

**Interpretation:**
- 100 emails sent total
- 85 delivered successfully
- 15 failed to deliver
- 85% success rate (good performance)

### What's a Good Success Rate?
- **90-100%**: Excellent ✅
- **80-89%**: Good 👍
- **70-79%**: Fair ⚠️
- **Below 70%**: Needs attention ❌

## Tips for Using the Dashboard

1. **Check Regularly**: Monitor email delivery status
2. **Filter Failed**: Focus on failed emails to debug issues
3. **Track by Country**: See which countries receive most alerts
4. **Monitor Success Rate**: Ensure high delivery rate
5. **Use Search**: Quickly find specific emails

---

**This is what you'll see when you access `/email-logs/`!**
