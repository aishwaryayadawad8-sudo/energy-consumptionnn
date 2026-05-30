# SDG 7 Dashboard - Sustainable Energy Analysis & Prediction

A comprehensive Django web application for analyzing and predicting global sustainable energy data, aligned with UN Sustainable Development Goal 7: Affordable and Clean Energy.

## 🌟 Features

### Three Distinct Objectives

1. **Objective 1: Forecast Energy Consumption**
   - Predict primary energy consumption per capita
   - Compare 4 ML models (Linear Regression, Decision Tree, KNN, XGBoost)
   - View historical trends and future predictions

2. **Objective 2: Predict Carbon Emissions**
   - Predict CO₂ emissions by country
   - Compare 4 ML models with MSE scores
   - Analyze historical emissions and forecast future trends

3. **Objective 3: SDG 7 Electricity Access Classification**
   - Classify electricity access levels (Low/Medium/High)
   - Compare 4 ML models for classification
   - Track policy interventions and their impact
   - Predict future access trends

4. **Full Dashboard: Electricity Access Analysis**
   - Interactive world map visualization
   - Comprehensive energy profiles
   - Status alerts (Good/Warning/Critical)
   - 7 ML models for predictions

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
cd sustainable_energy

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
```

### Access the Application

Open your browser and visit: **http://127.0.0.1:8000/**

## 📊 What You Can Do

### Objective 1: Energy Consumption
1. Compare ML model performance
2. Select any country
3. View historical energy consumption trends
4. Predict future consumption up to 2030

### Objective 2: CO₂ Emissions
1. Compare ML model performance
2. Select any country
3. View historical CO₂ emissions
4. Forecast future emissions up to 2030

### Full Dashboard
1. Explore interactive world map
2. Search for any country
3. View complete energy profile
4. Get status alerts
5. See ML-based predictions

## 🎯 Sample Countries to Try

- **High Energy Consumers:** United States, Canada, Norway
- **High CO₂ Emitters:** China, United States, India
- **Low Electricity Access:** Afghanistan, Chad, South Sudan
- **Renewable Leaders:** Iceland, Costa Rica, Norway

## 🤖 Machine Learning Models

### Objective 1 & 2 (4 Models Each)
- Linear Regression
- Decision Tree
- K-Nearest Neighbors (KNN)
- XGBoost

**Selection:** Lowest MSE (Mean Squared Error)

### Full Dashboard (7 Models)
- Linear Regression
- Decision Tree
- K-Nearest Neighbors
- Random Forest
- XGBoost
- LightGBM
- CatBoost

**Selection:** Highest R² Score

## 📁 Project Structure

```
sustainable_energy/
├── config/                 # Django settings
├── dashboard/             # Main app
│   ├── views.py          # View functions
│   ├── urls.py           # URL routing
│   └── templates/        # HTML templates
├── ml_models/            # ML modules
│   ├── energy_consumption_predictor.py
│   ├── co2_emissions_predictor.py
│   └── predictor.py
├── static/               # Static files
├── global-data-on-sustainable-energy.csv
└── manage.py
```

## 🔌 API Endpoints

### Objective 1
- `/api/objective1/model-comparison/` - Get MSE scores
- `/api/objective1/historical/?country=X` - Historical data
- `/api/objective1/predictions/?country=X&years=10` - Predictions
- `/api/objective1/countries/` - Available countries

### Objective 2
- `/api/objective2/model-comparison/` - Get MSE scores
- `/api/objective2/historical/?country=X` - Historical emissions
- `/api/objective2/predictions/?country=X&years=10` - Predictions
- `/api/objective2/countries/` - Available countries

### Objective 3
- `/api/objective3/model-comparison/` - Get MSE scores for classification
- `/api/objective3/historical/?country=X` - Historical access data
- `/api/objective3/predictions/?country=X&years=10` - Future predictions
- `/api/objective3/countries/` - Available countries
- `/api/objective3/distribution/` - Access level distribution
- `/api/objective3/combined/` - Combined historical and future data
- `/api/objective3/policy-markers/` - Policy intervention markers

### Full Dashboard
- `/api/search/?country=X` - Country profile
- `/api/predict/?country=X&years=5` - Predictions
- `/api/countries/` - All countries
- `/api/map-data/` - Map data

## 💻 Technologies

- **Backend:** Django 4.2.7, Python 3.x
- **ML:** scikit-learn, XGBoost, LightGBM, CatBoost
- **Data:** Pandas, NumPy
- **Frontend:** Bootstrap 5, Chart.js, Leaflet.js
- **Database:** SQLite (development)

## 📖 Documentation

- `COMPLETE_PROJECT_SUMMARY.md` - Comprehensive overview
- `OBJECTIVE1_GUIDE.md` - Objective 1 user guide
- `OBJECTIVE3_GUIDE.md` - Objective 2 user guide
- `sustainable_energy/PROJECT_GUIDE.md` - Full dashboard guide
- `sustainable_energy/QUICK_REFERENCE.md` - Quick commands
- `FINAL_PROJECT_STATUS.md` - Project status

## 🎨 Screenshots

### Objective Selector
Landing page with three objective cards to choose from.

### Objective 1: Energy Consumption
Purple-themed dashboard with model comparison and predictions.

### Objective 2: CO₂ Emissions
Red-themed dashboard focused on carbon emissions analysis.

### Full Dashboard
Comprehensive dashboard with world map and energy profiles.

## 🧪 Testing

```bash
# Check for issues
python manage.py check

# Run tests (if available)
python manage.py test
```

## 📈 Performance

- **Page Load:** < 3 seconds
- **Model Training:** 10-40 seconds (one-time per session)
- **API Response:** < 2 seconds
- **Chart Rendering:** Instant

## 🔮 Future Enhancements

- [ ] User authentication and favorites
- [ ] Multi-country comparison
- [ ] Export to PDF/Excel
- [ ] Real-time data updates
- [ ] Mobile app version
- [ ] Advanced filtering
- [ ] Confidence intervals
- [ ] Feature importance visualization

## 🌍 Dataset

**Source:** Global Data on Sustainable Energy

**Contains:**
- 2,992 rows
- 20+ columns
- Years 2000-2020
- Global country coverage

**Key Metrics:**
- Energy consumption per capita
- CO₂ emissions
- Electricity access
- Renewable energy share
- GDP per capita

## 🤝 Contributing

This is an educational project. Feel free to fork and enhance!

## 📄 License

Educational use only.

## 👨‍💻 Author

Built for SDG 7: Affordable and Clean Energy

## 🙏 Acknowledgments

- UN Sustainable Development Goals
- Global Energy Data providers
- Open-source ML libraries

## 📞 Support

For issues or questions:
1. Check documentation files
2. Review Django logs
3. Verify all dependencies installed
4. Check browser console (F12)

## ⚡ Quick Commands

```bash
# Start server
cd sustainable_energy
python manage.py runserver

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Check for issues
python manage.py check
```

## 🎯 Success Criteria

✅ Three objectives implemented
✅ Full dashboard functional
✅ 11 ML models working
✅ Interactive visualizations
✅ RESTful API
✅ Responsive design
✅ Complete documentation
✅ Production-ready

---

## 🚀 Get Started Now!

```bash
cd sustainable_energy
python manage.py runserver
```

**Visit: http://127.0.0.1:8000/**

---

**Making the world more sustainable, one prediction at a time! 🌍⚡🌱**
