# Testing Checklist - SDG 7 Dashboard

## ✅ Features to Test

### 1. Dashboard Loading
- [ ] Dashboard loads at http://127.0.0.1:8000/
- [ ] Header displays: "Towards Affordable and Clean Energy"
- [ ] Project objectives section visible
- [ ] Search bar is present and functional
- [ ] World map loads correctly

### 2. World Map Functionality
- [ ] Map displays with countries marked
- [ ] Markers are color-coded (Green/Yellow/Red)
- [ ] Clicking markers shows popup with country info
- [ ] Popup displays: Country name, Electricity %, Renewable %, CO₂

### 3. Search Functionality
- [ ] Search bar accepts text input
- [ ] Autocomplete suggestions appear when typing
- [ ] Enter key triggers search
- [ ] Search button triggers search
- [ ] Loading spinner appears during search

### 4. Country Found - Complete Profile
Test with: **India**, **Germany**, **United States**

- [ ] Country name displays with flag icon
- [ ] Status alert box appears (Good/Warning/Critical)
- [ ] Alert shows appropriate color (Green/Yellow/Red)
- [ ] Alert lists specific conditions

#### Metrics Cards (4 cards)
- [ ] Electricity Access card displays with value
- [ ] Clean Cooking card displays with value
- [ ] Renewable Share card displays with value
- [ ] CO₂ Emissions card displays with value
- [ ] Cards have gradient backgrounds
- [ ] Cards show units (%, kt)

#### Historical Charts (4 charts)
- [ ] Electricity Access Trend chart loads
- [ ] Renewable Energy Trend chart loads
- [ ] CO₂ Emissions Trend chart loads
- [ ] Energy Mix pie chart loads
- [ ] Charts are interactive (hover shows values)
- [ ] Charts have proper labels and legends

#### Future Predictions
- [ ] Prediction chart loads
- [ ] Shows 5-year forecast
- [ ] Model name displayed (e.g., "CatBoost")
- [ ] Prediction values are reasonable (0-100%)

### 5. Country Not Found
Test with: **Atlantis**, **XYZ**, **NonExistentCountry**

- [ ] Warning icon (⚠️) displays
- [ ] "Country Not Found" message appears
- [ ] Clear explanation provided
- [ ] No empty charts shown
- [ ] No blank sections visible
- [ ] Message is on same page (not error page)

### 6. Edge Cases

#### Empty Search
- [ ] Clicking search with empty field shows alert

#### Partial Country Names
- [ ] Typing "Ind" shows India in autocomplete
- [ ] Typing "Ger" shows Germany in autocomplete

#### Case Sensitivity
- [ ] "india" (lowercase) works
- [ ] "INDIA" (uppercase) works
- [ ] "India" (mixed case) works

#### Special Characters
- [ ] Countries with spaces work (e.g., "United States")
- [ ] Countries with accents work (if in dataset)

### 7. Responsive Design
- [ ] Dashboard works on desktop (1920x1080)
- [ ] Dashboard works on laptop (1366x768)
- [ ] Dashboard works on tablet (768x1024)
- [ ] Dashboard works on mobile (375x667)
- [ ] Search bar is usable on mobile
- [ ] Charts resize properly

### 8. Performance
- [ ] Initial page load < 3 seconds
- [ ] Search results appear < 2 seconds
- [ ] Map loads < 2 seconds
- [ ] Charts render smoothly
- [ ] No lag when scrolling

### 9. API Endpoints

#### Test /api/search/
```bash
http://127.0.0.1:8000/api/search/?country=India
```
- [ ] Returns JSON with country data
- [ ] Returns 'found: true' for valid country
- [ ] Returns 'found: false' for invalid country

#### Test /api/predict/
```bash
http://127.0.0.1:8000/api/predict/?country=India&years=5
```
- [ ] Returns predictions array
- [ ] Shows model used
- [ ] Predictions are reasonable

#### Test /api/countries/
```bash
http://127.0.0.1:8000/api/countries/
```
- [ ] Returns list of all countries
- [ ] List is sorted alphabetically

#### Test /api/map-data/
```bash
http://127.0.0.1:8000/api/map-data/
```
- [ ] Returns map data for all countries
- [ ] Includes lat/lon coordinates
- [ ] Includes electricity access values

### 10. Browser Compatibility
- [ ] Works in Chrome
- [ ] Works in Firefox
- [ ] Works in Edge
- [ ] Works in Safari (if available)

### 11. Error Handling
- [ ] Server errors show friendly message
- [ ] Network errors handled gracefully
- [ ] Missing data shows "N/A" not errors
- [ ] Console shows no critical errors

## 🎯 Sample Countries to Test

### High Access Countries (Should show GOOD status)
- Germany
- United States
- Japan
- Australia
- France

### Medium Access Countries (Should show WARNING)
- India (improving)
- Brazil
- South Africa

### Low Access Countries (Should show CRITICAL)
- Afghanistan
- Chad
- Niger
- South Sudan

### Countries with Good Renewable Share
- Iceland
- Norway
- Costa Rica
- Albania

## 📊 Expected Results

### India (Example)
- Electricity Access: ~99%
- Status: GOOD or WARNING
- Renewable Share: ~20-40%
- CO₂ Emissions: High (large population)
- Trend: Improving over years

### Germany (Example)
- Electricity Access: 100%
- Status: GOOD
- Renewable Share: ~30-40%
- CO₂ Emissions: Moderate
- Trend: Stable/Improving

### Afghanistan (Example)
- Electricity Access: ~40-98% (varies by year)
- Status: WARNING or CRITICAL
- Renewable Share: Variable
- CO₂ Emissions: Low
- Trend: Improving

## 🐛 Common Issues & Solutions

### Issue: Charts not displaying
**Check**: Browser console for JavaScript errors
**Solution**: Refresh page, clear cache

### Issue: Map not loading
**Check**: Internet connection (needs OpenStreetMap tiles)
**Solution**: Check network, try different browser

### Issue: Predictions not showing
**Check**: Country has sufficient historical data
**Solution**: Try different country with more data

### Issue: Slow performance
**Check**: Dataset size, number of records
**Solution**: Optimize queries, add caching

## ✨ Success Criteria

All features working = **Project Complete! 🎉**

- ✅ Map displays correctly
- ✅ Search works for valid countries
- ✅ "Not Found" message for invalid countries
- ✅ All 4 metrics display
- ✅ All 4 historical charts display
- ✅ Predictions chart displays
- ✅ Status alerts work correctly
- ✅ No empty graphs or blank sections

---

**Happy Testing! 🧪✅**
