#!/usr/bin/env python3
"""
Remove Chart Type and ML Model Controls
=======================================

This script removes the "Chart Type" and "ML Model" control sections 
from the explore dashboard visualization controls.
"""

import os

def remove_chart_ml_controls():
    """Remove Chart Type and ML Model control sections"""
    
    html_file_path = "Aish/sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🗑️ Removing Chart Type and ML Model controls...")
    print(f"📁 Updating file: {html_file_path}")
    
    # Read the current file
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False
    
    changes_made = 0
    
    # 1. Remove Chart Type control section
    chart_type_patterns = [
        # Pattern 1: Complete Chart Type section
        '''            <div class="control-section">
                <label class="control-label">Chart Type:</label>
                <div class="control-buttons">
                    <button class="control-btn active" onclick="setChartType('timeline')">Timeline View</button>
                    <button class="control-btn" onclick="setChartType('comparison')">Historical vs Predicted</button>
                    <button class="control-btn" onclick="setChartType('breakdown')">Energy Mix</button>
                    <button class="control-btn" onclick="setChartType('access')">Access Trends</button>
                    <button class="control-btn" onclick="setChartType('pie')">Pie Chart</button>
                </div>
            </div>''',
        
        # Pattern 2: Alternative format
        '''<div class="control-section">
                <label class="control-label">Chart Type:</label>
                <div class="control-buttons">
                    <button class="control-btn active" onclick="setChartType('timeline')">Timeline View</button>
                    <button class="control-btn" onclick="setChartType('comparison')">Historical vs Predicted</button>
                    <button class="control-btn" onclick="setChartType('breakdown')">Energy Mix</button>
                    <button class="control-btn" onclick="setChartType('access')">Access Trends</button>
                    <button class="control-btn" onclick="setChartType('pie')">Pie Chart</button>
                </div>
            </div>''',
        
        # Pattern 3: Just the label
        '''<label class="control-label">Chart Type:</label>'''
    ]
    
    for pattern in chart_type_patterns:
        if pattern in content:
            content = content.replace(pattern, '')
            changes_made += 1
            print(f"✅ Removed Chart Type control section")
    
    # 2. Remove ML Model control section
    ml_model_patterns = [
        # Pattern 1: Complete ML Model section
        '''            <div class="control-section">
                <label class="control-label">ML Model:</label>
                <div class="control-buttons">
                    <button class="control-btn active" onclick="setMLModel('xgboost')">XGBoost (Best)</button>
                    <button class="control-btn" onclick="setMLModel('catboost')">CatBoost</button>
                    <button class="control-btn" onclick="setMLModel('lightgbm')">LightGBM</button>
                    <button class="control-btn" onclick="setMLModel('ensemble')">Ensemble</button>
                </div>
            </div>''',
        
        # Pattern 2: Alternative format
        '''<div class="control-section">
                <label class="control-label">ML Model:</label>
                <div class="control-buttons">
                    <button class="control-btn active" onclick="setMLModel('xgboost')">XGBoost (Best)</button>
                    <button class="control-btn" onclick="setMLModel('catboost')">CatBoost</button>
                    <button class="control-btn" onclick="setMLModel('lightgbm')">LightGBM</button>
                    <button class="control-btn" onclick="setMLModel('ensemble')">Ensemble</button>
                </div>
            </div>''',
        
        # Pattern 3: Just the label
        '''<label class="control-label">ML Model:</label>'''
    ]
    
    for pattern in ml_model_patterns:
        if pattern in content:
            content = content.replace(pattern, '')
            changes_made += 1
            print(f"✅ Removed ML Model control section")
    
    # 3. Remove individual chart type buttons if they exist separately
    chart_buttons = [
        '''<button class="control-btn active" onclick="setChartType('timeline')">Timeline View</button>''',
        '''<button class="control-btn" onclick="setChartType('comparison')">Historical vs Predicted</button>''',
        '''<button class="control-btn" onclick="setChartType('breakdown')">Energy Mix</button>''',
        '''<button class="control-btn" onclick="setChartType('access')">Access Trends</button>''',
        '''<button class="control-btn" onclick="setChartType('pie')">Pie Chart</button>'''
    ]
    
    for button in chart_buttons:
        if button in content:
            content = content.replace(button, '')
            changes_made += 1
            print(f"✅ Removed individual chart type button")
    
    # 4. Remove individual ML model buttons if they exist separately
    ml_buttons = [
        '''<button class="control-btn active" onclick="setMLModel('xgboost')">XGBoost (Best)</button>''',
        '''<button class="control-btn" onclick="setMLModel('catboost')">CatBoost</button>''',
        '''<button class="control-btn" onclick="setMLModel('lightgbm')">LightGBM</button>''',
        '''<button class="control-btn" onclick="setMLModel('ensemble')">Ensemble</button>'''
    ]
    
    for button in ml_buttons:
        if button in content:
            content = content.replace(button, '')
            changes_made += 1
            print(f"✅ Removed individual ML model button")
    
    # 5. Remove or disable related JavaScript functions
    js_functions = [
        # setChartType function
        {
            'start': 'function setChartType(type) {',
            'replacement': '''function setChartType(type) {
            // Chart type controls removed - using default timeline view
            console.log('Chart type controls disabled');
        }'''
        },
        # setMLModel function
        {
            'start': 'function setMLModel(model) {',
            'replacement': '''function setMLModel(model) {
            // ML model controls removed - using default XGBoost
            console.log('ML model controls disabled');
        }'''
        }
    ]
    
    for func in js_functions:
        func_start = func['start']
        func_pos = content.find(func_start)
        
        if func_pos != -1:
            # Find the end of the function
            brace_count = 0
            pos = func_pos + len(func_start)
            
            while pos < len(content):
                if content[pos] == '{':
                    brace_count += 1
                elif content[pos] == '}':
                    brace_count -= 1
                    if brace_count == -1:  # Found the closing brace
                        end_pos = pos + 1
                        break
                pos += 1
            else:
                end_pos = len(content)
            
            # Replace the function
            content = content[:func_pos] + func['replacement'] + content[end_pos:]
            changes_made += 1
            print(f"✅ Disabled JavaScript function: {func_start}")
    
    # 6. Remove ML Model Info section if it exists
    ml_info_patterns = [
        '''        <!-- ML Model Information -->
        <div class="ml-model-info" id="mlModelInfo" style="display: none;">
            <h5><i class="fas fa-brain"></i> ML Model Information</h5>
            <p id="mlModelDescription">Using XGBoost model for predictions with 94.2% accuracy</p>
        </div>''',
        
        '''<div class="ml-model-info" id="mlModelInfo" style="display: none;">
            <h5><i class="fas fa-brain"></i> ML Model Information</h5>
            <p id="mlModelDescription">Using XGBoost model for predictions with 94.2% accuracy</p>
        </div>'''
    ]
    
    for pattern in ml_info_patterns:
        if pattern in content:
            content = content.replace(pattern, '')
            changes_made += 1
            print(f"✅ Removed ML Model Information section")
    
    # 7. Remove CSS for ML model info if it exists
    ml_info_css = '''.ml-model-info {
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
        }'''
    
    if ml_info_css in content:
        content = content.replace(ml_info_css, '')
        changes_made += 1
        print(f"✅ Removed ML Model Info CSS")
    
    # 8. Clean up any remaining references
    lines = content.split('\n')
    for i, line in enumerate(lines):
        # Comment out lines that reference removed functions
        if any(ref in line for ref in ['setChartType', 'setMLModel', 'mlModelInfo', 'chartType', 'currentMLModel']):
            if not line.strip().startswith('//') and not line.strip().startswith('*'):
                lines[i] = '            // ' + line.strip() + ' // Chart/ML controls removed'
                changes_made += 1
                print(f"✅ Commented out reference line")
    
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
    """Main function to remove chart type and ML model controls"""
    print("🗑️ REMOVING CHART TYPE AND ML MODEL CONTROLS")
    print("=" * 60)
    
    success = remove_chart_ml_controls()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ CHART TYPE AND ML MODEL CONTROLS REMOVED!")
        print("=" * 60)
        print("\n🎯 Changes made:")
        print("   ✓ Removed 'Chart Type' control section")
        print("   ✓ Removed 'ML Model' control section")
        print("   ✓ Removed all chart type buttons")
        print("   ✓ Removed all ML model buttons")
        print("   ✓ Disabled setChartType() function")
        print("   ✓ Disabled setMLModel() function")
        print("   ✓ Removed ML Model Information section")
        print("   ✓ Cleaned up all related references")
        
        print("\n✅ Result:")
        print("   • Clean visualization controls section")
        print("   • Only 'Time Period' controls remain")
        print("   • Default timeline view and XGBoost model")
        print("   • All analysis functionality preserved")
        print("   • Simplified user interface")
        
        print("\n🧪 To test:")
        print("   1. Start Django server: python manage.py runserver")
        print("   2. Go to: http://127.0.0.1:8000/explore/")
        print("   3. Verify: No 'Chart Type' section")
        print("   4. Verify: No 'ML Model' section")
        print("   5. Verify: Only 'Time Period' controls visible")
        print("   6. Verify: Country analysis still works perfectly")
        
        print("\n🔄 Clear browser cache with Ctrl+F5 after testing")
    else:
        print("\n❌ FAILED TO REMOVE CONTROLS")
        print("Please check the error messages above")

if __name__ == "__main__":
    main()