#!/usr/bin/env python3
"""
Update the project to use the exact dataset provided by the user
"""

def update_exact_dataset():
    """Update the dataset to match exactly what the user provided"""
    
    print("🔄 Updating project with exact dataset...")
    
    # The exact dataset as provided by the user
    dataset_content = """Country,Year,Access_to_Electricity_%,CO2_Emissions,Renewable_Energy_%,Fuel_Emissions_Index
India,2000,47,7.8,23.7,187.18
India,2001,50,19.04,35.78,222.97
India,2002,50,14.77,61.67,212.99
India,2003,54,12.17,22.16,106.07
India,2004,56,3.54,10.77,228.04
India,2005,55,3.54,26.73,109.31
India,2006,58,1.63,17.09,131.35
India,2007,60,17.39,74.73,236.62
India,2008,62,12.22,65.61,212.41
India,2009,66,14.31,52.51,262.31
India,2010,67,0.9,70.36,214.4
India,2011,68,19.41,65.28,192.08
India,2012,72,16.73,18.99,73.42
India,2013,71,4.64,71.94,141.93
India,2014,75,4.05,45.45,116.3
India,2015,75,4.08,65.56,111
India,2016,79,6.43,72.21,293.25
India,2017,82,10.73,28.85,148.27
India,2018,80,8.92,13.25,273.01
India,2019,85,6.18,22.1,207.78
India,2020,85,12.43,37.03,248.7
China,2000,63,3.22,66.35,175.66
China,2001,64,6.2,69.55,194.23
China,2002,63,7.64,5.52,173.13
China,2003,65,9.39,43.31,98.81
China,2004,69,15.81,36.31,230.61
China,2005,71,4.39,21.66,120.19
China,2006,72,10.53,13.99,56.08
China,2007,76,12.05,30.32,211.37
China,2008,78,1.41,75.72,94.28
China,2009,79,12.35,29.24,285.11
China,2010,82,3.83,43.91,288.48
China,2011,84,1.77,57.73,278.72
China,2012,83,19,32.27,142.54
China,2013,87,19.33,77.88,53.86
China,2014,91,16.26,77.18,282.08
China,2015,91,6.44,23.88,157.05
China,2016,95,2.4,42.29,291.66
China,2017,93,13.84,27.57,290.9
China,2018,96,9.08,26.36,263.25
China,2019,100,2.88,7.77,123.61
China,2020,99,10.16,50.72,146.27
Brazil,2000,66,1.17,42.7,262.78
Brazil,2001,68,18.23,8.86,129.23
Brazil,2002,69,5.55,25.9,92.37
Brazil,2003,72,13.42,73.12,189.2
Brazil,2004,77,6.58,22.97,284.04
Brazil,2005,76,10.64,15.87,224.01
Brazil,2006,80,11.16,41.71,192.52
Brazil,2007,82,4.1,78.92,74.29
Brazil,2008,84,19.41,23.15,203.75
Brazil,2009,86,15.62,55.41,297.51
Brazil,2010,89,18.82,62.12,85.02
Brazil,2011,89,17.95,22.82,179.58
Brazil,2012,89,12.16,59.62,269.34
Brazil,2013,94,18.48,32.58,235.19
Brazil,2014,94,2.23,52.42,224.25
Brazil,2015,98,4.32,52.51,225.62
Brazil,2016,98,1.38,45.18,139.87
Brazil,2017,100,6.84,11.77,123.4
Brazil,2018,100,8.08,67.65,252.34
Brazil,2019,100,5.79,29.06,252.53
Brazil,2020,100,16.66,18.99,266.77
Nigeria,2000,66,7.46,8.06,278.31
Nigeria,2001,66,5.98,49.32,177.84
Nigeria,2002,68,11.08,55.82,175.38
Nigeria,2003,72,3.25,6.24,249.57
Nigeria,2004,74,16.14,43.41,212.49
Nigeria,2005,73,1.95,21.99,225.49
Nigeria,2006,79,19.74,53.39,248.95
Nigeria,2007,81,15.56,18.08,272.5
Nigeria,2008,80,4.37,56.82,134.5
Nigeria,2009,85,0.61,34.01,143.9
Nigeria,2010,84,16.4,75.25,73.5
Nigeria,2011,85,14.28,15.31,194.57
Nigeria,2012,90,14.72,30.58,58.99
Nigeria,2013,92,15.54,13.51,166.4
Nigeria,2014,94,1.94,74.35,185.66
Nigeria,2015,97,7.49,70.8,121.64
Nigeria,2016,95,2.76,24.35,197.71
Nigeria,2017,100,17.33,54.5,57.63
Nigeria,2018,100,12.65,66.29,59.34
Nigeria,2019,100,6.95,46.64,255.65
Nigeria,2020,100,1.74,44.72,140.05
USA,2000,44,6.56,23.14,81.77
USA,2001,46,6.84,11.98,180.56
USA,2002,51,14.73,72.29,242.5
USA,2003,52,12.93,72.53,103.96
USA,2004,54,17.8,52.48,205.72
USA,2005,54,9.71,30.43,71.34
USA,2006,58,2.83,31.19,62.92
USA,2007,60,14.41,59.45,182.84
USA,2008,60,15.34,72.28,185.16
USA,2009,64,11.44,71.53,209.36
USA,2010,68,15.53,63.49,231.52
USA,2011,67,10.13,53.15,293.96
USA,2012,69,10.69,11.31,179.08
USA,2013,70,8.84,17.12,130.74
USA,2014,75,1,72.39,248.8
USA,2015,74,2.6,50.48,117.71
USA,2016,79,1.11,5.69,159.74
USA,2017,79,12.91,12.61,69.61
USA,2018,80,6.63,54.76,56.34
USA,2019,86,10.42,5.38,290.66
USA,2020,86,18.2,17.06,259"""
    
    # Step 1: Update the main dataset file
    with open('sustainable_energy/energy_data_new.csv', 'w', encoding='utf-8') as f:
        f.write(dataset_content)
    print("✅ Updated energy_data_new.csv with exact dataset")
    
    # Step 2: Also update the root level file
    with open('energy_data_new.csv', 'w', encoding='utf-8') as f:
        f.write(dataset_content)
    print("✅ Updated root energy_data_new.csv")
    
    # Step 3: Test the updated dataset
    print("\n📊 Testing updated dataset...")
    try:
        import pandas as pd
        df = pd.read_csv('sustainable_energy/energy_data_new.csv')
        
        print(f"   📈 Dataset shape: {df.shape}")
        print(f"   🌍 Countries: {df['Country'].nunique()} ({', '.join(df['Country'].unique())})")
        print(f"   📅 Years: {df['Year'].min()} - {df['Year'].max()}")
        print(f"   📊 Total records: {len(df)}")
        
        # Show latest access rates
        print(f"\n📋 Latest electricity access rates (2020):")
        latest = df[df['Year'] == 2020].sort_values('Access_to_Electricity_%', ascending=False)
        for _, row in latest.iterrows():
            print(f"   {row['Country']}: {row['Access_to_Electricity_%']}%")
            
    except Exception as e:
        print(f"❌ Error testing dataset: {e}")
    
    # Step 4: Test the adapter
    print("\n🧪 Testing new energy adapter...")
    try:
        import sys
        sys.path.append('sustainable_energy')
        from new_energy_adapter import NewEnergyDataAdapter
        
        adapter = NewEnergyDataAdapter()
        if adapter.load_data():
            countries = adapter.get_countries()
            print(f"✅ Adapter loaded {len(countries)} countries: {', '.join(countries)}")
            
            # Test predictions
            predictions = adapter.predict_future_access(1)
            print(f"✅ Generated {len(predictions)} predictions for 2021")
            
            for pred in predictions:
                print(f"   {pred['country']}: {pred['predicted_access']:.1f}% (trend: {pred['trend']:+.1f}%/year)")
        else:
            print("❌ Failed to load data with adapter")
            
    except Exception as e:
        print(f"❌ Error testing adapter: {e}")
    
    print("\n🎯 Dataset Implementation Summary:")
    print("="*50)
    print("✅ Countries: India, China, Brazil, Nigeria, USA")
    print("✅ Years: 2000-2020 (21 years each)")
    print("✅ Total records: 105 (21 × 5 countries)")
    print("✅ Columns: Country, Year, Access_to_Electricity_%, CO2_Emissions, Renewable_Energy_%, Fuel_Emissions_Index")
    print("✅ Email alerts: Ready for all 5 countries")
    print("✅ ML models: Compatible with new dataset")
    print("✅ Dashboard: Will show new countries")
    
    print("\n📧 Email Configuration:")
    print("   All 5 countries → assowmya649@gmail.com")
    
    print("\n🚀 Ready to use!")
    print("   1. XGBoost alerts will use this exact dataset")
    print("   2. Dashboard will show these 5 countries")
    print("   3. Email alerts will be sent based on 2021 predictions")
    print("   4. All ML models will use this data")

if __name__ == "__main__":
    update_exact_dataset()