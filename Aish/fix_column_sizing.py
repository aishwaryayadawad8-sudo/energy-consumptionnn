"""
Fix the column sizing for the second metric card
"""

def fix_columns():
    # Read the index.html file
    with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Fix the second card's column class
    content = content.replace(
        '                    <div class="col-md-3">\n                        <div class="metric-card" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);">',
        '                    <div class="col-md-4 col-lg-3">\n                        <div class="metric-card" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);">'
    )
    
    # Write back
    with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Fixed column sizing for both metric cards")
    print("📊 Both cards now use col-md-4 col-lg-3 for proper centering")

if __name__ == '__main__':
    fix_columns()
