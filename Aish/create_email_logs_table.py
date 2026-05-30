"""
Script to create email logs database table
Run this after creating the model
"""
import os
import sys
import django

# Add sustainable_energy to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sustainable_energy'))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.management import call_command

print("Creating migrations for email logs...")
call_command('makemigrations', 'dashboard')

print("\nApplying migrations...")
call_command('migrate')

print("\n✅ Email logs table created successfully!")
print("\nYou can now:")
print("1. Access the email logs at: http://127.0.0.1:8000/email-logs/")
print("2. Send emails from: http://127.0.0.1:8000/objective8/")
print("3. All sent emails will be logged automatically")
