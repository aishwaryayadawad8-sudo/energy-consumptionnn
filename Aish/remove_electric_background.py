"""
Script to remove the electric lightning background and restore original
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

def remove_background(filepath):
    """Remove electric background from template"""
    if not os.path.exists(filepath):
        print(f"❌ Skipping {filepath} - file not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove {% load static %} if it exists
    if '{% load static %}' in content:
        content = content.replace('{% load static %}\n', '')
        content = content.replace('{% load static %}', '')
        print("✓ Removed load static from " + os.path.basename(filepath))
    
    # Remove electric-background.css link
    if 'electric-background.css' in content:
        # Remove the entire link tag
        content = re.sub(
            r'\s*<link rel="stylesheet" href="{%\s*static\s*[\'"]css/electric-background\.css[\'"]\s*%}">\n?',
            '',
            content
        )
        print(f"✓ Removed electric background CSS from {os.path.basename(filepath)}")
    
    # Remove electric-bg class from body tag
    if 'electric-bg' in content:
        content = re.sub(
            r'<body([^>]*)\s+class="electric-bg"([^>]*)>',
            r'<body\1\2>',
            content
        )
        content = re.sub(
            r'<body([^>]*)class="([^"]*)\s*electric-bg\s*([^"]*)"([^>]*)>',
            r'<body\1class="\2\3"\4>',
            content
        )
        print(f"✓ Removed electric-bg class from {os.path.basename(filepath)}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("=" * 70)
print("Removing Electric Lightning Background from All Templates")
print("=" * 70)

for template in templates:
    filepath = os.path.join(template_dir, template)
    print(f"\nProcessing: {template}")
    remove_background(filepath)

print("\n" + "=" * 70)
print("✅ Electric background removed from all templates!")
print("=" * 70)
print("\nOriginal gradient backgrounds restored.")
print("Restart your Django server to see the changes.")
