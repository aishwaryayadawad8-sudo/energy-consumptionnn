# Objective 8: Email Alert System - User Guide

## ✅ What I Created

I've added a new **Objective 8: Email Alert System** to your Django dashboard that allows you to:
- **Select specific countries** to send alerts to
- **Send to all countries** at once
- **View results** with country status breakdown

## 🚀 How to Access

### Step 1: Start Your Django Server

```bash
python manage.py runserver
```

### Step 2: Open Your Browser

Go to: **http://127.0.0.1:8000/**

### Step 3: Click on "Email Alert System"

You'll see a new card on the main page:
- **📧 Email Alert System**
- Click "Send Alerts" button

## 📧 How to Use

### Option 1: Send to Specific Countries

1. **Select Countries**:
   - Click the dropdown menu
   - Type to search for countries
   - Select multiple countries (e.g., India, Nigeria, Kenya)
   - See the count update

2. **Send Alerts**:
   - Click "Send Alerts to Selected Countries"
   - Confirm the action
   - Wait for analysis (loading spinner)
   - View results

### Option 2: Send to All Countries

1. Click "Send to All Countries" button
2. Confirm the action
3. System analyzes all countries
4. Sends alerts to those needing attention

## 📊 What Happens

The system:
1. **Analyzes** electricity access for each country
2. **Classifies** status:
   - 🚨 **Critical** (< 50% access) - Urgent action needed
   - ⚠️ **Needs Improvement** (50-75%) - Below target
   - 👍 **Good** (75-95%) - On track
   - 🎉 **Excellent** (> 95%) - Target achieved

3. **Sends** customized emails to country addresses
4. **Shows** results grouped by status

## 📧 Email Addresses

All emails are sent to addresses from `country_emails.csv`:
- India → india@sdg7_alerts.org
- Nigeria → nigeria@sdg7_alerts.org
- etc.

## ⚙️ Current Settings

- **Mode**: SIMULATION (emails not actually sent)
- **Testing**: All emails go to your test address
- **Safe**: Perfect for testing without sending real emails

## 🔓 To Enable Real Email Sending

1. **Get Gmail App Password**:
   - Visit: https://myaccount.google.com/apppasswords
   - Generate App Password for "Mail"

2. **Update Configuration**:
   - Open `sustainable_energy/email_config.py`
   - Line 8: Add your App Password
   - Line 28: Set `ENABLE_ACTUAL_EMAIL_SENDING = True`

3. **Restart Server**:
   ```bash
   python manage.py runserver
   ```

## 🎯 Example Usage

### Example 1: Send to 3 Countries

1. Go to http://127.0.0.1:8000/objective8/
2. Select: India, Nigeria, Kenya
3. Click "Send Alerts to Selected Countries"
4. View results:
   - India: 99.0% - Excellent
   - Nigeria: 55.4% - Needs Improvement
   - Kenya: 71.4% - Needs Improvement

### Example 2: Send to All Countries

1. Go to http://127.0.0.1:8000/objective8/
2. Click "Send to All Countries"
3. Confirm
4. View results for all countries

## 📁 Files Created/Modified

### New Files:
- `sustainable_energy/dashboard/templates/dashboard/objective8.html` - Email alert page

### Modified Files:
- `sustainable_energy/dashboard/views.py` - Added objective8_dashboard and send_email_alerts_selected functions
- `sustainable_energy/dashboard/urls.py` - Added objective8 routes
- `sustainable_energy/dashboard/templates/dashboard/objective_selector.html` - Added Objective 8 card

## 🎨 Features

✅ **Multi-select dropdown** with search
✅ **Real-time country count** display
✅ **Loading spinner** during analysis
✅ **Results grouped by status**
✅ **Beautiful UI** matching your dashboard style
✅ **Responsive design** works on all devices

## 🔧 Troubleshooting

**"Countries not loading"**
- Make sure Django server is running
- Check console for errors

**"Error sending alerts"**
- Check that `country_emails.csv` exists
- Verify `global-data-on-sustainable-energy.csv` is present

**"No results shown"**
- Check browser console for JavaScript errors
- Verify API endpoint is working: http://127.0.0.1:8000/api/send-email-alerts-selected/

## 📸 What You'll See

1. **Main Page**: New "Email Alert System" card
2. **Email Alert Page**:
   - Header with instructions
   - Country selection dropdown
   - Two buttons: "Send to Selected" and "Send to All"
   - Loading spinner
   - Results section with status breakdown

## 🎓 Quick Start

```bash
# 1. Start server
python manage.py runserver

# 2. Open browser
# Go to: http://127.0.0.1:8000/

# 3. Click "Email Alert System"

# 4. Select countries and send!
```

That's it! You now have a fully functional email alert system with country selection! 🌍📧✨
