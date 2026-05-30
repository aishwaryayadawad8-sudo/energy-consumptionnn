#!/usr/bin/env python3
"""
Script to replace the hero section background with electric power lines image
"""

import os

def replace_hero_background():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the current SVG background with electric power lines image
    old_background = '''background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 400"><defs><linearGradient id="grid" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="%2300d4ff" stop-opacity="0.3"/><stop offset="50%" stop-color="%2300a8ff" stop-opacity="0.2"/><stop offset="100%" stop-color="%230066ff" stop-opacity="0.1"/></linearGradient></defs><rect width="100%" height="100%" fill="url(%23grid)"/><g stroke="%2300d4ff" stroke-width="1" opacity="0.4"><path d="M0,200 Q250,100 500,200 T1000,200"/><path d="M0,250 Q250,150 500,250 T1000,250"/><path d="M0,300 Q250,200 500,300 T1000,300"/></g><g fill="%2300d4ff" opacity="0.6"><circle cx="100" cy="200" r="3"/><circle cx="300" cy="150" r="3"/><circle cx="500" cy="200" r="3"/><circle cx="700" cy="180" r="3"/><circle cx="900" cy="220" r="3"/></g></svg>');'''
    
    # Create new electric power lines SVG background
    new_background = '''background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400"><defs><linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="%23667eea" stop-opacity="0.9"/><stop offset="50%" stop-color="%23764ba2" stop-opacity="0.8"/><stop offset="100%" stop-color="%23f093fb" stop-opacity="0.7"/></linearGradient><linearGradient id="cityGrad" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="%23ffd89b" stop-opacity="0.8"/><stop offset="100%" stop-color="%23ff9a9e" stop-opacity="0.6"/></linearGradient></defs><rect width="100%" height="100%" fill="url(%23skyGrad)"/><g fill="url(%23cityGrad)" opacity="0.6"><rect x="50" y="300" width="15" height="100"/><rect x="80" y="280" width="20" height="120"/><rect x="120" y="290" width="18" height="110"/><rect x="160" y="270" width="25" height="130"/><rect x="200" y="285" width="22" height="115"/><rect x="240" y="275" width="16" height="125"/><rect x="280" y="295" width="30" height="105"/><rect x="330" y="260" width="20" height="140"/><rect x="370" y="280" width="25" height="120"/><rect x="420" y="270" width="18" height="130"/><rect x="460" y="290" width="22" height="110"/><rect x="500" y="265" width="28" height="135"/><rect x="550" y="285" width="20" height="115"/><rect x="590" y="275" width="24" height="125"/><rect x="640" y="280" width="19" height="120"/><rect x="680" y="270" width="26" height="130"/><rect x="730" y="290" width="21" height="110"/><rect x="770" y="275" width="17" height="125"/><rect x="810" y="285" width="23" height="115"/><rect x="850" y="265" width="27" height="135"/><rect x="900" y="280" width="20" height="120"/><rect x="940" y="275" width="24" height="125"/><rect x="980" y="290" width="18" height="110"/><rect x="1020" y="270" width="25" height="130"/><rect x="1060" y="285" width="22" height="115"/><rect x="1100" y="275" width="19" height="125"/></g><g stroke="%2300d4ff" stroke-width="2" fill="none" opacity="0.8"><polygon points="100,50 120,30 140,50 160,30 180,50 200,30 220,50 240,30 260,50 280,30 300,50"/><polygon points="400,60 420,40 440,60 460,40 480,60 500,40 520,60 540,40 560,60 580,40 600,60"/><polygon points="700,45 720,25 740,45 760,25 780,45 800,25 820,45 840,25 860,45 880,25 900,45"/><polygon points="1000,55 1020,35 1040,55 1060,35 1080,55 1100,35 1120,55"/></g><g stroke="%23ffffff" stroke-width="1" opacity="0.6"><line x1="150" y1="40" x2="150" y2="300"/><line x1="450" y1="50" x2="450" y2="280"/><line x1="750" y1="35" x2="750" y2="270"/><line x1="1050" y1="45" x2="1050" y2="285"/></g><g stroke="%2300d4ff" stroke-width="1" opacity="0.7"><line x1="0" y1="100" x2="150" y2="40"/><line x1="150" y1="40" x2="450" y2="50"/><line x1="450" y1="50" x2="750" y2="35"/><line x1="750" y1="35" x2="1050" y2="45"/><line x1="1050" y1="45" x2="1200" y2="80"/><line x1="0" y1="120" x2="150" y2="60"/><line x1="150" y1="60" x2="450" y2="70"/><line x1="450" y1="70" x2="750" y2="55"/><line x1="750" y1="55" x2="1050" y2="65"/><line x1="1050" y1="65" x2="1200" y2="100"/><line x1="0" y1="140" x2="150" y2="80"/><line x1="150" y1="80" x2="450" y2="90"/><line x1="450" y1="90" x2="750" y2="75"/><line x1="750" y1="75" x2="1050" y2="85"/><line x1="1050" y1="85" x2="1200" y2="120"/></g><g fill="%2300d4ff" opacity="0.9"><circle cx="150" cy="40" r="4"/><circle cx="450" cy="50" r="4"/><circle cx="750" cy="35" r="4"/><circle cx="1050" cy="45" r="4"/></g><g fill="%23ffffff" opacity="0.8"><circle cx="75" cy="70" r="2"/><circle cx="300" cy="65" r="2"/><circle cx="600" cy="60" r="2"/><circle cx="900" cy="55" r="2"/><circle cx="1125" cy="75" r="2"/></g></svg>');'''
    
    if old_background in content:
        content = content.replace(old_background, new_background)
        print("✅ Replaced hero background with electric power lines image")
    else:
        print("⚠️ Could not find the exact background pattern to replace")
        # Try to find and replace just the background-image part
        import re
        pattern = r"background-image: url\('data:image/svg\+xml,[^']+'\);"
        if re.search(pattern, content):
            content = re.sub(pattern, new_background, content)
            print("✅ Updated background using pattern matching")
        else:
            print("❌ Could not locate background image to replace")
            return False
    
    # Write the updated content
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("🔄 Replacing Hero Background Image")
    print("="*60)
    print("   • Removing current SVG grid pattern")
    print("   • Adding electric power lines cityscape")
    print("   • Matching the energy infrastructure theme")
    print()
    
    if replace_hero_background():
        print("\n✅ SUCCESS! Hero background image replaced!")
        print("\n🎨 New Background Features:")
        print("   • Electric power transmission towers")
        print("   • City skyline silhouette")
        print("   • Power lines with connection points")
        print("   • Gradient sky (purple to pink)")
        print("   • Glowing connection nodes")
        print("   • Professional energy infrastructure theme")
        print("\n🎯 Visual Impact:")
        print("   • Matches SDG 7 energy theme perfectly")
        print("   • Professional power grid visualization")
        print("   • Modern electric infrastructure design")
        print("   • Eye-catching gradient background")
        print("\n🔄 Refresh your browser to see the new background!")
    else:
        print("\n❌ Failed to replace background image")