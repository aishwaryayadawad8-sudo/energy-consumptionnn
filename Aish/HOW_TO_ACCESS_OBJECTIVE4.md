# 🎯 How to Access Objective 4

## Quick Start (3 Steps)

### Step 1: Start the Server
```bash
cd sustainable_energy
python manage.py runserver
```

Wait for:
```
Starting development server at http://127.0.0.1:8000/
```

### Step 2: Open Your Browser
Navigate to: **http://localhost:8000/**

### Step 3: Click the Correct Card
Click on: **"Objective 4: SDG 7 Access Classification"**

---

## Visual Guide

```
Browser: http://localhost:8000/
    ↓
┌─────────────────────────────────────────────────────────┐
│  SDG 7: Affordable and Clean Energy                     │
│  Select an objective to explore                         │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐│
│  │Objective │  │Objective │  │Objective │  │Objective ││
│  │    1     │  │    2     │  │    3     │  │    4     ││
│  │  Energy  │  │   CO₂    │  │   CO₂    │  │   SDG 7  ││
│  │Consumption│  │Emissions │  │Emissions │  │  Access  ││  ← CLICK THIS!
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘│
│                                                          │
└─────────────────────────────────────────────────────────┘
    ↓
    ↓ Click "Objective 4: SDG 7 Access Classification"
    ↓
┌─────────────────────────────────────────────────────────┐
│  Objective 4: SDG 7 Electricity Access Classification   │
│  ← Back to Objectives                                   │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  📊 Model Comparison (MSE Scores)                       │
│  [Load Model Comparison] ← Click to train models        │
│                                                          │
│  🌍 Select Country for Analysis                         │
│  [Dropdown: Select a Country ▼] [Analyze Country]       │
│                                                          │
│  📈 Historical Electricity Access (hidden until loaded) │
│  📊 Combined Historical + Future (hidden until loaded)  │
│  🏛️ Policy Interventions (hidden until loaded)          │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## What to Do on the Page

### 1. Load Model Comparison (Optional but Recommended)
- Click: **"Load Model Comparison"** button
- Wait: 3-5 seconds (training 4 models)
- See: Bar chart with MSE scores
- Result: Best model identified (usually XGBoost)

### 2. Select a Country
- Click: Dropdown menu
- Choose: Any country (e.g., "India", "Brazil", "Kenya")
- Click: **"Analyze Country"** button

### 3. View Results
Three charts will appear:
1. **Historical Trends**: Line chart showing electricity access over time
2. **Combined View**: Historical + future predictions (2021-2030)
3. **Policy Markers**: Shows policy interventions (for 5 countries)

---

## Sample Countries to Try

### Countries with Policy Markers (Most Interesting!)
- 🇮🇳 **India** - Policy in 2010, shows improvement
- 🇧🇩 **Bangladesh** - Policy in 2008, rapid growth
- 🇰🇪 **Kenya** - Policy in 2013, low to medium transition
- 🇳🇬 **Nigeria** - Policy in 2015, medium access
- 🇧🇷 **Brazil** - Policy in 2003, high access

### Other Interesting Countries
- **United States** - Consistently high access
- **China** - Rapid improvement over time
- **Ethiopia** - Low to medium transition
- **Germany** - Stable high access

---

## Expected Results

### Model Comparison Chart
```
MSE Scores (Lower is Better)
┌─────────────────────────────────┐
│ XGBoost          ████ 0.0606    │ ← Best!
│ Decision Tree    ████ 0.0682    │
│ KNN              ████████ 0.59  │
│ Logistic Reg     ██████████ 0.87│
└─────────────────────────────────┘
```

### Historical Chart (Example: India)
```
Electricity Access (%)
100% ┤                        ●●●●
 90% ┤                   ●●●●
 80% ┤              ●●●●
 70% ┤         ●●●●
 60% ┤    ●●●●
     └────────────────────────────
     2000  2005  2010  2015  2020
```

### Combined Chart (Historical + Future)
```
Access Level
High    ┤        ────────●●●●●●●● (Predicted)
        ┤    ●●●●
Medium  ┤ ●●●
Low     ┤●
        └────────────────────────────────
        2000  2010  2020  2030
        ←Historical→ ←Future→
```

---

## Troubleshooting

### ❌ Problem: Page is blank
**Solution**: 
- Make sure you clicked **"Objective 4: SDG 7 Access Classification"**
- NOT "Objective 5: Policy Impact Tracking"
- Clear browser cache and refresh

### ❌ Problem: Dropdown is empty
**Solution**:
- Open browser console (F12)
- Look for error messages
- Check server is running
- Test API: `curl http://localhost:8000/api/objective4/countries/`

### ❌ Problem: Charts don't appear
**Solution**:
- Charts don't auto-load, you must click buttons!
- Click "Load Model Comparison" for first chart
- Select country and click "Analyze Country" for other charts

### ❌ Problem: "Loading..." never finishes
**Solution**:
- Check browser console for errors
- Check server terminal for errors
- Model training takes 3-5 seconds (be patient)
- Try refreshing the page

---

## Browser Console (F12)

### What You Should See:
```
Page loaded, initializing Objective 4...
Loading countries...
Countries response received: 200
Countries data: {success: true, countries: Array(127)}
✓ Loaded 127 countries
```

### After Clicking "Load Model Comparison":
```
Loading model comparison...
Model comparison response: 200
Model comparison data: {success: true, mse_scores: {...}, best_model: "XGBoost"}
Creating MSE chart with models: ["Logistic Regression", "Decision Tree", "KNN", "XGBoost"]
```

### If You See Errors:
- Red text = JavaScript error
- Check the error message
- Common issues:
  - Network error = Server not running
  - 404 error = Wrong URL
  - 500 error = Server-side error

---

## Server Terminal

### What You Should See:
```
[30/Nov/2025 15:46:30] "GET / HTTP/1.1" 200 9332
[30/Nov/2025 15:46:35] "GET /objective4/ HTTP/1.1" 200 26769
[30/Nov/2025 15:46:40] "GET /api/objective4/countries/ HTTP/1.1" 200 1539
[30/Nov/2025 15:46:50] "GET /api/objective4/model-comparison/ HTTP/1.1" 200 156
```

### Status Codes:
- **200** = Success ✅
- **404** = Not Found ❌
- **500** = Server Error ❌

---

## Complete Workflow

```
1. Start Server
   cd sustainable_energy
   python manage.py runserver
   ↓
2. Open Browser
   http://localhost:8000/
   ↓
3. Click Objective 4 Card
   "Objective 4: SDG 7 Access Classification"
   ↓
4. Load Model Comparison (Optional)
   Click "Load Model Comparison"
   Wait 3-5 seconds
   See bar chart
   ↓
5. Select Country
   Choose from dropdown (e.g., "India")
   ↓
6. Analyze Country
   Click "Analyze Country"
   ↓
7. View Results
   - Historical trends chart
   - Combined historical + future chart
   - Policy markers (if applicable)
   ↓
8. Try Different Countries
   Repeat steps 5-7 with different countries
```

---

## Quick Test

Run this to verify everything works:
```bash
# Terminal 1: Start server
cd sustainable_energy
python manage.py runserver

# Terminal 2: Test API
curl http://localhost:8000/api/objective4/countries/
```

Expected output:
```json
{
  "success": true,
  "countries": ["Afghanistan", "Albania", ...]
}
```

---

## Summary

✅ **Correct URL**: `http://localhost:8000/objective4/`
✅ **Correct Card**: "Objective 4: SDG 7 Access Classification"
✅ **Page Size**: ~27KB (not blank!)
✅ **Features**: Model comparison, historical trends, future predictions, policy markers
✅ **Countries**: 127 available
✅ **Models**: 4 classification algorithms

**Everything is working!** Just make sure you click the right card! 🎉

---

**Last Updated**: November 30, 2025
**Status**: ✅ WORKING
