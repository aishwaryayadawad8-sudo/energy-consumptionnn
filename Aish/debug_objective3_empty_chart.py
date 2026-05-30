#!/usr/bin/env python3
"""
Debug and fix the empty Energy Access Classification chart in Objective 3
"""

import requests
import json

def test_objective3_apis():
    """Test all Objective 3 API endpoints to identify the issue"""
    print("🔍 Testing Objective 3 API Endpoints...")
    
    base_url = "http://localhost:8000"
    test_country = "Belarus"
    
    # Test 1: Countries endpoint
    print(f"\n1️⃣ Testing Countries API...")
    try:
        response = requests.get(f"{base_url}/api/objective3/countries/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                countries = data.get('countries', [])
                print(f"   ✅ Found {len(countries)} countries")
                if test_country in countries:
                    print(f"   ✅ {test_country} is available")
                else:
                    print(f"   ⚠️  {test_country} not found, using {countries[0] if countries else 'None'}")
                    test_country = countries[0] if countries else None
            else:
                print(f"   ❌ Countries API failed: {data.get('error')}")
                return False
        else:
            print(f"   ❌ HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False
    
    if not test_country:
        print("❌ No countries available for testing")
        return False
    
    # Test 2: Combined endpoint (what we need for the chart)
    print(f"\n2️⃣ Testing Combined API for {test_country}...")
    try:
        response = requests.get(f"{base_url}/api/objective3/combined/?country={test_country}", timeout=10)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"   Success: {data.get('success')}")
            
            if data.get('success') and data.get('data'):
                combined_data = data['data']
                print(f"   Total data points: {len(combined_data)}")
                
                # Analyze data structure
                historical = [d for d in combined_data if d.get('type') == 'historical']
                predicted = [d for d in combined_data if d.get('type') == 'predicted']
                
                print(f"   Historical points: {len(historical)}")
                print(f"   Predicted points: {len(predicted)}")
                
                if historical:
                    print(f"   Sample historical: {historical[0]}")
                if predicted:
                    print(f"   Sample predicted: {predicted[0]}")
                
                # Check required fields
                required_fields = ['year', 'access_level', 'type']
                sample_point = combined_data[0] if combined_data else {}
                missing_fields = [field for field in required_fields if field not in sample_point]
                
                if missing_fields:
                    print(f"   ❌ Missing fields: {missing_fields}")
                    return False
                else:
                    print(f"   ✅ All required fields present")
                    return True, test_country, combined_data
            else:
                print(f"   ❌ No data returned: {data.get('error', 'Unknown error')}")
                return False
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def create_debug_html(country, data):
    """Create a debug HTML to test the chart independently"""
    print(f"\n3️⃣ Creating debug HTML for {country}...")
    
    # Prepare data for JavaScript
    historical = [d for d in data if d.get('type') == 'historical']
    predicted = [d for d in data if d.get('type') == 'predicted']
    
    html_content = f'''<!DOCTYPE html>
<html>
<head>
    <title>Debug Objective 3 Classification Chart</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 20px; }}
        .container {{ max-width: 1000px; margin: 0 auto; }}
        .chart-container {{ width: 100%; height: 400px; margin: 20px 0; }}
        .info {{ background: #e8f4fd; padding: 15px; border-radius: 5px; margin: 10px 0; }}
        .debug {{ background: #f8f9fa; padding: 10px; margin: 10px 0; font-family: monospace; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔧 Debug: Objective 3 Classification Chart</h1>
        
        <div class="info">
            <h3>Data Summary for {country}:</h3>
            <ul>
                <li><strong>Total Points:</strong> {len(data)}</li>
                <li><strong>Historical:</strong> {len(historical)} points</li>
                <li><strong>Predicted:</strong> {len(predicted)} points</li>
            </ul>
        </div>
        
        <button onclick="createChart()">Create Chart</button>
        <button onclick="testAPI()">Test API</button>
        
        <div class="chart-container">
            <canvas id="debugChart"></canvas>
        </div>
        
        <div class="debug" id="debugLog">Ready to test...</div>
    </div>

    <script>
        let chart = null;
        
        function log(message) {{
            console.log(message);
            document.getElementById('debugLog').innerHTML += new Date().toLocaleTimeString() + ': ' + message + '<br>';
        }}
        
        function createChart() {{
            log('🎨 Creating chart with sample data...');
            
            const canvas = document.getElementById('debugChart');
            const ctx = canvas.getContext('2d');
            
            if (chart) chart.destroy();
            
            // Map access levels to numbers
            const levelMap = {{
                'Low Access': 1,
                'Medium Access': 2,
                'High Access': 3
            }};
            
            // Prepare historical data
            const historicalData = {json.dumps([{"x": d["year"], "y": 1 if d.get("access_level") == "Low Access" else 2 if d.get("access_level") == "Medium Access" else 3} for d in historical])};
            
            // Prepare predicted data  
            const predictedData = {json.dumps([{"x": d["year"], "y": 1 if d.get("access_level") == "Low Access" else 2 if d.get("access_level") == "Medium Access" else 3} for d in predicted])};
            
            log('📊 Historical data points: ' + historicalData.length);
            log('📊 Predicted data points: ' + predictedData.length);
            
            const datasets = [];
            
            // Add historical dataset
            if (historicalData.length > 0) {{
                datasets.push({{
                    label: 'Historical',
                    data: historicalData,
                    borderColor: 'rgba(52, 152, 219, 1)',
                    backgroundColor: 'rgba(52, 152, 219, 0.1)',
                    borderWidth: 3,
                    stepped: true,
                    fill: false,
                    pointRadius: 4
                }});
            }}
            
            // Add predicted dataset
            if (predictedData.length > 0) {{
                datasets.push({{
                    label: 'Future Predictions',
                    data: predictedData,
                    borderColor: 'rgba(46, 204, 113, 1)',
                    backgroundColor: 'rgba(46, 204, 113, 0.1)',
                    borderWidth: 3,
                    borderDash: [10, 5],
                    stepped: true,
                    fill: false,
                    pointRadius: 4
                }});
            }}
            
            chart = new Chart(ctx, {{
                type: 'line',
                data: {{ datasets: datasets }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        title: {{
                            display: true,
                            text: 'Energy Access Classification - {country}',
                            font: {{ size: 16, weight: 'bold' }}
                        }},
                        legend: {{ display: true }}
                    }},
                    scales: {{
                        x: {{
                            type: 'linear',
                            min: 2000,
                            max: 2030,
                            title: {{ display: true, text: 'Year' }},
                            ticks: {{ stepSize: 5 }}
                        }},
                        y: {{
                            min: 0.5,
                            max: 3.5,
                            title: {{ display: true, text: 'Access Level' }},
                            ticks: {{
                                stepSize: 1,
                                callback: function(value) {{
                                    const labels = {{1: 'Low Access', 2: 'Medium Access', 3: 'High Access'}};
                                    return labels[value] || '';
                                }}
                            }}
                        }}
                    }}
                }}
            }});
            
            log('✅ Chart created successfully!');
        }}
        
        function testAPI() {{
            log('🌐 Testing API...');
            
            fetch('/api/objective3/combined/?country={country}')
                .then(response => {{
                    log('📡 API Response: ' + response.status);
                    return response.json();
                }})
                .then(data => {{
                    log('📋 API Data: ' + JSON.stringify(data, null, 2));
                    
                    if (data.success && data.data) {{
                        log('✅ API works! Data points: ' + data.data.length);
                    }} else {{
                        log('❌ API failed: ' + (data.error || 'Unknown error'));
                    }}
                }})
                .catch(error => {{
                    log('❌ API Error: ' + error.message);
                }});
        }}
        
        // Auto-create chart on load
        window.onload = function() {{
            createChart();
        }};
    </script>
</body>
</html>'''
    
    with open('debug_objective3_classification.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"   ✅ Created debug_objective3_classification.html")

def main():
    print("🚀 Debugging Objective 3 Empty Classification Chart")
    print("=" * 60)
    
    # Test APIs
    result = test_objective3_apis()
    
    if isinstance(result, tuple) and len(result) == 3:
        success, country, data = result
        if success:
            # Create debug HTML
            create_debug_html(country, data)
            
            print("\n" + "=" * 60)
            print("✅ API is working correctly!")
            print(f"   Country: {country}")
            print(f"   Data points: {len(data)}")
            
            print(f"\n🔧 Next Steps:")
            print(f"   1. Open debug_objective3_classification.html in browser")
            print(f"   2. Verify the chart displays correctly")
            print(f"   3. If debug chart works, the issue is in the main template")
            print(f"   4. Check browser console in Objective 3 for JavaScript errors")
            
            return True
    
    print("\n❌ API testing failed - need to fix API first")
    return False

if __name__ == "__main__":
    main()