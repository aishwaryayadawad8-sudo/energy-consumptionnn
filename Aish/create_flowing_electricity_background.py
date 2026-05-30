#!/usr/bin/env python3
"""
Script to create a background showing electricity flowing and passing through circuits
"""

import os

def create_flowing_electricity():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the entire hero section with flowing electricity
    hero_section_start = content.find('        /* Hero Section with Background */')
    if hero_section_start != -1:
        # Find the end of the @keyframes energyWave
        energy_wave_end = content.find('        }', content.find('@keyframes energyWave', hero_section_start))
        if energy_wave_end != -1:
            energy_wave_end = content.find('\n', energy_wave_end) + 1
            
            # Create flowing electricity background
            new_hero_section = '''        /* Hero Section with Background */
        .hero-section {
            background: 
                radial-gradient(ellipse at center, #0a1628 0%, #050b14 50%, #000000 100%);
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
            background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400"><defs><filter id="electricGlow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="4" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter><linearGradient id="flowGrad" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" style="stop-color:%23000000;stop-opacity:0"/><stop offset="20%" style="stop-color:%2300ffff;stop-opacity:0.3"/><stop offset="40%" style="stop-color:%23ffffff;stop-opacity:1"/><stop offset="60%" style="stop-color:%2300d4ff;stop-opacity:0.8"/><stop offset="80%" style="stop-color:%2300ffff;stop-opacity:0.3"/><stop offset="100%" style="stop-color:%23000000;stop-opacity:0"/></linearGradient></defs><g stroke="%23334455" stroke-width="2" fill="none" opacity="0.6"><path d="M0,100 L200,100 L200,150 L400,150 L400,100 L600,100 L600,200 L800,200 L800,150 L1000,150 L1000,100 L1200,100"/><path d="M0,200 L150,200 L150,250 L350,250 L350,200 L550,200 L550,300 L750,300 L750,250 L950,250 L950,200 L1200,200"/><path d="M0,300 L100,300 L100,350 L300,350 L300,300 L500,300 L500,250 L700,250 L700,300 L900,300 L900,350 L1200,350"/></g><g fill="%2300ffff" opacity="0.8" filter="url(%23electricGlow)"><circle cx="200" cy="100" r="4"/><circle cx="400" cy="150" r="4"/><circle cx="600" cy="100" r="4"/><circle cx="800" cy="200" r="4"/><circle cx="1000" cy="150" r="4"/><circle cx="150" cy="200" r="4"/><circle cx="350" cy="250" r="4"/><circle cx="550" cy="200" r="4"/><circle cx="750" cy="300" r="4"/><circle cx="950" cy="250" r="4"/><circle cx="100" cy="300" r="4"/><circle cx="300" cy="350" r="4"/><circle cx="500" cy="300" r="4"/><circle cx="700" cy="250" r="4"/><circle cx="900" cy="300" r="4"/></g></svg>');
            background-size: cover;
            background-position: center;
        }
        
        /* Flowing electricity animation layer 1 */
        .hero-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400"><defs><filter id="flowGlow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter><linearGradient id="electricFlow1" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" style="stop-color:%23000000;stop-opacity:0"/><stop offset="30%" style="stop-color:%2300ffff;stop-opacity:0.5"/><stop offset="50%" style="stop-color:%23ffffff;stop-opacity:1"/><stop offset="70%" style="stop-color:%2300d4ff;stop-opacity:0.5"/><stop offset="100%" style="stop-color:%23000000;stop-opacity:0"/></linearGradient></defs><g stroke="url(%23electricFlow1)" stroke-width="6" fill="none" opacity="1" filter="url(%23flowGlow)"><path d="M0,100 L200,100 L200,150 L400,150 L400,100 L600,100 L600,200 L800,200 L800,150 L1000,150 L1000,100 L1200,100"/></g></svg>');
            background-size: 200% 100%;
            animation: electricFlow1 3s linear infinite;
        }
        
        /* Flowing electricity animation layer 2 */
        .hero-section::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400"><defs><filter id="flowGlow2" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter><linearGradient id="electricFlow2" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" style="stop-color:%23000000;stop-opacity:0"/><stop offset="25%" style="stop-color:%2300d4ff;stop-opacity:0.4"/><stop offset="45%" style="stop-color:%2300ffff;stop-opacity:0.8"/><stop offset="55%" style="stop-color:%23ffffff;stop-opacity:1"/><stop offset="75%" style="stop-color:%2300ffff;stop-opacity:0.4"/><stop offset="100%" style="stop-color:%23000000;stop-opacity:0"/></linearGradient></defs><g stroke="url(%23electricFlow2)" stroke-width="4" fill="none" opacity="0.8" filter="url(%23flowGlow2)"><path d="M0,200 L150,200 L150,250 L350,250 L350,200 L550,200 L550,300 L750,300 L750,250 L950,250 L950,200 L1200,200"/><path d="M0,300 L100,300 L100,350 L300,350 L300,300 L500,300 L500,250 L700,250 L700,300 L900,300 L900,350 L1200,350"/></g></svg>');
            background-size: 200% 100%;
            animation: electricFlow2 4s linear infinite;
        }
        
        @keyframes electricFlow1 {
            0% { background-position: -200% 0; }
            100% { background-position: 200% 0; }
        }
        
        @keyframes electricFlow2 {
            0% { background-position: -200% 0; }
            100% { background-position: 200% 0; }
        }
        
        /* Additional flowing particles */
        .hero-section .flowing-particles {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                radial-gradient(3px 3px at 0% 25%, #00ffff, transparent),
                radial-gradient(2px 2px at 0% 50%, #ffffff, transparent),
                radial-gradient(2px 2px at 0% 75%, #00d4ff, transparent);
            background-size: 100px 400px;
            animation: particleFlow 2s linear infinite;
            opacity: 0.7;
        }
        
        @keyframes particleFlow {
            0% { transform: translateX(-100px); }
            100% { transform: translateX(1300px); }
        }
        
        /* Electrical pulse effect */
        .hero-bg {
            animation: electricPulse 2s ease-in-out infinite alternate;
        }
        
        @keyframes electricPulse {
            0% { opacity: 0.8; filter: brightness(1); }
            100% { opacity: 1; filter: brightness(1.3); }
        }'''
            
            content = content[:hero_section_start] + new_hero_section + content[energy_wave_end:]
            print("✅ Created flowing electricity background")
        else:
            print("⚠️ Could not find animation section end")
            return False
    else:
        print("⚠️ Could not find hero section start")
        return False
    
    # Add the flowing particles div to the HTML
    hero_html_start = content.find('<section class="hero-section">')
    if hero_html_start != -1:
        hero_bg_div = content.find('<div class="hero-bg"></div>', hero_html_start)
        if hero_bg_div != -1:
            hero_bg_end = hero_bg_div + len('<div class="hero-bg"></div>')
            particles_div = '\n        <div class="flowing-particles"></div>'
            content = content[:hero_bg_end] + particles_div + content[hero_bg_end:]
            print("✅ Added flowing particles element")
    
    # Write the updated content
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("⚡ Creating Flowing Electricity Background")
    print("="*60)
    print("   • Electricity flowing through circuits")
    print("   • Animated electrical current paths")
    print("   • Multiple flowing layers")
    print("   • Visible electrical particles")
    print("   • Dynamic current movement")
    print()
    
    if create_flowing_electricity():
        print("\n✅ SUCCESS! Flowing electricity background created!")
        print("\n⚡ Flowing Electricity Features:")
        print("   • Circuit pathways with electrical current flowing")
        print("   • 3 layers of animated electrical flow")
        print("   • Gradient electricity moving through paths")
        print("   • Flowing electrical particles")
        print("   • Connection nodes at circuit junctions")
        print("   • Continuous electrical current animation")
        print("\n🔄 Animation Layers:")
        print("   • Layer 1: Main electrical flow (3-second cycle)")
        print("   • Layer 2: Secondary current paths (4-second cycle)")
        print("   • Layer 3: Flowing particles (2-second cycle)")
        print("   • Background: Electrical pulse effect")
        print("\n⚡ Visual Flow Effects:")
        print("   • Electricity visibly moving left to right")
        print("   • Gradient current showing electrical flow")
        print("   • Multiple circuit paths with different speeds")
        print("   • Glowing electrical connections")
        print("   • Continuous flowing motion")
        print("\n🎯 Perfect Electrical Representation:")
        print("   • Shows actual electricity in motion")
        print("   • Circuit-like pathways")
        print("   • Realistic electrical flow visualization")
        print("   • Dynamic, engaging electrical effects")
        print("   • Professional electrical circuit aesthetic")
        print("\n🔄 Refresh your browser to see electricity flowing!")
    else:
        print("\n❌ Failed to create flowing electricity background")