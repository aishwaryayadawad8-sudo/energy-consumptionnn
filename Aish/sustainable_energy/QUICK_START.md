# Quick Start Guide - SDG 7 Dashboard

## 🚀 Start the Server

### Windows:
```bash
cd sustainable_energy
python manage.py runserver
```

### Or use the batch file:
```bash
start.bat
```

## 🌐 Access Dashboard
Open browser: **http://127.0.0.1:8000/**

## 🔍 How to Use

### 1. View World Map
- See global electricity access visualization
- Green = Good, Yellow = Warning, Red = Critical

### 2. Search Country
- Type country name in search bar
- Example: "India", "Germany", "Kenya"
- Press Enter or click Search

### 3. View Results
✅ **If Found**: See complete energy profile with:
- Status alert (Good/Warning/Critical)
- 4 key metrics
- 4 historical charts
- ML predictions for next 5 years

❌ **If Not Found**: Clear message displayed
- "Country Not Found"
- "Data Unavailable"

## 📊 What You'll See

### Metrics Displayed:
1. **Electricity Access** (% of population)
2. **Clean Cooking Access** (%)
3. **Renewable Energy Share** (%)
4. **CO₂ Emissions** (kt)

### Charts Displayed:
1. Electricity Access Trend
2. Renewable Energy Trend
3. CO₂ Emissions Trend
4. Energy Mix (Fossil/Renewable/Nuclear)
5. Future Predictions (ML-based)

## ⚠️ Status Meanings

- 🟢 **GOOD**: Electricity ≥80%, Good renewables
- 🟡 **WARNING**: Electricity 50-80%, Moderate renewables
- 🔴 **CRITICAL**: Electricity <50%, Low renewables

## 🛠️ Troubleshooting

**Server won't start?**
```bash
pip install -r requirements.txt
python manage.py migrate
```

**Country not found?**
- Check spelling
- Try full name (e.g., "United States" not "USA")

## 📁 Project Structure
```
sustainable_energy/
├── dashboard/          # Main app
├── ml_models/         # ML prediction engine
├── config/            # Django settings
├── global-data-on-sustainable-energy.csv
└── manage.py
```

## 🎯 Project Objectives
1. Forecast energy consumption
2. Predict carbon emissions
3. Evaluate renewable potential
4. Classify electricity access

## 🤖 ML Models Used
- Linear Regression
- Decision Tree
- K-Nearest Neighbors
- Random Forest
- XGBoost
- LightGBM
- CatBoost (usually best)

---

**That's it! Start exploring sustainable energy data! 🌍⚡**
