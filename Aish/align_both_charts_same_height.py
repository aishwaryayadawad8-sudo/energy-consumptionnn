"""
Make both CO₂ Emissions and Energy Mix charts the same height for proper alignment
"""

def align_charts():
    # Read the file
    with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Find and replace both chart containers to have the same height
    old_charts = '''                <div class="row">
                    <div class="col-md-6">
                        <div class="chart-container">
                            <h4><i class="fas fa-chart-bar"></i> CO₂ Emissions Trend</h4>
                            <canvas id="co2Chart"></canvas>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="chart-container" style="height: 350px;">
                            <h4><i class="fas fa-chart-pie"></i> Energy Mix</h4>
                            <canvas id="energyMixChart"></canvas>
                        </div>
                    </div>
                </div>'''
    
    new_charts = '''                <div class="row">
                    <div class="col-md-6">
                        <div class="chart-container" style="height: 350px;">
                            <h4><i class="fas fa-chart-bar"></i> CO₂ Emissions Trend</h4>
                            <canvas id="co2Chart"></canvas>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="chart-container" style="height: 350px;">
                            <h4><i class="fas fa-chart-pie"></i> Energy Mix</h4>
                            <canvas id="energyMixChart"></canvas>
                        </div>
                    </div>
                </div>'''
    
    if old_charts in content:
        content = content.replace(old_charts, new_charts)
        
        # Write back
        with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully aligned both charts!")
        print("📊 Both charts now have the same height:")
        print("   - CO₂ Emissions Trend: 350px")
        print("   - Energy Mix: 350px")
        print("   Perfect alignment achieved!")
        return True
    else:
        print("❌ Could not find the charts section")
        return False

if __name__ == '__main__':
    align_charts()
