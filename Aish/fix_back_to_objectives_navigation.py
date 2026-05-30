#!/usr/bin/env python3
"""
Fix Back to Objectives Navigation
This script ensures all objective pages have correct navigation back to the main objectives selector
"""

import os
import glob

def fix_back_navigation():
    """Fix the back navigation for all objective templates"""
    
    # Find all objective template files
    template_dir = "sustainable_energy/dashboard/templates/dashboard/"
    objective_files = []
    
    for i in range(1, 9):  # Objectives 1-8
        file_path = f"{template_dir}objective{i}.html"
        if os.path.exists(file_path):
            objective_files.append(file_path)
    
    print(f"Found {len(objective_files)} objective template files")
    
    for file_path in objective_files:
        print(f"\n🔧 Fixing: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for existing back button patterns
        back_patterns = [
            "onclick=\"window.location.href='/'\"",
            "onclick=\"window.location.href='/dashboard/'\"",
            "onclick=\"window.location.href='/explore/'\"",
            "href=\"/\"",
            "href=\"/dashboard/\"",
            "href=\"/explore/\""
        ]
        
        # The correct navigation should be to the root path which shows objective selector
        correct_navigation = "onclick=\"window.location.href='/'\""
        
        updated = False
        
        # Check and fix various back button patterns
        for pattern in back_patterns:
            if pattern in content and pattern != correct_navigation:
                content = content.replace(pattern, correct_navigation)
                updated = True
                print(f"   ✅ Updated navigation from {pattern}")
        
        # Also check for any hardcoded links that might be wrong
        if "href=\"/dashboard/\"" in content:
            content = content.replace("href=\"/dashboard/\"", "href=\"/\"")
            updated = True
            print("   ✅ Fixed hardcoded dashboard link")
        
        if "href=\"/explore/\"" in content:
            content = content.replace("href=\"/explore/\"", "href=\"/\"")
            updated = True
            print("   ✅ Fixed hardcoded explore link")
        
        # Ensure the back button text is consistent
        if "Back to Objectives" not in content and "back-btn" in content:
            # Look for back button and ensure it has the right text
            if "Back to Dashboard" in content:
                content = content.replace("Back to Dashboard", "Back to Objectives")
                updated = True
                print("   ✅ Updated button text to 'Back to Objectives'")
        
        if updated:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"   💾 Saved changes to {file_path}")
        else:
            print(f"   ✅ Navigation already correct")

def verify_objective_selector():
    """Verify the objective selector page exists and is accessible"""
    
    selector_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print(f"\n🔍 Verifying objective selector page...")
    
    if os.path.exists(selector_path):
        print(f"   ✅ Found: {selector_path}")
        
        with open(selector_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if it has the 8 objective cards
        objective_count = content.count("objective")
        print(f"   📊 Contains {objective_count} objective references")
        
        if "Country Energy Forecasts" in content:
            print("   ✅ Contains main title")
        
        return True
    elif os.path.exists(index_path):
        print(f"   ✅ Found: {index_path} (alternative)")
        return True
    else:
        print(f"   ❌ Objective selector page not found!")
        return False

def test_navigation():
    """Test the navigation URLs"""
    
    print(f"\n🧪 Navigation Test URLs:")
    print(f"   🏠 Main Page (Objective Selector): http://127.0.0.1:8000/")
    print(f"   📊 Objective 1: http://127.0.0.1:8000/objective1/")
    print(f"   📊 Objective 2: http://127.0.0.1:8000/objective2/")
    print(f"   📊 Objective 3: http://127.0.0.1:8000/objective3/")
    print(f"   📊 Objective 4: http://127.0.0.1:8000/objective4/")
    print(f"   📊 Objective 5: http://127.0.0.1:8000/objective5/")
    print(f"   📊 Objective 6: http://127.0.0.1:8000/objective6/")
    print(f"   📊 Objective 7: http://127.0.0.1:8000/objective7/")
    print(f"   📊 Objective 8: http://127.0.0.1:8000/objective8/")

if __name__ == "__main__":
    print("🔧 Fixing Back to Objectives Navigation...")
    print("=" * 60)
    
    fix_back_navigation()
    verify_objective_selector()
    test_navigation()
    
    print("\n" + "=" * 60)
    print("✅ COMPLETE! All objective pages should now navigate back correctly.")
    print("🔄 Test by clicking 'Back to Objectives' from any objective page.")