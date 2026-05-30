# 🧪 How to Test Your APIs in Postman - Step by Step

## ✅ Your Server is Working!

I just tested it - your APIs are responding perfectly! Here's how YOU can test them in Postman.

---

## 🚀 Method 1: Quick Test (2 Minutes)

### Step 1: Open Postman
You already have it open! ✅

### Step 2: Create a New Request
1. Look at the top left
2. Click the **"New"** button (orange/red button)
3. Click **"HTTP Request"** or **"Request"**

### Step 3: Test Your First API
1. **Method**: Make sure it says **"GET"** (dropdown on the left)
2. **URL**: Copy and paste this:
   ```
   http://127.0.0.1:8000/api/countries/
   ```
3. **Click "Send"** (big blue button on the right)

### Step 4: Check the Result
Look at the bottom section - you should see:
- **Status**: `200 OK` (in green) ✅
- **Body**: A list of countries in JSON format

**Example Response:**
```json
{
    "countries": [
        "Afghanistan",
        "Albania",
        "Algeria",
        "India",
        "Kenya",
        ...
    ]
}
```

**✅ If you see this, your API is working!**

---

## 🎯 Method 2: Test with Parameters (3 Minutes)

### Test: Search for India

1. **New Request** (click "New" again)
2. **Method**: GET
3. **URL**: `http://127.0.0.1:8000/api/search/`
4. **Add Parameters**:
   - Click the **"Params"** tab (below the URL)
   - In the table that appears:
     - **Key**: type `country`
     - **Value**: type `India`
   - Postman will automatically add `?country=India` to your URL
5. **Click "Send"**

**Expected Result:**
```json
{
    "found": true,
    "country": "India",
    "electricity_access": 99.0,
    "clean_cooking_access": 67.9,
    ...
}
```

**✅ If you see India's data, it's working!**

---

## 📊 Method 3: Import My Collection (1 Minute)

### Step 1: Import the Collection
1. In Postman, click **"Import"** (top left, next to "New")
2. Click **"Upload Files"**
3. Select the file: **`SDG7_Postman_Collection.json`**
4. Click **"Import"**

### Step 2: Use Pre-made Requests
1. Look at the left sidebar
2. You'll see: **"SDG 7 Dashboard - Complete API Collection"**
3. Click the arrow to expand it
4. Click any request (like "Get All Countries")
5. Click **"Send"**

**✅ All requests are pre-configured and ready to use!**

---

## 🔍 How to Know if It's Working

### ✅ Success Signs:
1. **Status Code**: `200 OK` (green)
2. **Response Time**: Shows milliseconds (e.g., "245 ms")
3. **Body**: Shows JSON data
4. **Size**: Shows data size (e.g., "1.5 KB")

### ❌ Error Signs:
1. **Status Code**: `404 Not Found` or `500 Error` (red)
2. **Message**: "Could not get any response"
3. **Empty Body**: No data shown

---

## 🧪 5 Quick Tests to Try

### Test 1: Get All Countries ✅
```
Method: GET
URL: http://127.0.0.1:8000/api/countries/
Expected: List of 176 countries
```

### Test 2: Search India ✅
```
Method: GET
URL: http://127.0.0.1:8000/api/search/?country=India
Expected: India's energy data
```

### Test 3: Search Kenya ✅
```
Method: GET
URL: http://127.0.0.1:8000/api/search/?country=Kenya
Expected: Kenya's energy data
```

### Test 4: Predict Future ✅
```
Method: GET
URL: http://127.0.0.1:8000/api/predict/?country=Kenya&years=5
Expected: 5-year predictions for Kenya
```

### Test 5: Get Map Data ✅
```
Method: GET
URL: http://127.0.0.1:8000/api/map-data/
Expected: Map coordinates for all countries
```

---

## 📸 Visual Guide - What You Should See

### In Postman:

```
┌─────────────────────────────────────────────────────────┐
│  [New] [Import]                            [Send] ←Click│
├─────────────────────────────────────────────────────────┤
│                                                         │
│  GET ▼  http://127.0.0.1:8000/api/countries/  ←URL     │
│                                                         │
│  [Params] [Authorization] [Headers] [Body]              │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  Response                                               │
│  Status: 200 OK ✅  Time: 245 ms  Size: 1.5 KB         │
│                                                         │
│  [Body] [Cookies] [Headers]                             │
│                                                         │
│  {                                                      │
│    "countries": [                                       │
│      "Afghanistan",                                     │
│      "Albania",                                         │
│      "Algeria",                                         │
│      ...                                                │
│    ]                                                    │
│  }                                                      │
└─────────────────────────────────────────────────────────┘
```

---

## 🎯 Testing Checklist

Copy this and check off as you test:

### Basic Tests
- [ ] Get All Countries - Working? ___
- [ ] Search India - Working? ___
- [ ] Search Kenya - Working? ___
- [ ] Predict Kenya - Working? ___
- [ ] Get Map Data - Working? ___

### Status Codes
- [ ] All showing 200 OK? ___
- [ ] Response time < 1 second? ___
- [ ] JSON data visible? ___

---

## 🐛 Troubleshooting

### Problem 1: "Could not get any response"
**Cause**: Server not running
**Solution**:
```bash
cd sustainable_energy
python manage.py runserver
```
**Check**: Look for "Starting development server at http://127.0.0.1:8000/"

### Problem 2: "404 Not Found"
**Cause**: Wrong URL
**Solution**: Double-check the URL
- ✅ Correct: `http://127.0.0.1:8000/api/countries/`
- ❌ Wrong: `http://localhost:8000/api/countries/`
- ❌ Wrong: `http://127.0.0.1:8000/countries/` (missing /api/)

### Problem 3: "500 Internal Server Error"
**Cause**: Server error
**Solution**: Check your Django terminal for error messages

### Problem 4: Empty Response
**Cause**: Wrong country name
**Solution**: 
1. First test `/api/countries/` to get the list
2. Copy the exact country name
3. Use it in your search

---

## 💡 Pro Tips

### Tip 1: Save Your Requests
After testing, click **"Save"** to keep the request for later

### Tip 2: Organize in Folders
Create folders like:
- 📁 Main APIs
- 📁 Objective 1
- 📁 Objective 2

### Tip 3: Use Collections
Import `SDG7_Postman_Collection.json` to get all requests at once

### Tip 4: Check Response Time
Good: < 500ms
Acceptable: < 1000ms
Slow: > 1000ms

---

## 🎓 What Each Status Code Means

| Code | Meaning | What to Do |
|------|---------|------------|
| **200 OK** | ✅ Success! | Nothing - it's working |
| **404 Not Found** | ❌ Wrong URL | Check the URL spelling |
| **500 Error** | ❌ Server error | Check Django console |
| **Connection Error** | ❌ Server not running | Start Django server |

---

## 📝 Quick Reference Card

### To Test an API:
1. **Method**: GET (usually)
2. **URL**: `http://127.0.0.1:8000/api/...`
3. **Params**: Add in "Params" tab
4. **Send**: Click the blue button
5. **Check**: Look for 200 OK

### Common URLs:
```
/api/countries/                    - Get all countries
/api/search/?country=India         - Search India
/api/predict/?country=Kenya&years=5 - Predict Kenya
/api/map-data/                     - Get map data
```

---

## ✅ Verification Steps

### Step 1: Check Server
Open browser: `http://127.0.0.1:8000/`
- ✅ Should show your dashboard

### Step 2: Test in Postman
URL: `http://127.0.0.1:8000/api/countries/`
- ✅ Should show 200 OK
- ✅ Should show list of countries

### Step 3: Test with Parameters
URL: `http://127.0.0.1:8000/api/search/?country=India`
- ✅ Should show 200 OK
- ✅ Should show India's data

**If all 3 work, your APIs are 100% working!** ✅

---

## 🎉 Success Criteria

Your API is working if you see:
- ✅ Status: **200 OK** (green)
- ✅ Response time: **< 1 second**
- ✅ Body: **JSON data visible**
- ✅ Size: **Shows KB/MB**

---

## 📞 Need Help?

### If it's not working:
1. Check Django server is running
2. Check URL is correct
3. Check for typos in country name
4. Look at Django console for errors

### If it IS working:
1. ✅ Save your requests
2. ✅ Test all 5 quick tests
3. ✅ Import the collection
4. ✅ Ready for presentation!

---

**Your APIs are working! I tested them and got 200 OK responses. Now you try in Postman!** 🚀
