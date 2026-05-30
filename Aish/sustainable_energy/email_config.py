"""
Email Configuration for SDG 7 Alert System
Configure your email settings here
"""

# SMTP Configuration
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',  # For Gmail
    'smtp_port': 587,  # TLS port
    'sender_email': 'assowmya649@gmail.com',  # Your email
    'sender_password': 'pjwm rdas vswn foua',  # Gmail App Password
    'sender_name': 'SDG 7 Monitoring System'
}

# Instructions to set up Gmail:
"""
1. Go to your Google Account: https://myaccount.google.com/
2. Enable 2-Factor Authentication
3. Go to App Passwords: https://myaccount.google.com/apppasswords
4. Create a new App Password for "Mail"
5. Copy the 16-character password
6. Replace 'your-app-password' above with that password
7. Replace 'your-email@gmail.com' with your actual Gmail address

For other email providers:
- Outlook/Hotmail: smtp.office365.com, port 587
- Yahoo: smtp.mail.yahoo.com, port 587
- Custom SMTP: Contact your email provider for settings
"""

# Testing Mode - Send all emails to one dummy address
# Set to False to use actual emails from country_emails.csv
TESTING_MODE = False  # Set to False to use emails from country_emails.csv (All 128 countries → assowmya649@gmail.com)
DUMMY_EMAIL = 'assowmya649@gmail.com'  # Only used if TESTING_MODE = True

# Email Simulation Mode - DISABLED to send REAL emails
# Set ENABLE_ACTUAL_EMAIL_SENDING = True to send real emails
# Set SIMULATION_MODE = False to disable simulation
ENABLE_ACTUAL_EMAIL_SENDING = True  # ✅ ENABLED - Will send REAL emails
SIMULATION_MODE = False  # ✅ DISABLED - No simulation, real emails only
