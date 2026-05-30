#!/usr/bin/env python3
"""
Verify that the dashboard now has 9 complete objectives
"""

import requests
import re

def verify_dashboard_objectives():
    """Verify that the main dashboard shows 9 objective cards"""
    print("🎯 Verifying Dashboard Objectives Count")
    print("=" * 50)
    
    try:
        # Test main dashboard page
        response = requests.get("http://127.0.0.1:8000/", timeout=10)
        
        if response.status_code == 200:
            html_content = response.text
            
            # Count objective cards
            objective_cards = re.findall(r'<div class="objective-card">', html_content)
            card_count = len(objective_cards)
            
            print(f"📊 Found {card_count} objective cards")
            
            # Check for specific objective numbers
            objective_numbers = re.findall(r'<div class="objective-number">(\d+)</div>', html_content)
            print(f"📋 Objective numbers found: {sorted(objective_numbers)}")
            
            # Check for Objective 9 specifically
            obj9_found = "Energy Transition Roadmap" in html_content
            route_icon_found = "fas fa-route" in html_content
            
            print(f"🛣️  Objective 9 title found: {obj9_found}")
            print(f"🔗 Route icon found: {route_icon_found}")
            
            if card_count == 9 and obj9_found and route_icon_found and "09" in objective_numbers:
                print("✅ SUCCESS: Dashboard now has 9 complete objectives!")
                return True
            else:
                print("❌ FAIL: Dashboard verification failed")
                return False
        else:
            print(f"❌ FAIL: Dashboard returned status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def verify_objective9_dashboard():
    """Verify that Objective 9 dashboard is accessible"""
    print("\n🎯 Verifying Objective 9 Dashboard")
    print("=" * 50)
    
    try:
        response = requests.get("http://127.0.0.1:8000/objective9/", timeout=10)
        
        if response.status_code == 200:
            html_content = response.text
            
            # Check for key elements
            title_found = "Energy Transition Roadmap" in html_content
            chart_found = "modelComparisonChart" in html_content
            api_calls_found = "/api/objective9/" in html_content
            
            print(f"📊 Title found: {title_found}")
            print(f"📈 Chart elements found: {chart_found}")
            print(f"🔗 API calls found: {api_calls_found}")
            
            if title_found and chart_found and api_calls_found:
                print("✅ SUCCESS: Objective 9 dashboard is working!")
                return True
            else:
                print("❌ FAIL: Objective 9 dashboard verification failed")
                return False
        else:
            print(f"❌ FAIL: Objective 9 dashboard returned status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def main():
    """Main verification function"""
    print("🚀 Complete Dashboard Verification")
    print("=" * 60)
    
    dashboard_ok = verify_dashboard_objectives()
    objective9_ok = verify_objective9_dashboard()
    
    print("\n" + "=" * 60)
    print("📋 FINAL RESULTS:")
    
    if dashboard_ok:
        print("✅ Main Dashboard: 9 objectives working")
    else:
        print("❌ Main Dashboard: Issues found")
    
    if objective9_ok:
        print("✅ Objective 9: Dashboard working")
    else:
        print("❌ Objective 9: Issues found")
    
    if dashboard_ok and objective9_ok:
        print("\n🎉 COMPLETE SUCCESS!")
        print("The dashboard now has 9 fully functional objectives:")
        print("1. Energy Consumption Prediction")
        print("2. CO₂ Emission Forecasting")
        print("3. Energy Access Classification")
        print("4. SDG-7 Progress Monitoring")
        print("5. Energy Equity Analysis")
        print("6. Efficiency Optimization Identification")
        print("7. Renewable Energy Potential Assessment")
        print("8. Sustainable Investment Strategy Support")
        print("9. Energy Transition Roadmap (NEW!)")
        print("\n🌐 Visit: http://127.0.0.1:8000/ to see all 9 objectives")
    else:
        print("\n⚠️  Some issues need attention")

if __name__ == "__main__":
    main()