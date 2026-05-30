#!/usr/bin/env python3
"""
Script to diagnose and fix the objectives not appearing issue
"""

import os

def diagnose_and_fix_objectives():
    """Diagnose and fix the objectives toggle functionality"""
    
    selector_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(selector_path):
        print(f"❌ File not found: {selector_path}")
        return False
    
    try:
        # Read the selector file
        with open(selector_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("🔍 Diagnosing objectives toggle issue...")
        
        # Check if objectives section exists
        if 'id="objectives-section"' in content:
            print("✅ Objectives section found")
        else:
            print("❌ Objectives section missing")
        
        # Check if Country Forecasts tab exists
        if 'id="country-forecasts-tab"' in content:
            print("✅ Country Forecasts tab found")
        else:
            print("❌ Country Forecasts tab missing")
        
        # Check CSS for objectives section
        if '.objectives-section {' in content:
            print("✅ Objectives CSS found")
        else:
            print("❌ Objectives CSS missing")
        
        # Fix 1: Ensure objectives section has proper CSS
        css_fix = '''    /* Objectives Grid (Hidden by default, shown when Country Forecasts is clicked) */
    .objectives-section {
        display: none;
        padding: 60px 0;
        background: #f8fafc;
    }
    
    .objectives-section.active {
        display: block;
    }'''
        
        # Find existing CSS and replace/add it
        css_start = content.find('.objectives-section {')
        if css_start != -1:
            # Find the end of the CSS block
            css_end = content.find('}', content.find('}', css_start) + 1) + 1
            # Replace the CSS
            before_css = content[:css_start - 4]  # Include the comment
            after_css = content[css_end:]
            content = before_css + css_fix + after_css
            print("✅ Fixed objectives CSS")
        else:
            # Add CSS before </style>
            style_end = content.find('</style>')
            if style_end != -1:
                content = content[:style_end] + '\n' + css_fix + '\n' + content[style_end:]
                print("✅ Added objectives CSS")
        
        # Fix 2: Ensure JavaScript toggle functionality exists
        js_fix = '''
<script>
// Handle Country Forecasts tab click
document.getElementById('country-forecasts-tab').addEventListener('click', function(e) {
    e.preventDefault();
    
    // Toggle active state
    document.querySelectorAll('.nav-tab').forEach(tab => tab.classList.remove('active'));
    this.classList.add('active');
    
    // Show/hide sections
    const mainContent = document.getElementById('main-content');
    const objectivesSection = document.getElementById('objectives-section');
    
    if (objectivesSection.classList.contains('active')) {
        // Hide objectives, show main content
        objectivesSection.classList.remove('active');
        mainContent.style.display = 'block';
        this.classList.remove('active');
    } else {
        // Show objectives, hide main content
        objectivesSection.classList.add('active');
        mainContent.style.display = 'none';
    }
});

// Handle other nav tabs
document.querySelectorAll('.nav-tab:not(#country-forecasts-tab)').forEach(tab => {
    tab.addEventListener('click', function() {
        // Reset objectives section
        document.getElementById('objectives-section').classList.remove('active');
        document.getElementById('main-content').style.display = 'block';
        document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
    });
});
</script>'''
        
        # Check if JavaScript exists and fix it
        if 'country-forecasts-tab' in content and 'addEventListener' in content:
            print("✅ JavaScript toggle found")
        else:
            # Add JavaScript before </body> or {% endblock %}
            if '{% endblock %}' in content:
                endblock_pos = content.rfind('{% endblock %}')
                content = content[:endblock_pos] + js_fix + '\n\n' + content[endblock_pos:]
                print("✅ Added JavaScript toggle functionality")
        
        # Fix 3: Ensure Country Forecasts tab has correct ID
        if 'id="country-forecasts-tab"' not in content:
            # Find and fix the Country Forecasts tab
            country_tab_pattern = '<a href="#" class="nav-tab">\n            <div class="nav-icon"><i class="fas fa-globe"></i></div>\n            <span>COUNTRY ENERGY FORECASTS</span>'
            country_tab_fixed = '<a href="#" class="nav-tab" id="country-forecasts-tab">\n            <div class="nav-icon"><i class="fas fa-globe"></i></div>\n            <span>COUNTRY ENERGY FORECASTS</span>'
            
            if country_tab_pattern in content:
                content = content.replace(country_tab_pattern, country_tab_fixed)
                print("✅ Fixed Country Forecasts tab ID")
        
        # Write the file back
        with open(selector_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully updated {selector_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing objectives: {e}")
        return False

def main():
    """Main function"""
    print("🔧 Diagnosing and Fixing Objectives Toggle Issue")
    print("="*60)
    print("   • Checking objectives section existence")
    print("   • Fixing CSS for proper hide/show")
    print("   • Ensuring JavaScript toggle works")
    print("   • Fixing Country Forecasts tab ID")
    print()
    
    success = diagnose_and_fix_objectives()
    
    if success:
        print("\n✅ SUCCESS! Objectives toggle should now work!")
        print("\n🔧 What was fixed:")
        print("   • Objectives CSS (display: none/block)")
        print("   • JavaScript toggle functionality")
        print("   • Country Forecasts tab ID")
        print("   • Proper event listeners")
        print("\n🔄 How to test:")
        print("   1. Restart Django server: python manage.py runserver")
        print("   2. Clear browser cache (Ctrl+Shift+R)")
        print("   3. Visit: http://localhost:8000/objectives/")
        print("   4. Click 'COUNTRY ENERGY FORECASTS' tab")
        print("   5. Objectives should appear!")
        print("\n🎯 If still not working:")
        print("   • Check browser console for JavaScript errors")
        print("   • Try incognito/private browsing mode")
        print("   • Ensure you're clicking the correct tab")
    else:
        print("\n❌ Failed to fix objectives toggle.")

if __name__ == "__main__":
    main()