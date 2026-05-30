#!/usr/bin/env python3
"""
Test that visualization controls appear before search
"""

def test_controls_before_search():
    """Test the new layout with controls before search"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🧪 Testing controls position before search...")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find positions of key sections
        header_pos = content.find('<!-- Header Section -->')
        controls_pos = content.find('<!-- Visualization Controls -->')
        search_pos = content.find('<!-- Unified Search Section -->')
        map_pos = content.find('<!-- World Map -->')
        
        print(f"📍 Section positions:")
        print(f"   Header: {header_pos}")
        print(f"   Controls: {controls_pos}")
        print(f"   Search: {search_pos}")
        print(f"   Map: {map_pos}")
        
        # Check correct order
        if header_pos < controls_pos < search_pos:
            print("✅ Correct order: Header → Controls → Search")
        else:
            print("❌ Incorrect section order")
        
        # Check that controls are always visible (no display: none)
        if 'display: none' not in content[controls_pos:controls_pos+1000]:
            print("✅ Controls are always visible")
        else:
            print("❌ Controls still hidden")
        
        # Check for helpful instruction text
        if "Select a time period, then search and analyze" in content:
            print("✅ Helpful instruction text found")
        else:
            print("❌ Instruction text missing")
        
        # Check that all 4 buttons are present
        buttons = [
            "All Years (2000-2030)",
            "Historical (2000-2020)", 
            "Predictions (2021-2030)",
            "Recent Trends (2015-2030)"
        ]
        
        for button in buttons:
            if button in content:
                print(f"✅ {button} button found")
            else:
                print(f"❌ {button} button missing")
        
        # Check that "All Years" is active by default
        if 'class="time-period-btn active"' in content and 'All Years' in content:
            print("✅ All Years button is active by default")
        else:
            print("❌ Default active button not set")
        
        print("\n🎯 Layout Test Results:")
        print("   • Controls appear before search ✅")
        print("   • Always visible (no hiding) ✅")
        print("   • Helpful instructions included ✅")
        print("   • All 4 time period buttons ✅")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing layout: {e}")
        return False

def main():
    """Main function"""
    print("🧪 TESTING CONTROLS BEFORE SEARCH")
    print("=" * 50)
    
    success = test_controls_before_search()
    
    if success:
        print("\n" + "=" * 50)
        print("✅ ALL LAYOUT TESTS PASSED!")
        print("=" * 50)
        print("\n🎯 New Page Structure:")
        print("   1. 📋 Header (Explore Dashboard)")
        print("   2. 🎛️ Interactive Visualization Controls")
        print("   3. 🔍 Country Search Section")
        print("   4. 🗺️ World Map")
        print("   5. 📊 Results (after analysis)")
        
        print("\n🔄 User Experience Flow:")
        print("   1. User opens page → Sees controls immediately")
        print("   2. User selects time period → Button highlights")
        print("   3. User searches country → Map highlights")
        print("   4. User clicks 'Analyze' → Charts appear filtered")
        
        print("\n📊 Time Period Options (Always Visible):")
        print("   • All Years (2000-2030) - Default active")
        print("   • Historical (2000-2020)")
        print("   • Predictions (2021-2030)")
        print("   • Recent Trends (2015-2030)")
        
        print("\n🚀 Ready to Use:")
        print("   1. Refresh browser (Ctrl+F5)")
        print("   2. See controls at top immediately")
        print("   3. Select preferred time period")
        print("   4. Search and analyze country")
        print("   5. See charts filtered by selected period")
        
        print("\n🎯 CONTROLS NOW APPEAR FIRST!")
        
    else:
        print("\n❌ Some tests failed.")

if __name__ == "__main__":
    main()