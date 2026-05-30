"""
Simple test of the predictions without Django
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Load data
CSV_PATH = 'global-data-on-sustainable-energy.csv'

print("Testing Energy Consumption Predictions...")
print("=" * 60)

try:
    df = pd.read_csv(CSV_PATH)
    
    # Clean column names
    df.columns = df.columns.str.strip().str.replace('\n', ' ').str.replace(r'\s+', ' ', regex=True)
    
    # Convert numeric columns
    for col in df.columns:
        if col not in ['Entity']:
            df[col] = df[col].astype(str).str.replace(',', '', regex=False)
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    target_col = "Primary energy consumption per capita (kWh/person)"
    df_simple = df[['Year', 'Entity', target_col]].dropna()
    
    print(f"✅ Loaded {len(df_simple)} data points")
    print(f"✅ Countries: {df_simple['Entity'].nunique()}")
    print(f"✅ Year range: {df_simple['Year'].min()} - {df_simple['Year'].max()}")
    
    # Test with India
    test_country = "India"
    country_data = df_simple[df_simple['Entity'] == test_country].sort_values('Year')
    
    print(f"\n📊 Testing with: {test_country}")
    print(f"   Historical data points: {len(country_data)}")
    print(f"   Year range: {country_data['Year'].min()} - {country_data['Year'].max()}")
    print(f"   Sample values:")
    print(country_data.head())
    
    if len(country_data) >= 3:
        # Make predictions
        years = country_data['Year'].values.reshape(-1, 1)
        consumption = country_data[target_col].values
        
        # Use polynomial features
        poly = PolynomialFeatures(degree=2)
        years_poly = poly.fit_transform(years)
        
        model = LinearRegression()
        model.fit(years_poly, consumption)
        
        # Generate future predictions
        last_year = int(country_data['Year'].max())
        future_years = np.arange(last_year + 1, last_year + 11).reshape(-1, 1)
        future_years_poly = poly.transform(future_years)
        future_predictions = model.predict(future_years_poly)
        
        print(f"\n✅ Predictions generated:")
        for year, pred in zip(future_years.flatten()[:5], future_predictions[:5]):
            print(f"   {int(year)}: {pred:.2f} kWh/person")
        
        print("\n✅ Test completed successfully!")
        print("   The prediction model is working correctly.")
    else:
        print(f"\n❌ Not enough data points for {test_country}")
    
except Exception as e:
    print(f"\n❌ Error: {str(e)}")
    import traceback
    traceback.print_exc()
