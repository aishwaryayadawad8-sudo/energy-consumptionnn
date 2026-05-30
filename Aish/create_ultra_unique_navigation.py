#!/usr/bin/env python3

"""
Create ultra-unique navigation with holographic effects, energy waves, and particle animations
"""

def create_ultra_unique_navigation():
    """Create the most unique navigation design with advanced effects"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the navigation CSS
        old_css_start = '        /* Navigation Icons Section - 3D Energy Theme */'
        
        # Find the navigation CSS section
        start_index = content.find(old_css_start)
        if start_index != -1:
            # Find the end of the navigation CSS section
            temp_content = content[start_index:]
            brace_count = 0
            end_offset = 0
            in_nav_section = False
            
            for i, char in enumerate(temp_content):
                if char == '{':
                    brace_count += 1
                    in_nav_section = True
                elif char == '}':
                    brace_count -= 1
                    if in_nav_section and brace_count == 0:
                        # Check if next section starts
                        next_section = temp_content[i:i+100]
                        if '\n        @media' in next_section or '\n        .' in next_section or '\n        /*' in next_section:
                            if '/* Navigation' not in next_section[:50]:
                                end_offset = i + 1
                                break
            
            if end_offset > 0:
                end_index = start_index + end_offset
                
                # Create the ultra-unique CSS with holographic and energy effects
                ultra_unique_css = '''        /* Ultra-Unique Navigation - Holographic Energy System */
        .navigation-icons-section {
            background: 
                radial-gradient(circle at 20% 50%, rgba(30, 60, 114, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 50%, rgba(255, 107, 53, 0.1) 0%, transparent 50%),
                linear-gradient(135deg, #f8f9fa 0%, #ffffff 50%, #f0f4f8 100%);
            padding: 60px 0;
            border-bottom: 1px solid transparent;
            position: relative;
            overflow: hidden;
            perspective: 1200px;
        }
        
        /* Animated Energy Wave Background */
        .navigation-icons-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            right: -100%;
            height: 100%;
            background: 
                linear-gradient(90deg, 
                    transparent 0%, 
                    rgba(255, 107, 53, 0.05) 25%, 
                    rgba(30, 60, 114, 0.05) 50%, 
                    rgba(255, 107, 53, 0.05) 75%, 
                    transparent 100%);
            animation: energyWave 8s ease-in-out infinite;
            z-index: 0;
        }
        
        /* Floating Particles */
        .navigation-icons-section::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: 
                radial-gradient(2px 2px at 20px 30px, rgba(255, 107, 53, 0.3), transparent),
                radial-gradient(2px 2px at 40px 70px, rgba(30, 60, 114, 0.3), transparent),
                radial-gradient(1px 1px at 90px 40px, rgba(255, 165, 0, 0.4), transparent),
                radial-gradient(1px 1px at 130px 80px, rgba(42, 82, 152, 0.3), transparent),
                radial-gradient(2px 2px at 160px 30px, rgba(255, 107, 53, 0.2), transparent);
            background-repeat: repeat;
            background-size: 200px 100px;
            animation: particleFloat 15s linear infinite;
            z-index: 0;
        }
        
        .nav-icons-row {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            gap: 70px;
            position: relative;
            z-index: 1;
            transform-style: preserve-3d;
        }
        
        .nav-icon-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-decoration: none;
            color: #2c3e50;
            transition: all 0.8s cubic-bezier(0.23, 1, 0.32, 1);
            padding: 25px;
            position: relative;
            transform-style: preserve-3d;
            transform: translateZ(0) rotateX(0deg) rotateY(0deg);
        }
        
        /* Holographic Base Effect */
        .nav-icon-item::before {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%) translateZ(-20px);
            width: 120px;
            height: 8px;
            background: 
                linear-gradient(90deg, 
                    transparent 0%, 
                    rgba(255, 107, 53, 0.6) 20%, 
                    rgba(30, 60, 114, 0.8) 50%, 
                    rgba(255, 107, 53, 0.6) 80%, 
                    transparent 100%);
            border-radius: 50%;
            opacity: 0;
            transition: all 0.8s ease;
            filter: blur(2px);
            animation: hologramPulse 3s ease-in-out infinite;
        }
        
        /* Energy Field Effect */
        .nav-icon-item::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) translateZ(-30px);
            width: 150px;
            height: 150px;
            background: 
                conic-gradient(from 0deg, 
                    transparent 0deg, 
                    rgba(255, 107, 53, 0.1) 90deg, 
                    rgba(30, 60, 114, 0.1) 180deg, 
                    rgba(255, 165, 0, 0.1) 270deg, 
                    transparent 360deg);
            border-radius: 50%;
            opacity: 0;
            transition: all 0.8s ease;
            animation: energyField 4s linear infinite;
        }
        
        .nav-icon-item:hover::before {
            opacity: 1;
            width: 140px;
            height: 12px;
        }
        
        .nav-icon-item:hover::after {
            opacity: 1;
            transform: translate(-50%, -50%) translateZ(-30px) scale(1.2);
        }
        
        .nav-icon-item:hover {
            transform: translateZ(40px) rotateX(-15deg) rotateY(8deg) translateY(-15px);
        }
        
        .nav-icon-circle {
            width: 90px;
            height: 90px;
            border-radius: 50%;
            background: 
                linear-gradient(145deg, 
                    rgba(255, 255, 255, 0.9) 0%, 
                    rgba(248, 249, 250, 0.8) 30%, 
                    rgba(240, 244, 248, 0.7) 70%, 
                    rgba(232, 238, 245, 0.9) 100%);
            border: 2px solid transparent;
            background-clip: padding-box;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 18px;
            transition: all 0.8s cubic-bezier(0.23, 1, 0.32, 1);
            position: relative;
            overflow: hidden;
            transform-style: preserve-3d;
            
            /* Holographic Border */
            box-shadow: 
                0 0 0 1px rgba(255, 107, 53, 0.3),
                0 8px 32px rgba(0, 0, 0, 0.1),
                0 4px 16px rgba(0, 0, 0, 0.08),
                inset 0 1px 0 rgba(255, 255, 255, 0.9),
                inset 0 -1px 0 rgba(0, 0, 0, 0.1);
        }
        
        /* Holographic Shimmer Effect */
        .nav-icon-circle::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: 
                linear-gradient(45deg, 
                    transparent 30%, 
                    rgba(255, 255, 255, 0.8) 50%, 
                    transparent 70%);
            transform: translateZ(1px) rotate(0deg);
            transition: transform 0.8s ease;
            opacity: 0;
        }
        
        /* Energy Core */
        .nav-icon-circle::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) translateZ(2px);
            width: 60%;
            height: 60%;
            background: 
                radial-gradient(circle, 
                    rgba(255, 107, 53, 0.1) 0%, 
                    rgba(30, 60, 114, 0.1) 50%, 
                    transparent 100%);
            border-radius: 50%;
            animation: energyCore 3s ease-in-out infinite alternate;
        }
        
        .nav-icon-item:hover .nav-icon-circle {
            transform: translateZ(25px) rotateX(-20deg) scale(1.2);
            box-shadow: 
                0 0 0 2px rgba(255, 107, 53, 0.6),
                0 0 20px rgba(255, 107, 53, 0.4),
                0 20px 60px rgba(255, 107, 53, 0.2),
                0 10px 30px rgba(0, 0, 0, 0.2),
                inset 0 2px 0 rgba(255, 255, 255, 1),
                inset 0 -2px 0 rgba(0, 0, 0, 0.2);
        }
        
        .nav-icon-item:hover .nav-icon-circle::before {
            opacity: 1;
            transform: translateZ(1px) rotate(180deg);
        }
        
        .nav-icon-circle i {
            font-size: 36px;
            background: 
                linear-gradient(135deg, 
                    #1e3c72 0%, 
                    #2a5298 25%, 
                    #ff6b35 50%, 
                    #ffa500 75%, 
                    #ff6b35 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            transition: all 0.8s ease;
            position: relative;
            z-index: 3;
            transform: translateZ(8px);
            filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1));
        }
        
        .nav-icon-item:hover .nav-icon-circle i {
            -webkit-text-fill-color: white;
            transform: translateZ(15px) scale(1.3) rotateY(15deg);
            filter: 
                drop-shadow(0 4px 8px rgba(0, 0, 0, 0.3))
                drop-shadow(0 0 20px rgba(255, 107, 53, 0.6));
            animation: iconGlow 2s ease-in-out infinite alternate;
        }
        
        .nav-icon-label {
            font-size: 11px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            text-align: center;
            line-height: 1.4;
            max-width: 130px;
            color: #2c3e50;
            transition: all 0.8s ease;
            transform: translateZ(5px);
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
            position: relative;
        }
        
        .nav-icon-item:hover .nav-icon-label {
            color: #ff6b35;
            transform: translateZ(20px) translateY(-8px);
            text-shadow: 
                0 2px 4px rgba(255, 107, 53, 0.4),
                0 0 10px rgba(255, 107, 53, 0.3),
                0 1px 2px rgba(0, 0, 0, 0.2);
        }
        
        /* Advanced Animations */
        @keyframes energyWave {
            0%, 100% { 
                transform: translateX(0%) skewX(0deg); 
                opacity: 0.3;
            }
            50% { 
                transform: translateX(50%) skewX(5deg); 
                opacity: 0.7;
            }
        }
        
        @keyframes particleFloat {
            0% { 
                transform: translateY(0px) rotate(0deg); 
            }
            100% { 
                transform: translateY(-100px) rotate(360deg); 
            }
        }
        
        @keyframes hologramPulse {
            0%, 100% { 
                opacity: 0.4;
                transform: translateX(-50%) translateZ(-20px) scaleX(1);
            }
            50% { 
                opacity: 0.8;
                transform: translateX(-50%) translateZ(-20px) scaleX(1.1);
            }
        }
        
        @keyframes energyField {
            0% { 
                transform: translate(-50%, -50%) translateZ(-30px) rotate(0deg); 
            }
            100% { 
                transform: translate(-50%, -50%) translateZ(-30px) rotate(360deg); 
            }
        }
        
        @keyframes energyCore {
            0% { 
                opacity: 0.3;
                transform: translate(-50%, -50%) translateZ(2px) scale(1);
            }
            100% { 
                opacity: 0.7;
                transform: translate(-50%, -50%) translateZ(2px) scale(1.2);
            }
        }
        
        @keyframes iconGlow {
            0% { 
                filter: 
                    drop-shadow(0 4px 8px rgba(0, 0, 0, 0.3))
                    drop-shadow(0 0 20px rgba(255, 107, 53, 0.6));
            }
            100% { 
                filter: 
                    drop-shadow(0 4px 8px rgba(0, 0, 0, 0.3))
                    drop-shadow(0 0 30px rgba(255, 107, 53, 0.9))
                    drop-shadow(0 0 40px rgba(30, 60, 114, 0.5));
            }
        }
        
        /* Staggered Animation Delays */
        .nav-icon-item:nth-child(1) { animation-delay: 0s; }
        .nav-icon-item:nth-child(2) { animation-delay: 0.5s; }
        .nav-icon-item:nth-child(3) { animation-delay: 1s; }
        .nav-icon-item:nth-child(4) { animation-delay: 1.5s; }
        .nav-icon-item:nth-child(5) { animation-delay: 2s; }
        .nav-icon-item:nth-child(6) { animation-delay: 2.5s; }
        
        /* Responsive Ultra-Unique Design */
        @media (max-width: 992px) {
            .navigation-icons-section {
                perspective: 1000px;
                padding: 50px 0;
            }
            
            .nav-icons-row {
                gap: 55px;
            }
            
            .nav-icon-circle {
                width: 80px;
                height: 80px;
            }
            
            .nav-icon-circle i {
                font-size: 32px;
            }
        }
        
        @media (max-width: 768px) {
            .navigation-icons-section {
                perspective: 800px;
                padding: 40px 0;
            }
            
            .nav-icons-row {
                gap: 40px;
            }
            
            .nav-icon-circle {
                width: 70px;
                height: 70px;
            }
            
            .nav-icon-circle i {
                font-size: 28px;
            }
            
            .nav-icon-label {
                font-size: 10px;
                max-width: 110px;
            }
        }
        
        @media (max-width: 576px) {
            .navigation-icons-section {
                perspective: 600px;
                padding: 35px 0;
            }
            
            .nav-icons-row {
                gap: 30px;
            }
            
            .nav-icon-circle {
                width: 60px;
                height: 60px;
            }
            
            .nav-icon-circle i {
                font-size: 24px;
            }
            
            .nav-icon-label {
                font-size: 9px;
                max-width: 95px;
                letter-spacing: 1px;
            }
            
            /* Reduce complex animations on mobile */
            .navigation-icons-section::before,
            .navigation-icons-section::after {
                animation-duration: 20s;
            }
        }'''
                
                # Replace the old CSS with ultra-unique CSS
                before_css = content[:start_index]
                after_css = content[end_index:]
                
                new_content = before_css + ultra_unique_css + after_css
                
                # Write the updated content
                with open(template_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print("🚀 ULTRA-UNIQUE NAVIGATION CREATED!")
                print("\n✨ Revolutionary Features:")
                print("   🌊 Animated energy waves flowing across background")
                print("   ✨ Floating particle system with physics")
                print("   🔮 Holographic shimmer effects on hover")
                print("   ⚡ Rotating energy field animations")
                print("   💎 Conic gradient energy cores")
                print("   🌟 Multi-layer glow and shadow effects")
                print("   🎭 Staggered animation sequences")
                print("   🔥 Advanced CSS transforms and filters")
                print("\n🎨 Unique Visual Elements:")
                print("   - Holographic base projections")
                print("   - Energy field rotations")
                print("   - Particle float animations")
                print("   - Dynamic shimmer sweeps")
                print("   - Multi-dimensional shadows")
                print("   - Gradient text with glow effects")
                print("\n🎯 This navigation is absolutely one-of-a-kind!")
                
            else:
                print("❌ Could not find the end of navigation CSS section")
        else:
            print("❌ Could not find the navigation CSS section")
            
    except Exception as e:
        print(f"❌ Error creating ultra-unique navigation: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    create_ultra_unique_navigation()