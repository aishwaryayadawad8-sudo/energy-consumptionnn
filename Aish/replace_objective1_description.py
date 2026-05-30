#!/usr/bin/env python3
"""
Replace Objective 1 description with the new provided text
"""

def replace_objective1_description():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Replacing Objective 1 description...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the current description and replace it
        old_description = '''                            <p style="text-align: left; margin-top: 15px; line-height: 1.6; color: #2c3e50; font-size: 1rem;">
                                This studies how energy is used around the world by looking at past information and uses it to understand how energy needs may change in the future for different countries. It helps show usage patterns and gives useful insights that support better planning and responsible energy use.
                            </p>'''
        
        new_description = '''                            <p style="text-align: left; margin-top: 15px; line-height: 1.6; color: #2c3e50; font-size: 1rem;">
                                It helps people understand how much energy different countries use, how this changes over time, and how much energy they may need in the future. This makes it easier to plan for energy use, avoid shortages, and support a cleaner and more sustainable environment.
                            </p>'''
        
        if old_description in content:
            content = content.replace(old_description, new_description)
            print("✅ Found and replaced Objective 1 description")
        else:
            # Try to find just the text part
            old_text = "This studies how energy is used around the world by looking at past information and uses it to understand how energy needs may change in the future for different countries. It helps show usage patterns and gives useful insights that support better planning and responsible energy use."
            new_text = "It helps people understand how much energy different countries use, how this changes over time, and how much energy they may need in the future. This makes it easier to plan for energy use, avoid shortages, and support a cleaner and more sustainable environment."
            
            if old_text in content:
                content = content.replace(old_text, new_text)
                print("✅ Found and replaced Objective 1 description text")
            else:
                print("❌ Could not find the current description to replace")
                return False
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Objective 1 description replaced successfully!")
        print("📝 New description:")
        print("   'It helps people understand how much energy different countries use,")
        print("    how this changes over time, and how much energy they may need in")
        print("    the future. This makes it easier to plan for energy use, avoid")
        print("    shortages, and support a cleaner and more sustainable environment.'")
        print("🔄 Please refresh your browser to see the updated description")
        
        return True
        
    except Exception as e:
        print(f"❌ Error replacing Objective 1 description: {e}")
        return False

if __name__ == "__main__":
    replace_objective1_description()