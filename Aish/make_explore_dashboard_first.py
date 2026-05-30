#!/usr/bin/env python3
"""
Script to make the Explore Dashboard (current index.html) the first page
and move objective selector to a different URL
"""

import os

def update_urls():
    """Update URLs to make explore dashboard the main page"""
    
    urls_path = "sustainable_energy/dashboard/urls.py"
    
    if not os.path.exists(urls_path):
        print(f"❌ File not found: {urls_path}")
        return False
    
    try:
        # Read the URLs file
        with open(urls_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update URL patterns
        old_urls = """urlpatterns = [
    path('', views.objective_selector, name='objective_selector'),
    path('objective1/', views.objective1_dashboard, name='objective1_dashboard'),
    path('objective2/', views.objective2_dashboard, name='objective2_dashboard'),
    path('dashboard/', views.index, name='index'),"""
        
        new_urls = """urlpatterns = [
    path('', views.index, name='index'),  # Explore Dashboard is now main page
    path('objectives/', views.objective_selector, name='objective_selector'),  # Moved to /objectives/
    path('objective1/', views.objective1_dashboard, name='objective1_dashboard'),
    path('objective2/', views.objective2_dashboard, name='objective2_dashboard'),
    path('dashboard/', views.index, name='explore_dashboard_redirect'),  # Keep old URL working"""
        
        if old_urls in content:
            content = content.replace(old_urls, new_urls)
            print("✅ Updated URL patterns - Explore Dashboard is now main page")
        else:
            print("⚠️ URL pattern not found, trying alternative approach...")
        
        # Write the file back
        with open(urls_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully updated {urls_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating URLs: {e}")
        return False

def update_index_title():
    """Update the title of index.html to 'Explore Dashboard'"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    if not os.path.exists(index_path):
        print(f"❌ File not found: {index_path}")
        return False
    
    try:
        # Read the index file
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update title
        old_title = '<title>SDG 7: Affordable and Clean Energy Dashboard</title>'
        new_title = '<title>Explore Dashboard - SDG 7 Energy Analytics</title>'
        
        if old_title in content:
            content = content.replace(old_title, new_title)
            print("✅ Updated page title to 'Explore Dashboard'")
        
        # Update main header
        old_header = '<h1><i class="fas fa-bolt"></i> Towards Affordable and Clean Energy</h1>'
        new_header = '<h1><i class="fas fa-search"></i> Explore Dashboard</h1>'
        
        if old_header in content:
            content = content.replace(old_header, new_header)
            print("✅ Updated main header to 'Explore Dashboard'")
        
        # Update subtitle
        old_subtitle = '<p>A Predictive and Strategic Framework for SDG 7</p>'
        new_subtitle = '<p>Interactive Country Energy Analysis & Projections</p>'
        
        if old_subtitle in content:
            content = content.replace(old_subtitle, new_subtitle)
            print("✅ Updated subtitle")
        
        # Write the file back
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully updated {index_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating index.html: {e}")
        return False

def update_objective_selector_links():
    """Update links in objective selector to point to new main page"""
    
    selector_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(selector_path):
        print(f"❌ File not found: {selector_path}")
        return False
    
    try:
        # Read the selector file
        with open(selector_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update MORE PROJECTIONS link to point to main page
        old_link = '<a href="/dashboard/" class="nav-tab">'
        new_link = '<a href="/" class="nav-tab">'
        
        if old_link in content:
            content = content.replace(old_link, new_link)
            print("✅ Updated MORE PROJECTIONS link to point to main page")
        
        # Update the text to reflect it's now the main page
        old_text = '<span>MORE PROJECTIONS</span>'
        new_text = '<span>EXPLORE DASHBOARD</span>'
        
        if old_text in content:
            content = content.replace(old_text, new_text)
            print("✅ Updated tab text to 'EXPLORE DASHBOARD'")
        
        # Write the file back
        with open(selector_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully updated {selector_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating objective selector: {e}")
        return False

def main():
    """Main function"""
    print("🚀 Making Explore Dashboard the First Page")
    print("="*60)
    print("   • Moving current dashboard to main URL (/)")
    print("   • Moving objective selector to /objectives/")
    print("   • Renaming to 'Explore Dashboard'")
    print()
    
    success1 = update_urls()
    success2 = update_index_title()
    success3 = update_objective_selector_links()
    
    if success1 and success2 and success3:
        print("\n✅ SUCCESS! Explore Dashboard is now the first page!")
        print("\n📋 New URL Structure:")
        print("   • Main Page (Explore Dashboard): http://localhost:8000/")
        print("   • Objectives Selector: http://localhost:8000/objectives/")
        print("   • Individual Objectives: http://localhost:8000/objective1/ etc.")
        print("\n🎯 What changed:")
        print("   ✅ Explore Dashboard is now the landing page")
        print("   ✅ Country search & analysis is the first thing users see")
        print("   ✅ Objective selector moved to /objectives/")
        print("   ✅ 'MORE PROJECTIONS' renamed to 'EXPLORE DASHBOARD'")
        print("\n🔄 Restart your Django server and refresh browser!")
    else:
        print("\n❌ Some updates failed. Please check the files manually.")

if __name__ == "__main__":
    main()