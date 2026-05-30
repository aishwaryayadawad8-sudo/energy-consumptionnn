#!/usr/bin/env python3
"""Update send functions to include custom subject and message"""

# Read the file
with open('sustainable_energy/dashboard/templates/dashboard/objective8.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the sendAlerts function to include custom fields
old_send_function = '''        // Send alerts (main function)
        function sendAlerts(countries) {
            // Show loading
            $('#loading').addClass('active');
            $('#results').hide();
            
            // Prepare request
            const url = '/api/send-email-alerts-selected/';
            const data = {
                countries: countries
            };'''

new_send_function = '''        // Send alerts (main function)
        function sendAlerts(countries) {
            // Show loading
            $('#loading').addClass('active');
            $('#results').hide();
            
            // Get custom subject and message (if provided)
            const customSubject = $('#emailSubject').val().trim();
            const customMessage = $('#alertMessage').val().trim();
            
            // Prepare request
            const url = '/api/send-email-alerts-selected/';
            const data = {
                countries: countries,
                custom_subject: customSubject || null,
                custom_message: customMessage || null
            };'''

# Replace
content = content.replace(old_send_function, new_send_function)

# Write back
with open('sustainable_energy/dashboard/templates/dashboard/objective8.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Send functions updated!")
print("📧 Custom subject and message will now be included in email alerts")
