#!/usr/bin/env python3
"""
Add admin panel URL to urls.py
"""

print("Adding admin panel URL...")
with open('sustainable_energy/dashboard/urls.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the admin panel URL after admin-logout
old_line = "    path('admin-logout/', views.admin_logout, name='admin_logout'),"
new_lines = """    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),"""

if old_line in content and "path('admin-panel/'," not in content:
    content = content.replace(old_line, new_lines)
    print("✓ Added admin panel URL")
else:
    print("✗ URL already exists or pattern not found")

with open('sustainable_energy/dashboard/urls.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Done!")
