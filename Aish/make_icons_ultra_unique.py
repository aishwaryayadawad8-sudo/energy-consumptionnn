#!/usr/bin/env python3

"""
Create ultra-unique navigation icons with hexagonal shapes and energy effects
"""

def update_navigation_html():
    """Update the HTML structure for unique hexagonal icons"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the navigation HTML
        old_html_start = '<div class="navigation-icons-section">'
        old_html_end = '</div>\n</div>'
        
        start_index = content.find(old_html_start)
        if start_index != -1:
            # Find the end of the navigation section
            temp_content = content[start_index:]
            # Look for the closing div of navigation-icons-section
            div_count = 0
            end_offset = 0
            
            for i, char in enumerate(temp_c