"""
Complete fix for predictions chart - store data separately and combine properly
"""

def complete_fix():
    with open('sustainable_energy/dashboard/templates/dashboard/objective1.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Find the script section and add a variable to store historical data
    old_script_start = '''    <script>
        let mseChart = null;
        let historicalChart = null;
        let predictionsChart = null;'''
    
    new_script_start = '''    <script>
        let mseChart = null;
        let historicalChart = null;
        let predictionsChart = null;
        let historicalDataStore = null; // Store historical data for predictions chart'''
    
    content = content.replace(old_script_start, new_script_start)
    
    # Now find and replace the loadCountryData function to store historical data
    old_load_function = '''                        const years = data.data.map(d => d.Year);
                        const consumption = data.data.map(d => d['Primary energy consumption per capita (kWh/person)']);
                        
                        historicalChart = new Chart(ctx, {'''
    
    new_load_function = '''                        const years = data.data.map(d => d.Year);
                        const consumption = data.data.map(d => d['Primary energy consumption per capita (kWh/person)']);
                        
                        // Store historical data for use in predictions chart
                        historicalDataStore = {
                            years: years,
                            consumption: consumption
                        };
                        
                        historicalChart = new Chart(ctx, {'''
    
    content = content.replace(old_load_function, new_load_function)
    
    # Now fix the predictions chart to use stored data instead of historicalChart
    old_predictions = '''                    console.log('Predictions API Response:', data);
                    console.log('Historical Chart:', historicalChart);
                    if (historicalChart) {
                        console.log('Historical Years:', historicalChart.data.labels);
                        console.log('Historical Data:', historicalChart.data.datasets[0].data);
                    }
                    if (data.success && data.predictions && data.predictions.length > 0) {
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
                        const allYears = [...historicalYears, ...predictionYears];'''
    
    new_predictions = '''                    console.log('Predictions API Response:', data);
                    console.log('Historical Data Store:', historicalDataStore);
                    
                    if (data.success && data.predictions && data.predictions.length > 0) {
                        // Show predictions section
                        document.getElementById('predictionsSection').style.display = 'block';
                        document.getElementById('predictionsCountryName').textContent = 
                            `Historical & Predicted energy consumption for ${country}`;
                        
                        const ctx = document.getElementById('predictionsChart').getContext('2d');
                        
                        if (predictionsChart) {
                            predictionsChart.destroy();
                        }
                        
                        // Get historical data from stored data
                        const historicalYears = historicalDataStore ? historicalDataStore.years : [];
                        const historicalData = historicalDataStore ? historicalDataStore.consumption : [];
                        
                        // Get prediction data
                        const predictionYears = data.predictions.map(d => d.year);
                        const predictionData = data.predictions.map(d => d.predicted_consumption);
                        
                        console.log('Historical Years:', historicalYears);
                        console.log('Historical Data:', historicalData);
                        console.log('Prediction Years:', predictionYears);
                        console.log('Prediction Data:', predictionData);
                        
                        // Combine years for x-axis
                        const allYears = [...historicalYears, ...predictionYears];'''
    
    content = content.replace(old_predictions, new_predictions)
    
    with open('sustainable_energy/dashboard/templates/dashboard/objective1.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Complete fix applied!")
    print("📊 Changes:")
    print("   - Added historicalDataStore variable to store data separately")
    print("   - Historical data is now stored when loaded")
    print("   - Predictions chart uses stored data instead of chart object")
    print("   - Added comprehensive console logging")
    print("\n🔧 Next steps:")
    print("   1. Refresh your browser (Ctrl+F5)")
    print("   2. Open console (F12)")
    print("   3. Select a country")
    print("   4. Check console for data values")
    return True

if __name__ == '__main__':
    complete_fix()
