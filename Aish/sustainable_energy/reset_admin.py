from django.contrib.auth.models import User

# Reset admin password
admin = User.objects.get(username='admin')
admin.set_password('admin123')
admin.is_staff = True
admin.is_superuser = True
admin.save()

print("✅ Admin password reset successfully!")
print("\n🔑 Admin Login Credentials:")
print("   Username: admin")
print("   Password: admin123")
print("\n🌐 Admin Panel URL:")
print("   http://127.0.0.1:8000/admin-login/")