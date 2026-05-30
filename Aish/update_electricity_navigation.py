#!/usr/bin/env python3
"""
Update the Electricity navigation icon to link to the new electricity dashboard
"""

def update_electricity_navigation():
    print("🔧 Updating Electricity navigation link...")
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    try:
        # Read the template file with proper encoding
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update the electricity navigation link
        old_link = '''<a href="{% url 'objective2_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon"><i class="fas fa-plug"></i></div>
                <div class="nav-label">Electricity</div>
            </a>'''
        
        new_link = '''<a href="{% url 'electricity_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon"><i class="fas fa-plug"></i></div>
                <div class="nav-label">Electricity</div>
            </a>'''
        
        if old_link in content:
            content = content.replace(old_link, new_link)
            
            # Write back the updated content
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ Updated Electricity navigation link successfully!")
            print("🔗 Electricity icon now links to: /electricity/")
            return True
        else:
            print("⚠️ Could not find the exact navigation link to update")
            print("🔍 Searching for alternative patterns...")
            
            # Try alternative pattern
            if 'objective2_dashboard' in content and 'fas fa-plug' in content:
                content = content.replace("{% url 'objective2_dashboard' %}", "{% url 'electricity_dashboard' %}")
                
                with open(template_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print("✅ Updated using alternative pattern!")
                return True
            else:
                print("❌ Could not find navigation link to update")
                return False
        
    except Exception as e:
        print(f"❌ Error updating navigation: {e}")
        return False

if __name__ == "__main__":
    update_electricity_navigation()