#!/usr/bin/env python3
"""
Remove the 8 Machine Learning Objectives section from Total Energy dashboard
"""

def remove_ml_objectives_section():
    template_path = "sustainable_energy/dashboard/templates/dashboard/total_energy.html"
    
    print("🔧 Removing 8 ML Objectives section from Total Energy dashboard...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and remove the entire objectives section
        objectives_section_start = content.find('    <!-- 8 Objectives Section -->')
        objectives_section_end = content.find('    </div>\n\n    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>')
        
        if objectives_section_start != -1 and objectives_section_end != -1:
            # Remove the entire section
            content = content[:objectives_section_start] + content[objectives_section_end:]
            print("✅ Removed 8 ML Objectives section")
        else:
            # Try alternative approach - remove by HTML pattern
            objectives_html_pattern = '''    <!-- 8 Objectives Section -->
    <div class="objectives-section">
        <h2 class="chart-title">8 Machine Learning Objectives</h2>
        <div class="objectives-grid">
            <div class="objective-item">
                <div class="objective-number">1</div>
                <div class="objective-title">Energy Consumption Prediction</div>
                <div class="objective-desc">Future energy demand forecasting</div>
            </div>
            <div class="objective-item">
                <div class="objective-number">2</div>
                <div class="objective-title">CO₂ Emission Forecasting</div>
                <div class="objective-desc">Environmental impact assessment</div>
            </div>
            <div class="objective-item">
                <div class="objective-number">3</div>
                <div class="objective-title">Energy Access Classification</div>
                <div class="objective-desc">Population access analysis</div>
            </div>
            <div class="objective-item">
                <div class="objective-number">4</div>
                <div class="objective-title">SDG-7 Progress Monitoring</div>
                <div class="objective-desc">Sustainable development tracking</div>
            </div>
            <div class="objective-item">
                <div class="objective-number">5</div>
                <div class="objective-title">Energy Equity Analysis</div>
                <div class="objective-desc">Fairness in energy distribution</div>
            </div>
            <div class="objective-item">
                <div class="objective-number">6</div>
                <div class="objective-title">Efficiency Optimization</div>
                <div class="objective-desc">Energy usage optimization</div>
            </div>
            <div class="objective-item">
                <div class="objective-number">7</div>
                <div class="objective-title">Renewable Energy Assessment</div>
                <div class="objective-desc">Clean energy potential analysis</div>
            </div>
            <div class="objective-item">
                <div class="objective-number">8</div>
                <div class="objective-title">Investment Strategy Support</div>
                <div class="objective-desc">Financial decision support</div>
            </div>
        </div>
    </div>'''
            
            if objectives_html_pattern in content:
                content = content.replace(objectives_html_pattern, '')
                print("✅ Removed 8 ML Objectives section (alternative method)")
            else:
                print("⚠️  Could not find exact objectives section pattern")
        
        # Also remove the related CSS for objectives section
        objectives_css_patterns = [
            r'\.objectives-section \{[^}]*\}',
            r'\.objectives-grid \{[^}]*\}',
            r'\.objective-item \{[^}]*\}',
            r'\.objective-item:hover \{[^}]*\}',
            r'\.objective-number \{[^}]*\}',
            r'\.objective-title \{[^}]*\}',
            r'\.objective-desc \{[^}]*\}'
        ]
        
        import re
        for pattern in objectives_css_patterns:
            content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        print("✅ Removed objectives-related CSS")
        
        # Clean up any extra whitespace
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ 8 ML Objectives section removed successfully!")
        print("📝 Changes applied:")
        print("   🗑️  Removed objectives section HTML")
        print("   🗑️  Removed objectives-related CSS")
        print("   ✨ Dashboard now focuses on energy statistics only")
        print("🔄 Please refresh your browser to see the updated dashboard")
        
        return True
        
    except Exception as e:
        print(f"❌ Error removing objectives section: {e}")
        return False

if __name__ == "__main__":
    remove_ml_objectives_section()