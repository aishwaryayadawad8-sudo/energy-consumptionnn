"""
Add an alert at the start of loadCountryData to verify it's being called
"""

def add_alert():
    with open('sustainable_energy/dashboard/templates/dashboard/objective1.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    old_start = '''        function loadCountryData() {
            const country = document.getElementById('countrySelect').value;
            if (!country) {
                alert('Please select a country');
                return;
            }
            
            console.log('Loading data for:', country);'''
    
    new_start = '''        function loadCountryData() {
            alert('loadCountryData function called!');
            const country = document.getElementById('countrySelect').value;
            console.log('Selected country:', country);
            if (!country) {
                alert('Please select a country');
                return;
            }
            
            console.log('Loading data for:', country);'''
    
    if old_start in content:
        content = content.replace(old_start, new_start)
        
        with open('sustainable_energy/dashboard/templates/dashboard/objective1.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Added alert for testing")
        print("Now when you click 'Load Data', you should see an alert")
        print("This will confirm the function is being called")
        return True
    
    print("❌ Could not find the function start")
    return False

if __name__ == '__main__':
    add_alert()
