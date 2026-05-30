"""
Center-align the remaining two metric cards in the dashboard
"""

def center_align_cards():
    # Read the index.html file
    with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the row with the two remaining cards and change col-md-3 to col-md-6 with offset
    # This will make them centered
    old_pattern = '''                <div class="row">
                    <div class="col-md-3">
                        <div class="metric-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
                            <h4><i class="fas fa-leaf"></i> Renewable Share</h4>
                            <div class="value" id="renewableShare">-</div>
                            <div class="unit">%</div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="metric-card" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);">
                            <h4><i class="fas fa-smog"></i> CO₂ Emissions</h4>
                            <div class="value" id="co2Emissions">-</div>
                            <div class="unit">kt</div>
                        </div>
                    </div>
                </div>'''
    
    new_pattern = '''                <div class="row justify-content-center">
                    <div class="col-md-4 col-lg-3">
                        <div class="metric-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
                            <h4><i class="fas fa-leaf"></i> Renewable Share</h4>
                            <div class="value" id="renewableShare">-</div>
                            <div class="unit">%</div>
                        </div>
                    </div>
                    <div class="col-md-4 col-lg-3">
                        <div class="metric-card" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);">
                            <h4><i class="fas fa-smog"></i> CO₂ Emissions</h4>
                            <div class="value" id="co2Emissions">-</div>
                            <div class="unit">kt</div>
                        </div>
                    </div>
                </div>'''
    
    if old_pattern in content:
        content = content.replace(old_pattern, new_pattern)
        
        # Write back
        with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully centered the metric cards!")
        print("📊 The two cards (Renewable Share and CO₂ Emissions) are now center-aligned")
        return True
    else:
        print("❌ Could not find the metric cards pattern")
        return False

if __name__ == '__main__':
    center_align_cards()
