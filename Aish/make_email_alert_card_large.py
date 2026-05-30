#!/usr/bin/env python3
"""Make Email Alert System card full width (larger)"""

# Read the file
with open('sustainable_energy/dashboard/templates/dashboard/objective_selector.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Change from col-md-6 (half width) to col-md-12 (full width)
old_card = '''        <div class="row mt-4">
            <!-- Objective 8: Email Alert System -->
            <div class="col-md-6">
                <div class="objective-card" onclick="openEmailAlertSystem()">
                    <div class="objective-icon">
                        <i class="fas fa-envelope"></i>
                    </div>
                    <div class="objective-title">📧 Email Alert System (Multiple)</div>
                    <div class="objective-description">
                        Send electricity access alerts to multiple countries at once
                    </div>
                    <div class="objective-features">
                        <ul>
                            <li><i class="fas fa-check-circle text-success"></i> Select multiple countries</li>
                            <li><i class="fas fa-check-circle text-success"></i> Automated analysis</li>
                            <li><i class="fas fa-check-circle text-success"></i> Customized emails</li>
                        </ul>
                    </div>
                    <button class="btn btn-objective">
                        Send Alerts <i class="fas fa-paper-plane"></i>
                    </button>
                </div>
            </div>

        </div>'''

new_card = '''        <div class="row mt-4">
            <!-- Objective 8: Email Alert System -->
            <div class="col-md-12">
                <div class="objective-card" onclick="openEmailAlertSystem()">
                    <div class="objective-icon">
                        <i class="fas fa-envelope"></i>
                    </div>
                    <div class="objective-title">📧 Email Alert System (Multiple)</div>
                    <div class="objective-description">
                        Send electricity access alerts to multiple countries at once
                    </div>
                    <div class="objective-features">
                        <ul>
                            <li><i class="fas fa-check-circle text-success"></i> Select multiple countries</li>
                            <li><i class="fas fa-check-circle text-success"></i> Automated analysis</li>
                            <li><i class="fas fa-check-circle text-success"></i> Customized emails</li>
                        </ul>
                    </div>
                    <button class="btn btn-objective">
                        Send Alerts <i class="fas fa-paper-plane"></i>
                    </button>
                </div>
            </div>
        </div>'''

# Replace
content = content.replace(old_card, new_card)

# Write back
with open('sustainable_energy/dashboard/templates/dashboard/objective_selector.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Email Alert System card made larger!")
print("📏 Changed from col-md-6 (50% width) to col-md-12 (100% width)")
print("🔄 Card now spans full width of the page")
