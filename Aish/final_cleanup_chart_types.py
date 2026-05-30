#!/usr/bin/env python3
"""
Final Cleanup of Chart Type References
=====================================

Remove any remaining Chart Type references from the dashboard.
"""

import os

def final_cleanup():
    """Remove any remaining Chart Type references"""
    
    html_file_path = "Aish/sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🧹 FINAL CLEANUP OF CHART TYPE REFERENCES")
    print("=" * 50)
    
    # Read current file
    with open(html_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove any remaining Chart Type function references
    patterns_to_remove = [
        'function renderComparisonChart(countryName, coords) {\n            const historicalAvg = coords.access;\n            const predictedAvg = Math.min(100, historicalAvg + 8);\n\n            const trace = {\n                x: [\'Historical Average (2000-2020)\', \'Predicted Average (2021-2030)\'],\n                y: [historicalAvg, predictedAvg],\n                type: \'bar\',\n                marker: { \n                    color: [\'#3498db\', \'#27ae60\'],\n                    opacity: 0.8\n                }\n            };\n\n            const layout = {\n                title: `${countryName} - Historical vs Predicted Comparison`,\n                xaxis: { title: \'Period\' },\n                yaxis: { title: \'Electricity Access (%)\' }\n            };\n\n            Plotly.newPlot(\'mainChart\', [trace], layout, { responsive: true });\n        }',
        'renderComparisonChart',
        'Historical vs Predicted'
    ]
    
    changes_made = 0
    for pattern in patterns_to_remove:
        if pattern in content:
            content = content.replace(pattern, '')
            changes_made += 1
            print(f"✅ Removed: {pattern[:50]}...")
    
    if changes_made == 0:
        print("✅ No Chart Type references found - already clean")
    
    # Write the cleaned content
    try:
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Final cleanup complete - {changes_made} changes made")
        return True
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False

if __name__ == "__main__":
    final_cleanup()