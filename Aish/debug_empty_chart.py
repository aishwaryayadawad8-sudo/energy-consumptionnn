#!/usr/bin/env python3
"""
Debug the empty chart issue and create a working solution
"""

import requests
import json

def check_browser_console_errors():
    """Create a test page to check for JavaScript errors"""
    print("🔍 Creating browser console test...")
    
    test_html = '''<!DOCTYPE html>
<html>
<head>
    <title>Debug Objective 5 Chart</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        .test-section { margin: 20px 0; padding: 15px; border: 1px solid #ddd; }
        .chart-container { width: 100%; height: 400px; margin: 20px 0; }
        .log { background: #f5f5f5; padding: 10px; margin: 10px 0; font-family: monospace; }
    </style>
</head>
<body>
    <h1>🔧 Objective 5 Chart Debug Tool</h1>
    
    <div class="test-section">
        <h2>Test 1: Basic Chart.js Test</h2>
        <button onclick="testBasicChart()">Test Basic Chart</button>
        <div class="chart-container">
            <canvas id="basicChart"></canvas>
        </div>
    </div>
    
    <div class="test-section">
        <h2>Test 2: API Connection Test</h2>
        <button onclick="testAPI()">Test API</button>
        <div id="apiResult" class="log">Click button to test API...</div>
    </div>
    
    <div class="test-section">
        <h2>Test 3: Real Predictions Chart</h2>
        <select id="countrySelect">
            <option value="Belarus">Belarus</option>
            <option value="Afghanistan">Afghanistan</option>
            <option value="Albania">Albania</option>
        </select>
        <button onclick="testRealChart()">Test Real Chart</button>
        <div class="chart-container">
            <canvas id="realChart"></canvas>
        </div>
    </div>
    
    <div class="test-section">
        <h2>Console Log</h2>
        <div id="consoleLog" class="log">Ready...</div>
    </div>

    <script>
        let basicChart = null;
        let realChart = null;
        
        function log(message) {
            console.log(message);
            const logDiv = document.getElementById('consoleLog');
            logDiv.innerHTML += new Date().toLocaleTimeString() + ': ' + message + '<br>';
            logDiv.scrollTop = logDiv.scrollHeight;
        }
        
        function testBasicChart() {
            log('🧪 Testing basic Chart.js functionality...');
            
            try {
                const ctx = document.getElementById('basicChart').getContext('2d');
                if (basicChart) basicChart.destroy();
                
                basicChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: [2021, 2022, 2023, 2024, 2025],
                        datasets: [{
                            label: 'Test Data',
                            data: [85, 87, 89, 91, 93],
                            borderColor: 'rgba(56, 239, 125, 1)',
                            backgroundColor: 'rgba(56, 239, 125, 0.2)',
                            borderWidth: 3,
                            borderDash: [10, 5],
                            fill: true,
                            tension: 0.1,
                            pointRadius: 4
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            title: {
                                display: true,
                                text: 'Basic Chart Test'
                            }
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                max: 100,
                                title: { display: true, text: 'Access (%)' }
                            },
                            x: {
                                title: { display: true, text: 'Year' }
                            }
                        }
                    }
                });
                
                log('✅ Basic chart created successfully!');
                
            } catch (error) {
                log('❌ Basic chart failed: ' + error.message);
            }
        }
        
        function testAPI() {
            log('🌐 Testing API connection...');
            
            fetch('/api/objective5/predictions/?country=Belarus&years=10')
                .then(response => {
                    log('📡 API Response Status: ' + response.status);
                    return response.json();
                })
                .then(data => {
                    log('📊 API Response: ' + JSON.stringify(data, null, 2));
                    
                    const resultDiv = document.getElementById('apiResult');
                    if (data.success && data.predictions) {
                        resultDiv.innerHTML = `
                            <strong>✅ API Success!</strong><br>
                            Country: ${data.country}<br>
                            Predictions: ${data.predictions.length} points<br>
                            Range: ${data.predictions[0].year} - ${data.predictions[data.predictions.length-1].year}<br>
                            Sample: ${data.predictions[0].predicted_access.toFixed(1)}% - ${data.predictions[data.predictions.length-1].predicted_access.toFixed(1)}%
                        `;
                    } else {
                        resultDiv.innerHTML = `<strong>❌ API Failed:</strong> ${data.error || 'Unknown error'}`;
                    }
                })
                .catch(error => {
                    log('❌ API Error: ' + error.message);
                    document.getElementById('apiResult').innerHTML = `<strong>❌ API Error:</strong> ${error.message}`;
                });
        }
        
        function testRealChart() {
            const country = document.getElementById('countrySelect').value;
            log('🎯 Testing real chart for: ' + country);
            
            fetch(`/api/objective5/predictions/?country=${country}&years=10`)
                .then(response => {
                    log('📡 Real API Status: ' + response.status);
                    return response.json();
                })
                .then(data => {
                    log('📊 Real API Data: ' + JSON.stringify(data));
                    
                    if (data.success && data.predictions && data.predictions.length > 0) {
                        log('✅ Got ' + data.predictions.length + ' predictions');
                        
                        const ctx = document.getElementById('realChart').getContext('2d');
                        if (realChart) realChart.destroy();
                        
                        const years = data.predictions.map(d => d.year);
                        const values = data.predictions.map(d => d.predicted_access);
                        
                        log('📈 Chart Data - Years: ' + years.join(', '));
                        log('📈 Chart Data - Values: ' + values.map(v => v.toFixed(1)).join(', '));
                        
                        realChart = new Chart(ctx, {
                            type: 'line',
                            data: {
                                labels: years,
                                datasets: [{
                                    label: country + ' - Predicted Access (%)',
                                    data: values,
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
                                }]
                            },
                            options: {
                                responsive: true,
                                maintainAspectRatio: false,
                                plugins: {
                                    legend: { display: true },
                                    title: {
                                        display: true,
                                        text: 'Real Predictions Chart - ' + country
                                    }
                                },
                                scales: {
                                    y: {
                                        beginAtZero: true,
                                        max: 100,
                                        title: { display: true, text: 'Access (%)' }
                                    },
                                    x: {
                                        title: { display: true, text: 'Year' }
                                    }
                                }
                            }
                        });
                        
                        log('✅ Real chart created successfully!');
                        
                    } else {
                        log('❌ No data available: ' + (data.error || 'Unknown error'));
                    }
                })
                .catch(error => {
                    log('❌ Real chart error: ' + error.message);
                });
        }
        
        // Auto-run basic test on load
        window.onload = function() {
            log('🚀 Page loaded, running auto-tests...');
            setTimeout(testBasicChart, 500);
            setTimeout(testAPI, 1000);
        };
    </script>
</body>
</html>'''
    
    with open('debug_objective5_chart.html', 'w', encoding='utf-8') as f:
        f.write(test_html)
    
    print("✅ Created debug_objective5_chart.html")
    print("   Open this file in your browser to test step by step")

def test_current_api():
    """Test the current API to see what's happening"""
    print("\n🔍 Testing current API...")
    
    try:
        response = requests.get("http://localhost:8000/api/objective5/predictions/?country=Belarus&years=10", timeout=5)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("Response:")
            print(json.dumps(data, indent=2))
            
            if data.get('success') and data.get('predictions'):
                print(f"\n✅ API is working! Found {len(data['predictions'])} predictions")
                return True
            else:
                print(f"\n❌ API returned no data: {data.get('error', 'Unknown')}")
                return False
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Connection Error: {e}")
        return False

def main():
    print("🚀 Debugging Empty Chart Issue")
    print("=" * 50)
    
    # Test API first
    api_working = test_current_api()
    
    # Create debug HTML
    check_browser_console_errors()
    
    print("\n" + "=" * 50)
    print("📋 Debug Summary:")
    print(f"   API Working: {'✅' if api_working else '❌'}")
    print(f"   Debug Tool: ✅ Created")
    
    print(f"\n🔧 Next Steps:")
    print(f"   1. Open debug_objective5_chart.html in your browser")
    print(f"   2. Run all three tests:")
    print(f"      - Test 1: Basic Chart (should work)")
    print(f"      - Test 2: API Test (should show data)")
    print(f"      - Test 3: Real Chart (should show predictions)")
    print(f"   3. Check console log for any errors")
    print(f"   4. If tests work, the main app needs fixing")
    
    if api_working:
        print(f"\n💡 Since API is working, the issue is likely:")
        print(f"   - JavaScript errors in the main template")
        print(f"   - Chart container not visible")
        print(f"   - Browser cache issues")
        print(f"   - Missing Chart.js library")

if __name__ == "__main__":
    main()