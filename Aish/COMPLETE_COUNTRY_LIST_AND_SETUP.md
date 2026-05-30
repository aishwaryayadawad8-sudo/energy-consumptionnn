# 📋 Complete Country List & Email Setup Guide

## 🌍 ALL 176 COUNTRIES AVAILABLE

### Africa (45 countries)
- Algeria, Angola, Benin, Botswana, Burkina Faso, Burundi
- Cameroon, Central African Republic, Chad, Comoros, Congo
- Djibouti, Egypt, Equatorial Guinea, Eritrea, Eswatini, Ethiopia
- Gabon, Gambia, Ghana, Guinea, Guinea-Bissau, Kenya, Lesotho
- Liberia, Libya, Madagascar, Malawi, Mali, Mauritania, Mauritius
- Morocco, Mozambique, Namibia, Niger, Nigeria, Rwanda, Senegal
- Sierra Leone, Somalia, South Africa, South Sudan, Sudan
- Tanzania, Togo, Tunisia, Uganda, Zambia, Zimbabwe

### Asia (38 countries)
- Afghanistan, Armenia, Azerbaijan, Bahrain, Bangladesh, Bhutan
- Cambodia, China, Georgia, India, Indonesia, Iraq, Israel
- Japan, Jordan, Kazakhstan, Kuwait, Kyrgyzstan, Lebanon
- Malaysia, Maldives, Mongolia, Myanmar, Nepal, Oman, Pakistan
- Philippines, Qatar, Saudi Arabia, Singapore, Sri Lanka
- Syria, Tajikistan, Thailand, Turkey, Turkmenistan
- United Arab Emirates, Uzbekistan, Yemen

### Europe (42 countries)
- Albania, Austria, Belarus, Belgium, Bosnia and Herzegovina
- Bulgaria, Croatia, Cyprus, Czechia, Denmark, Estonia, Finland
- France, Germany, Greece, Hungary, Iceland, Ireland, Italy
- Latvia, Lithuania, Luxembourg, Malta, Montenegro
- Netherlands, North Macedonia, Norway, Poland, Portugal
- Romania, Serbia, Slovakia, Slovenia, Spain, Sweden
- Switzerland, Ukraine, United Kingdom

### Americas (35 countries)
- Antigua and Barbuda, Argentina, Aruba, Bahamas, Barbados
- Belize, Bermuda, Brazil, Canada, Cayman Islands, Chile
- Colombia, Costa Rica, Cuba, Dominica, Dominican Republic
- Ecuador, El Salvador, French Guiana, Grenada, Guatemala
- Guyana, Haiti, Honduras, Jamaica, Mexico, Nicaragua, Panama
- Paraguay, Peru, Puerto Rico, Saint Kitts and Nevis
- Saint Lucia, Saint Vincent and the Grenadines, Suriname
- Trinidad and Tobago, United States, Uruguay

### Oceania (16 countries)
- Australia, Fiji, Kiribati, Nauru, New Caledonia, New Zealand
- Papua New Guinea, Samoa, Solomon Islands, Tonga, Tuvalu, Vanuatu

---

## 🎯 How to Configure Your Email

### Method 1: Interactive Setup (Easiest)

```bash
python configure_country_emails.py
```

**Options:**
1. Set ALL countries to your email
2. Set SPECIFIC countries to your email
3. View current configuration

**Example:**
```
Enter your choice: 2
Countries: Albania, Kenya, India, Brazil
Your email: your.email@gmail.com

✅ Albania → your.email@gmail.com
✅ Kenya → your.email@gmail.com
✅ India → your.email@gmail.com
✅ Brazil → your.email@gmail.com
```

### Method 2: Update All Countries

```bash
python update_all_emails.py
```

This sets ALL 176 countries to your email address.

### Method 3: Manual Edit

Edit `country_emails.csv`:
```csv
Country,Email
Albania,your.email@gmail.com
Kenya,your.email@gmail.com
India,your.email@gmail.com
```

---

## 📧 Send Alerts

### Send to Specific Country:
```bash
python send_xgboost_alert_to_country.py Albania
```

### Send to ALL Countries (Automatic):
```bash
python auto_send_xgboost_alerts.py
```

---

## 📊 View Sent Alerts in Admin Page

### Step 1: Start Django Server
```bash
cd sustainable_energy
python manage.py runserver
```

### Step 2: Login to Admin
Visit: **http://localhost:8000/admin-login/**

**Default Credentials:**
- Username: `admin`
- Password: (the one you created)

### Step 3: View Email Logs
Visit: **http://localhost:8000/email-logs/**

**You'll see:**
- Date & Time
- Country
- Email Address
- Subject
- Status (success/failed)
- Alert Type
- Access %
- Year
- Sent By

---

## 📊 Admin Page Features

### Email Logs Dashboard Shows:

1. **All Sent Emails**
   - Date and time sent
   - Country name
   - Recipient email
   - Email subject
   - Success/Failed status

2. **Filter Options**
   - By country
   - By status
   - By alert type
   - By date

3. **Statistics**
   - Total emails sent
   - Success rate
   - Failed emails
   - Emails by country

4. **Export Options**
   - Download as CSV
   - Print report
   - Email summary

---

## 🎯 Example Workflow

### 1. Configure Countries
```bash
python configure_country_emails.py
```
Choose option 2, enter:
- Countries: `Albania, Kenya, India`
- Email: `your.email@gmail.com`

### 2. Send Alerts
```bash
python send_xgboost_alert_to_country.py Albania
python send_xgboost_alert_to_country.py Kenya
python send_xgboost_alert_to_country.py India
```

### 3. View in Admin
1. Visit: http://localhost:8000/admin-login/
2. Login with your credentials
3. Go to: http://localhost:8000/email-logs/
4. See all sent emails with details

---

## 📧 Email Logging Details

Every email sent is automatically logged with:

```
✅ Country: Albania
✅ Email: your.email@gmail.com
✅ Subject: Status Update: Electricity Access Progress in Albania
✅ Status: success
✅ Alert Type: status_update
✅ Access: 84.31%
✅ Year: 2024
✅ Sent By: XGBoost System
✅ Timestamp: 2025-12-03 01:34:23
```

---

## 🎯 Current Configuration

**Your Email:** tejaswini.y2004teju@gmail.com  
**Password:** unbkroqmxrlzhpxb  
**Countries:** ALL 176 countries  
**Admin Page:** http://localhost:8000/email-logs/  
**Status:** ✅ WORKING  

---

## 📝 Quick Commands

```bash
# Configure countries
python configure_country_emails.py

# Send to specific country
python send_xgboost_alert_to_country.py [Country]

# Send to all countries
python auto_send_xgboost_alerts.py

# Start Django server
cd sustainable_energy
python manage.py runserver

# View admin page
# Visit: http://localhost:8000/admin-login/

# View email logs
# Visit: http://localhost:8000/email-logs/
```

---

## ✅ Summary

1. **176 countries available** for email alerts
2. **Configure** which countries get your email
3. **Send alerts** automatically with XGBoost (99.16% accuracy)
4. **View all logs** in admin page at http://localhost:8000/email-logs/
5. **All data stored** in database automatically

**Everything is logged and visible in your admin page!** 📊✅
