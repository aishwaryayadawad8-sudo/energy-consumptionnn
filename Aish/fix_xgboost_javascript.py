#!/usr/bin/env python3
"""
Fix the XGBoost alerts JavaScript to provide better feedback
"""

def fix_javascript():
    """Fix the JavaScript function for better user feedback"""
    
    print("🔧 Fixing XGBoost alerts JavaScript...")
    
    with open('sustainable_energy/dashboard/templates/dashboard/admin_panel.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the JavaScript function
    old_js = '''    function sendXGBoostAlerts() {
        if (!confirm('Send XGBoost alerts to all countries with low electricity access?')) {
            return;
        }
        
        fetch('/api/send-xgboost-alerts/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert(`Success! Sent ${data.emails_sent} alerts to countries with low access.`);
            } else {
                alert('Error: ' + data.error);
            }
        })
        .catch(error => {
            alert('Error sending alerts: ' + error);
        });
    }'''
    
    new_js = '''    function sendXGBoostAlerts() {
        if (!confirm('Send XGBoost alerts to all countries with low electricity access?\\n\\nThis will send emails to assowmya649@gmail.com')) {
            return;
        }
        
        // Show loading message
        const button = event.target;
        const originalText = button.innerHTML;
        button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
        button.disabled = true;
        
        console.log('🚀 Starting XGBoost alerts...');
        
        fetch('/api/send-xgboost-alerts/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(response => {
            console.log('📡 Response status:', response.status);
            console.log('📄 Response headers:', response.headers);
            
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }
            
            return response.json();
        })
        .then(data => {
            console.log('📊 Response data:', data);
            
            // Reset button
            button.innerHTML = originalText;
            button.disabled = false;
            
            if (data.success) {
                const message = `🎉 SUCCESS!\\n\\n` +
                    `📧 Emails sent: ${data.emails_sent}\\n` +
                    `📊 Total predictions: ${data.total_predictions}\\n` +
                    `🤖 Model: ${data.model}\\n\\n` +
                    `Countries that received emails:\\n` +
                    data.alerts.map(alert => 
                        `• ${alert.country}: ${alert.status} (${alert.access}%)`
                    ).join('\\n') +
                    `\\n\\nCheck your email: assowmya649@gmail.com`;
                
                alert(message);
            } else {
                alert('❌ Error: ' + (data.error || 'Unknown error'));
            }
        })
        .catch(error => {
            console.error('❌ Error:', error);
            
            // Reset button
            button.innerHTML = originalText;
            button.disabled = false;
            
            alert(`❌ Error sending alerts:\\n\\n${error.message}\\n\\nCheck browser console for details.`);
        });
    }'''
    
    if old_js in content:
        content = content.replace(old_js, new_js)
        print("✅ Updated JavaScript function")
    else:
        print("⚠️ Could not find JavaScript function to replace")
    
    with open('sustainable_energy/dashboard/templates/dashboard/admin_panel.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ JavaScript fix complete!")
    print("\n🎯 Improvements made:")
    print("   ✅ Better confirmation dialog")
    print("   ✅ Loading spinner while sending")
    print("   ✅ Detailed success message")
    print("   ✅ Better error handling")
    print("   ✅ Console logging for debugging")
    print("   ✅ Shows which countries received emails")

if __name__ == "__main__":
    fix_javascript()