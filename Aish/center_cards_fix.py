"""
Center-align the remaining two metric cards in the dashboard
"""

def center_align_cards():
    # Read the index.html file with proper encoding
    with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Find and replace the row with centered cards
    old_row = '                <div class="row">\n                    <div class="col-md-3">'
    new_row = '                <div class="row justify-content-center">\n                    <div class="col-md-4 col-lg-3">'
    
    # Replace first occurrence (the metric cards row)
    if old_row in content:
        # Find the position
        pos = content.find(old_row)
        # Replace only this occurrence
        content = content[:pos] + new_row + content[pos + len(old_row):]
        
        # Now replace the second col-md-3 in the same row
        # Find the next col-md-3 after our replacement
        next_pos = content.find('<div class="col-md-3">', pos + len(new_row))
        if next_pos != -1 and next_pos < pos + 500:  # Make sure it's in the same section
            content = content[:next_pos] + '<div class="col-md-4 col-lg-3">' + content[next_pos + len('<div class="col-md-3">'):]
        
        # Also fix the duplicate gradient issue
        content = content.replace(
            'style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">4facfe 0%, #00f2fe 100%);">',
            'style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">'
        )
        
        # Write back
        with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully centered the metric cards!")
        print("📊 The two cards are now center-aligned with responsive sizing")
        print("🔧 Also fixed the duplicate gradient style issue")
        return True
    else:
        print("❌ Could not find the metric cards row")
        return False

if __name__ == '__main__':
    center_align_cards()
