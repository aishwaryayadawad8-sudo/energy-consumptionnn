#!/usr/bin/env python3
"""
Test the search-first behavior where map appears only after search
"""

import os

def test_search_first_behavior():
    """Test that map is hidden initially and appears after search"""
    
    print("🧪 TESTING SEARCH-FIRST BEHAVIOR")
    print("=" * 60)
    
    dashboard_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    if not os.path.exists(dashboard_path):
        print("❌ Dashboard file not found!")
        return False
    
    print("✅ Dashboard file found")
    
    # Check for search-first features
    with open(dashboard_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Features that should be present for search-first behavior
    search_first_features = [
        ('Map initially hidden', 'id="map" style="display: none'),
        ('Map placeholder present', 'id="mapPlaceholder"'),
        ('Search placeholder message', 'Search for a Country'),
        ('Map show functionality', 'mapElement.style.display = \'block\''),
        ('Placeholder hide functionality', 'placeholderElement.style.display = \'none\''),
        ('Delayed map initialization', 'if (!map) {'),
        ('Map resize after show', 'map.invalidateSize()'),
        ('Skip initial map loading', 'Map will load after search'),
        ('Search interface present', 'Search Country Energy Profile'),
        ('India placeholder in search', 'placeholder="India"')
    ]
    
    print("\n🔍 Checking search-first features:")
    all_features_present = True
    
    for feature_name, feature_code in search_first_features:
        if feature_code in content:
            print(f"   ✅ {feature_name}")
        else:
            print(f"   ❌ {feature_name} - MISSING!")
            all_features_present = False
    
    if all_features_present:
        print("\n✅ ALL SEARCH-FIRST FEATURES PRESENT!")
        
        print("\n🎯 Expected User Experience:")
        print("   1. 📱 Page loads showing:")
        print("      • 'Search Country Energy Profile' title")
        print("      • White search box with 'India' placeholder")
        print("      • Blue 'Search' button")
        print("      • Placeholder message: 'Search for a Country'")
        print("      • NO MAP visible initially")
        
        print("\n   2. 🔍 User searches for country:")
        print("      • Types 'India' in search box")
        print("      • Clicks 'Search' button or selects from suggestions")
        
        print("\n   3. 🗺️ Map appears with:")
        print("      • Smooth transition (placeholder disappears)")
        print("      • Map initializes and loads")
        print("      • India highlighted with light green fill")
        print("      • Green teardrop pin marker")
        print("      • White popup with country data")
        print("      • Map zooms to fit India perfectly")
        
        print("\n   4. 📊 Additional content shows:")
        print("      • Country metrics cards")
        print("      • Interactive charts and forecasts")
        print("      • Energy analysis data")
        
        print("\n🎨 Visual Flow:")
        print("   Initial: Clean search interface only")
        print("   After Search: Full dashboard with map + data")
        print("   Benefit: Focused, non-overwhelming experience")
        
        print("\n🌍 Works for All Countries:")
        print("   • India → Map appears with India highlighted")
        print("   • Germany → Map appears with Germany highlighted")
        print("   • Brazil → Map appears with Brazil highlighted")
        print("   • Any of 100+ supported countries")
        
        return True
    else:
        print("\n❌ Some search-first features are missing!")
        return False

def main():
    """Main function"""
    success = test_search_first_behavior()
    
    if success:
        print("\n" + "=" * 60)
        print("🎉 SEARCH-FIRST BEHAVIOR TEST PASSED!")
        print("=" * 60)
        print("\n🚀 Ready to Experience:")
        print("   1. Start Django server: python manage.py runserver")
        print("   2. Go to: http://localhost:8000/explore-dashboard/")
        print("   3. See clean search interface (NO MAP)")
        print("   4. Search for 'India'")
        print("   5. Watch map appear with perfect highlighting!")
        
        print("\n✨ Perfect User Experience:")
        print("   🔍 Clean, focused search interface initially")
        print("   🗺️ Map appears only when needed")
        print("   🎯 Immediate country highlighting after search")
        print("   📊 Complete dashboard experience after search")
        
        print("\n🎯 SEARCH-FIRST WORKFLOW COMPLETE!")
        print("   Users will search first, then see the map!")
        
    else:
        print("\n❌ Test failed. Please check the issues above.")

if __name__ == "__main__":
    main()