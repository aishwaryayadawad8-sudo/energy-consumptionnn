# SDG 7 Dashboard - Complete Project Guide

## Project Title
**"Towards Affordable and Clean Energy: A Predictive and Strategic Framework for SDG 7"**

## Overview
This Django-based dashboard provides comprehensive analysis and prediction of global sustainable energy data, aligned with UN Sustainable Development Goal 7 (Affordable and Clean Energy).

## Key Features Implemented

### 1. Interactive World Map
- Global visualization of electricity access
- Color-coded markers:
  - 🟢 Green: Good access (≥80%)
  - 🟡 Yellow: Warning (50-80%)
  - 🔴 Red: Critical (<50%)
- Click on any country marker to see quick stats

### 2. Smart Country Search
- Autocomplete search bar with all available countries
- Real-time search functionality
- Press Enter or click Search button

### 3. Complete Energy Profile Display
When you search for a country, the system displays:

#### A. Status Alert Box
- **GOOD**: Electricity access ≥80% and good renewable adoption
- **WARNING**: Electricity access 50-80% or moderate renewable share
- **CRITICAL**: Electricity access <50% or very low renewable share

#### B. Key Metrics Cards (4 Cards)
1. **Electricity Access** - % of population with electricity
2. **Clean Cooking Access** - % with access to clean cooking fuels
3. **Renewable Share** - % of renewable energy in total consumption
4. **CO₂ Emissions** - Carbon emissions in kilotons

#### C. Historical Trend Charts (4 Charts)
1. **Electricity Access Trend** - Line chart showing historical progress
2. **Renewable Energy Trend** - Growth of renewable energy adoption
3. **CO₂ Emissions Trend** - Bar chart of carbon emissions over time
4. **Energy Mix** - Pie chart showing Fossil/Renewable/Nuclear distribution

#### D. ML-Based Future Predictions
- Predicts electricity access for next 5 years
- Uses best-performing model (typically CatBoost or LightGBM)
- Shows model name used for prediction

### 4. Country Not Found Handling
If a country is not in the dataset or has no data:
- Clear warning icon displayed
- Message: "Country Not Found" or "Data Unavailable for the Selected Country"
- No empty graphs or blank sections shown
- User immediately understands the issue

### 5. Machine Learning Models
The system trains and compares 7 ML models:
1. Linear Regression
2. Decision Tree
3. K-Nearest Neighbors (KNN)
4. Random Forest
5. XGBoost
6. LightGBM
7. CatBoost

**Best Model Selection**: Automatically selects the model with highest R² score

## How to Use the Dashboard

### Step 1: Start the Server
```bash
cd sustainable_energy
python manage.py runserver
```

### Step 2: Open Browser
Navigate to: `http://127.0.0.1:8000/`

### Step 3: Explore the Dashboard

#### Option A: Use the World Map
- View the global map showing all countries
- Click on markers to see quick information
- Colors indicate electricity access levels

#### Option B: Search for a Country
1. Type country name in the search bar (e.g., "India", "Germany", "Kenya")
2. Autocomplete will suggest available countries
3. Press Enter or click "Search" button

### Step 4: Analyze Results

#### If Country is Found:
You'll see:
1. **Status Alert** at the top showing overall condition
2. **4 Metric Cards** with current values
3. **4 Historical Charts** showing trends
4. **Future Predictions Chart** with ML forecasts

#### If Country is Not Found:
You'll see:
- ⚠️ Warning icon
- Clear message: "Country Not Found"
- Explanation that data is unavailable

## Project Objectives (Displayed on Dashboard)

1. **Forecast Energy Consumption**: Predict future electricity usage patterns
2. **Predict Carbon Emissions**: Analyze CO₂ emissions trends
3. **Evaluate Renewable Potential**: Assess renewable energy adoption
4. **Classify Electricity Access**: Monitor global energy accessibility

## Technical Architecture

### Backend (Django)
- **Views**: Handle API requests and render templates
- **ML Module**: Train models and generate predictions
- **Data Processing**: Pandas for CSV data manipulation

### Frontend
- **Bootstrap 5**: Responsive UI framework
- **Chart.js**: Interactive charts and graphs
- **Leaflet.js**: Interactive world map
- **Font Awesome**: Icons

### Machine Learning
- **scikit-learn**: Base ML algorithms
- **XGBoost**: Gradient boosting
- **LightGBM**: Fast gradient boosting
- **CatBoost**: Categorical boosting (often best performer)

## API Endpoints

### 1. Search Country
```
GET /api/search/?country=<country_name>
```
Returns complete energy profile for the country

### 2. Get Predictions
```
GET /api/predict/?country=<country_name>&years=5
```
Returns ML-based future predictions

### 3. Get All Countries
```
GET /api/countries/
```
Returns list of all available countries

### 4. Get Map Data
```
GET /api/map-data/
```
Returns data for world map visualization

## Status Determination Logic

### Critical Status
- Electricity access < 50%, OR
- Renewable energy share < 10%

### Warning Status
- Electricity access 50-80%, OR
- Renewable energy share 10-25%, OR
- High CO₂ emissions (>100,000 kt)

### Good Status
- Electricity access ≥ 80%, AND
- Renewable energy share ≥ 25%, AND
- Moderate CO₂ emissions

## Dataset Information

**File**: `global-data-on-sustainable-energy.csv`

**Key Columns**:
- Entity (Country name)
- Year
- Access to electricity (% of population)
- Access to clean fuels for cooking
- Renewable energy share in total final energy consumption (%)
- Value_co2_emissions_kt_by_country
- Electricity from fossil fuels (TWh)
- Electricity from renewables (TWh)
- Electricity from nuclear (TWh)
- Primary energy consumption per capita (kWh/person)
- gdp_per_capita
- Latitude, Longitude

## Troubleshooting

### Issue: Country not found but you know it exists
**Solution**: Check spelling. Try variations (e.g., "United States" vs "USA")

### Issue: No predictions shown
**Solution**: Country may have insufficient historical data for ML training

### Issue: Charts not loading
**Solution**: Refresh the page. Check browser console for errors.

### Issue: Server won't start
**Solution**: 
1. Ensure all packages are installed: `pip install -r requirements.txt`
2. Run migrations: `python manage.py migrate`
3. Check if port 8000 is available

## Future Enhancements (Optional)

1. Add more ML models (Neural Networks, LSTM for time series)
2. Export reports as PDF
3. Compare multiple countries side-by-side
4. Add user authentication for saving favorites
5. Real-time data updates from external APIs
6. Mobile app version

## Credits

- **Dataset**: Global Data on Sustainable Energy
- **UN SDG 7**: Affordable and Clean Energy
- **ML Libraries**: scikit-learn, XGBoost, LightGBM, CatBoost
- **Visualization**: Chart.js, Leaflet.js

## Support

For issues or questions:
1. Check this guide
2. Review the README.md
3. Check Django logs in terminal
4. Verify dataset is in correct location

---

**Server is running at**: http://127.0.0.1:8000/

**Enjoy exploring sustainable energy data! 🌍⚡🌱**
