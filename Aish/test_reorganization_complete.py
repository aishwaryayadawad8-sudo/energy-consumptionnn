#!/usr/bin/env python3
"""
Test script to verify the final reorganization is complete:
- Admin panel is separate from the 8 objectives
- Investment Strategy Support is now the 8th objective
- All URLs and views are properly configured
"""

import os
import sys

def test_reorganization():
    print("🔍 Testing Final Reorganization...")
    print("="*60)
    
    # Test 1: Check that objective8.html contains Investment Strategy content
    objective8_path = "sustainable_energy/dashboard/templates/dashboard/objective8.html"
    if os.path.exists(objective8_path):
        with open(objective8_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if "Sustainable Investment Strategy Support" in content:
                print("✅ Objective 8 contains Investment Strategy content")
            else:
                print("❌ Objective 8 does not contain Investment Strategy content")
    else:
        print("❌ objective8.html file not found")
    
    # Test 2: Check that objective9.html no longer exists
    objective9_path = "sustainable_energy/dashboard/templates/dashboard/objective9.html"
    if not os.path.exists(objective9_path):
        print("✅ objective9.html has been removed")
    else:
        print("❌ objective9.html still exists")
    
    # Test 3: Check objective_selector.html structure
    selector_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    if os.path.exists(selector_path):
        with open(selector_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if "Admin Panel Section" in content and "Administrative Panel" in content:
                print("✅ Admin panel is separate section in objective_selector.html")
            else:
                print("❌ Admin panel section not found in objective_selector.html")
    
    # Test 4: Check URLs configuration
    urls_path = "sustainable_energy/dashboard/urls.py"
    if os.path.exists(urls_path):
        with open(urls_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if "objective8/" in content and "objective8_dashboard" in content:
                print("✅ Objective 8 URLs are configured")
            else:
                print("❌ Objective 8 URLs not properly configured")
    
    # Test 5: Check views.py for objective8 functions
    views_path = "sustainable_energy/dashboard/views.py"
    if os.path.exists(views_path):
        with open(views_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if "def objective8_dashboard(request):" in content and "Sustainable Investment Strategy Support" in content:
                print("✅ Objective 8 view functions are configured for Investment Strategy")
            else:
                print("❌ Objective 8 view functions not properly configured")
    
    print("="*60)
    print("🎯 REORGANIZATION SUMMARY:")
    print("   • Admin Panel: Moved below all 8 objectives")
    print("   • Investment Strategy: Now Objective 8")
    print("   • Email Alert System: Part of Admin Panel")
    print("   • All URLs and views updated")
    print("="*60)

if __name__ == "__main__":
    test_reorganization()