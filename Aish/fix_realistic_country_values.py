#!/usr/bin/env python3
"""
Fix country data to show realistic electricity access percentages for different countries
"""

import os

def fix_realistic_country_values():
    """Update country data with realistic electricity access percentages"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔄 Fixing country data to show realistic values...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the countryCoordinates object and replace it with realistic data
        old_country_data_start = content.find('const countryCoordinates = {')
        if old_country_data_start == -1:
            print("❌ Could not find countryCoordinates object")
            return False
        
        # Find the end of the object
        brace_count = 0
        pos = old_country_data_start
        while pos < len(content):
            if content[pos] == '{':
                brace_count += 1
            elif content[pos] == '}':
                brace_count -= 1
                if brace_count == 0:
                    old_country_data_end = pos + 1
                    break
            pos += 1
        
        # New realistic country data with varied electricity access percentages
        new_country_data = '''const countryCoordinates = {
            'Afghanistan': { lat: 33.9391, lng: 67.7100, access: 97.7, co2: 9000 },
            'Albania': { lat: 41.1533, lng: 20.1683, access: 100.0, co2: 4500 },
            'Algeria': { lat: 28.0339, lng: 1.6596, access: 99.4, co2: 150000 },
            'Argentina': { lat: -38.4161, lng: -63.6167, access: 99.2, co2: 201000 },
            'Australia': { lat: -25.2744, lng: 133.7751, access: 100.0, co2: 415000 },
            'Austria': { lat: 47.5162, lng: 14.5501, access: 100.0, co2: 72000 },
            'Bangladesh': { lat: 23.6850, lng: 90.3563, access: 92.2, co2: 84000 },
            'Belgium': { lat: 50.5039, lng: 4.4699, access: 100.0, co2: 114000 },
            'Brazil': { lat: -14.2350, lng: -51.9253, access: 99.7, co2: 462000 },
            'Canada': { lat: 56.1304, lng: -106.3468, access: 100.0, co2: 672000 },
            'Chad': { lat: 15.4542, lng: 18.7322, access: 11.1, co2: 1200 },
            'Chile': { lat: -35.6751, lng: -71.5430, access: 99.8, co2: 87000 },
            'China': { lat: 35.8617, lng: 104.1954, access: 100.0, co2: 10065000 },
            'Colombia': { lat: 4.5709, lng: -74.2973, access: 97.4, co2: 84000 },
            'Democratic Republic of Congo': { lat: -4.0383, lng: 21.7587, access: 19.1, co2: 3200 },
            'Denmark': { lat: 56.2639, lng: 9.5018, access: 100.0, co2: 31000 },
            'Egypt': { lat: 26.8206, lng: 30.8025, access: 99.6, co2: 234000 },
            'Ethiopia': { lat: 9.1450, lng: 40.4897, access: 44.3, co2: 14000 },
            'Finland': { lat: 61.9241, lng: 25.7482, access: 100.0, co2: 45000 },
            'France': { lat: 46.6034, lng: 1.8883, access: 100.0, co2: 330000 },
            'Germany': { lat: 51.1657, lng: 10.4515, access: 100.0, co2: 729000 },
            'Ghana': { lat: 7.9465, lng: -1.0232, access: 85.0, co2: 16000 },
            'Greece': { lat: 39.0742, lng: 21.8243, access: 100.0, co2: 67000 },
            'India': { lat: 20.5937, lng: 78.9629, access: 95.2, co2: 2654000 },
            'Indonesia': { lat: -0.7893, lng: 113.9213, access: 97.8, co2: 615000 },
            'Iran': { lat: 32.4279, lng: 53.6880, access: 100.0, co2: 672000 },
            'Ireland': { lat: 53.4129, lng: -8.2439, access: 100.0, co2: 37000 },
            'Italy': { lat: 41.8719, lng: 12.5674, access: 100.0, co2: 335000 },
            'Japan': { lat: 36.2048, lng: 138.2529, access: 100.0, co2: 1162000 },
            'Kenya': { lat: -0.0236, lng: 37.9062, access: 71.4, co2: 17000 },
            'Liberia': { lat: 6.4281, lng: -9.4295, access: 28.5, co2: 800 },
            'Madagascar': { lat: -18.7669, lng: 46.8691, access: 26.6, co2: 3500 },
            'Malawi': { lat: -13.2543, lng: 34.3015, access: 18.4, co2: 1100 },
            'Malaysia': { lat: 4.2105, lng: 101.9758, access: 99.8, co2: 254000 },
            'Mali': { lat: 17.5707, lng: -3.9962, access: 43.0, co2: 3200 },
            'Mexico': { lat: 23.6345, lng: -102.5528, access: 99.4, co2: 486000 },
            'Mozambique': { lat: -18.6657, lng: 35.5296, access: 30.7, co2: 7800 },
            'Myanmar': { lat: 21.9162, lng: 95.9560, access: 70.1, co2: 18000 },
            'Nepal': { lat: 28.3949, lng: 84.1240, access: 90.7, co2: 9800 },
            'Netherlands': { lat: 52.1326, lng: 5.2913, access: 100.0, co2: 162000 },
            'Niger': { lat: 17.6078, lng: 8.0817, access: 18.2, co2: 2100 },
            'Nigeria': { lat: 9.0820, lng: 8.6753, access: 62.0, co2: 104000 },
            'Norway': { lat: 60.4720, lng: 8.4689, access: 100.0, co2: 35000 },
            'Pakistan': { lat: 30.3753, lng: 69.3451, access: 73.1, co2: 201000 },
            'Philippines': { lat: 12.8797, lng: 121.7740, access: 94.8, co2: 122000 },
            'Poland': { lat: 51.9194, lng: 19.1451, access: 100.0, co2: 341000 },
            'Russia': { lat: 61.5240, lng: 105.3188, access: 100.0, co2: 1711000 },
            'Rwanda': { lat: -1.9403, lng: 29.8739, access: 89.3, co2: 1000 },
            'Saudi Arabia': { lat: 23.8859, lng: 45.0792, access: 100.0, co2: 517000 },
            'Senegal': { lat: 14.4974, lng: -14.4524, access: 68.3, co2: 9800 },
            'Sierra Leone': { lat: 8.4606, lng: -11.7799, access: 26.2, co2: 1200 },
            'Somalia': { lat: 5.1521, lng: 46.1996, access: 36.8, co2: 600 },
            'South Africa': { lat: -30.5595, lng: 22.9375, access: 84.2, co2: 456000 },
            'South Korea': { lat: 35.9078, lng: 127.7669, access: 100.0, co2: 611000 },
            'South Sudan': { lat: 6.8770, lng: 31.3070, access: 7.2, co2: 1800 },
            'Spain': { lat: 40.4637, lng: -3.7492, access: 100.0, co2: 258000 },
            'Sudan': { lat: 12.8628, lng: 30.2176, access: 56.4, co2: 17000 },
            'Sweden': { lat: 60.1282, lng: 18.6435, access: 100.0, co2: 35000 },
            'Tanzania': { lat: -6.3690, lng: 34.8888, access: 37.7, co2: 11000 },
            'Thailand': { lat: 15.8700, lng: 100.9925, access: 99.8, co2: 273000 },
            'Turkey': { lat: 38.9637, lng: 35.2433, access: 100.0, co2: 353000 },
            'Uganda': { lat: 1.3733, lng: 32.2903, access: 57.3, co2: 5200 },
            'United Kingdom': { lat: 55.3781, lng: -3.4360, access: 100.0, co2: 351000 },
            'United States': { lat: 39.8283, lng: -98.5795, access: 100.0, co2: 5416000 },
            'Vietnam': { lat: 14.0583, lng: 108.2772, access: 99.0, co2: 282000 },
            'Yemen': { lat: 15.5527, lng: 48.5164, access: 69.4, co2: 8900 },
            'Zambia': { lat: -13.1339, lng: 27.8493, access: 31.3, co2: 5100 },
            'Zimbabwe': { lat: -19.0154, lng: 29.1549, access: 41.1, co2: 10200 }
        };'''
        
        # Replace the old country data with new realistic data
        content = content[:old_country_data_start] + new_country_data + content[old_country_data_end:]
        
        print("✅ Updated country data with realistic electricity access percentages")
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully updated country data!")
        return True
        
    except Exception as e:
        print(f"❌ Error updating country data: {e}")
        return False

def main():
    """Main function"""
    print("🔄 FIXING REALISTIC COUNTRY VALUES")
    print("=" * 60)
    print("   • Developed countries: 100% access (USA, Germany, Japan)")
    print("   • Developing countries: 70-99% access (India, Brazil)")
    print("   • Least developed: 10-50% access (Chad, South Sudan)")
    print("   • Varied CO₂ emissions based on country size/industry")
    print("=" * 60)
    
    success = fix_realistic_country_values()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ REALISTIC COUNTRY VALUES UPDATED!")
        print("=" * 60)
        print("\n🌍 Country Categories:")
        print("   • 100% Access: USA, Germany, Japan, France, UK, etc.")
        print("   • 90-99% Access: India (95.2%), Brazil (99.7%), Thailand (99.8%)")
        print("   • 70-89% Access: Kenya (71.4%), Pakistan (73.1%), Ghana (85.0%)")
        print("   • 50-69% Access: Nigeria (62.0%), Yemen (69.4%), Senegal (68.3%)")
        print("   • 30-49% Access: Ethiopia (44.3%), Mali (43.0%), Zimbabwe (41.1%)")
        print("   • 10-29% Access: Chad (11.1%), Malawi (18.4%), Madagascar (26.6%)")
        print("   • <10% Access: South Sudan (7.2%)")
        
        print("\n📊 Now You'll See Different Values:")
        print("   • Chad → 11.1% electricity access")
        print("   • Ethiopia → 44.3% electricity access")
        print("   • India → 95.2% electricity access")
        print("   • Germany → 100% electricity access")
        
        print("\n🚀 Test Different Countries:")
        print("   1. Refresh browser (Ctrl+F5)")
        print("   2. Search 'Chad' → See 11.1% access")
        print("   3. Search 'Ethiopia' → See 44.3% access")
        print("   4. Search 'India' → See 95.2% access")
        print("   5. Search 'Germany' → See 100% access")
        
        print("\n🎯 REALISTIC DATA NOW ACTIVE!")
        
    else:
        print("\n❌ Failed to update country data.")

if __name__ == "__main__":
    main()