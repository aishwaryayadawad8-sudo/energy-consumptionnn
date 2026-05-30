#!/usr/bin/env python3
"""
Update admin login to redirect to admin panel
"""

print("Updating admin login redirects...")
with open('sustainable_energy/dashboard/views.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Update the redirects in admin_login function
content = content.replace(
    "return redirect('objective8_dashboard')",
    "return redirect('admin_panel')"
)

with open('sustainable_energy/dashboard/views.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Updated admin login redirects to admin panel")
print("✅ Done!")
