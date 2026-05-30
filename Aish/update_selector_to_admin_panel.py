#!/usr/bin/env python3
"""
Update objective selector to link to admin panel
"""

print("Updating objective_selector.html...")
with open('sustainable_energy/dashboard/templates/dashboard/objective_selector.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update the onclick function
old_function = """            function openEmailAlertSystem() {
                // Try the protected route first
                window.location.href = '/objective8/';
                
                // If that doesn't work after 2 seconds, show instructions
                setTimeout(function() {
                    if (window.location.pathname === '/') {
                        alert('Email Alert System requires server restart.\\n\\nPlease:\\n1. Stop Django server (Ctrl+C)\\n2. Start again: python manage.py runserver\\n3. Try again');
                    }
                }, 2000);
            }"""

new_function = """            function openEmailAlertSystem() {
                // Redirect to admin panel (requires login)
                window.location.href = '/admin-panel/';
            }"""

if old_function in content:
    content = content.replace(old_function, new_function)
    print("✓ Updated function to redirect to admin panel")
else:
    print("✗ Could not find function")

# Update the title
old_title = """                    <div class="objective-title">📧 Email Alert System (Multiple)</div>"""
new_title = """                    <div class="objective-title">🔐 Admin Panel - Email Alert System</div>"""

if old_title in content:
    content = content.replace(old_title, new_title)
    print("✓ Updated title")
else:
    print("✗ Could not find title")

# Update description
old_desc = """                    <div class="objective-description">
                        Send electricity access alerts to multiple countries at once
                    </div>"""

new_desc = """                    <div class="objective-description">
                        Admin panel for managing email alerts and monitoring system
                    </div>"""

if old_desc in content:
    content = content.replace(old_desc, new_desc)
    print("✓ Updated description")
else:
    print("✗ Could not find description")

with open('sustainable_energy/dashboard/templates/dashboard/objective_selector.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Done!")
