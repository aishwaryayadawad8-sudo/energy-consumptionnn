"""
Fix: Combine historical and predicted values in the same chart for Objective 1
"""

def fix_combined_chart():
    with open('sustainable_energy/dashboard/templates/dashboard/objective1.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Find the section where we load historical data and predictions separately
    old_code = '''            // Load predictions
            fetch(`/api/objective1/predictions/?country=${encodeURIComponent(country)}&years=10`)
                .then(response => response.json())
                .then(data => {
                    if (data.success && data.predictions.length > 0) {
                        document.getElementById('predictionsSection').style.display = 'block';
                        document.getElementById('predictionsCountryName').textContent = 
                            `Predicted energy consumption for ${country}`;
                        
                        const ctx = document.getElementById('predictionsChart').getContext('2d');
                        
                        if (predictionsChart) {
                            predictionsChart.destroy();
                        }
                        
                        const years = data.predictions.map(d => d.year);
                        const predictions = data.predictions.map(d => d.predicted_consumption);
                        
                        predictionsChart = new Chart(ctx, {
                            type: 'line',
                            data: {
                                labels: years,
                                datasets: [{
                                    label: 'Predicted Consumption (kWh/person)',
                                    data: predictions,
                                    borderColor: 'rgba(39, 174, 96, 1)',
                                    backgroundColor: 'rgba(39, 174, 96, 0.1)',
                                    borderWidth: 3,
                                    fill: true,
                                    tension: 0.4,
                                    borderDash: [5, 5]
                                }]
                            },'''
    
    new_code = '''            // Load predictions and combine with historical data
            fetch(`/api/objective1/predictions/?country=${encodeURIComponent(country)}&years=10`)
                .then(response => response.json())
                .then(data => {
                    if (data.success && data.predictions.length > 0) {
                        // Show predictions section
                        document.getElementById('predictionsSection').style.display = 'block';
                        document.getElementById('predictionsCountryName').textContent = 
                            `Historical & Predicted energy consumption for ${country}`;
                        
                        const ctx = document.getElementById('predictionsChart').getContext('2d');
                        
                        if (predictionsChart) {
                            predictionsChart.destroy();
                        }
                        
                        // Get historical data from the already loaded historicalChart
                        const historicalYears = historicalChart.data.labels;
                        const historicalData = historicalChart.data.datasets[0].data;
                        
                        // Get prediction data
                        const predictionYears = data.predictions.map(d => d.year);
                        const predictionData = data.predictions.map(d => d.predicted_consumption);
                        
                        // Combine years for x-axis
                        const allYears = [...historicalYears, ...predictionYears];
                        
                        // Create combined datasets
                        predictionsChart = new Chart(ctx, {
                            type: 'line',
                            data: {
                                labels: allYears,
                                datasets: [
                                    {
                                        label: 'Historical Consumption (kWh/person)',
                                        data: [...historicalData, ...Array(predictionYears.length).fill(null)],
                                        borderColor: 'rgba(52, 152, 219, 1)',
                                        backgroundColor: 'rgba(52, 152, 219, 0.1)',
                                        borderWidth: 2,
                                        fill: true,
                                        tension: 0.4
                                    },
                                    {
                                        label: 'Predicted Consumption (kWh/person)',
                                        data: [...Array(historicalYears.length).fill(null), ...predictionData],
                                        borderColor: 'rgba(39, 174, 96, 1)',
                                        backgroundColor: 'rgba(39, 174, 96, 0.1)',
                                        borderWidth: 3,
                                        fill: true,
                                        tension: 0.4,
                                        borderDash: [5, 5]
                                    }
                                ]
                            },'''
    
    if old_code in content:
        content = content.replace(old_code, new_code)
        
        with open('sustainable_energy/dashboard/templates/dashboard/objective1.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully combined historical and predicted data in one chart!")
        print("📊 Changes:")
        print("   - Historical data (solid blue line)")
        print("   - Predicted data (dashed green line)")
        print("   - Both shown in the same graph")
        print("   - Seamless transition from historical to predictions")
        return True
    else:
        print("❌ Could not find the code to replace")
        print("The structure might have changed. Please check objective1.html manually.")
        return False

if __name__ == '__main__':
    fix_combined_chart()
