# Debug HTTP 500 Error - Step by Step

## I've Added Debug Logging

I've added extensive debug logging to help us find the exact issue.

## What You Need to Do:

### Step 1: Restart Django Server

**CRITICAL**: Stop and restart your server!

```bash
# In terminal, press Ctrl+C to stop
# Then start again:
python manage.py runserver
```

### Step 2: Try Sending Alert Again

1. Go to: http://127.0.0.1:8000/objective8/
2. Select Albania
3. Click "Send Alerts to Selected Countries"

### Step 3: Check Django Terminal

Look at the terminal where Django is running. You should see debug messages like:

```
DEBUG: predictions_df shape: (1, 3)
DEBUG: predictions_df columns: ['year', 'country', 'predicted_access']
DEBUG: alerts_sent type: <class 'list'>
DEBUG: alerts_sent length: 1
DEBUG: First alert: {'country': 'Albania', 'email': '...', ...}
DEBUG: Converted alert for Albania
```

### Step 4: Copy the Error

If you see an error, copy the ENTIRE error message from the terminal and share it with me.

It will look something like:

```
============================================================
ERROR in send_email_alerts_selected:
Traceback (most recent call last):
  File "...", line ..., in send_email_alerts_selected
    ...
[ERROR DETAILS HERE]
============================================================
```

## Common Issues & Solutions

### Issue 1: "No module named 'ml_models'"

**Solution**: Make sure you're running the server from the correct directory:
```bash
cd C:\Users\aish0\OneDrive\Documents\Desktop\Aish\Aish
python manage.py runserver
```

### Issue 2: "CSV file not found"

**Solution**: Check that `global-data-on-sustainable-energy.csv` exists in your project root.

### Issue 3: "KeyError" or "AttributeError"

**Solution**: The debug logs will show exactly which line is failing. Share the error with me.

## Quick Test

Try this simple test to see if the basic API works:

1. Open a new terminal
2. Run:
```bash
curl -X POST http://127.0.0.1:8000/api/send-email-alerts-selected/ -H "Content-Type: application/json" -d "{\"countries\": [\"Albania\"]}"
```

3. Check what it returns

## What I Need From You

To fix this, I need to see:

1. ✅ The FULL error message from Django terminal
2. ✅ The debug output (all the "DEBUG:" lines)
3. ✅ Any other error messages

## Alternative: Check Browser Console

1. Press F12 in your browser
2. Go to "Console" tab
3. Look for error messages
4. Share any red error messages you see

---

**Please restart your server and share the error output from the Django terminal!**
