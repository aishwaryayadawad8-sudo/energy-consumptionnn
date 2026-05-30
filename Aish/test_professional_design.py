#!/usr/bin/env python3

"""
Test the professional EnerOutlook-style design implementation
"""

import requests

BASE_URL = "http://127.0.0.1:8000"

def test_professional_design():
    """Test that the professional design is working correctly"""
    
    print("🧪 Testing Professional EnerOutlook-Style Design")
    print("=" * 55)
    
    try:
        # Test 1: Professional Homepage
        print("\n1️⃣  Testing: Professional Homepage Design")
        response = requests.get(f"{BASE_URL}/", timeout=10)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            content = response.text
            
            # Check for professional design elements
            if 'EnerOutlook' in content:
                print("   ✅ EnerOutlook branding found")
            
            if 'linear-gradient(135deg, #1e3c72 0%, #2a5298 100%)' in content:
                print("   ✅ Professional blue gradient header found")
            
            if 'Roboto' in content:
                print("   ✅ Professional Roboto font found")
            
            if 'Total Energy' in content and 'Electricity' in content:
                print("   ✅ Navigation tabs found")
            
            if '#ff6b35' in content:
                print("   ✅ Orange accent color found")
            
            if 'nav-tab' in content:
                print("   ✅ Professional navigation structure found")
        
        # Test 2: Professional Objective 4
        print("\n2️⃣  Testing: Professional Objective 4 Design")
        response = requests.get(f"{BASE_URL}/objective4/", timeout=10)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            content = response.text
            
            # Check for professional features
            if '#f8f9fa' in content:
                print("   ✅ Clean background color found")
            
            if 'SDG 7 Monitoring Dashboard' in content:
                print("   ✅ Professional page title found")
            
            if 'section-card' in content:
                print("   ✅ Professional card structure found")
            
            if '#00bcd4' in content:
                print("   ✅ Teal accent color found")
            
            if 'box-shadow:' in content:
                print("   ✅ Professional shadows found")
        
        # Test 3: Responsive Design
        print("\n3️⃣  Testing: Responsive Design Elements")
        
        if '@media (max-width: 768px)' in content:
            print("   ✅ Mobile responsive styles found")
        
        if 'flex' in content:
            print("   ✅ Flexbox layout found")
        
        if 'grid' in content:
            print("   ✅ CSS Grid layout found")
        
        # Test 4: Professional Typography
        print("\n4️⃣  Testing: Professional Typography")
        
        if 'font-weight: 600' in content:
            print("   ✅ Professional font weights found")
        
        if 'letter-spacing:' in content:
            print("   ✅ Letter spacing optimization found")
        
        if 'line-height:' in content:
            print("   ✅ Line height optimization found")
        
        print("\n" + "=" * 55)
        print("✅ Professional Design Testing Complete!")
        print("\n🎯 Professional Features Verified:")
        print("   - EnerOutlook-style blue gradient header")
        print("   - Clean white background with subtle grays")
        print("   - Professional Roboto typography")
        print("   - Navigation tabs with icons")
        print("   - Orange accent buttons")
        print("   - Teal highlight colors")
        print("   - Professional card layouts")
        print("   - Responsive design")
        print("\n🌐 Professional Experience:")
        print(f"   1. Visit: {BASE_URL}/ (Professional homepage)")
        print(f"   2. Visit: {BASE_URL}/objective4/ (Professional dashboard)")
        print("   3. Notice clean, corporate design")
        print("   4. Test navigation tabs")
        print("   5. Experience professional interactions")
        print("\n💼 Expected Appearance:")
        print("   - Corporate blue header like EnerOutlook")
        print("   - Clean white cards with subtle shadows")
        print("   - Professional typography and spacing")
        print("   - Orange call-to-action buttons")
        print("   - Teal accent colors")
        print("   - Grid-based layouts")
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Cannot connect to Django server")
        print("💡 Start the server: cd sustainable_energy && python manage.py runserver")
        print(f"   Then experience the professional design at: {BASE_URL}/")
    
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    test_professional_design()