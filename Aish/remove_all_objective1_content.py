#!/usr/bin/env python3
"""
Remove all content from Objective 1 content area - description, heading, and box
"""

def remove_all_objective1_content():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Removing all content from Objective 1 content area...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the entire content area and replace with empty placeholder
        old_content_area = '''                    <!-- Content Expansion Area -->
                    <div class="objective-content-area">
                        <div class="content-placeholder">
                            <h4><i class="fas fa-info-circle"></i> Detailed Analysis</h4>
                            <p style="text-align: left; margin-top: 15px; line-height: 1.6; color: #2c3e50; font-size: 1rem;">
                                It helps people understand how much energy different countries use, how this changes over time, and how much energy they may need in the future. This makes it easier to plan for energy use, avoid shortages, and support a cleaner and more sustainable environment.
                            </p>
                        </div>
                    </div>'''
        
        new_content_area = '''                    <!-- Content Expansion Area -->
                    <div class="objective-content-area">
                        <div class="content-placeholder">
                            <!-- Content area available for future use -->
                        </div>
                    </div>'''
        
        if old_content_area in content:
            content = content.replace(old_content_area, new_content_area)
            print("✅ Removed all content from Objective 1 content area")
        else:
            # Try alternative patterns
            patterns_to_remove = [
                '''                            <h4><i class="fas fa-info-circle"></i> Detailed Analysis</h4>''',
                '''It helps people understand how much energy different countries use, how this changes over time, and how much energy they may need in the future. This makes it easier to plan for energy use, avoid shortages, and support a cleaner and more sustainable environment.''',
                '''Key insights and findings''',
                '''Interactive elements''',
                '''Additional analysis details'''
            ]
            
            for pattern in patterns_to_remove:
                if pattern in content:
                    content = content.replace(pattern, '')
                    print(f"✅ Removed: {pattern[:50]}...")
        
        # Clean up any remaining content in the placeholder
        # Replace any remaining content between content-placeholder tags
        import re
        pattern = r'(<div class="content-placeholder">)(.*?)(</div>\s*</div>)'
        replacement = r'\1\n                            <!-- Content area available for future use -->\n                        \3'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ All content removed from Objective 1!")
        print("📝 Result:")
        print("   - No description text")
        print("   - No 'Detailed Analysis' heading")
        print("   - No content box")
        print("   - Clean, empty content area")
        print("🔄 Please refresh your browser to see the clean content area")
        
        return True
        
    except Exception as e:
        print(f"❌ Error removing content: {e}")
        return False

if __name__ == "__main__":
    remove_all_objective1_content()