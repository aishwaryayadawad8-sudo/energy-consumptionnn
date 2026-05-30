#!/usr/bin/env python3
"""
Fix indentation and key names in views.py
"""

print("Fixing views.py...")
with open('sustainable_energy/dashboard/views.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the indentation and key names
old_code = """        
selected_countries = body.get('countries', None)
        custom_subject = body.get('customSubject', '').strip()
        custom_message = body.get('customMessage', '').strip()"""

new_code = """        
        selected_countries = body.get('countries', None)
        custom_subject = body.get('custom_subject', '').strip()
        custom_message = body.get('custom_message', '').strip()"""

if old_code in content:
    content = content.replace(old_code, new_code)
    print("✓ Fixed indentation and key names")
else:
    print("✗ Pattern not found, trying alternative...")
    # Try without the leading whitespace
    old_code2 = """selected_countries = body.get('countries', None)
        custom_subject = body.get('customSubject', '').strip()
        custom_message = body.get('customMessage', '').strip()"""
    
    new_code2 = """        selected_countries = body.get('countries', None)
        custom_subject = body.get('custom_subject', '').strip()
        custom_message = body.get('custom_message', '').strip()"""
    
    if old_code2 in content:
        content = content.replace(old_code2, new_code2)
        print("✓ Fixed with alternative pattern")
    else:
        print("✗ Could not find pattern")

with open('sustainable_energy/dashboard/views.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Done!")
