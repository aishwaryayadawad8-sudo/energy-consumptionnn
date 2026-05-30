#!/usr/bin/env python3
"""
Update the back button text from "Back to Objectives" to just "Back"
"""

def update_back_button_text():
    template_path = "sustainable_energy/dashboard/templates/dashboard/total_energy.html"
    
    print("🔧 Updating back button text to 'Back' only...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and update the back button text
        old_back_button = '''        <a href="/country-forecasts/" class="back-btn">
            <i class="fas fa-arrow-left"></i> Back to Objectives
        </a>'''
        
        new_back_button = '''        <a href="/country-forecasts/" class="back-btn">
            <i class="fas fa-arrow-left"></i> Back
        </a>'''
        
        if old_back_button in content:
            content = content.replace(old_back_button, new_back_button)
            print("✅ Updated back button text to 'Back'")
        else:
            # Try alternative pattern without exact spacing
            import re
            pattern = r'(<a href="/country-forecasts/" class="back-btn">\s*<i class="fas fa-arrow-left"></i>\s*)Back to Objectives(\s*</a>)'
            replacement = r'\1Back\2'
            
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                print("✅ Updated back button text to 'Back' (regex method)")
            else:
                print("⚠️  Could not find exact back button pattern")
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Back button text updated successfully!")
        print("📝 Change applied:")
        print("   🔄 'Back to Objectives' → 'Back'")
        print("🔄 Please refresh your browser to see the updated button")
        
        return True
        
    except Exception as e:
        print(f"❌ Error updating back button text: {e}")
        return False

if __name__ == "__main__":
    update_back_button_text()