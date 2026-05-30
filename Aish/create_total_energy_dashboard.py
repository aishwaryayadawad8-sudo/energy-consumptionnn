#!/usr/bin/env python3
"""
Create a comprehensive Total Energy Dashboard page
This will be accessible via the Total Energy navigation icon
"""

def create_total_energy_dashboard():
    print("🔧 Creating Total Energy Dashboard page...")
    
    # Create the Total Energy dashboard HTML template
    total_energy_html = '''{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Total Energy - SDG-7 Project</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }
        
        .header-section {
            background: white;
            padding: 30px;
            margin: 20px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            text-align: center;
        }
        
        .energy-icon {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px;
            font-size: 2.5rem;
            color: white;
        }
        
        .main-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #1f2937;
            margin-bottom: 10px;
        }
        
        .subtitle {
            font-size: 1.2rem;
            color: #6b7280;
            margin-bottom: 20px;
        }
        
        .back-btn {
            background: linear-gradient(135deg, #6b7280 0%, #4b5563 100%);
            color: white;
            padding: 12px 24px;
            border-radius: 25px;
            text-decoration: none;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.3s ease;
        }
        
        .back-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            color: white;
            text-decoration: none;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px;
        }
        
        .stat-card {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        
        .stat-card:hover {
            transform: translateY(-5px);
        }
        
        .stat-header {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 20px;
        }
        
        .stat-icon {
            width: 50px;
            height: 50px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            color: white;
        }
        
        .stat-icon.consumption {
            background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
        }
        
        .stat-icon.generation {
            background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        }
        
        .stat-icon.renewable {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        }
        
        .stat-icon.access {
            background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
        }
        
        .stat-icon.investment {
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        }
        
        .stat-title {
            font-size: 1.3rem;
            font-weight: 600;
            color: #1f2937;
        }
        
        .stat-value {
            font-size: 2.5rem;
            font-weight: 700;
            color: #f97316;
            margin-bottom: 10px;
        }
        
        .stat-description {
            color: #6b7280;
            line-height: 1.6;
            margin-bottom: 15px;
        }
        
        .stat-details {
            background: #f8fafc;
            border-radius: 8px;
            padding: 15px;
        }
        
        .stat-details ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        
        .stat-details li {
            padding: 5px 0;
            display: flex;
            justify-content: space-between;
            border-bottom: 1px solid #e5e7eb;
        }
        
        .stat-details li:last-child {
            border-bottom: none;
        }
        
        .breakdown-chart {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .chart-title {
            font-size: 1.5rem;
            font-weight: 600;
            color: #1f2937;
            margin-bottom: 20px;
            text-align: center;
        }
        
        .energy-bar {
            display: flex;
            height: 60px;
            border-radius: 30px;
            overflow: hidden;
            margin-bottom: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        
        .energy-segment {
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 600;
            font-size: 0.9rem;
            transition: all 0.3s ease;
        }
        
        .energy-segment:hover {
            filter: brightness(1.1);
        }
        
        .fossil {
            background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        }
        
        .renewable {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        }
        
        .nuclear {
            background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        }
        
        .legend {
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
        }
        
        .legend-item {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .legend-color {
            width: 20px;
            height: 20px;
            border-radius: 4px;
        }
        
        .objectives-section {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .objectives-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }
        
        .objective-item {
            background: #f8fafc;
            border-radius: 10px;
            padding: 20px;
            border-left: 4px solid #f97316;
            transition: all 0.3s ease;
        }
        
        .objective-item:hover {
            background: #f1f5f9;
            transform: translateX(5px);
        }
        
        .objective-number {
            background: #f97316;
            color: white;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            font-size: 0.9rem;
            margin-bottom: 10px;
        }
        
        .objective-title {
            font-weight: 600;
            color: #1f2937;
            margin-bottom: 5px;
        }
        
        .objective-desc {
            color: #6b7280;
            font-size: 0.9rem;
        }
        
        @media (max-width: 768px) {
            .stats-grid {
                grid-template-columns: 1fr;
                margin: 10px;
            }
            
            .breakdown-chart,
            .objectives-section {
                margin: 10px;
                padding: 20px;
            }
            
            .main-title {
                font-size: 2rem;
            }
            
            .legend {
                gap: 15px;
            }
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <div class="header-section">
        <div class="energy-icon">
            <i class="fas fa-bolt"></i>
        </div>
        <h1 class="main-title">TOTAL ENERGY</h1>
        <p class="subtitle">Comprehensive Energy Analysis - SDG-7 Project</p>
        <a href="/country-forecasts/" class="back-btn">
            <i class="fas fa-arrow-left"></i> Back to Objectives
        </a>
    </div>

    <!-- Energy Statistics Grid -->
    <div class="stats-grid">
        <!-- Energy Consumption Card -->
        <div class="stat-card">
            <div class="stat-header">
                <div class="stat-icon consumption">
                    <i class="fas fa-home"></i>
                </div>
                <div class="stat-title">Energy Consumption</div>
            </div>
            <div class="stat-value">23,462</div>
            <div class="stat-description">kWh per person per year (Global Average)</div>
            <div class="stat-details">
                <ul>
                    <li><span>Highest Consumer:</span> <strong>Bahrain</strong></li>
                    <li><span>Consumption:</span> <strong>156,096 kWh/person</strong></li>
                    <li><span>Lowest Consumer:</span> <strong>Central African Republic</strong></li>
                    <li><span>Consumption:</span> <strong>281 kWh/person</strong></li>
                    <li><span>Variation:</span> <strong>557x difference</strong></li>
                </ul>
            </div>
        </div>

        <!-- Electricity Generation Card -->
        <div class="stat-card">
            <div class="stat-header">
                <div class="stat-icon generation">
                    <i class="fas fa-industry"></i>
                </div>
                <div class="stat-title">Electricity Generation</div>
            </div>
            <div class="stat-value">252,987</div>
            <div class="stat-description">TWh Total Global Generation</div>
            <div class="stat-details">
                <ul>
                    <li><span>Fossil Fuels:</span> <strong>162,543 TWh (64.2%)</strong></li>
                    <li><span>Renewables:</span> <strong>66,962 TWh (26.5%)</strong></li>
                    <li><span>Nuclear:</span> <strong>23,483 TWh (9.3%)</strong></li>
                    <li><span>Countries:</span> <strong>128 Countries</strong></li>
                    <li><span>Time Period:</span> <strong>2000-2020</strong></li>
                </ul>
            </div>
        </div>

        <!-- Renewable Energy Card -->
        <div class="stat-card">
            <div class="stat-header">
                <div class="stat-icon renewable">
                    <i class="fas fa-leaf"></i>
                </div>
                <div class="stat-title">Renewable Energy</div>
            </div>
            <div class="stat-value">34.09%</div>
            <div class="stat-description">Global Average Renewable Share</div>
            <div class="stat-details">
                <ul>
                    <li><span>Best Performance:</span> <strong>96.04% renewable</strong></li>
                    <li><span>Renewable Generation:</span> <strong>66,962 TWh</strong></li>
                    <li><span>Clean Energy Growth:</span> <strong>26.5% of electricity</strong></li>
                    <li><span>Future Potential:</span> <strong>Significant growth</strong></li>
                </ul>
            </div>
        </div>

        <!-- Energy Access Card -->
        <div class="stat-card">
            <div class="stat-header">
                <div class="stat-icon access">
                    <i class="fas fa-users"></i>
                </div>
                <div class="stat-title">Energy Access</div>
            </div>
            <div class="stat-value">78.39%</div>
            <div class="stat-description">Global Population with Electricity Access</div>
            <div class="stat-details">
                <ul>
                    <li><span>People without electricity:</span> <strong>~1.7 billion</strong></li>
                    <li><span>Clean cooking access:</span> <strong>61.99% globally</strong></li>
                    <li><span>Full access records:</span> <strong>1,222 instances</strong></li>
                    <li><span>Limited access:</span> <strong>565 instances</strong></li>
                </ul>
            </div>
        </div>

        <!-- Investment Card -->
        <div class="stat-card">
            <div class="stat-header">
                <div class="stat-icon investment">
                    <i class="fas fa-dollar-sign"></i>
                </div>
                <div class="stat-title">Energy Investment</div>
            </div>
            <div class="stat-value">$120.24B</div>
            <div class="stat-description">Total Investment in Developing Countries</div>
            <div class="stat-details">
                <ul>
                    <li><span>Average Investment:</span> <strong>$101.2 Million</strong></li>
                    <li><span>Investment Records:</span> <strong>1,188 instances</strong></li>
                    <li><span>Focus:</span> <strong>Sustainable Energy</strong></li>
                    <li><span>Impact:</span> <strong>Global SDG-7 Progress</strong></li>
                </ul>
            </div>
        </div>

        <!-- Project Scope Card -->
        <div class="stat-card">
            <div class="stat-header">
                <div class="stat-icon consumption">
                    <i class="fas fa-globe"></i>
                </div>
                <div class="stat-title">Project Scope</div>
            </div>
            <div class="stat-value">2,990</div>
            <div class="stat-description">Total Data Points Analyzed</div>
            <div class="stat-details">
                <ul>
                    <li><span>Countries/Regions:</span> <strong>128 global</strong></li>
                    <li><span>Years Covered:</span> <strong>21 years (2000-2020)</strong></li>
                    <li><span>ML Objectives:</span> <strong>8 comprehensive</strong></li>
                    <li><span>Energy Sources:</span> <strong>Multiple tracked</strong></li>
                </ul>
            </div>
        </div>
    </div>

    <!-- Energy Mix Breakdown Chart -->
    <div class="breakdown-chart">
        <h2 class="chart-title">Global Electricity Generation Mix</h2>
        <div class="energy-bar">
            <div class="energy-segment fossil" style="width: 64.2%;">
                Fossil Fuels 64.2%
            </div>
            <div class="energy-segment renewable" style="width: 26.5%;">
                Renewables 26.5%
            </div>
            <div class="energy-segment nuclear" style="width: 9.3%;">
                Nuclear 9.3%
            </div>
        </div>
        <div class="legend">
            <div class="legend-item">
                <div class="legend-color fossil"></div>
                <span>Fossil Fuels (162,543 TWh)</span>
            </div>
            <div class="legend-item">
                <div class="legend-color renewable"></div>
                <span>Renewables (66,962 TWh)</span>
            </div>
            <div class="legend-item">
                <div class="legend-color nuclear"></div>
                <span>Nuclear (23,483 TWh)</span>
            </div>
        </div>
    </div>

    <!-- 8 Objectives Section -->
    <div class="objectives-section">
        <h2 class="chart-title">8 Machine Learning Objectives</h2>
        <div class="objectives-grid">
            <div class="objective-item">
                <div class="objective-number">1</div>
                <div class="objective-title">Energy Consumption Prediction</div>
                <div class="objective-desc">Future energy demand forecasting</div>
            </div>
            <div class="objective-item">
                <div class="objective-number">2</div>
                <div class="objective-title">CO₂ Emission Forecasting</div>
                <div class="objective-desc">Environmental impact assessment</div>
            </div>
            <div class="objective-item">
                <div class="objective-number">3</div>
                <div class="objective-title">Energy Access Classification</div>
                <div class="objective-desc">Population access analysis</div>
            </div>
            <div class="objective-item">
                <div class="objective-number">4</div>
                <div class="objective-title">SDG-7 Progress Monitoring</div>
                <div class="objective-desc">Sustainable development tracking</div>
            </div>
            <div class="objective-item">
                <div class="objective-number">5</div>
                <div class="objective-title">Energy Equity Analysis</div>
                <div class="objective-desc">Fairness in energy distribution</div>
            </div>
            <div class="objective-item">
                <div class="objective-number">6</div>
                <div class="objective-title">Efficiency Optimization</div>
                <div class="objective-desc">Energy usage optimization</div>
            </div>
            <div class="objective-item">
                <div class="objective-number">7</div>
                <div class="objective-title">Renewable Energy Assessment</div>
                <div class="objective-desc">Clean energy potential analysis</div>
            </div>
            <div class="objective-item">
                <div class="objective-number">8</div>
                <div class="objective-title">Investment Strategy Support</div>
                <div class="objective-desc">Financial decision support</div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>'''
    
    try:
        # Create the template file
        template_path = "sustainable_energy/dashboard/templates/dashboard/total_energy.html"
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(total_energy_html)
        
        print("✅ Created Total Energy dashboard template")
        
        # Now update the views.py to add the total energy view
        views_path = "sustainable_energy/dashboard/views.py"
        
        # Read current views
        with open(views_path, 'r', encoding='utf-8') as f:
            views_content = f.read()
        
        # Add total energy view function
        total_energy_view = '''

def total_energy_dashboard(request):
    """Total Energy Dashboard - Comprehensive energy analysis"""
    return render(request, 'dashboard/total_energy.html')
'''
        
        # Add the view if it doesn't exist
        if 'def total_energy_dashboard' not in views_content:
            views_content += total_energy_view
            
            with open(views_path, 'w', encoding='utf-8') as f:
                f.write(views_content)
            
            print("✅ Added total_energy_dashboard view to views.py")
        
        # Update URLs
        urls_path = "sustainable_energy/dashboard/urls.py"
        
        with open(urls_path, 'r', encoding='utf-8') as f:
            urls_content = f.read()
        
        # Add total energy URL pattern
        total_energy_url = "    path('total-energy/', views.total_energy_dashboard, name='total_energy_dashboard'),"
        
        if 'total-energy/' not in urls_content:
            # Find the urlpatterns list and add the new URL
            if 'urlpatterns = [' in urls_content:
                insertion_point = urls_content.find('urlpatterns = [') + len('urlpatterns = [')
                urls_content = urls_content[:insertion_point] + '\n    ' + total_energy_url + urls_content[insertion_point:]
                
                with open(urls_path, 'w', encoding='utf-8') as f:
                    f.write(urls_content)
                
                print("✅ Added total energy URL to urls.py")
        
        print("✅ Total Energy Dashboard created successfully!")
        print("📝 Features added:")
        print("   🔋 Comprehensive energy statistics")
        print("   📊 Visual energy mix breakdown")
        print("   🌍 Global consumption analysis")
        print("   💰 Investment tracking")
        print("   🎯 8 ML objectives overview")
        print("🔗 Access via: /total-energy/")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating Total Energy dashboard: {e}")
        return False

if __name__ == "__main__":
    create_total_energy_dashboard()