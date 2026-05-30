#!/usr/bin/env python3
"""
Add @csrf_exempt decorator to send_xgboost_alerts
"""

print("🔧 Adding @csrf_exempt decorator...")

with open('sustainable_energy/dashboard/views.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add @csrf_exempt before the function
old_line = "def send_xgboost_alerts(request):"
new_line = "@csrf_exempt\ndef send_xgboost_alerts(request):"

if old_line in content and "@csrf_exempt" not in content.split(old_line)[0].split('\n')[-5:]:
    content = content.replace(old_line, new_line)
    print("✅ Added @csrf_exempt decorator")
else:
    print("⚠️ @csrf_exempt already exists or function not found")

with open('sustainable_energy/dashboard/views.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Done!")