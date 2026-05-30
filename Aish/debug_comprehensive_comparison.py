#!/usr/bin/env python3
"""
Debug the comprehensive comparison issue
"""

def create_debug_html():
    """Create a debug HTML file to test the comparison"""
    
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Debug ML Comparison</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js"></script>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; background: #f5f5f5; }
        .test-section { background: white; padding: 20px; margin: 20px 0; border-radius: 10px; }
        .chart-container { width: 100%; height: 400px; margin: 20px 0; }
        .status { padding: 10px; border-radius: 5px; margin: 10px 0; }
        .success { background: #d4edda; color: #155724; }
        .error { background: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <h1>🔧 Debug ML Model Comparison</h1>
    
    <div class="test-section">
        <h2>📡 API Test</h2>
        <button onclick="testAPI()">Test API Endpoint</button>
        <div id="apiStatus"></div>
        <pre id="apiResponse"></pre>
    </div>
    
    <div class="test-section">
        <h2>📊 Chart Test</h2>
        <div class="chart-container">
            <canvas id="testChart"></canvas>
        </div>
        <div id="chartStatus"></div>
    </div>
    
    <div class="test-section">
        <h2>📋 Data Structure Test</h2>
        <div id="dataStatus"></div>
    </div>

    <script>
        // Test the API endpoint
        async function testAPI() {
            const statusDiv = document.getElementById('apiStatus');
            const responseDiv = document.getElementById('apiResponse');
            
            statusDiv.innerHTML = '<div class="status">🔄 Testing API...</div>';
            
            try {
                const response = await fetch('/api/comprehensive-comparison/');
                const data = await response.json();
                
                if (data.success) {
                    statusDiv.innerHTML = '<div class="status success">✅ API Working!</div>';
                    responseDiv.textContent = JSON.stringify(data, null, 2);
                    
                    // Test the data structure
                    testDataStructure(data);
                    
                    // Create test chart
                    createTestChart(data);
                } else {
                    statusDiv.innerHTML = '<div class="status error">❌ API Error: ' + data.error + '</div>';
                    responseDiv.textContent = JSON.stringify(data, null, 2);
                }
            } catch (error) {
                statusDiv.innerHTML = '<div class="status error">❌ Network Error: ' + error.message + '</div>';
                responseDiv.textContent = 'Error: ' + error.message;
            }
        }
        
        function testDataStructure(data) {
            const statusDiv = document.getElementById('dataStatus');
            
            let html = '<h3>📊 Data Analysis:</h3>';
            
            // Check objectives
            const objectives = data.objectives || [];
            html += `<p>Objectives: ${objectives.length}</p>`;
            
            // Check results
            const results = data.results || {};
            html += `<p>Result Sets: ${Object.keys(results).length}</p>`;
            
            // Check each objective's models
            html += '<h4>Model Coverage:</h4><ul>';
            for (let i = 1; i <= 8; i++) {
                if (results[i]) {
                    const models = Object.keys(results[i]);
                    html += `<li>Objective ${i}: ${models.length} models (${models.join(', ')})</li>`;
                } else {
                    html += `<li>Objective ${i}: ❌ Missing</li>`;
                }
            }
            html += '</ul>';
            
            statusDiv.innerHTML = html;
        }
        
        function createTestChart(data) {
            const statusDiv = document.getElementById('chartStatus');
            
            // Use Objective 3 data (classification)
            const obj3Data = data.results['3'];
            if (!obj3Data) {
                statusDiv.innerHTML = '<div class="status error">❌ No data for Objective 3</div>';
                return;
            }
            
            const ctx = document.getElementById('testChart');
            const labels = Object.keys(obj3Data);
            const values = Object.values(obj3Data);
            
            // Find best model (highest accuracy for classification)
            const bestModel = labels.reduce((a, b) => obj3Data[a] > obj3Data[b] ? a : b);
            
            // Colors
            const colors = labels.map(label => 
                label === bestModel ? '#FFD700' : '#667eea'
            );
            
            try {
                new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Accuracy',
                            data: values,
                            backgroundColor: colors,
                            borderColor: colors.map(c => c === '#FFD700' ? '#FFA500' : '#4a5fc1'),
                            borderWidth: 2
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            title: {
                                display: true,
                                text: 'Objective 3: Energy Access Classification'
                            }
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                max: 1.0
                            }
                        }
                    }
                });
                
                statusDiv.innerHTML = `
                    <div class="status success">✅ Chart Created Successfully!</div>
                    <p>Models: ${labels.length}</p>
                    <p>Best Model: ${bestModel} (${obj3Data[bestModel]})</p>
                `;
            } catch (error) {
                statusDiv.innerHTML = '<div class="status error">❌ Chart Error: ' + error.message + '</div>';
            }
        }
        
        // Auto-run test on page load
        window.addEventListener('DOMContentLoaded', function() {
            setTimeout(testAPI, 1000);
        });
    </script>
</body>
</html>'''
    
    with open('debug_ml_comparison.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ Created debug_ml_comparison.html")
    print("📋 Instructions:")
    print("1. Start Django server: python manage.py runserver")
    print("2. Open debug_ml_comparison.html in browser")
    print("3. Click 'Test API Endpoint' button")
    print("4. Check if all 7 models appear in the chart")

if __name__ == "__main__":
    create_debug_html()