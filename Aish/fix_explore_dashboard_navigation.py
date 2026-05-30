#!/usr/bin/env python3
"""
Script to fix the Explore Dashboard button in the navigation section
"""

import os

def fix_explore_dashboard_navigation():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the broken navigation structure
    # Find the broken nav item (first one with missing closing div)
    broken_nav_start = content.find('<a href="{% url \'objective1_dashboard\' %}" class="nav-icon-item">')
    if broken_nav_start != -1:
        # Find the end of this broken nav item
        broken_nav_end = content.find('</a>', broken_nav_start)
        if broken_nav_end != -1:
            broken_nav_end += 4  # Include the </a> tag
            
            # Replace the broken nav item with fixed version
            fixed_nav_item = '''<a href="{% url 'objective1_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon"><i class="fas fa-bolt"></i></div>
                <div class="nav-label">Total Energy</div>
            </a>
            <a href="/explore/" class="nav-icon-item">
                <div class="nav-icon"><i class="fas fa-search"></i></div>
                <div class="nav-label">Explore Dashboard</div>
            </a>'''
            
            content = content[:broken_nav_start] + fixed_nav_item + content[broken_nav_end:]
            print("✅ Fixed broken navigation structure")
            print("✅ Added Explore Dashboard to navigation")
        else:
            print("⚠️ Could not find end of broken nav item")
    else:
        print("⚠️ Broken nav item not found")
    
    # Remove the explore section from main content since it's now in navigation
    explore_section_start = content.find('        <!-- Explore Dashboard Section -->')
    if explore_section_start != -1:
        explore_section_end = content.find('        </section>', explore_section_start)
        if explore_section_end != -1:
            explore_section_end = content.find('\n', explore_section_end) + 1
            content = content[:explore_section_start] + content[explore_section_end:]
            print("✅ Removed duplicate Explore Dashboard section from main content")
    
    # Write the updated content
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("🔧 Fixing Explore Dashboard Button in Navigation")
    print("="*60)
    print("   • Fixing broken navigation structure")
    print("   • Adding Explore Dashboard to navigation bar")
    print("   • Removing duplicate section from main content")
    print()
    
    if fix_explore_dashboard_navigation():
        print("\n✅ SUCCESS! Explore Dashboard navigation fixed!")
        print("\n📋 What was fixed:")
        print("   1. Fixed broken navigation HTML structure")
        print("   2. Added Explore Dashboard to navigation bar")
        print("   3. Removed duplicate section from main content")
        print("   4. Clean, consistent navigation layout")
        print("\n🎯 Navigation now includes:")
        print("   • Total Energy")
        print("   • Explore Dashboard")
        print("   • Electricity")
        print("   • Renewables")
        print("   • CO Emissions")
        print("   • Country Forecasts")
        print("   • More Projections")
        print("\n🔄 Refresh your browser to see the fixed navigation!")
    else:
        print("\n❌ Failed to fix Explore Dashboard navigation")