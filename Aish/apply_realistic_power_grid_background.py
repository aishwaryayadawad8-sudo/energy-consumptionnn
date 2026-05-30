#!/usr/bin/env python3
"""
Script to apply a realistic power grid background matching the reference image
"""

import os

def apply_realistic_background():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the hero section styling
    old_hero_css = '''        /* Hero Section with Background */
        .hero-section {
            background: linear-gradient(135deg, #000814 0%, #001d3d 50%, #003566 100%);
            position: relative;
            height: 400px;
            overflow: hidden;
            border-bottom: 3px solid #00d4ff;
        }
        
        .hero-bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('data:image/svg+xml,'''
    
    # Create new realistic power grid background
    new_hero_css = '''        /* Hero Section with Background */
        .hero-section {
            background: linear-gradient(180deg, 
                #1a2332 0%, 
                #243447 30%, 
                #2d4159 60%, 
                #1f3142 100%);
            position: relative;
            height: 400px;
            overflow: hidden;
        }
        
        .hero-bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                radial-gradient(circle at 20% 30%, rgba(0, 212, 255, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 80% 40%, rgba(0, 212, 255, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 50% 60%, rgba(0, 212, 255, 0.08) 0%, transparent 50%),
                url('data:image/svg+xml,'''
    
    if old_hero_css in content:
        content = content.replace(old_hero_css, new_hero_css)
        print("✅ Updated hero section styling")
    else:
        print("⚠️ Could not find exact hero CSS pattern")
    
    # Find and replace the SVG background with realistic power grid
    start_marker = "background-image: url('data:image/svg+xml,<svg"
    if start_marker in content:
        start_pos = content.find(start_marker)
        end_pos = content.find("</svg>');", start_pos) + len("</svg>');")
        
        if start_pos != -1 and end_pos != -1:
            # Create realistic power transmission tower SVG
            realistic_svg = '''background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" preserveAspectRatio="xMidYMid slice"><defs><linearGradient id="skyGradient" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" style="stop-color:%231a2332;stop-opacity:1"/><stop offset="50%" style="stop-color:%232d4159;stop-opacity:1"/><stop offset="100%" style="stop-color:%231f3142;stop-opacity:1"/></linearGradient><filter id="glow"><feGaussianBlur stdDeviation="2.5" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter><radialGradient id="lightGlow"><stop offset="0%" style="stop-color:%2300d4ff;stop-opacity:0.8"/><stop offset="100%" style="stop-color:%2300d4ff;stop-opacity:0"/></radialGradient></defs><rect width="100%" height="100%" fill="url(%23skyGradient)"/><g opacity="0.4"><circle cx="150" cy="80" r="40" fill="url(%23lightGlow)"/><circle cx="450" cy="100" r="35" fill="url(%23lightGlow)"/><circle cx="750" cy="70" r="45" fill="url(%23lightGlow)"/><circle cx="1050" cy="90" r="38" fill="url(%23lightGlow)"/></g><g stroke="%2300d4ff" stroke-width="1.5" fill="none" opacity="0.6"><line x1="0" y1="150" x2="150" y2="120"/><line x1="150" y1="120" x2="450" y2="140"/><line x1="450" y1="140" x2="750" y2="110"/><line x1="750" y1="110" x2="1050" y2="130"/><line x1="1050" y1="130" x2="1200" y2="160"/><line x1="0" y1="180" x2="150" y2="150"/><line x1="150" y1="150" x2="450" y2="170"/><line x1="450" y1="170" x2="750" y2="140"/><line x1="750" y1="140" x2="1050" y2="160"/><line x1="1050" y1="160" x2="1200" y2="190"/></g><g fill="%23334455" stroke="%23556677" stroke-width="2"><polygon points="140,120 145,100 150,80 155,100 160,120 150,125"/><line x1="150" y1="125" x2="150" y2="250" stroke-width="3"/><polygon points="145,250 150,240 155,250"/><polygon points="440,140 445,120 450,100 455,120 460,140 450,145"/><line x1="450" y1="145" x2="450" y2="270" stroke-width="3"/><polygon points="445,270 450,260 455,270"/><polygon points="740,110 745,90 750,70 755,90 760,110 750,115"/><line x1="750" y1="115" x2="750" y2="240" stroke-width="3"/><polygon points="745,240 750,230 755,240"/><polygon points="1040,130 1045,110 1050,90 1055,110 1060,130 1050,135"/><line x1="1050" y1="135" x2="1050" y2="260" stroke-width="3"/><polygon points="1045,260 1050,250 1055,260"/></g><g stroke="%2300d4ff" stroke-width="2" fill="none" opacity="0.8" filter="url(%23glow)"><line x1="140" y1="100" x2="160" y2="100"/><line x1="145" y1="110" x2="155" y2="110"/><line x1="440" y1="120" x2="460" y2="120"/><line x1="445" y1="130" x2="455" y2="130"/><line x1="740" y1="90" x2="760" y2="90"/><line x1="745" y1="100" x2="755" y2="100"/><line x1="1040" y1="110" x2="1060" y2="110"/><line x1="1045" y1="120" x2="1055" y2="120"/></g><g fill="%2300d4ff" opacity="0.9" filter="url(%23glow)"><circle cx="150" cy="120" r="4"/><circle cx="450" cy="140" r="4"/><circle cx="750" cy="110" r="4"/><circle cx="1050" cy="130" r="4"/></g><g fill="%2300d4ff" opacity="0.6"><circle cx="100" cy="135" r="2"/><circle cx="300" cy="155" r="2"/><circle cx="600" cy="125" r="2"/><circle cx="900" cy="145" r="2"/><circle cx="1100" cy="145" r="2"/></g></svg>');'''
            
            content = content[:start_pos] + realistic_svg + content[end_pos:]
            print("✅ Applied realistic power grid background")
        else:
            print("⚠️ Could not find SVG boundaries")
            return False
    else:
        print("⚠️ Could not find background image marker")
        return False
    
    # Write the updated content
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("🏗️  Applying Realistic Power Grid Background")
    print("="*60)
    print("   • Matching reference image style")
    print("   • Dark blue atmospheric gradient")
    print("   • Realistic transmission towers")
    print("   • Glowing power lines and nodes")
    print()
    
    if apply_realistic_background():
        print("\n✅ SUCCESS! Realistic background applied!")
        print("\n🎨 Background Features:")
        print("   • Dark blue atmospheric gradient (like reference)")
        print("   • Realistic power transmission towers")
        print("   • Glowing cyan power lines")
        print("   • Connection nodes with glow effects")
        print("   • Subtle light halos around towers")
        print("   • Professional energy infrastructure theme")
        print("\n🌟 Visual Style:")
        print("   • Matches the reference image aesthetic")
        print("   • Dark, professional color scheme")
        print("   • Realistic tower silhouettes")
        print("   • Atmospheric lighting effects")
        print("   • Clean, modern design")
        print("\n🔄 Refresh your browser to see the realistic background!")
    else:
        print("\n❌ Failed to apply realistic background")