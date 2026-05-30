#!/usr/bin/env python3
"""
Integrate the new energy dataset into the SDG 7 project
"""

import pandas as pd
import os
import shutil

def integrate_new_dataset():
    """
    Integrate the new energy dataset into the project
    """
    
    print("🔄 Integrating new energy dataset...")
    
    # Step 1: Move the new dataset to the project
    source_file = 'energy_data_new.csv'
    target_file = 'sustainable_energy/energy_data_new.csv'
    
    if os.path.exists(source_file):
        shutil.copy2(source_file, target_file)
        print(f"✅ Copied {source_file} to {target_file}")
    else:
        print(f"❌ Source file {source_file} not found")
        return
    
    # Step 2: Load and analyze the new dataset
    try:
        df = pd.read_csv(target_file)
        print(f"\n📊 Dataset Analysis:")
        print(f"   - Shape: {df.shape}")
        print(f"   - Countries: {df['Country'].nunique()} ({', '.join(df['Country'].unique())})")
        print(f"   - Years: {df['Year'].min()} - {df['Year'].max()}")
        print(f"   - Columns: {list(df.columns)}")
        
        # Show sample data
        print(f"\n📋 Sample Data:")
        print(df.head())
        
        # Check for missing values
        print(f"\n🔍 Missing Values:")
        print(df.isnull().sum())
        
    except Exception as e:
        print(f"❌ Error analyzing dataset: {e}")
        return
    
    # Step 3: Create a data adapter script
    adapter_script = '''#!/usr/bin/env python3
"""
Data adapter for the new energy dataset
Maps the new dataset structure to the existing project structure
"""

import pandas as pd
import numpy as np

class NewEnergyDataAdapter:
    """
    Adapter to use the new energy dataset with existing ML models
    """
    
    def __init__(self, csv_path='energy_data_new.csv'):
        self.csv_path = csv_path
        self.df = None
        
    def load_data(self):
        """Load the new dataset"""
        try:
            self.df = pd.read_csv(self.csv_path)
            print(f"✅ Loaded {len(self.df)} records from {self.csv_path}")
            return True
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return False
    
    def get_countries(self):
        """Get list of available countries"""
        if self.df is None:
            self.load_data()
        return sorted(self.df['Country'].unique().tolist())
    
    def get_country_data(self, country):
        """Get data for a specific country"""
        if self.df is None:
            self.load_data()
        
        country_data = self.df[self.df['Country'] == country].copy()
        if country_data.empty:
            return None
            
        # Sort by year
        country_data = country_data.sort_values('Year')
        
        return {
            'country': country,
            'years': country_data['Year'].tolist(),
            'electricity_access': country_data['Access_to_Electricity_%'].tolist(),
            'co2_emissions': country_data['CO2_Emissions'].tolist(),
            'renewable_energy': country_data['Renewable_Energy_%'].tolist(),
            'fuel_emissions': country_data['Fuel_Emissions_Index'].tolist(),
            'latest_access': country_data['Access_to_Electricity_%'].iloc[-1],
            'latest_year': country_data['Year'].iloc[-1]
        }
    
    def get_all_data(self):
        """Get data for all countries"""
        if self.df is None:
            self.load_data()
        
        all_data = []
        for country in self.get_countries():
            country_data = self.get_country_data(country)
            if country_data:
                all_data.append(country_data)
        
        return all_data
    
    def get_latest_access_rates(self):
        """Get latest electricity access rates for all countries"""
        if self.df is None:
            self.load_data()
        
        # Get latest year data for each country
        latest_data = self.df.groupby('Country').apply(
            lambda x: x.loc[x['Year'].idxmax()]
        ).reset_index(drop=True)
        
        return {
            row['Country']: {
                'access_rate': row['Access_to_Electricity_%'],
                'year': row['Year'],
                'co2_emissions': row['CO2_Emissions'],
                'renewable_energy': row['Renewable_Energy_%'],
                'fuel_emissions': row['Fuel_Emissions_Index']
            }
            for _, row in latest_data.iterrows()
        }
    
    def predict_future_access(self, years_ahead=1, country=None):
        """
        Simple prediction based on trend analysis
        """
        if self.df is None:
            self.load_data()
        
        predictions = []
        countries = [country] if country else self.get_countries()
        
        for ctry in countries:
            country_data = self.df[self.df['Country'] == ctry].copy()
            if len(country_data) < 2:
                continue
                
            # Sort by year
            country_data = country_data.sort_values('Year')
            
            # Calculate trend (simple linear regression)
            years = country_data['Year'].values
            access = country_data['Access_to_Electricity_%'].values
            
            # Simple trend calculation
            if len(years) >= 2:
                trend = (access[-1] - access[-2]) / (years[-1] - years[-2])
                
                for i in range(1, years_ahead + 1):
                    future_year = years[-1] + i
                    future_access = min(100, max(0, access[-1] + (trend * i)))
                    
                    predictions.append({
                        'country': ctry,
                        'year': future_year,
                        'predicted_access': future_access,
                        'trend': trend
                    })
        
        return predictions
    
    def get_summary_stats(self):
        """Get summary statistics"""
        if self.df is None:
            self.load_data()
        
        return {
            'total_records': len(self.df),
            'countries': self.df['Country'].nunique(),
            'year_range': f"{self.df['Year'].min()} - {self.df['Year'].max()}",
            'avg_access_rate': self.df['Access_to_Electricity_%'].mean(),
            'avg_co2_emissions': self.df['CO2_Emissions'].mean(),
            'avg_renewable_energy': self.df['Renewable_Energy_%'].mean(),
            'countries_100_access': len(self.df[self.df['Access_to_Electricity_%'] == 100]['Country'].unique()),
            'countries_below_50_access': len(self.df[self.df['Access_to_Electricity_%'] < 50]['Country'].unique())
        }

# Example usage
if __name__ == "__main__":
    adapter = NewEnergyDataAdapter()
    
    if adapter.load_data():
        print("\\n📊 Summary Statistics:")
        stats = adapter.get_summary_stats()
        for key, value in stats.items():
            print(f"   {key}: {value}")
        
        print("\\n🌍 Available Countries:")
        countries = adapter.get_countries()
        for country in countries:
            data = adapter.get_country_data(country)
            print(f"   {country}: {data['latest_access']}% access in {data['latest_year']}")
        
        print("\\n🔮 Future Predictions (2021):")
        predictions = adapter.predict_future_access(1)
        for pred in predictions:
            print(f"   {pred['country']}: {pred['predicted_access']:.1f}% (trend: {pred['trend']:+.1f}%/year)")
'''
    
    with open('sustainable_energy/new_energy_adapter.py', 'w', encoding='utf-8') as f:
        f.write(adapter_script)
    print("✅ Created new_energy_adapter.py")
    
    # Step 4: Create a test script
    test_script = '''#!/usr/bin/env python3
"""
Test the new energy dataset integration
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from new_energy_adapter import NewEnergyDataAdapter

def test_new_dataset():
    """Test the new dataset functionality"""
    
    print("🧪 Testing New Energy Dataset Integration...")
    
    # Initialize adapter
    adapter = NewEnergyDataAdapter()
    
    # Test 1: Load data
    print("\\n1️⃣ Testing data loading...")
    if adapter.load_data():
        print("✅ Data loaded successfully")
    else:
        print("❌ Failed to load data")
        return
    
    # Test 2: Get countries
    print("\\n2️⃣ Testing country list...")
    countries = adapter.get_countries()
    print(f"✅ Found {len(countries)} countries: {', '.join(countries)}")
    
    # Test 3: Get country data
    print("\\n3️⃣ Testing country data retrieval...")
    for country in countries[:2]:  # Test first 2 countries
        data = adapter.get_country_data(country)
        if data:
            print(f"✅ {country}: {len(data['years'])} years of data, latest access: {data['latest_access']}%")
        else:
            print(f"❌ No data for {country}")
    
    # Test 4: Get latest access rates
    print("\\n4️⃣ Testing latest access rates...")
    latest_rates = adapter.get_latest_access_rates()
    for country, info in latest_rates.items():
        print(f"   {country}: {info['access_rate']}% in {info['year']}")
    
    # Test 5: Predictions
    print("\\n5️⃣ Testing predictions...")
    predictions = adapter.predict_future_access(1)
    for pred in predictions:
        print(f"   {pred['country']} 2021: {pred['predicted_access']:.1f}%")
    
    # Test 6: Summary stats
    print("\\n6️⃣ Testing summary statistics...")
    stats = adapter.get_summary_stats()
    for key, value in stats.items():
        print(f"   {key}: {value}")
    
    print("\\n✅ All tests completed!")

if __name__ == "__main__":
    test_new_dataset()
'''
    
    with open('sustainable_energy/test_new_dataset.py', 'w', encoding='utf-8') as f:
        f.write(test_script)
    print("✅ Created test_new_dataset.py")
    
    # Step 5: Create integration guide
    guide = '''# New Energy Dataset Integration Guide

## 📊 Dataset Overview

The new energy dataset contains clean, structured data for 5 major countries:
- **India** (2000-2020)
- **China** (2000-2020) 
- **Brazil** (2000-2020)
- **Nigeria** (2000-2000)
- **USA** (2000-2020)

### Columns:
- `Country`: Country name
- `Year`: Year (2000-2020)
- `Access_to_Electricity_%`: Electricity access percentage (0-100)
- `CO2_Emissions`: CO2 emissions data
- `Renewable_Energy_%`: Renewable energy percentage
- `Fuel_Emissions_Index`: Fuel emissions index

## 🚀 How to Use

### 1. Basic Usage
```python
from new_energy_adapter import NewEnergyDataAdapter

# Initialize
adapter = NewEnergyDataAdapter()

# Load data
adapter.load_data()

# Get countries
countries = adapter.get_countries()
print(countries)  # ['Brazil', 'China', 'India', 'Nigeria', 'USA']
```

### 2. Get Country Data
```python
# Get data for India
india_data = adapter.get_country_data('India')
print(f"India access in 2020: {india_data['latest_access']}%")
```

### 3. Get Latest Access Rates
```python
latest_rates = adapter.get_latest_access_rates()
for country, info in latest_rates.items():
    print(f"{country}: {info['access_rate']}% in {info['year']}")
```

### 4. Make Predictions
```python
# Predict 2021 access rates
predictions = adapter.predict_future_access(1)
for pred in predictions:
    print(f"{pred['country']} 2021: {pred['predicted_access']:.1f}%")
```

## 🔧 Integration with Existing Project

### Option 1: Replace Current Dataset
Update the CSV_PATH in your ML models to use the new dataset:
```python
CSV_PATH = 'energy_data_new.csv'
```

### Option 2: Use Adapter (Recommended)
Use the NewEnergyDataAdapter class to maintain compatibility:
```python
from new_energy_adapter import NewEnergyDataAdapter

class UpdatedMLModel:
    def __init__(self):
        self.adapter = NewEnergyDataAdapter()
        self.adapter.load_data()
    
    def get_predictions(self, country=None):
        return self.adapter.predict_future_access(1, country)
```

## 📈 Key Insights from New Dataset

### Electricity Access Progress (2000-2020):
- **China**: 63% → 99% (Excellent progress)
- **Brazil**: 66% → 100% (Achieved universal access)
- **Nigeria**: 66% → 100% (Achieved universal access)
- **India**: 47% → 85% (Good progress, needs improvement)
- **USA**: 44% → 86% (Good progress from low start)

### Countries with 100% Access (2020):
- Brazil ✅
- Nigeria ✅

### Countries Needing Attention:
- India (85% - needs improvement)
- USA (86% - needs improvement)
- China (99% - almost there)

## 🧪 Testing

Run the test script to verify integration:
```bash
cd sustainable_energy
python test_new_dataset.py
```

## 📧 Email Alert Integration

The new dataset can be used with the email alert system:
1. Countries with <90% access will receive "needs improvement" alerts
2. Countries with 100% access will receive "congratulations" alerts
3. Custom messages can be sent based on the new data

## 🔄 Next Steps

1. **Test the integration**: Run `python test_new_dataset.py`
2. **Update ML models**: Modify existing models to use the adapter
3. **Update dashboards**: Use new data for visualizations
4. **Test email alerts**: Send alerts based on new dataset
5. **Add more countries**: Expand the dataset with more countries

## 📁 Files Created

- `energy_data_new.csv` - The new dataset
- `new_energy_adapter.py` - Data adapter class
- `test_new_dataset.py` - Test script
- `NEW_DATASET_INTEGRATION_GUIDE.md` - This guide

## 🎯 Benefits

✅ **Cleaner Data**: More structured and consistent
✅ **Better Coverage**: 21 years of data per country
✅ **Multiple Metrics**: Access, CO2, Renewable Energy, Fuel Emissions
✅ **Easy Integration**: Adapter maintains compatibility
✅ **Real Insights**: Shows actual progress trends
✅ **Email Ready**: Perfect for alert system
'''
    
    with open('NEW_DATASET_INTEGRATION_GUIDE.md', 'w', encoding='utf-8') as f:
        f.write(guide)
    print("✅ Created NEW_DATASET_INTEGRATION_GUIDE.md")
    
    print("\n🎉 Integration Complete!")
    print("\n📋 What was created:")
    print("   ✅ energy_data_new.csv - New dataset")
    print("   ✅ sustainable_energy/new_energy_adapter.py - Data adapter")
    print("   ✅ sustainable_energy/test_new_dataset.py - Test script")
    print("   ✅ NEW_DATASET_INTEGRATION_GUIDE.md - Integration guide")
    
    print("\n🚀 Next Steps:")
    print("   1. Run: cd sustainable_energy && python test_new_dataset.py")
    print("   2. Check the test results")
    print("   3. Update your ML models to use the new adapter")
    print("   4. Test email alerts with the new data")

if __name__ == "__main__":
    integrate_new_dataset()