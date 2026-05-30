#!/usr/bin/env python3

"""
Fix the entire website to have proper responsive design and professional appearance
"""

def fix_website_responsive_design():
    """Update all templates to have proper website-like responsive design"""
    
    # First, let's update the base template for consistent styling
    base_template_path = "sustainable_energy/dashboard/templates/dashboard/base.html"
    
    try:
        with open(base_template_path, 'r', encoding='utf-8') as f:
            base_content = f.read()
    except FileNotFoundError:
        print("❌ Base template not found, creating one...")
        base_content = create_base_template()
    
    # Create improved base t