#!/usr/bin/env python3
"""
Fix Objective 2 description in the template
"""

def fix_objective2_description():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Fixing Objective 2 description...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the incorrect description in Objective 2
        old_description = '''                            <p style="text-align: left; line-height: 1.6; color: #2c3e50; font-size: 1rem; margin: 0;">
                                It helps people understand how much energy different countries use, how this changes over time, and how much energy they may need in the future. This makes it easier to plan for energy use, avoid shortages, and support a cleaner and more sustainable environment.
                            </p>
                        </div>
                    </div>
                </div>
                
                <!-- Objective 3: Renewables -->'''
        
        new_description = '''                            <p style="text-align: left; line-height: 1.6; color: #2c3e50; font-size: 1rem; margin: 0;">
                                It helps people see how much carbon pollution is being released into the air, how it has changed over the years, and how it may change in the future. This supports better decisions to reduce pollution and protect the environment.
                            </p>
                        </div>
                    </div>
                </div>
                
                <!-- Objective 3: Renewables -->'''
        
        if old_description in content:
            content = content.replace(old_description, new_description)
            print("✅ Fixed Objective 2 description")
        else:
            print("⚠️  Could not find the exact pattern to replace")
            # Try a more specific pattern
            old_pattern = '''It helps people understand how much energy different countries use, how this changes over time, and how much energy they may need in the future. This makes it easier to plan for energy use, avoid shortages, and support a cleaner and more sustainable environment.'''
            new_pattern = '''It helps people see how much carbon pollution is being released into the air, how it has changed over the years, and how it may change in the future. This supports better decisions to reduce pollution and protect the environment.'''
            
            # Count occurrences to make sure we only replace the second one (Objective 2)
            occurrences = content.count(old_pattern)
            if occurrences >= 2:
                # Replace only the second occurrence (Objective 2)
                parts = content.split(old_pattern)
                if len(parts) >= 3:
                    # Rejoin with the first occurrence unchanged, second occurrence replaced
                    content = old_pattern.join(parts[:2]) + new_pattern + old_pattern.join(parts[2:])
                    print("✅ Fixed Objective 2 description (alternative method)")
                else:
                    print("❌ Could not fix Objective 2 description")
            else:
                print(f"❌ Found {occurrences} occurrences, expected at least 2")
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Objective 2 description updated!")
        print("📝 Updated content:")
        print("   🌍 Objective 2: Carbon pollution tracking and environmental protection")
        print("🔄 Please refresh your browser to see the updated description")
        
        return True
        
    except Exception as e:
        print(f"❌ Error fixing Objective 2 description: {e}")
        return False

if __name__ == "__main__":
    fix_objective2_description()