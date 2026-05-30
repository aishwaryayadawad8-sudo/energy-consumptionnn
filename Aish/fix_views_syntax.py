#!/usr/bin/env python3
"""
Fix syntax error in views.py
"""

print("🔧 Fixing syntax error in views.py...")

with open('sustainable_energy/dashboard/views.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the misplaced import statements
fixes = [
    # Fix 1: Remove the wrongly placed import in send_email_alerts
    ("        from ml_models.sdg7_forecasting import SDG7Forecasting\nfrom new_energy_adapter import NewEnergyDataAdapter",
     "        from ml_models.sdg7_forecasting import SDG7Forecasting\n        from new_energy_adapter import NewEnergyDataAdapter"),
    
    # Fix 2: Remove the wrongly placed import in send_email_alerts_selected
    ("        from ml_models.sdg7_forecasting import SDG7Forecasting\nfrom new_energy_adapter import NewEnergyDataAdapter",
     "        from ml_models.sdg7_forecasting import SDG7Forecasting\n        from new_energy_adapter import NewEnergyDataAdapter"),
]

for old, new in fixes:
    if old in content:
        content = content.replace(old, new)
        print("✅ Fixed import indentation")

# Also remove any duplicate imports at the top level that might be wrong
lines = content.split('\n')
fixed_lines = []
in_function = False
indent_level = 0

for line in lines:
    # Skip standalone imports of NewEnergyDataAdapter that are not properly indented
    if line.strip() == "from new_energy_adapter import NewEnergyDataAdapter" and not line.startswith('    '):
        print(f"⚠️ Skipping misplaced import: {line}")
        continue
    
    fixed_lines.append(line)

content = '\n'.join(fixed_lines)

with open('sustainable_energy/dashboard/views.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed views.py syntax errors")