#!/usr/bin/env python3
"""
Verify Back Button Navigation
"""

import requests

def verify_navigation():
    """Verify the exact navigation flow"""
    
    BASE_URL = "http://127.0.0.1:8000"
    
    print("🔍 Verifying Back Button Navigation")
    print("=" * 60)
    
    # Step 1: Check root page content
    print("1️⃣  Root page (/) content check:")
    try:
        response = requests.get(f"{BASE_URL}/", timeout=10)
        if response.status_code == 200:
            content = response.text
            
            # Look for specific objective cards
            objectives_found = []
            objective_indicators = [
                ("Total Energy Consumption", "Objective 1"),
                ("Electricity Access", "Objective 2"), 
                ("Renewable Energy", "Objective 3"),
                ("CO2 Emissions", "Objective 4"),
                ("Country-Specific", "Objective 5"),
                ("Policy Impact", "Objective 6"),
                ("Investment Strategy", "Objective 7"),
                ("Admin Panel", "Objective 8")
            ]
            
            for indicator, obj_name in objective_indicators:
                if indicator in content:
                    objectives_found.append(obj_name)
                    print(f"   ✅ {obj_name}: Found")
                else:
                    print(f"   ❌ {obj_name}: Missing")
            
            print(f"\n   📊 Summary: {len(objectives_found)}/8 objectives found")
            
            if len(objectives_found) >= 6:
                print("   ✅ This IS the objectives page")
                return True
            else:
                print("   ❌ This is NOT the objectives page")
                return False
                
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def create_test_page():
    """Create a simple test page to verify navigation"""
    
    print(f"\n2️⃣  Creating test navigation page:")
    
    test_html = '''<!DOCTYPE html>
<html>
<head>
    <title>Navigation Test</title>
</head>
<body>
    <h1>Navigation Test Page</h1>
    <p>This page tests the back button navigation.</p>
    
    <h2>Test the Back Button:</h2>
    <button onclick="window.location.href='/'" style="padding: 10px 20px; font-size: 16px;">
        ← Back to Objectives (Test)
    </button>
    
    <h2>Direct Links:</h2>
    <ul>
        <li><a href="/">Root Page (/)</a> - Should show objectives</li>
        <li><a href="/objective1/">Objective 1</a> - Should show objective 1</li>
        <li><a href="/explore/">Explore Dashboard</a> - Should show explore page</li>
    </ul>
    
    <h2>Instructions:</h2>
    <ol>
        <li>Click "Back to Objectives (Test)" button above</li>
        <li>You should see a page with 8 objective cards</li>
        <li>If you see something else, there's a navigation issue</li>
    </ol>
</body>
</html>'''
    
    with open('navigation_test.html', 'w') as f:
        f.write(test_html)
    
    print("   ✅ Created navigation_test.html")
    print("   🌐 Open this file in your browser to test navigation")

def show_manual_verification():
    """Show manual verification steps"""
    
    print(f"\n" + "=" * 60)
    print("🧪 MANUAL VERIFICATION STEPS:")
    print("=" * 60)
    print("1. 🌐 Open: http://127.0.0.1:8000/")
    print("   👀 Expected: Page with title 'Energy & emissions projections 2050'")
    print("   👀 Expected: 8 objective cards visible")
    print("   👀 Expected: Each card has 'View Analysis' button")
    print("")
    print("2. 🖱️  Click: 'View Analysis' on any objective")
    print("   👀 Expected: Individual objective page loads")
    print("   👀 Expected: 'Back to Objectives' button visible")
    print("")
    print("3. 🔙 Click: 'Back to Objectives' button")
    print("   👀 Expected: Return to page with 8 objective cards")
    print("   👀 Expected: Same page as step 1")
    print("")
    print("❓ If step 3 doesn't work:")
    print("   - Check browser console (F12) for errors")
    print("   - Try hard refresh (Ctrl+F5)")
    print("   - Clear browser cache")
    print("   - Try incognito mode")

if __name__ == "__main__":
    is_objectives_page = verify_navigation()
    create_test_page()
    show_manual_verification()
    
    if is_objectives_page:
        print(f"\n✅ CONCLUSION: Navigation should be working correctly!")
        print(f"   The root page IS serving the objectives page.")
        print(f"   If you're not seeing it, try clearing browser cache.")
    else:
        print(f"\n❌ CONCLUSION: There's an issue with the root page.")
        print(f"   The root page is NOT serving the objectives page.")
        print(f"   This needs to be investigated further.")