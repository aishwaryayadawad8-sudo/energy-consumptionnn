# Admin Login System - Setup Guide

## Overview

I've created an admin login system so only authorized administrators can access the email alert feature.

## Features

✅ **Secure Login** - Username and password authentication  
✅ **Admin Only** - Only staff users can access email alerts  
✅ **Session Management** - Stay logged in across pages  
✅ **Logout Function** - Secure logout when done  
✅ **Protected Routes** - Email alert page requires login  

---

## Setup Steps

### Step 1: Create Admin User

Run this command:

```bash
python create_email_admin.py
```

You'll be asked for:
- **Username** (default: admin)
- **Email** (default: admin@sdg7.org)
- **Password** (minimum 8 characters)
- **Confirm Password**

Example:
```
Enter admin username (default: admin): sdg7admin
Enter admin email (default: admin@sdg7.org): admin@sdg7.org
Enter admin password: ********
Confirm password: ********

✅ Admin user 'sdg7admin' created successfully!
```

### Step 2: Restart Django Server

```bash
# Stop server (Ctrl+C)
# Start again:
python manage.py runserver
```

### Step 3: Access Admin Login

Go to: **http://127.0.0.1:8000/admin-login/**

---

## How to Use

### 1. Login

1. Go to: http://127.0.0.1:8000/admin-login/
2. Enter your username and password
3. Click "Login"
4. You'll be redirected to the Email Alert System

### 2. Send Email Alerts

Once logged in:
- Select countries from dropdown
- Click "Send Alerts to Selected Countries"
- View results

### 3. Logout

Click the "Logout" button in the top-right corner

---

## Access Flow

```
┌─────────────────────────────────────┐
│  User tries to access Objective 8   │
│  http://127.0.0.1:8000/objective8/  │
└────────────────┬────────────────────┘
                 │
                 ▼
         ┌───────────────┐
         │ Logged in?    │
         └───┬───────┬───┘
             │       │
         NO  │       │  YES
             │       │
             ▼       ▼
    ┌────────────┐  ┌──────────────────┐
    │ Redirect   │  │ Show Email Alert │
    │ to Login   │  │ System           │
    └────────────┘  └──────────────────┘
```

---

## URLs

| Page | URL | Access |
|------|-----|--------|
| Admin Login | `/admin-login/` | Public |
| Email Alerts | `/objective8/` | Admin Only |
| Logout | `/admin-logout/` | Logged in users |

---

## Default Credentials

If you use the defaults:

```
Username: admin
Password: [what you set]
Email: admin@sdg7.org
```

---

## Security Features

### 1. Authentication Required
- Email alert page requires login
- Redirects to login if not authenticated

### 2. Staff Permission Check
- Only users with `is_staff=True` can access
- Regular users cannot access even if logged in

### 3. Session Management
- Secure Django sessions
- Automatic logout on browser close (optional)

### 4. CSRF Protection
- All forms protected with CSRF tokens
- Prevents cross-site request forgery

---

## Updating the Objective Selector

Update the Objective 8 card to show it requires admin login:

The card on the main page now shows:
```
📧 Email Alert System
🔒 Admin Login Required
```

---

## Troubleshooting

### "Invalid credentials"
- Check username and password
- Username is case-sensitive
- Make sure you created the admin user

### "Insufficient permissions"
- User must have `is_staff=True`
- Run `create_email_admin.py` to create proper admin

### Can't access after login
- Make sure server is restarted
- Clear browser cache (Ctrl+F5)
- Check that you're going to `/objective8/`

### Forgot password
- Run `create_email_admin.py` again
- Choose to update the password

---

## Creating Multiple Admins

You can create multiple admin accounts:

```bash
python create_email_admin.py
# Enter different username each time
```

Example admins:
- `admin` - Main administrator
- `sdg7admin` - SDG 7 team lead
- `emailadmin` - Email system manager

---

## Integration with Django Admin

The admin users can also access Django's built-in admin:

**http://127.0.0.1:8000/admin/**

This gives access to:
- User management
- Database records
- System configuration

---

## Files Created/Modified

### New Files:
1. `sustainable_energy/dashboard/templates/dashboard/admin_login.html` - Login page
2. `create_email_admin.py` - Script to create admin users

### Modified Files:
1. `sustainable_energy/dashboard/views.py` - Added login/logout functions
2. `sustainable_energy/dashboard/urls.py` - Added login/logout routes
3. `sustainable_energy/dashboard/templates/dashboard/objective8.html` - Added admin info bar

---

## Quick Start

```bash
# 1. Create admin user
python create_email_admin.py

# 2. Restart server
python manage.py runserver

# 3. Login
# Go to: http://127.0.0.1:8000/admin-login/

# 4. Send emails
# You'll be at: http://127.0.0.1:8000/objective8/
```

---

## Summary

✅ **Admin login system created**  
✅ **Email alerts protected**  
✅ **Easy admin user creation**  
✅ **Secure authentication**  
✅ **Session management**  

**Next Steps:**
1. Run `python create_email_admin.py`
2. Create your admin account
3. Restart Django server
4. Login and send emails!

---

**Your email alert system is now secure and admin-only!** 🔒✨
