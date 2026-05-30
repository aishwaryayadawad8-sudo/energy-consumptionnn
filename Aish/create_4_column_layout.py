#!/usr/bin/env python3
"""
Create 4-column layout with 2 objectives per column (stacked vertically)
Column 1: Obj 1&2, Column 2: Obj 3&4, Column 3: Obj 5&6, Column 4: Obj 7&8
"""

def create_4_column_layout():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    print("🔧 Creating 4-column layout with 2 objectives per column...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update CSS for 4-column layout
        old_css = '''        .objectives-grid {
            display: grid;
            grid-template-columns: 1fr 1fr; /* 2 columns */
            gap: 30px; /* Gap between cards */
            margin-top: 20px;
        }'''
        
        new_css = '''        .objectives-grid {
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
        
        if old_css in content:
            content = content.replace(old_css, new_css)
            print("✅ Updated CSS for 4-column layout")
        
        # Update mobile responsive CSS
        old_mobile = '''            .objectives-grid {
                grid-template-columns: 1fr; /* Single column on mobile */
                gap: 20px;
            }'''
        
        new_mobile = '''            .objectives-grid {
                grid-template-columns: 1fr; /* Single column on mobile */
                gap: 20px;
            }
            
            .objective-column {
                gap: 15px;
            }'''
        
        if old_mobile in content:
            content = content.replace(old_mobile, new_mobile)
            print("✅ Updated mobile responsive CSS")
        
        # Now restructure the HTML to group objectives into columns
        # Find the objectives section
        objectives_start = content.find('<div class="objectives-grid">')
        objectives_end = content.find('</div>\n        </div>\n    </section>')
        
        if objectives_start != -1 and objectives_end != -1:
            # Extract the part before and after objectives
            before_objectives = content[:objectives_start]
            after_objectives = content[objectives_end:]
            
            # Create new HTML structure with 4 columns
            new_objectives_html = '''<div class="objectives-grid">
                <!-- Column 1: Objectives 1 & 2 -->
                <div class="objective-column">
                    <!-- Objective 1: Energy Consumption Prediction -->
                    <div class="objective-card">
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
                    <div class="objective-card">
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
                </div>
                
                <!-- Column 2: Objectives 3 & 4 -->
                <div class="objective-column">
                    <!-- Objective 3: Energy Access Classification -->
                    <div class="objective-card">
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
                    <div class="objective-card">
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
                </div>
                
                <!-- Column 3: Objectives 5 & 6 -->
                <div class="objective-column">
                    <!-- Objective 5: Energy Equity Analysis -->
                    <div class="objective-card">
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
                    <div class="objective-card">
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
                </div>
                
                <!-- Column 4: Objectives 7 & 8 -->
                <div class="objective-column">
                    <!-- Objective 7: Renewable Energy Potential Assessment -->
                    <div class="objective-card">
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
                    <div class="objective-card">
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
                </div>
            </div>'''
            
            # Reconstruct the content
            content = before_objectives + new_objectives_html + after_objectives
            print("✅ Restructured HTML for 4-column layout")
        
        # Update objective card CSS for smaller size
        old_card_css = '''        .objective-card {
            background: white;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border: 1px solid #f1f5f9;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            min-height: 300px;
            display: flex;
            flex-direction: column;
        }'''
        
        new_card_css = '''        .objective-card {
            background: white;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border: 1px solid #f1f5f9;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            min-height: 250px;
            display: flex;
            flex-direction: column;
        }'''
        
        if old_card_css in content:
            content = content.replace(old_card_css, new_card_css)
            print("✅ Updated objective card CSS for compact layout")
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ 4-column layout created successfully!")
        print("📝 Layout structure:")
        print("   📊 Column 1: Objectives 1 & 2")
        print("   🌍 Column 2: Objectives 3 & 4") 
        print("   ⚖️  Column 3: Objectives 5 & 6")
        print("   🌱 Column 4: Objectives 7 & 8")
        print("🔄 Please refresh your browser to see the new 4-column layout")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating 4-column layout: {e}")
        return False

if __name__ == "__main__":
    create_4_column_layout()