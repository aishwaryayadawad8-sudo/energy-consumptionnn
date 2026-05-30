#!/usr/bin/env python3
"""
Show Interactive Visualization Controls before country search
"""

import os

def show_controls_before_search():
    """Update dashboard to show controls before search"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔄 Moving visualization controls before search...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Change controls CSS to be visible by default (remove display: none)
        old_controls_css = '''        .visualization-controls {
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            display: none; /* Hidden initially */
        }'''
        
        new_controls_css = '''        .visualization-controls {
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            /* Always visible */
        }'''
        
        if old_controls_css in content:
            content = content.replace(old_controls_css, new_controls_css)
            print("✅ Updated controls CSS to be always visible")
        
        # 2. Move the visualization controls HTML to appear after header but before search
        # First, find and remove the current controls HTML
        controls_start = content.find('<!-- Visualization Controls -->')
        if controls_start != -1:
            # Find the end of the controls section
            controls_end = content.find('</div>', controls_start)
            # Find the actual end by counting divs
            div_count = 0
            pos = controls_start
            while pos < len(content):
                if content[pos:pos+5] == '<div ':
                    div_count += 1
                elif content[pos:pos+6] == '</div>':
                    div_count -= 1
                    if div_count == 0:
                        controls_end = pos + 6
                        break
                pos += 1
            
            # Extract the controls HTML
            controls_html = content[controls_start:controls_end]
            
            # Remove from current location
            content = content[:controls_start] + content[controls_end:]
            
            # Insert after header section but before search section
            search_section_start = content.find('<!-- Unified Search Section -->')
            if search_section_start == -1:
                search_section_start = content.find('<div class="search-section">')
            
            if search_section_start != -1:
                content = content[:search_section_start] + controls_html + '\n\n        ' + content[search_section_start:]
                print("✅ Moved controls before search section")
            else:
                print("⚠️ Could not find search section, adding after header")
                header_end = content.find('</div>', content.find('header-section'))
                if header_end != -1:
                    content = content[:header_end+6] + '\n\n        ' + controls_html + content[header_end+6:]
        
        # 3. Remove the code that shows controls after analysis
        old_show_controls = '''            // Show visualization controls
            const visualizationControls = document.getElementById('visualizationControls');
            if (visualizationControls) {
                visualizationControls.style.display = 'block';
            }'''
        
        if old_show_controls in content:
            content = content.replace(old_show_controls, '')
            print("✅ Removed code that shows controls after analysis")
        
        # 4. Update the controls description to indicate they work after country selection
        old_header = '''            <div class="controls-header">
                <i class="fas fa-sliders-h"></i>
                <h3>Interactive Visualization Controls</h3>
            </div>'''
        
        new_header = '''            <div class="controls-header">
                <i class="fas fa-sliders-h"></i>
                <h3>Interactive Visualization Controls</h3>
            </div>
            
            <div class="mb-3" style="color: #666; font-size: 14px; text-align: center;">
                <i class="fas fa-info-circle"></i> Select a time period, then search and analyze a country to see filtered charts
            </div>'''
        
        if old_header in content:
            content = content.replace(old_header, new_header)
            print("✅ Added helpful instruction text")
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully moved controls before search!")
        return True
        
    except Exception as e:
        print(f"❌ Error updating controls position: {e}")
        return False

def main():
    """Main function"""
    print("🔄 MOVING CONTROLS BEFORE SEARCH")
    print("=" * 50)
    print("   • Controls visible immediately")
    print("   • Appears before country search")
    print("   • Users can select time period first")
    print("   • Charts filter when country analyzed")
    print("=" * 50)
    
    success = show_controls_before_search()
    
    if success:
        print("\n" + "=" * 50)
        print("✅ CONTROLS MOVED SUCCESSFULLY!")
        print("=" * 50)
        print("\n🎯 New Layout Order:")
        print("   1. Header (Explore Dashboard)")
        print("   2. Interactive Visualization Controls ✅")
        print("   3. Country Search Section")
        print("   4. World Map")
        print("   5. Results (after analysis)")
        
        print("\n🔄 User Experience:")
        print("   1. User sees controls immediately")
        print("   2. User selects preferred time period")
        print("   3. User searches for country")
        print("   4. User clicks 'Analyze Country'")
        print("   5. Charts appear filtered by selected period")
        
        print("\n📊 Time Period Options:")
        print("   • All Years (2000-2030) - Default selected")
        print("   • Historical (2000-2020)")
        print("   • Predictions (2021-2030)")
        print("   • Recent Trends (2015-2030)")
        
        print("\n🚀 Ready to Test:")
        print("   1. Refresh browser (Ctrl+F5)")
        print("   2. See controls at top of page")
        print("   3. Select a time period")
        print("   4. Search for country")
        print("   5. Analyze to see filtered charts")
        
        print("\n🎯 CONTROLS NOW VISIBLE FIRST!")
        
    else:
        print("\n❌ Failed to move controls.")

if __name__ == "__main__":
    main()