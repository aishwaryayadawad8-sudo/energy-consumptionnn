#!/usr/bin/env python3
"""
Fix Objective 5 to load model comparison instantly without loading spinner or button
"""

def fix_objective5_instant_loading():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective5_classification.html"
    
    print("🔧 Making Objective 5 model comparison load instantly...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove the "Reload Model Comparison" button
        button_section = '''            <button class="btn btn-load" onclick="loadModelComparison()">
                <i class="fas fa-sync-alt"></i> Reload Model Comparison
            </button>'''
        
        if button_section in content:
            content = content.replace(button_section, '')
            print("✅ Removed 'Reload Model Comparison' button")
        
        # Hide the loading spinner by default and show it only briefly
        loading_div = '''            <div id="modelComparisonLoading" class="loading" style="display: block;">'''
        loading_div_hidden = '''            <div id="modelComparisonLoading" class="loading" style="display: none;">'''
        
        if loading_div in content:
            content = content.replace(loading_div, loading_div_hidden)
            print("✅ Set loading spinner to hidden by default")
        
        # Update the loadModelComparison function to be faster
        old_loading_logic = '''        function loadModelComparison() {
            console.log('Loading model comparison...');
            document.getElementById('modelComparisonLoading').style.display = 'block';'''
        
        new_loading_logic = '''        function loadModelComparison() {
            console.log('Loading model comparison instantly...');
            // No loading spinner needed for instant loading'''
        
        if old_loading_logic in content:
            content = content.replace(old_loading_logic, new_loading_logic)
            print("✅ Updated loading function for instant loading")
        
        # Remove the loading spinner hide call since we don't show it
        old_hide_loading = '''                    document.getElementById('modelComparisonLoading').style.display = 'none';'''
        new_hide_loading = '''                    // Loading complete - chart will appear instantly'''
        
        if old_hide_loading in content:
            content = content.replace(old_hide_loading, new_hide_loading)
            print("✅ Removed loading spinner hide call")
        
        # Update the section description to indicate instant loading
        old_description = '''            <p class="text-muted">Fast-loading model comparison with pre-computed results</p>'''
        new_description = '''            <p class="text-muted">Instant model comparison with pre-computed results - loads automatically</p>'''
        
        if old_description in content:
            content = content.replace(old_description, new_description)
            print("✅ Updated description to indicate instant loading")
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Objective 5 instant loading fix applied successfully!")
        print("📝 Changes made:")
        print("   - Removed 'Reload Model Comparison' button")
        print("   - Hidden loading spinner by default")
        print("   - Updated loading function for instant display")
        print("   - Updated description text")
        print("🔄 Please refresh your browser to see changes")
        
    except FileNotFoundError:
        print(f"❌ Template file not found: {template_path}")
    except Exception as e:
        print(f"❌ Error applying fix: {e}")

if __name__ == "__main__":
    fix_objective5_instant_loading()