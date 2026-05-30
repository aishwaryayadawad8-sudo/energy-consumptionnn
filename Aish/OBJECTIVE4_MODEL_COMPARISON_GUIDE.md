# Objective 4: SDG 7 Monitoring - Model Comparison Guide

## Overview
Objective 4 now includes comprehensive model comparison with **7 ML algorithms** for SDG 7 monitoring. After selecting a country, you'll see:
- Model comparison chart (7 algorithms)
- Historical electricity access data
- Future predictions (next 7 years)

## Features

### 1. Model Comparison (7 Algorithms)
The system compares these algorithms:
- **Linear Regression**
- **Decision Tree**
- **KNN (K-Nearest Neighbors)**
- **XGBoost**
- **LightGBM**
- **CatBoost**
- **Random Forest**

The best model (lowest MSE) is highlighted in **gold** on the chart.

### 2. Historical Data
Shows electricity access trends for the selected country over available years.

### 3. Future Predictions
Predicts electricity access for the next 7 years using the best-performing model.

## How to Use

### Step 1: Start the Server
```bash
cd sustainable_energy
python manage.py runserver
```

### Step 2: Access Objective 4
Open your browser and go to:
```
http://127.0.0.1:8000/objective4/
```

### Step 3: Select a Country
1. Choose a country from the dropdown menu
2. Click "Analyze Country"

### Step 4: View Results
The page will display three sections:
1. **Model Comparison** - Bar chart showing MSE scores for all 7 algorithms
2. **Historical Data** - Line chart of past electricity access
3. **Future Predictions** - Line chart of predicted access (next 7 years)

## API Endpoints

### Get All Countries
```
GET /api/objective4/countries/
```

### Model Comparison
```
GET /api/objective4/model-comparison/
```
Returns MSE scores for all 7 algorithms and identifies the best model.

### Historical Data
```
GET /api/objective4/historical/?country=Albania
```

### Future Predictions
```
GET /api/objective4/predictions/?country=Albania&years=7
```

### Combined Data
```
GET /api/objective4/combined/?country=Albania
```
Returns both historical and predicted data in one response.

## Testing

Run the test script to verify everything works:
```bash
python test_objective4_complete.py
```

This will test:
- ✅ Country list retrieval
- ✅ Model comparison (7 algorithms)
- ✅ Historical data loading
- ✅ Future predictions
- ✅ Combined data endpoint

## Model Performance

The system automatically:
1. Trains all 7 ML models
2. Calculates MSE (Mean Squared Error) for each
3. Selects the best model (lowest MSE)
4. Uses the best model for predictions
5. Highlights the best model in gold on the chart

## Example Output

```
Model Comparison Results:
- Linear Regression: MSE = 0.2276
- Decision Tree: MSE = 0.0251
- KNN: MSE = 0.0662
- XGBoost: MSE = 0.0142
- LightGBM: MSE = 0.0160
- CatBoost: MSE = 0.0096 ⭐ (Best)
- Random Forest: MSE = 0.0120

✅ Best Model: CatBoost
```

## Integration with Your Code

The implementation follows the pattern you provided:
- Uses the same 7 algorithms
- Calculates MSE for regression tasks
- Highlights the best model
- Shows all algorithm comparisons in a bar chart

## Troubleshooting

### Issue: "Cannot connect to server"
**Solution:** Make sure Django server is running:
```bash
cd sustainable_energy
python manage.py runserver
```

### Issue: "Country not found"
**Solution:** Check the country name spelling. Use the dropdown to select from available countries.

### Issue: "Model comparison not loading"
**Solution:** 
1. Check server logs for errors
2. Ensure CSV data file exists
3. Verify all ML libraries are installed (sklearn, xgboost, lightgbm, catboost)

## Next Steps

1. ✅ Objective 4 is ready with 7-algorithm comparison
2. You can now select any country and see:
   - Model comparison
   - Historical data
   - Future predictions
3. The same objective selector remains consistent
4. All data is loaded dynamically after country selection

## Summary

Objective 4 now provides:
- **Comprehensive model comparison** (7 algorithms)
- **Same objective** for both historical and future data
- **Country-specific analysis** after selection
- **Visual charts** for easy interpretation
- **Best model highlighting** in gold

The implementation matches your requirements exactly! 🎯
