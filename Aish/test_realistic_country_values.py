#!/usr/bin/env python3
"""
Test that countries now show different realistic electricity access values
"""

def test_realistic_values():
    """Test the updated country data with realistic values"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🧪 Testing realistic country values...")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Test specific countries with different access levels
        test_countries = [
            ("South Sudan", "7.2", "Lowest access"),
            ("Chad", "11.1", "Very low access"),
            ("Ethiopia", "44.3", "Medium-low access"),
            ("Nigeria", "62.0", "Medium access"),
            ("Kenya", "71.4", "Medium-high access"),
            ("India", "95.2", "High access"),
            ("Brazil", "99.7", "Very high access"),
            ("Germany", "100.0", "Full access"),
            ("United States", "100.0", "Full access")
        ]
        
        print("📊 Checking country electricity access values:")
        print("-" * 50)
        
        all_found = True
        for country, access, category in test_countries:
            if f"'{country}'" in content and f"access: {access}" in content:
                print(f"✅ {country}: {access}% - {category}")
            else:
                print(f"❌ {country}: {access}% - NOT FOUND")
                all_found = False
        
        # Check that we don't have all 100% anymore
        country_section = content[content.find('countryCoordinates'):content.find('};', content.find('countryCoordinates'))]
        access_100_count = country_section.count('access: 100.0')
        total_countries = country_section.count('access:')
        
        print(f"\n📈 Access Distribution:")
        print(f"   • Countries with 100% access: {access_100_count}")
        print(f"   • Total countries: {total_countries}")
        print(f"   • Countries with <100% access: {total_countries - access_100_count}")
        
        if access_100_count < total_countries:
            print("✅ Good! Not all countries show 100% access")
        else:
            print("❌ Problem! All countries still show 100% access")
        
        # Check for variety in access levels
        access_levels = []
        import re
        matches = re.findall(r'access: (\d+\.?\d*)', country_section)
        unique_access_levels = len(set(matches))
        
        print(f"\n🎯 Data Variety:")
        print(f"   • Unique access levels: {unique_access_levels}")
        print(f"   • Range: {min(matches)} - {max(matches)}%")
        
        if unique_access_levels > 10:
            print("✅ Excellent variety in electricity access data!")
        elif unique_access_levels > 5:
            print("✅ Good variety in electricity access data!")
        else:
            print("⚠️ Limited variety in electricity access data")
        
        print("\n🎯 Realistic Values Test Results:")
        if all_found and access_100_count < total_countries and unique_access_levels > 10:
            print("   ✅ All test countries found with correct values")
            print("   ✅ Variety in electricity access percentages")
            print("   ✅ Realistic data distribution")
            return True
        else:
            print("   ❌ Some issues found with country data")
            return False
        
    except Exception as e:
        print(f"❌ Error testing values: {e}")
        return False

def main():
    """Main function"""
    print("🧪 TESTING REALISTIC COUNTRY VALUES")
    print("=" * 50)
    
    success = test_realistic_values()
    
    if success:
        print("\n" + "=" * 50)
        print("✅ REALISTIC VALUES WORKING!")
        print("=" * 50)
        print("\n🌍 Country Examples to Test:")
        print("   • South Sudan (7.2%) - Lowest access")
        print("   • Chad (11.1%) - Very low access")
        print("   • Ethiopia (44.3%) - Medium access")
        print("   • Nigeria (62.0%) - Medium access")
        print("   • India (95.2%) - High access")
        print("   • Germany (100%) - Full access")
        
        print("\n🚀 Test It Now:")
        print("   1. Refresh browser (Ctrl+F5)")
        print("   2. Search 'Chad' → See 11.1% in charts")
        print("   3. Search 'Ethiopia' → See 44.3% in charts")
        print("   4. Search 'India' → See 95.2% in charts")
        print("   5. Search 'Germany' → See 100% in charts")
        
        print("\n📊 Charts Will Show:")
        print("   • Different Y-axis scales for different countries")
        print("   • Varied timeline progressions")
        print("   • Realistic forecast projections")
        print("   • Country-specific metric cards")
        
        print("\n🎯 NO MORE 100% FOR ALL COUNTRIES!")
        
    else:
        print("\n❌ Some tests failed - may need additional fixes.")

if __name__ == "__main__":
    main()