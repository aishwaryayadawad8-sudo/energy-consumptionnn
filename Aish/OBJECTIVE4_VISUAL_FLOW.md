# Objective 4: Visual Flow Diagram

## User Journey

```
┌─────────────────────────────────────────────────────────────┐
│                    START: Open Browser                       │
│              http://127.0.0.1:8000/objective4/              │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                  STEP 1: Page Loads                          │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  🌍 Select Country for Analysis                       │  │
│  │  ┌─────────────────────────────────────────────┐     │  │
│  │  │  [Dropdown: -- Select a Country --]  ▼     │     │  │
│  │  └─────────────────────────────────────────────┘     │  │
│  │  [Analyze Country Button]                            │  │
│  └───────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              STEP 2: Select Country (e.g., Albania)          │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  🌍 Select Country for Analysis                       │  │
│  │  ┌─────────────────────────────────────────────┐     │  │
│  │  │  [Dropdown: Albania]  ▼                     │     │  │
│  │  └─────────────────────────────────────────────┘     │  │
│  │  [Analyze Country Button] ← CLICK HERE               │  │
│  └───────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│           STEP 3: System Loads All Data                      │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  API Call 1: /api/objective4/model-comparison/     │    │
│  │  → Trains 7 ML models                              │    │
│  │  → Calculates MSE scores                           │    │
│  │  → Identifies best model                           │    │
│  └─────────────────────────────────────────────────────┘    │
│                         │                                     │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  API Call 2: /api/objective4/historical/           │    │
│  │  → Gets historical electricity access data         │    │
│  └─────────────────────────────────────────────────────┘    │
│                         │                                     │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  API Call 3: /api/objective4/predictions/          │    │
│  │  → Generates 7-year predictions                    │    │
│  │  → Uses best model from comparison                 │    │
│  └─────────────────────────────────────────────────────┘    │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              STEP 4: Display Results                         │
│                                                               │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  🏆 Model Comparison (7 Algorithms)                   │  │
│  │  Lower MSE = Better Model Performance                 │  │
│  │  ⭐ Best Model: CatBoost                              │  │
│  │                                                        │  │
│  │  ┌────────────────────────────────────────────────┐  │  │
│  │  │  Linear Regression  ████████████ 0.2276        │  │  │
│  │  │  Decision Tree      ███ 0.0251                 │  │  │
│  │  │  KNN                ██████ 0.0662              │  │  │
│  │  │  XGBoost            ██ 0.0142                  │  │  │
│  │  │  LightGBM           ██ 0.0160                  │  │  │
│  │  │  CatBoost           █ 0.0096 ⭐ GOLD           │  │  │
│  │  │  Random Forest      ██ 0.0120                  │  │  │
│  │  └────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                               │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  📈 Historical Electricity Access                     │  │
│  │  Electricity access trends for Albania                │  │
│  │                                                        │  │
│  │  ┌────────────────────────────────────────────────┐  │  │
│  │  │  100% ●─────●─────●─────●─────●                │  │  │
│  │  │   90%                                           │  │  │
│  │  │   80%                                           │  │  │
│  │  │   70%                                           │  │  │
│  │  │   60%                                           │  │  │
│  │  │        2000  2005  2010  2015  2020            │  │  │
│  │  └────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                               │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  🔮 Future Predictions (Next 7 Years)                 │  │
│  │  Predicted electricity access for Albania             │  │
│  │                                                        │  │
│  │  ┌────────────────────────────────────────────────┐  │  │
│  │  │  100% ●┄┄┄●┄┄┄●┄┄┄●┄┄┄●┄┄┄●┄┄┄●                 │  │  │
│  │  │   90%                                           │  │  │
│  │  │   80%                                           │  │  │
│  │  │   70%                                           │  │  │
│  │  │   60%                                           │  │  │
│  │  │        2024 2025 2026 2027 2028 2029 2030      │  │  │
│  │  └────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                        Frontend (HTML/JS)                     │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  objective4.html                                       │  │
│  │  - Country dropdown                                    │  │
│  │  - Chart.js visualizations                            │  │
│  │  - AJAX API calls                                      │  │
│  └────────────────────────────────────────────────────────┘  │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         │ HTTP Requests
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│                    Django Backend (views.py)                  │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  objective4_dashboard()                                │  │
│  │  objective4_model_comparison()                         │  │
│  │  objective4_historical_data()                          │  │
│  │  objective4_future_predictions()                       │  │
│  │  objective4_countries()                                │  │
│  └────────────────────────────────────────────────────────┘  │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         │ Data Processing
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│                ML Models (sdg7_forecasting.py)                │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  SDG7Forecasting Class                                 │  │
│  │  ├─ load_and_clean_data()                             │  │
│  │  ├─ train_and_compare_models()                        │  │
│  │  │   ├─ Linear Regression                             │  │
│  │  │   ├─ Decision Tree                                 │  │
│  │  │   ├─ KNN                                           │  │
│  │  │   ├─ XGBoost                                       │  │
│  │  │   ├─ LightGBM                                      │  │
│  │  │   ├─ CatBoost                                      │  │
│  │  │   └─ Random Forest                                 │  │
│  │  ├─ get_historical_data()                             │  │
│  │  └─ predict_future_access()                           │  │
│  └────────────────────────────────────────────────────────┘  │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         │ Data Source
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│                    CSV Data File                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  global-data-on-sustainable-energy.csv                 │  │
│  │  - 176 countries                                       │  │
│  │  - Years: 2000-2020                                    │  │
│  │  - Electricity access data                             │  │
│  │  - Renewable energy data                               │  │
│  │  - CO2 emissions data                                  │  │
│  └────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

## Model Comparison Process

```
┌─────────────────────────────────────────────────────────────┐
│              Model Training & Comparison Flow                │
└─────────────────────────────────────────────────────────────┘

1. Load Data
   ↓
   [CSV File] → [Clean & Prepare] → [Feature Engineering]
   
2. Train Models (Parallel)
   ↓
   ┌─────────────────────────────────────────────────────────┐
   │  Model 1: Linear Regression    → MSE: 0.2276           │
   │  Model 2: Decision Tree        → MSE: 0.0251           │
   │  Model 3: KNN                  → MSE: 0.0662           │
   │  Model 4: XGBoost              → MSE: 0.0142           │
   │  Model 5: LightGBM             → MSE: 0.0160           │
   │  Model 6: CatBoost             → MSE: 0.0096 ⭐        │
   │  Model 7: Random Forest        → MSE: 0.0120           │
   └─────────────────────────────────────────────────────────┘
   
3. Compare & Select Best
   ↓
   [Find Minimum MSE] → [CatBoost = 0.0096] → [Best Model! 🏆]
   
4. Use Best Model for Predictions
   ↓
   [CatBoost] → [Predict 2024-2030] → [Return Results]
```

## Color Coding

```
🟡 GOLD (#FFD700)     → Best performing model
🔵 BLUE (#667eea)     → Other models
🟣 PURPLE (#764ba2)   → Background gradient
🟢 GREEN (#27ae60)    → Future predictions
```

## Chart Types

```
1. Model Comparison
   Type: Bar Chart (Horizontal)
   X-axis: MSE Score
   Y-axis: Model Names
   Highlight: Gold for best model

2. Historical Data
   Type: Line Chart
   X-axis: Years (2000-2020)
   Y-axis: Electricity Access (%)
   Style: Solid line, filled area

3. Future Predictions
   Type: Line Chart
   X-axis: Years (2024-2030)
   Y-axis: Electricity Access (%)
   Style: Dashed line, filled area
```

## Summary

✅ **One Objective** - SDG 7 Monitoring
✅ **Three Views** - Model Comparison, Historical, Predictions
✅ **Seven Algorithms** - Comprehensive comparison
✅ **One Dashboard** - Everything in one place
✅ **Dynamic Loading** - Data loads after country selection
✅ **Best Model Highlighting** - Gold color for winner

**The flow is simple, intuitive, and powerful!** 🚀
