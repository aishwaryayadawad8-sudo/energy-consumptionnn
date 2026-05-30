#!/usr/bin/env python3
"""
Debug Objective 5 Predictions Chart
This script will help identify why the chart is empty
"""

import requests
import json

def test_predictions_api():
    """Test the predictions API directly"""
    print("🔍 Testing Objective 5 Predictions API...")
    
    try:
        # Test with Belarus (a country that should have data)
        url = "http://localhost:8000/api/objective5/predictions/?country=Belarus&years=10"
        print(f"📡 Calling: {url}")
        
        response = requests.get(url, timeout=10)
        print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"📋 Response Data:")
            print(json.dumps(data, indent=2))
            
            if data.get('success'):
                predictions = data.get('predictions', [])
                print(f"\n✅ API Success: Found {len(predictions)} predictions")
                
                if predictions:
                    print(f"📅 First prediction: {predictions[0]}")
                    print(f"📅 Last prediction: {predictions[-1]}")
                    
                    # Check data structure
                    first_pred = predictions[0]
                    if 'year' in first_pred and 'predicted_access' in first_pred:
                        print("✅ Data structure is correct")
                        return True, data
                    else:
                        print("❌ Data structure is wrong")
                        print(f"   Expected: 'year' and 'predicted_access'")
                        print(f"   Found: {list(first_pred.keys())}")
                        return False, data
                else:
                    print("❌ No predictions in response")
                    return False, data
            else:
                print(f"❌ API returned success=false: {data.get('error', 'Unknown error')}")
                return False, data
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            print(f"   Response: {response.text}")
            return False, None
            
    except requests.exceptions.ConnectionError:
        print("❌ Server not running. Start with: python manage.py runserver")
        return False, None
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False, None

def check_frontend_template():
    """Check if the frontend template has the correct code"""
    print("\n🔍 Checking Frontend Template...")
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective5_classification.html"
    
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for key elements
        checks = [
            ("predictions section", 'id="predictionsSection"'),
            ("predictions chart canvas", 'id="predictionsChart"'),
            ("loadPredictions function", 'function loadPredictions('),
            ("correct API endpoint", '/api/objective5/predictions/'),
            ("data mapping", 'data.predictions.map(d => d.predicted_access)'),
            ("chart creation", 'new Chart(ctx, {')
        ]
        
        print("📋 Template Checks:")
        all_good = True
        for name, pattern in checks:
            if pattern in content:
                print(f"   ✅ {name}")
            else:
                print(f"   ❌ {name} - MISSING!")
                all_good = False
        
        return all_good
        
    except FileNotFoundError:
        print(f"❌ Template file not found: {template_path}")
        return False
    except Exception as e:
        print(f"❌ Error reading template: {str(e)}")
        return False

def create_test_html():
    """Create a simple test HTML to verify the API works"""
    print("\n🔧 Creating test HTML file...")
    
    test_html = '''<!DOCTYPE html>
<html>
<head>
    <title>Test Objective 5 Predictions</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h1>Objective 5 Predictions Test</h1>
    <div>
        <select id="countrySelect">
            <option value="Belarus">Belarus</option>
            <option value="Afghanistan">Afghanistan</option>
            <option value="Albania">Albania</option>
        </select>
        <button onclick="testPredictions()">Test Predictions</button>
    </div>
    <div style="width: 800px; height: 400px; margin: 20px 0;">
        <canvas id="testChart"></canvas>
    </div>
    <div id="debug" style="background: #f0f0f0; padding: 10px; margin: 10px 0;"></div>

    <script>
        let testChart = null;
        
        function log(message) {
            console.log(message);
            document.getElementById('debug').innerHTML += message + '<br>';
        }
        
        function testPredictions() {
            const country = document.getElementById('countrySelect').value;
            log('Testing predictions for: ' + country);
            
            const url = `/api/objective5/predictions/?country=${encodeURIComponent(country)}&years=10`;
            log('Calling: ' + url);
            
            fetch(url)
                .then(response => {
                    log('Response status: ' + response.status);
                    return response.json();
                })
                .then(data => {
                    log('Response data: ' + JSON.stringify(data, null, 2));
                    
                    if (data.success && data.predictions && data.predictions.length > 0) {
                        log('✅ API Success! Found ' + data.predictions.length + ' predictions');
                        
                        // Create chart
                        const ctx = document.getElementById('testChart').getContext('2d');
                        if (testChart) testChart.destroy();
                        
                        const years = data.predictions.map(d => d.year);
                        const values = data.predictions.map(d => d.predicted_access);
                        
                        log('Years: ' + JSON.stringify(years));
                        log('Values: ' + JSON.stringify(values));
                        
                        testChart = new Chart(ctx, {
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
                                    pointHoverRadius: 6
                                }]
                            },
                            options: {
                                responsive: true,
                                maintainAspectRatio: false,
                                plugins: {
                                    title: {
                                        display: true,
                                        text: 'Test Predictions Chart - ' + country
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
                        
                        log('✅ Chart created successfully!');
                    } else {
                        log('❌ API failed or no data: ' + (data.error || 'Unknown error'));
                    }
                })
                .catch(error => {
                    log('❌ Fetch error: ' + error.message);
                });
        }
    </script>
</body>
</html>'''
    
    with open('test_objective5_predictions_debug.html', 'w', encoding='utf-8') as f:
        f.write(test_html)
    
    print("✅ Created test_objective5_predictions_debug.html")
    print("   Open this file in your browser to test the API directly")

def main():
    print("🚀 Debugging Objective 5 Predictions Chart")
    print("=" * 50)
    
    # Step 1: Test API
    api_success, api_data = test_predictions_api()
    
    # Step 2: Check template
    template_ok = check_frontend_template()
    
    # Step 3: Create test file
    create_test_html()
    
    print("\n" + "=" * 50)
    print("📋 Debug Summary:")
    print(f"   API Working: {'✅' if api_success else '❌'}")
    print(f"   Template OK: {'✅' if template_ok else '❌'}")
    
    if api_success and template_ok:
        print("\n✅ Both API and template look good!")
        print("   The issue might be in browser cache or JavaScript errors.")
        print("   Try:")
        print("   1. Hard refresh (Ctrl+F5)")
        print("   2. Clear browser cache")
        print("   3. Check browser console for errors")
        print("   4. Open test_objective5_predictions_debug.html to verify API")
    elif api_success and not template_ok:
        print("\n⚠️  API works but template has issues!")
        print("   The template needs to be fixed.")
    elif not api_success:
        print("\n❌ API is not working!")
        print("   Check the server and API implementation.")
    
    print(f"\n🔧 Next steps:")
    print(f"   1. Open test_objective5_predictions_debug.html in browser")
    print(f"   2. Click 'Test Predictions' button")
    print(f"   3. Check if chart appears with data")
    print(f"   4. If test works, the main template needs fixing")

if __name__ == "__main__":
    main()