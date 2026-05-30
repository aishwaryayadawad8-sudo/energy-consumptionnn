# Objective 5: Energy Equity Analysis - Behavior Summary

## ✅ Current Implementation

### **Auto-Loading Behavior (Page Load)**
1. **Model Comparison** - Loads automatically after 1 second
   - Shows 4 ML models: Linear Regression, Decision Tree, KNN, XGBoost
   - XGBoost highlighted in gold as best model (lowest MSE)
   - Uses your exact model comparison code
   - No user interaction required

2. **Country Dropdown** - Loads automatically
   - Populates with 127 available countries
   - Sorted alphabetically (Afghanistan, Albania, Algeria, etc.)
   - Shows "-- Select a Country --" as default option

### **User-Triggered Behavior (Country Selection)**
3. **Country Analysis** - Triggered by "Analyze Country" button
   - User selects country from dropdown
   - User clicks "Analyze Country" button
   - Three charts appear:

#### **Chart 1: Historical Data**
- Shows past electricity access trends (2000-2020)
- Blue line chart with filled area
- Real historical data from your dataset

#### **Chart 2: Future Predictions** 
- Shows forecasted electricity access (2021-2030)
- Green dashed line chart with filled area
- Uses Linear Regression model for predictions

#### **Chart 3: Combined Analysis**
- Shows both historical and predicted data
- Two datasets on same chart:
  - Blue solid line: Historical (2000-2020)
  - Green dashed line: Predictions (2021-2030)
- Complete timeline view

### **Hidden by Default**
- All country analysis sections are hidden initially
- Only appear after successful country analysis
- If no data available, sections remain hidden

## 🎯 User Flow

```
1. User visits Objective 5
   ↓
2. Page loads → Model comparison appears automatically (1 sec delay)
   ↓
3. Country dropdown populates automatically
   ↓
4. User selects a country from dropdown
   ↓
5. User clicks "Analyze Country" button
   ↓
6. Three analysis charts appear:
   - Historical electricity access
   - Future predictions
   - Combined historical + future
```

## 🔧 Technical Implementation

### **Backend APIs**
- `/api/objective5/model-comparison/` - Auto-loaded
- `/api/objective5/countries/` - Auto-loaded
- `/api/objective5/historical/?country=X` - User-triggered
- `/api/objective5/predictions/?country=X` - User-triggered
- `/api/objective5/combined/?country=X` - User-triggered

### **Frontend JavaScript**
- `window.onload` → Auto-loads model comparison + countries
- `loadCountryData()` → User-triggered country analysis
- Chart.js for all visualizations
- Error handling for missing data

## ✅ Confirmation

**Model Comparison**: ✅ Auto-loads on page load
**Country Selection**: ✅ User selects from dropdown
**Analysis Charts**: ✅ Appear after country selection

This matches your requirements perfectly!