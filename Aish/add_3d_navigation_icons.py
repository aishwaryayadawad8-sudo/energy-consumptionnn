#!/usr/bin/env python3

"""
Update navigation icons with stunning 3D effects
"""

def update_navigation_3d():
    """Update CSS styling for 3D navigation icons"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the navigation CSS
        old_css_start = '        /* Navigation Icons Section - Unique Energy Theme */'
        
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
                
                # Create the new 3D CSS
                new_3d_navigation_css = '''        /* Navigation Icons Section - 3D Energy Theme */
        .navigation-icons-section {
            background: linear-gradient(to bottom, #f8f9fa 0%, #ffffff 100%);
            padding: 50px 0;
            border-bottom: 3px solid #e8eef5;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            position: relative;
            overflow: hidden;
            perspective: 1000px;
        }
        
        .navigation-icons-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, 
                #1e3c72 0%, 
                #2a5298 25%, 
                #ff6b35 50%, 
                #2a5298 75%, 
                #1e3c72 100%);
            box-shadow: 0 2px 10px rgba(255, 107, 53, 0.3);
        }
        
        .nav-icons-row {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            gap: 60px;
            position: relative;
            transform-style: preserve-3d;
        }
        
        .nav-icon-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-decoration: none;
            color: #2c3e50;
            transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
            padding: 20px;
            position: relative;
            transform-style: preserve-3d;
            transform: translateZ(0) rotateX(0deg) rotateY(0deg);
        }
        
        .nav-icon-item::before {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 50%;
            transform: translateX(-50%) translateZ(-10px);
            width: 0;
            height: 4px;
            background: linear-gradient(90deg, #ff6b35, #ffa500);
            transition: width 0.6s ease;
            border-radius: 2px;
            box-shadow: 0 2px 8px rgba(255, 107, 53, 0.4);
        }
        
        .nav-icon-item:hover::before {
            width: 90%;
        }
        
        .nav-icon-item:hover {
            transform: translateZ(30px) rotateX(-10deg) rotateY(5deg) translateY(-10px);
        }
        
        .nav-icon-circle {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            background: linear-gradient(145deg, #ffffff 0%, #f0f4f8 50%, #e8eef5 100%);
            border: 3px solid #e8eef5;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 15px;
            transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            transform-style: preserve-3d;
            
            /* 3D Shadow Effects */
            box-shadow: 
                0 8px 16px rgba(0,0,0,0.1),
                0 4px 8px rgba(0,0,0,0.08),
                inset 0 1px 0 rgba(255,255,255,0.8),
                inset 0 -1px 0 rgba(0,0,0,0.1);
        }
        
        .nav-icon-circle::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(145deg, #ff6b35 0%, #ffa500 50%, #ff8c42 100%);
            opacity: 0;
            transition: opacity 0.6s ease;
            border-radius: 50%;
            transform: translateZ(-1px);
        }
        
        .nav-icon-circle::after {
            content: '';
            position: absolute;
            top: 10%;
            left: 10%;
            width: 30%;
            height: 30%;
            background: linear-gradient(145deg, rgba(255,255,255,0.8) 0%, rgba(255,255,255,0.2) 100%);
            border-radius: 50%;
            transform: translateZ(2px);
            transition: all 0.6s ease;
        }
        
        .nav-icon-item:hover .nav-icon-circle {
            border-color: #ff6b35;
            transform: translateZ(20px) rotateX(-15deg) scale(1.15);
            box-shadow: 
                0 20px 40px rgba(255, 107, 53, 0.3),
                0 10px 20px rgba(255, 107, 53, 0.2),
                0 5px 10px rgba(0,0,0,0.1),
                inset 0 2px 0 rgba(255,255,255,0.9),
                inset 0 -2px 0 rgba(0,0,0,0.2);
        }
        
        .nav-icon-item:hover .nav-icon-circle::before {
            opacity: 1;
        }
        
        .nav-icon-item:hover .nav-icon-circle::after {
            transform: translateZ(5px) scale(1.2);
            opacity: 0.9;
        }
        
        .nav-icon-circle i {
            font-size: 32px;
            background: linear-gradient(145deg, #1e3c72 0%, #2a5298 30%, #ff6b35 70%, #ffa500 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            transition: all 0.6s ease;
            position: relative;
            z-index: 2;
            transform: translateZ(5px);
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .nav-icon-item:hover .nav-icon-circle i {
            -webkit-text-fill-color: white;
            transform: translateZ(10px) scale(1.2) rotateY(10deg);
            text-shadow: 
                0 4px 8px rgba(0,0,0,0.3),
                0 2px 4px rgba(0,0,0,0.2);
        }
        
        .nav-icon-label {
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            text-align: center;
            line-height: 1.4;
            max-width: 120px;
            color: #2c3e50;
            transition: all 0.6s ease;
            transform: translateZ(0px);
            text-shadow: 0 1px 2px rgba(0,0,0,0.1);
        }
        
        .nav-icon-item:hover .nav-icon-label {
            color: #ff6b35;
            transform: translateZ(15px) translateY(-5px);
            text-shadow: 
                0 2px 4px rgba(255, 107, 53, 0.3),
                0 1px 2px rgba(0,0,0,0.2);
        }
        
        /* 3D Floating Animation */
        @keyframes float3d {
            0%, 100% { 
                transform: translateZ(0px) rotateX(0deg) rotateY(0deg); 
            }
            50% { 
                transform: translateZ(5px) rotateX(2deg) rotateY(1deg); 
            }
        }
        
        .nav-icon-item:nth-child(odd) {
            animation: float3d 4s ease-in-out infinite;
        }
        
        .nav-icon-item:nth-child(even) {
            animation: float3d 4s ease-in-out infinite reverse;
        }
        
        /* Responsive 3D Design */
        @media (max-width: 992px) {
            .navigation-icons-section {
                perspective: 800px;
                padding: 40px 0;
            }
            
            .nav-icons-row {
                gap: 45px;
            }
            
            .nav-icon-circle {
                width: 70px;
                height: 70px;
            }
            
            .nav-icon-circle i {
                font-size: 28px;
            }
            
            .nav-icon-item:hover {
                transform: translateZ(20px) rotateX(-8deg) rotateY(3deg) translateY(-8px);
            }
        }
        
        @media (max-width: 768px) {
            .navigation-icons-section {
                perspective: 600px;
                padding: 35px 0;
            }
            
            .nav-icons-row {
                gap: 35px;
            }
            
            .nav-icon-circle {
                width: 60px;
                height: 60px;
            }
            
            .nav-icon-circle i {
                font-size: 24px;
            }
            
            .nav-icon-label {
                font-size: 10px;
                max-width: 100px;
            }
            
            .nav-icon-item:hover {
                transform: translateZ(15px) rotateX(-6deg) rotateY(2deg) translateY(-6px);
            }
        }
        
        @media (max-width: 576px) {
            .navigation-icons-section {
                perspective: 500px;
                padding: 30px 0;
            }
            
            .nav-icons-row {
                gap: 25px;
            }
            
            .nav-icon-circle {
                width: 55px;
                height: 55px;
                border-width: 2px;
            }
            
            .nav-icon-circle i {
                font-size: 22px;
            }
            
            .nav-icon-label {
                font-size: 9px;
                max-width: 85px;
                letter-spacing: 0.8px;
            }
            
            .nav-icon-item:hover {
                transform: translateZ(10px) rotateX(-4deg) rotateY(1deg) translateY(-4px);
            }
            
            /* Reduce animation on mobile for performance */
            .nav-icon-item:nth-child(odd),
            .nav-icon-item:nth-child(even) {
                animation: none;
            }
        }'''
                
                # Replace the old CSS with new 3D CSS
                before_css = content[:start_index]
                after_css = content[end_index:]
                
                new_content = before_css + new_3d_navigation_css + after_css
                
                # Write the updated content
                with open(template_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print("✅ Successfully updated navigation icons with stunning 3D effects!")
                print("\n🎨 3D Design Features:")
                print("   - Realistic 3D perspective and depth")
                print("   - Multi-layered shadows and lighting")
                print("   - 3D rotation and tilt effects on hover")
                print("   - Floating animation with 3D transforms")
                print("   - Gradient highlights and reflections")
                print("   - Advanced CSS 3D transforms")
                print("   - Perspective-based responsive design")
                print("   - Hardware-accelerated animations")
                print("\n🚀 Your navigation icons now have incredible 3D depth!")
                
            else:
                print("❌ Could not find the end of navigation CSS section")
        else:
            print("❌ Could not find the navigation CSS section")
            
    except Exception as e:
        print(f"❌ Error updating navigation CSS: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    update_navigation_3d()