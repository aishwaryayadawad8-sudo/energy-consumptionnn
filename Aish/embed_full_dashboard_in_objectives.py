#!/usr/bin/env python3
"""
Script to embed the full Explore Dashboard content directly in the objectives section
"""

import os

def get_dashboard_content():
    """Extract the main dashboard content from index.html"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    if not os.path.exists(index_path):
        print(f"❌ File not found: {index_path}")
        return None
    
    try:
        # Read the index file
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract the main dashboard content (everything inside body)
        body_start = content.find('<body>')
        body_end = content.find('</body>')
        
        if body_start != -1 and body_end != -1:
            # Get content between body tags
            body_content = content[body_start + 6:body_end]
            
            # Extract the dashboard container content
            container_start = body_content.find('<div class="dashboard-container">')
            container_end = body_content.find('</div>\n\n    <script')
            
            if container_start != -1 and container_end != -1:
                dashboard_content = body_content[container_start:container_end + 6]
                print("✅ Successfully extracted dashboard content")
                return dashboard_content
        
        print("⚠️ Could not find dashboard content boundaries")
        return None
        
    except Exception as e:
        print(f"❌ Error reading index.html: {e}")
        return None

def get_dashboard_styles():
    """Extract the styles from index.html"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    try:
        # Read the index file
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract styles
        style_start = content.find('<style>')
        style_end = content.find('</style>')
        
        if style_start != -1 and style_end != -1:
            styles = content[style_start:style_end + 8]
            print("✅ Successfully extracted dashboard styles")
            return styles
        
        return None
        
    except Exception as e:
        print(f"❌ Error extracting styles: {e}")
        return None

def get_dashboard_scripts():
    """Extract the JavaScript from index.html"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    try:
        # Read the index file
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract scripts (everything after the last </div> before </body>)
        script_start = content.find('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>')
        script_end = content.find('</body>')
        
        if script_start != -1 and script_end != -1:
            scripts = content[script_start:script_end].strip()
            print("✅ Successfully extracted dashboard scripts")
            return scripts
        
        return None
        
    except Exception as e:
        print(f"❌ Error extracting scripts: {e}")
        return None

def embed_dashboard_in_objectives():
    """Embed the full dashboard content in the objectives section"""
    
    selector_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(selector_path):
        print(f"❌ File not found: {selector_path}")
        return False
    
    try:
        # Get dashboard components
        dashboard_content = get_dashboard_content()
        dashboard_styles = get_dashboard_styles()
        dashboard_scripts = get_dashboard_scripts()
        
        if not all([dashboard_content, dashboard_styles, dashboard_scripts]):
            print("❌ Failed to extract dashboard components")
            return False
        
        # Read the selector file
        with open(selector_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add dashboard styles to the existing styles section
        existing_styles_end = content.find('</style>')
        if existing_styles_end != -1:
            content = content[:existing_styles_end] + '\n\n    /* Embedded Dashboard Styles */\n' + dashboard_styles[7:-8] + '\n' + content[existing_styles_end:]
            print("✅ Added dashboard styles")
        
        # Replace the 8th objective card with the full dashboard
        old_card = '''            
            <!-- Objective 8: Explore Dashboard -->
            <div class="objective-card">
                <div class="objective-header">
                    <div class="objective-icon">
                        <i class="fas fa-search"></i>
                    </div>
                    <div class="objective-number">08</div>
                </div>
                <h3 class="objective-title">Explore Dashboard</h3>
                <p class="objective-description">
                    Interactive country energy analysis with search functionality, world map visualization, and comprehensive energy profiles for 128+ countries.
                </p>
                <a href="/" class="objective-btn">
                    View Analysis
                </a>
            </div>'''
        
        new_card = f'''            
            <!-- Objective 8: Full Explore Dashboard -->
            <div class="objective-card" style="grid-column: 1 / -1; max-width: none;">
                <div class="objective-header">
                    <div class="objective-icon">
                        <i class="fas fa-search"></i>
                    </div>
                    <div class="objective-number">08</div>
                </div>
                <h3 class="objective-title">Explore Dashboard</h3>
                <p class="objective-description">
                    Interactive country energy analysis with search functionality, world map visualization, and comprehensive energy profiles for 128+ countries.
                </p>
                
                <!-- Full Dashboard Content -->
                <div style="margin-top: 20px;">
                    {dashboard_content}
                </div>
            </div>'''
        
        if old_card in content:
            content = content.replace(old_card, new_card)
            print("✅ Replaced objective card with full dashboard")
        else:
            print("⚠️ Could not find objective card to replace")
        
        # Add dashboard scripts before the closing script tag
        script_section_end = content.find('</script>\n\n{% endblock %}')
        if script_section_end != -1:
            content = content[:script_section_end] + '\n\n// Embedded Dashboard Scripts\n' + dashboard_scripts + '\n' + content[script_section_end:]
            print("✅ Added dashboard scripts")
        
        # Write the file back
        with open(selector_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully updated {selector_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error embedding dashboard: {e}")
        return False

def main():
    """Main function"""
    print("🚀 Embedding Full Dashboard in Objectives Section")
    print("="*60)
    print("   • Extracting complete dashboard content")
    print("   • Embedding in objective #8 card")
    print("   • Including all styles and scripts")
    print()
    
    success = embed_dashboard_in_objectives()
    
    if success:
        print("\n✅ SUCCESS! Full dashboard embedded in objectives!")
        print("\n📋 What's new:")
        print("   • Objective #8 now contains the complete Explore Dashboard")
        print("   • Country search functionality available in objectives section")
        print("   • Interactive world map embedded")
        print("   • All charts and analysis tools included")
        print("\n🎯 User Experience:")
        print("   1. Visit /objectives/")
        print("   2. Click 'COUNTRY ENERGY FORECASTS' tab")
        print("   3. Scroll down to see full Explore Dashboard as objective #8")
        print("   4. Use country search directly in the objectives section")
        print("\n🔄 Refresh your browser to see the embedded dashboard!")
    else:
        print("\n❌ Failed to embed dashboard. Please check the files manually.")

if __name__ == "__main__":
    main()