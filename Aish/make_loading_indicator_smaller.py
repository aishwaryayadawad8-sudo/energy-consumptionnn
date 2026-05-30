"""
Make the loading indicator smaller and more compact
"""

def make_loading_smaller():
    # Read the file
    with open('sustainable_energy/dashboard/templates/dashboard/comprehensive_comparison.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Replace the large loading content with a smaller version
    old_loading = '''        <!-- Loading Overlay -->
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
        </div>'''
    
    new_loading = '''        <!-- Loading Overlay -->
        <div id="loadingOverlay" class="loading-overlay" style="display: none;">
            <div class="loading-content" style="padding: 25px;">
                <div class="spinner-border text-primary" role="status" style="width: 2.5rem; height: 2.5rem;">
                    <span class="visually-hidden">Loading...</span>
                </div>
                <h5 class="mt-3 mb-2">Running Analysis...</h5>
                <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 10px;">Comparing ML models</p>
                <div class="progress" style="width: 200px; height: 8px;">
                    <div id="progressBar" class="progress-bar progress-bar-striped progress-bar-animated" 
                         role="progressbar" style="width: 0%"></div>
                </div>
            </div>
        </div>'''
    
    if old_loading in content:
        content = content.replace(old_loading, new_loading)
        
        # Write back
        with open('sustainable_energy/dashboard/templates/dashboard/comprehensive_comparison.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully made loading indicator smaller!")
        print("📊 Changes:")
        print("   - Reduced padding (40px → 25px)")
        print("   - Smaller spinner (4rem → 2.5rem)")
        print("   - Smaller heading (h3 → h5)")
        print("   - Shorter text")
        print("   - Narrower progress bar (300px → 200px)")
        print("   - Thinner progress bar (default → 8px)")
        return True
    else:
        print("❌ Could not find the loading overlay")
        return False

if __name__ == '__main__':
    make_loading_smaller()
