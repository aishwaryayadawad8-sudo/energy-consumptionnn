"""
Add console logging to debug the predictions issue
"""

def add_logging():
    with open('sustainable_energy/dashboard/templates/dashboard/objective1.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Add logging after the predictions fetch
    old_code = '''            // Load predictions and combine with historical data
            fetch(`/api/objective1/predictions/?country=${encodeURIComponent(country)}&years=10`)
                .then(response => response.json())
                .then(data => {
                    if (data.success && data.predictions.length > 0) {'''
    
    new_code = '''            // Load predictions and combine with historical data
            fetch(`/api/objective1/predictions/?country=${encodeURIComponent(country)}&years=10`)
                .then(response => response.json())
                .then(data => {
                    console.log('Predictions API Response:', data);
                    console.log('Historical Chart:', historicalChart);
                    if (historicalChart) {
                        console.log('Historical Years:', historicalChart.data.labels);
                        console.log('Historical Data:', historicalChart.data.datasets[0].data);
                    }
                    if (data.success && data.predictions && data.predictions.length > 0) {'''
    
    if old_code in content:
        content = content.replace(old_code, new_code)
        
        with open('sustainable_energy/dashboard/templates/dashboard/objective1.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Added debug logging!")
        print("📊 Now check the browser console (F12) to see:")
        print("   - Predictions API Response")
        print("   - Historical Chart data")
        print("   - Any errors")
        return True
    
    print("❌ Could not find the code")
    return False

if __name__ == '__main__':
    add_logging()
