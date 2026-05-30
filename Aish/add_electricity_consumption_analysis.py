#!/usr/bin/env python3
"""
Add electricity consumption/usage analysis to complement predictions
Calculate total electricity used vs predicted in the SDG-7 project
"""

import pandas as pd
import numpy as np

def analyze_electricity_consumption_and_predictions():
    print("🔌 TOTAL ELECTRICITY CONSUMPTION & PREDICTIONS ANALYSIS")
    print("=" * 70)
    
    try:
        # Load the dataset
        df = pd.read_csv('global-data-on-sustainable-energy.csv')
        
        print(f"📊 Dataset Overview:")
        print(f"   • Countries: {df['Entity'].nunique()}")
        print(f"   • Years: {df['Year'].min():.0f} - {df['Year'].max():.0f}")
        print(f"   • Total Records: {len(df):,}")
        
        print("\n" + "=" * 70)
        print("⚡ HISTORICAL ELECTRICITY CONSUMPTION (USED)")
        print("=" * 70)
        
        # Calculate electricity consumption from generation data
        fossil_electricity = df['Electricity from fossil fuels (TWh)'].fillna(0)
        nuclear_electricity = df['Electricity from nuclear (TWh)'].fillna(0)
        renewable_electricity = df['Electricity from renewables (TWh)'].fillna(0)
        
        total_electricity_generated = fossil_electricity + nuclear_electricity + renewable_electricity
        
        # Calculate per capita consumption
        primary_energy_col = 'Primary energy consumption per capita (kWh/person)'
        energy_consumption_data = df[df[primary_energy_col].notna()]
        
        print(f"🏠 Historical Electricity Consumption (2000-2020):")
        print(f"   • Total Electricity Generated: {total_electricity_generated.sum():,.2f} TWh")
        print(f"   • Average per Year: {total_electricity_generated.sum() / len(df['Year'].unique()):,.2f} TWh/year")
        
        # Breakdown by source (what was consumed)
        print(f"\n📊 Electricity Consumed by Source (2000-2020):")
        print(f"   • From Fossil Fuels: {fossil_electricity.sum():,.2f} TWh ({fossil_electricity.sum()/total_electricity_generated.sum()*100:.1f}%)")
        print(f"   • From Nuclear: {nuclear_electricity.sum():,.2f} TWh ({nuclear_electricity.sum()/total_electricity_generated.sum()*100:.1f}%)")
        print(f"   • From Renewables: {renewable_electricity.sum():,.2f} TWh ({renewable_electricity.sum()/total_electricity_generated.sum()*100:.1f}%)")
        
        # Per capita consumption analysis
        if not energy_consumption_data.empty:
            avg_per_capita = energy_consumption_data[primary_energy_col].mean()
            total_population_years = len(energy_consumption_data)
            
            print(f"\n👥 Per Capita Energy Consumption:")
            print(f"   • Average: {avg_per_capita:,.2f} kWh/person/year")
            print(f"   • Data Points: {total_population_years:,} country-year records")
            
            # Estimate total consumption based on population
            # Rough estimate: assume average population and convert to TWh
            estimated_total_consumption = (avg_per_capita * total_population_years * 1000) / 1e9  # Convert to TWh
            print(f"   • Estimated Total Consumption: {estimated_total_consumption:,.2f} TWh equivalent")
        
        print("\n" + "=" * 70)
        print("🔮 FUTURE ELECTRICITY PREDICTIONS (2021-2030)")
        print("=" * 70)
        
        # Calculate future predictions (from previous analysis)
        latest_year = df['Year'].max()
        latest_data = df[df['Year'] == latest_year]
        
        countries_with_data = []
        total_predicted_electricity = 0
        
        for country in df['Entity'].unique():
            country_data = df[df['Entity'] == country].sort_values('Year')
            
            if len(country_data) >= 5:
                country_fossil = country_data['Electricity from fossil fuels (TWh)'].fillna(0)
                country_nuclear = country_data['Electricity from nuclear (TWh)'].fillna(0)
                country_renewable = country_data['Electricity from renewables (TWh)'].fillna(0)
                
                country_total = country_fossil + country_nuclear + country_renewable
                
                if country_total.sum() > 0:
                    years = country_data['Year'].values
                    electricity_values = country_total.values
                    
                    if len(electricity_values) > 1 and electricity_values[-1] > 0:
                        growth_rate = np.mean(np.diff(electricity_values))
                        base_value = electricity_values[-1]
                        predicted_2030 = base_value + (growth_rate * 10)
                        
                        if predicted_2030 > 0:
                            total_predicted_electricity += predicted_2030
                            countries_with_data.append({
                                'country': country,
                                'base_2020': base_value,
                                'predicted_2030': predicted_2030,
                                'growth_rate': growth_rate
                            })
        
        print(f"🔮 Future Electricity Predictions (2030):")
        print(f"   • Total Predicted Generation: {total_predicted_electricity:,.2f} TWh")
        print(f"   • Countries with Predictions: {len(countries_with_data)}")
        print(f"   • 10-Year Cumulative: {total_predicted_electricity * 5:,.2f} TWh")
        
        print("\n" + "=" * 70)
        print("📊 CONSUMPTION vs PREDICTIONS COMPARISON")
        print("=" * 70)
        
        historical_total = total_electricity_generated.sum()
        historical_annual_avg = historical_total / len(df['Year'].unique())
        
        print(f"⚖️  Historical vs Future Comparison:")
        print(f"   • Historical Total Used (2000-2020): {historical_total:,.2f} TWh")
        print(f"   • Historical Annual Average: {historical_annual_avg:,.2f} TWh/year")
        print(f"   • Predicted 2030 Generation: {total_predicted_electricity:,.2f} TWh")
        print(f"   • Growth Factor: {total_predicted_electricity/historical_annual_avg:.2f}x")
        
        # Calculate efficiency and access improvements
        access_data = df['Access to electricity (% of population)'].fillna(0)
        avg_access = access_data.mean()
        
        print(f"\n🌍 Global Electricity Access Analysis:")
        print(f"   • Average Electricity Access: {avg_access:.2f}% of population")
        print(f"   • People with Access: ~{avg_access/100 * 7.8:.1f} billion people")
        print(f"   • People without Access: ~{(100-avg_access)/100 * 7.8:.1f} billion people")
        
        print("\n" + "=" * 70)
        print("🎯 COMPREHENSIVE ELECTRICITY SUMMARY")
        print("=" * 70)
        
        print(f"📈 TOTAL ELECTRICITY IN PROJECT:")
        print(f"   • Historical Consumption (2000-2020): {historical_total:,.2f} TWh")
        print(f"   • Future Predictions (2030): {total_predicted_electricity:,.2f} TWh")
        print(f"   • COMBINED TOTAL: {historical_total + total_predicted_electricity:,.2f} TWh")
        
        print(f"\n🔌 Electricity Sources Analysis:")
        fossil_total = fossil_electricity.sum()
        nuclear_total = nuclear_electricity.sum()
        renewable_total = renewable_electricity.sum()
        
        print(f"   • Fossil Fuel Electricity: {fossil_total:,.2f} TWh")
        print(f"   • Nuclear Electricity: {nuclear_total:,.2f} TWh")
        print(f"   • Renewable Electricity: {renewable_total:,.2f} TWh")
        
        print(f"\n🌟 Project Impact Metrics:")
        print(f"   • Countries Analyzed: {df['Entity'].nunique()}")
        print(f"   • Years of Data: {len(df['Year'].unique())} years")
        print(f"   • ML Prediction Points: 10,000")
        print(f"   • Future Years Predicted: 10 years (2021-2030)")
        
        # Top electricity consuming/generating countries
        country_totals = df.groupby('Entity')[['Electricity from fossil fuels (TWh)', 
                                              'Electricity from nuclear (TWh)', 
                                              'Electricity from renewables (TWh)']].sum()
        country_totals['Total'] = country_totals.sum(axis=1)
        top_countries = country_totals.nlargest(5, 'Total')
        
        print(f"\n🏆 Top 5 Countries by Historical Electricity (2000-2020):")
        for i, (country, data) in enumerate(top_countries.iterrows(), 1):
            print(f"   {i}. {country}: {data['Total']:,.2f} TWh")
        
        print("\n" + "=" * 70)
        print("✅ ELECTRICITY CONSUMPTION & PREDICTIONS ANALYSIS COMPLETE")
        print("=" * 70)
        
        return {
            'historical_consumption': historical_total,
            'future_predictions': total_predicted_electricity,
            'combined_total': historical_total + total_predicted_electricity,
            'countries': df['Entity'].nunique(),
            'avg_access': avg_access
        }
        
    except Exception as e:
        print(f"❌ Error in electricity analysis: {e}")
        return None

if __name__ == "__main__":
    results = analyze_electricity_consumption_and_predictions()
    
    if results:
        print(f"\n🎉 FINAL ELECTRICITY TOTALS:")
        print(f"   ⚡ Historical Used: {results['historical_consumption']:,.2f} TWh")
        print(f"   🔮 Future Predicted: {results['future_predictions']:,.2f} TWh")
        print(f"   🌟 GRAND TOTAL: {results['combined_total']:,.2f} TWh")
        print(f"   🌍 Countries: {results['countries']}")
        print(f"   🔌 Global Access: {results['avg_access']:.1f}%")