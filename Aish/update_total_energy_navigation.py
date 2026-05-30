#!/usr/bin/env python3
"""
Update the Total Energy navigation icon to link to the new dashboard
"""

def update_total_energy_navigation():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Updating Total Energy navigation link...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and update the Total Energy navigation link
        old_nav_link = '''            <a href="{% url 'objective1_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon"><i class="fas fa-bolt"></i></div>
                <div class="nav-label">Total Energy</div>
            </a>'''
        
        new_nav_link = '''            <a href="{% url 'total_energy_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon"><i class="fas fa-bolt"></i></div>
                <div class="nav-label">Total Energy</div>
            </a>'''
        
        if old_nav_link in content:
            content = content.replace(old_nav_link, new_nav_link)
            print("✅ Updated Total Energy navigation link")
        else:
            # Try alternative pattern
            alt_pattern = '''<a href="{% url 'objective1_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon"><i class="fas fa-bolt"></i></div>
                <div class="nav-label">Total Energy</div>
            </a>'''
            
            alt_replacement = '''<a href="{% url 'total_energy_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon"><i class="fas fa-bolt"></i></div>
                <div class="nav-label">Total Energy</div>
            </a>'''
            
            if alt_pattern in content:
                content = content.replace(alt_pattern, alt_replacement)
                print("✅ Updated Total Energy navigation link (alternative pattern)")
            else:
                print("⚠️  Could not find exact navigation pattern to update")
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Total Energy navigation updated successfully!")
        print("🔗 Total Energy icon now links to comprehensive dashboard")
        print("📊 Users can access all energy statistics via the navigation")
        
        return True
        
    except Exception as e:
        print(f"❌ Error updating navigation: {e}")
        return False

if __name__ == "__main__":
    update_total_energy_navigation()