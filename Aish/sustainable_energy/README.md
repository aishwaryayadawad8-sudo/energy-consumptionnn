# Towards Affordable and Clean Energy: SDG 7 Dashboard

A comprehensive Django-based dashboard for predicting and analyzing global sustainable energy data aligned with UN Sustainable Development Goal 7.

## 🎯 Three Objectives Available

### Objective 1: Forecast Energy Consumption
- Compare 4 ML models for energy consumption prediction
- View historical energy consumption trends
- Predict future consumption up to 2030

### Objective 2: Predict Carbon Emissions
- Compare 4 ML models for CO₂ emissions prediction
- Analyze historical emissions trends
- Forecast future emissions up to 2030

### Full Dashboard: Electricity Access Analysis
- Interactive world map visualization
- Complete country energy profiles
- Status alerts (Good/Warning/Critical)
- 7 ML models for electricity access predictions

## Features

### Objective 1 & 2:
- **Model Comparison**: Compare 4 ML models with MSE scores
- **Historical Analysis**: View trends from 2000-2020
- **Future Predictions**: Forecast up to 2030
- **Country Selection**: Analyze specific countries

### Full Dashboard:
- **Interactive World Map**: Visualize global electricity access with color-coded markers
- **Country Search**: Search any country and view complete energy profile
- **Real-time Status Alerts**: Get instant alerts on electricity conditions (Good/Warning/Critical)
- **Historical Trends**: View past trends for electricity access, renewable energy, and CO₂ emissions
- **ML-Based Predictions**: Future electricity access predictions using 7 ML models:
  - Linear Regression
  - Decision Tree
  - K-Nearest Neighbors
  - Random Forest
  - XGBoost
  - LightGBM
  - CatBoost (Best performing)

- **Comprehensive Metrics**:
  - Electricity Access (% of population)
  - Clean Cooking Access
  - Renewable Energy Share
  - CO₂ Emissions
  - Energy Mix (Fossil/Renewable/Nuclear)

- **Smart Error Handling**: Clear "Country Not Found" messages when data is unavailable

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Navigate to project directory:
```bash
cd sustainable_energy
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

5. Open your browser and visit:
```
http://127.0.0.1:8000/
```

## Usage

### Select Your Objective:
1. Visit http://127.0.0.1:8000/
2. Choose from three objectives:
   - **Objective 1:** Forecast Energy Consumption
   - **Objective 2:** Predict Carbon Emissions
   - **Full Dashboard:** Electricity Access Analysis

### Objective 1 & 2:
1. Click "Load Model Comparison" to compare ML models
2. Select a country from dropdown
3. Click "Analyze Country"
4. View historical trends and future predictions

### Full Dashboard:
1. **View Global Map**: Interactive world map showing electricity access
2. **Search Country**: Enter country name (autocomplete enabled)
3. **View Profile**: Complete energy profile with metrics and charts
4. **Check Predictions**: ML-based future predictions
5. **Analyze Trends**: Historical trends and forecasts

## Project Structure

```
sustainable_energy/
├── config/                 # Django settings
├── dashboard/             # Main dashboard app
│   ├── templates/        # HTML templates
│   ├── views.py          # View functions
│   └── urls.py           # URL routing
├── ml_models/            # Machine learning module
│   └── predictor.py      # ML prediction engine
├── global-data-on-sustainable-energy.csv  # Dataset
└── manage.py
```

## API Endpoints

- `/api/search/?country=<name>` - Get country energy profile
- `/api/predict/?country=<name>&years=5` - Get ML predictions
- `/api/countries/` - List all available countries
- `/api/map-data/` - Get data for world map

## Technologies Used

- **Backend**: Django 5.2
- **ML Models**: scikit-learn, XGBoost, LightGBM, CatBoost
- **Data Processing**: Pandas, NumPy
- **Frontend**: Bootstrap 5, Chart.js, Leaflet.js
- **Visualization**: Interactive charts and maps

## Status Thresholds

- **Critical**: Electricity access < 50% OR Renewable share < 10%
- **Warning**: Electricity access < 80% OR Renewable share < 25%
- **Good**: Electricity access ≥ 80% AND good renewable adoption

## Author

Project for SDG 7: Affordable and Clean Energy
