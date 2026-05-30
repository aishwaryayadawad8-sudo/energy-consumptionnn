#!/usr/bin/env python3

# Add admin panel view to views.py

view_code = '''
@login_required(login_url='/admin-login/')
def admin_panel(request):
    """Admin Panel - Email Alert System Management"""
    if not request.user.is_staff:
        return redirect('admin_login')
    return render(request, 'dashboard/admin_panel.html', {
        'user': request.user
    })
'''

# Read the views file
with open('sustainable_energy/dashboard/views.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the position to insert (after admin_logout function)
insert_marker = "def admin_logout(request):\n    \"\"\"Admin logout\"\"\"\n    logout(request)\n    return redirect('admin_login')"

if insert_marker in content:
    # Insert the new view after admin_logout
    content = content.replace(
        insert_marker,
        insert_marker + '\n' + view_code
    )
    
    # Write back
    with open('sustainable_energy/dashboard/views.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Added admin_panel view to views.py")
else:
    print("✗ Could not find insertion point in views.py")
