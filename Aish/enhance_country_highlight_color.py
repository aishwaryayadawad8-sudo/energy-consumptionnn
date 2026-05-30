#!/usr/bin/env python3
"""Enhance country highlighting with more distinct, vibrant colors"""

# Read the file
with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update the highlight marker with more vibrant, distinct colors
old_highlight_marker = '''            // Create a larger, highlighted marker
            highlightMarker = L.circleMarker([lat, lon], {
                radius: 15,
                fillColor: '#FFD700',  // Gold color for highlight
                color: '#FF4500',      // Orange-red border
                weight: 3,
                opacity: 1,
                fillOpacity: 0.9
            }).addTo(map);'''

new_highlight_marker = '''            // Create a larger, highlighted marker with vibrant colors
            highlightMarker = L.circleMarker([lat, lon], {
                radius: 20,              // Larger size
                fillColor: '#FF1493',    // Deep Pink - very distinct!
                color: '#FFFF00',        // Bright Yellow border
                weight: 4,               // Thicker border
                opacity: 1,
                fillOpacity: 1           // Fully opaque
            }).addTo(map);'''

content = content.replace(old_highlight_marker, new_highlight_marker)

# Also update the label styling to match
old_label_css = '''        .country-highlight-label {
            background-color: #FFD700;
            border: 2px solid #FF4500;
            border-radius: 5px;
            padding: 5px 10px;
            font-weight: bold;
            font-size: 14px;
            color: #2c3e50;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }'''

new_label_css = '''        .country-highlight-label {
            background-color: #FF1493;  /* Deep Pink */
            border: 3px solid #FFFF00;  /* Bright Yellow border */
            border-radius: 8px;
            padding: 8px 15px;
            font-weight: bold;
            font-size: 16px;
            color: #FFFFFF;             /* White text */
            box-shadow: 0 4px 15px rgba(255, 20, 147, 0.6);
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        }'''

content = content.replace(old_label_css, new_label_css)

# Write back
with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Enhanced country highlighting with vibrant colors!")
print("🎨 New color scheme:")
print("   • Marker: Deep Pink (#FF1493) - Very distinct!")
print("   • Border: Bright Yellow (#FFFF00) - High contrast!")
print("   • Size: 20px radius (larger)")
print("   • Label: Pink background with yellow border")
print("   • Text: White with shadow for readability")
print("🌟 Selected country will now stand out dramatically!")
