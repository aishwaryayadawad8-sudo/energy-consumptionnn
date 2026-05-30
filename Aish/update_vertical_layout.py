#!/usr/bin/env python3
"""Update layout: Full Dashboard on top, ML Comparison below"""

# Read the current file
with open('sustainable_energy/dashboard/templates/dashboard/objective_selector.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace to vertical layout
old_section = '''        <!-- Featured Dashboards at Top -->
        <div class="row mb-4">
            <!-- Full Dashboard -->
            <div class="col-md-6">
                <div class="objective-card" onclick="window.location.href='/dashboard/'" style="background: white; border: 3px solid #667eea; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);">
                    <div class="objective-icon">
                        <i class="fas fa-globe"></i>
                    </div>
                    <div class="objective-title">🌍 Full Dashboard</div>
                    <div class="objective-description">
                        Complete energy analysis with world map and status alerts
                    </div>
                    <div class="objective-features">
                        <ul>
                            <li><i class="fas fa-check-circle text-success"></i> World map</li>
                            <li><i class="fas fa-check-circle text-success"></i> 7 ML models</li>
                            <li><i class="fas fa-check-circle text-success"></i> Status alerts</li>
                        </ul>
                    </div>
                    <button class="btn btn-objective">
                        Explore Dashboard <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>
            
            <!-- Comprehensive ML Comparison -->
            <div class="col-md-6">
                <div class="objective-card" onclick="window.location.href='/comprehensive-comparison/'" style="background: white; border: 3px solid #FFD700; box-shadow: 0 10px 30px rgba(255, 215, 0, 0.3);">
                    <div class="objective-icon">
                        <i class="fas fa-chart-bar"></i>
                    </div>
                    <div class="objective-title">🏆 Comprehensive ML Comparison</div>
                    <div class="objective-description">
                        Compare 7 ML algorithms across all 8 sub-objectives
                    </div>
                    <div class="objective-features">
                        <ul>
                            <li><i class="fas fa-check-circle text-success"></i> 7 ML algorithms</li>
                            <li><i class="fas fa-check-circle text-success"></i> 8 sub-objectives</li>
                            <li><i class="fas fa-check-circle text-success"></i> Best model selection</li>
                        </ul>
                    </div>
                    <button class="btn btn-objective">
                        Compare Models <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>
        </div>'''

new_section = '''        <!-- Section 1: Full Dashboard (Top) -->
        <div class="row mb-4">
            <div class="col-12">
                <div class="objective-card" onclick="window.location.href='/dashboard/'" style="background: white; border: 3px solid #667eea; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);">
                    <div class="objective-icon">
                        <i class="fas fa-globe"></i>
                    </div>
                    <div class="objective-title">🌍 Full Dashboard: Comprehensive Analysis</div>
                    <div class="objective-description">
                        Complete energy analysis with world map and status alerts
                    </div>
                    <div class="objective-features">
                        <ul>
                            <li><i class="fas fa-check-circle text-success"></i> World map</li>
                            <li><i class="fas fa-check-circle text-success"></i> 7 ML models</li>
                            <li><i class="fas fa-check-circle text-success"></i> Status alerts</li>
                        </ul>
                    </div>
                    <button class="btn btn-objective">
                        Explore Dashboard <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>
        </div>
        
        <!-- Section 2: Comprehensive ML Comparison (Below Dashboard) -->
        <div class="row mb-4">
            <div class="col-12">
                <div class="objective-card" onclick="window.location.href='/comprehensive-comparison/'" style="background: white; border: 3px solid #FFD700; box-shadow: 0 10px 30px rgba(255, 215, 0, 0.3);">
                    <div class="objective-icon">
                        <i class="fas fa-chart-bar"></i>
                    </div>
                    <div class="objective-title">🏆 Comprehensive ML Comparison</div>
                    <div class="objective-description">
                        Compare 7 ML algorithms across all 8 sub-objectives
                    </div>
                    <div class="objective-features">
                        <ul>
                            <li><i class="fas fa-check-circle text-success"></i> 7 ML algorithms</li>
                            <li><i class="fas fa-check-circle text-success"></i> 8 sub-objectives</li>
                            <li><i class="fas fa-check-circle text-success"></i> Best model selection</li>
                        </ul>
                    </div>
                    <button class="btn btn-objective">
                        Compare Models <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>
        </div>'''

# Replace the section
content = content.replace(old_section, new_section)

# Write back
with open('sustainable_energy/dashboard/templates/dashboard/objective_selector.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Layout updated to vertical!")
print("📊 Section 1 (Top): Full Dashboard (Blue border)")
print("🏆 Section 2 (Below): ML Comparison (Gold border)")
print("📐 Both sections now span full width")
