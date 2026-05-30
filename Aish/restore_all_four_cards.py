"""
Restore all 4 original metric cards (Electricity Access, Clean Cooking, Renewable Share, CO₂ Emissions)
"""

def restore_cards():
    # Read the index.html file
    with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Find the current metric cards section
    old_section = '''                <!-- Key Metrics -->
                <div class="row justify-content-center">
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
    
    # Restore all 4 cards
    new_section = '''                <!-- Key Metrics -->
                <div class="row">
                    <div class="col-md-3">
                        <div class="metric-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
                            <h4><i class="fas fa-plug"></i> Electricity Access</h4>
                            <div class="value" id="electricityAccess">-</div>
                            <div class="unit">% of population</div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="metric-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
                            <h4><i class="fas fa-fire"></i> Clean Cooking</h4>
                            <div class="value" id="cleanCooking">-</div>
                            <div class="unit">% access</div>
                        </div>
                    </div>
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
    
    if old_section in content:
        content = content.replace(old_section, new_section)
        
        # Also restore the JavaScript to update all 4 cards
        old_js = '''            // Update metrics
            document.getElementById('renewableShare').textContent = 
                data.renewable_share ? data.renewable_share.toFixed(1) : 'N/A';
            document.getElementById('co2Emissions').textContent = 
                data.co2_emissions ? data.co2_emissions.toFixed(0) : 'N/A';'''
        
        new_js = '''            // Update metrics
            document.getElementById('electricityAccess').textContent = 
                data.electricity_access ? data.electricity_access.toFixed(1) : 'N/A';
            document.getElementById('cleanCooking').textContent = 
                data.clean_cooking_access ? data.clean_cooking_access.toFixed(1) : 'N/A';
            document.getElementById('renewableShare').textContent = 
                data.renewable_share ? data.renewable_share.toFixed(1) : 'N/A';
            document.getElementById('co2Emissions').textContent = 
                data.co2_emissions ? data.co2_emissions.toFixed(0) : 'N/A';'''
        
        content = content.replace(old_js, new_js)
        
        # Write back
        with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully restored all 4 metric cards!")
        print("📊 Cards restored:")
        print("   1. Electricity Access (Purple gradient)")
        print("   2. Clean Cooking (Pink gradient)")
        print("   3. Renewable Share (Blue gradient)")
        print("   4. CO₂ Emissions (Orange gradient)")
        print("\n💡 The cards will show actual data when you search for a country")
        print("   They show 'N/A' initially because no country is selected yet")
        return True
    else:
        print("❌ Could not find the metric cards section")
        return False

if __name__ == '__main__':
    restore_cards()
