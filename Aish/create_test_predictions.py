#!/usr/bin/env python3
"""Create test page for predictions"""

html = """<!DOCTYPE html>
<html>
<head>
    <title>Test Objective 5 Predictions</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h1>Test Predictions</h1>
    <button onclick="test()">Test Belarus</button>
    <div id="result"></div>
    <canvas id="chart"></canvas>
    
    <script>
        async function test() {
            const response = await fetch('/api/objective5/predictions/?country=Belarus&years=10');
            const data = await response.json();
            document.getElementById('result').innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
            
            if (data.success && data.predictions) {
                const ctx = document.getElementById('chart').getContext('2d');
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: data.predictions.map(d => d.year),
                        datasets: [{
                            label: 'Predicted Access',
                            data: data.predictions.map(d => d.predicted_access),
                            borderColor: 'blue',
                            fill: false
                        }]
                    }
                });
            }
        }
    </script>
</body>
</html>"""

with open('test_predictions_simple.html', 'w') as f:
    f.write(html)
    
print("Created test_predictions_simple.html")
print("Open this file in your browser while the Django server is running")
