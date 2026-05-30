#!/usr/bin/env python3
"""Delete the Send Alerts (Multi-Select) section from objective selector"""

# Read the current file
with open('sustainable_energy/dashboard/templates/dashboard/objective_selector.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and remove the Send Alerts Multi-Select section
old_section = '''            <!-- Send Alerts to Multiple Countries -->
            <div class="col-md-6">
                <div class="objective-card" onclick="window.location.href='/send-alerts-multi/'">
                    <div class="objective-icon">
                        <i class="fas fa-paper-plane"></i>
                    </div>
                    <div class="objective-title">📧 Send Alerts (Multi-Select)</div>
                    <div class="objective-description">
                        Select multiple countries and send alerts to each
                    </div>
                    <div class="objective-features">
                        <ul>
                            <li><i class="fas fa-check-circle text-success"></i> Multi-select countries</li>
                            <li><i class="fas fa-check-circle text-success"></i> Auto-generated alerts</li>
                            <li><i class="fas fa-check-circle text-success"></i> Send to all option</li>
                        </ul>
                    </div>
                    <button class="btn btn-objective">
                        Send to Multiple <i class="fas fa-paper-plane"></i>
                    </button>
                </div>
            </div>
            '''

new_section = ''

# Replace the section (remove it)
content = content.replace(old_section, new_section)

# Write back
with open('sustainable_energy/dashboard/templates/dashboard/objective_selector.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Send Alerts (Multi-Select) section deleted!")
print("🗑️  Removed from home page")
print("📄 File updated: objective_selector.html")
