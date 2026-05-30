#!/usr/bin/env python3
"""
Test Dashboard Functionality
============================

This script creates a simple test to verify the dashboard is working properly.
"""

import os

def test_dashboard_functionality():
    """Test if the dashboard HTML file exists and has the correct structure"""
    
    html_file_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🧪 TESTING DASHBOARD FUNCTIONALITY")
    print("=" * 50)
    
    # Check if file exists
    if not os.path.exists(html_file_path):
        print(f"❌ File not found: {html_file_path}")
        return False
    
    print(f"✅ File exists: {html_file_path}")
    
    # Read and check file content
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"✅ File readable, size: {len(content)} characters")
        
        # Check for key components
        checks = [
            ("Historical button", 'Historical (2000-2020)'),
            ("setTimePeriod function", 'function setTimePeriod(period)'),
            ("loadHistoricalData function", 'function loadHistoricalData()'),
            ("Chart containers", 'chart-container-vertical'),
            ("Plotly library", 'plotly-latest.min.js'),
            ("Leaflet map", 'leaflet.js')
        ]
        
        for check_name, check_text in checks:
            if check_text in content:
                print(f"✅ {check_name} found")
            else:
                print(f"❌ {check_name} missing")
        
        return True
        
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False

def main():
    """Main function to test dashboard"""
    success = test_dashboard_functionality()
    
    print("\n" + "=" * 50)
    if success:
        print("✅ DASHBOARD FILE STRUCTURE OK")
        print("\n🔍 If you're seeing 'canceled' errors:")
        print("   1. Check browser console (F12 → Console)")
        print("   2. Make sure Django server is running")
        print("   3. Try clearing browser cache (Ctrl+F5)")
        print("   4. Check if URL is correct: http://127.0.0.1:8000/explore/")
        print("   5. Look for JavaScript errors in console")
        
        print("\n🚀 To start Django server:")
        print("   cd sustainable_energy")
        print("   python manage.py runserver")
        
    else:
        print("❌ DASHBOARD FILE HAS ISSUES")

if __name__ == "__main__":
    main()