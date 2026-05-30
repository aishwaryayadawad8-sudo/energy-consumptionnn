#!/usr/bin/env python3
"""
Fix Back to Objectives to Go Directly to Country Forecasts Page
Instead of main page, ensure it goes to the 8 objective cards page
"""

import os

def create_dedicated_country_forecasts_url():
    """Create a dedicated URL for the country forecasts page"""
    
    # First, let's add a specific URL for country forecasts
    urls_path = "sustainable_energy/dashboard/urls.py"
    
    if not os.path.exists(urls_path):
        print(f"❌ {urls_path} not found")
        return
    
    with open(urls_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if we already have a country-forecasts URL
    if 'country-forecasts/' not in content:
        # Find where to insert the new URL (after the main path)
        insert_point = content.find("path('explore/', views.index")
        
        if insert_point != -1:
            # Insert the new URL
            new_url = "    path('country-forecasts/', views.country_forecasts_page, name='country_forecasts'),\n    "
            new_content = content[:insert_point] + new_url + content[insert_point:]
            
            with open(urls_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ Added dedicated country-forecasts URL")
        else:
            print("❌ Could not find insertion point in URLs")
    else:
        print("✅ Country forecasts URL already exists")

def create_dedicated_view_function():
    """Create a dedicated view function for country forecasts"""
    
    views_path = "sustainable_energy/dashboard/views.py"
    
    if not os.path.exists(views_path):
        print(f"❌ {views_path} not found")
        return
    
    with open(views_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if we already have the country_forecasts_page function
    if 'def country_forecasts_page(request):' not in content:
        # Find where to insert the new function (after objective_selector)
        insert_point = content.find("def clean_for_json(value):")
        
        if insert_point != -1:
            new_function = '''def country_forecasts_page(request):
    """Dedicated Country Energy Forecasts page with 8 objectives"""
    response = render(request, 'dashboard/objective_selector.html')
    # Force no-cache to ensure fresh page
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache' 
    response['Expires'] = '0'
    return response

'''
            
            new_content = content[:insert_point] + new_function + content[insert_point:]
            
            with open(views_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ Added dedicated country_forecasts_page view function")
        else:
            print("❌ Could not find insertion point in views")
    else:
        print("✅ Country forecasts view function already exists")

def update_all_back_buttons():
    """Update all back buttons to use the dedicated country forecasts URL"""
    
    print("\n🔧 Updating all back buttons to use /country-forecasts/")
    
    template_dir = "sustainable_energy/dashboard/templates/dashboard/"
    
    for i in range(1, 9):
        file_path = f"{template_dir}objective{i}.html"
        
        if os.path.exists(file_path):
            print(f"🔧 Processing: {file_path}")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace all variations of back button URLs
            replacements = [
                ("window.location.href='/?objectives=true&t=", "window.location.href='/country-forecasts/?t="),
                ("window.location.href='/?objectives=true'", "window.location.href='/country-forecasts/'"),
                ("window.location.href='/'", "window.location.href='/country-forecasts/'"),
                ("href='/?objectives=true'", "href='/country-forecasts/'"),
                ("href='/'", "href='/country-forecasts/'")
            ]
            
            updated = False
            for old, new in replacements:
                if old in content:
                    content = content.replace(old, new)
                    updated = True
                    print(f"   ✅ Updated: {old} → {new}")
            
            # Handle timestamp patterns with regex
            import re
            timestamp_pattern = r"window\.location\.href='/\?objectives=true&t=(\d+)'"
            if re.search(timestamp_pattern, content):
                content = re.sub(timestamp_pattern, r"window.location.href='/country-forecasts/?t=\1'", content)
                updated = True
                print(f"   ✅ Updated timestamp pattern")
            
            if updated:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"   💾 Saved changes")
            else:
                print(f"   ✅ No changes needed")

def create_test_page():
    """Create a test page to verify the fix"""
    
    test_html = '''<!DOCTYPE html>
<html>
<head>
    <title>Country Forecasts Navigation Test</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .test-button { 
            display: inline-block; 
            padding: 15px 30px; 
            margin: 10px; 
            background: #28a745; 
            color: white; 
            text-decoration: none; 
            border-radius: 5px; 
            border: none;
            cursor: pointer;
            font-size: 16px;
        }
        .test-button:hover { background: #218838; }
        .section { margin: 30px 0; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
        .wrong { background: #dc3545; }
        .wrong:hover { background: #c82333; }
    </style>
</head>
<body>
    <h1>🔧 Country Forecasts Navigation Test</h1>
    
    <div class="section">
        <h2>✅ CORRECT Navigation (What Back Button Should Do):</h2>
        
        <button class="test-button" onclick="window.location.href='/country-forecasts/'">
            Go to Country Forecasts Page
        </button>
        
        <p><strong>Expected:</strong> Page with 8 objective cards titled "Country Energy Forecasts - All Objectives"</p>
    </div>
    
    <div class="section">
        <h2>❌ WRONG Navigation (What You Don't Want):</h2>
        
        <button class="test-button wrong" onclick="window.location.href='/'">
            Go to Main Page (Wrong)
        </button>
        
        <button class="test-button wrong" onclick="window.location.href='/explore/'">
            Go to Explore Dashboard (Wrong)
        </button>
        
        <p><strong>These should NOT be what Back to Objectives shows</strong></p>
    </div>
    
    <div class="section">
        <h2>🧪 Test Instructions:</h2>
        <ol>
            <li>Click "Go to Country Forecasts Page" above</li>
            <li>Verify you see a page with 8 objective cards</li>
            <li>Page title should be "Energy & emissions projections 2050 - EnerOutlook"</li>
            <li>You should see cards for: Total Energy, Electricity Access, Renewable Energy, etc.</li>
            <li>If this works, then "Back to Objectives" will work correctly</li>
        </ol>
    </div>
</body>
</html>'''
    
    with open('country_forecasts_test.html', 'w', encoding='utf-8') as f:
        f.write(test_html)
    
    print("✅ Created country_forecasts_test.html")

if __name__ == "__main__":
    print("🔧 Fixing Back to Objectives Navigation")
    print("Creating dedicated Country Forecasts URL to avoid main page")
    print("=" * 60)
    
    create_dedicated_country_forecasts_url()
    create_dedicated_view_function()
    update_all_back_buttons()
    create_test_page()
    
    print("\n" + "=" * 60)
    print("✅ FIXED: Back to Objectives Navigation")
    print("✅ Created: /country-forecasts/ URL")
    print("✅ Updated: All back buttons now use /country-forecasts/")
    print("✅ Created: country_forecasts_test.html for testing")
    print("")
    print("🔄 Now when you click 'Back to Objectives':")
    print("   - URL will be: /country-forecasts/")
    print("   - Page will be: Country Energy Forecasts with 8 cards")
    print("   - NO MORE: Main page or other unwanted pages")
    print("")
    print("🧪 Test by opening: country_forecasts_test.html")