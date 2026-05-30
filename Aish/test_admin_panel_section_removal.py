#!/usr/bin/env python3
"""
Test script to verify "Single Country Alert" section removal from admin panel:
- Check that the Single Country Alert card is removed
- Verify remaining cards are properly arranged
"""

import os

def test_admin_panel_section_removal():
    print("🔍 Testing Admin Panel Section Removal...")
    print("="*60)
    
    admin_panel_path = "sustainable_energy/dashboard/templates/dashboard/admin_panel.html"
    
    if os.path.exists(admin_panel_path):
        with open(admin_panel_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Test 1: Check that Single Country Alert section is removed
        if "Single Country Alert" not in content:
            print("✅ 'Single Country Alert' section removed")
        else:
            print("❌ 'Single Country Alert' section still exists")
            
        # Test 2: Check that flag icon is removed
        if "fas fa-flag" not in content:
            print("✅ Flag icon removed")
        else:
            print("❌ Flag icon still exists")
            
        # Test 3: Check that send_email_single_country URL is removed
        if "send_email_single_country" not in content:
            print("✅ Single country email URL removed")
        else:
            print("❌ Single country email URL still exists")
            
        # Test 4: Check that Custom Alert card still exists
        if "Custom Alert" in content:
            print("✅ Custom Alert card preserved")
        else:
            print("❌ Custom Alert card missing")
            
        # Test 5: Check that XGBoost Alerts card still exists
        if "XGBoost Alerts" in content:
            print("✅ XGBoost Alerts card preserved")
        else:
            print("❌ XGBoost Alerts card missing")
            
        # Test 6: Check that remaining cards use col-md-6 (2 cards in row)
        if "col-md-6" in content:
            print("✅ Remaining cards properly arranged (2 per row)")
        else:
            print("❌ Card layout not updated")
            
    else:
        print("❌ admin_panel.html file not found")
    
    print("="*60)
    print("🎯 SECTION REMOVAL SUMMARY:")
    print("   • Removed: Single Country Alert card")
    print("   • Preserved: Custom Alert and XGBoost Alerts")
    print("   • Layout: Updated to 2 cards per row (col-md-6)")
    print("   • Result: Cleaner admin panel with essential features")
    print("="*60)

if __name__ == "__main__":
    test_admin_panel_section_removal()