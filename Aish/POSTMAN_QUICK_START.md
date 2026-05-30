# 🚀 Postman Quick Start - Test Your APIs in 5 Minutes

## ✅ Prerequisites

1. ✅ Postman installed and open (You have this!)
2. ✅ Django server running
3. ✅ Your SDG 7 Dashboard working

---

## 🎯 Quick Start (5 Steps)

### Step 1: Start Your Django Server (1 minute)

Open terminal and run:
```bash
cd sustainable_energy
python manage.py runserver
```

**Wait for**: `Starting development server at http://127.0.0.1:8000/`

---

### Step 2: Import Collection into Postman (1 minute)

**Option A: Import JSON File**
1. In Postman, click **"Import"** (top left)
2. Click **"Upload Files"**
3. Select: `SDG7_Postman_Collection.json`
4. Click **"Import"**

**Option B: Manual Setup**
1. Click **"Collections"** in left sidebar
2. Click **"New"** → **"Collection"**
3. Name it: **"SDG 7 APIs"**
4. Click **"Create"**

---

### Step 3: Test Your First API (1 minute)

**Test: Get All Countries**

1. Click **"New"** → **"Request"**
2. Name: **"Get All Countries"**
3. Save to: **SDG 7 APIs** collection
4. Set Method: **GET**
5. Enter URL: `http://127.0.0.1:8000/api/countries/`
6. Click **"Send"** (blue button)

**✅ Expected Result:**
```json
{
    "countries": [
        "Afghanistan",
        "Albania",
        "Algeria",
        ...
        "India",
        "Kenya",
        ...
    ]
}
```

**Status**: Should show **200 OK** (green)

---

### Step 4: Test Search Country API (1 minute)

**Test: Search for India**

1. Click **"New"** → **"Request"**
2. Name: **"Search India"**
3. Method: **GET**
4. URL: `http://127.0.0.1:8000/api/search/`
5. Click **"Params"** tab (below URL)
6. Add parameter:
   - **Key**: `country`
   - **Value**: `India`
7. Click **"Send"**

**✅ Expected Result:**
```json
{
    "found": true,
    "country": "India",
    "latest_year": 2020,
    "electricity_access": 99.6,
    "clean_cooking_access": 58.7,
    "renewable_share": 38.2,
    "co2_emissions": 2441705.0,
    "status": {
        "status": "Excellent",
        "alerts": [...]
    },
    "historical_data": [...]
}
```

---

### Step 5: Test ML Predictions API (1 minute)

**Test: Predict Future for Kenya**

1. New Request: **"Predict Kenya"**
2. Method: **GET**
3. URL: `http://127.0.0.1:8000/api/predict/`
4. Params:
   - **Key**: `country`, **Value**: `Kenya`
   - **Key**: `years`, **Value**: `5`
5. Click **"Send"**

**✅ Expected Result:**
```json
{
    "found": true,
    "country": "Kenya",
    "model_used": "CatBoost",
    "predictions": [
        {
            "year": 2021,
            "predicted_access": 75.3
        },
        {
            "year": 2022,
            "predicted_access": 76.8
        },
        ...
    ]
}
```

---

## 🎨 Postman Interface Guide

### Main Areas:

```
┌─────────────────────────────────────────────────────────┐
│  [Import] [New]                            [Send] ←Click│
├─────────────────────────────────────────────────────────┤
│                                                         │
│  GET  http://127.0.0.1:8000/api/search/  ←Enter URL    │
│                                                         │
│  [Params] [Authorization] [Headers] [Body]  ←Tabs      │
│                                                         │
│  Key          Value                         ←Add params│
│  country      India                                     │
│  + Add                                                  │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  Response (200 OK)                         ←Check here │
│                                                         │
│  {                                                      │
│    "found": true,                                       │
│    "country": "India",                                  │
│    ...                                                  │
│  }                                                      │
└─────────────────────────────────────────────────────────┘
```

---

## 📋 Quick Test Checklist

Test these APIs in order:

### ✅ Basic APIs (Start Here!)
- [ ] **Get All Countries** - `GET /api/countries/`
- [ ] **Search India** - `GET /api/search/?country=India`
- [ ] **Search Kenya** - `GET /api/search/?country=Kenya`
- [ ] **Predict Kenya** - `GET /api/predict/?country=Kenya&years=5`
- [ ] **Get Map Data** - `GET /api/map-data/`

### ✅ Objective 1: Energy Consumption
- [ ] **Model Comparison** - `GET /api/objective1/model-comparison/`
- [ ] **Historical Data** - `GET /api/objective1/historical-data/?country=Germany`
- [ ] **Future Predictions** - `GET /api/objective1/future-predictions/?country=United States&years=10`

### ✅ Objective 2: CO₂ Emissions
- [ ] **Model Comparison** - `GET /api/objective2/model-comparison/`
- [ ] **Historical Data** - `GET /api/objective2/historical-data/?country=China`

### ✅ Objective 3: Electricity Access
- [ ] **Model Comparison** - `GET /api/objective3/model-comparison/`
- [ ] **Historical Data** - `GET /api/objective3/historical-data/?country=Nigeria`

### ✅ Email Alerts
- [ ] **Send Alerts** - `POST /api/send-email-alerts/`

---

## 🎯 Common Test Scenarios

### Scenario 1: Test Different Countries
```
India       → High electricity access (99.6%)
Kenya       → Medium access (75%)
Nigeria     → Lower access (55%)
Afghanistan → Low access (43%)
```

### Scenario 2: Test Different Time Ranges
```
years=1   → Next year only
years=5   → 5-year forecast
years=10  → 10-year forecast
```

### Scenario 3: Test All Objectives
```
Objective 1 → Energy Consumption
Objective 2 → CO₂ Emissions
Objective 3 → Electricity Access
Objective 4 → SDG 7 Forecasting
Objective 5 → Energy Classification
Objective 6 → Renewable Potential
Objective 7 → Investment Strategy
Objective 8 → Email Alerts
```

---

## 🐛 Troubleshooting

### ❌ Error: "Could not get any response"
**Problem**: Django server not running
**Solution**:
```bash
cd sustainable_energy
python manage.py runserver
```

### ❌ Error: "404 Not Found"
**Problem**: Wrong URL
**Solution**: Check URL is exactly: `http://127.0.0.1:8000/api/...`

### ❌ Error: "500 Internal Server Error"
**Problem**: Server error
**Solution**: Check Django console for error details

### ❌ Empty Response `{}`
**Problem**: Country name incorrect
**Solution**: 
1. First call `/api/countries/` to get correct names
2. Use exact spelling (case-sensitive)

---

## 💡 Pro Tips

### Tip 1: Save Responses
Click **"Save Response"** to keep examples

### Tip 2: Use Variables
Create environment variable for base URL:
- Variable: `base_url`
- Value: `http://127.0.0.1:8000`
- Use: `{{base_url}}/api/search/`

### Tip 3: Organize Requests
Create folders for each objective:
- 📁 Main Dashboard
- 📁 Objective 1
- 📁 Objective 2
- 📁 Email Alerts

### Tip 4: Add Tests
In Postman, go to "Tests" tab and add:
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response has data", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('found');
});
```

---

## 📊 All Your API Endpoints

### Main Dashboard (5 APIs)
```
GET  /api/search/           - Search country
GET  /api/predict/          - Predict future
GET  /api/countries/        - Get all countries
GET  /api/map-data/         - Get map data
GET  /                      - Main dashboard page
```

### Objective 1: Energy Consumption (4 APIs)
```
GET  /api/objective1/model-comparison/
GET  /api/objective1/historical-data/
GET  /api/objective1/future-predictions/
GET  /api/objective1/countries/
```

### Objective 2: CO₂ Emissions (4 APIs)
```
GET  /api/objective2/model-comparison/
GET  /api/objective2/historical-data/
GET  /api/objective2/future-predictions/
GET  /api/objective2/countries/
```

### Objective 3: Electricity Access (7 APIs)
```
GET  /api/objective3/model-comparison/
GET  /api/objective3/historical-data/
GET  /api/objective3/future-predictions/
GET  /api/objective3/countries/
GET  /api/objective3/distribution/
GET  /api/objective3/combined-data/
GET  /api/objective3/policy-markers/
```

### Objectives 4-8: Similar structure

### Email Alerts (1 API)
```
POST /api/send-email-alerts/
```

**Total: 40+ APIs ready to test!**

---

## 🎉 You're Ready!

You now know how to:
- ✅ Import Postman collection
- ✅ Test GET requests
- ✅ Test POST requests
- ✅ Add query parameters
- ✅ Check responses
- ✅ Troubleshoot errors

**Start testing your APIs now!** 📮

---

## 📚 Next Steps

1. **Test all basic APIs** (5 minutes)
2. **Test each objective** (10 minutes)
3. **Save your collection** (Export → Share)
4. **Add to documentation** (Screenshots)
5. **Demo in presentation** (Show live API calls)

---

**Your APIs are production-ready and fully testable!** ✅
