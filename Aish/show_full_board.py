#!/usr/bin/env python3
"""
Script to show the full board by making all objectives visible by default
"""

import os

def fix_objective_selector():
    """Fix the objective selector to show all objectives by default"""
    
    file_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return False
    
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the CSS to show objectives by default
        old_css = """    /* Objectives Grid (Hidden by default, shown when Country Forecasts is clicked) */
    .objectives-section {
        display: none;
        padding: 60px 0;
        background: #f8fafc;
    }
    
    .objectives-section.active {
        display: block;
    }"""
        
        new_css = """    /* Objectives Grid (Always visible) */
    .objectives-section {
        display: block;
        padding: 60px 0;
        background: #f8fafc;
    }"""
        
        if old_css in content:
            content = content.replace(old_css, new_css)
            print("✅ Updated CSS to show objectives by default")
        else:
            print("⚠️ CSS pattern not found, trying alternative approach...")
            # Alternative approach - just change display: none to display: block
            content = content.replace('display: none;', 'display: block;')
            print("✅ Changed display: none to display: block")
        
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
    print("🚀 Showing Full Board - Making All Objectives Visible")
    print("="*60)
    
    success = fix_objective_selector()
    
    if success:
        print("\n✅ SUCCESS! Your full board is now visible!")
        print("\n📋 Available Dashboards:")
        print("   • Main Selector: http://localhost:8000/")
        print("   • Objective 1: http://localhost:8000/objective1/")
        print("   • Objective 2: http://localhost:8000/objective2/")
        print("   • Objective 3: http://localhost:8000/objective3/")
        print("   • Objective 4: http://localhost:8000/objective4/")
        print("   • Objective 5: http://localhost:8000/objective5/")
        print("   • Objective 6: http://localhost:8000/objective6/")
        print("   • Objective 7: http://localhost:8000/objective7/")
        print("   • Objective 8: http://localhost:8000/objective8/ (Admin)")
        print("   • Full Analysis: http://localhost:8000/full-analysis/")
        print("   • ML Comparison: http://localhost:8000/comprehensive-comparison/")
        print("\n🔄 Refresh your browser to see all objectives!")
    else:
        print("\n❌ Failed to update the board. Please check the file manually.")

if __name__ == "__main__":
    main()