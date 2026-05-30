"""
Make the Energy Mix chart slightly larger (350px instead of 300px)
"""

def make_chart_larger():
    # Read the file
    with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Replace the chart container height
    old_chart = '''                    <div class="col-md-6">
                        <div class="chart-container" style="height: 300px;">
                            <h4><i class="fas fa-chart-pie"></i> Energy Mix</h4>
                            <canvas id="energyMixChart"></canvas>
                        </div>
                    </div>'''
    
    new_chart = '''                    <div class="col-md-6">
                        <div class="chart-container" style="height: 350px;">
                            <h4><i class="fas fa-chart-pie"></i> Energy Mix</h4>
                            <canvas id="energyMixChart"></canvas>
                        </div>
                    </div>'''
    
    if old_chart in content:
        content = content.replace(old_chart, new_chart)
        
        # Write back
        with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully made Energy Mix chart slightly larger!")
        print("📊 Chart height increased: 300px → 350px")
        print("   Better balance with other charts")
        return True
    else:
        print("❌ Could not find the Energy Mix chart")
        return False

if __name__ == '__main__':
    make_chart_larger()
