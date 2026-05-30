#!/usr/bin/env python3
"""
Test that the empty chart section has been removed from Objective 3
"""

import requests

def test_objective3_chart_sections():
    """Test that Objective 3 has the correct chart sections"""
    print("🧪 Testing Objective 3 Chart Sections")
    print("=" * 50)
    
    try:
        response = requests.get("http://127.0.0.1:8000/objective3/", timeout=10)
        
        if response.status_code == 200:
            html_content = response.text
            
            # Check for remaining chart sections
            historical_section = 'id="historicalPercentageSection"' in html_content
            classification_section = 'id="classificationSection"' in html_content
            combined_section = 'id="combinedSection"' in html_content
            
            # Check that the problematic section is removed
            combined_plotly_section = 'id="combinedPlotlySection"' in html_content
            combined_plot_div = 'id="combinedPlot"' in html_content
            plotly_newplot_combined = 'Plotly.newPlot(\'combinedPlot\'' in html_content
            
            print(f"📊 Historical Percentage Section: {historical_section}")
            print(f"📊 Classification Section: {classification_section}")
            print(f"📊 Combined Section: {combined_section}")
            print(f"❌ Combined Plotly Section (should be False): {combined_plotly_section}")
            print(f"❌ Combined Plot Div (should be False): {combined_plot_div}")
            print(f"❌ Plotly NewPlot Combined (should be False): {plotly_newplot_combined}")
            
            # Count total chart sections
            chart_sections = html_content.count('class="section-card"')
            print(f"📊 Total chart sections: {chart_sections}")
            
            if (historical_section and classification_section and combined_section and 
                not combined_plotly_section and not combined_plot_div and not plotly_newplot_combined):
                print("✅ Empty chart section successfully removed")
                return True
            else:
                print("❌ Chart sections have issues")
                return False
        else:
            print(f"❌ Failed to load dashboard: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_objective3_functionality():
    """Test that Objective 3 still functions correctly after removal"""
    print("\n🧪 Testing Objective 3 Functionality")
    print("=" * 50)
    
    try:
        # Test model comparison API
        response = requests.get("http://127.0.0.1:8000/api/objective3/model-comparison/", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            model_comparison_ok = data.get('success', False)
            has_8_models = len(data.get('mse_scores', {})) == 8
            catboost_best = data.get('best_model') == 'CatBoost'
            
            print(f"📊 Model comparison working: {model_comparison_ok}")
            print(f"📈 Has 8 models: {has_8_models}")
            print(f"🏆 CatBoost is best: {catboost_best}")
            
            # Test countries API
            countries_response = requests.get("http://127.0.0.1:8000/api/objective3/countries/", timeout=10)
            countries_ok = countries_response.status_code == 200
            
            print(f"🌍 Countries API working: {countries_ok}")
            
            if model_comparison_ok and has_8_models and catboost_best and countries_ok:
                print("✅ Objective 3 functionality intact")
                return True
            else:
                print("❌ Objective 3 functionality has issues")
                return False
        else:
            print(f"❌ API failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Testing Objective 3 Empty Chart Removal")
    print("=" * 60)
    
    sections_ok = test_objective3_chart_sections()
    functionality_ok = test_objective3_functionality()
    
    print("\n" + "=" * 60)
    print("📋 FINAL RESULTS:")
    
    if sections_ok:
        print("✅ Chart Sections: Empty section removed successfully")
    else:
        print("❌ Chart Sections: Issues found")
    
    if functionality_ok:
        print("✅ Functionality: All APIs working correctly")
    else:
        print("❌ Functionality: Issues found")
    
    if sections_ok and functionality_ok:
        print("\n🎉 SUCCESS! Empty chart section removed successfully")
        print("📊 Objective 3 now has clean chart layout")
        print("🌐 Visit: http://127.0.0.1:8000/objective3/ to verify")
    else:
        print("\n⚠️  Some issues need attention")

if __name__ == "__main__":
    main()