# 📧 Email Logs System - Architecture Diagram

## System Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                         USER (Admin)                                │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      ADMIN LOGIN PAGE                               │
│                   /admin-login/                                     │
│                                                                     │
│   ┌─────────────────────────────────────────┐                     │
│   │  Username: [admin____________]          │                     │
│   │  Password: [••••••••••••••••]          │                     │
│   │  [Login Button]                         │                     │
│   └─────────────────────────────────────────┘                     │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   EMAIL ALERT SYSTEM (Objective 8)                  │
│                        /objective8/                                 │
│                                                                     │
│   ┌─────────────────────────────────────────┐                     │
│   │  Select Countries:                      │                     │
│   │  [Albania ▼] [Kenya ▼] [Nigeria ▼]    │                     │
│   │                                         │                     │
│   │  [Send Alerts to Selected Countries]   │                     │
│   │  [View Email Logs] ←──────────────────┐│                     │
│   └─────────────────────────────────────────┘│                     │
└────────────────────────────┬─────────────────┼─────────────────────┘
                             │                 │
                             ▼                 │
┌─────────────────────────────────────────────┐│
│         EMAIL SENDING PROCESS               ││
│                                             ││
│  1. Get predictions for countries          ││
│  2. Classify alert type                    ││
│  3. Generate email content                 ││
│  4. Send email via SMTP                    ││
│  5. Log to database ✨                     ││
└────────────────────────────┬────────────────┘│
                             │                 │
                             ▼                 │
┌─────────────────────────────────────────────┐│
│           DATABASE (EmailLog)               ││
│                                             ││
│  ┌───────────────────────────────────────┐ ││
│  │ id: 1                                 │ ││
│  │ country: "Albania"                    │ ││
│  │ recipient_email: "albania@gov.al"    │ ││
│  │ subject: "🚨 URGENT: Critical..."    │ ││
│  │ status: "success"                     │ ││
│  │ alert_type: "critical"                │ ││
│  │ electricity_access: 45.5              │ ││
│  │ year: 2024                            │ ││
│  │ sent_at: "2024-12-02 10:30:00"       │ ││
│  │ error_message: null                   │ ││
│  │ sent_by: "admin"                      │ ││
│  └───────────────────────────────────────┘ ││
└────────────────────────────┬────────────────┘│
                             │                 │
                             │                 │
                             │    ┌────────────┘
                             │    │
                             ▼    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    EMAIL LOGS DASHBOARD                             │
│                       /email-logs/                                  │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │ Statistics                                                   │  │
│  │ ┌─────────┬─────────┬─────────┬─────────┐                  │  │
│  │ │ Total   │ Success │ Failed  │ Rate    │                  │  │
│  │ │   25    │   22    │    3    │  88%    │                  │  │
│  │ └─────────┴─────────┴─────────┴─────────┘                  │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │ Filters                                                      │  │
│  │ Status: [All ▼]  Alert Type: [All ▼]  Country: [Search...] │  │
│  │ [🔄 Refresh]                                                │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │ Email History Table                                          │  │
│  │ ┌────────┬─────────┬──────────┬────────┬────────┬────────┐ │  │
│  │ │ Date   │ Country │ Email    │ Alert  │ Access │ Status │ │  │
│  │ ├────────┼─────────┼──────────┼────────┼────────┼────────┤ │  │
│  │ │ 10:30  │ Albania │ alb@...  │ 🔴 Crit│ 45.5%  │ ✅ OK  │ │  │
│  │ │ 10:31  │ Kenya   │ ken@...  │ 🟡 Need│ 68.2%  │ ✅ OK  │ │  │
│  │ │ 10:32  │ Chad    │ cha@...  │ 🔴 Crit│ 12.3%  │ ❌ Fail│ │  │
│  │ └────────┴─────────┴──────────┴────────┴────────┴────────┘ │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  Auto-refreshes every 30 seconds ⟳                                │
└─────────────────────────────────────────────────────────────────────┘
```

## Data Flow

```
┌──────────────┐
│ Admin User   │
└──────┬───────┘
       │
       │ 1. Login
       ▼
┌──────────────────┐
│ Authentication   │
└──────┬───────────┘
       │
       │ 2. Select Countries
       ▼
┌──────────────────────┐
│ Objective 8 Page     │
└──────┬───────────────┘
       │
       │ 3. Click "Send Alerts"
       ▼
┌──────────────────────────────┐
│ Email Alert System           │
│ (email_alerts.py)            │
│                              │
│ • Get predictions            │
│ • Classify alert type        │
│ • Generate email content     │
└──────┬───────────────────────┘
       │
       │ 4. Send Email
       ▼
┌──────────────────────────────┐
│ SMTP Server                  │
│ (Gmail/Other)                │
└──────┬───────────────────────┘
       │
       │ 5. Log Result
       ▼
┌──────────────────────────────┐
│ Database                     │
│ EmailLog Table               │
│                              │
│ • country                    │
│ • recipient_email            │
│ • subject                    │
│ • status (success/failed)    │
│ • alert_type                 │
│ • electricity_access         │
│ • year                       │
│ • sent_at                    │
│ • error_message              │
│ • sent_by                    │
└──────┬───────────────────────┘
       │
       │ 6. View Logs
       ▼
┌──────────────────────────────┐
│ Email Logs Dashboard         │
│ (/email-logs/)               │
│                              │
│ • Display all logs           │
│ • Show statistics            │
│ • Enable filtering           │
│ • Auto-refresh               │
└──────────────────────────────┘
```

## Component Interaction

```
┌─────────────────────────────────────────────────────────────────┐
│                         FRONTEND                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────┐    ┌──────────────────┐                 │
│  │  objective8.html │    │ email_logs.html  │                 │
│  │                  │    │                  │                 │
│  │ • Country select │    │ • Statistics     │                 │
│  │ • Send button    │    │ • Filter controls│                 │
│  │ • View logs link │    │ • Email table    │                 │
│  └────────┬─────────┘    └────────┬─────────┘                 │
│           │                       │                            │
└───────────┼───────────────────────┼────────────────────────────┘
            │                       │
            │ POST                  │ GET
            │                       │
┌───────────┼───────────────────────┼────────────────────────────┐
│           ▼                       ▼         BACKEND            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │                      views.py                            │ │
│  │                                                          │ │
│  │  send_email_alerts_selected()  get_email_logs()        │ │
│  │           │                            │                 │ │
│  │           ▼                            ▼                 │ │
│  │  ┌─────────────────┐         ┌─────────────────┐       │ │
│  │  │ email_alerts.py │         │   models.py     │       │ │
│  │  │                 │         │                 │       │ │
│  │  │ • send_email()  │         │ EmailLog model  │       │ │
│  │  │ • analyze_and_  │         │                 │       │ │
│  │  │   send_alerts() │         │ • country       │       │ │
│  │  │                 │         │ • status        │       │ │
│  │  │ Logs to DB ────────────▶  │ • alert_type    │       │ │
│  │  └─────────────────┘         │ • sent_at       │       │ │
│  │                              │ • sent_by       │       │ │
│  │                              └─────────────────┘       │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         DATABASE                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │              dashboard_emaillog Table                    │ │
│  │                                                          │ │
│  │  id | country | recipient_email | subject | status |    │ │
│  │  alert_type | electricity_access | year | sent_at |     │ │
│  │  error_message | sent_by                                │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## File Structure

```
Project Root
│
├── sustainable_energy/
│   ├── dashboard/
│   │   ├── models.py ✨ NEW
│   │   │   └── EmailLog model
│   │   │
│   │   ├── views.py ✨ UPDATED
│   │   │   ├── send_email_alerts_selected()
│   │   │   ├── email_logs_dashboard() ✨ NEW
│   │   │   └── get_email_logs() ✨ NEW
│   │   │
│   │   ├── urls.py ✨ UPDATED
│   │   │   ├── /email-logs/ ✨ NEW
│   │   │   └── /api/email-logs/ ✨ NEW
│   │   │
│   │   ├── templates/
│   │   │   └── dashboard/
│   │   │       ├── objective8.html ✨ UPDATED
│   │   │       └── email_logs.html ✨ NEW
│   │   │
│   │   └── migrations/
│   │       └── 0001_initial.py ✨ NEW
│   │
│   └── ml_models/
│       └── email_alerts.py ✨ UPDATED
│           ├── send_email() - Added logging
│           └── analyze_and_send_alerts() - Added logging
│
├── create_email_logs_table.py ✨ NEW
│
└── Documentation/
    ├── EMAIL_LOGS_READY.md ✨ NEW
    ├── SETUP_EMAIL_LOGS.md ✨ NEW
    ├── EMAIL_LOGS_ADMIN_GUIDE.md ✨ NEW
    ├── EMAIL_LOGS_DEMO.md ✨ NEW
    ├── EMAIL_LOGS_QUICK_REFERENCE.md ✨ NEW
    ├── START_EMAIL_LOGS_SYSTEM.md ✨ NEW
    └── EMAIL_LOGS_SYSTEM_DIAGRAM.md ✨ NEW (This file)
```

## URL Routing

```
┌─────────────────────────────────────────────────────────────────┐
│                         URL Routes                              │
└─────────────────────────────────────────────────────────────────┘

/admin-login/
    │
    ├─ GET  → admin_login() → admin_login.html
    └─ POST → authenticate() → redirect to /objective8/

/objective8/
    │
    └─ GET → objective8_dashboard_protected() → objective8.html
              (requires login)

/api/send-email-alerts-selected/
    │
    └─ POST → send_email_alerts_selected()
              ├─ Get predictions
              ├─ Send emails
              ├─ Log to database ✨
              └─ Return JSON response

/email-logs/ ✨ NEW
    │
    └─ GET → email_logs_dashboard() → email_logs.html
              (requires login)

/api/email-logs/ ✨ NEW
    │
    └─ GET → get_email_logs()
              ├─ Query EmailLog table
              └─ Return JSON response
```

## Database Schema

```
┌─────────────────────────────────────────────────────────────────┐
│                    EmailLog Table                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Field Name           Type            Description              │
│  ─────────────────────────────────────────────────────────────  │
│  id                   Integer         Primary key              │
│  country              CharField(100)  Country name             │
│  recipient_email      EmailField      Recipient email          │
│  subject              CharField(500)  Email subject            │
│  status               CharField(20)   success/failed/pending   │
│  alert_type           CharField(50)   critical/needs_improve/  │
│                                       excellent/good           │
│  electricity_access   FloatField      Access percentage        │
│  year                 IntegerField    Prediction year          │
│  sent_at              DateTimeField   Timestamp                │
│  error_message        TextField       Error (if failed)        │
│  sent_by              CharField(100)  Admin username           │
│                                                                 │
│  Indexes:                                                       │
│  • sent_at (DESC) - For sorting                                │
│  • status - For filtering                                      │
│  • country - For searching                                     │
└─────────────────────────────────────────────────────────────────┘
```

## Security Flow

```
┌──────────────┐
│ User Request │
└──────┬───────┘
       │
       ▼
┌──────────────────┐
│ Is Authenticated?│
└──────┬───────────┘
       │
       ├─ NO ──▶ Redirect to /admin-login/
       │
       ▼
┌──────────────────┐
│ Is Staff User?   │
└──────┬───────────┘
       │
       ├─ NO ──▶ Redirect to /admin-login/
       │
       ▼
┌──────────────────┐
│ Allow Access     │
└──────────────────┘
```

## Email Sending Flow

```
1. Admin selects countries
        ↓
2. System gets predictions for each country
        ↓
3. For each country:
   ├─ Calculate electricity access
   ├─ Classify alert type (critical/needs_improvement/excellent/good)
   ├─ Generate email content
   ├─ Create EmailLog entry (status: pending)
   ├─ Send email via SMTP
   ├─ Update EmailLog entry:
   │  ├─ If success: status = "success"
   │  └─ If failed: status = "failed", error_message = error
   └─ Continue to next country
        ↓
4. Return summary to admin
        ↓
5. Admin views logs at /email-logs/
```

## Auto-Refresh Mechanism

```
┌─────────────────────────────────────────────────────────────────┐
│                    Email Logs Page                              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ On page load
                              ▼
                    ┌──────────────────┐
                    │  loadLogs()      │
                    │  • Fetch logs    │
                    │  • Update table  │
                    │  • Update stats  │
                    └────────┬─────────┘
                             │
                             │ Every 30 seconds
                             ▼
                    ┌──────────────────┐
                    │  setInterval()   │
                    │  • Call loadLogs │
                    │  • Refresh data  │
                    └──────────────────┘
```

---

**This diagram shows the complete architecture of your email logs tracking system!**
