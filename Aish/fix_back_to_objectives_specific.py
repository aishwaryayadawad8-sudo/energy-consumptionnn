#!/usr/bin/env python3
"""
Fix Back to Objectives to be More Specific
Make sure it goes to the exact objectives page
"""

import os
import time

def update_back_buttons_to_be_specific():
    """Update back buttons to be more specific about going to objectives page"""
    
    print("🔧 Making Back Buttons More Specific...")
    print("=" * 60)
    
    # Find all objective template files
    template_dir = "sustainable_energy/dashboard/templates/dashboard/"
    
    for i in range(1, 9):
        file_path = f"{template_dir}objective{i}.html"
        
        if os.path.exists(file_path):
            print(f"🔧 Processing: {file_path}")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Look for current back button patterns
            patterns_to_replace = [
                ("window.location.href='/?t=", "window.location.href='/?objectives=true&t="),
                ("window.location.href='/'", "window.location.href='/?objectives=true'"),
                ("href='/'", "href='/?objectives=true'")
            ]
            
            updated = False
            for old_pattern, new_pattern in patterns_to_replace:
                if old_pattern in content:
                    if old_pattern.endswith("t="):
                        # Handle timestamp pattern
                        import re
                        content = re.sub(r"window\.location\.href='/\?t=(\d+)'", 
                                       r"window.location.href='/?objectives=true&t=\1'", content)
                    else:
                        content = content.replace(old_pattern, new_pattern)
                    updated = True
                    print(f"   ✅ Updated pattern: {old_pattern}")
            
            if updated:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"   💾 Saved changes")
            else:
                print(f"   ✅ No changes needed")

def create_objectives_redirect_handler():
    """Create a view to handle the objectives parameter"""
    
    print(f"\n🔧 Adding Objectives Parameter Handler...")
    
    views_path = "sustainable_energy/dashboard/views.py"
    
    if not os.path.exists(views_path):
        print(f"❌ {views_path} not found")
        return
    
    with open(views_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if we need to modify the objective_selector function
    if "def objective_selector(request):" in content:
        # Find the function
        func_start = content.find("def objective_selector(request):")
        func_end = content.find("\ndef ", func_start + 1)
        
        if func_end == -1:
            func_end = content.find("\nclass ", func_start + 1)
        if func_end == -1:
            func_end = len(content)
        
        current_function = content[func_start:func_end]
        
        # Create enhanced function
        new_function = '''def objective_selector(request):
    """Main objective selector dashboard"""
    # Check if this is specifically requesting the objectives page
    objectives_param = request.GET.get('objectives', None)
    if objectives_param:
        # Force no-cache headers to ensure fresh page load
        response = render(request, 'dashboard/objective_selector.html')
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response
    
    return render(request, 'dashboard/objective_selector.html')'''
        
        # Replace the function
        new_content = content[:func_start] + new_function + content[func_end:]
        
        with open(views_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("   ✅ Enhanced objective_selector function with cache control")
    else:
        print("   ❌ Could not find objective_selector function")

def create_test_links():
    """Create test links to verify navigation"""
    
    test_html = '''<!DOCTYPE html>
<html>
<head>
    <title>Back to Objectives Test</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .test-button { 
            display: inline-block; 
            padding: 15px 30px; 
            margin: 10px; 
            background: #007bff; 
            color: white; 
            text-decoration: none; 
            border-radius: 5px; 
            border: none;
            cursor: pointer;
            font-size: 16px;
        }
        .test-button:hover { background: #0056b3; }
        .section { margin: 30px 0; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>Back to Objectives Navigation Test</h1>
    
    <div class="section">
        <h2>Test Different Navigation Options:</h2>
        
        <button class="test-button" onclick="window.location.href='/'">
            Option 1: Root URL (/)
        </button>
        
        <button class="test-button" onclick="window.location.href='/?objectives=true'">
            Option 2: With Objectives Parameter
        </button>
        
        <button class="test-button" onclick="window.location.href='/?objectives=true&nocache=' + Date.now()">
            Option 3: With Cache Busting
        </button>
        
        <p><strong>Expected Result:</strong> All buttons should take you to the page with 8 objective cards</p>
        <p><strong>Page Title Should Be:</strong> "Energy & emissions projections 2050 - EnerOutlook"</p>
    </div>
    
    <div class="section">
        <h2>Direct Links for Comparison:</h2>
        <ul>
            <li><a href="/">Root Page</a> - Should show 8 objective cards</li>
            <li><a href="/explore/">Explore Dashboard</a> - Should show explore page</li>
            <li><a href="/objective1/">Objective 1</a> - Individual objective</li>
        </ul>
    </div>
    
    <div class="section">
        <h2>Instructions:</h2>
        <ol>
            <li>Click each test button above</li>
            <li>Verify you see the page with 8 objective cards</li>
            <li>If any button shows a different page, that indicates the issue</li>
            <li>The correct page should have cards for: Total Energy Consumption, Electricity Access, Renewable Energy, etc.</li>
        </ol>
    </div>
</body>
</html>'''
    
    with open('back_to_objectives_test.html', 'w', encoding='utf-8') as f:
        f.write(test_html)
    
    print("✅ Created back_to_objectives_test.html")

if __name__ == "__main__":
    update_back_buttons_to_be_specific()
    create_objectives_redirect_handler()
    create_test_links()
    
    print(f"\n" + "=" * 60)
    print("✅ ENHANCED BACK TO OBJECTIVES NAVIGATION:")
    print("✅ Back buttons now use: /?objectives=true")
    print("✅ Added cache control to force fresh page loads")
    print("✅ Created test file: back_to_objectives_test.html")
    print("")
    print("🔄 Please test the navigation now:")
    print("1. Go to any objective page")
    print("2. Click 'Back to Objectives'")
    print("3. You should see the page with 8 objective cards")
    print("4. If not, open back_to_objectives_test.html to debug")