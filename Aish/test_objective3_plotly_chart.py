#!/usr/bin/env python3
"""
Test Objective 3 Plotly historical chart functionality
"""

import requests
import json

def test_objective3_dashboard():
    """Test that Objective 3 dashboard loads correctly"""
    print("🧪 Testing Objective 3 Dashboard")
    print("=" * 50)
    
    try:
        response = requests.get("http://127.0.0.1:8000/objective3/", timeout=10)
        print(f"📊 Status: {response.status_code}")
        
        if response.status_code == 200:
            html_content = response.text
            
            # Check for required elements
            plotly_loaded = "plotly-2.24.1.min.js" in html_content
            historical_plot_div = 'id="historicalPercentagePlot"' in html_content
            combined_plot_div = 'id="combinedPlot"' in html_content
            api_calls = '/api/objective3/historical/' in html_content
            
            print(f"📈 Plotly library loaded: {plotly_loaded}")
            print(f"📊 Historical plot div exists: {historical_plot_div}")
            print(f"📊 Combined plot div exists: {combined_plot_div}")
            print(f"🔗 API calls configured: {api_calls}")
            
            if plotly_loaded and historical_plot_div and combined_plot_div and api_calls:
                print("✅ Dashboard structure is correct")
                return True
            else:
                print("❌ Dashboard structure has issues")
                return False
        else:
            print(f"❌ Failed to load dashboard: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_historical_data_structure():
    """Test that historical data has the correct structure for Plotly"""
    print("\n🧪 Testing Historical Data Structure")
    print("=" * 50)
    
    try:
        response = requests.get("http://127.0.0.1:8000/api/objective3/historical/", timeout=10)
        print(f"📊 Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('success') and 'data' in data:
                all_data = data['data']
                print(f"📊 Total data points: {len(all_data)}")
                
                # Check data structure for Plotly compatibility
                if all_data:
                    sample = all_data[0]
                    required_fields = ['Year', 'Entity', 'Access to electricity (% of population)']
                    
                    has_all_fields = all(field in sample for field in required_fields)
                    print(f"📋 Required fields present: {has_all_fields}")
                    
                    # Check data types
                    year_is_int = isinstance(sample['Year'], int)
                    entity_is_string = isinstance(sample['Entity'], str)
                    access_is_number = isinstance(sample['Access to electricity (% of population)'], (int, float))
                    
                    print(f"📊 Year is integer: {year_is_int}")
                    print(f"🌍 Entity is string: {entity_is_string}")
                    print(f"⚡ Access is number: {access_is_number}")
                    
                    # Count unique countries and years
                    countries = set(row['Entity'] for row in all_data)
                    years = set(row['Year'] for row in all_data)
                    
                    print(f"🌍 Unique countries: {len(countries)}")
                    print(f"📅 Year range: {min(years)} - {max(years)}")
                    
                    if has_all_fields and year_is_int and entity_is_string and access_is_number:
                        print("✅ Data structure is Plotly-compatible")
                        return True
                    else:
                        print("❌ Data structure has issues")
                        return False
                else:
                    print("❌ No data available")
                    return False
            else:
                print("❌ API returned error or no data")
                return False
        else:
            print(f"❌ API failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Testing Objective 3 Plotly Chart Implementation")
    print("=" * 70)
    
    dashboard_ok = test_objective3_dashboard()
    data_ok = test_historical_data_structure()
    
    print("\n" + "=" * 70)
    print("📋 FINAL RESULTS:")
    
    if dashboard_ok:
        print("✅ Dashboard: Plotly chart elements ready")
    else:
        print("❌ Dashboard: Issues found")
    
    if data_ok:
        print("✅ Data API: Plotly-compatible structure")
    else:
        print("❌ Data API: Issues found")
    
    if dashboard_ok and data_ok:
        print("\n🎉 SUCCESS! Objective 3 should now display the historical chart correctly")
        print("📈 The chart will show all countries with the selected country highlighted")
        print("🌐 Visit: http://127.0.0.1:8000/objective3/ and select a country to test")
    else:
        print("\n⚠️  Some issues need attention")

if __name__ == "__main__":
    main()