#!/usr/bin/env python3
"""Update Objective 4 to show zigzag pattern in historical chart"""

import re

# Read the current file
with open('sustainable_energy/dashboard/templates/dashboard/objective4.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the historical chart tension from 0.4 to 0 (zigzag)
# Also add point markers for better visibility
old_pattern = r"tension: 0\.4"
new_pattern = "tension: 0,  // Zigzag pattern (sharp angles)\n                                    pointRadius: 5,  // Show data points\n                                    pointHoverRadius: 7  // Larger on hover"

content = re.sub(old_pattern, new_pattern, content)

# Write back
with open('sustainable_energy/dashboard/templates/dashboard/objective4.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Updated objective4.html")
print("   - Historical chart: Changed to zigzag pattern (tension: 0)")
print("   - Added point markers for better visibility")
print("\n📋 Changes:")
print("   Before: tension: 0.4 (smooth curves)")
print("   After:  tension: 0 (zigzag/sharp angles)")
print("           pointRadius: 5 (visible data points)")
print("           pointHoverRadius: 7 (larger on hover)")
