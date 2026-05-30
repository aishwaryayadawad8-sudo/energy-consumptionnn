#!/usr/bin/env python3
"""
Reset admin password for the SDG 7 project
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append('sustainable_energy')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sustainable_energy.settings')

# Setup Django
django.setup()

from django.contrib.auth.models import User

def reset_admin_password():
    try:
        # Get or create admin user
        admin, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@sdg7.com',
                'is_staff': True,
                'is_superuser': True,
                'first_name': 'Admin',
                'last_name': 'User'
            }
        )
        
        # Set password to 'admin123'
        admin.set_password('admin123')
        admin.is_staff = True
        admin.is_superuser = True
        admin.save()
        
        if created:
            print("✅ Admin user created successfully!")
        else:
            print("✅ Admin user password updated successfully!")
            
        print("\n🔑 Admin Login Credentials:")
        print("   Username: admin")
        print("   Password: admin123")
        print("\n🌐 Admin Panel URL:")
        print("   http://127.0.0.1:8000/admin-login/")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    reset_admin_password()