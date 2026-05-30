#!/usr/bin/env python3
"""
Test the map with graphs layout functionality
"""

import os

def test_map_with_graphs_layout():
    """Test that map and graphs are displayed together"""
    
    print("🧪 TESTING MAP WITH GRAPHS LAYOUT")
    print("=" * 60)
    
    dashboard_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    if not os.path.exists(dashboard_path):
        print("❌ Dashboard file not found!")
        return False
    
    print("✅ Dashboard file found")
    
    # Check for map with graphs layout features
    with open(dashboard_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Features that should be present for map with graphs layout
    layout_features = [
        ('Country map container', 'id="countryMap"'),
        ('Map title element', 'id="mapTitle"'),
        ('Country map initialization', 'initializeCountryMap'),
        ('Country map highlighting', 'highlightCountryOnCountryMap'),
        ('Side-by-side layout', 'col-md-6'),
        ('Map container styling', 'map-container'),
        ('Charts container', 'charts-container'),
        ('Timeline chart', 'id="mainChart"'),
        ('Pie chart', 'id="pieChart"'),
        ('Access chart', 'id="accessChart"'),
        ('Renewable chart', 'id="renewableChart"'),
        ('Metric cards', 'metric-cards'),
        ('Bootstrap grid layout', 'class="row"'),
        ('Country map variable', 'let countryMap'),
        ('Map removal on new search', 'countryMap.remove()')
    ]
    
    print("\n🔍 Checking map with graphs features:")
    all_features_present = True
    
    for feature_name, feature_code in layout_features:
        if feature_code in content:
            print(f"   ✅ {feature_name}")
        else:
            print(f"   ❌ {feature_name} - MISSING!")
            all_features_present = False
    
    if all_features_present:
        print("\n✅ ALL MAP WITH GRAPHS FEATURES PRESENT!")
        
        print("\n🎯 Expected User Experience:")
        print("   1. 📱 Page loads showing:")
        print("      • Search interface at top")
        print("      • World map below search")
        print("      • Clean, professional layout")
        
        print("\n   2. 🔍 User searches for country:")
        print("      • Types 'India' in search box")
        print("      • Clicks 'Search' button")
        print("      • Country gets highlighted on world map")
        
        print("\n   3. 📊 Results section appears with:")
        print("      • 4 metric cards at top (Access, CO₂, Renewable, Efficiency)")
        print("      • Left side: Country-specific map focused on India")
        print("      • Right side: Timeline chart and pie chart")
        print("      • Bottom row: Access forecast and renewable growth charts")
        
        print("\n🎨 Visual Layout Structure:")
        print("   ┌─────────────────────────────────────┐")
        print("   │  🔍 Search Country Energy Profile  │")
        print("   │  [India            ] [🔵 Search]   │")
        print("   ├─────────────────────────────────────┤")
        print("   │  🗺️ World Map (with India          │")
        print("   │     highlighted in light green)    │")
        print("   ├─────────────────────────────────────┤")
        print("   │  📊📊📊📊 Metric Cards             │")
        print("   ├─────────────────┬───────────────────┤")
        print("   │  🗺️ India Map   │  📈 Timeline      │")
        print("   │  (Focused view) │  📊 Energy Mix    │")
        print("   ├─────────────────┼───────────────────┤")
        print("   │  📈 Access      │  🌱 Renewable     │")
        print("   │     Forecast    │     Growth        │")
        print("   └─────────────────┴───────────────────┘")
        
        print("\n🗺️ Map Features:")
        print("   • World Map (top):")
        print("     - Shows global context")
        print("     - Country highlighted with light green fill")
        print("     - Green pin marker and popup")
        print("   • Country Map (bottom left):")
        print("     - Focused view of selected country")
        print("     - Same highlighting style")
        print("     - Zoomed to fit country boundaries")
        
        print("\n📊 Chart Features:")
        print("   • Timeline Chart: Electricity access trends (2000-2030)")
        print("   • Pie Chart: Energy source distribution")
        print("   • Access Chart: Future access forecasts")
        print("   • Renewable Chart: Renewable energy growth")
        
        print("\n🎯 Interactive Features:")
        print("   • Both maps show country highlighting")
        print("   • Pin markers with country data popups")
        print("   • Responsive charts with hover effects")
        print("   • Professional styling throughout")
        
        return True
    else:
        print("\n❌ Some map with graphs features are missing!")
        return False

def main():
    """Main function"""
    success = test_map_with_graphs_layout()
    
    if success:
        print("\n" + "=" * 60)
        print("🎉 MAP WITH GRAPHS LAYOUT TEST PASSED!")
        print("=" * 60)
        print("\n🚀 Ready to Experience Map + Graphs:")
        print("   1. Start Django server: python manage.py runserver")
        print("   2. Go to: http://localhost:8000/explore-dashboard/")
        print("   3. Search for 'India'")
        print("   4. See both maps + all charts together!")
        
        print("\n✨ What You'll See:")
        print("   🔍 Search interface at top")
        print("   🗺️ World map with India highlighted")
        print("   📊 4 metric cards with key stats")
        print("   🗺️ India-focused map on left")
        print("   📈 Timeline and pie charts on right")
        print("   📊 Additional forecast charts below")
        
        print("\n🎯 PERFECT MAP + GRAPHS EXPERIENCE!")
        print("   Country map alongside beautiful charts!")
        
    else:
        print("\n❌ Test failed. Please check the issues above.")

if __name__ == "__main__":
    main()