# Fix 404 Error for Admin Login

## The Problem

You're getting "Page not found (404)" for `/admin-login/` because:
- The new URL routes haven't been loaded yet
- Django server needs to be restarted

## The Solution

### ⚠️ YOU MUST RESTART THE DJANGO SERVER!

**Step 1**: Stop the server
- Go to your Django terminal
- Press **Ctrl + C**

**Step 2**: Start the server again
```bash
python manage.py runserver
```

**Step 3**: Try the URL again
```
http://127.0.0.1:8000/admin-login/
```

## It Should Work Now! ✅

---

## If Still Getting 404:

### Check 1: Are you in the right directory?

Make sure you're running the server from:
```bash
cd C:\Users\aish0\OneDrive\Documents\Desktop\Aish\Aish
python manage.py runserver
```

### Check 2: Is the server actually running?

Look for this message:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Check 3: Try the exact URL

Make sure you're going to:
```
http://127.0.0.1:8000/admin-login/
```

NOT:
- ~~http://127.0.0.1:8000/admin/login/~~
- ~~http://127.0.0.1:8000/login/~~

---

## Quick Test

After restarting, try these URLs to verify:

1. Main page: http://127.0.0.1:8000/
2. Admin login: http://127.0.0.1:8000/admin-login/
3. Email alerts: http://127.0.0.1:8000/objective8/

---

## The Fix is Simple:

```bash
# 1. Stop server
Ctrl + C

# 2. Start server
python manage.py runserver

# 3. Go to browser
http://127.0.0.1:8000/admin-login/
```

**That's it! The 404 error will be gone!** 🚀
