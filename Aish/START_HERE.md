# 🚀 START HERE - Email Alert System

## How to Access and Use the Email Alert System

### Option 1: Quick Demo (Recommended First Step)

Open your terminal/command prompt and run:

```bash
python auto_demo.py
```

This will show you how the system works with 5 example countries (India, Nigeria, Kenya, Chad, Brazil).

**What you'll see:**
- Electricity access percentage for each country
- Status classification (Critical/Needs Improvement/Good/Excellent)
- Email addresses
- Summary of results

---

### Option 2: Send Alerts to Countries You Choose

Run this command:

```bash
python send_email_simple.py
```

**Then follow the prompts:**

1. **Enter countries** (comma-separated):
   ```
   Enter countries: India, Nigeria, Kenya
   ```

2. **Review the analysis** - The system will show:
   - Electricity access for each country
   - Status classification
   - Email addresses

3. **Confirm** - Type `yes` to send (or `no` to cancel)

---

### Option 3: See All Available Countries

Run this command:

```bash
python list_countries.py
```

This shows all 176 countries with their email addresses.

---

## 📝 Step-by-Step Example

### Example 1: Send Alert to India

1. Open terminal/command prompt
2. Navigate to your project folder:
   ```bash
   cd C:\Users\aish0\OneDrive\Documents\Desktop\Aish\Aish
   ```
3. Run:
   ```bash
   python send_email_simple.py
   ```
4. When prompted, type:
   ```
   India
   ```
5. Review the results
6. Type `yes` to send

### Example 2: Send Alerts to Multiple Countries

1. Run:
   ```bash
   python send_email_simple.py
   ```
2. When prompted, type:
   ```
   India, Nigeria, Kenya, Brazil, Chad
   ```
3. Review the results for all 5 countries
4. Type `yes` to send

---

## 🎯 What Each Country Status Means

When you run the system, countries are classified as:

| Status | Icon | Access % | Meaning |
|--------|------|----------|---------|
| **CRITICAL** | 🚨 | < 50% | Urgent action needed |
| **NEEDS IMPROVEMENT** | ⚠️ | 50-75% | Below target |
| **GOOD** | 👍 | 75-95% | On track |
| **EXCELLENT** | 🎉 | > 95% | Target achieved |

---

## 📧 Current Settings

- **Mode**: SIMULATION (no actual emails sent)
- **Your Email**: electricity.prediction2000@gmail.com
- **Testing**: All emails go to your address (safe for testing)

---

## 🔓 To Send Real Emails (Optional)

If you want to actually send emails:

1. **Get Gmail App Password**:
   - Go to: https://myaccount.google.com/apppasswords
   - Sign in with `electricity.prediction2000@gmail.com`
   - Generate App Password for "Mail"
   - Copy the 16-character code

2. **Update Configuration**:
   - Open `send_email_simple.py` in a text editor
   - Find line 11: `SENDER_PASSWORD = 'your-app-password'`
   - Replace `'your-app-password'` with your actual App Password
   - Find line 12: `ENABLE_SENDING = False`
   - Change to: `ENABLE_SENDING = True`
   - Save the file

3. **Test**:
   ```bash
   python send_email_simple.py
   ```

---

## 🌍 Popular Countries to Try

**High Access (Excellent)**:
- United States, Germany, Japan, France, United Kingdom, Brazil, India

**Needs Improvement**:
- Nigeria, Kenya, Bangladesh, Pakistan, Ghana, Indonesia

**Critical (Low Access)**:
- Chad, South Sudan, Burundi, Niger, Central African Republic

---

## 💡 Quick Commands Reference

| Command | What It Does |
|---------|--------------|
| `python auto_demo.py` | Shows demo with 5 countries |
| `python send_email_simple.py` | Send alerts to countries you choose |
| `python list_countries.py` | View all 176 available countries |

---

## ❓ Troubleshooting

**"Country not found"**
- Check spelling (case doesn't matter)
- Run `python list_countries.py` to see available countries

**"No module named pandas"**
- Install required packages:
  ```bash
  pip install pandas scikit-learn
  ```

**Script doesn't run**
- Make sure you're in the correct folder
- Check that Python is installed: `python --version`

---

## 🎓 Try It Now!

**Easiest way to start:**

1. Open terminal/command prompt
2. Run:
   ```bash
   python auto_demo.py
   ```
3. Watch the demo!

**Then try sending your own:**

1. Run:
   ```bash
   python send_email_simple.py
   ```
2. Enter: `India, Nigeria, Kenya`
3. Type `yes` to send

That's it! You're ready to use the email alert system! 🌍⚡📧

---

## 📚 More Help

- **HOW_TO_SEND_EMAILS.md** - Complete guide
- **EMAIL_QUICK_REFERENCE.md** - Quick commands
- **SEND_EMAIL_TO_COUNTRIES_GUIDE.md** - Detailed documentation

**Need help?** Just ask!
