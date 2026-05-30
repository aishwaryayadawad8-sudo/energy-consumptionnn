#!/usr/bin/env python3

"""
Add navigation icons under the project title
"""

def add_navigation_icons():
    """Add the navigation icons under the project title"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find where to insert the navigation icons (after the title section)
        insert_marker = '</div>\n</div>'
        # Look for the end of the project-title-section
        title_section_start = content.find('<div class="project-title-section">')
        if title_section_start != -1:
            # Find the end of this section
            section_end = content.find('</div>\n</div>', title_section_start)
            
            if section_end != -1:
                # Create the navigation icons HTML
                navigation_icons = '''

<div class="navigation-icons-section">
    <div class="container">
        <div class="nav-icons-row">
            <a href="{% url 'objective1_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon-circle">
                    <i class="fas fa-bolt"></i>
                </div>
                <span class="nav-icon-label">TOTAL ENERGY</span>
            </a>
            <a href="{% url 'objective2_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon-circle">
                    <i class="fas fa-plug"></i>
                </div>
                <span class="nav-icon-label">ELECTRICITY</span>
            </a>
            <a href="{% url 'objective3_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon-circle">
                    <i class="fas fa-leaf"></i>
                </div>
                <span class="nav-icon-label">RENEWABLES</span>
            </a>
            <a href="{% url 'objective4_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon-circle">
                    <i class="fas fa-smog"></i>
                </div>
                <span class="nav-icon-label">CO₂ EMISSIONS</span>
            </a>
            <a href="{% url 'objective5_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon-circle">
                    <i class="fas fa-globe"></i>
                </div>
                <span class="nav-icon-label">COUNTRY ENERGY FORECASTS</span>
            </a>
            <a href="{% url 'comprehensive_comparison_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon-circle">
                    <i class="fas fa-arrow-right"></i>
                </div>
                <span class="nav-icon-label">MORE PROJECTIONS</span>
            </a>
        </div>
    </div>
</div>'''
                
                # Insert the navigation icons after the title section
                before_nav = content[:section_end + len('</div>\n</div>')]
                after_nav = content[section_end + len('</div>\n</div>'):]
                
                # Combine the parts
                new_content = before_nav + navigation_icons + after_nav
                
                # Write the updated content
                with open(template_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print("✅ Successfully added navigation icons!")
                print("   - Added 6 navigation icons")
                print("   - Icons: Energy, Electricity, Renewables, CO₂, Country Forecasts, More")
                print("\n🎯 Navigation icons will appear under the project title")
                
            else:
                print("❌ Could not find the end of title section")
        else:
            print("❌ Could not find the title section")
            
    except Exception as e:
        print(f"❌ Error adding navigation icons: {e}")

def add_navigation_css():
    """Add CSS styling for the navigation icons"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find where to insert CSS (before </style>)
        css_marker = '</style>'
        css_index = content.find(css_marker)
        
        if css_index != -1:
            # Create the CSS for the navigation icons
            navigation_css = '''
        /* Navigation Icons Section */
        .navigation-icons-section {
            background: white;
            padding: 30px 0;
            border-bottom: 1px solid #e0e0e0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .nav-icons-row {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            gap: 40px;
        }
        
        .nav-icon-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-decoration: none;
            color: #666;
            transition: all 0.3s ease;
            padding: 10px;
        }
        
        .nav-icon-item:hover {
            color: #ff6b35;
            transform: translateY(-3px);
        }
        
        .nav-icon-circle {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: #f8f9fa;
            border: 2px solid #e0e0e0;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 10px;
            transition: all 0.3s ease;
        }
        
        .nav-icon-item:hover .nav-icon-circle {
            background: #ff6b35;
            border-color: #ff6b35;
            color: white;
        }
        
        .nav-icon-circle i {
            font-size: 24px;
            color: #ff6b35;
            transition: color 0.3s ease;
        }
        
        .nav-icon-item:hover .nav-icon-circle i {
            color: white;
        }
        
        .nav-icon-label {
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            text-align: center;
            line-height: 1.2;
            max-width: 100px;
        }
        
        @media (max-width: 768px) {
            .nav-icons-row {
                gap: 20px;
            }
            
            .nav-icon-circle {
                width: 50px;
                height: 50px;
            }
            
            .nav-icon-circle i {
                font-size: 20px;
            }
            
            .nav-icon-label {
                font-size: 10px;
                max-width: 80px;
            }
        }
        
        @media (max-width: 576px) {
            .nav-icons-row {
                gap: 15px;
            }
            
            .nav-icon-circle {
                width: 45px;
                height: 45px;
            }
            
            .nav-icon-circle i {
                font-size: 18px;
            }
            
            .nav-icon-label {
                font-size: 9px;
                max-width: 70px;
            }
        }
'''
            
            # Insert the CSS before the closing style tag
            before_css = content[:css_index]
            after_css = content[css_index:]
            
            # Combine the parts
            new_content = before_css + navigation_css + after_css
            
            # Write the updated content
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ Successfully added CSS styling for navigation icons!")
            print("   - Clean white background")
            print("   - Orange hover effects")
            print("   - Responsive design")
            print("   - Smooth animations")
            
        else:
            print("❌ Could not find the CSS insertion point")
            
    except Exception as e:
        print(f"❌ Error adding navigation CSS: {e}")

if __name__ == "__main__":
    add_navigation_icons()
    add_navigation_css()