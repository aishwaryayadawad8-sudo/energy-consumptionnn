#!/usr/bin/env python3
"""
Comprehensive Total Energy Analysis for the SDG-7 Project
Shows total energy statistics, consumption, generation, and key insights
"""

import pandas as pd
import numpy as np
from datetime import datetime

def analyze_total_energy():
    print("🔋 TOTAL ENERGY ANALYSIS - SDG-7 PROJECT")
    print("=" * 60)
    
    try:
        # Load the dataset
        df = pd.read_csv('global-data-on-sustainable-energy.csv')
        
        print(f"📊 Dataset Overview:")
        print(f"   • Total Records: {len(df):,}")
        print(f"   • Countries: {df['Entity'].nunique()}")
        print(f"   • Years Covered: {df['Year'].min()} - {df['Year'].max()}")
        print(f"   • Time Span: {df['Year'].max() - df['Year'].min() + 1} years")
        
        print("\n" + "=" * 60)
        print("⚡ TOTAL ENERGY CONSUMPTION ANALYSIS")
        print("=" * 60)
        
        # Primary Energy Consumption Analysis
        primary_energy_col = 'Primary energy consumption per capita (kWh/person)'
        if primary_energy_col in df.columns:
            # Remove NaN values for calculation
            energy_data = df[df[primary_energy_col].notna()]
            
            total_records = len(energy_data)
            avg_per_capita = energy_data[primary_energy_col].mean()
            max_per_capita = energy_data[primary_energy_col].max()
            min_per_capita = energy_data[primary_energy_col].min()
            
            print(f"📈 Primary Energy Consumption Per Capita:")
            print(f"   • Average: {avg_per_capita:,.2f} kWh/person/year")
            print(f"   • Maximum: {max_per_capita:,.2f} kWh/person/year")
            print(f"   • Minimum: {min_per_capita:,.2f} kWh/person/year")
            print(f"   • Data Points: {total_records:,} records")
            
            # Find countries with highest and lowest consumption
            latest_year = energy_data['Year'].max()
            latest_data = energy_data[energy_data['Year'] == latest_year]
            
            if not latest_data.empty:
                highest_consumer = latest_data.loc[latest_data[primary_energy_col].idxmax()]
                lowest_consumer = latest_data.loc[latest_data[primary_energy_col].idxmin()]
                
                print(f"\n🏆 {latest_year} Energy Consumption Leaders:")
                print(f"   • Highest: {highest_consumer['Entity']} ({highest_consumer[primary_energy_col]:,.2f} kWh/person)")
                print(f"   • Lowest: {lowest_consumer['Entity']} ({lowest_consumer[primary_energy_col]:,.2f} kWh/person)")
        
        print("\n" + "=" * 60)
        print("🔌 ELECTRICITY GENERATION ANALYSIS")
        print("=" * 60)
        
        # Electricity Generation Analysis
        fossil_col = 'Electricity from fossil fuels (TWh)'
        nuclear_col = 'Electricity from nuclear (TWh)'
        renewable_col = 'Electricity from renewables (TWh)'
        
        electricity_cols = [fossil_col, nuclear_col, renewable_col]
        electricity_data = df[electricity_cols].fillna(0)
        
        total_fossil = electricity_data[fossil_col].sum()
        total_nuclear = electricity_data[nuclear_col].sum()
        total_renewable = electricity_data[renewable_col].sum()
        total_electricity = total_fossil + total_nuclear + total_renewable
        
        print(f"⚡ Total Electricity Generation (All Countries, All Years):")
        print(f"   • Fossil Fuels: {total_fossil:,.2f} TWh ({total_fossil/total_electricity*100:.1f}%)")
        print(f"   • Nuclear: {total_nuclear:,.2f} TWh ({total_nuclear/total_electricity*100:.1f}%)")
        print(f"   • Renewables: {total_renewable:,.2f} TWh ({total_renewable/total_electricity*100:.1f}%)")
        print(f"   • TOTAL: {total_electricity:,.2f} TWh")
        
        print("\n" + "=" * 60)
        print("🌱 RENEWABLE ENERGY ANALYSIS")
        print("=" * 60)
        
        # Renewable Energy Share Analysis
        renewable_share_col = 'Renewable energy share in the total final energy consumption (%)'
        if renewable_share_col in df.columns:
            renewable_share_data = df[df[renewable_share_col].notna()]
            
            avg_renewable_share = renewable_share_data[renewable_share_col].mean()
            max_renewable_share = renewable_share_data[renewable_share_col].max()
            min_renewable_share = renewable_share_data[renewable_share_col].min()
            
            print(f"🌿 Renewable Energy Share in Total Final Energy:")
            print(f"   • Global Average: {avg_renewable_share:.2f}%")
            print(f"   • Maximum: {max_renewable_share:.2f}%")
            print(f"   • Minimum: {min_renewable_share:.2f}%")
            
            # Countries with highest renewable share (latest year)
            if not latest_data.empty:
                renewable_latest = latest_data[latest_data[renewable_share_col].notna()]
                if not renewable_latest.empty:
                    top_renewable = renewable_latest.nlargest(5, renewable_share_col)
                    print(f"\n🏆 Top 5 Countries by Renewable Share ({latest_year}):")
                    for idx, row in top_renewable.iterrows():
                        print(f"   • {row['Entity']}: {row[renewable_share_col]:.2f}%")
        
        print("\n" + "=" * 60)
        print("🌍 ACCESS TO ENERGY ANALYSIS")
        print("=" * 60)
        
        # Energy Access Analysis
        electricity_access_col = 'Access to electricity (% of population)'
        clean_cooking_col = 'Access to clean fuels for cooking'
        
        if electricity_access_col in df.columns:
            access_data = df[df[electricity_access_col].notna()]
            avg_electricity_access = access_data[electricity_access_col].mean()
            
            print(f"🔌 Electricity Access:")
            print(f"   • Global Average: {avg_electricity_access:.2f}% of population")
            
            # Countries with full access vs limited access
            full_access = len(access_data[access_data[electricity_access_col] >= 99])
            limited_access = len(access_data[access_data[electricity_access_col] < 50])
            
            print(f"   • Countries with >99% access: {full_access}")
            print(f"   • Countries with <50% access: {limited_access}")
        
        if clean_cooking_col in df.columns:
            cooking_data = df[df[clean_cooking_col].notna()]
            if not cooking_data.empty:
                avg_clean_cooking = cooking_data[clean_cooking_col].mean()
                print(f"🔥 Clean Cooking Access:")
                print(f"   • Global Average: {avg_clean_cooking:.2f}% of population")
        
        print("\n" + "=" * 60)
        print("💰 ENERGY INVESTMENT ANALYSIS")
        print("=" * 60)
        
        # Financial Flows Analysis
        financial_col = 'Financial flows to developing countries (US $)'
        if financial_col in df.columns:
            financial_data = df[df[financial_col].notna()]
            total_investment = financial_data[financial_col].sum()
            avg_investment = financial_data[financial_col].mean()
            
            print(f"💵 Financial Flows to Developing Countries:")
            print(f"   • Total Investment: ${total_investment:,.0f}")
            print(f"   • Average per Record: ${avg_investment:,.0f}")
            print(f"   • Investment Records: {len(financial_data):,}")
        
        print("\n" + "=" * 60)
        print("🎯 PROJECT IMPACT SUMMARY")
        print("=" * 60)
        
        print(f"📊 Our SDG-7 Project Covers:")
        print(f"   • {df['Entity'].nunique()} Countries/Regions")
        print(f"   • {len(df):,} Data Points")
        print(f"   • {df['Year'].max() - df['Year'].min() + 1} Years of Energy Data")
        print(f"   • 8 Machine Learning Objectives")
        print(f"   • Multiple Energy Sources & Metrics")
        
        print(f"\n🎯 Key Focus Areas:")
        print(f"   • Energy Consumption Prediction")
        print(f"   • CO₂ Emission Forecasting")
        print(f"   • Energy Access Classification")
        print(f"   • SDG-7 Progress Monitoring")
        print(f"   • Energy Equity Analysis")
        print(f"   • Efficiency Optimization")
        print(f"   • Renewable Energy Assessment")
        print(f"   • Investment Strategy Support")
        
        print("\n" + "=" * 60)
        print("✅ ANALYSIS COMPLETE")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"❌ Error analyzing energy data: {e}")
        return False

if __name__ == "__main__":
    analyze_total_energy()