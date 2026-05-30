#!/usr/bin/env python3
"""
Fix background images for objectives in the new 4-column layout
"""

def fix_objective_background_images():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Fixing objective background images for 4-column layout...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # The current CSS selectors are based on :nth-child() which won't work correctly
        # in the new structure. We need to use more specific selectors.
        
        # Remove old background image CSS that uses nth-child selectors
        old_css_patterns = [
            r'\/\* Special background for Energy Consumption Prediction objective \*\/.*?\.objective-card:first-child \.objective-info \{.*?\}',
            r'\/\* Special background for CO Emission Forecasting objective \*\/.*?\.objective-card:nth-child\(2\) \.objective-info \{.*?\}',
            r'\/\* Special background for Energy Access Classification objective \*\/.*?\.objective-card:nth-child\(3\) \.objective-info \{.*?\}',
            r'\/\* Special background for SDG-7 Progress Monitoring objective \*\/.*?\.objective-card:nth-child\(4\) \.objective-info \{.*?\}',
            r'\/\* Special background for Energy Equity Analysis objective \*\/.*?\.objective-card:nth-child\(5\) \.objective-info \{.*?\}',
            r'\/\* Special background for Efficiency Optimization Identification objective \*\/.*?\.objective-card:nth-child\(6\) \.objective-info \{.*?\}',
            r'\/\* Special background for Renewable Energy Potential Assessment objective \*\/.*?\.objective-card:nth-child\(7\) \.objective-info \{.*?\}',
            r'\/\* Special background for Sustainable Investment Strategy Support objective \*\/.*?\.objective-card:nth-child\(8\) \.objective-info \{.*?\}'
        ]
        
        # Remove overlay CSS patterns too
        overlay_patterns = [
            r'\/\* Overlay for better text readability on background image \*\/.*?\.objective-card:first-child \.objective-info::before \{.*?\}',
            r'\/\* Overlay for CO₂ Emission Forecasting objective \*\/.*?\.objective-card:nth-child\(2\) \.objective-info::before \{.*?\}',
            r'\/\* Overlay for Energy Access Classification objective \*\/.*?\.objective-card:nth-child\(3\) \.objective-info::before \{.*?\}',
            r'\/\* Watermark overlay for SDG-7 Progress Monitoring objective \*\/.*?\.objective-card:nth-child\(4\) \.objective-info::before \{.*?\}',
            r'\/\* Watermark overlay for Energy Equity Analysis objective \*\/.*?\.objective-card:nth-child\(5\) \.objective-info::before \{.*?\}',
            r'\/\* Watermark overlay for Efficiency Optimization Identification objective \*\/.*?\.objective-card:nth-child\(6\) \.objective-info::before \{.*?\}',
            r'\/\* Overlay for better text readability on 7th objective background image \*\/.*?\.objective-card:nth-child\(7\) \.objective-info::before \{.*?\}',
            r'\/\* Overlay for better text readability on 8th objective background image \*\/.*?\.objective-card:nth-child\(8\) \.objective-info::before \{.*?\}'
        ]
        
        import re
        
        # Remove old CSS patterns
        for pattern in old_css_patterns + overlay_patterns:
            content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        print("✅ Removed old background image CSS")
        
        # Add new CSS with specific class-based selectors
        new_background_css = '''
        /* Objective Background Images - Using specific selectors for 4-column layout */
        
        /* Objective 1: Energy Consumption Prediction */
        .objective-card[data-objective="1"] .objective-info {
            background-image: url('/static/images/energy-consumption-prediction.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            border-radius: 8px;
            padding: 20px;
            position: relative;
        }
        
        .objective-card[data-objective="1"] .objective-info::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(255, 255, 255, 0.4);
            border-radius: 8px;
            z-index: 1;
        }
        
        /* Objective 2: CO₂ Emission Forecasting */
        .objective-card[data-objective="2"] .objective-info {
            background-image: url('/static/images/co2-emission.webp');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            border-radius: 8px;
            padding: 20px;
            position: relative;
        }
        
        .objective-card[data-objective="2"] .objective-info::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(255, 255, 255, 0.4);
            border-radius: 8px;
            z-index: 1;
        }
        
        /* Objective 3: Energy Access Classification */
        .objective-card[data-objective="3"] .objective-info {
            background-image: url('/static/images/energy-access-classification.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            border-radius: 8px;
            padding: 20px;
            position: relative;
        }
        
        .objective-card[data-objective="3"] .objective-info::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(255, 255, 255, 0.4);
            border-radius: 8px;
            z-index: 1;
        }
        
        /* Objective 4: SDG-7 Progress Monitoring */
        .objective-card[data-objective="4"] .objective-info {
            background-image: url('/static/images/sdg7-progress-monitoring.webp');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            border-radius: 8px;
            padding: 20px;
            position: relative;
        }
        
        .objective-card[data-objective="4"] .objective-info::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(255, 255, 255, 0.7);
            border-radius: 8px;
            z-index: 1;
        }
        
        /* Objective 5: Energy Equity Analysis */
        .objective-card[data-objective="5"] .objective-info {
            background-image: url('/static/images/energy-equity-analysis.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            border-radius: 8px;
            padding: 20px;
            position: relative;
        }
        
        .objective-card[data-objective="5"] .objective-info::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 8px;
            z-index: 1;
        }
        
        /* Objective 6: Efficiency Optimization Identification */
        .objective-card[data-objective="6"] .objective-info {
            background-image: url('/static/images/efficiency-optimization-identification.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            border-radius: 8px;
            padding: 20px;
            position: relative;
        }
        
        .objective-card[data-objective="6"] .objective-info::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 8px;
            z-index: 1;
        }
        
        /* Objective 7: Renewable Energy Potential Assessment */
        .objective-card[data-objective="7"] .objective-info {
            background-image: url('/static/images/renewable-energy-potential-assessment.webp');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            border-radius: 8px;
            padding: 20px;
            position: relative;
        }
        
        .objective-card[data-objective="7"] .objective-info::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(255, 255, 255, 0.4);
            border-radius: 8px;
            z-index: 1;
        }
        
        /* Objective 8: Sustainable Investment Strategy Support */
        .objective-card[data-objective="8"] .objective-info {
            background-image: url('/static/images/sustainable-investment-strategy-support.png');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            border-radius: 8px;
            padding: 20px;
            position: relative;
        }
        
        .objective-card[data-objective="8"] .objective-info::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(255, 255, 255, 0.4);
            border-radius: 8px;
            z-index: 1;
        }
        
        /* Ensure content appears above overlay with better contrast */
        .objective-card .objective-info > * {
            position: relative;
            z-index: 2;
        }
        
        /* Apply text visibility styling to all objectives */
        .objective-card .objective-title {
            color: #1f2937;
            font-weight: 700;
            text-shadow: 2px 2px 4px rgba(255, 255, 255, 1), 
                         -1px -1px 2px rgba(255, 255, 255, 1),
                         1px -1px 2px rgba(255, 255, 255, 1),
                         -1px 1px 2px rgba(255, 255, 255, 1);
        }
        
        .objective-card .objective-description {
            color: #374151;
            font-weight: 600;
            text-shadow: 2px 2px 4px rgba(255, 255, 255, 1), 
                         -1px -1px 2px rgba(255, 255, 255, 1),
                         1px -1px 2px rgba(255, 255, 255, 1),
                         -1px 1px 2px rgba(255, 255, 255, 1);
        }
        
        .objective-card .objective-number {
            color: #f97316;
            font-weight: 700;
            text-shadow: 2px 2px 4px rgba(255, 255, 255, 1), 
                         -1px -1px 2px rgba(255, 255, 255, 1),
                         1px -1px 2px rgba(255, 255, 255, 1),
                         -1px 1px 2px rgba(255, 255, 255, 1);
        }
        '''
        
        # Find where to insert the new CSS (before the closing </style> tag)
        style_end = content.find('</style>')
        if style_end != -1:
            content = content[:style_end] + new_background_css + '\n        ' + content[style_end:]
            print("✅ Added new background image CSS")
        
        # Now update the HTML to add data-objective attributes
        html_updates = [
            ('<!-- Objective 1: Energy Consumption Prediction -->\n                    <div class="objective-card">',
             '<!-- Objective 1: Energy Consumption Prediction -->\n                    <div class="objective-card" data-objective="1">'),
            ('<!-- Objective 2: CO₂ Emission Forecasting -->\n                    <div class="objective-card">',
             '<!-- Objective 2: CO₂ Emission Forecasting -->\n                    <div class="objective-card" data-objective="2">'),
            ('<!-- Objective 3: Energy Access Classification -->\n                    <div class="objective-card">',
             '<!-- Objective 3: Energy Access Classification -->\n                    <div class="objective-card" data-objective="3">'),
            ('<!-- Objective 4: SDG-7 Progress Monitoring -->\n                    <div class="objective-card">',
             '<!-- Objective 4: SDG-7 Progress Monitoring -->\n                    <div class="objective-card" data-objective="4">'),
            ('<!-- Objective 5: Energy Equity Analysis -->\n                    <div class="objective-card">',
             '<!-- Objective 5: Energy Equity Analysis -->\n                    <div class="objective-card" data-objective="5">'),
            ('<!-- Objective 6: Efficiency Optimization Identification -->\n                    <div class="objective-card">',
             '<!-- Objective 6: Efficiency Optimization Identification -->\n                    <div class="objective-card" data-objective="6">'),
            ('<!-- Objective 7: Renewable Energy Potential Assessment -->\n                    <div class="objective-card">',
             '<!-- Objective 7: Renewable Energy Potential Assessment -->\n                    <div class="objective-card" data-objective="7">'),
            ('<!-- Objective 8: Sustainable Investment Strategy Support -->\n                    <div class="objective-card">',
             '<!-- Objective 8: Sustainable Investment Strategy Support -->\n                    <div class="objective-card" data-objective="8">')
        ]
        
        for old_html, new_html in html_updates:
            content = content.replace(old_html, new_html)
        
        print("✅ Added data-objective attributes to HTML")
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Background images fixed successfully!")
        print("📝 Each objective now has its unique background image:")
        print("   📊 Objective 1: Energy Consumption Prediction image")
        print("   🌍 Objective 2: CO₂ Emission image")
        print("   👥 Objective 3: Energy Access Classification image")
        print("   🎯 Objective 4: SDG-7 Progress Monitoring image")
        print("   ⚖️  Objective 5: Energy Equity Analysis image")
        print("   ⚡ Objective 6: Efficiency Optimization image")
        print("   🌱 Objective 7: Renewable Energy Potential image")
        print("   💰 Objective 8: Investment Strategy image")
        print("🔄 Please refresh your browser to see the unique background images")
        
        return True
        
    except Exception as e:
        print(f"❌ Error fixing background images: {e}")
        return False

if __name__ == "__main__":
    fix_objective_background_images()