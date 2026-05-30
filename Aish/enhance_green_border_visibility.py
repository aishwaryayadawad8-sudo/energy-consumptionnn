#!/usr/bin/env python3
"""
Script to make the green border more prominent and visible for country highlighting
"""

import os

def enhance_green_border_visibility():
    """Make the green border more prominent and visible"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🎯 Enhancing green border visibility...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the existing country highlight circle CSS
        old_css = '''        .country-highlight-circle {
            border: 3px solid #90EE90 !important;
            border-radius: 50% !important;
            background-color: rgba(144, 238, 144, 0.2) !important;
            box-shadow: 0 0 20px rgba(144, 238, 144, 0.6) !important;
            animation: pulseGreen 2s infinite !important;
        }'''
        
        # Enhanced CSS with more prominent green border
        new_css = '''        .country-highlight-circle {
            border: 5px solid #32CD32 !important;
            border-radius: 50% !important;
            background-color: rgba(50, 205, 50, 0.3) !important;
            box-shadow: 0 0 30px rgba(50, 205, 50, 0.8), 0 0 60px rgba(50, 205, 50, 0.4) !important;
            animation: pulseGreenStrong 2s infinite !important;
        }'''
        
        if old_css in content:
            content = content.replace(old_css, new_css)
            print("✅ Enhanced country highlight circle CSS")
        
        # Find and replace the existing pulse animation
        old_animation = '''        @keyframes pulseGreen {
            0% {
                box-shadow: 0 0 20px rgba(144, 238, 144, 0.6);
                transform: scale(1);
            }
            50% {
                box-shadow: 0 0 30px rgba(144, 238, 144, 0.8);
                transform: scale(1.05);
            }
            100% {
                box-shadow: 0 0 20px rgba(144, 238, 144, 0.6);
                transform: scale(1);
            }
        }'''
        
        # Enhanced animation with stronger pulse effect
        new_animation = '''        @keyframes pulseGreenStrong {
            0% {
                box-shadow: 0 0 30px rgba(50, 205, 50, 0.8), 0 0 60px rgba(50, 205, 50, 0.4);
                transform: scale(1);
                border-width: 5px;
            }
            50% {
                box-shadow: 0 0 50px rgba(50, 205, 50, 1.0), 0 0 100px rgba(50, 205, 50, 0.6);
                transform: scale(1.08);
                border-width: 7px;
            }
            100% {
                box-shadow: 0 0 30px rgba(50, 205, 50, 0.8), 0 0 60px rgba(50, 205, 50, 0.4);
                transform: scale(1);
                border-width: 5px;
            }
        }'''
        
        if old_animation in content:
            content = content.replace(old_animation, new_animation)
            print("✅ Enhanced pulse animation")
        
        # Find and enhance the JavaScript highlighting function
        old_js_circle = '''            const highlightCircle = L.circle([coords.lat, coords.lng], {
                color: '#90EE90',
                fillColor: '#90EE90',
                fillOpacity: 0.2,
                radius: 200000, // 200km radius
                weight: 3,
                className: 'country-highlight-circle'
            }).addTo(map);'''
        
        # Enhanced JavaScript with stronger green colors
        new_js_circle = '''            const highlightCircle = L.circle([coords.lat, coords.lng], {
                color: '#32CD32',
                fillColor: '#32CD32',
                fillOpacity: 0.3,
                radius: 250000, // 250km radius for better visibility
                weight: 5,
                className: 'country-highlight-circle'
            }).addTo(map);'''
        
        if old_js_circle in content:
            content = content.replace(old_js_circle, new_js_circle)
            print("✅ Enhanced JavaScript circle properties")
        
        # Enhance the pin marker for better visibility
        old_pin = '''            const customIcon = L.divIcon({
                className: 'country-pin-marker',
                html: '<i class="fas fa-map-pin" style="color: #228B22; font-size: 16px; margin-top: 2px;"></i>',
                iconSize: [20, 20],
                iconAnchor: [10, 10]
            });'''
        
        new_pin = '''            const customIcon = L.divIcon({
                className: 'country-pin-marker',
                html: '<i class="fas fa-map-pin" style="color: #228B22; font-size: 20px; margin-top: 1px; text-shadow: 0 0 10px rgba(34, 139, 34, 0.8);"></i>',
                iconSize: [24, 24],
                iconAnchor: [12, 12]
            });'''
        
        if old_pin in content:
            content = content.replace(old_pin, new_pin)
            print("✅ Enhanced pin marker visibility")
        
        # Enhance pin marker CSS
        old_pin_css = '''        .country-pin-marker {
            background-color: #32CD32 !important;
            border: 2px solid #228B22 !important;
            border-radius: 50% !important;
            width: 20px !important;
            height: 20px !important;
            box-shadow: 0 0 15px rgba(50, 205, 50, 0.7) !important;
        }'''
        
        new_pin_css = '''        .country-pin-marker {
            background-color: #32CD32 !important;
            border: 3px solid #228B22 !important;
            border-radius: 50% !important;
            width: 24px !important;
            height: 24px !important;
            box-shadow: 0 0 20px rgba(50, 205, 50, 0.9), 0 0 40px rgba(50, 205, 50, 0.5) !important;
            animation: pinPulse 1.5s infinite !important;
        }'''
        
        if old_pin_css in content:
            content = content.replace(old_pin_css, new_pin_css)
            print("✅ Enhanced pin marker CSS")
        
        # Add pin pulse animation if not exists
        pin_animation = '''        
        @keyframes pinPulse {
            0% {
                box-shadow: 0 0 20px rgba(50, 205, 50, 0.9), 0 0 40px rgba(50, 205, 50, 0.5);
                transform: scale(1);
            }
            50% {
                box-shadow: 0 0 30px rgba(50, 205, 50, 1.0), 0 0 60px rgba(50, 205, 50, 0.7);
                transform: scale(1.1);
            }
            100% {
                box-shadow: 0 0 20px rgba(50, 205, 50, 0.9), 0 0 40px rgba(50, 205, 50, 0.5);
                transform: scale(1);
            }
        }'''
        
        # Add pin animation before closing style tag
        style_end = content.find('</style>')
        if style_end != -1 and '@keyframes pinPulse' not in content:
            content = content[:style_end] + pin_animation + '\n        ' + content[style_end:]
            print("✅ Added pin pulse animation")
        
        # Write the updated content back to file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully enhanced green border visibility")
        return True
        
    except Exception as e:
        print(f"❌ Error enhancing green border: {e}")
        return False

def main():
    """Main function"""
    print("🎯 ENHANCING GREEN BORDER VISIBILITY")
    print("=" * 50)
    print("   • Making green border more prominent")
    print("   • Stronger pulse animation")
    print("   • Enhanced pin marker visibility")
    print("   • Brighter green colors")
    print("=" * 50)
    
    success = enhance_green_border_visibility()
    
    if success:
        print("\n" + "=" * 50)
        print("✅ GREEN BORDER ENHANCED!")
        print("=" * 50)
        print("\n🎯 Enhancements:")
        print("   ✅ Stronger green border (5px instead of 3px)")
        print("   ✅ Brighter green color (#32CD32)")
        print("   ✅ Larger radius (250km instead of 200km)")
        print("   ✅ Enhanced pulse animation")
        print("   ✅ Bigger pin marker (24px instead of 20px)")
        print("   ✅ Pin marker pulse animation")
        print("   ✅ Stronger glow effects")
        
        print("\n🌟 Visual Improvements:")
        print("   • Border: 5px solid bright green")
        print("   • Fill: 30% opacity bright green")
        print("   • Glow: Double shadow effect")
        print("   • Animation: Stronger pulse with border width change")
        print("   • Pin: Larger with pulsing animation")
        
        print("\n🔄 Next Steps:")
        print("   1. Refresh your browser (Ctrl+F5)")
        print("   2. Search for a country")
        print("   3. See the enhanced bright green highlighting!")
        
    else:
        print("\n❌ Enhancement failed. Please check the error messages above.")

if __name__ == "__main__":
    main()