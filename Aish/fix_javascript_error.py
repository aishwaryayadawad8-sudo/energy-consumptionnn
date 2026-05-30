"""
Fix JavaScript error by removing references to deleted metric cards
"""

def fix_javascript():
    # Read the index.html file
    with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Remove the lines that try to update electricityAccess and cleanCooking
    old_js = '''            // Update metrics
            document.getElementById('electricityAccess').textContent = 
                data.electricity_access ? data.electricity_access.toFixed(1) : 'N/A';
            document.getElementById('cleanCooking').textContent = 
                data.clean_cooking_access ? data.clean_cooking_access.toFixed(1) : 'N/A';
            document.getElementById('renewableShare').textContent = 
                data.renewable_share ? data.renewable_share.toFixed(1) : 'N/A';
            document.getElementById('co2Emissions').textContent = 
                data.co2_emissions ? data.co2_emissions.toFixed(0) : 'N/A';'''
    
    new_js = '''            // Update metrics
            document.getElementById('renewableShare').textContent = 
                data.renewable_share ? data.renewable_share.toFixed(1) : 'N/A';
            document.getElementById('co2Emissions').textContent = 
                data.co2_emissions ? data.co2_emissions.toFixed(0) : 'N/A';'''
    
    if old_js in content:
        content = content.replace(old_js, new_js)
        
        # Write back
        with open('sustainable_energy/dashboard/templates/dashboard/index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Fixed JavaScript error!")
        print("🔧 Removed references to deleted electricityAccess and cleanCooking elements")
        print("📊 The dashboard should now work without errors")
        return True
    else:
        print("❌ Could not find the JavaScript code to fix")
        return False

if __name__ == '__main__':
    fix_javascript()
