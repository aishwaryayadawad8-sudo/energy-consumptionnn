# Quick Start - Objective 1

## Start the Server

```bash
cd sustainable_energy
python manage.py runserver
```

## Access the Dashboard

Open your browser and visit:
```
http://127.0.0.1:8000/
```

## What You'll See

### 1. Objective Selector Page
- Two cards: Objective 1 and Objective 2
- Click **"Objective 1: Forecast Energy Consumption"**

### 2. Objective 1 Dashboard
Three main sections:

#### A. Model Comparison
- Click **"Load Model Comparison"** button
- Wait 10-30 seconds for training
- View bar chart showing MSE scores
- Best model is highlighted

#### B. Country Selection
- Select a country from dropdown (e.g., "India")
- Click **"Analyze Country"**

#### C. Results
- **Historical Chart:** Past energy consumption (2000-2020)
- **Predictions Chart:** Future consumption (2021-2030)

## Quick Test

1. Start server
2. Go to `http://127.0.0.1:8000/`
3. Click "Objective 1"
4. Click "Load Model Comparison"
5. Select "India" → Click "Analyze Country"
6. View the charts!

## Best Model Answer

**Question:** Which is the best model in ML?

**Answer:** The system automatically selects the best model based on **lowest MSE (Mean Squared Error)**. 

**Expected Best Performer:** **XGBoost**
- Typically achieves lowest MSE
- Handles complex patterns well
- Robust and accurate

**To See Results:**
1. Click "Load Model Comparison" on Objective 1 dashboard
2. Wait for training to complete
3. Check the bar chart - shortest bar = best model
4. Green badge shows: "Best Model: [Model Name]"

## URLs

- **Home/Selector:** http://127.0.0.1:8000/
- **Objective 1:** http://127.0.0.1:8000/objective1/
- **Objective 2 (Original):** http://127.0.0.1:8000/dashboard/

---

**That's it! Enjoy exploring energy consumption predictions! 📊⚡**
