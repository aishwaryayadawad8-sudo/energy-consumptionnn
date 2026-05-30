#!/usr/bin/env python3
"""
Add support for custom email subject and message in the email alert system
"""

# Step 1: Update views.py to extract custom subject and message from request
views_update = '''
        selected_countries = body.get('countries', None)
        custom_subject = body.get('customSubject', '').strip()
        custom_message = body.get('customMessage', '').strip()
'''

# Step 2: Update the analyze_and_send_alerts call to pass custom content
views_call_update = '''
        # Send alerts with user info for logging and custom content
        alerts_sent = alert_system.analyze_and_send_alerts(
            predictions_df, 
            log_to_db=True, 
            user=request.user if request.user.is_authenticated else None,
            custom_subject=custom_subject if custom_subject else None,
            custom_message=custom_message if custom_message else None
        )
'''

print("Step 1: Update views.py")
with open('sustainable_energy/dashboard/views.py', 'r', encoding='utf-8') as f:
    views_content = f.read()

# Find and replace the selected_countries line
old_line = "        selected_countries = body.get('countries', None)"
if old_line in views_content:
    views_content = views_content.replace(
        old_line,
        views_update.strip()
    )
    print("✓ Added custom subject and message extraction")
else:
    print("✗ Could not find selected_countries line")

# Find and replace the analyze_and_send_alerts call
old_call = "        # Send alerts with user info for logging\n        alerts_sent = alert_system.analyze_and_send_alerts(predictions_df, log_to_db=True, user=request.user if request.user.is_authenticated else None)"
if old_call in views_content:
    views_content = views_content.replace(
        old_call,
        views_call_update.strip()
    )
    print("✓ Updated analyze_and_send_alerts call")
else:
    print("✗ Could not find analyze_and_send_alerts call")

with open('sustainable_energy/dashboard/views.py', 'w', encoding='utf-8') as f:
    f.write(views_content)

print("\nStep 2: Update email_alerts.py")
with open('sustainable_energy/ml_models/email_alerts.py', 'r', encoding='utf-8') as f:
    email_content = f.read()

# Update the function signature
old_sig = "    def analyze_and_send_alerts(self, predictions_df, log_to_db=True, user=None):"
new_sig = "    def analyze_and_send_alerts(self, predictions_df, log_to_db=True, user=None, custom_subject=None, custom_message=None):"

if old_sig in email_content:
    email_content = email_content.replace(old_sig, new_sig)
    print("✓ Updated function signature")
else:
    print("✗ Could not find function signature")

# Update the email generation part
old_generation = """            # Only send alerts for critical, needs_improvement, or excellent
            if status in ['critical', 'needs_improvement', 'excellent']:
                subject, body = self.generate_email_content(country, access, status, country_type, year)
                email = self.COUNTRY_EMAILS[country]"""

new_generation = """            # Only send alerts for critical, needs_improvement, or excellent
            if status in ['critical', 'needs_improvement', 'excellent']:
                # Use custom content if provided, otherwise generate automatic content
                if custom_subject or custom_message:
                    subject = custom_subject if custom_subject else f"SDG 7 Alert: {country} - {status.replace('_', ' ').title()}"
                    if custom_message:
                        body = custom_message
                    else:
                        _, body = self.generate_email_content(country, access, status, country_type, year)
                else:
                    subject, body = self.generate_email_content(country, access, status, country_type, year)
                email = self.COUNTRY_EMAILS[country]"""

if old_generation in email_content:
    email_content = email_content.replace(old_generation, new_generation)
    print("✓ Updated email generation logic")
else:
    print("✗ Could not find email generation code")

with open('sustainable_energy/ml_models/email_alerts.py', 'w', encoding='utf-8') as f:
    f.write(email_content)

print("\nStep 3: Update objective8.html to send custom content")
with open('sustainable_energy/dashboard/templates/dashboard/objective8.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Find the fetch call and update it
old_fetch = """            // Prepare request
            const requestData = {
                countries: selectedCountries
            };"""

new_fetch = """            // Prepare request
            const requestData = {
                countries: selectedCountries,
                customSubject: customSubject,
                customMessage: customMessage
            };"""

if old_fetch in html_content:
    html_content = html_content.replace(old_fetch, new_fetch)
    print("✓ Updated JavaScript to send custom content")
else:
    print("✗ Could not find fetch request data")

with open('sustainable_energy/dashboard/templates/dashboard/objective8.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("\n✅ All updates completed!")
print("\nNow users can:")
print("1. Type custom subject in the 'Email Subject' field")
print("2. Type custom message in the 'Alert Message' field")
print("3. Click 'Send Alerts' and the custom content will be sent to selected countries")
