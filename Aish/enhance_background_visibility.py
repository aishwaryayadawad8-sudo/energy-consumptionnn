#!/usr/bin/env python3
"""
Script to enhance the background image visibility with better contrast and brighter elements
"""

import os

def enhance_background_visibility():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the current background and replace with enhanced version
    old_pattern = '''background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400">'''
    
    if old_pattern in content:
        # Create a much more visible and dramatic background
        new_background = '''background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400"><defs><linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="%23001122" stop-opacity="1"/><stop offset="30%" stop-color="%23003366" stop-opacity="1"/><stop offset="70%" stop-color="%23004488" stop-opacity="1"/><stop offset="100%" stop-color="%23002244" stop-opacity="1"/></linearGradient><linearGradient id="cityGrad" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="%23ffaa00" stop-opacity="0.9"/><stop offset="100%" stop-color="%23ff6600" stop-opacity="0.8"/></linearGradient><filter id="glow"><feGaussianBlur stdDeviation="3" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="100%" height="100%" fill="url(%23skyGrad)"/><g fill="url(%23cityGrad)" opacity="0.8"><rect x="50" y="300" width="15" height="100"/><rect x="80" y="280" width="20" height="120"/><rect x="120" y="290" width="18" height="110"/><rect x="160" y="270" width="25" height="130"/><rect x="200" y="285" width="22" height="115"/><rect x="240" y="275" width="16" height="125"/><rect x="280" y="295" width="30" height="105"/><rect x="330" y="260" width="20" height="140"/><rect x="370" y="280" width="25" height="120"/><rect x="420" y="270" width="18" height="130"/><rect x="460" y="290" width="22" height="110"/><rect x="500" y="265" width="28" height="135"/><rect x="550" y="285" width="20" height="115"/><rect x="590" y="275" width="24" height="125"/><rect x="640" y="280" width="19" height="120"/><rect x="680" y="270" width="26" height="130"/><rect x="730" y="290" width="21" height="110"/><rect x="770" y="275" width="17" height="125"/><rect x="810" y="285" width="23" height="115"/><rect x="850" y="265" width="27" height="135"/><rect x="900" y="280" width="20" height="120"/><rect x="940" y="275" width="24" height="125"/><rect x="980" y="290" width="18" height="110"/><rect x="1020" y="270" width="25" height="130"/><rect x="1060" y="285" width="22" height="115"/><rect x="1100" y="275" width="19" height="125"/></g><g fill="%23ffaa00" opacity="0.6"><rect x="60" y="350" width="3" height="3"/><rect x="90" y="340" width="3" height="3"/><rect x="130" y="345" width="3" height="3"/><rect x="170" y="335" width="3" height="3"/><rect x="210" y="350" width="3" height="3"/><rect x="250" y="340" width="3" height="3"/><rect x="290" y="355" width="3" height="3"/><rect x="340" y="330" width="3" height="3"/><rect x="380" y="345" width="3" height="3"/><rect x="430" y="335" width="3" height="3"/><rect x="470" y="350" width="3" height="3"/><rect x="510" y="325" width="3" height="3"/><rect x="560" y="345" width="3" height="3"/><rect x="600" y="335" width="3" height="3"/><rect x="650" y="340" width="3" height="3"/><rect x="690" y="330" width="3" height="3"/><rect x="740" y="350" width="3" height="3"/><rect x="780" y="335" width="3" height="3"/><rect x="820" y="345" width="3" height="3"/><rect x="860" y="325" width="3" height="3"/><rect x="910" y="340" width="3" height="3"/><rect x="950" y="335" width="3" height="3"/><rect x="990" y="350" width="3" height="3"/><rect x="1030" y="330" width="3" height="3"/><rect x="1070" y="345" width="3" height="3"/><rect x="1110" y="335" width="3" height="3"/></g><g stroke="%2300ffff" stroke-width="4" fill="none" opacity="1" filter="url(%23glow)"><polygon points="100,80 120,60 140,80 160,60 180,80 200,60 220,80 240,60 260,80 280,60 300,80"/><polygon points="400,90 420,70 440,90 460,70 480,90 500,70 520,90 540,70 560,90 580,70 600,90"/><polygon points="700,75 720,55 740,75 760,55 780,75 800,55 820,75 840,55 860,75 880,55 900,75"/><polygon points="1000,85 1020,65 1040,85 1060,65 1080,85 1100,65 1120,85"/></g><g stroke="%23ffffff" stroke-width="3" opacity="0.9" filter="url(%23glow)"><line x1="150" y1="70" x2="150" y2="300"/><line x1="450" y1="80" x2="450" y2="280"/><line x1="750" y1="65" x2="750" y2="270"/><line x1="1050" y1="75" x2="1050" y2="285"/></g><g stroke="%2300ffff" stroke-width="2" opacity="0.9" filter="url(%23glow)"><line x1="0" y1="130" x2="150" y2="70"/><line x1="150" y1="70" x2="450" y2="80"/><line x1="450" y1="80" x2="750" y2="65"/><line x1="750" y1="65" x2="1050" y2="75"/><line x1="1050" y1="75" x2="1200" y2="110"/><line x1="0" y1="150" x2="150" y2="90"/><line x1="150" y1="90" x2="450" y2="100"/><line x1="450" y1="100" x2="750" y2="85"/><line x1="750" y1="85" x2="1050" y2="95"/><line x1="1050" y1="95" x2="1200" y2="130"/><line x1="0" y1="170" x2="150" y2="110"/><line x1="150" y1="110" x2="450" y2="120"/><line x1="450" y1="120" x2="750" y2="105"/><line x1="750" y1="105" x2="1050" y2="115"/><line x1="1050" y1="115" x2="1200" y2="150"/></g><g fill="%2300ffff" opacity="1" filter="url(%23glow)"><circle cx="150" cy="70" r="6"/><circle cx="450" cy="80" r="6"/><circle cx="750" cy="65" r="6"/><circle cx="1050" cy="75" r="6"/></g><g fill="%23ffff00" opacity="0.9" filter="url(%23glow)"><circle cx="75" cy="100" r="3"/><circle cx="300" cy="95" r="3"/><circle cx="600" cy="90" r="3"/><circle cx="900" cy="85" r="3"/><circle cx="1125" cy="105" r="3"/></g><g stroke="%2300ffff" stroke-width="1" opacity="0.7" fill="none"><circle cx="150" cy="70" r="15"/><circle cx="450" cy="80" r="15"/><circle cx="750" cy="65" r="15"/><circle cx="1050" cy="75" r="15"/></g></svg>');'''
        
        # Find the start and end of the background-image declaration
        start_pos = content.find('background-image: url(\'data:image/svg+xml,<svg')
        if start_pos != -1:
            end_pos = content.find('</svg>\');', start_pos) + len('</svg>\');')
            if end_pos != -1:
                content = content[:start_pos] + new_background + content[end_pos:]
                print("✅ Enhanced background visibility with brighter elements")
            else:
                print("⚠️ Could not find end of SVG")
                return False
        else:
            print("⚠️ Could not find background image to enhance")
            return False
    else:
        print("⚠️ Background pattern not found")
        return False
    
    # Also enhance the hero section styling for better contrast
    hero_section_css = '''        /* Hero Section with Background */
        .hero-section {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            position: relative;
            height: 400px;
            overflow: hidden;
        }'''
    
    enhanced_hero_css = '''        /* Hero Section with Background */
        .hero-section {
            background: linear-gradient(135deg, #000814 0%, #001d3d 50%, #003566 100%);
            position: relative;
            height: 400px;
            overflow: hidden;
            border-bottom: 3px solid #00d4ff;
        }'''
    
    if hero_section_css in content:
        content = content.replace(hero_section_css, enhanced_hero_css)
        print("✅ Enhanced hero section contrast")
    
    # Write the updated content
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("🔆 Enhancing Background Visibility")
    print("="*60)
    print("   • Increasing contrast and brightness")
    print("   • Adding glowing effects")
    print("   • Making power lines more prominent")
    print("   • Enhancing city lights")
    print()
    
    if enhance_background_visibility():
        print("\n✅ SUCCESS! Background visibility enhanced!")
        print("\n🎨 Enhanced Features:")
        print("   • Darker, more contrasted sky gradient")
        print("   • Bright cyan glowing power lines")
        print("   • Glowing transmission towers")
        print("   • Bright yellow city lights")
        print("   • Enhanced power connection nodes")
        print("   • Glowing effects on all elements")
        print("   • Better contrast with dark background")
        print("\n🔆 Visibility Improvements:")
        print("   • 4x brighter power lines")
        print("   • Glowing filter effects")
        print("   • High contrast colors")
        print("   • Prominent electrical elements")
        print("   • Clear infrastructure visualization")
        print("\n🔄 Refresh your browser to see the enhanced visibility!")
    else:
        print("\n❌ Failed to enhance background visibility")