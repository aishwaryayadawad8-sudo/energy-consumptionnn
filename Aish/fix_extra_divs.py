#!/usr/bin/env python3
"""
Fix extra closing div tags in the objectives section
"""

def fix_extra_divs():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Fixing extra closing div tags...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix the pattern where we have extra </div> tags
        # Replace patterns like:
        # </div>
        # </div>
        # with just:
        # </div>
        
        import re
        
        # Remove double closing divs that were created during the content area removal
        content = re.sub(r'</div>\s*</div>\s*</div>', '</div>', content)
        content = re.sub(r'</div>\s*</div>', '</div>', content)
        
        # Specifically fix the objective card structure
        old_pattern = '''                        </a>
                    </div>
                </div>
                </div>'''
        
        new_pattern = '''                        </a>
                    </div>
                </div>'''
        
        content = content.replace(old_pattern, new_pattern)
        
        print("✅ Fixed extra closing div tags")
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Template structure cleaned up!")
        print("🔄 Please refresh your browser to see the corrected layout")
        
        return True
        
    except Exception as e:
        print(f"❌ Error fixing div tags: {e}")
        return False

if __name__ == "__main__":
    fix_extra_divs()