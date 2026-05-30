#!/usr/bin/env python3
"""Delete the Send Email Alerts bar from Full Dashboard"""

# Read the file
with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the Email Alert Section
old_section = '''        
        <!-- Email Alert Section -->
        <div class="search-section">
            <h3 class="mb-4"><i class="fas fa-envelope"></i> Send Email Alerts to Countries</h3>
            <p class="text-muted">All emails will be sent to your configured dummy email address for testing</p>
            <div class="text-center">
                <button class="btn btn-warning btn-lg" onclick="sendEmailAlerts()" id="sendAlertsBtn">
                    <i class="fas fa-paper-plane"></i> Send Email Alerts to All Countries
                </button>
            </div>
            <div id="emailAlertResults" class="mt-4"></div>
        </div>
        '''

new_section = '''        '''

# Replace
content = content.replace(old_section, new_section)

# Write back
with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Send Email Alerts bar deleted from Full Dashboard!")
print("🗑️  Removed from index.html")
print("📄 Dashboard is now cleaner")
