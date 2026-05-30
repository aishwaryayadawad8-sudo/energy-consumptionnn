#!/usr/bin/env python3
"""
Restore background image for Objective 4 (SDG-7 Progress Monitoring)
"""

def restore_objective4_background():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Restoring background image for Objective 4...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add the CSS for Objective 4 background image back
        objective4_css = '''        
        /* Objective 4: SDG-7 Progress Monitoring */
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
        
        # Find where to insert the CSS (after Objective 3 CSS)
        insertion_point = content.find('        /* Objective 5: Energy Equity Analysis */')
        
        if insertion_point != -1:
            # Insert the Objective 4 CSS before Objective 5
            content = content[:insertion_point] + objective4_css + '\n        ' + content[insertion_point:]
            print("✅ Added Objective 4 background image CSS")
        else:
            # Alternative: find a good insertion point
            alt_insertion = content.find('        /* Ensure content appears above overlay with better contrast */')
            if alt_insertion != -1:
                content = content[:alt_insertion] + objective4_css + '\n        ' + content[alt_insertion:]
                print("✅ Added Objective 4 background image CSS (alternative location)")
            else:
                print("⚠️  Could not find insertion point, adding at end of CSS section")
                style_end = content.find('</style>')
                if style_end != -1:
                    content = content[:style_end] + objective4_css + '\n        ' + content[style_end:]
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Objective 4 background image restored successfully!")
        print("📝 Changes applied:")
        print("   🖼️  Added SDG-7 Progress Monitoring background image")
        print("   ✨ Added overlay effect for better text readability")
        print("   🎨 Objective 4 now matches other objectives with background")
        print("🔄 Please refresh your browser to see the restored background image")
        
        return True
        
    except Exception as e:
        print(f"❌ Error restoring Objective 4 background: {e}")
        return False

if __name__ == "__main__":
    restore_objective4_background()