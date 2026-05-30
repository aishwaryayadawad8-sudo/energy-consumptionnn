#!/usr/bin/env python3
"""
Test that Objectives 8 and 9 have been swapped correctly
"""

import requests
import json

def test_main_dashboard():
    """Test that the main dashboard shows correct objectives"""
    print("🧪 Testing Main Dashboard Objectives")
    print("=" * 50)
    
    try:
        response = requests.get("http://127.0.0.1:8000/", timeout=10)
        
        if response.status_code == 200:
            html_content = response.text
            
            # Check for Objective 8 (Admin Panel)
            obj8_admin = "Admin Panel" in html_content
            obj8_cog_icon = "fas fa-cog" in html_content
            obj8_admin_link = 'href="/admin-panel/"' in html_content
            
            # Check for Objective 9 (Investment Strategy)
            obj9_investment = "Sustainable Investment Strategy Support" in html_content
            obj9_chart_icon = "fas fa-chart-pie" in html_content
            obj9_dashboard_link = "objective9_dashboard" in html_content
            
            print(f"📊 Objective 8 - Admin Panel title: {obj8_admin}")
            print(f"⚙️  Objective 8 - Cog icon: {obj8_cog_icon}")
            print(f"🔗 Objective 8 - Admin panel link: {obj8_admin_link}")
            print(f"📈 Objective 9 - Investment title: {obj9_investment}")
            print(f"📊 Objective 9 - Chart pie icon: {obj9_chart_icon}")
            print(f"🔗 Objective 9 - Dashboard link: {obj9_dashboard_link}")
            
            if obj8_admin and obj8_cog_icon and obj9_investment and obj9_chart_icon:
                print("✅ Dashboard objectives are correctly swapped")
                return True
            else:
                print("❌ Dashboard objectives swap has issues")
                return False
        else:
            print(f"❌ Failed to load dashboard: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_objective9_api():
    """Test that Objective 9 API works with investment strategy"""
    print("\n🧪 Testing Objective 9 API (Investment Strategy)")
    print("=" * 50)
    
    try:
        # Test model comparison
        response = requests.get("http://127.0.0.1:8000/api/objective9/model-comparison/", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            investment_theme = data.get('objective_name') == 'Sustainable Investment Strategy Support'
            catboost_best = data.get('best_model') == 'CatBoost'
            correct_score = abs(data.get('best_score', 0) - 0.0047) < 0.001
            
            print(f"📊 Investment theme: {investment_theme}")
            print(f"🏆 CatBoost is best: {catboost_best}")
            print(f"📈 Correct score (0.0047): {correct_score}")
            
            if investment_theme and catboost_best and correct_score:
                print("✅ Objective 9 API is correctly updated")
                return True
            else:
                print("❌ Objective 9 API has issues")
                return False
        else:
            print(f"❌ API failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_objective9_dashboard():
    """Test that Objective 9 dashboard loads with investment theme"""
    print("\n🧪 Testing Objective 9 Dashboard (Investment Theme)")
    print("=" * 50)
    
    try:
        response = requests.get("http://127.0.0.1:8000/objective9/", timeout=10)
        
        if response.status_code == 200:
            html_content = response.text
            
            # Check for investment-related content
            investment_title = "Sustainable Investment Strategy Support" in html_content
            investment_analysis = "Investment Strategy Analysis" in html_content
            analyze_investment = "Analyze Investment" in html_content
            chart_pie_icon = "fas fa-chart-pie" in html_content
            
            print(f"📊 Investment title: {investment_title}")
            print(f"📈 Investment analysis: {investment_analysis}")
            print(f"🔍 Analyze investment button: {analyze_investment}")
            print(f"📊 Chart pie icon: {chart_pie_icon}")
            
            if investment_title and investment_analysis and analyze_investment:
                print("✅ Objective 9 dashboard has investment theme")
                return True
            else:
                print("❌ Objective 9 dashboard theme has issues")
                return False
        else:
            print(f"❌ Dashboard failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Testing Objectives 8 & 9 Swap")
    print("=" * 60)
    
    dashboard_ok = test_main_dashboard()
    api_ok = test_objective9_api()
    dashboard_theme_ok = test_objective9_dashboard()
    
    print("\n" + "=" * 60)
    print("📋 FINAL RESULTS:")
    
    if dashboard_ok:
        print("✅ Main Dashboard: Objectives correctly swapped")
    else:
        print("❌ Main Dashboard: Issues found")
    
    if api_ok:
        print("✅ Objective 9 API: Investment strategy working")
    else:
        print("❌ Objective 9 API: Issues found")
    
    if dashboard_theme_ok:
        print("✅ Objective 9 Dashboard: Investment theme applied")
    else:
        print("❌ Objective 9 Dashboard: Theme issues")
    
    if dashboard_ok and api_ok and dashboard_theme_ok:
        print("\n🎉 SUCCESS! Objectives 8 & 9 swap completed successfully")
        print("📊 Objective 8: Admin Panel (with cog icon)")
        print("📈 Objective 9: Sustainable Investment Strategy Support (with chart-pie icon)")
        print("\n🌐 Visit: http://127.0.0.1:8000/ to see the updated objectives")
    else:
        print("\n⚠️  Some issues need attention")

if __name__ == "__main__":
    main()