#!/usr/bin/env python3
"""
Add descriptions to Objective 1 and Objective 2 content areas
"""

def add_objective_descriptions():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Adding descriptions to Objective 1 and Objective 2...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Objective 1 content area update
        obj1_old = '''                    <!-- Content Expansion Area -->
                    <div class="objective-content-area">
                        <div class="content-placeholder">
                            <!-- Content area available for future use -->
                        </div>
                    </div>'''
        
        obj1_new = '''                    <!-- Content Expansion Area -->
                    <div class="objective-content-area">
                        <div class="content-placeholder">
                            <p style="text-align: left; line-height: 1.6; color: #2c3e50; font-size: 1rem; margin: 0;">
                                It helps people understand how much energy different countries use, how this changes over time, and how much energy they may need in the future. This makes it easier to plan for energy use, avoid shortages, and support a cleaner and more sustainable environment.
                            </p>
                        </div>
                    </div>'''
        
        # Find and replace Objective 1 content
        if obj1_old in content:
            content = content.replace(obj1_old, obj1_new)
            print("✅ Added description to Objective 1")
        else:
            # Try alternative pattern for Objective 1
            alt_pattern = '''                            <!-- Content area available for future use -->'''
            alt_replacement = '''                            <p style="text-align: left; line-height: 1.6; color: #2c3e50; font-size: 1rem; margin: 0;">
                                It helps people understand how much energy different countries use, how this changes over time, and how much energy they may need in the future. This makes it easier to plan for energy use, avoid shortages, and support a cleaner and more sustainable environment.
                            </p>'''
            
            if alt_pattern in content:
                content = content.replace(alt_pattern, alt_replacement)
                print("✅ Added description to Objective 1 (alternative pattern)")
        
        # Now find Objective 2 content area and add description
        # Look for Objective 2's content area pattern
        obj2_pattern = '''                                <li>COâ‚‚ emission trend analysis</li>
                                <li>Forecasting model comparisons</li>
                                <li>Environmental impact assessments</li>
                                <li>Country-wise emission patterns</li>
                                <li>Sustainability progress metrics</li>
                            </ul>'''
        
        obj2_replacement = '''                                <p style="text-align: left; line-height: 1.6; color: #2c3e50; font-size: 1rem; margin: 0;">
                                    It helps people see how much carbon pollution is being released into the air, how it has changed over the years, and how it may change in the future. This supports better decisions to reduce pollution and protect the environment.
                                </p>'''
        
        if obj2_pattern in content:
            content = content.replace(obj2_pattern, obj2_replacement)
            print("✅ Added description to Objective 2")
        else:
            # Try to find Objective 2 content area by looking for its structure
            import re
            # Look for Objective 2 content area and replace its content
            obj2_search = r'(<!-- Objective 2.*?<div class="content-placeholder">.*?<h4>.*?</h4>.*?<p>.*?</p>.*?<ul.*?>)(.*?)(</ul>.*?</div>.*?</div>)'
            
            def obj2_replace_func(match):
                return match.group(1).replace('<ul style="text-align: left; margin-top: 15px;">', '<div>').replace('</ul>', '</div>') + obj2_replacement + match.group(3).replace('</ul>', '</div>')
            
            # Alternative: find and replace the specific content for Objective 2
            obj2_alt_pattern = '''                            <p>This space is reserved for adding detailed content such as:</p>
                            <ul style="text-align: left; margin-top: 15px;">
                                <li>COâ‚‚ emission trend analysis</li>
                                <li>Forecasting model comparisons</li>
                                <li>Environmental impact assessments</li>
                                <li>Country-wise emission patterns</li>
                                <li>Sustainability progress metrics</li>
                            </ul>'''
            
            obj2_alt_replacement = '''                            <p style="text-align: left; line-height: 1.6; color: #2c3e50; font-size: 1rem; margin: 0;">
                                It helps people see how much carbon pollution is being released into the air, how it has changed over the years, and how it may change in the future. This supports better decisions to reduce pollution and protect the environment.
                            </p>'''
            
            if obj2_alt_pattern in content:
                content = content.replace(obj2_alt_pattern, obj2_alt_replacement)
                print("✅ Added description to Objective 2 (alternative pattern)")
            else:
                print("⚠️  Could not find Objective 2 content area pattern")
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Descriptions added to both objectives!")
        print("📝 Added content:")
        print("   📊 Objective 1: Energy consumption understanding and planning")
        print("   🌍 Objective 2: Carbon pollution tracking and environmental protection")
        print("🔄 Please refresh your browser to see the updated descriptions")
        
        return True
        
    except Exception as e:
        print(f"❌ Error adding descriptions: {e}")
        return False

if __name__ == "__main__":
    add_objective_descriptions()