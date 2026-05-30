#!/usr/bin/env python3
"""
Final cleanup of the dashboard to remove any leftover unified search code
"""

import os

def clean_dashboard_final():
    """Remove any leftover unified search code"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🧹 Final cleanup of dashboard...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove any leftover unified search elements
        lines = content.split('\n')
        cleaned_lines = []
        skip_section = False
        
        for i, line in enumerate(lines):
            # Skip leftover unified search sections
            if 'border-radius: 25px' in line and 'padding: 15px 20px' in line:
                skip_section = True
                continue
            elif skip_section and '</div>' in line:
                skip_section = False
                continue
            elif skip_section:
                continue
            
            cleaned_lines.append(line)
        
        # Join lines back
        content = '\n'.join(cleaned_lines)
        
        # Remove any duplicate sections or leftover code
        content = content.replace('                    </div>\n                </div>\n                \n                <!-- Analyze Button -->', '')
        
        # Write cleaned content back
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Final cleanup completed!")
        return True
        
    except Exception as e:
        print(f"❌ Error in final cleanup: {e}")
        return False

def main():
    """Main function"""
    print("🧹 FINAL DASHBOARD CLEANUP")
    print("=" * 40)
    
    success = clean_dashboard_final()
    
    if success:
        print("\n✅ DASHBOARD FULLY RESTORED!")
        print("=" * 40)
        print("\n🎯 Clean Original Layout:")
        print("   ┌─────────────────┬─────────────────┬─────────────┐")
        print("   │ [Search Input]  │ [Country Drop]  │  [Analyze]  │")
        print("   └─────────────────┴─────────────────┴─────────────┘")
        
        print("\n🚀 Ready to test!")
        
    else:
        print("\n❌ Cleanup failed.")

if __name__ == "__main__":
    main()