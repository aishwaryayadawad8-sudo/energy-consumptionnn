#!/usr/bin/env python3
"""
Fix for Objective 2 and 3 button issues
This script adds CSS to ensure buttons are clickable
"""

def fix_objective_buttons():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Fixing Objective 2 and 3 button issues...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add CSS fix for button clickability
        css_fix = """
        /* BUTTON CLICKABILITY FIX */
        .objective-btn {
            position: relative !important;
            z-index: 1000 !important;
            pointer-events: auto !important;
            cursor: pointer !important;
        }
        
        .objective-info {
            position: relative !important;
            z-index: 999 !important;
        }
        
        .objective-card .objective-info > * {
            position: relative !important;
            z-index: 1001 !important;
        }
        """
        
        # Find the closing </style> tag and insert our fix before it
        if "</style>" in content:
            content = content.replace("</style>", css_fix + "\n        </style>")
            
            # Write back the fixed content
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ CSS fix applied successfully!")
            print("📝 Added button clickability improvements")
            print("🔄 Please refresh your browser (Ctrl+F5) to see changes")
            
        else:
            print("❌ Could not find </style> tag in template")
            
    except FileNotFoundError:
        print(f"❌ Template file not found: {template_path}")
    except Exception as e:
        print(f"❌ Error applying fix: {e}")

if __name__ == "__main__":
    fix_objective_buttons()