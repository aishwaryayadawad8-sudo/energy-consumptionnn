#!/usr/bin/env python3
"""Remove the loading overlay from ML Comparison - load models silently in background"""

# Read the file
with open('sustainable_energy/dashboard/templates/dashboard/comprehensive_comparison.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the loading overlay display logic
old_loading_code = '''        async function runComparison() {
            // Show loading
            document.getElementById('loadingOverlay').style.display = 'flex';
            document.getElementById('resultsContainer').innerHTML = '';
            document.getElementById('summarySection').style.display = 'none';
            
            // Simulate progress
            let progress = 0;
            const progressInterval = setInterval(() => {
                progress += 2;
                if (progress >= 90) {
                    clearInterval(progressInterval);
                }
                document.getElementById('progressBar').style.width = progress + '%';
            }, 200);
            
            try {
                const response = await fetch('/api/comprehensive-comparison/');
                const data = await response.json();
                
                clearInterval(progressInterval);
                document.getElementById('progressBar').style.width = '100%';
                
                if (data.success) {
                    displayResults(data);
                    displaySummary(data.summary);
                } else {
                    alert('Error: ' + data.error);
                }
            } catch (error) {
                clearInterval(progressInterval);
                alert('Error running comparison: ' + error.message);
            } finally {
                setTimeout(() => {
                    document.getElementById('loadingOverlay').style.display = 'none';
                }, 500);
            }
        }'''

new_loading_code = '''        async function runComparison() {
            // Load silently in background - no loading overlay
            document.getElementById('resultsContainer').innerHTML = '';
            document.getElementById('summarySection').style.display = 'none';
            
            try {
                const response = await fetch('/api/comprehensive-comparison/');
                const data = await response.json();
                
                if (data.success) {
                    displayResults(data);
                    displaySummary(data.summary);
                } else {
                    alert('Error: ' + data.error);
                }
            } catch (error) {
                alert('Error running comparison: ' + error.message);
            }
        }'''

# Replace
content = content.replace(old_loading_code, new_loading_code)

# Also hide the loading overlay element completely by setting display: none permanently
old_overlay_html = '''        <!-- Loading Overlay -->
        <div id="loadingOverlay" class="loading-overlay" style="display: none;">
            <div class="loading-content">
                <div class="spinner-border text-primary" role="status"></div>
                <h3 class="mt-3">Running Comprehensive Analysis...</h3>
                <p class="text-muted">Training 7 ML models across 8 objectives<br>This may take 1-2 minutes</p>
                <div class="progress mt-3" style="width: 300px;">
                    <div id="progressBar" class="progress-bar progress-bar-striped progress-bar-animated" 
                         role="progressbar" style="width: 0%"></div>
                </div>
            </div>
        </div>'''

new_overlay_html = '''        <!-- Loading Overlay - Hidden (models load in background) -->
        <div id="loadingOverlay" class="loading-overlay" style="display: none !important;">
        </div>'''

content = content.replace(old_overlay_html, new_overlay_html)

# Write back
with open('sustainable_energy/dashboard/templates/dashboard/comprehensive_comparison.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Loading overlay removed!")
print("🚀 Models will now load automatically in the background")
print("⚡ No more 'Running Comprehensive Analysis' delay screen")
print("📊 Results will appear directly when ready")
