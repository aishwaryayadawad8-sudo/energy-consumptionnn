# Quick Reference Guide

## Start the Server

```bash
cd sustainable_energy
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

## All Objectives

| Objective | URL | Focus | Models |
|-----------|-----|-------|--------|
| **Objective 1** | `/objective1/` | Energy Consumption | 4 |
| **Objective 2** | `/objective3/` | CO₂ Emissions | 4 |
| **Full Dashboard** | `/dashboard/` | Electricity Access | 7 |

## Quick Actions

### Objective 1: Energy Consumption
1. Click "Load Model Comparison"
2. Select country (try "India")
3. Click "Analyze Country"
4. View historical + predictions

### Objective 2: CO₂ Emissions
1. Click "Load Model Comparison"
2. Select country (try "China")
3. Click "Analyze Country"
4. View emissions trends

### Full Dashboard
1. View world map
2. Search country (try "Germany")
3. View energy profile
4. Check status alerts

## Best Models

- **Objective 1:** XGBoost (usually)
- **Objective 2:** XGBoost or Decision Tree
- **Full Dashboard:** CatBoost or LightGBM

## Sample Countries

- **High consumption:** USA, Canada, Norway
- **High emissions:** China, USA, India
- **Low access:** Afghanistan, Chad
- **Renewables:** Iceland, Costa Rica

## API Endpoints

### Objective 1
- `/api/objective1/model-comparison/`
- `/api/objective1/historical/?country=X`
- `/api/objective1/predictions/?country=X&years=10`

### Objective 3
- `/api/objective3/model-comparison/`
- `/api/objective3/historical/?country=X`
- `/api/objective3/predictions/?country=X&years=10`

### Full Dashboard
- `/api/search/?country=X`
- `/api/predict/?country=X&years=5`
- `/api/map-data/`

## Troubleshooting

**Server won't start:**
```bash
pip install -r requirements.txt
python manage.py migrate
```

**Country not found:** Check spelling

**Charts not loading:** Refresh page (F5)

**Slow training:** Normal, wait 10-30 seconds

## Documentation

- `OBJECTIVE1_GUIDE.md` - Objective 1 details
- `OBJECTIVE3_GUIDE.md` - Objective 3 details
- `PROJECT_GUIDE.md` - Full dashboard guide
- `COMPLETE_PROJECT_SUMMARY.md` - Everything

## Key Features

✅ 3 objectives + full dashboard
✅ 11 ML models total
✅ Interactive charts
✅ World map visualization
✅ Historical trends
✅ Future predictions
✅ Country-specific analysis
✅ Model comparison
✅ Status alerts
✅ RESTful APIs

---

**That's it! Start exploring sustainable energy data! 🌍⚡**
