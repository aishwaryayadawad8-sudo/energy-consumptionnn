"""
Remove only the cards showing N/A (Renewable Share and CO₂ Emissions)
Keep the cards with actual values (Electricity Access and Clean Cooking)
"""

def remove_na_cards():
    # Read the index.html file
    with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Find and replace the 4-card section with only 2 cards (the ones with values)
    old_section = '''                <!-- Key Metrics -->
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
    
    # Keep only the first two cards (with values) and center them
    new_section = '''                <!-- Key Metrics -->
                <div class="row justify-content-center">
                    <div class="col-md-4 col-lg-3">
                        <div class="metric-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
                            <h4><i class="fas fa-plug"></i> Electricity Access</h4>
                            <div class="value" id="electricityAccess">-</div>
                            <div class="unit">% of population</div>
                        </div>
                    </div>
                    <div class="col-md-4 col-lg-3">
                        <div class="metric-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
                            <h4><i class="fas fa-fire"></i> Clean Cooking</h4>
                            <div class="value" id="cleanCooking">-</div>
                            <div class="unit">% access</div>
                        </div>
                    </div>
                </div>'''
    
    if old_section in content:
        content = content.replace(old_section, new_section)
        
        # Also update JavaScript to remove references to the deleted cards
        old_js = '''            // Update metrics
            document.getElementById('electricityAccess').textContent = 
                data.electricity_access ? data.electricity_access.toFixed(1) : 'N/A';
            document.getElementById('cleanCooking').textContent = 
                data.clean_cooking_access ? data.clean_cooking_access.toFixed(1) : 'N/A';
            document.getElementById('renewableShare').textContent = 
                data.renewable_share ? data.renewable_share.toFixed(1) : 'N/A';
            document.getElementById('co2Emissions').textContent = 
                data.co2_emissions ? data.co2_emissions.toFixed(0) : 'N/A';'''
        
        new_js = '''            // Update metrics
            document.getElementById('electricityAccess').textContent = 
                data.electricity_access ? data.electricity_access.toFixed(1) : 'N/A';
            document.getElementById('cleanCooking').textContent = 
                data.clean_cooking_access ? data.clean_cooking_access.toFixed(1) : 'N/A';'''
        
        content = content.replace(old_js, new_js)
        
        # Write back
        with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully removed N/A cards!")
        print("📊 Kept cards with values:")
        print("   1. Electricity Access (Purple gradient)")
        print("   2. Clean Cooking (Pink gradient)")
        print("\n❌ Removed cards showing N/A:")
        print("   - Renewable Share")
        print("   - CO₂ Emissions")
        print("\n💡 The two remaining cards are centered on the page")
        return True
    else:
        print("❌ Could not find the metric cards section")
        return False

if __name__ == '__main__':
    remove_na_cards()
