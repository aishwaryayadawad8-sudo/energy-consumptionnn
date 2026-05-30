#!/usr/bin/env python3

"""
Create realistic 3D icons with glossy effects and proper lighting like the electricity example
"""

def create_realistic_icons():
    """Update navigation to use realistic 3D icons with CSS-only graphics"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the navigation HTML first
        old_html_start = '<div class="nav-icons-row">'
        old_html_end = '</div>\n    </div>\n</div>'
        
        html_start_index = content.find(old_html_start)
        if html_start_index != -1:
            # Find the end of the nav-icons-row
            temp_content = content[html_start_index:]
            end_search = '</div>\n    </div>\n</div>'
            html_end_index = temp_content.find(end_search)
            
            if html_end_index != -1:
                html_end_index += html_start_index
                
                # Create new realistic 3D icon HTML
                new_realistic_html = '''<div class="nav-icons-row">
            <a href="{% url 'objective1_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon-circle">
                    <div class="realistic-icon energy-icon">
                        <div class="icon-body"></div>
                        <div class="icon-highlight"></div>
                    </div>
                </div>
                <span class="nav-icon-label">TOTAL ENERGY</span>
            </a>
            <a href="{% url 'objective2_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon-circle">
                    <div class="realistic-icon electricity-icon">
                        <div class="plug-body"></div>
                        <div class="plug-prongs"></div>
                        <div class="icon-highlight"></div>
                    </div>
                </div>
                <span class="nav-icon-label">ELECTRICITY</span>
            </a>
            <a href="{% url 'objective3_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon-circle">
                    <div class="realistic-icon renewable-icon">
                        <div class="leaf-body"></div>
                        <div class="leaf-vein"></div>
                        <div class="icon-highlight"></div>
                    </div>
                </div>
                <span class="nav-icon-label">RENEWABLES</span>
            </a>
            <a href="{% url 'objective4_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon-circle">
                    <div class="realistic-icon co2-icon">
                        <div class="cloud-body"></div>
                        <div class="cloud-particles"></div>
                        <div class="icon-highlight"></div>
                    </div>
                </div>
                <span class="nav-icon-label">CO₂ EMISSIONS</span>
            </a>
            <a href="{% url 'objective5_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon-circle">
                    <div class="realistic-icon globe-icon">
                        <div class="globe-body"></div>
                        <div class="globe-continents"></div>
                        <div class="icon-highlight"></div>
                    </div>
                </div>
                <span class="nav-icon-label">COUNTRY ENERGY FORECASTS</span>
            </a>
            <a href="{% url 'comprehensive_comparison_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon-circle">
                    <div class="realistic-icon chart-icon">
                        <div class="chart-bars"></div>
                        <div class="chart-arrow"></div>
                        <div class="icon-highlight"></div>
                    </div>
                </div>
                <span class="nav-icon-label">MORE PROJECTIONS</span>
            </a>
        </div>'''
                
                # Replace the HTML
                before_html = content[:html_start_index]
                after_html = content[html_end_index + len(end_search):]
                
                content = before_html + new_realistic_html + after_html
        
        # Now update the CSS for realistic 3D effects
        old_css_start = '        /* Ultra-Unique Navigation - Holographic Energy System */'
        
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
                            if '/* Ultra-Unique' not in next_section[:50]:
                                end_offset = i + 1
                                break
            
            if end_offset > 0:
                end_index = start_index + end_offset
                
                # Create realistic 3D CSS
                realistic_3d_css = '''        /* Realistic 3D Navigation Icons */
        .navigation-icons-section {
            background: 
                radial-gradient(circle at 30% 40%, rgba(255, 107, 53, 0.08) 0%, transparent 50%),
                radial-gradient(circle at 70% 60%, rgba(30, 60, 114, 0.08) 0%, transparent 50%),
                linear-gradient(135deg, #f8f9fa 0%, #ffffff 50%, #f0f4f8 100%);
            padding: 60px 0;
            position: relative;
            overflow: hidden;
            perspective: 1200px;
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
            gap: 70px;
            position: relative;
            z-index: 1;
        }
        
        .nav-icon-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-decoration: none;
            color: #2c3e50;
            transition: all 0.6s cubic-bezier(0.23, 1, 0.32, 1);
            padding: 25px;
            position: relative;
        }
        
        .nav-icon-item:hover {
            transform: translateY(-10px);
        }
        
        .nav-icon-circle {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background: 
                radial-gradient(circle at 30% 30%, 
                    rgba(255, 255, 255, 0.9) 0%, 
                    rgba(255, 140, 60, 0.8) 40%, 
                    rgba(255, 107, 53, 0.9) 70%, 
                    rgba(200, 80, 40, 1) 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 18px;
            transition: all 0.6s ease;
            position: relative;
            overflow: hidden;
            
            /* Realistic 3D Shadow */
            box-shadow: 
                0 15px 35px rgba(255, 107, 53, 0.4),
                0 8px 15px rgba(0, 0, 0, 0.2),
                inset 0 2px 0 rgba(255, 255, 255, 0.8),
                inset 0 -2px 0 rgba(0, 0, 0, 0.2);
        }
        
        .nav-icon-item:hover .nav-icon-circle {
            transform: scale(1.1);
            box-shadow: 
                0 25px 50px rgba(255, 107, 53, 0.5),
                0 15px 25px rgba(0, 0, 0, 0.3),
                inset 0 3px 0 rgba(255, 255, 255, 0.9),
                inset 0 -3px 0 rgba(0, 0, 0, 0.3);
        }
        
        /* Realistic Icon Styles */
        .realistic-icon {
            width: 50px;
            height: 50px;
            position: relative;
            transform-style: preserve-3d;
        }
        
        .icon-highlight {
            position: absolute;
            top: 15%;
            left: 20%;
            width: 30%;
            height: 30%;
            background: 
                radial-gradient(ellipse at center, 
                    rgba(255, 255, 255, 0.9) 0%, 
                    rgba(255, 255, 255, 0.4) 50%, 
                    transparent 100%);
            border-radius: 50%;
            transform: translateZ(2px);
        }
        
        /* Energy Icon (Lightning Bolt) */
        .energy-icon .icon-body {
            width: 100%;
            height: 100%;
            background: white;
            clip-path: polygon(20% 0%, 60% 0%, 40% 40%, 80% 40%, 40% 100%, 0% 60%, 20% 60%);
            filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));
        }
        
        /* Electricity Icon (Plug) */
        .electricity-icon .plug-body {
            width: 70%;
            height: 60%;
            background: white;
            border-radius: 0 0 50% 50%;
            position: absolute;
            top: 40%;
            left: 15%;
            filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));
        }
        
        .electricity-icon .plug-prongs {
            width: 40%;
            height: 30%;
            background: white;
            position: absolute;
            top: 10%;
            left: 30%;
            border-radius: 4px 4px 0 0;
        }
        
        .electricity-icon .plug-prongs::before,
        .electricity-icon .plug-prongs::after {
            content: '';
            position: absolute;
            width: 6px;
            height: 20px;
            background: white;
            border-radius: 3px;
        }
        
        .electricity-icon .plug-prongs::before {
            left: 20%;
            top: -10px;
        }
        
        .electricity-icon .plug-prongs::after {
            right: 20%;
            top: -10px;
        }
        
        /* Renewable Icon (Leaf) */
        .renewable-icon .leaf-body {
            width: 80%;
            height: 90%;
            background: white;
            border-radius: 0 100% 0 100%;
            position: absolute;
            top: 5%;
            left: 10%;
            transform: rotate(45deg);
            filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));
        }
        
        .renewable-icon .leaf-vein {
            width: 2px;
            height: 60%;
            background: rgba(255, 255, 255, 0.7);
            position: absolute;
            top: 20%;
            left: 50%;
            transform: translateX(-50%) rotate(45deg);
        }
        
        /* CO2 Icon (Cloud) */
        .co2-icon .cloud-body {
            width: 80%;
            height: 50%;
            background: white;
            border-radius: 25px;
            position: absolute;
            top: 30%;
            left: 10%;
            filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));
        }
        
        .co2-icon .cloud-body::before,
        .co2-icon .cloud-body::after {
            content: '';
            position: absolute;
            background: white;
            border-radius: 50%;
        }
        
        .co2-icon .cloud-body::before {
            width: 20px;
            height: 20px;
            top: -10px;
            left: 10px;
        }
        
        .co2-icon .cloud-body::after {
            width: 25px;
            height: 25px;
            top: -15px;
            right: 15px;
        }
        
        /* Globe Icon */
        .globe-icon .globe-body {
            width: 80%;
            height: 80%;
            background: white;
            border-radius: 50%;
            position: absolute;
            top: 10%;
            left: 10%;
            filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));
        }
        
        .globe-icon .globe-continents {
            width: 60%;
            height: 60%;
            position: absolute;
            top: 20%;
            left: 20%;
            background: rgba(255, 255, 255, 0.7);
            border-radius: 50%;
        }
        
        .globe-icon .globe-continents::before {
            content: '';
            position: absolute;
            width: 15px;
            height: 20px;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50% 0 50% 50%;
            top: 20%;
            left: 30%;
        }
        
        /* Chart Icon */
        .chart-icon .chart-bars {
            width: 80%;
            height: 60%;
            position: absolute;
            top: 30%;
            left: 10%;
            background: 
                linear-gradient(to right, 
                    white 0%, white 20%, 
                    transparent 20%, transparent 30%,
                    white 30%, white 50%,
                    transparent 50%, transparent 60%,
                    white 60%, white 80%,
                    transparent 80%);
            filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));
        }
        
        .chart-icon .chart-arrow {
            width: 30px;
            height: 3px;
            background: white;
            position: absolute;
            top: 20%;
            right: 10%;
            transform: rotate(45deg);
        }
        
        .chart-icon .chart-arrow::after {
            content: '';
            position: absolute;
            right: -2px;
            top: -3px;
            width: 0;
            height: 0;
            border-left: 8px solid white;
            border-top: 4px solid transparent;
            border-bottom: 4px solid transparent;
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
            transition: all 0.6s ease;
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
        }
        
        .nav-icon-item:hover .nav-icon-label {
            color: #ff6b35;
            text-shadow: 
                0 2px 4px rgba(255, 107, 53, 0.4),
                0 1px 2px rgba(0, 0, 0, 0.2);
        }
        
        /* Responsive Design */
        @media (max-width: 992px) {
            .nav-icons-row {
                gap: 55px;
            }
            
            .nav-icon-circle {
                width: 90px;
                height: 90px;
            }
            
            .realistic-icon {
                width: 45px;
                height: 45px;
            }
        }
        
        @media (max-width: 768px) {
            .navigation-icons-section {
                padding: 40px 0;
            }
            
            .nav-icons-row {
                gap: 40px;
            }
            
            .nav-icon-circle {
                width: 80px;
                height: 80px;
            }
            
            .realistic-icon {
                width: 40px;
                height: 40px;
            }
            
            .nav-icon-label {
                font-size: 10px;
                max-width: 110px;
            }
        }
        
        @media (max-width: 576px) {
            .navigation-icons-section {
                padding: 35px 0;
            }
            
            .nav-icons-row {
                gap: 30px;
            }
            
            .nav-icon-circle {
                width: 70px;
                height: 70px;
            }
            
            .realistic-icon {
                width: 35px;
                height: 35px;
            }
            
            .nav-icon-label {
                font-size: 9px;
                max-width: 95px;
                letter-spacing: 1px;
            }
        }'''
                
                # Replace the CSS
                before_css = content[:start_index]
                after_css = content[end_index:]
                
                new_content = before_css + realistic_3d_css + after_css
                
                # Write the updated content
                with open(template_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print("🎨 REALISTIC 3D ICONS CREATED!")
                print("\n✨ Realistic Features:")
                print("   🔌 Custom CSS-drawn electricity plug")
                print("   ⚡ Lightning bolt energy icon")
                print("   🍃 Detailed leaf for renewables")
                print("   ☁️ Cloud shape for CO2 emissions")
                print("   🌍 Globe with continents")
                print("   📊 Chart with arrow")
                print("\n🎯 Visual Effects:")
                print("   - Glossy orange gradient backgrounds")
                print("   - Realistic lighting and highlights")
                print("   - Drop shadows for depth")
                print("   - White icon shapes with proper shadows")
                print("   - Smooth hover animations")
                print("   - Professional 3D appearance")
                print("\n🚀 Your icons now look incredibly realistic!")
                
            else:
                print("❌ Could not find the end of navigation CSS section")
        else:
            print("❌ Could not find the navigation CSS section")
            
    except Exception as e:
        print(f"❌ Error creating realistic icons: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    create_realistic_icons()