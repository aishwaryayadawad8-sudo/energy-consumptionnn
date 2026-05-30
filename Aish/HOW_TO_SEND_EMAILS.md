# How to Send Email Alerts to Countries

## ✅ System is Ready!

Your email alert system is set up and working. Here's how to use it:

## 🎬 Quick Demo

See how it works with example countries:

```bash
python auto_demo.py
```

This shows analysis for India, Nigeria, Kenya, Chad, and Brazil.

## 📧 Send Alerts to Countries

### Step 1: Run the Script

```bash
python send_email_simple.py
```

### Step 2: Enter Countries

When prompted, enter country names separated by commas:

```
Enter countries (comma-separated): India, Nigeria, Kenya
```

### Step 3: Review & Confirm

The system will show:
- Electricity access percentage for each country
- Status classification (Critical/Needs Improvement/Good/Excellent)
- Email address that will receive the alert

Then type `yes` to send (or `no` to cancel).

## 📊 Example Output

```
🌍 SDG 7 Country Alert System
============================================================

✅ Loaded 176 country email addresses

============================================================
Analyzing Countries
============================================================

🎉 India
   Access: 99.0%
   Status: EXCELLENT
   Email: india@sdg7_alerts.org

⚠️ Nigeria
   Access: 55.4%
   Status: NEEDS IMPROVEMENT
   Email: nigeria@sdg7_alerts.org

🚨 Chad
   Access: 11.1%
   Status: CRITICAL
   Email: chad@sdg7_alerts.org

============================================================
📋 Summary: 3 countries ready for alerts
============================================================

📤 Send email alerts? (yes/no): yes

✅ Email SIMULATED to india@sdg7_alerts.org
✅ Email SIMULATED to nigeria@sdg7_alerts.org
✅ Email SIMULATED to chad@sdg7_alerts.org

✅ Successfully processed 3/3 emails!
```

## 🌍 Available Countries (176 Total)

To see all available countries:

```bash
python list_countries.py
```

Some examples:
- **Africa**: Nigeria, Kenya, Ethiopia, Ghana, South Africa, Egypt
- **Asia**: India, China, Bangladesh, Pakistan, Indonesia, Thailand
- **Europe**: Germany, France, United Kingdom, Italy, Spain
- **Americas**: United States, Brazil, Canada, Mexico, Argentina
- **Oceania**: Australia, New Zealand, Fiji

## 🎯 Status Classifications

| Access % | Status | Icon | Email Type |
|----------|--------|------|------------|
| < 50% | CRITICAL | 🚨 | Urgent action plan |
| 50-75% | NEEDS IMPROVEMENT | ⚠️ | Recommendations |
| 75-95% | GOOD | 👍 | Encouragement |
| > 95% | EXCELLENT | 🎉 | Congratulations |

## ⚙️ Current Settings

**Email Mode**: SIMULATION (emails not actually sent)
**Testing Mode**: ON (all emails go to your address)
**Your Email**: electricity.prediction2000@gmail.com

## 🔓 Enable Real Email Sending

To actually send emails:

### Step 1: Get Gmail App Password

1. Visit: https://myaccount.google.com/apppasswords
2. Sign in with `electricity.prediction2000@gmail.com`
3. Generate App Password for "Mail"
4. Copy the 16-character code

### Step 2: Update Configuration

Edit `send_email_simple.py` (lines 11-12):

```python
SENDER_PASSWORD = 'your-16-char-password'  # Paste your App Password
ENABLE_SENDING = True  # Change False to True
```

### Step 3: Test

```bash
python send_email_simple.py
```

Enter a test country and confirm. You'll receive the email!

## 📝 Example Use Cases

### Send to African Countries
```
Enter countries: Nigeria, Kenya, Ethiopia, Ghana, South Africa
```

### Send to Asian Countries
```
Enter countries: India, China, Bangladesh, Pakistan, Indonesia
```

### Send to Countries Needing Help
```
Enter countries: Chad, South Sudan, Burundi, Niger, Malawi
```

### Send to High-Performing Countries
```
Enter countries: United States, Germany, Japan, France, United Kingdom
```

## 🔧 Troubleshooting

**"Country not found in dataset"**
- Check spelling (case-insensitive now works)
- Run `python list_countries.py` to see available countries

**"No email address found"**
- Country might not be in country_emails.csv
- Check the CSV file for the exact country name

**"Authentication Failed"** (when sending real emails)
- Make sure you're using App Password, not regular password
- Enable 2-Factor Authentication on Google account first

## 📚 All Available Scripts

| Script | Purpose |
|--------|---------|
| `auto_demo.py` | Automated demo with example countries |
| `send_email_simple.py` | Main script to send alerts |
| `list_countries.py` | View all 176 available countries |
| `test_email_setup.py` | Test your email configuration |

## 🎓 Quick Examples

### Example 1: Demo
```bash
python auto_demo.py
```

### Example 2: Send to 3 Countries
```bash
python send_email_simple.py
# Enter: India, Nigeria, Brazil
```

### Example 3: List All Countries
```bash
python list_countries.py
```

## ✅ Summary

You have a complete email alert system that:
1. ✅ Loads 176 country email addresses from CSV
2. ✅ Analyzes electricity access for any country
3. ✅ Classifies countries by status
4. ✅ Generates customized email content
5. ✅ Simulates or sends real emails
6. ✅ Works with case-insensitive country names

**Ready to send your first alert?**

```bash
python send_email_simple.py
```

Then enter countries like: `India, Nigeria, Kenya`

That's it! 🌍⚡📧
