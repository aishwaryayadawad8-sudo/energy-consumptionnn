#!/usr/bin/env python3
"""
Fix Duplicate objective_selector Functions in views.py
"""

import os

def fix_duplicate_functions():
    """Remove duplicate objective_selector function"""
    
    views_path = "sustainable_energy/dashboard/views.py"
    
    if not os.path.exists(views_path):
        print(f"❌ {views_path} not found")
        return
    
    with open(views_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("🔧 Fixing duplicate objective_selector functions...")
    
    # Find the duplicate function (the second one)
    duplicate_start = content.find('def objective_selector(request):', content.find('def objective_selector(request):') + 1)
    
    if duplicate_start != -1:
        # Find the end of the duplicate function (next function definition)
        duplicate_end = content.find('def objective1_dashboard(request):', duplicate_start)
        
        if duplicate_end != -1:
            # Remove the duplicate function
            before_duplicate = content[:duplicate_start]
            after_duplicate = content[duplicate_end:]
            
            # Remove any extra newlines
            while before_duplicate.endswith('\n\n\n'):
                before_duplicate = before_duplicate[:-1]
            
            new_content = before_duplicate + '\n\n' + after_duplicate
            
            with open(views_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ Removed duplicate objective_selector function")
        else:
            print("❌ Could not find end of duplicate function")
    else:
        print("✅ No duplicate function found")

def verify_objective_selector():
    """Verify there's only one objective_selector function"""
    
    views_path = "sustainable_energy/dashboard/views.py"
    
    with open(views_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    count = content.count('def objective_selector(request):')
    
    print(f"\n🔍 Verification:")
    print(f"   objective_selector functions found: {count}")
    
    if count == 1:
        print("   ✅ Only one objective_selector function (correct)")
    else:
        print(f"   ⚠️  Found {count} objective_selector functions (should be 1)")

if __name__ == "__main__":
    print("🔧 Fixing Duplicate objective_selector Functions...")
    print("=" * 60)
    
    fix_duplicate_functions()
    verify_objective_selector()
    
    print("\n" + "=" * 60)
    print("✅ COMPLETE! objective_selector should now work correctly.")
    print("🔄 The 'Back to Objectives' button should now show the correct page.")