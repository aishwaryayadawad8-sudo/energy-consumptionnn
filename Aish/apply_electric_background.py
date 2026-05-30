"""
Script to apply the electric lightning background to all templates
"""
import os
import re

# Template files to update
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

def update_template(filepath):
    """Update a template file to use the electric background"""
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} - file not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has the static load
    if '{% load static %}' in content:
        print(f"✓ {filepath} already has static load")
    else:
        # Add {% load static %} after <title> tag
        content = re.sub(
            r'(<title>.*?</title>)',
            r'\1\n    {% load static %}',
            content,
            count=1
        )
        print(f"✓ Added static load to {filepath}")
    
    # Check if already has the CSS link
    if 'electric-background.css' in content:
        print(f"✓ {filepath} already has electric background CSS")
    else:
        # Add CSS link before </head>
        content = re.sub(
            r'(</head>)',
            r'    <link rel="stylesheet" href="{% static \'css/electric-background.css\' %}">\n\1',
            content,
            count=1
        )
        print(f"✓ Added electric background CSS to {filepath}")
    
    # Update body tag to include electric-bg class
    if 'class="electric-bg"' in content or 'class=\'electric-bg\'' in content:
        print(f"✓ {filepath} already has electric-bg class")
    else:
        # Add electric-bg class to body tag
        content = re.sub(
            r'<body([^>]*)>',
            r'<body\1 class="electric-bg">',
            content,
            count=1
        )
        # Clean up if there was already a class attribute
        content = re.sub(
            r'<body class="([^"]*)" class="electric-bg">',
            r'<body class="\1 electric-bg">',
            content
        )
        print(f"✓ Added electric-bg class to {filepath}")
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("=" * 60)
print("Applying Electric Lightning Background to Templates")
print("=" * 60)

for template in templates:
    filepath = os.path.join(template_dir, template)
    print(f"\nProcessing: {template}")
    update_template(filepath)

print("\n" + "=" * 60)
print("✅ Background application complete!")
print("=" * 60)
print("\nNext steps:")
print("1. Save your electric lightning image as:")
print("   sustainable_energy/static/images/electric-lightning.jpg")
print("2. Restart your Django server")
print("3. Clear browser cache and refresh")
