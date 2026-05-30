#!/usr/bin/env python3
"""Fix the coordinate field names for country highlighting"""

# Read the file
with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the coordinate field names from lat/lon to latitude/longitude
old_highlight_call = '''                    // Highlight country on map if coordinates are available
                    if (data.lat && data.lon) {
                        highlightCountryOnMap(data.country, data.lat, data.lon, data.electricity_access || 0);
                    }'''

new_highlight_call = '''                    // Highlight country on map if coordinates are available
                    if (data.latitude && data.longitude) {
                        highlightCountryOnMap(data.country, data.latitude, data.longitude, data.electricity_access || 0);
                    }'''

content = content.replace(old_highlight_call, new_highlight_call)

# Write back
with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed coordinate field names!")
print("🗺️  Changed from data.lat/data.lon to data.latitude/data.longitude")
print("📍 Country highlighting should now work correctly")
