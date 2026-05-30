#!/usr/bin/env python3
"""Revert to separate dashboards - keep them as individual cards"""

# Read the current file
with open('sustainable_energy/dashboard/templates/dashboard/objective_selector.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace back to original separate dashboards
old_section = '''        <!-- Featured: Full Analysis (Dashboard + ML Comparison) -->
        <div class="row mb-4">
            <div class="col-12">
                <div class="objective-card" onclick="window.location.href='/full-analysis/'" style="background: white; border: 3px solid #FFD700; box-shadow: 0 10px 30px rgba(255, 215, 0, 0.3);">
                    <div class="objective-icon">
                        <i class="fas fa-chart-line"></i>
                    </div>
                    <div class="objective-title">⭐ Complete SDG 7 Analysis</div>
                    <div class="objective-description">
                        Full Dashboard + Comprehensive ML Comparison in One Page
                    </div>
                    <div class="objective-features">
                        <div class="row">
                            <div class="col-md-6">
                                <h6><i class="fas fa-globe"></i> Full Dashboard Section:</h6>
                                <ul>
                                    <li><i class="fas fa-check-circle text-success"></i> World map visualization</li>
                                    <li><i class="fas fa-check-circle text-success"></i> 7 ML models analysis</li>
                                    <li><i class="fas fa-check-circle text-success"></i> Status alerts system</li>
                                </ul>
                            </div>
                            <div class="col-md-6">
                                <h6><i class="fas fa-chart-bar"></i> ML Comparison Section:</h6>
                                <ul>
                                    <li><i class="fas fa-check-circle text-success"></i> 7 ML algorithms</li>
                                    <li><i class="fas fa-check-circle text-success"></i> 8 sub-objectives</li>
                                    <li><i class="fas fa-check-circle text-success"></i> Best model selection</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <button class="btn btn-objective" style="font-size: 1.2rem; padding: 15px 40px;">
                        View Complete Analysis <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>
        </div>
        
        <!-- Individual Dashboards -->
        <div class="row mb-4">
            <!-- Comprehensive ML Comparison -->
            <div class="col-md-6">
                <div class="objective-card" onclick="window.location.href='/comprehensive-comparison/'">
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
            
            <!-- Full Dashboard -->
            <div class="col-md-6">
                <div class="objective-card" onclick="window.location.href='/dashboard/'">
                    <div class="objective-icon">
                        <i class="fas fa-globe"></i>
                    </div>
                    <div class="objective-title">Full Dashboard: Comprehensive Analysis</div>
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
                        Explore <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>
        </div>'''

new_section = '''        <!-- Featured Dashboards at Top -->
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

# Replace the section
content = content.replace(old_section, new_section)

# Write back
with open('sustainable_energy/dashboard/templates/dashboard/objective_selector.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Reverted to separate dashboards!")
print("📊 Full Dashboard - Left side (Blue border)")
print("🏆 ML Comparison - Right side (Gold border)")
print("🔗 Both are separate sections on home page")
