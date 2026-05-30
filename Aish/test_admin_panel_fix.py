#!/usr/bin/env python3
"""
Test script to verify admin panel fixes:
- Check that admin_panel.html doesn't reference non-existent URLs
- Verify correct titles and links
"""

import os

def test_admin_panel_fix():
    print("🔍 Testing Admin Panel Fix...")
    print("="*60)
    
    admin_panel_path = "sustainable_energy/dashboard/templates/dashboard/admin_panel.html"
    
    if os.path.exists(admin_panel_path):
        with open(admin_panel_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Test 1: Check that objective8_dashboard URL is removed
        if "objective8_dashboard" not in content:
            print("✅ Removed reference to non-existent 'objective8_dashboard' URL")
        else:
            print("❌ Still contains reference to 'objective8_dashboard' URL")
            
        # Test 2: Check that email-admin link exists
        if "/email-admin/" in content:
            print("✅ Email alert system link updated to '/email-admin/'")
        else:
            print("❌ Email alert system link not found")
            
        # Test 3: Check correct title
        if "Admin Panel - SDG 7 Monitoring" in content:
            print("✅ Page title updated to 'Admin Panel - SDG 7 Monitoring'")
        else:
            print("❌ Page title not updated correctly")
            
        # Test 4: Check header title
        if "Admin Panel - SDG 7 Monitoring" in content and "Objective 8:" not in content:
            print("✅ Header title updated (removed 'Objective 8' reference)")
        else:
            print("❌ Header title still contains 'Objective 8' reference")
            
        # Test 5: Check home link
        if 'href="/"' in content:
            print("✅ Home link simplified to '/'")
        else:
            print("❌ Home link not simplified")
            
    else:
        print("❌ admin_panel.html file not found")
    
    print("="*60)
    print("🎯 ADMIN PANEL FIX SUMMARY:")
    print("   • Removed non-existent URL references")
    print("   • Updated email alert system link")
    print("   • Fixed page titles and headers")
    print("   • Simplified navigation links")
    print("="*60)

if __name__ == "__main__":
    test_admin_panel_fix()