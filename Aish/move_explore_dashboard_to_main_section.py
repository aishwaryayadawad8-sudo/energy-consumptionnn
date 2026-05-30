#!/usr/bin/env python3
"""
Script to move the Explore Dashboard button from navigation to main content section
"""

import os

def move_explore_dashboard_button():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the Explore Dashboard from navigation
    # Find and remove the explore dashboard nav item
    nav_explore_start = content.find('<a href="/explore/" class="nav-icon-item">')
    if nav_explore_start != -1:
        # Find the end of this nav item
        nav_explore_end = content.find('</a>', nav_explore_start)
        if nav_explore_end != -1:
            nav_explore_end += 4  # Include the </a> tag
            # Remove the nav item
            content = content[:nav_explore_start] + content[nav_explore_end:]
            print("✅ Removed Explore Dashboard from navigation")
        else:
            print("⚠️ Could not find end of explore nav item")
    else:
        print("⚠️ Explore Dashboard nav item not found")
    
    # Add Explore Dashboard button to main content section
    # Find the main content area after hero section
    main_content_start = content.find('<main class="main-content" id="main-content">')
    if main_content_start != -1:
        # Find where to insert the explore section (after main-content opening tag)
        insert_pos = content.find('>', main_content_start) + 1
        
        # Create the explore dashboard section
        explore_section = '''
        <!-- Explore Dashboard Section -->
        <section class="explore-section">
            <h2 class="explore-title">🔍 Explore Dashboard</h2>
            <p class="explore-subtitle">
                Interactive country energy analysis with search functionality, world map visualization, 
                and comprehensive energy profiles for 128+ countries with ML predictions.
            </p>
            <a href="/explore/" class="explore-btn">
                <i class="fas fa-search"></i>
                Launch Explore Dashboard
            </a>
        </section>
'''
        
        # Insert the explore section
        content = content[:insert_pos] + explore_section + content[insert_pos:]
        print("✅ Added Explore Dashboard section to main content")
    else:
        print("⚠️ Could not find main content section")
    
    # Write the updated content
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("🔄 Moving Explore Dashboard Button to Main Section")
    print("="*60)
    print("   • Removing from navigation bar")
    print("   • Adding to main content area")
    print("   • Creating prominent section")
    print()
    
    if move_explore_dashboard_button():
        print("\n✅ SUCCESS! Explore Dashboard moved to main section!")
        print("\n📋 What changed:")
        print("   1. Removed from navigation tabs")
        print("   2. Added prominent section in main content")
        print("   3. Better visibility and user experience")
        print("\n🎯 User Experience:")
        print("   • Visit /objectives/ → See prominent Explore Dashboard section")
        print("   • Click 'Launch Explore Dashboard' → Go to /explore/")
        print("   • Clean navigation with focused content")
        print("\n🔄 Refresh your browser to see the changes!")
    else:
        print("\n❌ Failed to move Explore Dashboard button")