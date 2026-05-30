# ❌ Gmail App Password Not Working - How to Fix

## 🔍 Problem

The App Password `unbk roqm xrlz hpxb` is not being accepted by Gmail.

**Error:** `Username and Password not accepted`

---

## ✅ Solution: Generate New App Password

### Step 1: Check 2-Step Verification

1. Visit: https://myaccount.google.com/security
2. Sign in with: `assowmya649@gmail.com`
3. Look for **"2-Step Verification"**
4. Make sure it's **ENABLED** (turned ON)
5. If not enabled, click to enable it

### Step 2: Generate New App Password

1. Visit: https://myaccount.google.com/apppasswords
2. Sign in with: `assowmya649@gmail.com`
3. You should see "App passwords" page
4. Click **"Select app"** → Choose **"Mail"**
5. Click **"Select device"** → Choose **"Other (Custom name)"**
6. Type: **"SDG7 Alert System"**
7. Click **"Generate"**
8. **Copy the 16-character password** (e.g., `abcd efgh ijkl mnop`)

### Step 3: Update Configuration

Run this command and paste your NEW App Password:

```bash
python setup_gmail_password.py
```

**OR** manually edit `sustainable_energy/email_config.py`:

```python
'sender_password': 'your-new-16-char-password',  # Paste here (no spaces)
```

### Step 4: Test Again

```bash
python send_test_email_albania.py
```

---

## 🔧 Common Issues

### Issue 1: "App passwords" option not showing

**Solution:**
- Enable 2-Step Verification first
- Wait 5-10 minutes after enabling
- Refresh the page

### Issue 2: Old App Password not working

**Solution:**
- Generate a NEW App Password
- Delete the old one
- Use the new one in configuration

### Issue 3: Still getting authentication error

**Solution:**
- Make sure you're using the email: `assowmya649@gmail.com`
- Copy the App Password exactly (all 16 characters)
- Remove all spaces when pasting
- Try generating a fresh App Password

---

## 📝 Quick Steps

1. **Enable 2-Step Verification:**
   https://myaccount.google.com/security

2. **Generate App Password:**
   https://myaccount.google.com/apppasswords

3. **Update password:**
   ```bash
   python setup_gmail_password.py
   ```

4. **Test:**
   ```bash
   python send_test_email_albania.py
   ```

5. **Send real alert:**
   ```bash
   python send_xgboost_alert_to_country.py Albania
   ```

---

## ✅ Expected Result

When it works, you'll see:

```
✅ Login successful
✅ Email sent successfully!

🎉 SUCCESS! Email sent to assowmya649@gmail.com

📧 Check your inbox:
   Email: assowmya649@gmail.com
   Subject: 🎉 Test: XGBoost Alert System for Albania
```

Then check your email inbox at `assowmya649@gmail.com`!

---

## 🆘 Still Not Working?

Try these:

1. **Use Gmail's "Less secure app access"** (if available)
2. **Check if Gmail is blocking sign-in attempts**
   - Visit: https://myaccount.google.com/notifications
3. **Try from a different network** (mobile hotspot)
4. **Wait 15 minutes** and try again
5. **Contact Gmail support** if issue persists

---

## 📞 Need Help?

The App Password format should be:
- **16 characters**
- **4 groups of 4 characters**
- **Example:** `abcd efgh ijkl mnop`
- **No spaces when entering** (or keep spaces, both work)

Make sure you're copying the ENTIRE password from Google!

---

**Once you get a new App Password, the system will work perfectly!** 🎉
