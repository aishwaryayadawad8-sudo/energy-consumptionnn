# 🚀 Objective 7: Quick Start Guide

## Access Objective 7

### 🌐 URLs
- **Home Selector:** http://127.0.0.1:8000/
- **Objective 7 Dashboard:** http://127.0.0.1:8000/objective7/

## What You'll See

### 📊 Chart 1: Model Accuracy Comparison
- Bar chart showing 4 ML models
- Higher accuracy = better performance
- Best model highlighted with green badge

### 📈 Chart 2: Historical Renewable Capacity
- Line chart with ALL countries
- Click country names in legend to show/hide
- Shows renewable capacity per capita (2000-2020)

### 🔮 Chart 3: Historical + Future Predictions
- Combined timeline view
- Solid lines = historical data
- Dashed lines = future predictions (10 years)
- Click countries to toggle visibility

## 🎯 Classification Levels

| Level | Capacity Range | Color |
|-------|---------------|-------|
| **Low Potential** | < 20 | Red |
| **Medium Potential** | 20-100 | Yellow |
| **High Potential** | > 100 | Green |

## 🌍 Sample Countries

### High Potential
- Iceland
- Norway  
- Sweden
- Denmark

### Medium Potential
- United States
- Germany
- Canada
- Australia

### Low Potential
- Afghanistan
- Bangladesh
- India
- Nigeria

## 🔧 API Endpoints

```
GET /api/objective7/model-comparison/
GET /api/objective7/countries/
GET /api/objective7/historical/?country=United%20States
GET /api/objective7/predictions/?country=United%20States&years=10
GET /api/objective7/combined/?country=United%20States
```

## ⚡ Quick Tips

1. **Loading Time:** First load takes 10-30 seconds (model training)
2. **Legend Controls:** Click country names to show/hide
3. **Zoom:** Use mouse wheel on charts
4. **Pan:** Click and drag on charts
5. **Reset:** Double-click chart to reset view

## 🧪 Test the Implementation

Open `test_objective7_simple.html` in your browser to:
- Test all API endpoints
- Verify data loading
- Check predictions
- Quick access to dashboard

## 🎨 Theme

**Orange Gradient** (Solar/Renewable Energy)
- Primary: #e67e22
- Secondary: #d35400
- Represents: Solar panels, renewable energy, sustainability

## 📱 Features

✅ 4 ML Classification Models
✅ Historical Data (2000-2020)
✅ Future Predictions (10 years)
✅ Interactive Charts
✅ All Countries Included
✅ Responsive Design
✅ Real-time Model Training

## 🎉 That's It!

Visit **http://127.0.0.1:8000/objective7/** and start exploring renewable energy investment potential!

---

**Need Help?**
- Check `OBJECTIVE7_COMPLETE.md` for full documentation
- View `test_objective7_simple.html` for API testing
- Server logs: Check terminal running `python manage.py runserver`
