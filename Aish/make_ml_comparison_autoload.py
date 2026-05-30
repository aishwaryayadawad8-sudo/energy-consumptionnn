#!/usr/bin/env python3
"""Make ML Comparison auto-load without button"""

# Read the file
with open('sustainable_energy/dashboard/templates/dashboard/comprehensive_comparison.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the Run button
old_button_section = '''            <button class="btn btn-primary btn-lg mt-3" onclick="runComparison()">
                <i class="fas fa-play"></i> Run Comprehensive Analysis
            </button>
            <a href="/" class="btn btn-secondary btn-lg mt-3 ms-2">'''

new_button_section = '''            <a href="/" class="btn btn-secondary btn-lg mt-3">'''

content = content.replace(old_button_section, new_button_section)

# Add auto-run on page load - find the end of the script section
old_script_end = '''    <script>
        let charts = {};
        
        async function runComparison() {'''

new_script_end = '''    <script>
        let charts = {};
        
        // Auto-run comparison on page load
        window.addEventListener('DOMContentLoaded', function() {
            runComparison();
        });
        
        async function runComparison() {'''

content = content.replace(old_script_end, new_script_end)

# Write back
with open('sustainable_energy/dashboard/templates/dashboard/comprehensive_comparison.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ ML Comparison updated to auto-load!")
print("🔄 Changes made:")
print("   • Removed 'Run Comprehensive Analysis' button")
print("   • Added auto-run on page load")
print("   • Models will load automatically when page opens")
