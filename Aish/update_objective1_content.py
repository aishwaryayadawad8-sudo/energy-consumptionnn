#!/usr/bin/env python3
"""
Update Objective 1 content area with the provided description
"""

def update_objective1_content():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Updating Objective 1 content area...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the Objective 1 content area and replace it
        old_content = '''                    <!-- Content Expansion Area -->
                    <div class="objective-content-area">
                        <div class="content-placeholder">
                            <h4><i class="fas fa-plus-circle"></i> Content Area</h4>
                            <p>This space is reserved for adding detailed content such as:</p>
                            <ul style="text-align: left; margin-top: 15px;">
                                <li>Charts and visualizations</li>
                                <li>Model performance metrics</li>
                                <li>Country-wise energy consumption trends</li>
                                <li>Future energy demand predictions</li>
                                <li>Historical data analysis insights</li>
                            </ul>
                        </div>
                    </div>'''
        
        new_content = '''                    <!-- Content Expansion Area -->
                    <div class="objective-content-area">
                        <div class="content-placeholder">
                            <h4><i class="fas fa-info-circle"></i> Detailed Analysis</h4>
                            <p style="text-align: left; margin-top: 15px; line-height: 1.6; color: #2c3e50; font-size: 1rem;">
                                This studies how energy is used around the world by looking at past information and uses it to understand how energy needs may change in the future for different countries. It helps show usage patterns and gives useful insights that support better planning and responsible energy use.
                            </p>
                            <div style="margin-top: 20px;">
                                <h5 style="color: #667eea; margin-bottom: 10px;"><i class="fas fa-chart-bar"></i> Key Features:</h5>
                                <ul style="text-align: left; margin-top: 10px; color: #2c3e50;">
                                    <li>Historical energy consumption analysis across 128 countries</li>
                                    <li>Machine learning prediction models (7 algorithms)</li>
                                    <li>Country-wise usage pattern identification</li>
                                    <li>Future energy demand forecasting (2021-2030)</li>
                                    <li>Strategic planning support for policymakers</li>
                                    <li>Sustainable energy transition insights</li>
                                </ul>
                            </div>
                            <div style="margin-top: 20px; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
                                <h6 style="margin-bottom: 10px;"><i class="fas fa-bullseye"></i> Impact:</h6>
                                <p style="margin: 0; font-size: 0.9rem;">
                                    Enables data-driven decision making for energy policy, infrastructure planning, and sustainable development goals achievement.
                                </p>
                            </div>
                        </div>
                    </div>'''
        
        if old_content in content:
            content = content.replace(old_content, new_content)
            print("✅ Found and updated Objective 1 content area")
        else:
            # Try alternative pattern matching
            alt_pattern = '''                            <h4><i class="fas fa-plus-circle"></i> Content Area</h4>
                            <p>This space is reserved for adding detailed content such as:</p>
                            <ul style="text-align: left; margin-top: 15px;">
                                <li>Charts and visualizations</li>
                                <li>Model performance metrics</li>'''
            
            alt_replacement = '''                            <h4><i class="fas fa-info-circle"></i> Detailed Analysis</h4>
                            <p style="text-align: left; margin-top: 15px; line-height: 1.6; color: #2c3e50; font-size: 1rem;">
                                This studies how energy is used around the world by looking at past information and uses it to understand how energy needs may change in the future for different countries. It helps show usage patterns and gives useful insights that support better planning and responsible energy use.
                            </p>
                            <div style="margin-top: 20px;">
                                <h5 style="color: #667eea; margin-bottom: 10px;"><i class="fas fa-chart-bar"></i> Key Features:</h5>
                                <ul style="text-align: left; margin-top: 10px; color: #2c3e50;">
                                    <li>Historical energy consumption analysis across 128 countries</li>
                                    <li>Machine learning prediction models (7 algorithms)</li>
                                    <li>Country-wise usage pattern identification</li>
                                    <li>Future energy demand forecasting (2021-2030)</li>
                                    <li>Strategic planning support for policymakers</li>
                                    <li>Sustainable energy transition insights</li>
                                </ul>
                            </div>
                            <div style="margin-top: 20px; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
                                <h6 style="margin-bottom: 10px;"><i class="fas fa-bullseye"></i> Impact:</h6>
                                <p style="margin: 0; font-size: 0.9rem;">
                                    Enables data-driven decision making for energy policy, infrastructure planning, and sustainable development goals achievement.
                                </p>
                            </div>'''
            
            if alt_pattern in content:
                content = content.replace(alt_pattern, alt_replacement)
                print("✅ Found and updated Objective 1 content area (alternative pattern)")
            else:
                print("❌ Could not find Objective 1 content area to update")
                return False
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Objective 1 content area updated successfully!")
        print("📝 Added content:")
        print("   - Your provided description about energy usage analysis")
        print("   - Key features list with 6 specific capabilities")
        print("   - Impact section highlighting policy benefits")
        print("   - Enhanced styling with colors and icons")
        print("🔄 Please refresh your browser to see the updated content")
        
        return True
        
    except Exception as e:
        print(f"❌ Error updating Objective 1 content: {e}")
        return False

if __name__ == "__main__":
    update_objective1_content()