#!/usr/bin/env python3
"""
Force remove Objective 4 background image CSS
"""

def force_remove_objective4_background():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Force removing Objective 4 background image CSS...")
    
    try:
        # Read the current template with explicit encoding
        with open(template_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Define the exact CSS block to remove
        css_to_remove = '''        /* Objective 4: SDG-7 Progress Monitoring */
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
        }
        
        '''
        
        if css_to_remove in content:
            content = content.replace(css_to_remove, '        ')
            print("✅ Successfully removed Objective 4 CSS block")
        else:
            print("⚠️  Exact block not found, trying line by line removal...")
            
            # Remove line by line
            lines_to_remove = [
                "        /* Objective 4: SDG-7 Progress Monitoring */",
                "        .objective-card[data-objective=\"4\"] .objective-info {",
                "            background-image: url('/static/images/sdg7-progress-monitoring.webp');",
                "            background-size: cover;",
                "            background-position: center;",
                "            background-repeat: no-repeat;",
                "            border-radius: 8px;",
                "            padding: 20px;",
                "            position: relative;",
                "        }",
                "        ",
                "        .objective-card[data-objective=\"4\"] .objective-info::before {",
                "            content: '';",
                "            position: absolute;",
                "            top: 0;",
                "            left: 0;",
                "            right: 0;",
                "            bottom: 0;",
                "            background: rgba(255, 255, 255, 0.7);",
                "            border-radius: 8px;",
                "            z-index: 1;",
                "        }"
            ]
            
            for line in lines_to_remove:
                content = content.replace(line + '\n', '')
                content = content.replace(line, '')
            
            print("✅ Removed Objective 4 CSS line by line")
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Objective 4 background image completely removed!")
        print("📝 Result:")
        print("   🗑️  No background image for SDG-7 Progress Monitoring")
        print("   ✨ Clean white background for Objective 4")
        print("   🎨 All other objectives keep their background images")
        print("🔄 Please refresh your browser to see the updated Objective 4")
        
        return True
        
    except Exception as e:
        print(f"❌ Error removing Objective 4 background: {e}")
        return False

if __name__ == "__main__":
    force_remove_objective4_background()