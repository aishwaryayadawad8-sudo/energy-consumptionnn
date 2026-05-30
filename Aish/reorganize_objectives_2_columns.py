#!/usr/bin/env python3
"""
Remove content areas and reorganize objectives into 2 columns (2 objectives per row)
"""

def reorganize_objectives():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Reorganizing objectives into 2-column layout...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update CSS for 2-column grid layout
        old_css = '''        .objectives-grid {
            display: flex;
            flex-direction: column; /* Changed from grid to single column */
            gap: 0; /* Remove gap since we'll use horizontal lines */
        }
        
        .objective-card {
            background: white;
            border-radius: 12px;
            padding: 40px; /* Increased from 30px */
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border: 1px solid #f1f5f9;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            margin-bottom: 0; /* Remove margin since we'll use borders */
            border-bottom: 3px solid #e5e7eb; /* Add horizontal line between objectives */
            min-height: 400px; /* Add minimum height for consistent spacing */
            display: flex; /* Change to flex layout */
            gap: 40px; /* Add gap between objective info and content area */
            align-items: flex-start; /* Align items to top */
        }
        
        .objective-card:last-child {
            border-bottom: none; /* Remove border from last card */
        }
        
        /* Objective info section (left side) */
        .objective-info {
            flex: 0 0 400px; /* Fixed width for objective info */
            display: flex;
            flex-direction: column;
            position: relative;
        }'''
        
        new_css = '''        .objectives-grid {
            display: grid;
            grid-template-columns: 1fr 1fr; /* 2 columns */
            gap: 30px; /* Gap between cards */
            margin-top: 20px;
        }
        
        .objective-card {
            background: white;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border: 1px solid #f1f5f9;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            min-height: 300px;
            display: flex;
            flex-direction: column;
        }
        
        /* Objective info section (full width) */
        .objective-info {
            flex: 1;
            display: flex;
            flex-direction: column;
            position: relative;
        }'''
        
        if old_css in content:
            content = content.replace(old_css, new_css)
            print("✅ Updated CSS for 2-column grid layout")
        else:
            print("⚠️  Could not find exact CSS pattern, trying alternative...")
            # Try to find and replace just the grid part
            old_grid = '''        .objectives-grid {
            display: flex;
            flex-direction: column; /* Changed from grid to single column */
            gap: 0; /* Remove gap since we'll use horizontal lines */
        }'''
            
            new_grid = '''        .objectives-grid {
            display: grid;
            grid-template-columns: 1fr 1fr; /* 2 columns */
            gap: 30px; /* Gap between cards */
            margin-top: 20px;
        }'''
            
            if old_grid in content:
                content = content.replace(old_grid, new_grid)
                print("✅ Updated grid layout")
        
        # Remove all content expansion areas from objective cards
        import re
        
        # Pattern to match content expansion areas
        content_area_pattern = r'\s*<!-- Content Expansion Area -->\s*<div class="objective-content-area">.*?</div>\s*</div>'
        
        # Replace all content expansion areas with just the closing div
        content = re.sub(content_area_pattern, '\n                </div>', content, flags=re.DOTALL)
        
        print("✅ Removed all content expansion areas")
        
        # Update responsive design for mobile
        mobile_css = '''        @media (max-width: 768px) {
            .nav-container {
                flex-wrap: wrap;
                justify-content: center;
            }
            
            .nav-icon-item {
                min-width: 120px;
                padding: 20px 10px;
            }
            
            .main-content {
                padding: 40px 20px;
            }
            
            .objectives-grid {
                gap: 20px;
            }
            
            .header-container {
                flex-direction: column;
                gap: 15px;
                text-align: center;
                padding: 0 20px;
            }
            
            .project-title {
                position: static;
                margin-top: 10px;
            }
            
            /* Mobile responsive for objective cards */
            .objective-card {
                flex-direction: column;
                gap: 20px;
            }
            
            .objective-info {
                flex: none;
                width: 100%;
            }
            
            .objective-content-area {
                min-height: 200px;
            }
        }'''
        
        new_mobile_css = '''        @media (max-width: 768px) {
            .nav-container {
                flex-wrap: wrap;
                justify-content: center;
            }
            
            .nav-icon-item {
                min-width: 120px;
                padding: 20px 10px;
            }
            
            .main-content {
                padding: 40px 20px;
            }
            
            .objectives-grid {
                grid-template-columns: 1fr; /* Single column on mobile */
                gap: 20px;
            }
            
            .header-container {
                flex-direction: column;
                gap: 15px;
                text-align: center;
                padding: 0 20px;
            }
            
            .project-title {
                position: static;
                margin-top: 10px;
            }
            
            .objective-card {
                min-height: 250px;
            }
        }'''
        
        if mobile_css in content:
            content = content.replace(mobile_css, new_mobile_css)
            print("✅ Updated mobile responsive CSS")
        
        # Remove content area related CSS
        content_area_css_patterns = [
            r'\/\* Content expansion area \(right side\) \*\/.*?text-align: center;.*?color: #6b7280;.*?font-style: italic;.*?}',
            r'\.objective-content-area \{.*?\}',
            r'\.content-placeholder \{.*?\}',
            r'\.content-placeholder h4 \{.*?\}',
            r'\.content-placeholder p \{.*?\}'
        ]
        
        for pattern in content_area_css_patterns:
            content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        print("✅ Removed content area CSS")
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Objectives reorganized successfully!")
        print("📝 Changes applied:")
        print("   🗂️  2-column grid layout (2 objectives per row)")
        print("   🗑️  Removed all content expansion areas")
        print("   📱 Updated mobile responsive design")
        print("   🎨 Cleaned up CSS")
        print("🔄 Please refresh your browser to see the new layout")
        
        return True
        
    except Exception as e:
        print(f"❌ Error reorganizing objectives: {e}")
        return False

if __name__ == "__main__":
    reorganize_objectives()