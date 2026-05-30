#!/usr/bin/env python3
"""
Fix Auto-Scroll Behavior
========================

This script removes the automatic scrolling that happens when clicking "Analyze Country".
The page should stay at the current position until the user manually scrolls down.
"""

import os

def fix_auto_scroll_behavior():
    """Remove automatic scrolling when analyzing country"""
    
    html_file_path = "Aish/sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔧 Fixing auto-scroll behavior...")
    print(f"📁 Updating file: {html_file_path}")
    
    # Read the current file
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False
    
    # Find and remove auto-scroll code
    changes_made = 0
    
    # 1. Remove scrollIntoView calls
    scroll_patterns = [
        # Pattern 1: scrollIntoView in showCountryProfile
        {
            'old': '''            // Scroll to show the profile section
            setTimeout(() => {
                document.getElementById('countryProfileSection').scrollIntoView({
                    behavior: 'smooth',
                    block: 'nearest'
                });
            }, 2000);''',
            'new': '''            // Profile section shown but no auto-scroll
            // User can manually scroll to see the profile section'''
        },
        # Pattern 2: Any other scrollIntoView calls
        {
            'old': '''.scrollIntoView({
                    behavior: 'smooth',
                    block: 'nearest'
                })''',
            'new': '''// Auto-scroll removed - user controls scrolling'''
        },
        # Pattern 3: scrollIntoView with different parameters
        {
            'old': '''.scrollIntoView({
                behavior: 'smooth',
                block: 'nearest'
            })''',
            'new': '''// Auto-scroll removed - user controls scrolling'''
        },
        # Pattern 4: Simple scrollIntoView calls
        {
            'old': '.scrollIntoView()',
            'new': '// Auto-scroll removed'
        }
    ]
    
    for pattern in scroll_patterns:
        if pattern['old'] in content:
            content = content.replace(pattern['old'], pattern['new'])
            changes_made += 1
            print(f"✅ Removed auto-scroll pattern {changes_made}")
    
    # 2. Find and modify the showCountryProfile function to not auto-scroll
    show_profile_start = "function showCountryProfile(countryName, coords) {"
    show_profile_pos = content.find(show_profile_start)
    
    if show_profile_pos != -1:
        # Find the end of the function
        brace_count = 0
        pos = show_profile_pos + len(show_profile_start)
        start_pos = pos
        
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
        
        # Extract the function content
        old_function = content[show_profile_pos:end_pos]
        
        # Create new function without auto-scroll
        new_function = '''function showCountryProfile(countryName, coords) {
            // Show the bottom country profile section (no auto-scroll)
            const profileSection = document.getElementById('countryProfileSection');
            if (!profileSection) {
                // Create the profile section if it doesn't exist
                createCountryProfileSection();
            }
            
            // Update profile content
            document.getElementById('profileCountryName').textContent = countryName;
            document.getElementById('profileYear').textContent = '2020';
            document.getElementById('countryProfileSection').style.display = 'block';
            
            // No auto-scroll - user can manually scroll to see the profile
            console.log(`✅ Country profile shown for ${countryName} (no auto-scroll)`);
        }'''
        
        content = content[:show_profile_pos] + new_function + content[end_pos:]
        changes_made += 1
        print("✅ Updated showCountryProfile function to remove auto-scroll")
    
    # 3. Remove any other automatic scrolling in the searchCountry function
    search_country_patterns = [
        # Remove any scroll-related code in searchCountry
        {
            'old': '''document.getElementById('resultSection').scrollIntoView''',
            'new': '''// Auto-scroll removed from resultSection'''
        },
        {
            'old': '''window.scrollTo(''',
            'new': '''// window.scrollTo removed - no auto-scroll ('''
        }
    ]
    
    for pattern in search_country_patterns:
        if pattern['old'] in content:
            # Find the complete line and comment it out
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if pattern['old'] in line:
                    lines[i] = '            // ' + line.strip() + ' // Auto-scroll removed'
                    changes_made += 1
                    print(f"✅ Commented out auto-scroll line: {line.strip()[:50]}...")
            content = '\n'.join(lines)
    
    # 4. Ensure results section shows without scrolling
    display_results_start = "function displayResults(countryData, predictions, energyMix) {"
    display_results_pos = content.find(display_results_start)
    
    if display_results_pos != -1:
        # Make sure the results section shows but doesn't auto-scroll
        results_section_show = "document.getElementById('resultSection').style.display = 'block';"
        if results_section_show in content:
            # Add a comment after it
            content = content.replace(
                results_section_show,
                results_section_show + "\n            // Results shown at current position - no auto-scroll"
            )
            print("✅ Added no-scroll comment to results section")
    
    # Write the updated content back to the file
    try:
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Successfully updated index.html ({changes_made} changes made)")
        return True
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False

def add_user_scroll_indicator():
    """Add a subtle indicator that results are available below"""
    
    html_file_path = "Aish/sustainable_energy/dashboard/templates/dashboard/index.html"
    
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False
    
    # Add CSS for a subtle scroll indicator
    scroll_indicator_css = '''
        /* Subtle scroll indicator */
        .scroll-indicator {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
            color: white;
            padding: 12px 20px;
            border-radius: 25px;
            box-shadow: 0 4px 16px rgba(59, 130, 246, 0.3);
            cursor: pointer;
            display: none;
            z-index: 1000;
            font-size: 0.9rem;
            font-weight: 600;
            animation: pulse-glow 2s infinite;
        }
        
        .scroll-indicator:hover {
            background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(59, 130, 246, 0.5);
        }
        
        @keyframes pulse-glow {
            0%, 100% { 
                box-shadow: 0 4px 16px rgba(59, 130, 246, 0.3);
            }
            50% { 
                box-shadow: 0 4px 20px rgba(59, 130, 246, 0.6);
            }
        }'''
    
    # Find the CSS section and add the indicator styles
    css_end_marker = "</style>"
    css_position = content.rfind(css_end_marker)
    if css_position != -1:
        content = content[:css_position] + scroll_indicator_css + "\n        " + content[css_position:]
    
    # Add the scroll indicator HTML
    scroll_indicator_html = '''
        <!-- Scroll Indicator (appears when results are ready) -->
        <div id="scrollIndicator" class="scroll-indicator" onclick="scrollToResults()">
            <i class="fas fa-arrow-down"></i> View Analysis Results
        </div>'''
    
    # Add before the closing body tag
    body_end = "</body>"
    body_position = content.rfind(body_end)
    if body_position != -1:
        content = content[:body_position] + scroll_indicator_html + "\n    " + content[body_position:]
    
    # Add JavaScript function to show/hide indicator and handle scroll
    scroll_js = '''
        
        function showScrollIndicator() {
            // Show the scroll indicator when results are ready
            const indicator = document.getElementById('scrollIndicator');
            if (indicator) {
                indicator.style.display = 'block';
                
                // Hide after 5 seconds
                setTimeout(() => {
                    indicator.style.display = 'none';
                }, 5000);
            }
        }
        
        function scrollToResults() {
            // Smooth scroll to results when user clicks the indicator
            const resultsSection = document.getElementById('resultSection');
            if (resultsSection) {
                resultsSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
            
            // Hide the indicator
            document.getElementById('scrollIndicator').style.display = 'none';
        }'''
    
    # Add the JavaScript before the closing script tag
    script_end = "</script>"
    script_position = content.rfind(script_end)
    if script_position != -1:
        content = content[:script_position] + scroll_js + "\n    " + content[script_position:]
    
    # Update displayResults function to show the indicator
    display_results_show = "document.getElementById('resultSection').style.display = 'block';"
    if display_results_show in content:
        content = content.replace(
            display_results_show,
            display_results_show + "\n            \n            // Show scroll indicator to let user know results are ready\n            showScrollIndicator();"
        )
    
    try:
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Added subtle scroll indicator for user convenience")
        return True
    except Exception as e:
        print(f"❌ Error adding scroll indicator: {e}")
        return False

def main():
    """Main function to fix auto-scroll behavior"""
    print("🔧 FIXING AUTO-SCROLL BEHAVIOR")
    print("=" * 60)
    
    # Step 1: Remove automatic scrolling
    scroll_fixed = fix_auto_scroll_behavior()
    
    # Step 2: Add optional scroll indicator
    indicator_added = add_user_scroll_indicator()
    
    if scroll_fixed:
        print("\n" + "=" * 60)
        print("✅ AUTO-SCROLL BEHAVIOR FIXED!")
        print("=" * 60)
        print("\n🎯 Changes made:")
        print("   ✓ Removed automatic scrolling when clicking 'Analyze Country'")
        print("   ✓ Page stays at current position after analysis")
        print("   ✓ Results appear without auto-scroll")
        print("   ✓ User has full control over scrolling")
        
        if indicator_added:
            print("   ✓ Added subtle scroll indicator for user convenience")
            print("   ✓ Indicator appears for 5 seconds when results are ready")
            print("   ✓ User can click indicator to scroll to results")
        
        print("\n🧪 To test:")
        print("   1. Start Django server: python manage.py runserver")
        print("   2. Go to: http://127.0.0.1:8000/explore/")
        print("   3. Search for any country and click 'Analyze Country'")
        print("   4. Page should NOT scroll automatically")
        print("   5. Results appear at the bottom (scroll down to see them)")
        print("   6. Optional: Blue indicator appears bottom-right for 5 seconds")
        
        print("\n✅ User Experience:")
        print("   • No more automatic scrolling")
        print("   • User controls when to scroll down")
        print("   • Results are ready but don't force scroll")
        print("   • Subtle indicator shows results are available")
        
        print("\n🔄 Clear browser cache with Ctrl+F5 after testing")
    else:
        print("\n❌ FAILED TO FIX AUTO-SCROLL")
        print("Please check the error messages above")

if __name__ == "__main__":
    main()