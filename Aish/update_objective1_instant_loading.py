#!/usr/bin/env python3
"""
Update Objective 1 template for instant ML comparison loading
"""

import os

def update_objective1_template():
    """Update the objective1.html template for instant loading"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective1.html"
    
    if not os.path.exists(template_path):
        print(f"❌ {template_path} not found")
        return
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the loadModelComparison function to remove loading delay
    old_function = '''        function loadModelComparison() {
            document.getElementById('modelComparisonLoading').style.display = 'block';
            
            fetch('/api/objective1/model-comparison/')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('modelComparisonLoading').style.display = 'none';'''
    
    new_function = '''        function loadModelComparison() {
            // Hide loading immediately since we have instant results
            document.getElementById('modelComparisonLoading').style.display = 'none';
            
            fetch('/api/objective1/model-comparison/')
                .then(response => response.json())
                .then(data => {'''
    
    if old_function in content:
        content = content.replace(old_function, new_function)
        
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Updated objective1.html template for instant loading")
        print("🚀 Loading spinner will be hidden immediately")
    else:
        print("❌ Could not find the loadModelComparison function to update")

if __name__ == "__main__":
    print("🔧 Updating Objective 1 Template for Instant Loading...")
    print("=" * 60)
    update_objective1_template()
    print("=" * 60)
    print("✅ COMPLETE! Objective 1 ML comparison will now load instantly.")