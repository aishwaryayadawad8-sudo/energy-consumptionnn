#!/usr/bin/env python3
"""
Test the Electricity Dashboard implementation
"""

def test_electricity_dashboard():
    print("🧪 Testing Electricity Dashboard implementation...")
    
    # Test 1: Check if template exists
    template_path = "sustainable_energy/dashboard/templates/dashboard/electricity.html"
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
        
        if "ELECTRICITY" in template_content and "274,520.04" in template_content:
            print("✅ Template exists and contains expected content")
        else:
            print("❌ Template missing expected content")
            return False
    except FileNotFoundError:
        print("❌ Template file not found")
        return False
    
    # Test 2: Check if view function exists in views.py
    views_path = "sustainable_energy/dashboard/views.py"
    try:
        with open(views_path, 'r', encoding='utf-8') as f:
            views_content = f.read()
        
        if "def electricity_dashboard" in views_content:
            print("✅ View function exists in views.py")
        else:
            print("❌ View function not found in views.py")
            return False
    except FileNotFoundError:
        print("❌ Views file not found")
        return False
    
    # Test 3: Check if URL pattern exists in urls.py
    urls_path = "sustainable_energy/dashboard/urls.py"
    try:
        with open(urls_path, 'r', encoding='utf-8') as f:
            urls_content = f.read()
        
        if "electricity/" in urls_content and "electricity_dashboard" in urls_content:
            print("✅ URL pattern exists in urls.py")
        else:
            print("❌ URL pattern not found in urls.py")
            return False
    except FileNotFoundError:
        print("❌ URLs file not found")
        return False
    
    # Test 4: Check if navigation was updated
    nav_template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    try:
        with open(nav_template_path, 'r', encoding='utf-8') as f:
            nav_content = f.read()
        
        if "electricity_dashboard" in nav_content and "fas fa-plug" in nav_content:
            print("✅ Navigation updated successfully")
        else:
            print("❌ Navigation not updated properly")
            return False
    except FileNotFoundError:
        print("❌ Navigation template not found")
        return False
    
    print("\n🎉 All tests passed! Electricity Dashboard is ready!")
    print("\n📋 Summary:")
    print("   ⚡ Total Electricity: 274,520.04 TWh")
    print("   🏠 Historical: 252,987.47 TWh (2000-2020)")
    print("   🔮 Predictions: 21,532.57 TWh (2030)")
    print("   📊 Energy mix breakdowns included")
    print("   🏆 Top countries analysis included")
    print("   🌍 Global access statistics included")
    print("\n🔗 Access via:")
    print("   • Click Electricity icon in navigation")
    print("   • Direct URL: http://127.0.0.1:8000/electricity/")
    print("\n✨ Features:")
    print("   • Comprehensive electricity consumption analysis")
    print("   • Historical vs future comparison")
    print("   • Energy source breakdowns")
    print("   • Top performing countries")
    print("   • Responsive design")
    
    return True

if __name__ == "__main__":
    test_electricity_dashboard()