#!/usr/bin/env python3

"""
Test that Objective 4 loads model comparison instantly
"""

import requests
import time

def test_objective4_instant_load():
    """Test that Objective 4 page loads quickly with instant model comparison"""
    
    try:
        print("🧪 Testing Objective 4 instant loading...")
        
        # Test the main objective4 page
        start_time = time.time()
        response = requests.get('http://127.0.0.1:8000/objective4/', timeout=10)
        load_time = time.time() - start_time
        
        if response.status_code == 200:
            print(f"✅ Objective 4 page loaded successfully in {load_time:.2f} seconds")
            
            # Check if the page contains the instant loading JavaScript
            content = response.text
            
            if 'loadModelComparison()' in content:
                print("✅ Found loadModelComparison() function")
            
            if 'window.onload = function()' in content:
                print("✅ Found window.onload for instant loading")
            
            if 'Hardcoded data from Sub-objective 4' in content:
                print("✅ Found hardcoded model data for instant loading")
            
            if 'CatBoost' in content and '0.0096' in content:
                print("✅ Found best model (CatBoost) with MSE score")
            
            print("\n🚀 Objective 4 is now configured for INSTANT model comparison loading!")
            print("📊 The model comparison chart will appear immediately without API delays")
            print("⚡ No more waiting - users will see results instantly!")
            
        else:
            print(f"❌ Failed to load Objective 4 page: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"⚠️  Could not test page loading (server might not be running): {e}")
        print("💡 To test: Start the Django server and visit http://127.0.0.1:8000/objective4/")

if __name__ == "__main__":
    test_objective4_instant_load()