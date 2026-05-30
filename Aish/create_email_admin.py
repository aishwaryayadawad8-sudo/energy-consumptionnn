"""
Create Admin User for Email Alert System
Run this script to create an admin account
"""
import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sustainable_energy.config.settings')
django.setup()

from django.contrib.auth.models import User

def create_admin():
    print("\n" + "="*60)
    print("Create Admin User for Email Alert System")
    print("="*60)
    print()
    
    # Get admin details
    username = input("Enter admin username (default: admin): ").strip() or "admin"
    email = input("Enter admin email (default: admin@sdg7.org): ").strip() or "admin@sdg7.org"
    
    # Get password
    import getpass
    while True:
        password = getpass.getpass("Enter admin password: ")
        password_confirm = getpass.getpass("Confirm password: ")
        
        if password == password_confirm:
            if len(password) < 8:
                print("❌ Password must be at least 8 characters long")
                continue
            break
        else:
            print("❌ Passwords don't match. Try again.")
    
    print()
    print("Creating admin user...")
    
    try:
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            print(f"⚠️  User '{username}' already exists!")
            response = input("Do you want to update the password? (yes/no): ").strip().lower()
            
            if response in ['yes', 'y']:
                user = User.objects.get(username=username)
                user.set_password(password)
                user.is_staff = True
                user.is_superuser = True
                user.email = email
                user.save()
                print(f"✅ Password updated for user '{username}'")
            else:
                print("❌ Operation cancelled")
                return
        else:
            # Create new user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.is_staff = True
            user.is_superuser = True
            user.save()
            print(f"✅ Admin user '{username}' created successfully!")
        
        print()
        print("="*60)
        print("Admin Account Details:")
        print("="*60)
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Password: {'*' * len(password)}")
        print()
        print("You can now login at:")
        print("http://127.0.0.1:8000/admin-login/")
        print()
        print("="*60)
        
    except Exception as e:
        print(f"❌ Error creating admin user: {e}")

if __name__ == '__main__':
    create_admin()
