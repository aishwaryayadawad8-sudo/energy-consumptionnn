#!/usr/bin/env python3
"""
Fix Objective 8 Duplicate Lines
"""

import os
import re

def fix_objective8_duplicates():
    """Fix duplicate lines in objective8.html"""
    
    file_path = "sustainable_energy/dashboard/templates/dashboard/objective8.html"
    
    if not os.path.exists(file_path):
        print(f"❌ {file_path} not found")
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("🔧 Fixing duplicate lines in objective8.html...")
    
    # Fix the back button duplicates
    old_back = '''            <a onclick="window.location.href='/'" class="btn btn-secondary btn-lg">
                <i class="fas fa-arrow-left"></i> Back to Objectives
                <i class="fas fa-arrow-left"></i> Back to Objectives
            </a>'''
    
    new_back = '''            <a onclick="window.location.href='/'" class="btn btn-secondary btn-lg">
                <i class="fas fa-arrow-left"></i> Back to Objectives
            </a>'''
    
    if old_back in content:
        content = content.replace(old_back, new_back)
        print("   ✅ Fixed back button duplicates")
    
    # Fix other duplicate patterns
    duplicates_fixed = 0
    
    # Pattern for duplicate href links
    patterns = [
        (r'(<a href="[^"]*" class="btn[^>]*>)\s*\1\s*\1', r'\1'),
        (r'(<button class="btn[^>]*>)\s*\1\s*\1', r'\1'),
        (r'(<button class="btn[^>]*>)\s*\1', r'\1'),
        (r'(<a href="[^"]*" class="btn[^>]*>)\s*\1', r'\1')
    ]
    
    for pattern, replacement in patterns:
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, replacement, content)
            duplicates_fixed += len(matches)
    
    if duplicates_fixed > 0:
        print(f"   ✅ Fixed {duplicates_fixed} other duplicate patterns")
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Fixed objective8.html duplicates")

def verify_objective8():
    """Verify objective8.html is now clean"""
    
    file_path = "sustainable_energy/dashboard/templates/dashboard/objective8.html"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for back button
    back_count = content.count("Back to Objectives")
    arrow_count = content.count("fas fa-arrow-left")
    
    print(f"\n🔍 Verification:")
    print(f"   'Back to Objectives' appears: {back_count} times")
    print(f"   'fas fa-arrow-left' appears: {arrow_count} times")
    
    if back_count == 1 and arrow_count >= 1:
        print("   ✅ Back button is now clean")
    else:
        print("   ⚠️  Back button may still have issues")

if __name__ == "__main__":
    print("🔧 Fixing Objective 8 Duplicate Lines...")
    print("=" * 60)
    
    fix_objective8_duplicates()
    verify_objective8()
    
    print("\n" + "=" * 60)
    print("✅ COMPLETE! Objective 8 should now have a clean back button.")