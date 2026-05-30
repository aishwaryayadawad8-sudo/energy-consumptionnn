# 🚀 Quick Start Guide - Objective 4

## Start the Dashboard in 3 Steps

### Step 1: Navigate to Project
```bash
cd sustainable_energy
```

### Step 2: Start Server
```bash
python manage.py runserver
```

### Step 3: Open Browser
Navigate to: **http://localhost:8000/**

## Using Objective 4

### 1. Select Objective 4
- Click on **"Objective 3: Access Classification"** card
- (This is your Objective 4 implementation)

### 2. Load Model Comparison
- Click **"Load Model Comparison"** button
- Wait 3-5 seconds for models to train
- View MSE scores for all 4 models
- Best model will be highlighted

### 3. Analyze a Country
- Select a country from dropdown (e.g., **India**)
- Click **"Analyze Country"** button
- View 3 charts:
  - Historical electricity access
  - Combined historical + future predictions
  - Policy interventions (if applicable)

## Quick Test

Run the test script to verify everything works:
```bash
python test_objective4_complete.py
```

Expected: All tests pass with ✓ marks

## Sample Countries to Try

### Countries with Policy Markers
- 🇮🇳 **India** - Policy in 2010
- 🇧🇩 **Bangladesh** - Policy in 2008
- 🇰🇪 **Kenya** - Policy in 2013
- 🇳🇬 **Nigeria** - Policy in 2015
- 🇧🇷 **Brazil** - Policy in 2003

### Countries with Interesting Trends
- **United States** - High access throughout
- **China** - Rapid improvement
- **Ethiopia** - Low to medium transition
- **Germany** - Consistently high

## API Quick Reference

### Get All Countries
```bash
curl http://localhost:8000/api/objective4/countries/
```

### Get Model Comparison
```bash
curl http://localhost:8000/api/objective4/model-comparison/
```

### Get Predictions for India
```bash
curl http://localhost:8000/api/objective4/predictions/?country=India&years=10
```

## Troubleshooting

### Server won't start?
```bash
python manage.py check
```

### Charts not showing?
- Press F12 to open browser console
- Check for JavaScript errors
- Try refreshing the page

### Country not found?
- Check spelling (case-sensitive)
- View available countries at `/api/objective4/countries/`

## What You'll See

### Model Comparison Chart
- Bar chart showing MSE scores
- Lower is better
- XGBoost typically wins (MSE ~0.06)

### Historical Chart
- Line chart of electricity access over time
- Shows percentage (0-100%)
- Years on X-axis

### Combined Chart
- Historical data (solid line)
- Future predictions (dashed line)
- Access levels: Low/Medium/High

### Policy Markers
- Shows policy intervention years
- Displays access percentage at intervention
- Only for 5 tracked countries

## Features at a Glance

✅ 4 ML models (Logistic Regression, Decision Tree, KNN, XGBoost)
✅ 3 access levels (Low, Medium, High)
✅ 127 countries available
✅ Predictions up to 2030
✅ Policy tracking for 5 countries
✅ Interactive charts
✅ RESTful API

## Need Help?

- Check `OBJECTIVE4_IMPLEMENTATION.md` for detailed guide
- Check `OBJECTIVE4_COMPLETE.md` for full summary
- Run `python test_objective4_complete.py` to verify setup

---

**Ready to go!** Start the server and explore Objective 4! 🎉
