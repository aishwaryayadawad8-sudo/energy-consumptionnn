# Objective 2: Predict Carbon Emissions - User Guide

## Overview

Objective 2 adds CO₂ emissions prediction capabilities to your SDG 7 Dashboard. This feature allows you to:
- Compare 4 different ML models for emissions prediction
- View historical CO₂ emissions trends by country
- Predict future emissions up to 2030

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

3. **Select Objective 2:** Click on "Objective 2: Predict Carbon Emissions"

## Features

### 1. Model Comparison
- Click "Load Model Comparison" button
- System trains 4 ML models and compares their MSE scores
- Lower MSE = Better performance for CO₂ prediction
- Best model is highlighted with a badge
- Bar chart visualizes performance differences

**Models Compared:**
- Linear Regression
- Decision Tree
- K-Nearest Neighbors (KNN)
- XGBoost

### 2. Historical CO₂ Emissions
- Select a country from the dropdown
- Click "Analyze Country"
- View line chart showing historical CO₂ emissions (kilotons)
- Data spans from 2000-2020 (depending on country availability)

### 3. Future Emissions Predictions
- Automatically generated when you select a country
- Predicts CO₂ emissions for next 10 years (2021-2030)
- Uses Linear Regression for predictions
- Dashed line chart shows predicted values

## API Endpoints

### Model Comparison
```
GET /api/objective2/model-comparison/
```
Returns MSE scores for all models and identifies best model.

### Historical Data
```
GET /api/objective2/historical/?country=<country_name>
```
Returns historical CO₂ emissions data for specified country.

### Future Predictions
```
GET /api/objective2/predictions/?country=<country_name>&years=10
```
Returns predicted CO₂ emissions for next N years.

### Available Countries
```
GET /api/objective2/countries/
```
Returns list of all countries with CO₂ emissions data.

## Technical Details

### Data Source
- Uses same CSV: `global-data-on-sustainable-energy.csv`
- Target variable: "Value_co2_emissions_kt_by_country"

### Features Used for Prediction
- Year
- Country Code
- Renewable energy share
- Electricity from fossil fuels
- Electricity from renewables
- GDP per capita
- Energy consumption per capita
- And more...

### Data Processing
1. **Cleaning:** Column names normalized, commas removed
2. **Encoding:** Countries encoded as numeric codes
3. **Imputation:** Missing values filled with mean
4. **Scaling:** Features standardized using StandardScaler
5. **Train/Test Split:** 80/20 split for model evaluation

## Usage Examples

### Example 1: Compare Models
1. Go to Objective 2 dashboard
2. Click "Load Model Comparison"
3. Wait for training (takes 10-30 seconds)
4. View MSE scores and best model

### Example 2: Analyze United States
1. Select "United States" from dropdown
2. Click "Analyze Country"
3. View historical emissions trend (2000-2020)
4. View future predictions (2021-2030)

### Example 3: Compare High vs Low Emitters
1. Analyze "China" (high emitter)
2. Note the emission values
3. Select "Norway" (low emitter)
4. Compare the differences in emission patterns

## Interpretation Guide

### MSE Scores
- **Lower is better**
- Typical range: 0.01 to 10.0 (varies by scale)
- Best model has shortest bar in chart

### Historical Trends
- **Upward trend:** Increasing emissions (industrialization, economic growth)
- **Flat trend:** Stable emissions
- **Downward trend:** Decreasing emissions (clean energy adoption, efficiency)

### Future Predictions
- **Predictions are estimates** based on historical patterns
- **Assumes trends continue** - doesn't account for policy changes
- **Use with caution** - Paris Agreement and climate policies can change outcomes

## Country Examples to Try

### High Emitters:
- **China** - Largest emitter, rapid industrial growth
- **United States** - High emissions, recent decline
- **India** - Growing emissions with development

### Medium Emitters:
- **Germany** - Declining due to renewable energy
- **Japan** - Stable with nuclear/renewables
- **United Kingdom** - Significant reduction achieved

### Low Emitters:
- **Norway** - Hydropower dominance
- **Sweden** - Nuclear and renewables
- **Costa Rica** - Nearly 100% renewable electricity

## Troubleshooting

### Issue: "Country not found"
**Solution:** Check spelling, try full country name

### Issue: Model comparison takes too long
**Solution:** Normal for first run. Training can take 20-30 seconds.

### Issue: No historical data shown
**Solution:** Country may have limited data. Try another country.

### Issue: Charts not displaying
**Solution:** Refresh page, check browser console (F12) for errors.

## Key Insights

### What Affects CO₂ Emissions?
1. **Fossil fuel usage** - Coal, oil, gas power plants
2. **Industrial activity** - Manufacturing, cement production
3. **Transportation** - Cars, trucks, aviation
4. **Economic development** - GDP growth often correlates with emissions
5. **Energy policy** - Renewable energy adoption reduces emissions

### Why This Matters for SDG 7?
- **SDG 7** aims for affordable and clean energy
- **Lower emissions** indicate cleaner energy sources
- **Predictions help** countries plan climate action
- **Model comparison** shows best methods for forecasting

## Differences from Original Code

Your original Python code was designed for Jupyter/Colab with Plotly. This Django version:

✅ **Converted to Django web app** - accessible via browser
✅ **Uses Chart.js** instead of Plotly for web compatibility
✅ **Added API endpoints** for data access
✅ **Country-specific filtering** - analyze one country at a time
✅ **Better error handling** - user-friendly messages
✅ **Red color theme** - visually distinct from Objective 1



### Enhancements You Can Add:
1. **Add more models:** Random Forest, LightGBM, CatBoost
2. **Multi-country comparison:** Compare emissions side-by-side
3. **Export functionality:** Download predictions as CSV/Excel
4. **Emissions per capita:** Normalize by population
5. **Sector breakdown:** Show emissions by sector (energy, transport, industry)
6. **Climate targets:** Compare predictions with Paris Agreement goals

## Performance Notes

- **Model training:** 10-30 seconds (one-time per session)
- **Historical data loading:** < 1 second
- **Predictions:** < 1 second
- **Page load:** < 2 seconds

## Related Objectives

- **Objective 1:** Forecast Energy Consumption
- **Full Dashboard:** Complete electricity access analysis with world map

## Credits

Based on your original Python code for CO₂ emissions prediction, adapted for Django web framework.

---

**Help reduce carbon emissions through data-driven insights! 🌍💨**
