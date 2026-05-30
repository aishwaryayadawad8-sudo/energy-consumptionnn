#!/usr/bin/env python3
"""
Remove background image from Objective 4 (SDG-7 Progress Monitoring)
"""

def remove_objective4_background():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Removing background image from Objective 4...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove the CSS for Objective 4 background image
        objective4_css = '''        /* Objective 4: SDG-7 Progress Monitoring */
        .objective-card[data-objective="4"] .objective-info {
            background-image: url('/static/images/sdg7-progress-monitoring.webp');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            border-radius: 8px;
            padding: 20px;
            position: relative;
        }
        
        .objective-card[data-objective="4"] .objective-info::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(255, 255, 255, 0.7);
            border-radius: 8px;
            z-index: 1;
        }'''
        
        if objective4_css in content:
            content = content.replace(objective4_css, '')
            print("✅ Removed Objective 4 background image CSS")
        else:
            print("⚠️  Could not find exact CSS pattern, trying alternative removal...")
            
            # Try to remove just the background image part
            import re
            
            # Remove the background image CSS block
            pattern1 = r'\/\* Objective 4: SDG-7 Progress Monitoring \*\/\s*\.objective-card\[data-objective="4"\] \.objective-info \{[^}]*\}'
            content = re.sub(pattern1, '', content, flags=re.DOTALL)
            
            # Remove the overlay CSS block
            pattern2 = r'\.objective-card\[data-objective="4"\] \.objective-info::before \{[^}]*\}'
            content = re.sub(pattern2, '', content, flags=re.DOTALL)
            
            print("✅ Removed Objective 4 background using regex patterns")
        
        # Clean up any extra whitespace left behind
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Objective 4 background image removed successfully!")
        print("📝 Changes applied:")
        print("   🗑️  Removed SDG-7 Progress Monitoring background image")
        print("   🗑️  Removed overlay effect for Objective 4")
        print("   ✨ Objective 4 now has clean white background")
        print("🔄 Please refresh your browser to see the updated Objective 4")
        
        return True
        
    except Exception as e:
        print(f"❌ Error removing Objective 4 background: {e}")
        return False

if __name__ == "__main__":
    remove_objective4_background()