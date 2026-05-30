#!/usr/bin/env python3
"""
Script to slow down the electricity animation flow for a more elegant effect
"""

import os

def slow_down_animation():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the animation durations
    replacements = [
        # Slow down main electrical flows
        ('animation: electricFlow1 3s linear infinite;', 'animation: electricFlow1 8s linear infinite;'),
        ('animation: electricFlow2 4s linear infinite;', 'animation: electricFlow2 10s linear infinite;'),
        
        # Slow down particle flow
        ('animation: particleFlow 2s linear infinite;', 'animation: particleFlow 6s linear infinite;'),
        
        # Slow down electrical pulse
        ('animation: electricPulse 2s ease-in-out infinite alternate;', 'animation: electricPulse 5s ease-in-out infinite alternate;'),
    ]
    
    changes_made = 0
    for old_text, new_text in replacements:
        if old_text in content:
            content = content.replace(old_text, new_text)
            changes_made += 1
            print(f"✅ Updated: {old_text.split()[1]} -> {new_text.split()[1]}")
    
    if changes_made > 0:
        # Write the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✅ Successfully slowed down {changes_made} animations")
        return True
    else:
        print("⚠️ No animation timings found to update")
        return False

if __name__ == "__main__":
    print("🐌 Slowing Down Electricity Animation Flow")
    print("="*60)
    print("   • Making electrical flow more elegant")
    print("   • Increasing animation durations")
    print("   • Creating smoother, relaxed movement")
    print("   • Better visual comfort")
    print()
    
    if slow_down_animation():
        print("\n✅ SUCCESS! Animation flow slowed down!")
        print("\n🐌 New Animation Speeds:")
        print("   • Main electrical flow: 3s → 8s (much slower)")
        print("   • Secondary flow: 4s → 10s (more relaxed)")
        print("   • Particle flow: 2s → 6s (gentler movement)")
        print("   • Electrical pulse: 2s → 5s (calmer pulsing)")
        print("\n🎯 Benefits:")
        print("   • More elegant and sophisticated")
        print("   • Easier to follow the electrical flow")
        print("   • Less distracting, more professional")
        print("   • Smoother, more relaxed visual experience")
        print("   • Better for reading content over the background")
        print("\n⚡ Visual Impact:")
        print("   • Electricity flows gracefully across circuits")
        print("   • Smooth, continuous electrical movement")
        print("   • Professional, calming electrical effects")
        print("   • Perfect balance of motion and elegance")
        print("\n🔄 Refresh your browser to see the slower, elegant flow!")
    else:
        print("\n❌ Failed to slow down animations")