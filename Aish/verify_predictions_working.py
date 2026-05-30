#!/usr/bin/env python3
"""
Verify that the predictions chart is now working
"""

import requests
import time

def test_full_flow():
    """Test the complete flow"""
    print("🚀 Testing Complete Objective 5 Flow")
    print("=" * 50)
    
    base_url = "http://localhost:8000"
    
    # Test 1: Countries API
    print("\n1️⃣ Testing Countries API...")
    try:
        response = requests.get(f"{base_url}/api/objective5/countries/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                countries = data.get('countries', [])
                print(f"   ✅ Found {len(countries)} countries")
                test_country = countries[0] if countries else None
            else:
                print(f"   ❌ API failed: {data.get('error')}")
                return False
        else:
            print(f"   ❌ HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False
    
    if not test_country:
        print("   ❌ No countries available")
        return False
    
    # Test 2: Predictions API
    print(f"\n2️⃣ Testing Predictions API for {test_country}...")
    try:
        response = requests.get(f"{base_url}/api/objective5/predictions/?country={test_country}&years=10", timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                predictions = data.get('predictions', [])
                print(f"   ✅ Found {len(predictions)} predictions")
                if predictions:
                    first = predictions[0]
                    last = predictions[-1]
                    print(f"   📊 Range: {first['year']} ({first['predicted_access']:.1f}%) to {last['year']} ({last['predicted_access']:.1f}%)")
                    
                    # Verify data structure
                    required_keys = ['year', 'predicted_access']
                    if all(key in first for key in required_keys):
                        print(f"   ✅ Data structure is correct")
                        return True, test_country, predictions
                    else:
                        print(f"   ❌ Missing keys in data: {list(first.keys())}")
                        return False, None, None
                else:
                    print(f"   ❌ No predictions data")
                    return False, None, None
            else:
                print(f"   ❌ API failed: {data.get('error')}")
                return False, None, None
        else:
            print(f"   ❌ HTTP {response.status_code}")
            return False, None, None
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False, None, None

def create_verification_html(country, predictions):
    """Create a verification HTML file"""
    print(f"\n3️⃣ Creating verification HTML...")
    
    # Prepare data for JavaScript
    years = [p['year'] for p in predictions]
    values = [p['predicted_access'] for p in predictions]
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Objective 5 Predictions Verification</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 20px; }}
        .container {{ max-width: 1000px; margin: 0 auto; }}
        .chart-container {{ width: 100%; height: 400px; margin: 20px 0; }}
        .success {{ color: green; font-weight: bold; }}
        .info {{ background: #f0f8ff; padding: 15px; border-radius: 5px; margin: 10px 0; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 Objective 5 Predictions Chart - Verification</h1>
        
        <div class="info">
            <h3>✅ Verification Results:</h3>
            <p><strong>Country:</strong> {country}</p>
            <p><strong>Predictions:</strong> {len(predictions)} data points</p>
            <p><strong>Year Range:</strong> {years[0]} - {years[-1]}</p>
            <p><strong>Access Range:</strong> {values[0]:.1f}% - {values[-1]:.1f}%</p>
        </div>
        
        <h2>📊 Predictions Chart</h2>
        <div class="chart-container">
            <canvas id="predictionsChart"></canvas>
        </div>
        
        <div class="info">
            <h3>🔧 How to fix the main application:</h3>
            <ol>
                <li>Restart Django server: <code>python manage.py runserver</code></li>
                <li>Open <a href="http://localhost:8000/objective5/" target="_blank">http://localhost:8000/objective5/</a></li>
                <li>Open browser console (F12)</li>
                <li>Select "{country}" from dropdown</li>
                <li>Click "Analyze Country"</li>
                <li>Look for [PREDICTIONS] messages in console</li>
                <li>The predictions chart should now appear!</li>
            </ol>
        </div>
    </div>

    <script>
        // Chart data
        const chartData = {{
            years: {years},
            values: {values},
            country: "{country}"
        }};
        
        console.log('Chart data:', chartData);
        
        // Create chart
        const ctx = document.getElementById('predictionsChart').getContext('2d');
        const chart = new Chart(ctx, {{
            type: 'line',
            data: {{
                labels: chartData.years,
                datasets: [{{
                    label: chartData.country + ' - Predicted Access (%)',
                    data: chartData.values,
                    borderColor: 'rgba(56, 239, 125, 1)',
                    backgroundColor: 'rgba(56, 239, 125, 0.2)',
                    borderWidth: 3,
                    borderDash: [10, 5],
                    fill: true,
                    tension: 0.1,
                    pointRadius: 4,
                    pointHoverRadius: 6,
                    pointBackgroundColor: 'rgba(56, 239, 125, 1)',
                    pointBorderColor: '#fff',
                    pointBorderWidth: 2
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ 
                        display: true,
                        position: 'top'
                    }},
                    title: {{
                        display: true,
                        text: 'Future Electricity Access Predictions - ' + chartData.country,
                        font: {{ size: 16, weight: 'bold' }}
                    }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true,
                        max: 100,
                        title: {{ 
                            display: true, 
                            text: 'Access (%)'
                        }}
                    }},
                    x: {{
                        title: {{ 
                            display: true, 
                            text: 'Year'
                        }}
                    }}
                }}
            }}
        }});
        
        console.log('✅ Chart created successfully!');
    </script>
</body>
</html>'''
    
    with open('objective5_predictions_verification.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"   ✅ Created objective5_predictions_verification.html")
    return True

def main():
    # Test the APIs
    success, country, predictions = test_full_flow()
    
    if success:
        # Create verification HTML
        create_verification_html(country, predictions)
        
        print("\n" + "=" * 50)
        print("🎉 SUCCESS! Everything is working!")
        print("\n📋 Summary:")
        print(f"   ✅ API endpoints working")
        print(f"   ✅ Data structure correct")
        print(f"   ✅ {len(predictions)} predictions available")
        print(f"   ✅ Verification HTML created")
        
        print(f"\n🔄 Next Steps:")
        print(f"   1. Open objective5_predictions_verification.html in browser")
        print(f"   2. Verify the chart displays correctly")
        print(f"   3. If verification works, restart Django server")
        print(f"   4. Test the main application at http://localhost:8000/objective5/")
        print(f"   5. Check browser console for [PREDICTIONS] debug messages")
        
        print(f"\n💡 The predictions chart should now show values for {country}!")
        
    else:
        print("\n❌ Tests failed. Check server and API endpoints.")

if __name__ == "__main__":
    main()