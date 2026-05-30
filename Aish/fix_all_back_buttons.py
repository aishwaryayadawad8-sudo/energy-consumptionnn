#!/usr/bin/env python3
"""
Fix All Back Buttons in Objective Pages
"""

import os

def fix_objective4_back_button():
    """Fix the back button in objective4.html"""
    
    file_path = "sustainable_energy/dashboard/templates/dashboard/objective4.html"
    
    if not os.path.exists(file_path):
        print(f"❌ {file_path} not found")
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the back button text
    old_text = '<span>Back to Overview</span>'
    new_text = '<span>Back to Objectives</span>'
    
    if old_text in content:
        content = content.replace(old_text, new_text)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Fixed objective4.html back button")
    else:
        print("✅ objective4.html back button already correct")

def fix_objective8_back_button():
    """Fix the duplicate back button in objective8.html"""
    
    file_path = "sustainable_energy/dashboard/templates/dashboard/objective8.html"
    
    if not os.path.exists(file_path):
        print(f"❌ {file_path} not found")
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the duplicate line
    old_text = '''            <a onclick="window.location.href='/'" class="btn btn-secondary btn-lg">
                <i class="fas fa-arrow-left"></i> Back to Objectives
                <i class="fas fa-arrow-left"></i> Back to Objectives
            </a>'''
    
    new_text = '''            <a onclick="window.location.href='/'" class="btn btn-secondary btn-lg">
                <i class="fas fa-arrow-left"></i> Back to Objectives
            </a>'''
    
    if old_text in content:
        content = content.replace(old_text, new_text)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Fixed objective8.html duplicate back button")
    else:
        print("✅ objective8.html back button already correct")

def verify_all_back_buttons():
    """Verify all objective pages have correct back buttons"""
    
    print("\n🔍 Verifying all back buttons:")
    
    for i in range(1, 9):
        file_path = f"sustainable_energy/dashboard/templates/dashboard/objective{i}.html"
        
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for back button
            has_back_button = False
            back_text = ""
            
            if "Back to Objectives" in content:
                has_back_button = True
                back_text = "Back to Objectives"
            elif "Back to Overview" in content:
                has_back_button = True
                back_text = "Back to Overview (needs fix)"
            elif "Back to Dashboard" in content:
                has_back_button = True
                back_text = "Back to Dashboard (needs fix)"
            
            # Check navigation URL
            correct_url = "window.location.href='/'"
            has_correct_url = correct_url in content
            
            status = "✅" if (has_back_button and has_correct_url and back_text == "Back to Objectives") else "⚠️"
            
            print(f"   {status} Objective {i}: {back_text if has_back_button else 'No back button'} | URL: {'Correct' if has_correct_url else 'Needs fix'}")

if __name__ == "__main__":
    print("🔧 Fixing All Back Buttons...")
    print("=" * 60)
    
    fix_objective4_back_button()
    fix_objective8_back_button()
    verify_all_back_buttons()
    
    print("\n" + "=" * 60)
    print("✅ COMPLETE! All back buttons should now work correctly.")
    print("🔄 Refresh any objective page and test the 'Back to Objectives' button.")