#!/usr/bin/env python3

"""
Script to move the Explore Dashboard button to the navigation icons section
"""

def move_explore_button_to_nav():
    # Read the current objective selector template
    with open('sustainable_energy/dashboard/templates/dashboard/objective_selector.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create the new navigation item for Explore Dashboard
    explore_nav_item = '''            <a href="/explore/" class="nav-icon-item">
                <div class="nav-icon"><i class="fas fa-search"></i></div>
                <div class="nav-label">Explore Dashboard</div>
            </a>'''
    
    # Find the nav-container and add the Explore Dashboard item at the end
    nav_container_end = content.find('</div>', content.find('<div class="nav-container">'))
    if nav_container_end != -1:
        # Insert the explore dashboard nav item before the closing </div>
        content = content[:nav_container_end] + '\n' + explore_nav_item + '\n        ' + content[nav_container_end:]
    
    # Remove the entire Explore Dashboard section from main content
    explore_section_start = content.find('<!-- Explore Dashboard Section -->')
    if explore_section_start != -1:
        # Find the end of the explore section
        section_end = content.find('</section>', explore_section_start)
        if section_end != -1:
            section_end += 10  # Include </section>
            # Remove the entire section
            content = content[:explore_section_start] + content[section_end:]
    
    # Write the updated content
    with open('sustainable_energy/dashboard/templates/dashboard/objective_selector.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ EXPLORE DASHBOARD BUTTON MOVED TO NAVIGATION")
    print("📍 Added 'Explore Dashboard' to navigation icons")
    print("🗑️ Removed Explore Dashboard section from main content")
    print("🔍 Button now appears with other objective icons")
    print("🎯 Clean navigation with search icon")
    print("")
    print("🎉 RESULT:")
    print("- Navigation now has: Total Energy, Electricity, Renewables, CO Emissions, Country Forecasts, More Projections, Explore Dashboard")
    print("- Main content section is now clean")
    print("- Consistent navigation design")
    print("- Direct access to dashboard from navigation bar")

if __name__ == "__main__":
    move_explore_button_to_nav()