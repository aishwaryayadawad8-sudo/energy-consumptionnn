# 📮 Postman API Testing Guide for SDG 7 Dashboard

## 🎯 Complete Guide to Test Your APIs

This guide shows you how to test all your SDG 7 Dashboard APIs using Postman.

---

## 🚀 Quick Start

### Step 1: Start Your Django Server
```bash
cd sustainable_energy
python manage.py runserver
```
Your server will run at: **http://127.0.0.1:8000/**

### Step 2: Open Postman
You already have it open! ✅

### Step 3: Create a New Collection
1. Click "Collections" in the left sidebar
2. Click "New" → "Collection"
3. Name it: **"SDG 7 Dashboard APIs"**
4. Click "Create"

---

## 📋 All Available APIs

Your dashboard has **40+ API endpoints**! Here are the main ones:

### 🌍 Main Dashboard APIs
1. Search Country
2. Predict Future
3. Get All Countries
4. Get Map Data

### ⚡ Objective 1: Energy Consumption
5. Model Comparison
6. Historical Data
7. Future Predictions
8. Countries List

### 💨 Objective 2: CO₂ Emissions
9. Model Comparison
10. Historical Data
11. Future Predictions
12. Countries List

### 🔌 Objective 3: Electricity Access
13. Model Comparison
14. Historical Data
15. Future Predictions
16. Countries List
17. Distribution Data
18. Combined Data
19. Policy Markers

### 🎯 Objective 4-8: Similar structure

### 📧 Email Alert APIs
40. Send Email Alerts
41. Get Email Logs

---

## 🧪 Testing Your APIs in Postman

### Test 1: Search Country (GET Request)

**Purpose**: Get energy profile for a specific country

**Steps in Postman:**

1. **Click "New" → "Request"**
2. **Name**: "Search Country - India"
3. **Save to**: SDG 7 Dashboard APIs collection

4. **Configure Request:**
   - **Method**: GET
   - **URL**: `http://127.0.0.1:8000/api/search/`
   - **Params** (click "Params" tab):
     - Key: `country`
     - Value: `India`

5. **Click "Send"**

**Expected Response:**
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
        "alerts": [
            "Electricity access is excellent (>80%)"
        ]
    },
    "historical_data": [...]
}
```

---

### Test 2: Get All Countries (GET Request)

**Purpose**: Get list of all countries in database

**Steps:**

1. **New Request**
2. **Name**: "Get All Countries"
3. **Method**: GET
4. **URL**: `http://127.0.0.1:8000/api/countries/`
5. **Click "Send"**

**Expected Response:**
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

---

### Test 3: Predict Future (GET Request)

**Purpose**: Get ML predictions for future electricity access

**Steps:**

1. **New Request**
2. **Name**: "Predict Future - Kenya"
3. **Method**: GET
4. **URL**: `http://127.0.0.1:8000/api/predict/`
5. **Params**:
   - Key: `country`, Value: `Kenya`
   - Key: `years`, Value: `5`
6. **Click "Send"**

**Expected Response:**
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

### Test 4: Get Map Data (GET Request)

**Purpose**: Get data for world map visualization

**Steps:**

1. **New Request**
2. **Name**: "Get Map Data"
3. **Method**: GET
4. **URL**: `http://127.0.0.1:8000/api/map-data/`
5. **Click "Send"**

**Expected Response:**
```json
{
    "map_data": [
        {
            "country": "India",
            "lat": 20.5937,
            "lon": 78.9629,
            "electricity_access": 99.6,
            "renewable_share": 38.2,
            "co2_emissions": 2441705.0
        },
        ...
    ]
}
```

---

### Test 5: Objective 1 - Model Comparison (GET Request)

**Purpose**: Compare ML models for energy consumption

**Steps:**

1. **New Request**
2. **Name**: "Objective 1 - Model Comparison"
3. **Method**: GET
4. **URL**: `http://127.0.0.1:8000/api/objective1/model-comparison/`
5. **Click "Send"**

**Expected Response:**
```json
{
    "models": {
        "CatBoost": 1234.56,
        "Random Forest": 2345.67,
        "XGBoost": 3456.78
    },
    "best_model": "CatBoost"
}
```

---

### Test 6: Objective 1 - Historical Data (GET Request)

**Purpose**: Get historical energy consumption data

**Steps:**

1. **New Request**
2. **Name**: "Objective 1 - Historical Data"
3. **Method**: GET
4. **URL**: `http://127.0.0.1:8000/api/objective1/historical-data/`
5. **Params**:
   - Key: `country`, Value: `Germany`
6. **Click "Send"**

**Expected Response:**
```json
{
    "country": "Germany",
    "data": [
        {
            "year": 2000,
            "consumption": 5432.1
        },
        {
            "year": 2001,
            "consumption": 5567.8
        },
        ...
    ]
}
```

---

### Test 7: Objective 1 - Future Predictions (GET Request)

**Purpose**: Get future energy consumption predictions

**Steps:**

1. **New Request**
2. **Name**: "Objective 1 - Future Predictions"
3. **Method**: GET
4. **URL**: `http://127.0.0.1:8000/api/objective1/future-predictions/`
5. **Params**:
   - Key: `country`, Value: `United States`
   - Key: `years`, Value: `10`
6. **Click "Send"**

---

### Test 8: Send Email Alerts (POST Request)

**Purpose**: Send email alerts to all countries

**Steps:**

1. **New Request**
2. **Name**: "Send Email Alerts"
3. **Method**: POST
4. **URL**: `http://127.0.0.1:8000/api/send-email-alerts/`
5. **Click "Send"**

**Expected Response:**
```json
{
    "success": true,
    "total_alerts": 15,
    "alerts_sent": [
        {
            "country": "Kenya",
            "access": 45.2,
            "status": "critical",
            "email": "kenya@example.com"
        },
        ...
    ]
}
```

---

## 📊 Complete API Endpoint List

### Main Dashboard
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/search/` | GET | Search country |
| `/api/predict/` | GET | Predict future |
| `/api/countries/` | GET | Get all countries |
| `/api/map-data/` | GET | Get map data |

### Objective 1: Energy Consumption
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/objective1/model-comparison/` | GET | Model comparison |
| `/api/objective1/historical-data/` | GET | Historical data |
| `/api/objective1/future-predictions/` | GET | Future predictions |
| `/api/objective1/countries/` | GET | Countries list |

### Objective 2: CO₂ Emissions
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/objective2/model-comparison/` | GET | Model comparison |
| `/api/objective2/historical-data/` | GET | Historical data |
| `/api/objective2/future-predictions/` | GET | Future predictions |
| `/api/objective2/countries/` | GET | Countries list |

### Objective 3: Electricity Access
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/objective3/model-comparison/` | GET | Model comparison |
| `/api/objective3/historical-data/` | GET | Historical data |
| `/api/objective3/future-predictions/` | GET | Future predictions |
| `/api/objective3/countries/` | GET | Countries list |
| `/api/objective3/distribution/` | GET | Distribution data |
| `/api/objective3/combined-data/` | GET | Combined data |
| `/api/objective3/policy-markers/` | GET | Policy markers |

### Objectives 4-8: Similar structure

### Email Alerts
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/send-email-alerts/` | POST | Send alerts |
| `/admin/email-logs/` | GET | View email logs |

---

## 🎨 Postman Collection JSON

Save this as a file and import into Postman:

```json
{
    "info": {
        "name": "SDG 7 Dashboard APIs",
        "description": "Complete API collection for SDG 7 Sustainable Energy Dashboard",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    },
    "item": [
        {
            "name": "Main Dashboard",
            "item": [
                {
                    "name": "Search Country",
                    "request": {
                        "method": "GET",
                        "header": [],
                        "url": {
                            "raw": "http://127.0.0.1:8000/api/search/?country=India",
                            "protocol": "http",
                            "host": ["127", "0", "0", "1"],
                            "port": "8000",
                            "path": ["api", "search", ""],
                            "query": [
                                {
                                    "key": "country",
                                    "value": "India"
                                }
                            ]
                        }
                    }
                },
                {
                    "name": "Get All Countries",
                    "request": {
                        "method": "GET",
                        "header": [],
                        "url": {
                            "raw": "http://127.0.0.1:8000/api/countries/",
                            "protocol": "http",
                            "host": ["127", "0", "0", "1"],
                            "port": "8000",
                            "path": ["api", "countries", ""]
                        }
                    }
                },
                {
                    "name": "Predict Future",
                    "request": {
                        "method": "GET",
                        "header": [],
                        "url": {
                            "raw": "http://127.0.0.1:8000/api/predict/?country=Kenya&years=5",
                            "protocol": "http",
                            "host": ["127", "0", "0", "1"],
                            "port": "8000",
                            "path": ["api", "predict", ""],
                            "query": [
                                {
                                    "key": "country",
                                    "value": "Kenya"
                                },
                                {
                                    "key": "years",
                                    "value": "5"
                                }
                            ]
                        }
                    }
                },
                {
                    "name": "Get Map Data",
                    "request": {
                        "method": "GET",
                        "header": [],
                        "url": {
                            "raw": "http://127.0.0.1:8000/api/map-data/",
                            "protocol": "http",
                            "host": ["127", "0", "0", "1"],
                            "port": "8000",
                            "path": ["api", "map-data", ""]
                        }
                    }
                }
            ]
        },
        {
            "name": "Objective 1: Energy Consumption",
            "item": [
                {
                    "name": "Model Comparison",
                    "request": {
                        "method": "GET",
                        "header": [],
                        "url": {
                            "raw": "http://127.0.0.1:8000/api/objective1/model-comparison/",
                            "protocol": "http",
                            "host": ["127", "0", "0", "1"],
                            "port": "8000",
                            "path": ["api", "objective1", "model-comparison", ""]
                        }
                    }
                },
                {
                    "name": "Historical Data",
                    "request": {
                        "method": "GET",
                        "header": [],
                        "url": {
                            "raw": "http://127.0.0.1:8000/api/objective1/historical-data/?country=Germany",
                            "protocol": "http",
                            "host": ["127", "0", "0", "1"],
                            "port": "8000",
                            "path": ["api", "objective1", "historical-data", ""],
                            "query": [
                                {
                                    "key": "country",
                                    "value": "Germany"
                                }
                            ]
                        }
                    }
                },
                {
                    "name": "Future Predictions",
                    "request": {
                        "method": "GET",
                        "header": [],
                        "url": {
                            "raw": "http://127.0.0.1:8000/api/objective1/future-predictions/?country=United States&years=10",
                            "protocol": "http",
                            "host": ["127", "0", "0", "1"],
                            "port": "8000",
                            "path": ["api", "objective1", "future-predictions", ""],
                            "query": [
                                {
                                    "key": "country",
                                    "value": "United States"
                                },
                                {
                                    "key": "years",
                                    "value": "10"
                                }
                            ]
                        }
                    }
                }
            ]
        },
        {
            "name": "Email Alerts",
            "item": [
                {
                    "name": "Send Email Alerts",
                    "request": {
                        "method": "POST",
                        "header": [],
                        "url": {
                            "raw": "http://127.0.0.1:8000/api/send-email-alerts/",
                            "protocol": "http",
                            "host": ["127", "0", "0", "1"],
                            "port": "8000",
                            "path": ["api", "send-email-alerts", ""]
                        }
                    }
                }
            ]
        }
    ]
}
```

---

## 🔍 How to Test Each API

### For GET Requests:
1. Select "GET" method
2. Enter URL
3. Add query parameters (if needed)
4. Click "Send"
5. Check response in "Body" tab

### For POST Requests:
1. Select "POST" method
2. Enter URL
3. Add body data (if needed)
4. Click "Send"
5. Check response

---

## ✅ Testing Checklist

Test these APIs in order:

- [ ] Get All Countries
- [ ] Search Country (India)
- [ ] Search Country (Kenya)
- [ ] Predict Future (Kenya, 5 years)
- [ ] Get Map Data
- [ ] Objective 1 - Model Comparison
- [ ] Objective 1 - Historical Data (Germany)
- [ ] Objective 1 - Future Predictions (USA, 10 years)
- [ ] Objective 2 - Model Comparison
- [ ] Objective 3 - Model Comparison
- [ ] Send Email Alerts (POST)

---

## 🐛 Troubleshooting

### Error: "Connection refused"
**Solution**: Make sure Django server is running
```bash
cd sustainable_energy
python manage.py runserver
```

### Error: "404 Not Found"
**Solution**: Check the URL is correct. Should be `http://127.0.0.1:8000/api/...`

### Error: "500 Internal Server Error"
**Solution**: Check Django console for error details

### Empty Response
**Solution**: Check if country name is spelled correctly

---

## 📝 Next Steps

1. **Import Collection**: Use the JSON above
2. **Test All APIs**: Go through the checklist
3. **Save Responses**: Use Postman's "Save Response" feature
4. **Create Tests**: Add assertions in Postman
5. **Share Collection**: Export and share with team

---

**Your APIs are ready to test! Start with "Get All Countries" to see the list of available countries.** 📮✅
