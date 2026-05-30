"""
Fix script to ensure all templates have the electric background CSS link
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
    """Ensure template has the CSS link in the right place"""
    if not os.path.exists(filepath):
        print(f"❌ Skipping {filepath} - file not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if CSS link already exists
    if "electric-background.css" in content:
        print(f"✓ {os.path.basename(filepath)} - Already has CSS link")
        return
    
    # Find the last stylesheet link before </head> or <style>
    # Insert our CSS link right before <style> or </head>
    if '<style>' in content:
        # Insert before <style>
        content = content.replace(
            '<style>',
            '<link rel="stylesheet" href="{% static \'css/electric-background.css\' %}">\n    <style>',
            1
        )
        print(f"✓ {os.path.basename(filepath)} - Added CSS link before <style>")
    elif '</head>' in content:
        # Insert before </head>
        content = content.replace(
            '</head>',
            '    <link rel="stylesheet" href="{% static \'css/electric-background.css\' %}">\n</head>',
            1
        )
        print(f"✓ {os.path.basename(filepath)} - Added CSS link before </head>")
    else:
        print(f"⚠️  {os.path.basename(filepath)} - Could not find insertion point")
        return
    
    # Ensure {% load static %} exists
    if '{% load static %}' not in content:
        # Add after <title> tag
        content = re.sub(
            r'(</title>)',
            r'\1\n    {% load static %}',
            content,
            count=1
        )
        print("  + Added {% load static %}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("=" * 70)
print("Fixing Electric Background CSS Links in All Templates")
print("=" * 70)

for template in templates:
    filepath = os.path.join(template_dir, template)
    fix_template(filepath)

print("\n" + "=" * 70)
print("✅ All templates updated!")
print("=" * 70)
