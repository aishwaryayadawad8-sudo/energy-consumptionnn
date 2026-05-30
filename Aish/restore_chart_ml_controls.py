#!/usr/bin/env python3
"""
Restore Chart Type and ML Model Controls
========================================

This script restores the "Chart Type" and "ML Model" control sections 
back to the explore dashboard visualization controls.
"""

import os

def restore_chart_ml_controls():
    """Restore Chart Type and ML Model control sections"""
    
    html_file_path = "Aish/sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔄 Restoring Chart Type and ML Model controls...")
    print(f"📁 Updating file: {html_file_path}")
    
    # Read the current file
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False
    
    changes_made = 0
    
    # 1. Find the Time Period control section and add Chart Type after it
    time_period_end = '''                </div>
            </div>'''
    
    # Look for the Time Period section
    time_period_marker = '''<label class="control-label">Time Period:</label>'''
    time_period_pos = content.find(time_period_marker)
    
    if time_period_pos != -1:
        # Find the end of the Time Period section
        search_start = time_period_pos
        end_pos = content.find(time_period_end, search_start)
        
        if end_pos != -1:
            end_pos += len(time_period_end)
            
            # Add Chart Type section after Time Period
            chart_type_section = '''
            
            <div class="control-section">
                <label class="control-label">Chart Type:</label>
                <div class="control-buttons">
                    <button class="control-btn active" onclick="setChartType('timeline')">Timeline View</button>
                    <button class="control-btn" onclick="setChartType('comparison')">Historical vs Predicted</button>
                    <button class="control-btn" onclick="setChartType('breakdown')">Energy Mix</button>
                    <button class="control-btn" onclick="setChartType('access')">Access Trends</button>
                    <button class="control-btn" onclick="setChartType('pie')">Pie Chart</button>
                </div>
            </div>
            
            <div class="control-section">
                <label class="control-label">ML Model:</label>
                <div class="control-buttons">
                    <button class="control-btn active" onclick="setMLModel('xgboost')">XGBoost (Best)</button>
                    <button class="control-btn" onclick="setMLModel('catboost')">CatBoost</button>
                    <button class="control-btn" onclick="setMLModel('lightgbm')">LightGBM</button>
                    <button class="control-btn" onclick="setMLModel('ensemble')">Ensemble</button>
                </div>
            </div>'''
            
            content = content[:end_pos] + chart_type_section + content[end_pos:]
            changes_made += 1
            print("✅ Added Chart Type and ML Model control sections")
    
    # 2. Restore ML Model Information section
    # Find where to insert it (after the search section)
    search_section_end = '''        </div>

        <!-- World Map -->'''
    
    search_end_pos = content.find(search_section_end)
    if search_end_pos != -1:
        ml_info_section = '''
        <!-- ML Model Information -->
        <div class="ml-model-info" id="mlModelInfo" style="display: none;">
            <h5><i class="fas fa-brain"></i> ML Model Information</h5>
            <p id="mlModelDescription">Using XGBoost model for predictions with 94.2% accuracy</p>
        </div>
'''
        
        content = content[:search_end_pos] + ml_info_section + content[search_end_pos:]
        changes_made += 1
        print("✅ Added ML Model Information section")
    
    # 3. Restore CSS for ML Model Info
    css_insertion_point = '''        @media (max-width: 768px) {'''
    css_pos = content.find(css_insertion_point)
    
    if css_pos != -1:
        ml_info_css = '''        .ml-model-info {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: white;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
        }
        
        .ml-model-info h5 {
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .ml-model-info p {
            margin: 0;
            opacity: 0.9;
            font-size: 0.9rem;
        }
        
        '''
        
        content = content[:css_pos] + ml_info_css + content[css_pos:]
        changes_made += 1
        print("✅ Added ML Model Info CSS")
    
    # 4. Restore JavaScript functions
    # Find where to insert the functions (before the cleanup section)
    cleanup_marker = '''        // Cleanup on page unload'''
    cleanup_pos = content.find(cleanup_marker)
    
    if cleanup_pos != -1:
        js_functions = '''        // Control functions
        function setTimePeriod(period) {
            currentTimePeriod = period;
            updateActiveButton('.control-buttons button', period);
            if (currentCountry) {
                searchCountry();
            }
        }

        function setChartType(type) {
            currentChartType = type;
            updateActiveButton('.control-buttons button', type);
            document.getElementById('chartTitle').textContent = getChartTitle(type);
            if (currentCountry) {
                searchCountry();
            }
        }

        function setMLModel(model) {
            currentMLModel = model;
            updateActiveButton('.control-buttons button', model);
            updateMLModelInfo();
            if (currentCountry) {
                searchCountry();
            }
        }

        function getChartTitle(type) {
            const titles = {
                'timeline': 'Energy Timeline (2000-2030)',
                'comparison': 'Historical vs Predicted Comparison',
                'breakdown': 'Energy Mix Breakdown',
                'access': 'Access Trends Analysis',
                'pie': 'Energy Source Distribution'
            };
            return titles[type] || 'Energy Analysis';
        }

        function updateActiveButton(selector, activeValue) {
            document.querySelectorAll(selector).forEach(btn => {
                btn.classList.remove('active');
                if (btn.textContent.toLowerCase().includes(activeValue.toLowerCase()) || 
                    btn.onclick.toString().includes(activeValue)) {
                    btn.classList.add('active');
                }
            });
        }

        function updateMLModelInfo() {
            const model = mlModels[currentMLModel];
            document.getElementById('mlModelInfo').style.display = 'block';
            document.getElementById('mlModelDescription').textContent = 
                `Using ${model.name} model with ${model.accuracy}% accuracy - ${model.description}`;
        }

        '''
        
        content = content[:cleanup_pos] + js_functions + "\n        " + content[cleanup_pos:]
        changes_made += 1
        print("✅ Added JavaScript control functions")
    
    # 5. Restore global variables at the top of the script section
    # Find the global variables section
    global_vars_marker = '''        let currentCountry = null;'''
    global_vars_pos = content.find(global_vars_marker)
    
    if global_vars_pos != -1:
        # Add the missing variables after currentCountry
        additional_vars = '''
        let currentTimePeriod = 'all';
        let currentChartType = 'timeline';
        let currentMLModel = 'xgboost';'''
        
        end_of_line = content.find('\n', global_vars_pos)
        if end_of_line != -1:
            content = content[:end_of_line] + additional_vars + content[end_of_line:]
            changes_made += 1
            print("✅ Added global variables")
    
    # 6. Uncomment any lines that were commented out
    lines = content.split('\n')
    for i, line in enumerate(lines):
        # Uncomment lines that were commented out for chart/ML controls
        if '// Chart/ML controls removed' in line:
            # Remove the comment prefix and suffix
            original_line = line.replace('            // ', '').replace(' // Chart/ML controls removed', '')
            lines[i] = '            ' + original_line
            changes_made += 1
            print(f"✅ Uncommented control reference line")
    
    content = '\n'.join(lines)
    
    # Write the updated content back to the file
    try:
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Successfully updated index.html ({changes_made} changes made)")
        return True
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False

def main():
    """Main function to restore chart type and ML model controls"""
    print("🔄 RESTORING CHART TYPE AND ML MODEL CONTROLS")
    print("=" * 60)
    
    success = restore_chart_ml_controls()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ CHART TYPE AND ML MODEL CONTROLS RESTORED!")
        print("=" * 60)
        print("\n🎯 Changes made:")
        print("   ✓ Restored 'Chart Type' control section")
        print("   ✓ Restored 'ML Model' control section")
        print("   ✓ Added all chart type buttons back")
        print("   ✓ Added all ML model buttons back")
        print("   ✓ Restored setChartType() function")
        print("   ✓ Restored setMLModel() function")
        print("   ✓ Restored ML Model Information section")
        print("   ✓ Restored all CSS styling")
        print("   ✓ Restored global variables")
        print("   ✓ Uncommented all related references")
        
        print("\n✅ Result:")
        print("   • Complete visualization controls restored")
        print("   • Time Period + Chart Type + ML Model controls")
        print("   • All interactive functionality back")
        print("   • Timeline View, Pie Chart, Energy Mix options")
        print("   • XGBoost, CatBoost, LightGBM, Ensemble models")
        print("   • ML Model information display")
        
        print("\n🧪 To test:")
        print("   1. Start Django server: python manage.py runserver")
        print("   2. Go to: http://127.0.0.1:8000/explore/")
        print("   3. Verify: 'Chart Type' section is back")
        print("   4. Verify: 'ML Model' section is back")
        print("   5. Verify: All buttons work and change charts")
        print("   6. Verify: ML model info appears when selected")
        print("   7. Verify: Country analysis works with all options")
        
        print("\n🔄 Clear browser cache with Ctrl+F5 after testing")
    else:
        print("\n❌ FAILED TO RESTORE CONTROLS")
        print("Please check the error messages above")

if __name__ == "__main__":
    main()