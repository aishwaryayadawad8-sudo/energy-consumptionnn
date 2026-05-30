#!/usr/bin/env python3
"""Add customization features to Email Alert System (objective8.html)"""

# Read the file
with open('sustainable_energy/dashboard/templates/dashboard/objective8.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the section to replace
old_section = '''        <!-- Country Selection -->
        <div class="card">
            <div class="card-header">
                <h4><i class="fas fa-globe"></i> Select Countries</h4>
            </div>
            <div class="card-body">
                <div class="mb-4">
                    <label for="countrySelect" class="form-label"><strong>Choose countries to send alerts to:</strong></label>
                    <select id="countrySelect" class="form-control" multiple="multiple" style="width: 100%;">
                        <!-- Countries will be loaded here -->
                    </select>
                    <small class="text-muted">You can select multiple countries. Start typing to search.</small>
                </div>
                
                <div class="d-flex justify-content-between align-items-center flex-wrap gap-2">
                    <div>
                        <button class="btn btn-send-alerts" onclick="sendSelectedAlerts()">
                            <i class="fas fa-paper-plane"></i> Send Alerts to Selected Countries
                        </button>
                    </div>
                    <div>
                        <button class="btn btn-send-all" onclick="sendAllAlerts()">
                            <i class="fas fa-globe-americas"></i> Send to All Countries
                        </button>
                    </div>
                    <div>
                        <button class="btn btn-primary" onclick="sendXGBoostAlertsAuto()" style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); border: none; padding: 12px 30px; border-radius: 50px; font-weight: bold;">
                            <i class="fas fa-robot"></i> 🤖 Auto Send XGBoost Alerts
                        </button>
                    </div>
                </div>
                
                <div id="selectedCount" class="mt-3 text-center">
                    <strong>Selected: <span id="countDisplay">0</span> countries</strong>
                </div>
            </div>
        </div>'''

new_section = '''        <!-- Country Selection -->
        <div class="card">
            <div class="card-header">
                <h4><i class="fas fa-globe"></i> Select Countries</h4>
            </div>
            <div class="card-body">
                <div class="mb-4">
                    <label for="countrySelect" class="form-label"><strong>Choose countries to send alerts to:</strong></label>
                    <select id="countrySelect" class="form-control" multiple="multiple" style="width: 100%;">
                        <!-- Countries will be loaded here -->
                    </select>
                    <small class="text-muted">You can select multiple countries. Start typing to search.</small>
                </div>
                
                <div id="selectedCount" class="mt-3 text-center">
                    <strong>Selected: <span id="countDisplay">0</span> countries</strong>
                </div>
            </div>
        </div>
        
        <!-- Customize Email Message -->
        <div class="card">
            <div class="card-header">
                <h4><i class="fas fa-edit"></i> Customize Email Message (Optional)</h4>
            </div>
            <div class="card-body">
                <!-- Quick Templates -->
                <div class="mb-4" style="background: #f0f8ff; padding: 20px; border-radius: 10px;">
                    <label class="form-label"><i class="fas fa-file-alt"></i> <strong>Quick Templates (Click to use)</strong></label>
                    <div class="d-flex flex-wrap gap-2">
                        <button class="btn btn-sm" onclick="useTemplate('urgent')" style="background: #ff4757; color: white; padding: 10px 20px; border-radius: 20px;">
                            ⚠️ Urgent Alert
                        </button>
                        <button class="btn btn-sm" onclick="useTemplate('reminder')" style="background: #ffa502; color: white; padding: 10px 20px; border-radius: 20px;">
                            📢 Reminder
                        </button>
                        <button class="btn btn-sm" onclick="useTemplate('congratulations')" style="background: #2ed573; color: white; padding: 10px 20px; border-radius: 20px;">
                            🎉 Congratulations
                        </button>
                        <button class="btn btn-sm" onclick="useTemplate('status')" style="background: #1e90ff; color: white; padding: 10px 20px; border-radius: 20px;">
                            📊 Status Update
                        </button>
                    </div>
                    <small class="text-muted d-block mt-2">Click a template to auto-fill the subject and message fields</small>
                </div>
                
                <!-- Email Subject -->
                <div class="mb-4">
                    <label for="emailSubject" class="form-label"><i class="fas fa-heading"></i> <strong>Email Subject</strong></label>
                    <input type="text" class="form-control" id="emailSubject" placeholder="Enter email subject..." maxlength="200" style="border-radius: 10px; border: 2px solid #e0e0e0; padding: 12px;">
                    <div class="d-flex justify-content-between mt-1">
                        <small class="text-muted">Leave empty to use automatic subject based on country status</small>
                        <small class="text-muted"><span id="subjectCount">0</span>/200 characters</small>
                    </div>
                </div>
                
                <!-- Alert Message -->
                <div class="mb-4">
                    <label for="alertMessage" class="form-label"><i class="fas fa-comment-alt"></i> <strong>Alert Message</strong></label>
                    <textarea class="form-control" id="alertMessage" rows="8" placeholder="Write your custom alert message here...

Example:
Dear Energy Ministry,

We would like to inform you about...

Best regards,
SDG 7 Monitoring Team" style="border-radius: 10px; border: 2px solid #e0e0e0; padding: 12px;"></textarea>
                    <small class="text-muted">Leave empty to use automatic message based on country's electricity access status</small>
                </div>
                
                <!-- Send Buttons -->
                <div class="d-flex justify-content-between align-items-center flex-wrap gap-2">
                    <div>
                        <button class="btn btn-send-alerts" onclick="sendSelectedAlerts()">
                            <i class="fas fa-paper-plane"></i> Send Alerts to Selected Countries
                        </button>
                    </div>
                    <div>
                        <button class="btn btn-send-all" onclick="sendAllAlerts()">
                            <i class="fas fa-globe-americas"></i> Send to All Countries
                        </button>
                    </div>
                    <div>
                        <button class="btn btn-primary" onclick="sendXGBoostAlertsAuto()" style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); border: none; padding: 12px 30px; border-radius: 50px; font-weight: bold;">
                            <i class="fas fa-robot"></i> 🤖 Auto Send XGBoost Alerts
                        </button>
                    </div>
                </div>
            </div>
        </div>'''

# Replace
content = content.replace(old_section, new_section)

# Now add the JavaScript functions for templates and character counting
js_functions = '''
        // Template functions
        const templates = {
            urgent: {
                subject: '🚨 URGENT: Electricity Access Alert - Immediate Action Required',
                message: `Dear Energy Ministry Officials,

This is an URGENT alert regarding electricity access in your country.

Our latest analysis indicates critical issues that require immediate attention. We strongly recommend taking swift action to address the electricity access challenges.

Key Points:
• Current situation requires urgent intervention
• Immediate policy review recommended
• Technical assistance available upon request

Please contact us at your earliest convenience to discuss action plans.

Best regards,
SDG 7 Monitoring Team`
            },
            reminder: {
                subject: '📢 Reminder: SDG 7 Electricity Access Status Update',
                message: `Dear Energy Ministry,

This is a friendly reminder about your country's electricity access status under SDG 7 (Affordable and Clean Energy).

We encourage you to:
• Review the latest electricity access data
• Update your national energy policies
• Share progress reports with our team

We're here to support your efforts toward universal electricity access.

Best regards,
SDG 7 Monitoring Team`
            },
            congratulations: {
                subject: '🎉 Congratulations! Excellent Progress on SDG 7',
                message: `Dear Energy Ministry,

Congratulations! We are pleased to inform you that your country has achieved excellent electricity access rates.

Your achievements:
• High electricity access coverage
• Strong progress toward SDG 7 targets
• Exemplary energy policies

Keep up the outstanding work! Your success serves as an inspiration to other nations.

Best regards,
SDG 7 Monitoring Team`
            },
            status: {
                subject: '📊 SDG 7 Status Update: Electricity Access Report',
                message: `Dear Energy Ministry,

We are writing to provide you with a status update on your country's electricity access under SDG 7.

Current Status:
• Electricity access data has been analyzed
• Recommendations are available
• Support resources are ready

Please review the attached information and let us know if you need any assistance.

Best regards,
SDG 7 Monitoring Team`
            }
        };
        
        function useTemplate(type) {
            const template = templates[type];
            if (template) {
                $('#emailSubject').val(template.subject);
                $('#alertMessage').val(template.message);
                updateCharacterCount();
            }
        }
        
        // Character counting
        function updateCharacterCount() {
            const subject = $('#emailSubject').val();
            $('#subjectCount').text(subject.length);
        }
        
        // Add event listener for character counting
        $(document).ready(function() {
            $('#emailSubject').on('input', updateCharacterCount);
        });'''

# Find the place to insert (before the closing script tag)
insert_marker = "        // Load countries on page load"
content = content.replace(insert_marker, js_functions + "\n        " + insert_marker)

# Write back
with open('sustainable_energy/dashboard/templates/dashboard/objective8.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Customization features added to Email Alert System!")
print("📝 Added features:")
print("   • Quick Templates (Urgent, Reminder, Congratulations, Status)")
print("   • Email Subject field (200 char limit)")
print("   • Custom Alert Message textarea")
print("   • Character counter for subject")
print("   • Template click-to-use functionality")
