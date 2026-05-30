#!/usr/bin/env python3
"""
Restore the original dashboard with separate search input and dropdown
"""

import os

def restore_original_dashboard():
    """Restore the dashboard to its original state"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔄 Restoring original dashboard...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the search section with original layout
        search_start = content.find('<!-- Search Section -->')
        if search_start != -1:
            search_end = content.find('</div>', content.find('</div>', search_start) + 1) + 6
            
            # Original search section with 3 columns
            original_search = '''<!-- Search Section -->
        <div class="search-section">
            <h3><i class="fas fa-globe"></i> Country Energy Analysis</h3>
            
            <div class="row">
                <!-- Search Input Column -->
                <div class="col-md-5">
                    <label for="countryInput" class="form-label">
                        <i class="fas fa-search"></i> Search Country
                    </label>
                    <input type="text" id="countryInput" class="form-control" 
                           placeholder="Type country name..." 
                           autocomplete="off"
                           style="border-radius: 8px; padding: 12px;">
                    <div id="searchSuggestions" class="search-suggestions"></div>
                </div>
                
                <!-- Dropdown Column -->
                <div class="col-md-5">
                    <label for="countrySelect" class="form-label">
                        <i class="fas fa-list"></i> Select Country
                    </label>
                    <select id="countrySelect" class="form-select" 
                            style="border-radius: 8px; padding: 12px;">
                        <option value="">-- Choose a Country --</option>
                    </select>
                </div>
                
                <!-- Button Column -->
                <div class="col-md-2">
                    <label class="form-label" style="opacity: 0;">Button</label>
                    <button class="btn btn-primary w-100" onclick="analyzeSelectedCountry()" 
                            style="border-radius: 8px; padding: 12px;">
                        <i class="fas fa-search"></i> Analyze
                    </button>
                </div>
            </div>
        </div>'''
            
            # Replace the search section
            content = content[:search_start] + original_search + content[search_end:]
            print("✅ Restored original 3-column search layout")
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully restored original dashboard!")
        return True
        
    except Exception as e:
        print(f"❌ Error restoring dashboard: {e}")
        return False

def main():
    """Main function"""
    print("🔄 RESTORING ORIGINAL DASHBOARD")
    print("=" * 50)
    
    success = restore_original_dashboard()
    
    if success:
        print("\n✅ ORIGINAL DASHBOARD RESTORED!")
        print("=" * 50)
        print("\n🎯 Dashboard Features:")
        print("   ✅ Search input field (left column)")
        print("   ✅ Country dropdown (middle column)")  
        print("   ✅ Analyze button (right column)")
        print("   ✅ Original 3-column layout")
        
        print("\n🚀 Ready to Use:")
        print("   1. Refresh browser (Ctrl+F5)")
        print("   2. See original layout restored")
        print("   3. Test both search methods")
        
    else:
        print("\n❌ Restoration failed.")

if __name__ == "__main__":
    main()