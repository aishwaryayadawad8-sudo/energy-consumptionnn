# Objective 1: Forecast Energy Consumption - User Guide

## Overview

Objective 1 adds energy consumption forecasting capabilities to your SDG 7 Dashboard. This feature allows you to:
- Compare 4 different ML models (Linear Regression, Decision Tree, KNN, XGBoost)
- View historical energy consumption trends by country
- Predict future energy consumption up to 2030

## How to Access

1. **Start the server:**
   ```bash
   cd sustainable_energy
   python manage.py runserver
   ```

2. **Open your browser:**
   ```
   http://127.0.0.1:8000/
   ```

3. **You'll see the Objective Selector page with two options:**
   - **Objective 1:** Forecast Energy Consumption (NEW!)
   - **Objective 2:** Electricity Access Analysis (Original Dashboard)

## Features

### 1. Model Comparison
- Click "Load Model Comparison" button
- System trains 4 ML models and compares their MSE (Mean Squared Error) scores
- Lower MSE = Better performance
- Best model is highlighted with a badge
- Bar chart visualizes performance differences

**Models Compared:**
- Linear Regression
- Decision Tree
- K-Nearest Neighbors (KNN)
- XGBoost

### 2. Historical Energy Consumption
- Select a country from the dropdown
- Click "Analyze Country"
- View line chart showing historical energy consumption per capita (kWh/person)
- Data spans from 2000-2020 (depending on country availability)

### 3. Future Predictions
- Automatically generated when you select a country
- Predicts energy consumption for next 10 years (2021-2030)
- Uses Linear Regression for predictions
- Dashed line chart shows predicted values

## API Endpoints

### Model Comparison
```
GET /api/objective1/model-comparison/
```
Returns MSE scores for all models and identifies best model.

### Historical Data
```
GET /api/objective1/historical/?country=<country_name>
```
Returns historical energy consumption data for specified country.

### Future Predictions
```
GET /api/objective1/predictions/?country=<country_name>&years=10
```
Returns predicted energy consumption for next N years.

### Available Countries
```
GET /api/objective1/countries/
```
Returns list of all countries with energy consumption data.

## Technical Details

### Data Source
- Uses same CSV: `global-data-on-sustainable-energy.csv`
- Target variable: "Primary energy consumption per capita (kWh/person)"

### Features Used for Prediction
- Year
- Country Code
- Renewable energy share
- CO₂ emissions
- Electricity from fossil fuels
- Electricity from renewables
- GDP per capita
- And more...

### Data Processing
1. **Cleaning:** Column names normalized, commas removed
2. **Encoding:** Countries encoded as numeric codes
3. **Imputation:** Missing values filled with mean
4. **Scaling:** Features standardized using StandardScaler
5. **Train/Test Split:** 80/20 split for model evaluation

## Usage Examples

### Example 1: Compare Models
1. Go to Objective 1 dashboard
2. Click "Load Model Comparison"
3. Wait for training (takes 10-30 seconds)
4. View MSE scores and best model

### Example 2: Analyze India
1. Select "India" from dropdown
2. Click "Analyze Country"
3. View historical consumption trend (2000-2020)
4. View future predictions (2021-2030)

### Example 3: Compare Countries
1. Analyze "United States"
2. Note the consumption values
3. Select "Afghanistan"
4. Compare the differences in consumption patterns

## Interpretation Guide

### MSE Scores
- **Lower is better**
- Typical range: 0.01 to 1.0
- If XGBoost has lowest MSE, it's the best model for this dataset

### Historical Trends
- **Upward trend:** Increasing energy consumption (economic growth)
- **Flat trend:** Stable consumption
- **Downward trend:** Decreasing consumption (efficiency improvements or economic issues)

### Future Predictions
- **Predictions are estimates** based on historical patterns
- **Assumes trends continue** - doesn't account for major policy changes
- **Use with caution** - real-world events can change outcomes

## Troubleshooting

### Issue: "Country not found"
**Solution:** Check spelling, try full country name (e.g., "United States" not "USA")

### Issue: Model comparison takes too long
**Solution:** Normal for first run. XGBoost training can take 20-30 seconds.

### Issue: No historical data shown
**Solution:** Country may have limited data in dataset. Try another country.

### Issue: Charts not displaying
**Solution:** Refresh page, check browser console (F12) for errors.

## Differences from Original Code

Your original Python code was designed for Jupyter/Colab with Plotly. This Django version:

✅ **Converted to Django web app** - accessible via browser
✅ **Uses Chart.js** instead of Plotly for web compatibility
✅ **Added API endpoints** for data access
✅ **Country-specific filtering** - analyze one country at a time
✅ **Persistent storage** - models can be saved/loaded
✅ **Better error handling** - user-friendly messages

## Next Steps

### Enhancements You Can Add:
1. **Add more models:** Random Forest, LightGBM, CatBoost
2. **Multi-country comparison:** Compare 2-3 countries side-by-side
3. **Export functionality:** Download predictions as CSV/Excel
4. **Model persistence:** Save trained models to disk
5. **Confidence intervals:** Show prediction uncertainty
6. **Feature importance:** Show which features matter most

## File Structure

```
sustainable_energy/
├── ml_models/
│   ├── predictor.py                          # Original (Objective 2)
│   └── energy_consumption_predictor.py       # NEW (Objective 1)
├── dashboard/
│   ├── views.py                              # Updated with Objective 1 views
│   ├── urls.py                               # Updated with Objective 1 routes
│   └── templates/dashboard/
│       ├── index.html                        # Original dashboard
│       ├── objective_selector.html           # NEW - Choose objective
│       └── objective1.html                   # NEW - Objective 1 dashboard
```

## Performance Notes

- **Model training:** 10-30 seconds (one-time per session)
- **Historical data loading:** < 1 second
- **Predictions:** < 1 second
- **Page load:** < 2 seconds

## Credits

Based on your original Python code for energy consumption forecasting, adapted for Django web framework.

---

**Enjoy forecasting energy consumption! 📊⚡**
