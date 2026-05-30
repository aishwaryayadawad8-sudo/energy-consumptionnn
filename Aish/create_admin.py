"""
Create Administrator Account
Run this script to create an admin user who can send email alerts
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
    print("=" * 60)
    print("CREATE ADMINISTRATOR ACCOUNT")
    print("=" * 60)
    print()
    
    username = input("Enter admin username: ").strip()
    email = input("Enter admin email: ").strip()
    password = input("Enter admin password: ").strip()
    
    if not username or not password:
        print("\n❌ Username and password are required!")
        return
    
    try:
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            print(f"\n⚠️  User '{username}' already exists!")
            update = input("Update to admin? (yes/no): ").strip().lower()
            if update == 'yes':
                user = User.objects.get(username=username)
                user.is_staff = True
                user.is_superuser = True
                if email:
                    user.email = email
                user.set_password(password)
                user.save()
                print(f"\n✅ User '{username}' updated to administrator!")
            else:
                print("\n❌ Operation cancelled")
            return
        
        # Create new admin user
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        
        print(f"\n✅ Administrator account created successfully!")
        print(f"\nLogin credentials:")
        print(f"  Username: {username}")
        print(f"  Email: {email}")
        print(f"\n🔐 You can now login at: http://127.0.0.1:8000/admin/")
        print(f"   Or use the dashboard with admin privileges")
        
    except Exception as e:
        print(f"\n❌ Error creating admin: {e}")

if __name__ == '__main__':
    create_admin()
