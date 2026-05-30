# Objective 4: SDG 7 Electricity Access Classification - Implementation Guide

## Overview
Objective 4 implements electricity access classification using machine learning to categorize countries into Low, Medium, and High access levels, and predict future trends.

## Features Implemented

### 1. **Classification Models**
- Logistic Regression
- Decision Tree Classifier
- K-Nearest Neighbors (KNN)
- XGBoost Classifier

### 2. **Access Level Categories**
- **Low Access**: 0-50% electricity access
- **Medium Access**: 50-90% electricity access
- **High Access**: 90-100% electricity access

### 3. **Visualizations**
- Model comparison (MSE scores)
- Historical electricity access trends
- Combined historical + future predictions
- Policy intervention markers for key countries

### 4. **Policy Tracking**
Tracks policy interventions for:
- India (2010)
- Bangladesh (2008)
- Kenya (2013)
- Nigeria (2015)
- Brazil (2003)

## File Structure

```
sustainable_energy/
├── ml_models/
│   └── sdg7_access_classifier.py    # Main classification model
├── dashboard/
│   ├── views.py                      # API endpoints
│   ├── urls.py                       # URL routing
│   └── templates/dashboard/
│       ├── objective4.html           # Dashboard UI
│       └── objective_selector.html   # Main selector
```

## API Endpoints

### 1. Model Comparison
```
GET /api/objective4/model-comparison/
```
Returns MSE scores for all models and identifies the best performer.

### 2. Historical Data
```
GET /api/objective4/historical/?country=India
```
Returns historical electricity access data with classifications.

### 3. Future Predictions
```
GET /api/objective4/predictions/?country=India&years=10
```
Returns predicted access levels for the next N years.

### 4. Combined Data
```
GET /api/objective4/combined/?country=India
```
Returns both historical and predicted data in a unified format.

### 5. Policy Markers
```
GET /api/objective4/policy-markers/?country=India
```
Returns policy intervention data for specific countries.

### 6. Countries List
```
GET /api/objective4/countries/
```
Returns all available countries in the dataset.

### 7. Access Distribution
```
GET /api/objective4/distribution/?country=India
```
Returns distribution of access levels over time.

## How to Use

### 1. Start the Server
```bash
cd sustainable_energy
python manage.py runserver
```

### 2. Access the Dashboard
Navigate to: `http://localhost:8000/`

### 3. Select Objective 4
Click on "Objective 3: Access Classification" card

### 4. Explore Features
- Load model comparison to see which algorithm performs best
- Select a country from the dropdown
- View historical trends
- See future predictions
- Check policy impact markers (for applicable countries)

## Model Performance

Based on test results:
- **Best Model**: XGBoost (MSE: 0.0606)
- **Second Best**: Decision Tree (MSE: 0.0682)
- **Third**: KNN (MSE: 0.5909)
- **Fourth**: Logistic Regression (MSE: 0.8674)

## Data Processing

### Input Features
- Year
- Country Code (encoded)

### Target Variable
- Access Level (Low/Medium/High) encoded as 0/1/2

### Data Cleaning
1. Filters records with electricity access data
2. Categorizes access into three levels
3. Encodes categorical variables
4. Handles missing values

## Example Usage

### Python API
```python
from ml_models.sdg7_access_classifier import SDG7AccessClassifier

# Initialize
classifier = SDG7AccessClassifier('path/to/data.csv')
classifier.load_and_clean_data()

# Train models
mse_scores = classifier.train_and_compare_models()

# Get predictions
predictions = classifier.predict_future_access(10, 'India')

# Get policy markers
markers = classifier.get_policy_impact_data('India')
```

### JavaScript (Frontend)
```javascript
// Load model comparison
fetch('/api/objective4/model-comparison/')
    .then(response => response.json())
    .then(data => {
        console.log('Best model:', data.best_model);
        console.log('MSE scores:', data.mse_scores);
    });

// Get predictions
fetch('/api/objective4/predictions/?country=India&years=10')
    .then(response => response.json())
    .then(data => {
        console.log('Predictions:', data.predictions);
    });
```

## Testing

Run the test script:
```bash
python test_objective4_complete.py
```

Expected output:
- ✓ 2639 records loaded
- ✓ 127 countries available
- ✓ 4 models trained and compared
- ✓ Historical data retrieved
- ✓ Future predictions generated
- ✓ Policy markers identified

## Key Differences from Original Code

### Improvements Made:
1. **Django Integration**: Converted standalone script to Django app
2. **API Endpoints**: Created RESTful APIs for all features
3. **Interactive UI**: Built responsive web dashboard
4. **Country Selection**: Added dropdown for easy country selection
5. **Error Handling**: Robust error handling and validation
6. **Data Caching**: Efficient data loading and processing

### Maintained Features:
- All 4 classification models
- Access level categorization (Low/Medium/High)
- Policy intervention tracking
- Future predictions
- Combined historical + future visualization

## Troubleshooting

### Issue: Models not training
**Solution**: Ensure CSV file path is correct and data is loaded

### Issue: Country not found
**Solution**: Check country name spelling (case-sensitive)

### Issue: No predictions returned
**Solution**: Ensure country has sufficient historical data

### Issue: Charts not displaying
**Solution**: Check browser console for JavaScript errors

## Next Steps

1. Add more policy intervention countries
2. Implement confidence intervals for predictions
3. Add export functionality for results
4. Create comparison view for multiple countries
5. Add trend analysis and insights

## Related Files
- `test_objective4_complete.py` - Comprehensive test suite
- `sustainable_energy/requirements.txt` - Dependencies
- `README.md` - Project overview

## Support
For issues or questions, check the test script output or Django logs.
