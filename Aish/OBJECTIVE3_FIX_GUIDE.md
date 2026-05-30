# 🔧 Objective 4 - Fix Guide

## Problem Identified

The "Objective 4" card on the selector page was linking to `/objective5/` which had a blank template, causing the blank page issue.

## Root Cause

The objective selector had incorrect mappings:
- **Objective 3 card** → linked to `/objective4/` ✅ (Your new implementation)
- **Objective 4 card** → linked to `/objective5/` ❌ (Blank page)

## Solution Applied

### 1. Fixed Objective Selector Mappings

**Before:**
```html
<!-- Objective 3 -->
<div onclick="window.location.href='/objective4/'">
    <div class="objective-title">Objective 3: Access Classification</div>
</div>

<!-- Objective 4 -->
<div onclick="window.location.href='/objective5/'">
    <div class="objective-title">Objective 4: Policy Impact</div>
</div>
```

**After:**
```html
<!-- Objective 3 -->
<div onclick="window.location.href='/objective3/'">
    <div class="objective-title">Objective 3: CO₂ Emissions</div>
</div>

<!-- Objective 4 -->
<div onclick="window.location.href='/objective4/'">
    <div class="objective-title">Objective 4: SDG 7 Access Classification</div>
</div>

<!-- Objective 5 -->
<div onclick="window.location.href='/objective5/'">
    <div class="objective-title">Objective 5: Policy Impact Tracking</div>
</div>
```

### 2. Added Console Logging

Added debug logging to help troubleshoot future issues:
```javascript
console.log('Page loaded, initializing Objective 4...');
console.log('Loading countries...');
console.log('✓ Loaded ${data.countries.length} countries');
```

## How to Access Objective 4 Now

### Method 1: From Selector (Recommended)
1. Start server: `cd sustainable_energy && python manage.py runserver`
2. Open browser: `http://localhost:8000/`
3. Click: **"Objective 4: SDG 7 Access Classification"** card
4. Page will load with all features

### Method 2: Direct URL
1. Start server
2. Navigate directly to: `http://localhost:8000/objective4/`

## What You Should See

### On Page Load:
1. ✅ Header with "Objective 4: SDG 7 Electricity Access Classification"
2. ✅ Model Comparison section with "Load Model Comparison" button
3. ✅ Country Selection dropdown (populated with 127 countries)
4. ✅ Hidden sections for Historical, Combined, and Policy charts

### After Clicking "Load Model Comparison":
1. ✅ Loading spinner (3-5 seconds)
2. ✅ Best model badge (e.g., "Best Model: XGBoost")
3. ✅ Bar chart showing MSE scores for 4 models

### After Selecting Country and Clicking "Analyze Country":
1. ✅ Historical electricity access line chart
2. ✅ Combined historical + future predictions chart
3. ✅ Policy intervention markers (for India, Bangladesh, Kenya, Nigeria, Brazil)

## Verification Steps

### 1. Check Server is Running
```bash
cd sustainable_energy
python manage.py runserver
```

Expected output:
```
Starting development server at http://127.0.0.1:8000/
```

### 2. Test API Endpoints
```bash
# Test countries endpoint
curl http://localhost:8000/api/objective4/countries/

# Expected: {"success": true, "countries": ["Afghanistan", ...]}
```

### 3. Check Browser Console
1. Open browser to `http://localhost:8000/objective4/`
2. Press F12 to open Developer Tools
3. Go to Console tab
4. You should see:
   ```
   Page loaded, initializing Objective 4...
   Loading countries...
   Countries response received: 200
   ✓ Loaded 127 countries
   ```

### 4. Test Model Comparison
1. Click "Load Model Comparison" button
2. Wait 3-5 seconds
3. Console should show:
   ```
   Loading model comparison...
   Model comparison response: 200
   Creating MSE chart with models: [...]
   ```
4. Chart should appear with 4 bars

### 5. Test Country Analysis
1. Select "India" from dropdown
2. Click "Analyze Country"
3. Three charts should appear:
   - Historical trends
   - Combined historical + future
   - Policy markers (for India)

## Troubleshooting

### Issue: Still seeing blank page
**Solution**: 
- Clear browser cache (Ctrl+Shift+Delete)
- Hard refresh (Ctrl+F5)
- Check you're clicking the correct card

### Issue: Dropdown not populating
**Solution**:
- Check browser console for errors
- Verify API endpoint: `curl http://localhost:8000/api/objective4/countries/`
- Check server logs for errors

### Issue: Charts not loading
**Solution**:
- Verify Chart.js CDN is accessible
- Check browser console for JavaScript errors
- Ensure buttons are clicked (charts don't auto-load)

### Issue: Model comparison takes too long
**Solution**:
- This is normal! Training 4 models takes 3-5 seconds
- Wait for the loading spinner to disappear
- Check console for progress messages

## Server Logs to Watch For

### Successful Page Load:
```
[30/Nov/2025 15:46:30] "GET /objective4/ HTTP/1.1" 200 26769
```
- Status 200 = Success
- 26769 bytes = Full page content

### Successful API Call:
```
[30/Nov/2025 15:46:35] "GET /api/objective4/countries/ HTTP/1.1" 200 1539
```
- Status 200 = Success
- 1539 bytes = JSON with countries

### Blank Page (Fixed):
```
[30/Nov/2025 15:42:02] "GET /objective5/ HTTP/1.1" 200 0
```
- 0 bytes = Empty page (this was the problem)

## Files Modified

1. ✅ `sustainable_energy/dashboard/templates/dashboard/objective_selector.html`
   - Fixed objective card mappings
   - Added Objective 5 card
   - Corrected URLs

2. ✅ `sustainable_energy/dashboard/templates/dashboard/objective4.html`
   - Added console logging
   - Added error handling
   - Improved user feedback

## Testing Checklist

- [x] Server starts without errors
- [x] Objective selector loads
- [x] Objective 4 card links to `/objective4/`
- [x] Objective 4 page loads (not blank)
- [x] Countries dropdown populates
- [x] Model comparison works
- [x] Country analysis works
- [x] All charts display correctly
- [x] Console logging works
- [x] No JavaScript errors

## Summary

The issue was **NOT** with your Objective 4 implementation - it was working perfectly! The problem was that the selector page had the wrong URL mapping. When you clicked "Objective 4", it was taking you to `/objective5/` which was blank.

**Now fixed!** Click "Objective 4: SDG 7 Access Classification" and everything works! 🎉

---

**Status**: ✅ FIXED
**Date**: November 30, 2025
**Issue**: Blank page on Objective 4
**Cause**: Wrong URL in selector
**Solution**: Fixed selector mappings
