#!/usr/bin/env python3
"""Remove Future Electricity Access Predictions section from Full Dashboard"""

# Read the file
with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the Future Predictions section
old_section = '''                
                <!-- Future Predictions -->
                <div class="chart-container">
                    <h4><i class="fas fa-crystal-ball"></i> Future Electricity Access Predictions (ML-Based)</h4>
                    <canvas id="predictionChart"></canvas>
                    <p class="text-muted mt-3" id="modelInfo"></p>
                </div>'''

new_section = ''

# Replace
content = content.replace(old_section, new_section)

# Write back
with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Future Electricity Access Predictions section removed!")
print("🗑️  Removed from Full Dashboard")
print("📄 Dashboard is now cleaner")
