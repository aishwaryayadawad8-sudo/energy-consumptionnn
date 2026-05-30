#!/usr/bin/env python3
"""Delete the Send Custom Alert section from objective selector"""

# Read the current file
with open('sustainable_energy/dashboard/templates/dashboard/objective_selector.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and remove the Send Custom Alert section
old_section = '''
            <!-- Send Custom Alert -->
            <div class="col-md-6">
                <div class="objective-card" onclick="window.location.href='/send-custom-alert/'">
                    <div class="objective-icon">
                        <i class="fas fa-edit"></i>
                    </div>
                    <div class="objective-title">✍️ Send Custom Alert</div>
                    <div class="objective-description">
                        Write your own custom message to send to a country
                    </div>
                    <div class="objective-features">
                        <ul>
                            <li><i class="fas fa-check-circle text-success"></i> Select country</li>
                            <li><i class="fas fa-check-circle text-success"></i> Write custom message</li>
                            <li><i class="fas fa-check-circle text-success"></i> Message templates</li>
                        </ul>
                    </div>
                    <button class="btn btn-objective">
                        Write Custom Alert <i class="fas fa-pen"></i>
                    </button>
                </div>
            </div>'''

new_section = ''

# Replace the section (remove it)
content = content.replace(old_section, new_section)

# Write back
with open('sustainable_energy/dashboard/templates/dashboard/objective_selector.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Send Custom Alert section deleted!")
print("🗑️  Removed from home page")
print("📄 File updated: objective_selector.html")
