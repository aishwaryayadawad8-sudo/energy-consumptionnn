#!/usr/bin/env python3

"""
Update navigation icons with a unique design that matches the webpage theme
"""

def update_navigation_css():
    """Update CSS styling for a more unique navigation design"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the navigation CSS
        old_css_start = '        /* Navigation Icons Section */'
        old_css_end = '        }'
        
        # Find the navigation CSS section
        start_index = content.find(old_css_start)
        if start_index != -1:
            # Find the end of the navigation CSS (look for the last closing brace of this section)
            # We need to find where the navigation CSS ends
            temp_content = content[start_index:]
            # Count opening and closing braces to find the end
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
                
                # Create the new unique CSS
                new_navigation_css = '''        /* Navigation Icons Section - Unique Energy Theme */
        .navigation-icons-section {
            background: linear-gradient(to bottom, #f8f9fa 0%, #ffffff 100%);
            padding: 40px 0;
            border-bottom: 3px solid #e8eef5;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            position: relative;
            overflow: hidden;
        }
        
        .navigation-icons-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, 
                #1e3c72 0%, 
                #2a5298 25%, 
                #ff6b35 50%, 
                #2a5298 75%, 
                #1e3c72 100%);
        }
        
        .nav-icons-row {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            gap: 50px;
            position: relative;
        }
        
        .nav-icon-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-decoration: none;
            color: #2c3e50;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            padding: 15px;
            position: relative;
        }
        
        .nav-icon-item::before {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 0;
            height: 3px;
            background: linear-gradient(90deg, #ff6b35, #ffa500);
            transition: width 0.4s ease;
            border-radius: 2px;
        }
        
        .nav-icon-item:hover::before {
            width: 80%;
        }
        
        .nav-icon-item:hover {
            transform: translateY(-5px);
        }
        
        .nav-icon-circle {
            width: 70px;
            height: 70px;
            border-radius: 50%;
            background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
            border: 3px solid #e8eef5;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 12px;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            position: relative;
            overflow: hidden;
        }
        
        .nav-icon-circle::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, #ff6b35 0%, #ffa500 100%);
            opacity: 0;
            transition: opacity 0.4s ease;
            border-radius: 50%;
        }
        
        .nav-icon-item:hover .nav-icon-circle {
            border-color: #ff6b35;
            transform: scale(1.1) rotate(5deg);
            box-shadow: 0 8px 25px rgba(255, 107, 53, 0.3);
        }
        
        .nav-icon-item:hover .nav-icon-circle::before {
            opacity: 1;
        }
        
        .nav-icon-circle i {
            font-size: 28px;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #ff6b35 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            transition: all 0.4s ease;
            position: relative;
            z-index: 1;
        }
        
        .nav-icon-item:hover .nav-icon-circle i {
            -webkit-text-fill-color: white;
            transform: scale(1.1);
        }
        
        .nav-icon-label {
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            text-align: center;
            line-height: 1.3;
            max-width: 110px;
            color: #2c3e50;
            transition: color 0.3s ease;
        }
        
        .nav-icon-item:hover .nav-icon-label {
            color: #ff6b35;
        }
        
        /* Responsive Design */
        @media (max-width: 992px) {
            .nav-icons-row {
                gap: 35px;
            }
            
            .nav-icon-circle {
                width: 65px;
                height: 65px;
            }
            
            .nav-icon-circle i {
                font-size: 26px;
            }
        }
        
        @media (max-width: 768px) {
            .navigation-icons-section {
                padding: 30px 0;
            }
            
            .nav-icons-row {
                gap: 25px;
            }
            
            .nav-icon-circle {
                width: 55px;
                height: 55px;
            }
            
            .nav-icon-circle i {
                font-size: 22px;
            }
            
            .nav-icon-label {
                font-size: 10px;
                max-width: 90px;
            }
        }
        
        @media (max-width: 576px) {
            .navigation-icons-section {
                padding: 25px 0;
            }
            
            .nav-icons-row {
                gap: 20px;
            }
            
            .nav-icon-circle {
                width: 50px;
                height: 50px;
                border-width: 2px;
            }
            
            .nav-icon-circle i {
                font-size: 20px;
            }
            
            .nav-icon-label {
                font-size: 9px;
                max-width: 75px;
                letter-spacing: 0.5px;
            }
        }'''
                
                # Replace the old CSS with new CSS
                before_css = content[:start_index]
                after_css = content[end_index:]
                
                new_content = before_css + new_navigation_css + after_css
                
                # Write the updated content
                with open(template_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print("✅ Successfully updated navigation icons with unique design!")
                print("\n🎨 New Design Features:")
                print("   - Gradient color scheme matching energy theme")
                print("   - Animated hover effects with scale and rotation")
                print("   - Gradient text for icons")
                print("   - Underline animation on hover")
                print("   - Enhanced shadows and depth")
                print("   - Smooth cubic-bezier transitions")
                print("   - Top gradient accent line")
                print("   - Fully responsive design")
                print("\n🎯 The navigation now has a unique, cohesive look!")
                
            else:
                print("❌ Could not find the end of navigation CSS section")
        else:
            print("❌ Could not find the navigation CSS section")
            
    except Exception as e:
        print(f"❌ Error updating navigation CSS: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    update_navigation_css()