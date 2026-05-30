#!/usr/bin/env python3
"""
Fix the objective card structure properly
"""

def fix_objective_structure():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Fixing objective card structure...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix each objective card structure
        # Pattern: missing closing </div> for objective-info and objective-card
        
        # Fix Objective 5
        old_obj5 = '''                        </a>
                    </div>
                
                <!-- Objective 6: Policy Analysis -->'''
        
        new_obj5 = '''                        </a>
                    </div>
                </div>
                
                <!-- Objective 6: Policy Analysis -->'''
        
        content = content.replace(old_obj5, new_obj5)
        
        # Fix Objective 6
        old_obj6 = '''                        </a>
                    </div>
                
                <!-- Objective 7: Investment Strategy -->'''
        
        new_obj6 = '''                        </a>
                    </div>
                </div>
                
                <!-- Objective 7: Investment Strategy -->'''
        
        content = content.replace(old_obj6, new_obj6)
        
        # Fix Objective 7
        old_obj7 = '''                        </a>
                    </div>
                
                <!-- Objective 8: Sustainable Investment Strategy Support -->'''
        
        new_obj7 = '''                        </a>
                    </div>
                </div>
                
                <!-- Objective 8: Sustainable Investment Strategy Support -->'''
        
        content = content.replace(old_obj7, new_obj7)
        
        # Fix Objective 8 (last one)
        old_obj8 = '''                        </a>
                    </div>
        </div>'''
        
        new_obj8 = '''                        </a>
                    </div>
                </div>
            </div>
        </div>'''
        
        content = content.replace(old_obj8, new_obj8)
        
        # Also fix missing closing div for objective-header in objectives 5-8
        # Fix missing </div> after objective-number
        content = content.replace('''                            <div class="objective-number">05</div>
                        <h3 class="objective-title">''', '''                            <div class="objective-number">05</div>
                        </div>
                        <h3 class="objective-title">''')
        
        content = content.replace('''                            <div class="objective-number">06</div>
                        <h3 class="objective-title">''', '''                            <div class="objective-number">06</div>
                        </div>
                        <h3 class="objective-title">''')
        
        content = content.replace('''                            <div class="objective-number">07</div>
                        <h3 class="objective-title">''', '''                            <div class="objective-number">07</div>
                        </div>
                        <h3 class="objective-title">''')
        
        content = content.replace('''                            <div class="objective-number">08</div>
                        <h3 class="objective-title">''', '''                            <div class="objective-number">08</div>
                        </div>
                        <h3 class="objective-title">''')
        
        print("✅ Fixed objective card structure")
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Objective structure fixed!")
        print("🔄 Please refresh your browser to see the corrected layout")
        
        return True
        
    except Exception as e:
        print(f"❌ Error fixing objective structure: {e}")
        return False

if __name__ == "__main__":
    fix_objective_structure()