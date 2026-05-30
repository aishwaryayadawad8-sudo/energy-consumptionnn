#!/usr/bin/env python3

"""
Add the project title to the objective selector template
"""

def add_project_title():
    """Add the project title 'TOWARDS AFFORDABLE AND CLEAN ENERGY: A PREDICTIVE AND STRATEGIC FRAMEWORK FOR SDG 7'"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find where to insert the title (after {% block content %})
        insert_marker = '{% block content %}'
        insert_index = content.find(insert_marker)
        
        if insert_index != -1:
            # Create the title section HTML
            title_section = '''
<div class="project-title-section">
    <div class="container">
        <h1 class="main-project-title">
            TOWARDS AFFORDABLE AND CLEAN ENERGY:<br>
            A PREDICTIVE AND STRATEGIC FRAMEWORK FOR SDG 7
        </h1>
    </div>
</div>
'''
            
            # Insert the title after the block content marker
            before_title = content[:insert_index + len(insert_marker)]
            after_title = content[insert_index + len(insert_marker):]
            
            # Combine the parts
            new_content = before_title + title_section + after_title
            
            # Write the updated content
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ Successfully added the project title!")
            print("   - Added: 'TOWARDS AFFORDABLE AND CLEAN ENERGY:'")
            print("   - Added: 'A PREDICTIVE AND STRATEGIC FRAMEWORK FOR SDG 7'")
            print("\n🎯 The title will appear at the top of your webpage")
            
        else:
            print("❌ Could not find the insertion point for the title")
            
    except Exception as e:
        print(f"❌ Error adding project title: {e}")

def add_title_css():
    """Add CSS styling for the project title"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find where to insert CSS (before </style>)
        css_marker = '</style>'
        css_index = content.find(css_marker)
        
        if css_index != -1:
            # Create the CSS for the title
            title_css = '''
        /* Project Title Section */
        .project-title-section {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            padding: 40px 0;
            margin-bottom: 30px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        
        .main-project-title {
            color: white;
            font-size: 2.5rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
            line-height: 1.3;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        @media (max-width: 768px) {
            .main-project-title {
                font-size: 1.8rem;
                letter-spacing: 1px;
            }
        }
        
        @media (max-width: 576px) {
            .main-project-title {
                font-size: 1.4rem;
                letter-spacing: 0.5px;
            }
        }
'''
            
            # Insert the CSS before the closing style tag
            before_css = content[:css_index]
            after_css = content[css_index:]
            
            # Combine the parts
            new_content = before_css + title_css + after_css
            
            # Write the updated content
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ Successfully added CSS styling for the title!")
            print("   - Blue gradient background")
            print("   - White text with shadow")
            print("   - Responsive design")
            
        else:
            print("❌ Could not find the CSS insertion point")
            
    except Exception as e:
        print(f"❌ Error adding title CSS: {e}")

if __name__ == "__main__":
    add_project_title()
    add_title_css()