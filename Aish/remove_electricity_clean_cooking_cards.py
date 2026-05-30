"""
Remove Electricity Access and Clean Cooking metric cards from the full dashboard
"""

def remove_metric_cards():
    # Read the index.html file
    with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and remove the Electricity Access and Clean Cooking cards section
    # These are the first two metric cards in the row
    start_marker = '                <div class="row">\n                    <div class="col-md-3">\n                        <div class="metric-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">\n                            <h4><i class="fas fa-plug"></i> Electricity Access</h4>'
    
    end_marker = '                    </div>\n                    <div class="col-md-3">\n                        <div class="metric-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">'
    
    if start_marker in content and end_marker in content:
        # Find the positions
        start_pos = content.find(start_marker)
        end_pos = content.find(end_marker)
        
        if start_pos != -1 and end_pos != -1:
            # Remove the two cards but keep the row and the remaining cards
            # We need to keep the row opening and adjust the remaining cards
            before = content[:start_pos]
            after = content[end_pos:]
            
            # Add back the row opening
            new_content = before + '                <div class="row">\n                    <div class="col-md-3">\n                        <div class="metric-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">' + after[len('                    <div class="col-md-3">\n                        <div class="metric-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">'):]
            
            # Write back
            with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ Successfully removed Electricity Access and Clean Cooking metric cards!")
            print("📊 Remaining cards: Renewable Share and CO₂ Emissions")
            return True
    
    print("❌ Could not find the metric cards to remove")
    return False

if __name__ == '__main__':
    remove_metric_cards()
