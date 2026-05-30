#!/usr/bin/env python3
"""Change pin marker and country highlight from pink to olive green"""

# Read the file
with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all pink (#FF1493) with olive green (#98BF64)
content = content.replace('#FF1493', '#98BF64')

# Also replace yellow (#FFFF00) with a darker green for better contrast
content = content.replace('#FFFF00', '#2E7D32')

# Write back
with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Changed highlight colors to green!")
print("🎨 Color changes:")
print("   • Pin marker: Olive Green (#98BF64)")
print("   • Border: Dark Green (#2E7D32)")
print("   • Country boundary: Olive Green (#98BF64)")
print("   • Label background: Olive Green (#98BF64)")
print("   • All pink replaced with green!")
