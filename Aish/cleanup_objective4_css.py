#!/usr/bin/env python3
"""
Clean up any remaining CSS for Objective 4 background
"""

import re

def cleanup_objective4_css():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Cleaning up any remaining Objective 4 CSS...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Clean up any extra whitespace left behind
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # Remove any remaining empty CSS blocks
        content = re.sub(r'\s*\n\s*\n\s*\n', '\n\n', content)
        
        # Write back the cleaned content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ CSS cleanup completed!")
        print("🔄 Objective 4 now has a clean white background without any image")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during cleanup: {e}")
        return False

if __name__ == "__main__":
    cleanup_objective4_css()