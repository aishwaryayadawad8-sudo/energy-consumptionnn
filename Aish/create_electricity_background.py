#!/usr/bin/env python3
"""
Script to create an electrical background with lightning bolts and energy effects
"""

import os

def create_electricity_background():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the entire hero section with electrical background
    hero_section_start = content.find('        /* Hero Section with Background */')
    if hero_section_start != -1:
        # Find the end of the hero-bg section
        hero_bg_end = content.find('        }', content.find('.hero-bg {', hero_section_start))
        if hero_bg_end != -1:
            hero_bg_end = content.find('\n', hero_bg_end) + 1
            
            # Create electrical background with lightning bolts
            new_hero_section = '''        /* Hero Section with Background */
        .hero-section {
            background: 
                radial-gradient(ellipse at center, #001122 0%, #000814 50%, #000000 100%);
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
            background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400"><defs><filter id="electricGlow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter><filter id="strongGlow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="8" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter><linearGradient id="lightningGrad" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" style="stop-color:%2300ffff;stop-opacity:1"/><stop offset="50%" style="stop-color:%23ffffff;stop-opacity:0.9"/><stop offset="100%" style="stop-color:%2300d4ff;stop-opacity:0.8"/></linearGradient></defs><g stroke="url(%23lightningGrad)" stroke-width="3" fill="none" opacity="0.9" filter="url(%23electricGlow)"><path d="M100,50 L120,80 L110,120 L130,160 L115,200 L135,240 L120,280 L140,320 L125,360"/><path d="M300,30 L285,70 L295,110 L280,150 L290,190 L275,230 L285,270 L270,310 L280,350"/><path d="M500,60 L520,90 L510,130 L525,170 L515,210 L530,250 L520,290 L535,330 L525,370"/><path d="M700,40 L685,75 L695,115 L680,155 L690,195 L675,235 L685,275 L670,315 L680,355"/><path d="M900,70 L920,100 L910,140 L925,180 L915,220 L930,260 L920,300 L935,340 L925,380"/><path d="M1100,35 L1085,70 L1095,110 L1080,150 L1090,190 L1075,230 L1085,270 L1070,310 L1080,350"/></g><g stroke="%2300ffff" stroke-width="2" fill="none" opacity="0.7" filter="url(%23electricGlow)"><path d="M150,100 Q200,80 250,120 T350,100 Q400,90 450,110 T550,95 Q600,85 650,105 T750,90 Q800,80 850,100 T950,85 Q1000,75 1050,95"/><path d="M80,180 Q130,160 180,200 T280,180 Q330,170 380,190 T480,175 Q530,165 580,185 T680,170 Q730,160 780,180 T880,165 Q930,155 980,175 T1080,160"/><path d="M200,260 Q250,240 300,280 T400,260 Q450,250 500,270 T600,255 Q650,245 700,265 T800,250 Q850,240 900,260 T1000,245 Q1050,235 1100,255"/></g><g fill="%2300ffff" opacity="1" filter="url(%23strongGlow)"><circle cx="100" cy="50" r="4"/><circle cx="300" cy="30" r="4"/><circle cx="500" cy="60" r="4"/><circle cx="700" cy="40" r="4"/><circle cx="900" cy="70" r="4"/><circle cx="1100" cy="35" r="4"/></g><g stroke="%23ffffff" stroke-width="1" fill="none" opacity="0.6"><path d="M50,150 Q100,130 150,170 L200,140 Q250,120 300,160 L350,130 Q400,110 450,150 L500,120 Q550,100 600,140 L650,110 Q700,90 750,130 L800,100 Q850,80 900,120 L950,90 Q1000,70 1050,110 L1100,80 Q1150,60 1200,100"/><path d="M0,220 Q50,200 100,240 L150,210 Q200,190 250,230 L300,200 Q350,180 400,220 L450,190 Q500,170 550,210 L600,180 Q650,160 700,200 L750,170 Q800,150 850,190 L900,160 Q950,140 1000,180 L1050,150 Q1100,130 1150,170 L1200,140"/></g><g fill="%2300d4ff" opacity="0.8"><circle cx="75" cy="125" r="2"/><circle cx="175" cy="145" r="2"/><circle cx="275" cy="135" r="2"/><circle cx="375" cy="155" r="2"/><circle cx="475" cy="145" r="2"/><circle cx="575" cy="165" r="2"/><circle cx="675" cy="155" r="2"/><circle cx="775" cy="175" r="2"/><circle cx="875" cy="165" r="2"/><circle cx="975" cy="185" r="2"/><circle cx="1075" cy="175" r="2"/></g><g stroke="%23ffff00" stroke-width="1" fill="none" opacity="0.5"><path d="M25,300 Q75,280 125,320 L175,290 Q225,270 275,310 L325,280 Q375,260 425,300 L475,270 Q525,250 575,290 L625,260 Q675,240 725,280 L775,250 Q825,230 875,270 L925,240 Q975,220 1025,260 L1075,230 Q1125,210 1175,250"/></g></svg>');
            background-size: cover;
            background-position: center;
            animation: electricPulse 3s ease-in-out infinite alternate;
        }
        
        @keyframes electricPulse {
            0% { opacity: 0.8; }
            100% { opacity: 1; }
        }
        
        /* Add electrical particle effects */
        .hero-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                radial-gradient(2px 2px at 20% 30%, #00ffff, transparent),
                radial-gradient(2px 2px at 40% 70%, #ffffff, transparent),
                radial-gradient(1px 1px at 90% 40%, #00d4ff, transparent),
                radial-gradient(1px 1px at 60% 90%, #ffff00, transparent),
                radial-gradient(2px 2px at 80% 10%, #00ffff, transparent),
                radial-gradient(1px 1px at 10% 80%, #ffffff, transparent);
            background-repeat: repeat;
            background-size: 200px 200px, 300px 300px, 150px 150px, 250px 250px, 180px 180px, 220px 220px;
            animation: sparkle 4s linear infinite;
            opacity: 0.6;
        }
        
        @keyframes sparkle {
            0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 0.6; }
            50% { transform: translateY(-10px) rotate(180deg); opacity: 1; }
        }'''
            
            content = content[:hero_section_start] + new_hero_section + content[hero_bg_end:]
            print("✅ Created electrical background with lightning effects")
        else:
            print("⚠️ Could not find hero-bg section end")
            return False
    else:
        print("⚠️ Could not find hero section start")
        return False
    
    # Write the updated content
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("⚡ Creating Electrical Background with Lightning")
    print("="*60)
    print("   • Dynamic lightning bolts")
    print("   • Electrical arcs and energy patterns")
    print("   • Animated electrical effects")
    print("   • Glowing energy particles")
    print("   • Pulsing electrical animation")
    print()
    
    if create_electricity_background():
        print("\n✅ SUCCESS! Electrical background created!")
        print("\n⚡ Electrical Features:")
        print("   • 6 dynamic lightning bolts with realistic zigzag patterns")
        print("   • Electrical arcs connecting energy points")
        print("   • Glowing energy nodes with strong glow effects")
        print("   • Animated electrical particles floating across screen")
        print("   • Pulsing electrical energy animation")
        print("   • Multiple layers of electrical effects")
        print("\n🌟 Visual Effects:")
        print("   • Realistic lightning bolt patterns")
        print("   • Bright cyan and white electrical colors")
        print("   • Strong glow filters for authentic electrical look")
        print("   • Animated sparkle effects")
        print("   • Pulsing energy animation")
        print("   • Dark background to make electricity pop")
        print("\n⚡ Animation Features:")
        print("   • Continuous electrical pulse animation")
        print("   • Floating energy particles")
        print("   • Dynamic sparkle effects")
        print("   • Smooth, professional animations")
        print("\n🎯 Perfect for Energy Theme:")
        print("   • Represents electrical power and energy")
        print("   • Dynamic, engaging visual effects")
        print("   • Professional electrical aesthetic")
        print("   • Perfect for SDG 7 energy project")
        print("\n🔄 Refresh your browser to see the electrical effects!")
    else:
        print("\n❌ Failed to create electrical background")