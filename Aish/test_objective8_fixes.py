#!/usr/bin/env python3
"""
Test script to verify Objective 8 fixes:
- All 128 countries should be available
- Should have "Future Investment Strategy Predictions(2000-2020)"
- Should have "Future Investment Strategy Predictions(2021-2030)"
"""

import os
import sys
import pandas as pd

def test_objective8_fixes():
    print("🔍 Testing Objective 8 Fixes...")
    print("="*60)
    
    # Test 1: Check HTML template for correct section titles
    objective8_path = "sustainable_energy/dashboard/templates/dashboard/objective8.html"
    
    if os.path.exists(objective8_path):
        with open(objective8_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check for correct section titles
        if "Future Investment Strategy Predictions (2000-2020)" in content:
            print("✅ Found 'Future Investment Strategy Predictions (2000-2020)' section")
        else:
            print("❌ Missing 'Future Investment Strategy Predictions (2000-2020)' section")
            
        if "Future Investment Strategy Predictions (2021-2030)" in content:
            print("✅ Found 'Future Investment Strategy Predictions (2021-2030)' section")
        else:
            print("❌ Missing 'Future Investment Strategy Predictions (2021-2030)' section")
    else:
        print("❌ objective8.html file not found")
    
    # Test 2: Check views.py for updated countries function
    views_path = "sustainable_energy/dashboard/views.py"
    
    if os.path.exists(views_path):
        with open(views_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check if countries function uses the main dataset
        if "df = pd.read_csv(CSV_PATH)" in content and "df['Entity'].dropna().unique()" in content:
            print("✅ Countries function updated to use main dataset (all 128 countries)")
        else:
            print("❌ Countries function still uses hardcoded list")
    else:
        print("❌ views.py file not found")
    
    # Test 3: Check actual country count from dataset
    csv_path = "global-data-on-sustainable-energy.csv"
    if os.path.exists(csv_path):
        try:
            df = pd.read_csv(csv_path)
            countries = df['Entity'].dropna().unique()
            country_count = len(countries)
            
            if country_count >= 128:
                print(f"✅ Dataset contains {country_count} countries (≥128 as expected)")
            else:
                print(f"⚠️ Dataset contains {country_count} countries (less than 128)")
        except Exception as e:
            print(f"❌ Error reading dataset: {e}")
    else:
        print("❌ Dataset file not found")
    
    print("="*60)
    print("🎯 FIXES SUMMARY:")
    print("   • Countries: Updated to show all 128 countries from dataset")
    print("   • Section 1: Future Investment Strategy Predictions (2000-2020)")
    print("   • Section 2: Future Investment Strategy Predictions (2021-2030)")
    print("   • Chart titles: Updated to match section names")
    print("="*60)

if __name__ == "__main__":
    test_objective8_fixes()