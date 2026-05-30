#!/usr/bin/env python3
"""
Test Objective 3 historical data API for all countries
"""

import requests
import json

def test_historical_all_countries():
    """Test the historical data API without country parameter"""
    print("🧪 Testing Objective 3 Historical Data (All Countries)")
    print("=" * 60)
    
    try:
        # Test without country parameter (should return all countries)
        url = "http://127.0.0.1:8000/api/objective3/historical/"
        print(f"📡 URL: {url}")
        
        response = requests.get(url, timeout=10)
        print(f"📊 Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success: {data.get('success', 'N/A')}")
            
            if data.get('success') and 'data' in data:
                all_data = data['data']
                print(f"📊 Total data points: {len(all_data)}")
                
                # Count unique countries
                countries = set(row['Entity'] for row in all_data)
                print(f"🌍 Unique countries: {len(countries)}")
                
                # Show sample data
                if all_data:
                    sample = all_data[0]
                    print(f"📋 Sample data: {sample}")
                
                # Check data structure
                required_fields = ['Year', 'Entity', 'Access to electricity (% of population)', 'Access_Level']
                sample_fields = list(all_data[0].keys()) if all_data else []
                missing_fields = [field for field in required_fields if field not in sample_fields]
                
                if not missing_fields:
                    print("✅ Data structure is correct")
                else:
                    print(f"❌ Missing fields: {missing_fields}")
                
                return True
            else:
                print("❌ No data returned")
                return False
        else:
            print(f"❌ Failed: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_historical_specific_country():
    """Test the historical data API with specific country"""
    print("\n🧪 Testing Objective 3 Historical Data (Specific Country)")
    print("=" * 60)
    
    try:
        # Test with specific country
        country = "Australia"
        url = f"http://127.0.0.1:8000/api/objective3/historical/?country={country}"
        print(f"📡 URL: {url}")
        
        response = requests.get(url, timeout=10)
        print(f"📊 Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success: {data.get('success', 'N/A')}")
            
            if data.get('success') and 'data' in data:
                country_data = data['data']
                print(f"📊 Data points for {country}: {len(country_data)}")
                
                if country_data:
                    sample = country_data[0]
                    print(f"📋 Sample data: {sample}")
                
                return True
            else:
                print("❌ No data returned")
                return False
        else:
            print(f"❌ Failed: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Testing Objective 3 Historical Data API")
    print("=" * 70)
    
    all_countries_ok = test_historical_all_countries()
    specific_country_ok = test_historical_specific_country()
    
    print("\n" + "=" * 70)
    print("📋 FINAL RESULTS:")
    
    if all_countries_ok:
        print("✅ All Countries API: Working")
    else:
        print("❌ All Countries API: Issues found")
    
    if specific_country_ok:
        print("✅ Specific Country API: Working")
    else:
        print("❌ Specific Country API: Issues found")
    
    if all_countries_ok and specific_country_ok:
        print("\n🎉 SUCCESS! Historical data API is working for both cases")
        print("📈 The Plotly chart should now load correctly with all countries data")
    else:
        print("\n⚠️  Some issues need attention")

if __name__ == "__main__":
    main()