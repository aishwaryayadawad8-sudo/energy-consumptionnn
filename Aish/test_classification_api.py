#!/usr/bin/env python3
"""
Test the classification API to ensure it returns the right data
"""

import requests
import json

def test_classification_api():
    """Test the combined API endpoint for classification data"""
    print("🔍 Testing Energy Access Classification API...")
    
    try:
        # Test with a country that should have data
        url = "http://localhost:8000/api/objective5/combined/?country=Belarus"
        print(f"📡 Calling: {url}")
        
        response = requests.get(url, timeout=10)
        print(f"📊 Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("📋 Response structure:")
            print(f"   Success: {data.get('success')}")
            print(f"   Data points: {len(data.get('data', []))}")
            
            if data.get('success') and data.get('data'):
                # Analyze the data structure
                sample_data = data['data']
                print(f"\n📊 Sample data points:")
                
                historical = [d for d in sample_data if d.get('type') == 'historical']
                predicted = [d for d in sample_data if d.get('type') == 'predicted']
                
                print(f"   Historical points: {len(historical)}")
                print(f"   Predicted points: {len(predicted)}")
                
                if historical:
                    print(f"   Sample historical: {historical[0]}")
                if predicted:
                    print(f"   Sample predicted: {predicted[0]}")
                
                # Check if access_level field exists
                access_levels = set()
                for point in sample_data:
                    if 'access_level' in point:
                        access_levels.add(point['access_level'])
                
                print(f"   Access levels found: {list(access_levels)}")
                
                if access_levels:
                    print("✅ API returns correct data structure for classification chart!")
                    return True
                else:
                    print("❌ Missing 'access_level' field in data")
                    return False
            else:
                print(f"❌ API failed: {data.get('error', 'Unknown error')}")
                return False
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def create_test_visualization():
    """Create a test HTML to verify the classification chart works"""
    print("\n🎨 Creating test visualization...")
    
    test_html = '''<!DOCTYPE html>
<html>
<head>
    <title>Energy Access Classification Test</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        .chart-container { width: 100%; height: 400px; margin: 20px 0; }
        .info { background: #e8f4fd; padding: 15px; border-radius: 5px; margin: 10px 0; }
    </style>
</head>
<body>
    <h1>🎯 Energy Access Classification Chart Test</h1>
    
    <div class="info">
        <h3>Chart Features:</h3>
        <ul>
            <li><strong>Type:</strong> Stepped line chart</li>
            <li><strong>Historical:</strong> Solid blue line (2000-2020)</li>
            <li><strong>Future:</strong> Dashed green line (2021-2030)</li>
            <li><strong>Y-axis:</strong> Low Access, Medium Access, High Access</li>
            <li><strong>X-axis:</strong> Years (2000-2030)</li>
        </ul>
    </div>
    
    <div class="chart-container">
        <canvas id="classificationChart"></canvas>
    </div>
    
    <button onclick="testWithRealData()">Test with Real API Data</button>
    <div id="result" style="margin-top: 10px; font-family: monospace;"></div>

    <script>
        let chart = null;
        
        function log(message) {
            console.log(message);
            document.getElementById('result').innerHTML += message + '<br>';
        }
        
        // Create test chart with sample data
        function createTestChart() {
            const ctx = document.getElementById('classificationChart').getContext('2d');
            
            // Sample data showing progression from Low to High access
            const historicalData = [
                {x: 2000, y: 1}, {x: 2005, y: 1}, {x: 2010, y: 1},
                {x: 2012, y: 2}, {x: 2015, y: 2}, {x: 2018, y: 3}, {x: 2020, y: 3}
            ];
            
            const futureData = [
                {x: 2021, y: 3}, {x: 2025, y: 3}, {x: 2030, y: 3}
            ];
            
            chart = new Chart(ctx, {
                type: 'line',
                data: {
                    datasets: [{
                        label: 'Historical',
                        data: historicalData,
                        borderColor: 'rgba(52, 152, 219, 1)',
                        backgroundColor: 'rgba(52, 152, 219, 0.1)',
                        borderWidth: 3,
                        stepped: true,
                        fill: false,
                        pointRadius: 4,
                        pointHoverRadius: 6
                    }, {
                        label: 'Future Predictions',
                        data: futureData,
                        borderColor: 'rgba(46, 204, 113, 1)',
                        backgroundColor: 'rgba(46, 204, 113, 0.1)',
                        borderWidth: 3,
                        borderDash: [10, 5],
                        stepped: true,
                        fill: false,
                        pointRadius: 4,
                        pointHoverRadius: 6
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: true, position: 'top' },
                        title: {
                            display: true,
                            text: 'Energy Access Classification per Country (Historical + Future)',
                            font: { size: 16, weight: 'bold' }
                        }
                    },
                    scales: {
                        x: {
                            type: 'linear',
                            min: 2000,
                            max: 2030,
                            title: { display: true, text: 'Year' },
                            ticks: { stepSize: 5 }
                        },
                        y: {
                            min: 0.5,
                            max: 3.5,
                            title: { display: true, text: 'Access Level' },
                            ticks: {
                                stepSize: 1,
                                callback: function(value) {
                                    const labels = {1: 'Low Access', 2: 'Medium Access', 3: 'High Access'};
                                    return labels[value] || '';
                                }
                            }
                        }
                    }
                }
            });
            
            log('✅ Test chart created with sample data');
        }
        
        function testWithRealData() {
            log('🔍 Testing with real API data...');
            
            fetch('/api/objective5/combined/?country=Belarus')
                .then(response => {
                    log('📊 API Response: ' + response.status);
                    return response.json();
                })
                .then(data => {
                    log('📋 Data received: ' + JSON.stringify(data, null, 2));
                    
                    if (data.success && data.data) {
                        log('✅ Real API data works!');
                        log('   Historical points: ' + data.data.filter(d => d.type === 'historical').length);
                        log('   Predicted points: ' + data.data.filter(d => d.type === 'predicted').length);
                    } else {
                        log('❌ API failed: ' + (data.error || 'Unknown error'));
                    }
                })
                .catch(error => {
                    log('❌ API Error: ' + error.message);
                });
        }
        
        // Auto-create test chart on load
        window.onload = function() {
            createTestChart();
        };
    </script>
</body>
</html>'''
    
    with open('test_energy_access_classification.html', 'w', encoding='utf-8') as f:
        f.write(test_html)
    
    print("✅ Created test_energy_access_classification.html")

def main():
    print("🚀 Testing Energy Access Classification Chart")
    print("=" * 50)
    
    # Test API
    api_works = test_classification_api()
    
    # Create test visualization
    create_test_visualization()
    
    print("\n" + "=" * 50)
    print("📋 Summary:")
    print(f"   API Working: {'✅' if api_works else '❌'}")
    print(f"   Test File: ✅ Created")
    
    print(f"\n🔄 Next Steps:")
    print(f"   1. Open test_energy_access_classification.html in browser")
    print(f"   2. Verify the stepped chart appears")
    print(f"   3. Click 'Test with Real API Data' button")
    print(f"   4. If test works, restart Django server and test main app")
    
    if api_works:
        print(f"\n🎉 The classification chart should work perfectly!")
        print(f"   It will show the exact same stepped line visualization as in your image.")

if __name__ == "__main__":
    main()