#!/usr/bin/env python3
"""
Analyze CO₂ emissions data in the project to create comprehensive dashboard
"""

import pandas as pd
import numpy as np

def analyze_co2_emissions():
    print("🔍 Analyzing CO₂ Emissions data in the project...")
    
    try:
        # Load the dataset
        df = pd.read_csv('global-data-on-sustainable-energy.csv')
        
        # Clean CO₂ emissions data
        co2_column = 'Value_co2_emissions_kt_by_country'
        df_co2 = df[df[co2_column].notna()].copy()
        
        print(f"📊 Dataset Overview:")
        print(f"   • Total records: {len(df):,}")
        print(f"   • Records with CO₂ data: {len(df_co2):,}")
        print(f"   • Countries: {df_co2['Entity'].nunique()}")
        print(f"   • Years: {df_co2['Year'].min()}-{df_co2['Year'].max()}")
        
        # Calculate total emissions
        total_emissions = df_co2[co2_column].sum()
        print(f"\n🌍 Total CO₂ Emissions: {total_emissions:,.2f} kt")
        print(f"   • Equivalent to: {total_emissions/1000:,.2f} Mt (Million tonnes)")
        print(f"   • Equivalent to: {total_emissions/1000000:,.2f} Gt (Billion tonnes)")
        
        # Historical analysis
        historical_data = df_co2[df_co2['Year'] <= 2020]
        historical_total = historical_data[co2_column].sum()
        historical_years = historical_data['Year'].nunique()
        historical_avg = historical_total / historical_years
        
        print(f"\n📈 Historical Analysis (2000-2020):")
        print(f"   • Total Historical Emissions: {historical_total:,.2f} kt")
        print(f"   • Years of Data: {historical_years}")
        print(f"   • Annual Average: {historical_avg:,.2f} kt/year")
        
        # Top emitting countries
        country_totals = df_co2.groupby('Entity')[co2_column].sum().sort_values(ascending=False)
        print(f"\n🏭 Top 10 CO₂ Emitting Countries:")
        for i, (country, emissions) in enumerate(country_totals.head(10).items(), 1):
            print(f"   {i:2d}. {country}: {emissions:,.2f} kt")
        
        # Yearly trends
        yearly_totals = df_co2.groupby('Year')[co2_column].sum().sort_index()
        print(f"\n📅 Yearly Emission Trends:")
        print(f"   • Highest Year: {yearly_totals.idxmax()} ({yearly_totals.max():,.2f} kt)")
        print(f"   • Lowest Year: {yearly_totals.idxmin()} ({yearly_totals.min():,.2f} kt)")
        
        # Recent trends (last 5 years of data)
        recent_years = yearly_totals.tail(5)
        trend = "increasing" if recent_years.iloc[-1] > recent_years.iloc[0] else "decreasing"
        print(f"   • Recent Trend (last 5 years): {trend}")
        
        # Emissions by energy source correlation
        fossil_fuel_corr = df_co2[['Electricity from fossil fuels (TWh)', co2_column]].corr().iloc[0,1]
        print(f"\n⚡ Energy-Emissions Correlation:")
        print(f"   • Fossil Fuel-CO₂ Correlation: {fossil_fuel_corr:.3f}")
        
        # Regional analysis (by continent - simplified)
        asia_countries = ['China', 'India', 'Japan', 'South Korea', 'Indonesia', 'Thailand', 'Malaysia', 'Singapore', 'Philippines', 'Vietnam']
        europe_countries = ['Germany', 'United Kingdom', 'France', 'Italy', 'Spain', 'Netherlands', 'Belgium', 'Poland', 'Sweden', 'Norway']
        americas_countries = ['United States', 'Canada', 'Brazil', 'Mexico', 'Argentina', 'Chile', 'Colombia', 'Venezuela', 'Peru', 'Ecuador']
        
        asia_emissions = df_co2[df_co2['Entity'].isin(asia_countries)][co2_column].sum()
        europe_emissions = df_co2[df_co2['Entity'].isin(europe_countries)][co2_column].sum()
        americas_emissions = df_co2[df_co2['Entity'].isin(americas_countries)][co2_column].sum()
        
        print(f"\n🌏 Regional Emissions (Major Countries):")
        print(f"   • Asia: {asia_emissions:,.2f} kt ({asia_emissions/total_emissions*100:.1f}%)")
        print(f"   • Europe: {europe_emissions:,.2f} kt ({europe_emissions/total_emissions*100:.1f}%)")
        print(f"   • Americas: {americas_emissions:,.2f} kt ({americas_emissions/total_emissions*100:.1f}%)")
        
        # Predictions analysis (if any future data exists)
        future_data = df_co2[df_co2['Year'] > 2020]
        if len(future_data) > 0:
            future_total = future_data[co2_column].sum()
            print(f"\n🔮 Future Predictions:")
            print(f"   • Future Emissions: {future_total:,.2f} kt")
        else:
            # Estimate future based on trend
            recent_avg = yearly_totals.tail(3).mean()
            estimated_2030 = recent_avg * 1.1  # Assume 10% increase
            print(f"\n🔮 Estimated Future (2030):")
            print(f"   • Estimated 2030 Emissions: {estimated_2030:,.2f} kt")
        
        # Summary for dashboard
        print(f"\n📋 Dashboard Summary Data:")
        print(f"   • Total Project CO₂: {total_emissions:,.2f} kt")
        print(f"   • In Million Tonnes: {total_emissions/1000:,.2f} Mt")
        print(f"   • Countries Analyzed: {df_co2['Entity'].nunique()}")
        print(f"   • Time Period: {df_co2['Year'].min()}-{df_co2['Year'].max()}")
        print(f"   • Annual Average: {historical_avg:,.2f} kt/year")
        
        return {
            'total_emissions_kt': total_emissions,
            'total_emissions_mt': total_emissions/1000,
            'historical_total': historical_total,
            'historical_avg': historical_avg,
            'countries': df_co2['Entity'].nunique(),
            'years': f"{df_co2['Year'].min()}-{df_co2['Year'].max()}",
            'top_countries': country_totals.head(10).to_dict(),
            'yearly_totals': yearly_totals.to_dict(),
            'regional_data': {
                'Asia': asia_emissions,
                'Europe': europe_emissions,
                'Americas': americas_emissions
            }
        }
        
    except Exception as e:
        print(f"❌ Error analyzing CO₂ data: {e}")
        return None

if __name__ == "__main__":
    analyze_co2_emissions()