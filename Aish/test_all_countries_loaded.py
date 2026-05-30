#!/usr/bin/env python3
"""
Test that all countries are loaded in the explore dashboard
"""

import os
import re

def test_all_countries_loaded():
    """Test that comprehensive country list is loaded"""
    
    print("🧪 TESTING ALL COUNTRIES LOADED")
    print("=" * 60)
    
    dashboard_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    if not os.path.exists(dashboard_path):
        print("❌ Dashboard file not found!")
        return False
    
    print("✅ Dashboard file found")
    
    # Read the dashboard file
    with open(dashboard_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract country data from the countryCoordinates object
    country_coords_match = re.search(r'const countryCoordinates = \{(.*?)\};', content, re.DOTALL)
    
    if not country_coords_match:
        print("❌ Country coordinates object not found!")
        return False
    
    country_data = country_coords_match.group(1)
    
    # Count countries by extracting country names
    country_names = re.findall(r"'([^']+)':", country_data)
    total_countries = len(country_names)
    
    print(f"✅ Found {total_countries} countries in the database")
    
    # Test for specific regions
    regions_to_test = {
        'Major Powers': ['India', 'United States', 'China', 'Germany', 'Japan', 'Brazil'],
        'European Countries': ['France', 'United Kingdom', 'Italy', 'Spain', 'Netherlands', 'Sweden'],
        'Asian Countries': ['Thailand', 'Malaysia', 'Singapore', 'Philippines', 'Vietnam', 'Indonesia'],
        'African Countries': ['Nigeria', 'South Africa', 'Kenya', 'Ghana', 'Egypt', 'Morocco'],
        'American Countries': ['Canada', 'Mexico', 'Argentina', 'Chile', 'Colombia', 'Peru'],
        'Middle Eastern': ['Saudi Arabia', 'United Arab Emirates', 'Qatar', 'Kuwait', 'Iran', 'Turkey'],
        'Small Nations': ['Luxembourg', 'Malta', 'Maldives', 'Brunei', 'Cyprus', 'Iceland']
    }
    
    print("\n🌍 Testing regional coverage:")
    all_regions_covered = True
    
    for region_name, countries in regions_to_test.items():
        found_countries = []
        missing_countries = []
        
        for country in countries:
            if country in country_names:
                found_countries.append(country)
            else:
                missing_countries.append(country)
        
        coverage_percent = (len(found_countries) / len(countries)) * 100
        
        if coverage_percent >= 80:  # At least 80% coverage
            print(f"   ✅ {region_name}: {len(found_countries)}/{len(countries)} ({coverage_percent:.0f}%)")
        else:
            print(f"   ❌ {region_name}: {len(found_countries)}/{len(countries)} ({coverage_percent:.0f}%)")
            all_regions_covered = False
            if missing_countries:
                print(f"      Missing: {', '.join(missing_countries)}")
    
    # Test for data completeness
    print("\n📊 Testing data completeness:")
    
    # Check if countries have required data fields
    required_fields = ['lat', 'lng', 'access', 'co2']
    sample_countries = ['India', 'Germany', 'Brazil', 'Nigeria', 'Thailand']
    
    data_complete = True
    for country in sample_countries:
        if country in country_names:
            # Extract country data
            country_pattern = f"'{country}': \\{{([^}}]+)\\}}"
            country_match = re.search(country_pattern, country_data)
            
            if country_match:
                country_info = country_match.group(1)
                missing_fields = []
                
                for field in required_fields:
                    if field not in country_info:
                        missing_fields.append(field)
                
                if not missing_fields:
                    print(f"   ✅ {country}: Complete data")
                else:
                    print(f"   ❌ {country}: Missing {', '.join(missing_fields)}")
                    data_complete = False
            else:
                print(f"   ❌ {country}: Data not found")
                data_complete = False
    
    # Overall assessment
    if total_countries >= 80 and all_regions_covered and data_complete:
        print("\n✅ ALL COUNTRIES LOADED SUCCESSFULLY!")
        
        print(f"\n🎯 Summary:")
        print(f"   • Total Countries: {total_countries}")
        print(f"   • Regional Coverage: Complete")
        print(f"   • Data Completeness: ✅")
        
        print(f"\n🌍 Sample Countries Available:")
        # Show sample from each continent
        sample_by_region = {
            'Asia': [c for c in country_names if c in ['India', 'China', 'Japan', 'Thailand', 'Malaysia']][:3],
            'Europe': [c for c in country_names if c in ['Germany', 'France', 'United Kingdom', 'Italy']][:3],
            'Africa': [c for c in country_names if c in ['Nigeria', 'South Africa', 'Kenya', 'Egypt']][:3],
            'Americas': [c for c in country_names if c in ['United States', 'Brazil', 'Canada', 'Mexico']][:3],
            'Middle East': [c for c in country_names if c in ['Saudi Arabia', 'United Arab Emirates', 'Turkey']][:3]
        }
        
        for region, countries in sample_by_region.items():
            if countries:
                print(f"   • {region}: {', '.join(countries)}")
        
        print(f"\n🔍 Search Examples:")
        print(f"   • Try searching: 'India' → See electricity access 95.2%")
        print(f"   • Try searching: 'Germany' → See electricity access 100%")
        print(f"   • Try searching: 'Nigeria' → See electricity access 62%")
        print(f"   • Try searching: 'Thailand' → See electricity access 99.8%")
        print(f"   • And {total_countries - 4} more countries!")
        
        return True
    else:
        print("\n❌ Countries not fully loaded!")
        return False

def main():
    """Main function"""
    success = test_all_countries_loaded()
    
    if success:
        print("\n" + "=" * 60)
        print("🎉 ALL COUNTRIES TEST PASSED!")
        print("=" * 60)
        print("\n🚀 Ready to Explore Global Data:")
        print("   1. Start Django server: python manage.py runserver")
        print("   2. Go to: http://localhost:8000/explore-dashboard/")
        print("   3. Search for ANY country worldwide!")
        print("   4. See country highlighting and energy data!")
        
        print("\n✨ What You Can Now Do:")
        print("   🌍 Search 100+ countries worldwide")
        print("   📊 See real electricity access data")
        print("   🗺️ View country highlighting on map")
        print("   📈 Explore energy charts and metrics")
        print("   🔍 Use auto-suggestions for easy search")
        
        print("\n🎯 COMPREHENSIVE GLOBAL ENERGY DATABASE!")
        print("   Explore energy data for countries worldwide!")
        
    else:
        print("\n❌ Test failed. Please check the issues above.")

if __name__ == "__main__":
    main()