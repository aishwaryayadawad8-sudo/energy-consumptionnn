#!/usr/bin/env python3
"""
Create 2-row layout with 4 objectives per row
Row 1: Objectives 1, 2, 3, 4
Row 2: Objectives 5, 6, 7, 8
"""

def create_2_row_layout():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Creating 2-row layout with 4 objectives per row...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update CSS for 2-row layout (4 columns grid)
        old_css = '''        .objectives-grid {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr 1fr; /* 4 columns */
            gap: 20px; /* Gap between columns */
            margin-top: 20px;
        }
        
        .objective-column {
            display: flex;
            flex-direction: column;
            gap: 20px; /* Gap between objectives in same column */
        }'''
        
        new_css = '''        .objectives-grid {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr 1fr; /* 4 columns for 4 objectives per row */
            grid-template-rows: auto auto; /* 2 rows */
            gap: 20px; /* Gap between objectives */
            margin-top: 20px;
        }'''
        
        if old_css in content:
            content = content.replace(old_css, new_css)
            print("✅ Updated CSS for 2-row layout")
        
        # Update mobile responsive CSS
        old_mobile = '''            .objectives-grid {
                grid-template-columns: 1fr; /* Single column on mobile */
                gap: 20px;
            }
            
            .objective-column {
                gap: 15px;
            }'''
        
        new_mobile = '''            .objectives-grid {
                grid-template-columns: 1fr 1fr; /* 2 columns on mobile */
                grid-template-rows: auto auto auto auto; /* 4 rows on mobile */
                gap: 15px;
            }'''
        
        if old_mobile in content:
            content = content.replace(old_mobile, new_mobile)
            print("✅ Updated mobile responsive CSS")
        
        # Now restructure the HTML to remove column grouping and place objectives directly in grid
        # Find the objectives section
        objectives_start = content.find('<div class="objectives-grid">')
        objectives_end = content.find('</div>\n        </div>\n    </section>')
        
        if objectives_start != -1 and objectives_end != -1:
            # Extract the part before and after objectives
            before_objectives = content[:objectives_start]
            after_objectives = content[objectives_end:]
            
            # Create new HTML structure with direct grid placement (no columns)
            new_objectives_html = '''<div class="objectives-grid">
                <!-- Row 1: Objectives 1, 2, 3, 4 -->
                
                <!-- Objective 1: Energy Consumption Prediction -->
                <div class="objective-card" data-objective="1">
                    <div class="objective-info">
                        <div class="objective-header">
                            <div class="objective-icon">
                                <i class="fas fa-bolt"></i>
                            </div>
                            <div class="objective-number">01</div>
                        </div>
                        <h3 class="objective-title">Energy Consumption Prediction</h3>
                        <p class="objective-description">
                            To analyze historical global energy consumption data and develop machine learning models to predict future electricity usage trends across different countries.
                        </p>
                        <a href="{% url 'objective1_dashboard' %}" class="objective-btn" style="margin-top: auto;">
                            View Analysis
                        </a>
                    </div>
                </div>
                
                <!-- Objective 2: CO₂ Emission Forecasting -->
                <div class="objective-card" data-objective="2">
                    <div class="objective-info">
                        <div class="objective-header">
                            <div class="objective-icon">
                                <i class="fas fa-smog"></i>
                            </div>
                            <div class="objective-number">02</div>
                        </div>
                        <h3 class="objective-title">CO₂ Emission Forecasting</h3>
                        <p class="objective-description">
                            To study past carbon emission patterns and forecast future CO₂ emission levels in order to assess environmental impact and sustainability progress.
                        </p>
                        <a href="{% url 'objective2_dashboard' %}" class="objective-btn" style="margin-top: auto;">
                            View Analysis
                        </a>
                    </div>
                </div>
                
                <!-- Objective 3: Energy Access Classification -->
                <div class="objective-card" data-objective="3">
                    <div class="objective-info">
                        <div class="objective-header">
                            <div class="objective-icon">
                                <i class="fas fa-users"></i>
                            </div>
                            <div class="objective-number">03</div>
                        </div>
                        <h3 class="objective-title">Energy Access Classification</h3>
                        <p class="objective-description">
                            To classify countries based on electricity access levels using machine learning techniques, identifying regions with inadequate or improving energy availability.
                        </p>
                        <a href="{% url 'objective3_dashboard' %}" class="objective-btn" style="margin-top: auto;">
                            View Analysis
                        </a>
                    </div>
                </div>
                
                <!-- Objective 4: SDG-7 Progress Monitoring -->
                <div class="objective-card" data-objective="4">
                    <div class="objective-info">
                        <div class="objective-header">
                            <div class="objective-icon">
                                <i class="fas fa-target"></i>
                            </div>
                            <div class="objective-number">04</div>
                        </div>
                        <h3 class="objective-title">SDG-7 Progress Monitoring</h3>
                        <p class="objective-description">
                            To monitor and visualize country-wise progress toward Sustainable Development Goal 7 using historical indicators and trend analysis.
                        </p>
                        <a href="{% url 'objective4_dashboard' %}" class="objective-btn" style="margin-top: auto;">
                            View Analysis
                        </a>
                    </div>
                </div>
                
                <!-- Row 2: Objectives 5, 6, 7, 8 -->
                
                <!-- Objective 5: Energy Equity Analysis -->
                <div class="objective-card" data-objective="5">
                    <div class="objective-info">
                        <div class="objective-header">
                            <div class="objective-icon">
                                <i class="fas fa-balance-scale"></i>
                            </div>
                            <div class="objective-number">05</div>
                        </div>
                        <h3 class="objective-title">Energy Equity Analysis</h3>
                        <p class="objective-description">
                            To evaluate disparities in energy access and consumption among developed, developing, and underdeveloped countries.
                        </p>
                        <a href="{% url 'objective5_dashboard' %}" class="objective-btn" style="margin-top: auto;">
                            View Analysis
                        </a>
                    </div>
                </div>
                
                <!-- Objective 6: Efficiency Optimization Identification -->
                <div class="objective-card" data-objective="6">
                    <div class="objective-info">
                        <div class="objective-header">
                            <div class="objective-icon">
                                <i class="fas fa-tachometer-alt"></i>
                            </div>
                            <div class="objective-number">06</div>
                        </div>
                        <h3 class="objective-title">Efficiency Optimization Identification</h3>
                        <p class="objective-description">
                            To identify high-consumption regions and inefficiencies in energy usage that can be optimized for better sustainability outcomes.
                        </p>
                        <a href="{% url 'objective6_dashboard' %}" class="objective-btn" style="margin-top: auto;">
                            View Analysis
                        </a>
                    </div>
                </div>
                
                <!-- Objective 7: Renewable Energy Potential Assessment -->
                <div class="objective-card" data-objective="7">
                    <div class="objective-info">
                        <div class="objective-header">
                            <div class="objective-icon">
                                <i class="fas fa-leaf"></i>
                            </div>
                            <div class="objective-number">07</div>
                        </div>
                        <h3 class="objective-title">Renewable Energy Potential Assessment</h3>
                        <p class="objective-description">
                            To assess renewable energy growth trends and predict future potential for clean energy adoption across countries.
                        </p>
                        <a href="{% url 'objective7_dashboard' %}" class="objective-btn" style="margin-top: auto;">
                            View Analysis
                        </a>
                    </div>
                </div>
                
                <!-- Objective 8: Sustainable Investment Strategy Support -->
                <div class="objective-card" data-objective="8">
                    <div class="objective-info">
                        <div class="objective-header">
                            <div class="objective-icon">
                                <i class="fas fa-chart-pie"></i>
                            </div>
                            <div class="objective-number">08</div>
                        </div>
                        <h3 class="objective-title">Sustainable Investment Strategy Support</h3>
                        <p class="objective-description">
                            To provide data-driven insights and forecasts that can support strategic investment decisions in sustainable and renewable energy sectors.
                        </p>
                        <a href="{% url 'objective8_dashboard' %}" class="objective-btn" style="margin-top: auto;">
                            View Analysis
                        </a>
                    </div>
                </div>
            </div>'''
            
            # Reconstruct the content
            content = before_objectives + new_objectives_html + after_objectives
            print("✅ Restructured HTML for 2-row layout")
        
        # Remove any remaining objective-column CSS since we're not using columns anymore
        column_css_patterns = [
            r'\.objective-column \{[^}]*\}',
            r'\/\* Content expansion area.*?\*\/',
        ]
        
        import re
        for pattern in column_css_patterns:
            content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        print("✅ Cleaned up unused column CSS")
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ 2-row layout created successfully!")
        print("📝 Layout structure:")
        print("   📊 Row 1: Objectives 1, 2, 3, 4")
        print("   📊 Row 2: Objectives 5, 6, 7, 8")
        print("🔄 Please refresh your browser to see the new 2-row layout")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating 2-row layout: {e}")
        return False

if __name__ == "__main__":
    create_2_row_layout()