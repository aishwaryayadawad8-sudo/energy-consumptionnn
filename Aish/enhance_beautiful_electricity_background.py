#!/usr/bin/env python3
"""
Script to create a beautiful, enhanced electrical background with stunning visual effects
"""

import os

def enhance_beautiful_electricity():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the entire hero section with beautiful electrical background
    hero_section_start = content.find('        /* Hero Section with Background */')
    if hero_section_start != -1:
        # Find the end of the @keyframes sparkle
        sparkle_end = content.find('        }', content.find('@keyframes sparkle', hero_section_start))
        if sparkle_end != -1:
            sparkle_end = content.find('\n', sparkle_end) + 1
            
            # Create beautiful enhanced electrical background
            new_hero_section = '''        /* Hero Section with Background */
        .hero-section {
            background: 
                radial-gradient(ellipse at top, #0a1628 0%, #050b14 50%, #000000 100%);
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
            background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400"><defs><filter id="electricGlow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="5" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter><filter id="superGlow" x="-150%" y="-150%" width="400%" height="400%"><feGaussianBlur stdDeviation="10" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter><linearGradient id="lightningGrad" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" style="stop-color:%2300ffff;stop-opacity:1"/><stop offset="30%" style="stop-color:%2366ffff;stop-opacity:1"/><stop offset="60%" style="stop-color:%23ffffff;stop-opacity:0.9"/><stop offset="100%" style="stop-color:%2300d4ff;stop-opacity:0.8"/></linearGradient><linearGradient id="energyGrad" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" style="stop-color:%2300ffff;stop-opacity:0.8"/><stop offset="50%" style="stop-color:%23ffffff;stop-opacity:1"/><stop offset="100%" style="stop-color:%2300d4ff;stop-opacity:0.8"/></linearGradient><radialGradient id="nodeGlow"><stop offset="0%" style="stop-color:%23ffffff;stop-opacity:1"/><stop offset="30%" style="stop-color:%2300ffff;stop-opacity:0.8"/><stop offset="100%" style="stop-color:%2300d4ff;stop-opacity:0"/></radialGradient></defs><g stroke="url(%23lightningGrad)" stroke-width="4" fill="none" opacity="0.9" filter="url(%23electricGlow)"><path d="M150,20 L165,50 L155,80 L170,110 L160,140 L175,170 L165,200 L180,230 L170,260 L185,290 L175,320 L190,350 L180,380"/><path d="M350,30 L335,60 L345,90 L330,120 L340,150 L325,180 L335,210 L320,240 L330,270 L315,300 L325,330 L310,360 L320,390"/><path d="M550,15 L565,45 L555,75 L570,105 L560,135 L575,165 L565,195 L580,225 L570,255 L585,285 L575,315 L590,345 L580,375"/><path d="M750,25 L735,55 L745,85 L730,115 L740,145 L725,175 L735,205 L720,235 L730,265 L715,295 L725,325 L710,355 L720,385"/><path d="M950,10 L965,40 L955,70 L970,100 L960,130 L975,160 L965,190 L980,220 L970,250 L985,280 L975,310 L990,340 L980,370"/><path d="M1050,35 L1035,65 L1045,95 L1030,125 L1040,155 L1025,185 L1035,215 L1020,245 L1030,275 L1015,305 L1025,335 L1010,365 L1020,395"/></g><g stroke="url(%23energyGrad)" stroke-width="2.5" fill="none" opacity="0.8" filter="url(%23electricGlow)"><path d="M0,100 Q100,80 200,100 T400,100 Q500,90 600,100 T800,100 Q900,90 1000,100 T1200,100"/><path d="M0,150 Q100,130 200,150 T400,150 Q500,140 600,150 T800,150 Q900,140 1000,150 T1200,150"/><path d="M0,200 Q100,180 200,200 T400,200 Q500,190 600,200 T800,200 Q900,190 1000,200 T1200,200"/><path d="M0,250 Q100,230 200,250 T400,250 Q500,240 600,250 T800,250 Q900,240 1000,250 T1200,250"/></g><g fill="url(%23nodeGlow)" opacity="1" filter="url(%23superGlow)"><circle cx="150" cy="20" r="6"/><circle cx="350" cy="30" r="6"/><circle cx="550" cy="15" r="6"/><circle cx="750" cy="25" r="6"/><circle cx="950" cy="10" r="6"/><circle cx="1050" cy="35" r="6"/></g><g stroke="%2300ffff" stroke-width="1.5" fill="none" opacity="0.6" filter="url(%23electricGlow)"><circle cx="150" cy="20" r="20"/><circle cx="350" cy="30" r="20"/><circle cx="550" cy="15" r="20"/><circle cx="750" cy="25" r="20"/><circle cx="950" cy="10" r="20"/><circle cx="1050" cy="35" r="20"/><circle cx="150" cy="20" r="35"/><circle cx="350" cy="30" r="35"/><circle cx="550" cy="15" r="35"/><circle cx="750" cy="25" r="35"/><circle cx="950" cy="10" r="35"/><circle cx="1050" cy="35" r="35"/></g><g fill="%2300ffff" opacity="0.7"><circle cx="200" cy="110" r="2.5"/><circle cx="400" cy="160" r="2.5"/><circle cx="600" cy="120" r="2.5"/><circle cx="800" cy="170" r="2.5"/><circle cx="1000" cy="130" r="2.5"/><circle cx="100" cy="220" r="2"/><circle cx="300" cy="270" r="2"/><circle cx="500" cy="230" r="2"/><circle cx="700" cy="280" r="2"/><circle cx="900" cy="240" r="2"/><circle cx="1100" cy="290" r="2"/></g><g stroke="%23ffffff" stroke-width="1" fill="none" opacity="0.4"><path d="M50,300 Q150,280 250,300 T450,300 Q550,290 650,300 T850,300 Q950,290 1050,300 T1150,300"/><path d="M25,340 Q125,320 225,340 T425,340 Q525,330 625,340 T825,340 Q925,330 1025,340 T1175,340"/></g></svg>');
            background-size: cover;
            background-position: center;
            animation: electricPulse 4s ease-in-out infinite alternate;
        }
        
        @keyframes electricPulse {
            0% { opacity: 0.85; filter: brightness(1); }
            50% { opacity: 1; filter: brightness(1.2); }
            100% { opacity: 0.9; filter: brightness(1.1); }
        }
        
        /* Beautiful electrical particle effects */
        .hero-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                radial-gradient(3px 3px at 15% 25%, rgba(0, 255, 255, 0.8), transparent),
                radial-gradient(2px 2px at 35% 65%, rgba(255, 255, 255, 0.9), transparent),
                radial-gradient(2px 2px at 85% 35%, rgba(0, 212, 255, 0.7), transparent),
                radial-gradient(3px 3px at 55% 85%, rgba(102, 255, 255, 0.8), transparent),
                radial-gradient(2px 2px at 75% 15%, rgba(0, 255, 255, 0.9), transparent),
                radial-gradient(2px 2px at 25% 75%, rgba(255, 255, 255, 0.8), transparent),
                radial-gradient(3px 3px at 95% 55%, rgba(0, 212, 255, 0.7), transparent),
                radial-gradient(2px 2px at 5% 45%, rgba(102, 255, 255, 0.8), transparent);
            background-repeat: repeat;
            background-size: 250px 250px, 350px 350px, 200px 200px, 300px 300px, 220px 220px, 280px 280px, 240px 240px, 320px 320px;
            animation: beautifulSparkle 6s ease-in-out infinite;
            opacity: 0.7;
        }
        
        @keyframes beautifulSparkle {
            0%, 100% { 
                transform: translateY(0px) translateX(0px) rotate(0deg); 
                opacity: 0.7; 
            }
            25% { 
                transform: translateY(-8px) translateX(5px) rotate(90deg); 
                opacity: 0.9; 
            }
            50% { 
                transform: translateY(-15px) translateX(-5px) rotate(180deg); 
                opacity: 1; 
            }
            75% { 
                transform: translateY(-8px) translateX(5px) rotate(270deg); 
                opacity: 0.9; 
            }
        }
        
        /* Additional energy wave effect */
        .hero-section::after {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 200%;
            height: 100%;
            background: linear-gradient(90deg, 
                transparent 0%, 
                rgba(0, 255, 255, 0.1) 25%, 
                rgba(255, 255, 255, 0.2) 50%, 
                rgba(0, 212, 255, 0.1) 75%, 
                transparent 100%);
            animation: energyWave 8s linear infinite;
        }
        
        @keyframes energyWave {
            0% { left: -100%; }
            100% { left: 100%; }
        }'''
            
            content = content[:hero_section_start] + new_hero_section + content[sparkle_end:]
            print("✅ Enhanced beautiful electrical background")
        else:
            print("⚠️ Could not find animation section end")
            return False
    else:
        print("⚠️ Could not find hero section start")
        return False
    
    # Write the updated content
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("✨ Enhancing Electrical Background to Beautiful")
    print("="*60)
    print("   • Richer color gradients")
    print("   • Smoother animations")
    print("   • Enhanced glow effects")
    print("   • Multiple animation layers")
    print("   • Energy wave effects")
    print()
    
    if enhance_beautiful_electricity():
        print("\n✅ SUCCESS! Beautiful electrical background created!")
        print("\n✨ Enhanced Visual Features:")
        print("   • Rich color gradients (cyan to white to blue)")
        print("   • 6 stunning lightning bolts with gradient colors")
        print("   • Multiple glow layers for depth")
        print("   • Radial gradient energy nodes")
        print("   • Concentric energy rings around nodes")
        print("   • Flowing energy wave patterns")
        print("\n🎨 Beautiful Animations:")
        print("   • Smooth electrical pulse (4-second cycle)")
        print("   • Beautiful sparkle animation with rotation")
        print("   • Flowing energy wave across screen (8-second cycle)")
        print("   • Brightness variations for dynamic effect")
        print("   • Multi-directional particle movement")
        print("\n⚡ Sophisticated Effects:")
        print("   • Super glow filters for intense brightness")
        print("   • Gradient lightning bolts (not solid colors)")
        print("   • Radial gradient energy nodes")
        print("   • Multiple particle layers")
        print("   • Smooth wave transitions")
        print("   • Professional color palette")
        print("\n🌟 Visual Enhancements:")
        print("   • Deeper, richer background")
        print("   • More vibrant electrical colors")
        print("   • Enhanced depth with multiple layers")
        print("   • Smoother, more elegant animations")
        print("   • Professional, polished appearance")
        print("\n🎯 Perfect Beauty:")
        print("   • Stunning visual impact")
        print("   • Professional and elegant")
        print("   • Dynamic yet sophisticated")
        print("   • Perfect for energy theme")
        print("   • Eye-catching without being distracting")
        print("\n🔄 Refresh your browser to see the beautiful effects!")
    else:
        print("\n❌ Failed to enhance electrical background")