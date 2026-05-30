"""
Fix script to remove all remaining static references
"""
import os
import re

template_dir = 'sustainable_energy/dashboard/templates/dashboard'
templates = [
    'index.html',
    'objective_selector.html',
    'objective1.html',
    'objective2.html',
    'objective3.html',
    'objective5.html',
    'objective5_global.html',
    'objective6.html',
    'objective7.html',
    'objective8.html',
    'send_alerts_multi.html',
    'send_custom_alert.html',
    'send_email_single.html',
    'email_logs.html',
    'admin_login.html'
]

def fix_template(filepath):
    """Remove all static references from template"""
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} - file not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remove any remaining static CSS links with various quote styles
    patterns = [
        r'\s*<link rel="stylesheet" href="{%\s*static\s*[\'"]css/electric-background\.css[\'"]\s*%}">\s*\n?',
        r'\s*<link rel="stylesheet" href="{%\s*static\s*\\[\'"]css/electric-background\.css\\[\'"]\s*%}">\s*\n?',
        r'\s*<link rel="stylesheet" href="{% static \'css/electric-background.css\' %}">\s*\n?',
        r'\s*<link rel="stylesheet" href="{% static "css/electric-background.css" %}">\s*\n?',
    ]
    
    for pattern in patterns:
        content = re.sub(pattern, '', content, flags=re.MULTILINE)
    
    # Remove {% load static %} if present
    content = content.replace('{% load static %}\n', '')
    content = content.replace('{% load static %}', '')
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {os.path.basename(filepath)}")
    else:
        print(f"No changes needed for {os.path.basename(filepath)}")

print("=" * 70)
print("Fixing Static Reference Errors")
print("=" * 70)

for template in templates:
    filepath = os.path.join(template_dir, template)
    fix_template(filepath)

print("\n" + "=" * 70)
print("Done! Restart your Django server.")
print("=" * 70)
