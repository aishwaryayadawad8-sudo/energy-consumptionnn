#!/usr/bin/env python3
"""Delete the Send Auto Alert section from objective selector"""

# Read the current file
with open('sustainable_energy/dashboard/templates/dashboard/objective_selector.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and remove the Send Auto Alert section
old_section = '''            
            <!-- Send Email to Single Country -->
            <div class="col-md-6">
                <div class="objective-card" onclick="window.location.href='/send-email-country/'">
                    <div class="objective-icon">
                        <i class="fas fa-envelope-open-text"></i>
                    </div>
                    <div class="objective-title">✉️ Send Auto Alert</div>
                    <div class="objective-description">
                        Send automatic alert based on predictions
                    </div>
                    <div class="objective-features">
                        <ul>
                            <li><i class="fas fa-check-circle text-success"></i> Select single country</li>
                            <li><i class="fas fa-check-circle text-success"></i> Auto-generated message</li>
                            <li><i class="fas fa-check-circle text-success"></i> Instant sending</li>
                        </ul>
                    </div>
                    <button class="btn btn-objective">
                        Send Auto Alert <i class="fas fa-paper-plane"></i>
                    </button>
                </div>
            </div>'''

new_section = ''

# Replace the section (remove it)
content = content.replace(old_section, new_section)

# Write back
with open('sustainable_energy/dashboard/templates/dashboard/objective_selector.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Send Auto Alert section deleted!")
print("🗑️  Removed from home page")
print("📄 File updated: objective_selector.html")
