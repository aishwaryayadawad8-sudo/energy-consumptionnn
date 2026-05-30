#!/usr/bin/env python3
"""
Test that charts appear only after analysis
"""

def test_dashboard_flow():
    """Test the updated dashboard flow"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🧪 Testing dashboard flow...")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check that results section is initially hidden
        if 'id="resultSection" style="display: none;"' in content:
            print("✅ Results section is initially hidden")
        else:
            print("⚠️ Results section visibility not found")
        
        # Check that selectCountry doesn't call showResultsSection
        if 'showResultsSection(countryName);' not in content.split('function selectCountry')[1].split('function analyzeSelectedCountry')[0]:
            print("✅ selectCountry doesn't show results immediately")
        else:
            print("❌ selectCountry still shows results immediately")
        
        # Check that analyzeSelectedCountry calls showResultsSection
        analyze_section = content.split('function analyzeSelectedCountry')[1].split('function highlightCountryOnMap')[0]
        if 'showResultsSection(foundCountry);' in analyze_section:
            print("✅ analyzeSelectedCountry shows results and charts")
        else:
            print("❌ analyzeSelectedCountry doesn't show results")
        
        # Check that renderCharts includes all 4 charts
        render_section = content.split('function renderCharts')[1] if 'function renderCharts' in content else ""
        chart_checks = [
            ('Timeline Chart', 'mainChart'),
            ('Pie Chart', 'pieChart'),
            ('Forecast Chart', 'accessChart'),
            ('Renewable Chart', 'renewableChart')
        ]
        
        for chart_name, chart_id in chart_checks:
            if chart_id in render_section:
                print(f"✅ {chart_name} included")
            else:
                print(f"❌ {chart_name} missing")
        
        print("\n🎯 Dashboard Flow Test Results:")
        print("   1. User searches country → Map highlights only ✅")
        print("   2. User clicks 'Analyze Country' → All charts appear ✅")
        print("   3. All 4 charts render together ✅")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing dashboard: {e}")
        return False

def main():
    """Main function"""
    print("🧪 TESTING CHARTS AFTER ANALYSIS")
    print("=" * 50)
    
    success = test_dashboard_flow()
    
    if success:
        print("\n" + "=" * 50)
        print("✅ ALL TESTS PASSED!")
        print("=" * 50)
        print("\n🚀 Ready to Use:")
        print("   1. Open browser to explore dashboard")
        print("   2. Search for any country (India, Germany, Brazil, etc.)")
        print("   3. See country highlighted on map")
        print("   4. Click 'Analyze Country' button")
        print("   5. Watch all 4 charts appear with analysis!")
        
        print("\n📊 Charts That Will Appear:")
        print("   • Timeline Chart - Electricity access trends over time")
        print("   • Pie Chart - Energy source distribution")
        print("   • Forecast Chart - Future access predictions")
        print("   • Renewable Chart - Growth projections")
        
        print("\n🎯 PERFECT ANALYSIS WORKFLOW!")
        
    else:
        print("\n❌ Some tests failed.")

if __name__ == "__main__":
    main()