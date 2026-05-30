"""
Make the Energy Mix chart smaller to fix alignment issues
"""

def make_chart_smaller():
    # Read the file
    with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Replace the Energy Mix chart container with a smaller version
    old_chart = '''                    <div class="col-md-6">
                        <div class="chart-container">
                            <h4><i class="fas fa-chart-pie"></i> Energy Mix</h4>
                            <canvas id="energyMixChart"></canvas>
                        </div>
                    </div>'''
    
    new_chart = '''                    <div class="col-md-6">
                        <div class="chart-container" style="height: 300px;">
                            <h4><i class="fas fa-chart-pie"></i> Energy Mix</h4>
                            <canvas id="energyMixChart"></canvas>
                        </div>
                    </div>'''
    
    if old_chart in content:
        content = content.replace(old_chart, new_chart)
        
        # Also update the Energy Mix chart options to maintain aspect ratio
        old_chart_config = '''            charts.energyMix = new Chart(document.getElementById('energyMixChart'), {
                type: 'doughnut',
                data: {
                    labels: ['Fossil Fuels', 'Renewables', 'Nuclear'],
                    datasets: [{
                        data: [
                            latestData['Electricity from fossil fuels (TWh)'] || 0,
                            latestData['Electricity from renewables (TWh)'] || 0,
                            latestData['Electricity from nuclear (TWh)'] || 0
                        ],
                        backgroundColor: ['#e74c3c', '#27ae60', '#3498db']
                    }]
                },
                options: {
                    responsive: true,
                    plugins: { legend: { position: 'bottom' } }
                }
            });'''
        
        new_chart_config = '''            charts.energyMix = new Chart(document.getElementById('energyMixChart'), {
                type: 'doughnut',
                data: {
                    labels: ['Fossil Fuels', 'Renewables', 'Nuclear'],
                    datasets: [{
                        data: [
                            latestData['Electricity from fossil fuels (TWh)'] || 0,
                            latestData['Electricity from renewables (TWh)'] || 0,
                            latestData['Electricity from nuclear (TWh)'] || 0
                        ],
                        backgroundColor: ['#e74c3c', '#27ae60', '#3498db']
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: true,
                    aspectRatio: 1.5,
                    plugins: { 
                        legend: { 
                            position: 'bottom',
                            labels: {
                                boxWidth: 12,
                                font: {
                                    size: 11
                                }
                            }
                        } 
                    }
                }
            });'''
        
        content = content.replace(old_chart_config, new_chart_config)
        
        # Write back
        with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully made Energy Mix chart smaller!")
        print("📊 Changes:")
        print("   - Reduced chart container height to 300px")
        print("   - Added aspect ratio control (1.5)")
        print("   - Smaller legend labels (font size 11)")
        print("   - Smaller legend boxes (12px)")
        print("   - Better alignment with other charts")
        return True
    else:
        print("❌ Could not find the Energy Mix chart")
        return False

if __name__ == '__main__':
    make_chart_smaller()
