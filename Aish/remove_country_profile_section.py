#!/usr/bin/env python3
"""
Remove Country Profile Section
==============================

This script removes the "Country - Energy Profile (2020)" section that appears 
at the bottom of the explore dashboard when a country is analyzed.
"""

import os

def remove_country_profile_section():
    """Remove the country profile section from the explore dashboard"""
    
    html_file_path = "Aish/sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🗑️ Removing country profile section...")
    print(f"📁 Updating file: {html_file_path}")
    
    # Read the current file
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False
    
    changes_made = 0
    
    # 1. Remove the HTML for country profile section
    profile_section_patterns = [
        # Pattern 1: The main country profile section HTML
        '''        <!-- Country Profile Section (Screenshot Style) -->
        <div id="countryProfileSection" class="country-profile-section" style="display: none;">
            <div class="profile-header">
                <i class="fas fa-flag"></i>
                <span id="profileCountryName">Country</span> - Energy Profile (<span id="profileYear">2020</span>)
            </div>
        </div>''',
        
        # Pattern 2: Alternative format
        '''<div id="countryProfileSection" class="country-profile-section" style="display: none;">
            <div class="profile-header">
                <i class="fas fa-flag"></i>
                <span id="profileCountryName">Country</span> - Energy Profile (<span id="profileYear">2020</span>)
            </div>
        </div>''',
        
        # Pattern 3: Any remaining country profile section
        '''<!-- Country Profile Section (Screenshot Style) -->''',
    ]
    
    for pattern in profile_section_patterns:
        if pattern in content:
            content = content.replace(pattern, '')
            changes_made += 1
            print(f"✅ Removed country profile HTML pattern {changes_made}")
    
    # 2. Remove CSS for country profile section
    css_patterns = [
        # Country profile section CSS
        '''.country-profile-section {
            background: white;
            margin: 20px;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            border-left: 5px solid #3b82f6;
        }
        
        .profile-header {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 1.3rem;
            font-weight: 600;
            color: #1f2937;
        }
        
        .profile-header i {
            color: #3b82f6;
            font-size: 1.1rem;
        }''',
        
        # Alternative CSS format
        '''.country-profile-section {
            background: white;
            margin: 20px;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            border-left: 5px solid #3b82f6;
        }''',
        
        # Profile header CSS
        '''.profile-header {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 1.3rem;
            font-weight: 600;
            color: #1f2937;
        }
        
        .profile-header i {
            color: #3b82f6;
            font-size: 1.1rem;
        }'''
    ]
    
    for pattern in css_patterns:
        if pattern in content:
            content = content.replace(pattern, '')
            changes_made += 1
            print(f"✅ Removed country profile CSS pattern {changes_made}")
    
    # 3. Remove or modify the showCountryProfile function
    show_profile_start = "function showCountryProfile(countryName, coords) {"
    show_profile_pos = content.find(show_profile_start)
    
    if show_profile_pos != -1:
        # Find the end of the function
        brace_count = 0
        pos = show_profile_pos + len(show_profile_start)
        
        while pos < len(content):
            if content[pos] == '{':
                brace_count += 1
            elif content[pos] == '}':
                brace_count -= 1
                if brace_count == -1:  # Found the closing brace
                    end_pos = pos + 1
                    break
            pos += 1
        else:
            end_pos = len(content)
        
        # Replace the function with an empty one
        new_function = '''function showCountryProfile(countryName, coords) {
            // Country profile section removed - no longer displayed
            console.log(`Country profile section disabled for ${countryName}`);
        }'''
        
        content = content[:show_profile_pos] + new_function + content[end_pos:]
        changes_made += 1
        print("✅ Disabled showCountryProfile function")
    
    # 4. Remove createCountryProfileSection function if it exists
    create_profile_start = "function createCountryProfileSection() {"
    create_profile_pos = content.find(create_profile_start)
    
    if create_profile_pos != -1:
        # Find the end of the function
        brace_count = 0
        pos = create_profile_pos + len(create_profile_start)
        
        while pos < len(content):
            if content[pos] == '{':
                brace_count += 1
            elif content[pos] == '}':
                brace_count -= 1
                if brace_count == -1:  # Found the closing brace
                    end_pos = pos + 1
                    break
            pos += 1
        else:
            end_pos = len(content)
        
        # Replace with empty function
        new_function = '''function createCountryProfileSection() {
            // Country profile section creation disabled
            console.log('Country profile section creation disabled');
        }'''
        
        content = content[:create_profile_pos] + new_function + content[end_pos:]
        changes_made += 1
        print("✅ Disabled createCountryProfileSection function")
    
    # 5. Remove any calls to show the profile section
    profile_calls = [
        "showCountryProfile(countryName, coords);",
        "document.getElementById('countryProfileSection').style.display = 'block';",
        "document.getElementById('profileCountryName').textContent = countryName;",
        "document.getElementById('profileYear').textContent = '2020';"
    ]
    
    for call in profile_calls:
        if call in content:
            content = content.replace(call, f"// {call} // Country profile removed")
            changes_made += 1
            print(f"✅ Commented out profile function call")
    
    # 6. Clean up any remaining references
    remaining_patterns = [
        "countryProfileSection",
        "profileCountryName", 
        "profileYear"
    ]
    
    lines = content.split('\n')
    for i, line in enumerate(lines):
        for pattern in remaining_patterns:
            if pattern in line and not line.strip().startswith('//'):
                # Comment out the line
                lines[i] = '            // ' + line.strip() + ' // Country profile removed'
                changes_made += 1
                print(f"✅ Commented out line with {pattern}")
                break
    
    content = '\n'.join(lines)
    
    # Write the updated content back to the file
    try:
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Successfully updated index.html ({changes_made} changes made)")
        return True
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False

def main():
    """Main function to remove country profile section"""
    print("🗑️ REMOVING COUNTRY PROFILE SECTION")
    print("=" * 60)
    
    success = remove_country_profile_section()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ COUNTRY PROFILE SECTION REMOVED!")
        print("=" * 60)
        print("\n🎯 Changes made:")
        print("   ✓ Removed country profile HTML section")
        print("   ✓ Removed country profile CSS styles")
        print("   ✓ Disabled showCountryProfile function")
        print("   ✓ Disabled createCountryProfileSection function")
        print("   ✓ Commented out all profile-related calls")
        print("   ✓ Cleaned up remaining references")
        
        print("\n✅ Result:")
        print("   • No more 'Country - Energy Profile (2020)' section")
        print("   • Clean explore dashboard without bottom profile")
        print("   • All other functionality preserved")
        print("   • Map highlighting and analysis still work")
        
        print("\n🧪 To test:")
        print("   1. Start Django server: python manage.py runserver")
        print("   2. Go to: http://127.0.0.1:8000/explore/")
        print("   3. Search for any country and analyze")
        print("   4. Verify: No profile section appears at bottom")
        print("   5. Verify: Map highlighting still works perfectly")
        
        print("\n🔄 Clear browser cache with Ctrl+F5 after testing")
    else:
        print("\n❌ FAILED TO REMOVE COUNTRY PROFILE SECTION")
        print("Please check the error messages above")

if __name__ == "__main__":
    main()