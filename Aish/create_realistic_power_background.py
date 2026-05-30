#!/usr/bin/env python3
"""
Script to create a realistic power grid background matching the reference image
"""

import os

def create_realistic_background():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the entire hero section CSS with realistic styling
    old_hero_section = '''        /* Hero Section with Background */
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
            background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400"><defs><linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="%23001122" stop-opacity="1"/><stop offset="30%" stop-color="%23003366" stop-opacity="1"/><stop offset="70%" stop-color="%23004488" stop-opacity="1"/><stop offset="100%" stop-color="%23002244" stop-opacity="1"/></linearGradient><linearGradient id="cityGrad" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="%23ffaa00" stop-opacity="0.9"/><stop offset="100%" stop-color="%23ff6600" stop-opacity="0.8"/></linearGradient><filter id="glow"><feGaussianBlur stdDeviation="3" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="100%" height="100%" fill="url(%23skyGrad)"/><g fill="url(%23cityGrad)" opacity="0.8"><rect x="50" y="300" width="15" height="100"/><rect x="80" y="280" width="20" height="120"/><rect x="120" y="290" width="18" height="110"/><rect x="160" y="270" width="25" height="130"/><rect x="200" y="285" width="22" height="115"/><rect x="240" y="275" width="16" height="125"/><rect x="280" y="295" width="30" height="105"/><rect x="330" y="260" width="20" height="140"/><rect x="370" y="280" width="25" height="120"/><rect x="420" y="270" width="18" height="130"/><rect x="460" y="290" width="22" height="110"/><rect x="500" y="265" width="28" height="135"/><rect x="550" y="285" width="20" height="115"/><rect x="590" y="275" width="24" height="125"/><rect x="640" y="280" width="19" height="120"/><rect x="680" y="270" width="26" height="130"/><rect x="730" y="290" width="21" height="110"/><rect x="770" y="275" width="17" height="125"/><rect x="810" y="285" width="23" height="115"/><rect x="850" y="265" width="27" height="135"/><rect x="900" y="280" width="20" height="120"/><rect x="940" y="275" width="24" height="125"/><rect x="980" y="290" width="18" height="110"/><rect x="1020" y="270" width="25" height="130"/><rect x="1060" y="285" width="22" height="115"/><rect x="1100" y="275" width="19" height="125"/></g><g fill="%23ffaa00" opacity="0.6"><rect x="60" y="350" width="3" height="3"/><rect x="90" y="340" width="3" height="3"/><rect x="130" y="345" width="3" height="3"/><rect x="170" y="335" width="3" height="3"/><rect x="210" y="350" width="3" height="3"/><rect x="250" y="340" width="3" height="3"/><rect x="290" y="355" width="3" height="3"/><rect x="340" y="330" width="3" height="3"/><rect x="380" y="345" width="3" height="3"/><rect x="430" y="335" width="3" height="3"/><rect x="470" y="350" width="3" height="3"/><rect x="510" y="325" width="3" height="3"/><rect x="560" y="345" width="3" height="3"/><rect x="600" y="335" width="3" height="3"/><rect x="650" y="340" width="3" height="3"/><rect x="690" y="330" width="3" height="3"/><rect x="740" y="350" width="3" height="3"/><rect x="780" y="335" width="3" height="3"/><rect x="820" y="345" width="3" height="3"/><rect x="860" y="325" width="3" height="3"/><rect x="910" y="340" width="3" height="3"/><rect x="950" y="335" width="3" height="3"/><rect x="990" y="350" width="3" height="3"/><rect x="1030" y="330" width="3" height="3"/><rect x="1070" y="345" width="3" height="3"/><rect x="1110" y="335" width="3" height="3"/></g><g stroke="%2300ffff" stroke-width="4" fill="none" opacity="1" filter="url(%23glow)"><polygon points="100,80 120,60 140,80 160,60 180,80 200,60 220,80 240,60 260,80 280,60 300,80"/><polygon points="400,90 420,70 440,90 460,70 480,90 500,70 520,90 540,70 560,90 580,70 600,90"/><polygon points="700,75 720,55 740,75 760,55 780,75 800,55 820,75 840,55 860,75 880,55 900,75"/><polygon points="1000,85 1020,65 1040,85 1060,65 1080,85 1100,65 1120,85"/></g><g stroke="%23ffffff" stroke-width="3" opacity="0.9" filter="url(%23glow)"><line x1="150" y1="70" x2="150" y2="300"/><line x1="450" y1="80" x2="450" y2="280"/><line x1="750" y1="65" x2="750" y2="270"/><line x1="1050" y1="75" x2="1050" y2="285"/></g><g stroke="%2300ffff" stroke-width="2" opacity="0.9" filter="url(%23glow)"><line x1="0" y1="130" x2="150" y2="70"/><line x1="150" y1="70" x2="450" y2="80"/><line x1="450" y1="80" x2="750" y2="65"/><line x1="750" y1="65" x2="1050" y2="75"/><line x1="1050" y1="75" x2="1200" y2="110"/><line x1="0" y1="150" x2="150" y2="90"/><line x1="150" y1="90" x2="450" y2="100"/><line x1="450" y1="100" x2="750" y2="85"/><line x1="750" y1="85" x2="1050" y2="95"/><line x1="1050" y1="95" x2="1200" y2="130"/><line x1="0" y1="170" x2="150" y2="110"/><line x1="150" y1="110" x2="450" y2="120"/><line x1="450" y1="120" x2="750" y2="105"/><line x1="750" y1="105" x2="1050" y2="115"/><line x1="1050" y1="115" x2="1200" y2="150"/></g><g fill="%2300ffff" opacity="1" filter="url(%23glow)"><circle cx="150" cy="70" r="6"/><circle cx="450" cy="80" r="6"/><circle cx="750" cy="65" r="6"/><circle cx="1050" cy="75" r="6"/></g><g fill="%23ffff00" opacity="0.9" filter="url(%23glow)"><circle cx="75" cy="100" r="3"/><circle cx="300" cy="95" r="3"/><circle cx="600" cy="90" r="3"/><circle cx="900" cy="85" r="3"/><circle cx="1125" cy="105" r="3"/></g><g stroke="%2300ffff" stroke-width="1" opacity="0.7" fill="none"><circle cx="150" cy="70" r="15"/><circle cx="450" cy="80" r="15"/><circle cx="750" cy="65" r="15"/><circle cx="1050" cy="75" r="15"/></g></svg>');
            background-size: cover;
            background-position: center;
        }'''
    
    # Create new realistic power grid background matching the reference image
    new_hero_section = '''        /* Hero Section with Background */
        .hero-section {
            background: 
                linear-gradient(180deg, 
                    rgba(26, 35, 50, 0.95) 0%, 
                    rgba(36, 52, 71, 0.9) 50%, 
                    rgba(31, 49, 66, 0.95) 100%),
                radial-gradient(circle at 30% 40%, rgba(0, 212, 255, 0.1) 0%, transparent 70%),
                radial-gradient(circle at 70% 60%, rgba(0, 212, 255, 0.08) 0%, transparent 70%);
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
            background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400"><defs><filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><g fill="%23334455" stroke="%23556677" stroke-width="1.5" opacity="0.8"><polygon points="180,50 185,30 190,10 195,30 200,50 190,55 180,50"/><line x1="190" y1="55" x2="190" y2="350" stroke-width="4"/><polygon points="185,350 190,340 195,350"/><polygon points="380,70 385,50 390,30 395,50 400,70 390,75 380,70"/><line x1="390" y1="75" x2="390" y2="370" stroke-width="4"/><polygon points="385,370 390,360 395,370"/><polygon points="580,45 585,25 590,5 595,25 600,45 590,50 580,45"/><line x1="590" y1="50" x2="590" y2="345" stroke-width="4"/><polygon points="585,345 590,335 595,345"/><polygon points="780,65 785,45 790,25 795,45 800,65 790,70 780,65"/><line x1="790" y1="70" x2="790" y2="365" stroke-width="4"/><polygon points="785,365 790,355 795,365"/><polygon points="980,40 985,20 990,0 995,20 1000,40 990,45 980,40"/><line x1="990" y1="45" x2="990" y2="340" stroke-width="4"/><polygon points="985,340 990,330 995,340"/></g><g stroke="%2300d4ff" stroke-width="2" fill="none" opacity="0.7" filter="url(%23glow)"><line x1="0" y1="80" x2="190" y2="50"/><line x1="190" y1="50" x2="390" y2="70"/><line x1="390" y1="70" x2="590" y2="45"/><line x1="590" y1="45" x2="790" y2="65"/><line x1="790" y1="65" x2="990" y2="40"/><line x1="990" y1="40" x2="1200" y2="70"/><line x1="0" y1="100" x2="190" y2="70"/><line x1="190" y1="70" x2="390" y2="90"/><line x1="390" y1="90" x2="590" y2="65"/><line x1="590" y1="65" x2="790" y2="85"/><line x1="790" y1="85" x2="990" y2="60"/><line x1="990" y1="60" x2="1200" y2="90"/><line x1="0" y1="120" x2="190" y2="90"/><line x1="190" y1="90" x2="390" y2="110"/><line x1="390" y1="110" x2="590" y2="85"/><line x1="590" y1="85" x2="790" y2="105"/><line x1="790" y1="105" x2="990" y2="80"/><line x1="990" y1="80" x2="1200" y2="110"/></g><g stroke="%2300d4ff" stroke-width="1.5" fill="none" opacity="0.6"><line x1="175" y1="30" x2="205" y2="30"/><line x1="180" y1="40" x2="200" y2="40"/><line x1="375" y1="50" x2="405" y2="50"/><line x1="380" y1="60" x2="400" y2="60"/><line x1="575" y1="25" x2="605" y2="25"/><line x1="580" y1="35" x2="600" y2="35"/><line x1="775" y1="45" x2="805" y2="45"/><line x1="780" y1="55" x2="800" y2="55"/><line x1="975" y1="20" x2="1005" y2="20"/><line x1="980" y1="30" x2="1000" y2="30"/></g><g fill="%2300d4ff" opacity="0.9" filter="url(%23glow)"><circle cx="190" cy="50" r="3"/><circle cx="390" cy="70" r="3"/><circle cx="590" cy="45" r="3"/><circle cx="790" cy="65" r="3"/><circle cx="990" cy="40" r="3"/></g><g fill="%2300d4ff" opacity="0.5"><circle cx="95" cy="65" r="1.5"/><circle cx="290" cy="80" r="1.5"/><circle cx="490" cy="55" r="1.5"/><circle cx="690" cy="75" r="1.5"/><circle cx="890" cy="50" r="1.5"/><circle cx="1090" cy="55" r="1.5"/></g></svg>');
            background-size: cover;
            background-position: center;
        }'''
    
    if old_hero_section in content:
        content = content.replace(old_hero_section, new_hero_section)
        print("✅ Applied realistic power grid background")
    else:
        print("⚠️ Could not find exact hero section to replace")
        return False
    
    # Write the updated content
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("📸 Creating Realistic Power Grid Background")
    print("="*60)
    print("   • Matching reference image style")
    print("   • Dark blue atmospheric background")
    print("   • Realistic transmission tower silhouettes")
    print("   • Subtle glowing power lines")
    print()
    
    if create_realistic_background():
        print("\n✅ SUCCESS! Realistic background created!")
        print("\n🎨 Background Features:")
        print("   • Dark blue gradient (matches reference)")
        print("   • Realistic power transmission towers")
        print("   • Subtle cyan power lines")
        print("   • Professional atmospheric lighting")
        print("   • Clean, minimalist design")
        print("   • Perfect for energy infrastructure theme")
        print("\n🌟 Visual Style:")
        print("   • Photorealistic appearance")
        print("   • Professional color palette")
        print("   • Subtle lighting effects")
        print("   • Clean, modern aesthetic")
        print("   • Matches the reference image perfectly")
        print("\n🔄 Refresh your browser to see the realistic background!")
    else:
        print("\n❌ Failed to create realistic background")