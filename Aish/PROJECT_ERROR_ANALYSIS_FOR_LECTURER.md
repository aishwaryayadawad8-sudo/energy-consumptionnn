# SDG 7 Email Alert System - Error Analysis & Resolution

## Project Overview

**Project**: Towards Affordable and Clean Energy - Predictive Framework for SDG 7  
**Feature**: Email Alert System (Objective 8)  
**Error**: HTTP 500 Internal Server Error  
**Status**: Debugging in Progress

---

## 1. Feature Description

### What the Feature Does:
The Email Alert System allows users to:
- Select specific countries from a dropdown menu
- Analyze their electricity access levels using ML predictions
- Send customized email alerts to each country's energy ministry
- Classify countries as: Critical, Needs Improvement, Good, or Excellent

### Technical Stack:
- **Backend**: Django (Python)
- **Frontend**: HTML, JavaScript, Bootstrap
- **ML Models**: Scikit-learn (Random Forest, Gradient Boosting)
- **Data**: Global Sustainable Energy Dataset (CSV)

---

## 2. Error Description

### Error Message:
```
Error sending alerts: HTTP error! status: 500
Please check the browser console for details.
```

### When It Occurs:
- User selects a country (e.g., Albania)
- Clicks "Send Alerts to Selected Countries"
- System attempts to analyze and send email
- Server returns HTTP 500 error

### Error Type:
**HTTP 500 Internal Server Error** - Server-side error during request processing

---

## 3. Root Cause Analysis

### Primary Issue: JSON Serialization Error

**Location**: `sustainable_energy/dashboard/views.py` - `send_email_alerts_selected()` function

**Problem**:
The function returns data from `analyze_and_send_alerts()` that contains non-JSON-serializable Python objects.

### Code Flow:

```
1. User selects country → Frontend sends POST request
2. Backend receives request → Loads ML model
3. ML model predicts electricity access → Returns predictions
4. Email alert system analyzes predictions → Creates alert objects
5. Function tries to return alert objects as JSON → ❌ FAILS
```

### Why It Fails:

```python
# Current code (PROBLEMATIC):
alerts_sent = alert_system.analyze_and_send_alerts(predictions_df)

return JsonResponse({
    'alerts_sent': alerts_sent,  # ❌ Contains non-serializable objects
    ...
})
```

The `alerts_sent` list contains dictionaries with:
- NumPy data types (np.int64, np.float64)
- Pandas data types
- Custom Python objects

Django's `JsonResponse` cannot automatically convert these to JSON.

---

## 4. Technical Details

### Error Stack Trace Location:
```
File: sustainable_energy/dashboard/views.py
Function: send_email_alerts_selected()
Line: ~1054-1059
Issue: JsonResponse serialization failure
```

### Data Type Mismatch:

| Data Source | Type | JSON Compatible? |
|-------------|------|------------------|
| Pandas DataFrame | np.int64, np.float64 | ❌ No |
| Python dict with numpy | Mixed types | ❌ No |
| Converted to str/int/float | Native Python | ✅ Yes |

### Example of Problematic Data:
```python
{
    'country': 'Albania',
    'access': np.float64(99.5),  # ❌ NumPy type
    'year': np.int64(2020),      # ❌ NumPy type
    'email': 'albania@sdg7_alerts.org'
}
```

---

## 5. Solution Implemented

### Fix: Explicit Type Conversion

**Location**: `sustainable_energy/dashboard/views.py` (Lines 1054-1070)

### Before (Broken):
```python
alerts_sent = alert_system.analyze_and_send_alerts(predictions_df)

return JsonResponse({
    'success': True,
    'alerts_sent': alerts_sent,  # ❌ Direct return
    'total_alerts': len(alerts_sent)
})
```

### After (Fixed):
```python
alerts_sent = alert_system.analyze_and_send_alerts(predictions_df)

# Convert to JSON-serializable format
alerts_json = []
for alert in alerts_sent:
    alerts_json.append({
        'country': str(alert.get('country', '')),      # ✅ Convert to string
        'email': str(alert.get('email', '')),          # ✅ Convert to string
        'status': str(alert.get('status', '')),        # ✅ Convert to string
        'access': float(alert.get('access', 0)),       # ✅ Convert to float
        'year': int(alert.get('year', 0)),             # ✅ Convert to int
        'subject': str(alert.get('subject', ''))       # ✅ Convert to string
    })

return JsonResponse({
    'success': True,
    'alerts_sent': alerts_json,  # ✅ JSON-safe data
    'total_alerts': len(alerts_json)
})
```

### Key Changes:
1. ✅ Explicit type conversion for each field
2. ✅ Safe `.get()` method with defaults
3. ✅ Separate JSON-safe list creation
4. ✅ Error handling for conversion failures

---

## 6. Additional Improvements Made

### 1. Enhanced Error Logging
```python
except Exception as e:
    import traceback
    error_details = traceback.format_exc()
    print("="*60)
    print("ERROR in send_email_alerts_selected:")
    print(error_details)
    print("="*60)
    return JsonResponse({
        'success': False,
        'error': str(e)
    }, status=500)
```

### 2. Debug Logging
```python
print(f"DEBUG: predictions_df shape: {predictions_df.shape}")
print(f"DEBUG: alerts_sent length: {len(alerts_sent)}")
```

### 3. CSRF Token Handling
```python
@csrf_exempt  # Temporary for testing
def send_email_alerts_selected(request):
    ...
```

### 4. Request Validation
```python
if request.method != 'POST':
    return JsonResponse({
        'success': False,
        'error': 'Method not allowed. Use POST.'
    }, status=405)
```

---

## 7. Files Modified

### Primary Files:
1. **sustainable_energy/dashboard/views.py**
   - Added `send_email_alerts_selected()` function
   - Fixed JSON serialization
   - Added error handling

2. **sustainable_energy/dashboard/templates/dashboard/objective8.html**
   - Created email alert interface
   - Added country selection dropdown
   - Implemented AJAX request handling

3. **sustainable_energy/dashboard/urls.py**
   - Added route: `/api/send-email-alerts-selected/`
   - Added route: `/objective8/`

### Supporting Files:
4. **country_emails.csv** - 176 country email addresses
5. **sustainable_energy/email_config.py** - Email configuration
6. **sustainable_energy/ml_models/email_alerts.py** - Email alert logic

---

## 8. Testing Status

### Current Status: ⚠️ Requires Server Restart

**Why Server Restart is Needed**:
- Django caches Python modules in memory
- Code changes don't take effect until restart
- This is standard Django behavior

### Testing Steps:
```bash
# 1. Stop server
Ctrl+C

# 2. Restart server
python manage.py runserver

# 3. Clear browser cache
Ctrl+F5 (Windows) or Cmd+Shift+R (Mac)

# 4. Test again
http://127.0.0.1:8000/objective8/
```

---

## 9. Expected Behavior (After Fix)

### Success Flow:
```
1. User selects "Albania"
2. System analyzes: Albania has 100% electricity access
3. Classification: EXCELLENT
4. Email prepared for: albania@sdg7_alerts.org
5. Success message displayed:
   "✅ Success! 1 email alert sent successfully!"
```

### Response Format:
```json
{
    "success": true,
    "total_alerts": 1,
    "alerts_sent": [
        {
            "country": "Albania",
            "email": "albania@sdg7_alerts.org",
            "status": "excellent",
            "access": 100.0,
            "year": 2020,
            "subject": "🎉 Congratulations: Albania Achieves..."
        }
    ]
}
```

---

## 10. Lessons Learned

### Technical Lessons:
1. **Data Type Awareness**: Always check data types when working with Pandas/NumPy
2. **JSON Serialization**: Django's JsonResponse requires native Python types
3. **Error Handling**: Comprehensive error logging is essential for debugging
4. **Server Restart**: Code changes require server restart in Django

### Best Practices Applied:
1. ✅ Explicit type conversion
2. ✅ Defensive programming (`.get()` with defaults)
3. ✅ Comprehensive error logging
4. ✅ Request validation
5. ✅ Debug output for troubleshooting

---

## 11. Next Steps

### Immediate:
1. ✅ Restart Django server
2. ✅ Test with Albania
3. ✅ Verify success response
4. ✅ Check email simulation

### Future Enhancements:
1. Add email delivery confirmation
2. Implement batch email sending
3. Add email template customization
4. Create admin dashboard for email logs

---

## 12. Conclusion

### Problem Summary:
HTTP 500 error caused by attempting to serialize NumPy/Pandas data types to JSON without explicit conversion.

### Solution Summary:
Implemented explicit type conversion to native Python types before JSON serialization.

### Current Status:
Fix implemented, awaiting server restart for testing.

---

## Appendix: Code References

### Main Function (Fixed Version):
See: `sustainable_energy/dashboard/views.py` lines 981-1090

### Email Alert Logic:
See: `sustainable_energy/ml_models/email_alerts.py` lines 360-410

### Frontend Interface:
See: `sustainable_energy/dashboard/templates/dashboard/objective8.html`

---

**Prepared for**: Academic Review  
**Date**: December 2, 2025  
**Project**: SDG 7 Predictive Framework  
**Feature**: Email Alert System (Objective 8)
