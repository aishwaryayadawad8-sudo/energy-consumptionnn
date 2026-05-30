"""
Test Database Logging for Email Alerts
This will verify that emails are being logged to the database
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, 'sustainable_energy')
django.setup()

from dashboard.models import EmailLog
from ml_models.email_alerts import SDG7EmailAlerts
import pandas as pd

print("=" * 70)
print("🧪 Testing Database Logging for Email Alerts")
print("=" * 70)

# Step 1: Check current database
print("\n📊 Step 1: Checking Current Database")
print("-" * 70)

current_count = EmailLog.objects.count()
print(f"Current email logs in database: {current_count}")

if current_count > 0:
    print(f"\nLast 5 emails:")
    for log in EmailLog.objects.all()[:5]:
        print(f"  - {log.country}: {log.status} ({log.sent_at.strftime('%Y-%m-%d %H:%M')})")

# Step 2: Send test alerts
print("\n📧 Step 2: Sending Test Alerts")
print("-" * 70)

# Create test predictions
test_data = pd.DataFrame({
    'country': ['Kenya', 'India', 'Nigeria'],
    'year': [2024, 2024, 2024],
    'predicted_access': [45.5, 99.2, 55.3]
})

print(f"Testing with {len(test_data)} countries:")
for _, row in test_data.iterrows():
    print(f"  - {row['country']}: {row['predicted_access']}%")

# Initialize and send
alert_system = SDG7EmailAlerts()
print(f"\n📤 Sending alerts...")

alerts_sent = alert_system.analyze_and_send_alerts(test_data, log_to_db=True, user=None)

print(f"\n✅ Alerts sent: {len(alerts_sent)}")

# Step 3: Check database again
print("\n📊 Step 3: Verifying Database Logs")
print("-" * 70)

new_count = EmailLog.objects.count()
print(f"Email logs in database now: {new_count}")
print(f"New logs added: {new_count - current_count}")

if new_count > current_count:
    print(f"\n✅ SUCCESS! New emails logged to database:")
    for log in EmailLog.objects.all()[:new_count - current_count]:
        print(f"\n  Country: {log.country}")
        print(f"  Email: {log.recipient_email}")
        print(f"  Status: {log.status}")
        print(f"  Alert Type: {log.alert_type}")
        print(f"  Access: {log.electricity_access}%")
        print(f"  Year: {log.year}")
        print(f"  Subject: {log.subject[:60]}...")
        print(f"  Sent At: {log.sent_at.strftime('%Y-%m-%d %H:%M:%S')}")
else:
    print(f"\n❌ WARNING: No new logs added to database!")
    print(f"   This might indicate a database logging issue.")

# Step 4: Summary
print("\n" + "=" * 70)
print("📊 Summary")
print("=" * 70)

stats = {
    'total': EmailLog.objects.count(),
    'success': EmailLog.objects.filter(status='success').count(),
    'failed': EmailLog.objects.filter(status='failed').count(),
    'critical': EmailLog.objects.filter(alert_type='critical').count(),
    'needs_improvement': EmailLog.objects.filter(alert_type='needs_improvement').count(),
    'excellent': EmailLog.objects.filter(alert_type='excellent').count(),
}

print(f"Total Emails Logged: {stats['total']}")
print(f"  ✅ Successful: {stats['success']}")
print(f"  ❌ Failed: {stats['failed']}")
print(f"\nBy Alert Type:")
print(f"  🚨 Critical: {stats['critical']}")
print(f"  ⚠️  Needs Improvement: {stats['needs_improvement']}")
print(f"  ✅ Excellent: {stats['excellent']}")

print("\n" + "=" * 70)
print("✅ Database logging test complete!")
print("=" * 70)
print("\nTo view logs in browser:")
print("1. Start server: cd sustainable_energy && python manage.py runserver")
print("2. Visit: http://127.0.0.1:8000/email-logs/")
print("3. Login with admin credentials")
