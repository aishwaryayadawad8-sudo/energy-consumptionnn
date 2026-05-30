#!/usr/bin/env python3
"""
Remove the Key Features and Impact sections from Objective 1, keeping only the main description
"""

def remove_objective1_extra_content():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Removing Key Features and Impact sections from Objective 1...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and remove the Key Features section
        key_features_section = '''                            <div style="margin-top: 20px;">
                                <h5 style="color: #667eea; margin-bottom: 10px;"><i class="fas fa-chart-bar"></i> Key Features:</h5>
                                <ul style="text-align: left; margin-top: 10px; color: #2c3e50;">
                                    <li>Historical energy consumption analysis across 128 countries</li>
                                    <li>Machine learning prediction models (7 algorithms)</li>
                                    <li>Country-wise usage pattern identification</li>
                                    <li>Future energy demand forecasting (2021-2030)</li>
                                    <li>Strategic planning support for policymakers</li>
                                    <li>Sustainable energy transition insights</li>
                                </ul>
                            </div>'''
        
        # Find and remove the Impact section
        impact_section = '''                            <div style="margin-top: 20px; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
                                <h6 style="margin-bottom: 10px;"><i class="fas fa-bullseye"></i> Impact:</h6>
                                <p style="margin: 0; font-size: 0.9rem;">
                                    Enables data-driven decision making for energy policy, infrastructure planning, and sustainable development goals achievement.
                                </p>
                            </div>'''
        
        # Remove both sections
        if key_features_section in content:
            content = content.replace(key_features_section, '')
            print("✅ Removed Key Features section")
        
        if impact_section in content:
            content = content.replace(impact_section, '')
            print("✅ Removed Impact section")
        
        # Clean up any extra whitespace or empty divs
        content = content.replace('\n                            \n                        </div>', '\n                        </div>')
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Extra content removed from Objective 1!")
        print("📝 Remaining content:")
        print("   - Main description only")
        print("   - Clean, simple layout")
        print("🔄 Please refresh your browser to see the simplified content")
        
        return True
        
    except Exception as e:
        print(f"❌ Error removing extra content: {e}")
        return False

if __name__ == "__main__":
    remove_objective1_extra_content()