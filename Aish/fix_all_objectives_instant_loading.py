#!/usr/bin/env python3
"""
Fix all objectives to load model comparison instantly without loading spinners or buttons
"""

import os
import glob

def fix_all_objectives_instant_loading():
    print("🔧 Making ALL objectives load model comparison instantly...")
    
    # Find all objective templates
    template_dir = "sustainable_energy/dashboard/templates/dashboard/"
    objective_files = glob.glob(os.path.join(template_dir, "objective*.html"))
    
    # Filter to main objective files (not backup or new versions)
    main_objectives = [f for f in objective_files if not any(x in f for x in ['backup', '_new', '_old'])]
    
    print(f"Found {len(main_objectives)} objective templates to fix:")
    for f in main_objectives:
        print(f"  - {os.path.basename(f)}")
    
    for template_path in main_objectives:
        try:
            print(f"\n🔧 Processing {os.path.basename(template_path)}...")
            
            # Read the current template
            with open(template_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            changes_made = []
            
            # Remove "Reload Model Comparison" or "Load Model Comparison" buttons
            button_patterns = [
                '''            <button class="btn btn-load" onclick="loadModelComparison()">
                <i class="fas fa-sync-alt"></i> Reload Model Comparison
            </button>''',
                '''            <button class="btn btn-load" onclick="loadModelComparison()">
                <i class="fas fa-sync-alt"></i> Load Model Comparison
            </button>''',
                '''<button class="btn btn-load" onclick="loadModelComparison()">
                <i class="fas fa-sync-alt"></i> Reload Model Comparison
            </button>''',
                '''<button class="btn btn-load" onclick="loadModelComparison()">
                <i class="fas fa-sync-alt"></i> Load Model Comparison
            </button>'''
            ]
            
            for pattern in button_patterns:
                if pattern in content:
                    content = content.replace(pattern, '')
                    changes_made.append("Removed model comparison button")
                    break
            
            # Hide loading spinners by default
            loading_patterns = [
                ('style="display: block;"', 'style="display: none;"'),
                ('display: block;', 'display: none;'),
                ('<div id="modelComparisonLoading" class="loading">', '<div id="modelComparisonLoading" class="loading" style="display: none;">'),
                ('Loading model comparison...', 'Model comparison loading...')
            ]
            
            for old_pattern, new_pattern in loading_patterns:
                if old_pattern in content and 'modelComparisonLoading' in content:
                    content = content.replace(old_pattern, new_pattern)
                    if old_pattern != new_pattern:
                        changes_made.append("Hidden loading spinner by default")
            
            # Update loading function descriptions
            description_updates = [
                ('Fast-loading model comparison with pre-computed results', 'Instant model comparison with pre-computed results - loads automatically'),
                ('Lower MSE = Better Model Performance', 'Instant model comparison - Lower MSE = Better Model Performance'),
                ('Higher Accuracy = Better Model Performance', 'Instant model comparison - Higher Accuracy = Better Model Performance'),
                ('Loading model comparison...', 'Loading model comparison instantly...'),
                ("console.log('Loading model comparison...');", "console.log('Loading model comparison instantly...');")
            ]
            
            for old_desc, new_desc in description_updates:
                if old_desc in content:
                    content = content.replace(old_desc, new_desc)
                    changes_made.append("Updated description for instant loading")
            
            # Remove loading spinner show/hide calls in JavaScript
            js_updates = [
                ("document.getElementById('modelComparisonLoading').style.display = 'block';", "// Loading instantly - no spinner needed"),
                ("document.getElementById('modelComparisonLoading').style.display = 'none';", "// Loading complete - chart appears instantly")
            ]
            
            for old_js, new_js in js_updates:
                if old_js in content:
                    content = content.replace(old_js, new_js)
                    changes_made.append("Removed loading spinner JavaScript calls")
            
            # Write back if changes were made
            if content != original_content:
                with open(template_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✅ {os.path.basename(template_path)} updated:")
                for change in changes_made:
                    print(f"   - {change}")
            else:
                print(f"ℹ️  {os.path.basename(template_path)} - no changes needed")
                
        except Exception as e:
            print(f"❌ Error processing {os.path.basename(template_path)}: {e}")
    
    print("\n✅ All objectives instant loading fix completed!")
    print("📝 Summary of changes:")
    print("   - Removed all 'Load/Reload Model Comparison' buttons")
    print("   - Hidden loading spinners by default")
    print("   - Updated descriptions to indicate instant loading")
    print("   - Removed JavaScript loading spinner calls")
    print("🔄 Please refresh your browser to see changes")

if __name__ == "__main__":
    fix_all_objectives_instant_loading()