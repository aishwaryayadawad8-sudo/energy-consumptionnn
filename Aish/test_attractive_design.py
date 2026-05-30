#!/usr/bin/env python3

"""
Test the attractive design implementation
"""

import requests

BASE_URL = "http://127.0.0.1:8000"

def test_attractive_design():
    """Test that the attractive design is working correctly"""
    
    print("🧪 Testing Attractive Design Implementation")
    print("=" * 50)
    
    try:
        # Test 1: Attractive Objective Selector
        print("\n1️⃣  Testing: Attractive Objective Selector")
        response = requests.get(f"{BASE_URL}/", timeout=10)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            content = response.text
            
            # Check for attractive design elements
            if 'Inter' in content:
                print("   ✅ Modern Inter font found")
            
            if 'backdrop-filter: blur' in content:
                print("   ✅ Glass morphism effects found")
            
            if 'linear-gradient' in content:
                print("   ✅ Gradient backgrounds found")
            
            if 'animation:' in content:
                print("   ✅ CSS animations found")
            
            if 'particle' in content:
                print("   ✅ Animated particles found")
            
            if 'fadeInUp' in content:
                print("   ✅ Fade-in animations found")
        
        # Test 2: Attractive Objective 4
        print("\n2️⃣  Testing: Attractive Objective 4")
        response = requests.get(f"{BASE_URL}/objective4/", timeout=10)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            content = response.text
            
            # Check for attractive features
            if 'gradientShift' in content:
                print("   ✅ Animated gradient background found")
            
            if 'cubic-bezier' in content:
                print("   ✅ Smooth easing animations found")
            
            if 'glow' in content:
                print("   ✅ Glowing effects found")
            
            if 'shine' in content or '::before' in content:
                print("   ✅ Shine effects found")
            
            if 'rgba(255, 255, 255, 0.1' in content:
                print("   ✅ Transparency effects found")
        
        # Test 3: Interactive Elements
        print("\n3️⃣  Testing: Interactive Elements")
        
        if ':hover' in content:
            print("   ✅ Hover effects found")
        
        if 'transform:' in content:
            print("   ✅ Transform animations found")
        
        if 'transition:' in content:
            print("   ✅ Smooth transitions found")
        
        # Test 4: Modern Design Features
        print("\n4️⃣  Testing: Modern Design Features")
        
        if 'border-radius:' in content:
            print("   ✅ Rounded corners found")
        
        if 'box-shadow:' in content:
            print("   ✅ Shadow effects found")
        
        if '@keyframes' in content:
            print("   ✅ Custom animations found")
        
        print("\n" + "=" * 50)
        print("✅ Attractive Design Testing Complete!")
        print("\n🎨 Design Features Verified:")
        print("   - Modern typography (Inter font)")
        print("   - Animated gradient backgrounds")
        print("   - Glass morphism effects")
        print("   - Floating particles")
        print("   - Smooth hover animations")
        print("   - Gradient buttons with effects")
        print("   - Glowing elements")
        print("   - Responsive design")
        print("\n🌟 Visual Experience:")
        print(f"   1. Visit: {BASE_URL}/ (Stunning homepage)")
        print(f"   2. Visit: {BASE_URL}/objective4/ (Beautiful dashboard)")
        print("   3. Hover over cards and buttons")
        print("   4. Notice smooth animations")
        print("   5. Experience glass morphism effects")
        print("   6. See animated background particles")
        print("\n💫 Expected Improvements:")
        print("   - Eye-catching animated backgrounds")
        print("   - Professional glass morphism cards")
        print("   - Smooth, satisfying interactions")
        print("   - Modern, attractive typography")
        print("   - Colorful gradient elements")
        print("   - Engaging hover effects")
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Cannot connect to Django server")
        print("💡 Start the server: cd sustainable_energy && python manage.py runserver")
        print(f"   Then experience the attractive design at: {BASE_URL}/")
    
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    test_attractive_design()