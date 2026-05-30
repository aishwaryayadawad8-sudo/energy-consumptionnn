#!/usr/bin/env python3
"""
Create a fixed version of Objective 5 with proper predictions chart
"""

# Read the current file
with open('sustainable_energy/dashboard/templates/dashboard/objective5.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Find the problematic loadPredictions function and replace it
old_start = "function loadPredictions(country) {"
old_end = "                .catch(error => console.error('Error loading countries:', error));"

# Find the start and end positions
start_pos = content.find(old_start)
if start_pos == -1:
    print("Could not find loadPredictions function")
    exit(1)

# Find the end position by looking for the specific error message
end_pos = content.find(old_end, start_pos)
if end_pos == -1:
    print("Could not find end of loadPredictions function")
    exit(1)

# Include the closing brace and whitespace
end_pos = content.find("        }", end_pos) + len("        }")

# Extract the old function
old_function = content[start_pos:end_pos]

# Define the new function
new_function = """function loadPredictions(country) {
            console.log('Loading predictions for:', country);
            fetch(`/api/objective5/predictions/?country=${encodeURIComponent(country)}&years=10`)
                .then(response => response.json())
                .then(data => {
                    console.log('Predictions data received:', data);
                    if (data.success && data.predictions.length > 0) {
                        document.getElementById('predictionsSection').style.display = 'block';
                        document.getElementById('predictionsCountryName').textContent = `Future predictions for ${country}`;
                        const ctx = document.getElementById('predictionsChart').getContext('2d');
                        if (predictionsChart) predictionsChart.destroy();
                        
                        console.log('Rendering predictions:', data.predictions); // DEBUG
                        
                        predictionsChart = new Chart(ctx, {
                            type: 'line',
                            data: {
                                labels: data.predictions.map(d => d.year),
                                datasets: [{
                                    label: `${country} - Predicted Access (%)`,
                                    data: data.predictions.map(d => d.predicted_access),
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
                                        position: 'top',
                                        labels: {
                                            font: { size: 14, weight: 'bold' },
                                            padding: 15
                                        }
                                    },
                                    title: {
                                        display: true,
                                        text: `Future Predictions - ${country}`,
                                        font: { size: 16, weight: 'bold' },
                                        padding: 20
                                    }
                                },
                                scales: {
                                    y: {
                                        beginAtZero: true,
                                        max: 100,
                                        title: { 
                                            display: true, 
                                            text: 'Access (%)',
                                            font: { size: 14, weight: 'bold' }
                                        },
                                        grid: { color: 'rgba(0, 0, 0, 0.1)' }
                                    },
                                    x: {
                                        title: { 
                                            display: true, 
                                            text: 'Year',
                                            font: { size: 14, weight: 'bold' }
                                        },
                                        grid: { color: 'rgba(0, 0, 0, 0.1)' }
                                    }
                                }
                            }
                        });
                    } else {
                        console.error('No predictions data available for', country);
                    }
                })
                .catch(error => console.error('Error loading predictions:', error));
        }"""

# Replace the function
new_content = content[:start_pos] + new_function + content[end_pos:]

# Write the updated content
with open('sustainable_energy/dashboard/templates/dashboard/objective5.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Successfully fixed Objective 5 predictions chart!")
print("\n📋 Changes made:")
print("   - Fixed API endpoint: /api/objective5/predictions/")
print("   - Now loads individual country predictions")
print("   - Added proper data mapping")
print("   - Added debug console logging")
print("   - Improved chart styling")
print("\n🔄 Next steps:")
print("   1. Restart Django server")
print("   2. Open http://localhost:8000/objective5/")
print("   3. Select a country and click 'Analyze Country'")
print("   4. Check browser console for debug messages")