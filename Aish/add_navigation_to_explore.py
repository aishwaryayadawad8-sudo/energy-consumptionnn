#!/usr/bin/env python3
"""
Script to add navigation from Explore Dashboard back to objectives
"""

import os

def add_navigation_to_explore():
    """Add navigation button to go back to objectives from explore dashboard"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    if not os.path.exists(index_path):
        print(f"❌ File not found: {index_path}")
        return False
    
    try:
        # Read the index file
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add navigation button after the header section
        navigation_html = '''        
        <!-- Navigation to Objectives -->
        <div class="header-section">
            <div class="d-flex justify-content-between align-items-center">
                <div>
                    <h3><i class="fas fa-compass"></i> Navigation</h3>
                    <p>Explore country-specific energy data or view all objectives</p>
                </div>
                <div>
                    <a href="/objectives/" class="btn btn-primary btn-lg">
                        <i class="fas fa-bullseye"></i> View All Objectives
                    </a>
                </div>
            </div>
        </div>
        '''
        
        # Find where to insert the navigation (after the first header-section)
        header_end = content.find('</div>\n        \n        <!-- Project Objectives -->')
        
        if header_end != -1:
            # Insert navigation after the first header section
            content = content[:header_end + 6] + navigation_html + content[header_end + 6:]
            print("✅ Added navigation to objectives from explore dashboard")
        else:
            # Alternative insertion point
            search_section_start = content.find('<!-- Search Section -->')
            if search_section_start != -1:
                content = content[:search_section_start] + navigation_html + '\n        ' + content[search_section_start:]
                print("✅ Added navigation (alternative position)")
        
        # Write the file back
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully updated {index_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating index.html: {e}")
        return False

def main():
    """Main function"""
    print("🧭 Adding Navigation to Explore Dashboard")
    print("="*50)
    
    success = add_navigation_to_explore()
    
    if success:
        print("\n✅ SUCCESS! Navigation added!")
        print("   • Users can now easily navigate from Explore Dashboard to Objectives")
        print("   • Added 'View All Objectives' button")
    else:
        print("\n❌ Failed to add navigation.")

if __name__ == "__main__":
    main()