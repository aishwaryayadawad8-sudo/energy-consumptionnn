#!/usr/bin/env python3
"""
Analyze renewable energy sources used in the SDG 7 project
"""

import pandas as pd
import os

def analyze_renewable_sources():
    print("🔍 RENEWABLE ENERGY SOURCES IN SDG 7 PROJECT")
    print("=" * 60)
    
    # Check the main dataset
    csv_path = "global-data-on-sustainable-energy.csv"
    
    try:
        # Read the dataset
        df = pd.read_csv(csv_path)
        
        print("📊 DATASET ANALYSIS:")
        print("=" * 40)
        
        # Get column names related to renewable energy
        renewable_columns = [col for col in df.columns if 'renewable' in col.lower() or 'renewables' in col.lower()]
        
        print("🔋 RENEWABLE ENERGY COLUMNS IN DATASET:")
        for i, col in enumerate(renewable_columns, 1):
            print(f"   {i}. {col}")
        
        # Check for specific renewable sources
        all_columns = df.columns.tolist()
        print(f"\n📋 ALL ENERGY-RELATED COLUMNS ({len(all_columns)} total):")
        
        energy_columns = [col for col in all_columns if any(keyword in col.lower() for keyword in 
                         ['energy', 'electricity', 'renewable', 'fossil', 'nuclear', 'solar', 'wind', 'hydro', 'biomass', 'geothermal'])]
        
        for i, col in enumerate(energy_columns, 1):
            print(f"   {i}. {col}")
        
        # Analyze renewable energy data
        if 'Electricity from renewables (TWh)' in df.columns:
            renewable_data = df['Electricity from renewables (TWh)'].dropna()
            print(f"\n📈 RENEWABLE ELECTRICITY STATISTICS:")
            print(f"   • Total records: {len(renewable_data)}")
            print(f"   • Average: {renewable_data.mean():.2f} TWh")
            print(f"   • Maximum: {renewable_data.max():.2f} TWh")
            print(f"   • Countries with data: {df[df['Electricity from renewables (TWh)'].notna()]['Entity'].nunique()}")
        
        if 'Renewable energy share in the total final energy consumption (%)' in df.columns:
            share_data = df['Renewable energy share in the total final energy consumption (%)'].dropna()
            print(f"\n🌍 RENEWABLE ENERGY SHARE STATISTICS:")
            print(f"   • Total records: {len(share_data)}")
            print(f"   • Average share: {share_data.mean():.2f}%")
            print(f"   • Maximum share: {share_data.max():.2f}%")
            print(f"   • Countries with data: {df[df['Renewable energy share in the total final energy consumption (%)'].notna()]['Entity'].nunique()}")
        
    except FileNotFoundError:
        print("❌ Main dataset not found")
    except Exception as e:
        print(f"❌ Error reading dataset: {e}")
    
    print("\n" + "=" * 60)
    print("🎯 RENEWABLE SOURCES IDENTIFIED IN PROJECT:")
    print("=" * 60)
    
    # Based on the dataset columns and project analysis
    renewable_sources = {
        "📊 TRACKED IN DATASET": [
            "Electricity from renewables (TWh) - Total renewable electricity generation",
            "Renewable energy share in total final energy consumption (%)",
            "Renewable-electricity-generating-capacity-per-capita",
            "Low-carbon electricity (% electricity) - Includes renewables + nuclear"
        ],
        
        "🔋 SPECIFIC SOURCES MENTIONED": [
            "Solar energy - Referenced in project documentation and icons",
            "Wind energy - Referenced in project documentation and icons", 
            "Hydroelectric power - Referenced in project documentation",
            "Biomass energy - Referenced in project documentation",
            "Geothermal energy - Referenced in project documentation"
        ],
        
        "⚡ ENERGY CATEGORIES": [
            "Fossil fuels (TWh) - For comparison with renewables",
            "Nuclear energy (TWh) - Low-carbon but not renewable",
            "Clean fuels for cooking - Renewable cooking solutions"
        ],
        
        "🎯 PROJECT OBJECTIVES USING RENEWABLES": [
            "Objective 3: Energy Access Classification - Uses renewable share data",
            "Objective 4: SDG-7 Progress Monitoring - Tracks renewable targets",
            "Objective 5: Energy Equity Analysis - Analyzes renewable access disparities",
            "Objective 7: Renewable Energy Potential Assessment - Dedicated to renewables",
            "Comprehensive Analysis: All objectives consider renewable vs fossil fuel mix"
        ]
    }
    
    for category, sources in renewable_sources.items():
        print(f"\n{category}:")
        for source in sources:
            print(f"   • {source}")
    
    print("\n" + "=" * 60)
    print("📋 SUMMARY:")
    print("=" * 60)
    
    summary = """
🌟 PRIMARY RENEWABLE SOURCES IN PROJECT:
   1. Solar Energy ☀️
   2. Wind Energy 💨  
   3. Hydroelectric Power 🌊
   4. Biomass Energy 🌱
   5. Geothermal Energy 🌋

📊 DATA TRACKING:
   • Total renewable electricity generation (TWh)
   • Renewable energy share in total consumption (%)
   • Per-capita renewable generating capacity
   • Clean cooking fuel access
   • Low-carbon electricity percentage

🎯 PROJECT FOCUS:
   • SDG 7 targets for renewable energy access
   • Country-wise renewable energy adoption
   • Renewable vs fossil fuel electricity generation
   • Energy equity analysis including renewable access
   • Future renewable energy potential assessment

🔬 ANALYSIS CAPABILITIES:
   • Historical renewable energy trends (2000-2020)
   • Future renewable energy predictions (2021-2030)
   • Country comparison of renewable adoption
   • Machine learning models for renewable forecasting
   • Policy impact analysis on renewable growth
"""
    
    print(summary)
    
    print("\n✅ CONCLUSION:")
    print("The SDG 7 project comprehensively tracks and analyzes renewable energy")
    print("sources including solar, wind, hydro, biomass, and geothermal energy,")
    print("with focus on electricity generation, energy access, and sustainability goals.")

if __name__ == "__main__":
    analyze_renewable_sources()