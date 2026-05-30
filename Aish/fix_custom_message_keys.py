#!/usr/bin/env python3
"""
Fix the key names to match between frontend and backend
"""

print("Fixing key names in views.py...")
with open('sustainable_energy/dashboard/views.py', 'r', encoding='utf-8') as f:
    content = f.read()

# The frontend sends: custom_subject and custom_message
# Update the backend to match
old_keys = """        selected_countries = body.get('countries', None)
        custom_subject = body.get('customSubject', '').strip()
        custom_message = body.get('customMessage', '').strip()"""

new_keys = """        selected_countries = body.get('countries', None)
        custom_subject = body.get('custom_subject', '').strip()
        custom_message = body.get('custom_message', '').strip()"""

if old_keys in content:
    content = content.replace(old_keys, new_keys)
    print("✓ Fixed key names to match frontend")
else:
    print("✗ Could not find key extraction code")

with open('sustainable_energy/dashboard/views.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Done!")
