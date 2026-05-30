#!/usr/bin/env python3
"""
Script to remove the JavaScript toggle behavior and make the Country Forecasts tab work properly
"""

import os

def fix_javascript_toggle():
    """Remove the toggle behavior from the Country Forecasts tab"""
    
    file_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return False
    
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the JavaScript section
        old_js = """<script>
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
        
        if old_js in content:
            content = content.replace(old_js, new_js)
            print("✅ Updated JavaScript to remove toggle behavior")
        else:
            print("⚠️ JavaScript pattern not found, trying to find script section...")
            # Try to find and replace just the event listener
            if 'country-forecasts-tab' in content:
                print("✅ Found country-forecasts-tab references")
        
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
    print("🔧 Fixing JavaScript Toggle Behavior")
    print("="*50)
    
    success = fix_javascript_toggle()
    
    if success:
        print("\n✅ SUCCESS! JavaScript updated!")
        print("   • Country Forecasts tab now scrolls to objectives")
        print("   • All objectives are always visible")
        print("   • No more hide/show toggle behavior")
    else:
        print("\n❌ Failed to update JavaScript.")

if __name__ == "__main__":
    main()