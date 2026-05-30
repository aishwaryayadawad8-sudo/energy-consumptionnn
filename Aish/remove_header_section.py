#!/usr/bin/env python3

"""
Remove the header section from the objective selector template
"""

def remove_header_section():
    """Remove the EnerData/EnerOutlook header section from the webpage"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and remove the header section
        start_marker = '{% block content %}\n<div class="hero-header">'
        end_marker = '</div>\n\n<div class="energy-background">'
        
        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        
        if start_index != -1 and end_index != -1:
            # Remove the header section but keep the block content start and energy background
            before_header = content[:start_index + len('{% block content %}')]
            after_header = content[end_index:]
            
            # Combine the parts
            new_content = before_header + '\n\n<div class="energy-background">' + after_header[len('</div>\n\n<div class="energy-background">'):]
            
            # Write the updated content
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ Successfully removed the header section!")
            print("   - Removed EnerData logo and branding")
            print("   - Removed EnerOutlook title")
            print("   - Removed subtitle text")
            print("   - Removed navigation icons")
            print("\n🎯 The webpage will now start directly with the objectives grid")
            
        else:
            print("❌ Could not find the header section to remove")
            print(f"   Start marker found: {start_index != -1}")
            print(f"   End marker found: {end_index != -1}")
            
    except Exception as e:
        print(f"❌ Error removing header section: {e}")

if __name__ == "__main__":
    remove_header_section()