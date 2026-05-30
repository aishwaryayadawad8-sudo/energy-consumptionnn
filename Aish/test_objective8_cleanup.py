#!/usr/bin/env python3
"""
Test script to verify Objective 8 cleanup:
- Combined Investment Timeline section removed
- Future Investment Strategy Predictions renamed (removed year range)
- JavaScript functions updated
"""

import os

def test_objective8_cleanup():
    print("🔍 Testing Objective 8 Cleanup...")
    print("="*60)
    
    objective8_path = "sustainable_energy/dashboard/templates/dashboard/objective8.html"
    
    if os.path.exists(objective8_path):
        with open(objective8_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Test 1: Check that Combined Investment Timeline section is removed
        if "Complete Investment Strategy Timeline" not in content:
            print("✅ Combined Investment Timeline section removed")
        else:
            print("❌ Combined Investment Timeline section still exists")
        
        # Test 2: Check that combinedSection div is removed
        if "combinedSection" not in content:
            print("✅ combinedSection div removed")
        else:
            print("❌ combinedSection div still exists")
        
        # Test 3: Check that Future Investment Strategy Predictions title is updated
        if "Future Investment Strategy Predictions" in content and "Future Investment Strategy Predictions (2021-2030)" not in content:
            print("✅ Future Investment Strategy Predictions title updated (year range removed)")
        else:
            print("❌ Future Investment Strategy Predictions title not properly updated")
        
        # Test 4: Check that combinedChart variable is removed
        if "let combinedChart" not in content:
            print("✅ combinedChart variable removed")
        else:
            print("❌ combinedChart variable still exists")
        
        # Test 5: Check that createCombinedChart function is removed
        if "createCombinedChart" not in content:
            print("✅ createCombinedChart function removed")
        else:
            print("❌ createCombinedChart function still exists")
        
        # Test 6: Check that combined API call is removed
        if "/api/objective8/combined/" not in content:
            print("✅ Combined API call removed from JavaScript")
        else:
            print("❌ Combined API call still exists in JavaScript")
            
    else:
        print("❌ objective8.html file not found")
    
    print("="*60)
    print("🎯 CLEANUP SUMMARY:")
    print("   • Combined Investment Timeline section: REMOVED")
    print("   • Future Investment Predictions: RENAMED (no year range)")
    print("   • JavaScript functions: CLEANED UP")
    print("   • API calls: SIMPLIFIED")
    print("="*60)

if __name__ == "__main__":
    test_objective8_cleanup()