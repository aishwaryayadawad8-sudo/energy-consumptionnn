"""
Add loading indicator to Comprehensive ML Model Comparison page
"""

def add_loading_indicator():
    # Read the file
    with open('sustainable_energy/dashboard/templates/dashboard/comprehensive_comparison.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Add loading overlay HTML after the header section
    loading_html = '''        
        <!-- Loading Overlay -->
        <div id="loadingOverlay" class="loading-overlay" style="display: none;">
            <div class="loading-content">
                <div class="spinner-border text-primary" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
                <h3 class="mt-4">Running Analysis...</h3>
                <p class="text-muted">Comparing 7 ML models across all 8 objectives</p>
                <div class="progress mt-3" style="width: 300px;">
                    <div id="progressBar" class="progress-bar progress-bar-striped progress-bar-animated" 
                         role="progressbar" style="width: 0%"></div>
                </div>
            </div>
        </div>
        
        <!-- Summary Section -->'''
    
    # Replace the summary section marker
    content = content.replace('        <!-- Summary Section -->', loading_html)
    
    # Update the runComparison function to show/hide loading
    old_function = '''        async function runComparison() {
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
    
    new_function = '''        async function runComparison() {
            // Show loading overlay
            const loadingOverlay = document.getElementById('loadingOverlay');
            const progressBar = document.getElementById('progressBar');
            loadingOverlay.style.display = 'flex';
            
            // Clear previous results
            document.getElementById('resultsContainer').innerHTML = '';
            document.getElementById('summarySection').style.display = 'none';
            
            // Simulate progress
            let progress = 0;
            const progressInterval = setInterval(() => {
                progress += 5;
                if (progress <= 90) {
                    progressBar.style.width = progress + '%';
                }
            }, 200);
            
            try {
                const response = await fetch('/api/comprehensive-comparison/');
                const data = await response.json();
                
                // Complete progress
                clearInterval(progressInterval);
                progressBar.style.width = '100%';
                
                // Small delay to show 100%
                await new Promise(resolve => setTimeout(resolve, 300));
                
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
                // Hide loading overlay
                loadingOverlay.style.display = 'none';
                progressBar.style.width = '0%';
            }
        }'''
    
    if old_function in content:
        content = content.replace(old_function, new_function)
        
        # Write back
        with open('sustainable_energy/dashboard/templates/dashboard/comprehensive_comparison.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully added loading indicator!")
        print("📊 Features added:")
        print("   - Loading overlay with spinner")
        print("   - 'Running Analysis...' message")
        print("   - Progress bar animation")
        print("   - Auto-hides when analysis completes")
        return True
    else:
        print("❌ Could not find the runComparison function")
        return False

if __name__ == '__main__':
    add_loading_indicator()
