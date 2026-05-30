#!/usr/bin/env python3
"""
Script to restore the original toggle behavior - objectives appear only after clicking Country Forecasts
"""

import os

def restore_toggle_behavior():
    """Restore the original toggle behavior for Country Forecasts"""
    
    file_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return False
    
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Restore CSS - hide objectives by default
        new_css = """    /* Objectives Grid (Always visible) */
    .objectives-section {
        display: block;
        padding: 60px 0;
        background: #f8fafc;
    }"""
        
        original_css = """    /* Objectives Grid (Hidden by default, shown when Country Forecasts is clicked) */
    .objectives-section {
        display: none;
        padding: 60px 0;
        background: #f8fafc;
    }
    
    .objectives-section.active {
        display: block;
    }"""
        
        if new_css in content:
            content = content.replace(new_css, original_css)
            print("✅ Restored CSS - objectives hidden by default")
        else:
            print("⚠️ CSS pattern not found")
        
        # Restore main content section visibility
        hidden_content = '<!-- Content Section (Hidden by default) -->\n<section class="content-section" id="main-content" style="display: none;">'
        visible_content = '<!-- Content Section -->\n<section class="content-section" id="main-content">'
        
        if hidden_content in content:
            content = content.replace(hidden_content, visible_content)
            print("✅ Restored main content section visibility")
        
        # Restore original JavaScript toggle behavior
        new_js = """<script>
// Handle Country Forecasts tab click - scroll to objectives section
document.getElementById('country-forecasts-tab').addEventListener('click', function(e) {
    e.preventDefault();
    
    // Toggle active state
    document.querySelectorAll('.nav-tab').forEach(tab => tab.classList.remove('active'));
    this.classList.add('active');
    
    // Scroll to objectives section
    const objectivesSection = document.getElementById('objectives-section');
    objectivesSection.scrollIntoView({ behavior: 'smooth' });
});

// Handle other nav tabs - remove active state from country forecasts
document.querySelectorAll('.nav-tab:not(#country-forecasts-tab)').forEach(tab => {
    tab.addEventListener('click', function() {
        document.getElementById('country-forecasts-tab').classList.remove('active');
    });
});
</script>"""
        
        original_js = """<script>
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
</script>"""
        
        if new_js in content:
            content = content.replace(new_js, original_js)
            print("✅ Restored original JavaScript toggle behavior")
        else:
            print("⚠️ JavaScript pattern not found")
        
        # Write the file back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully updated {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating file: {e}")
        return False

def main():
    """Main function"""
    print("🔄 Restoring Original Toggle Behavior")
    print("="*50)
    print("   Objectives will appear ONLY after clicking 'Country Energy Forecasts'")
    print()
    
    success = restore_toggle_behavior()
    
    if success:
        print("\n✅ SUCCESS! Original behavior restored!")
        print("\n📋 How it works now:")
        print("   1. Main page shows global energy content by default")
        print("   2. Click 'COUNTRY ENERGY FORECASTS' tab to show all objectives")
        print("   3. Click other tabs to hide objectives and show main content")
        print("\n🔄 Refresh your browser to see the restored behavior!")
    else:
        print("\n❌ Failed to restore behavior.")

if __name__ == "__main__":
    main()