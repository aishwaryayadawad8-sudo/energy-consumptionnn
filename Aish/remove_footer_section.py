#!/usr/bin/env python3

"""
Remove the footer section from the objective selector template
"""

def remove_footer_section():
    """Remove the EnerOutlook footer section from the webpage"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and remove the footer section
        start_marker = '<div class="project-footer">'
        end_marker = '</div>\n{% endblock %}'
        
        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        
        if start_index != -1 and end_index != -1:
            # Remove the footer section but keep the endblock
            before_footer = content[:start_index]
            after_footer = '{% endblock %}\n'
            
            # Combine the parts
            new_content = before_footer.rstrip() + '\n' + after_footer
            
            # Write the updated content
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ Successfully removed the footer section!")
            print("   - Removed EnerOutlook project title")
            print("   - Removed comprehensive Django description")
            print("   - Removed detailed project description")
            print("\n🎯 The webpage footer has been cleaned up")
            
        else:
            print("❌ Could not find the footer section to remove")
            print(f"   Start marker found: {start_index != -1}")
            print(f"   End marker found: {end_index != -1}")
            
    except Exception as e:
        print(f"❌ Error removing footer section: {e}")

if __name__ == "__main__":
    remove_footer_section()