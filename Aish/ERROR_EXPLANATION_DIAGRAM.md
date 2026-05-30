# Visual Error Explanation

## Error Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    USER ACTION                               │
│  User selects "Albania" and clicks "Send Alerts"            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                 FRONTEND (JavaScript)                        │
│  Sends POST request with JSON: {"countries": ["Albania"]}   │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              DJANGO BACKEND (views.py)                       │
│  Function: send_email_alerts_selected()                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                ML MODEL (sdg7_forecasting.py)                │
│  Predicts electricity access for Albania                    │
│  Returns: (2020, 'Albania', np.float64(100.0))             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│            EMAIL ALERT SYSTEM (email_alerts.py)              │
│  Analyzes prediction and creates alert                      │
│  Returns: [{'country': 'Albania', 'access': np.float64...}] │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              ❌ ERROR OCCURS HERE ❌                         │
│  Django tries to convert to JSON                            │
│  JsonResponse({'alerts_sent': [numpy types]})               │
│  ❌ FAILS: Cannot serialize numpy.float64 to JSON           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  HTTP 500 ERROR                              │
│  "Error sending alerts: HTTP error! status: 500"            │
└─────────────────────────────────────────────────────────────┘
```

## The Problem in Detail

### What Happens:

```python
# Step 1: ML Model returns NumPy types
prediction = (2020, 'Albania', np.float64(100.0))

# Step 2: Email system creates dict with NumPy types
alert = {
    'country': 'Albania',
    'access': np.float64(100.0),  # ❌ NumPy type
    'year': np.int64(2020)         # ❌ NumPy type
}

# Step 3: Django tries to convert to JSON
return JsonResponse({'alerts_sent': [alert]})
# ❌ ERROR: Object of type float64 is not JSON serializable
```

### Why It Fails:

```
JSON Standard Types:        NumPy/Pandas Types:
├── string                  ├── np.str_
├── number                  ├── np.int64    ❌ Not compatible
├── boolean                 ├── np.float64  ❌ Not compatible
├── null                    ├── np.bool_    ❌ Not compatible
├── array                   └── pd.Series   ❌ Not compatible
└── object
```

## The Solution

### Type Conversion Flow:

```
┌─────────────────────────────────────────────────────────────┐
│              EMAIL ALERT SYSTEM RETURNS                      │
│  [{'country': 'Albania', 'access': np.float64(100.0)}]     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│           ✅ TYPE CONVERSION (NEW CODE)                      │
│  for alert in alerts_sent:                                  │
│      alerts_json.append({                                   │
│          'country': str(alert['country']),                  │
│          'access': float(alert['access']),  # Convert!      │
│          'year': int(alert['year'])         # Convert!      │
│      })                                                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              NATIVE PYTHON TYPES                             │
│  [{'country': 'Albania', 'access': 100.0, 'year': 2020}]   │
│  ✅ All types are JSON-compatible                           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              JSON SERIALIZATION SUCCESS                      │
│  JsonResponse({'alerts_sent': alerts_json})                 │
│  ✅ Successfully converts to JSON                           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              FRONTEND RECEIVES RESPONSE                      │
│  {"success": true, "alerts_sent": [...]}                    │
│  ✅ Displays success message                                │
└─────────────────────────────────────────────────────────────┘
```

## Code Comparison

### ❌ BEFORE (Broken):

```python
def send_email_alerts_selected(request):
    # ... code ...
    
    alerts_sent = alert_system.analyze_and_send_alerts(predictions_df)
    
    # ❌ Direct return - contains NumPy types
    return JsonResponse({
        'success': True,
        'alerts_sent': alerts_sent,  # PROBLEM HERE
        'total_alerts': len(alerts_sent)
    })
```

### ✅ AFTER (Fixed):

```python
def send_email_alerts_selected(request):
    # ... code ...
    
    alerts_sent = alert_system.analyze_and_send_alerts(predictions_df)
    
    # ✅ Convert to JSON-safe types
    alerts_json = []
    for alert in alerts_sent:
        alerts_json.append({
            'country': str(alert.get('country', '')),
            'email': str(alert.get('email', '')),
            'status': str(alert.get('status', '')),
            'access': float(alert.get('access', 0)),    # ✅ Convert
            'year': int(alert.get('year', 0)),          # ✅ Convert
            'subject': str(alert.get('subject', ''))
        })
    
    # ✅ Return JSON-safe data
    return JsonResponse({
        'success': True,
        'alerts_sent': alerts_json,  # FIXED
        'total_alerts': len(alerts_json)
    })
```

## Key Takeaways

### 1. Data Type Compatibility
```
NumPy/Pandas → Must Convert → Native Python → JSON
np.float64   →    float()   →    float      → ✅
np.int64     →    int()     →    int        → ✅
np.str_      →    str()     →    str        → ✅
```

### 2. Why This Happens
- ML libraries (NumPy, Pandas) use optimized data types
- These types are not JSON-compatible
- Django's JsonResponse requires native Python types
- Explicit conversion is necessary

### 3. The Fix
- Loop through each alert
- Convert each field to native Python type
- Use `.get()` for safe access
- Return converted data

### 4. Prevention
- Always check data types when working with ML models
- Test JSON serialization early
- Use type hints in Python
- Add comprehensive error logging

---

**This diagram explains the complete error flow and solution for your lecturer.**
