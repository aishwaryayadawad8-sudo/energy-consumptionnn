#!/usr/bin/env python3
"""
Debug Objective 5 chart loading issue
"""

def debug_objective5_chart():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective5_classification.html"
    
    print("🔧 Debugging Objective 5 chart loading issue...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add comprehensive debugging to the loadModelComparison function
        debug_js = '''        function loadModelComparison() {
            console.log('🚀 [DEBUG] Starting loadModelComparison...');
            
            // Check if canvas exists
            const canvas = document.getElementById('mseChart');
            if (!canvas) {
                console.error('❌ [DEBUG] Canvas element #mseChart not found!');
                alert('Canvas element not found!');
                return;
            }
            console.log('✅ [DEBUG] Canvas element found:', canvas);
            
            // Check if Chart.js is loaded
            if (typeof Chart === 'undefined') {
                console.error('❌ [DEBUG] Chart.js not loaded!');
                alert('Chart.js library not loaded!');
                return;
            }
            console.log('✅ [DEBUG] Chart.js loaded successfully');
            
            console.log('📡 [DEBUG] Fetching model comparison data...');
            
            fetch('/api/objective5/model-comparison/')
                .then(response => {
                    console.log('📊 [DEBUG] Response status:', response.status);
                    if (!response.ok) {
                        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('📋 [DEBUG] Model comparison data received:', data);
                    
                    if (data.error) {
                        console.error('❌ [DEBUG] Server error:', data.error);
                        alert('Server error: ' + data.error);
                        return;
                    }
                    
                    if (!data.success) {
                        console.error('❌ [DEBUG] API returned success=false');
                        alert('API returned success=false');
                        return;
                    }
                    
                    if (!data.mse_scores) {
                        console.error('❌ [DEBUG] No mse_scores in response');
                        alert('No model scores in response');
                        return;
                    }
                    
                    console.log('✅ [DEBUG] Data validation passed');
                    
                    // Update section title with correct metric
                    const sectionTitle = document.querySelector('.section-title');
                    if (sectionTitle) {
                        sectionTitle.innerHTML = `<i class="fas fa-trophy"></i> Energy Equity Analysis - Model Comparison (${data.metric})`;
                        console.log('✅ [DEBUG] Section title updated');
                    }
                    
                    // Update description
                    const metricText = data.task_type === 'classification' ? 'Higher is Better' : 'Lower is Better';
                    const description = document.querySelector('.text-muted');
                    if (description) {
                        description.textContent = `${metricText} - ${data.objective_name}`;
                        console.log('✅ [DEBUG] Description updated');
                    }
                    
                    // Get canvas context
                    const ctx = canvas.getContext('2d');
                    if (!ctx) {
                        console.error('❌ [DEBUG] Could not get canvas context');
                        alert('Could not get canvas context');
                        return;
                    }
                    console.log('✅ [DEBUG] Canvas context obtained');
                    
                    // Destroy existing chart
                    if (mseChart) {
                        console.log('🗑️ [DEBUG] Destroying existing chart');
                        mseChart.destroy();
                    }
                    
                    const models = Object.keys(data.mse_scores);
                    const scoreValues = Object.values(data.mse_scores);
                    
                    console.log('📊 [DEBUG] Models:', models);
                    console.log('📊 [DEBUG] Scores:', scoreValues);
                    console.log('🏆 [DEBUG] Best model:', data.best_model);
                    
                    // Create colors array - highlight best model in gold
                    const colors = models.map(model => 
                        model === data.best_model ? 'rgba(255, 215, 0, 0.8)' : 'rgba(102, 126, 234, 0.7)'
                    );
                    const borderColors = models.map(model => 
                        model === data.best_model ? 'rgba(255, 215, 0, 1)' : 'rgba(102, 126, 234, 1)'
                    );
                    
                    console.log('🎨 [DEBUG] Colors configured');
                    
                    try {
                        console.log('🎯 [DEBUG] Creating Chart.js chart...');
                        
                        mseChart = new Chart(ctx, {
                            type: 'bar',
                            data: {
                                labels: models,
                                datasets: [{
                                    label: `${data.metric} Score`,
                                    data: scoreValues,
                                    backgroundColor: colors,
                                    borderColor: borderColors,
                                    borderWidth: 2
                                }]
                            },
                            options: {
                                responsive: true,
                                maintainAspectRatio: false,
                                plugins: {
                                    legend: {
                                        display: false
                                    },
                                    title: {
                                        display: true,
                                        text: `${data.objective_name} - ${data.metric} Comparison (${metricText})`,
                                        font: {
                                            size: 16,
                                            weight: 'bold'
                                        }
                                    },
                                    tooltip: {
                                        callbacks: {
                                            label: function(context) {
                                                const value = context.parsed.y.toFixed(4);
                                                const isBest = context.label === data.best_model;
                                                return `${context.label}: ${value}${isBest ? ' ⭐ (Best)' : ''}`;
                                            }
                                        }
                                    }
                                },
                                scales: {
                                    y: {
                                        beginAtZero: true,
                                        title: {
                                            display: true,
                                            text: data.metric
                                        }
                                    },
                                    x: {
                                        title: {
                                            display: true,
                                            text: 'Machine Learning Models'
                                        }
                                    }
                                }
                            }
                        });
                        
                        console.log('🎉 [DEBUG] Chart created successfully!');
                        console.log('📊 [DEBUG] Chart object:', mseChart);
                        
                    } catch (chartError) {
                        console.error('❌ [DEBUG] Chart creation error:', chartError);
                        alert('Chart creation failed: ' + chartError.message);
                    }
                })
                .catch(error => {
                    console.error('❌ [DEBUG] Fetch error:', error);
                    alert('Error loading model comparison: ' + error.message);
                });
        }'''
        
        # Find and replace the existing loadModelComparison function
        import re
        pattern = r'function loadModelComparison\(\) \{.*?(?=function|\s*</script>)'
        
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, debug_js + '\n\n        ', content, flags=re.DOTALL)
            
            # Write back the updated content
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ Debug version of loadModelComparison function applied!")
            print("📝 Added comprehensive debugging:")
            print("   - Canvas element validation")
            print("   - Chart.js library check")
            print("   - API response validation")
            print("   - Chart creation error handling")
            print("   - Console logging at each step")
            print("🔄 Please refresh your browser and check the console (F12)")
            
        else:
            print("❌ Could not find loadModelComparison function to replace")
            
    except FileNotFoundError:
        print(f"❌ Template file not found: {template_path}")
    except Exception as e:
        print(f"❌ Error applying debug fix: {e}")

if __name__ == "__main__":
    debug_objective5_chart()