#!/usr/bin/env python3
"""
Add visibility fixes to ensure the chart shows up
"""

# Read the current template
with open('sustainable_energy/dashboard/templates/dashboard/objective5_classification.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add CSS to ensure chart visibility
css_fix = '''        .chart-container {
            position: relative;
            height: 450px;
            margin-top: 20px;
            width: 100% !important;
            display: block !important;
            visibility: visible !important;
        }
        
        #predictionsChart {
            display: block !important;
            visibility: visible !important;
            width: 100% !important;
            height: 100% !important;
        }
        
        #predictionsSection {
            display: block !important;
            visibility: visible !important;
        }'''

# Find the existing chart-container style and replace it
old_chart_container = '''        .chart-container {
            position: relative;
            height: 450px;
            margin-top: 20px;
        }'''

if old_chart_container in content:
    content = content.replace(old_chart_container, css_fix)
    print("✅ Updated chart-container CSS")
else:
    # Add it before </style>
    style_end = content.find('</style>')
    if style_end != -1:
        content = content[:style_end] + css_fix + '\n    </style>' + content[style_end + 8:]
        print("✅ Added chart visibility CSS")

# Add a test button to force show the chart
test_button_html = '''        
        <!-- DEBUG: Test Predictions Button -->
        <div class="section-card" style="background: #fff3cd; border: 1px solid #ffeaa7;">
            <h3 style="color: #856404;">🔧 Debug: Force Test Predictions Chart</h3>
            <p style="color: #856404;">If the chart is not showing, click this button to force create it with test data:</p>
            <button class="btn btn-warning" onclick="forceTestChart()">
                <i class="fas fa-wrench"></i> Force Create Test Chart
            </button>
            <div id="testResult" style="margin-top: 10px; font-family: monospace; font-size: 12px;"></div>
        </div>
'''

# Add the test button before the historical section
historical_section_start = content.find('<!-- Historical Data Section -->')
if historical_section_start != -1:
    content = content[:historical_section_start] + test_button_html + '\n        ' + content[historical_section_start:]
    print("✅ Added debug test button")

# Add the forceTestChart function
force_test_function = '''        
        function forceTestChart() {
            console.log('🔧 [FORCE-TEST] Creating test chart...');
            document.getElementById('testResult').innerHTML = 'Testing...';
            
            try {
                // Force show predictions section
                const section = document.getElementById('predictionsSection');
                const nameElement = document.getElementById('predictionsCountryName');
                const canvas = document.getElementById('predictionsChart');
                
                if (!section) {
                    document.getElementById('testResult').innerHTML = '❌ predictionsSection not found';
                    return;
                }
                
                if (!canvas) {
                    document.getElementById('testResult').innerHTML = '❌ predictionsChart canvas not found';
                    return;
                }
                
                // Force visibility
                section.style.display = 'block';
                section.style.visibility = 'visible';
                canvas.style.display = 'block';
                canvas.style.visibility = 'visible';
                
                if (nameElement) {
                    nameElement.textContent = '🧪 Test Chart - Sample Data';
                }
                
                // Destroy existing chart
                if (window.testChart) {
                    window.testChart.destroy();
                }
                
                // Create test chart with sample data
                const ctx = canvas.getContext('2d');
                window.testChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: [2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030],
                        datasets: [{
                            label: 'Test Country - Predicted Access (%)',
                            data: [85.5, 87.2, 88.9, 90.1, 91.3, 92.5, 93.2, 94.0, 94.8, 95.5],
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
                            legend: { 
                                display: true,
                                position: 'top'
                            },
                            title: {
                                display: true,
                                text: '🧪 TEST CHART - This proves the chart can work!',
                                font: { size: 16, weight: 'bold' }
                            }
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                max: 100,
                                title: { 
                                    display: true, 
                                    text: 'Access (%)'
                                }
                            },
                            x: {
                                title: { 
                                    display: true, 
                                    text: 'Year'
                                }
                            }
                        }
                    }
                });
                
                document.getElementById('testResult').innerHTML = '✅ Test chart created! If you see a chart above, the system works.';
                console.log('✅ [FORCE-TEST] Test chart created successfully!');
                
            } catch (error) {
                console.error('❌ [FORCE-TEST] Error:', error);
                document.getElementById('testResult').innerHTML = '❌ Error: ' + error.message;
            }
        }'''

# Add the function before loadCombinedData
load_combined_pos = content.find('function loadCombinedData(country) {')
if load_combined_pos != -1:
    content = content[:load_combined_pos] + force_test_function + '\n        ' + content[load_combined_pos:]
    print("✅ Added forceTestChart function")

# Also add a simple auto-test on page load
auto_test_code = '''            // Auto-test: Try to create a test chart after 3 seconds
            setTimeout(() => {
                console.log('🔄 [AUTO-TEST] Running automatic chart test...');
                const section = document.getElementById('predictionsSection');
                if (section) {
                    section.style.display = 'block';
                    console.log('✅ [AUTO-TEST] Predictions section made visible');
                }
            }, 3000);'''

# Add after the existing window.onload
onload_pos = content.find('window.onload = function() {')
if onload_pos != -1:
    closing_brace = content.find('};', onload_pos)
    if closing_brace != -1:
        content = content[:closing_brace] + auto_test_code + '\n        ' + content[closing_brace:]
        print("✅ Added auto-test code")

# Write the updated file
with open('sustainable_energy/dashboard/templates/dashboard/objective5_classification.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n🎉 VISIBILITY FIX APPLIED!")
print("\n📋 What was added:")
print("   ✅ Force-visible CSS for chart containers")
print("   ✅ Debug test button to force create chart")
print("   ✅ Test function with sample data")
print("   ✅ Auto-test on page load")
print("   ✅ Enhanced visibility controls")

print("\n🔄 How to test:")
print("   1. Restart Django server")
print("   2. Open http://localhost:8000/objective5/")
print("   3. You'll see a yellow debug section")
print("   4. Click 'Force Create Test Chart' button")
print("   5. If test chart appears, the system works!")
print("   6. Then try selecting a country normally")

print("\n💡 This will help identify if the issue is:")
print("   - Chart.js not loading")
print("   - Canvas element not found")
print("   - CSS visibility problems")
print("   - JavaScript errors")

print("\n🎯 Expected result:")
print("   The test button should create a chart with sample data")
print("   If that works, the real API data should work too!")