#!/usr/bin/env python3
"""
Test script to verify animation slowdown:
- Check JavaScript animation speeds are reduced
- Check CSS animation durations are increased
"""

import os

def test_animation_slowdown():
    print("🔍 Testing Animation Slowdown...")
    print("="*60)
    
    # Test 1: Check JavaScript animation speeds
    js_path = "sustainable_energy/static/js/electric-animation.js"
    if os.path.exists(js_path):
        with open(js_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check wave speed
        if "speed: 0.2 + Math.random() * 0.2" in content:
            print("✅ Wave animation speed slowed down (0.2 instead of 0.5)")
        else:
            print("❌ Wave animation speed not slowed down")
            
        # Check particle velocity
        if "(Math.random() - 0.5) * 0.2" in content:
            print("✅ Particle velocity slowed down (0.2 instead of 0.5)")
        else:
            print("❌ Particle velocity not slowed down")
            
        # Check time increment
        if "this.time += 0.005" in content:
            print("✅ Time increment slowed down (0.005 instead of 0.01)")
        else:
            print("❌ Time increment not slowed down")
    else:
        print("❌ JavaScript animation file not found")
    
    # Test 2: Check CSS animation durations in objective selector
    selector_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    if os.path.exists(selector_path):
        with open(selector_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check electric flow animations
        if "electricFlow1 16s linear infinite" in content:
            print("✅ Electric flow 1 slowed down (16s instead of 8s)")
        else:
            print("❌ Electric flow 1 not slowed down")
            
        if "electricFlow2 20s linear infinite" in content:
            print("✅ Electric flow 2 slowed down (20s instead of 10s)")
        else:
            print("❌ Electric flow 2 not slowed down")
            
        if "particleFlow 12s linear infinite" in content:
            print("✅ Particle flow slowed down (12s instead of 6s)")
        else:
            print("❌ Particle flow not slowed down")
            
        if "electricPulse 10s ease-in-out infinite" in content:
            print("✅ Electric pulse slowed down (10s instead of 5s)")
        else:
            print("❌ Electric pulse not slowed down")
    else:
        print("❌ Objective selector file not found")
    
    # Test 3: Check admin panel pulse animation
    admin_path = "sustainable_energy/dashboard/templates/dashboard/admin_panel.html"
    if os.path.exists(admin_path):
        with open(admin_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "animation: pulse 4s infinite" in content:
            print("✅ Admin panel pulse slowed down (4s instead of 2s)")
        else:
            print("❌ Admin panel pulse not slowed down")
    else:
        print("❌ Admin panel file not found")
    
    print("="*60)
    print("🎯 ANIMATION SLOWDOWN SUMMARY:")
    print("   • JavaScript animations: Reduced speed by ~60%")
    print("   • CSS electric flows: Doubled duration (8s→16s, 10s→20s)")
    print("   • Particle animations: Doubled duration (6s→12s)")
    print("   • Pulse effects: Doubled duration (2s→4s, 5s→10s)")
    print("   • Overall effect: Much slower, more relaxed animations")
    print("="*60)

if __name__ == "__main__":
    test_animation_slowdown()