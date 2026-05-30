#!/usr/bin/env python3
"""
Create a comprehensive Electricity Dashboard page
This will be accessible via the Electricity navigation icon
Shows both consumption and predictions data
"""

def create_electricity_dashboard():
    print("🔧 Creating Electricity Dashboard page...")
    
    # Create the Electricity dashboard HTML template
    electricity_html = '''{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Electricity Analysis - SDG-7 Project</title>
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
        
        .electricity-icon {
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
        
        .grand-total-section {
            background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
            color: white;
            border-radius: 15px;
            padding: 40px;
            margin: 20px;
            text-align: center;
            box-shadow: 0 15px 40px rgba(249, 115, 22, 0.3);
        }
        
        .grand-total-value {
            font-size: 4rem;
            font-weight: 700;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .grand-total-label {
            font-size: 1.5rem;
            font-weight: 600;
            opacity: 0.9;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
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
            background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        }
        
        .stat-icon.prediction {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        }
        
        .stat-icon.access {
            background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
        }
        
        .stat-icon.countries {
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
        
        .comparison-section {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .section-title {
            font-size: 1.8rem;
            font-weight: 600;
            color: #1f2937;
            margin-bottom: 20px;
            text-align: center;
        }
        
        .comparison-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-top: 20px;
        }
        
        .comparison-card {
            background: #f8fafc;
            border-radius: 10px;
            padding: 25px;
            text-align: center;
        }
        
        .comparison-card.historical {
            border-left: 5px solid #3b82f6;
        }
        
        .comparison-card.future {
            border-left: 5px solid #10b981;
        }
        
        .comparison-value {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 10px;
        }
        
        .comparison-value.historical {
            color: #3b82f6;
        }
        
        .comparison-value.future {
            color: #10b981;
        }
        
        .comparison-label {
            font-weight: 600;
            color: #374151;
            margin-bottom: 15px;
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
        
        .top-countries {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .countries-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-top: 20px;
        }
        
        .country-list {
            background: #f8fafc;
            border-radius: 10px;
            padding: 20px;
        }
        
        .country-list h4 {
            color: #374151;
            margin-bottom: 15px;
            font-weight: 600;
        }
        
        .country-item {
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 1px solid #e5e7eb;
        }
        
        .country-item:last-child {
            border-bottom: none;
        }
        
        .country-name {
            font-weight: 500;
        }
        
        .country-value {
            color: #f97316;
            font-weight: 600;
        }
        
        @media (max-width: 768px) {
            .stats-grid {
                grid-template-columns: 1fr;
                margin: 10px;
            }
            
            .comparison-grid,
            .countries-grid {
                grid-template-columns: 1fr;
                gap: 20px;
            }
            
            .breakdown-chart,
            .comparison-section,
            .top-countries {
                margin: 10px;
                padding: 20px;
            }
            
            .main-title {
                font-size: 2rem;
            }
            
            .grand-total-value {
                font-size: 3rem;
            }
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <div class="header-section">
        <div class="electricity-icon">
            <i class="fas fa-plug"></i>
        </div>
        <h1 class="main-title">ELECTRICITY</h1>
        <p class="subtitle">Complete Consumption & Predictions Analysis - SDG-7 Project</p>
        <a href="/country-forecasts/" class="back-btn">
            <i class="fas fa-arrow-left"></i> Back
        </a>
    </div>

    <!-- Grand Total Section -->
    <div class="grand-total-section">
        <div class="grand-total-value">274,520.04</div>
        <div class="grand-total-label">TWh Total Electricity Analyzed</div>
        <p style="margin-top: 15px; opacity: 0.9;">Historical Consumption + Future Predictions (2000-2030)</p>
    </div>

    <!-- Main Statistics Grid -->
    <div class="stats-grid">
        <!-- Historical Consumption Card -->
        <div class="stat-card">
            <div class="stat-header">
                <div class="stat-icon consumption">
                    <i class="fas fa-history"></i>
                </div>
                <div class="stat-title">Historical Consumption</div>
            </div>
            <div class="stat-value">252,987.47</div>
            <div class="stat-description">TWh consumed globally (2000-2020)</div>
            <div class="stat-details">
                <ul>
                    <li><span>Time Period:</span> <strong>21 years (2000-2020)</strong></li>
                    <li><span>Annual Average:</span> <strong>11,499.43 TWh/year</strong></li>
                    <li><span>Countries:</span> <strong>128 countries</strong></li>
                    <li><span>Data Points:</span> <strong>2,990 records</strong></li>
                </ul>
            </div>
        </div>

        <!-- Future Predictions Card -->
        <div class="stat-card">
            <div class="stat-header">
                <div class="stat-icon prediction">
                    <i class="fas fa-crystal-ball"></i>
                </div>
                <div class="stat-title">Future Predictions</div>
            </div>
            <div class="stat-value">21,532.57</div>
            <div class="stat-description">TWh predicted for 2030</div>
            <div class="stat-details">
                <ul>
                    <li><span>Prediction Year:</span> <strong>2030</strong></li>
                    <li><span>10-Year Cumulative:</span> <strong>107,662.86 TWh</strong></li>
                    <li><span>Growth Factor:</span> <strong>1.87x increase</strong></li>
                    <li><span>ML Predictions:</span> <strong>10,000 points</strong></li>
                </ul>
            </div>
        </div>

        <!-- Global Access Card -->
        <div class="stat-card">
            <div class="stat-header">
                <div class="stat-icon access">
                    <i class="fas fa-users"></i>
                </div>
                <div class="stat-title">Global Electricity Access</div>
            </div>
            <div class="stat-value">69.2%</div>
            <div class="stat-description">of global population has electricity access</div>
            <div class="stat-details">
                <ul>
                    <li><span>People with Access:</span> <strong>~5.4 billion</strong></li>
                    <li><span>People without Access:</span> <strong>~2.4 billion</strong></li>
                    <li><span>Access Needed:</span> <strong>30.8% improvement</strong></li>
                    <li><span>SDG-7 Target:</span> <strong>Universal access by 2030</strong></li>
                </ul>
            </div>
        </div>

        <!-- Project Coverage Card -->
        <div class="stat-card">
            <div class="stat-header">
                <div class="stat-icon countries">
                    <i class="fas fa-globe"></i>
                </div>
                <div class="stat-title">Project Coverage</div>
            </div>
            <div class="stat-value">128</div>
            <div class="stat-description">Countries analyzed globally</div>
            <div class="stat-details">
                <ul>
                    <li><span>Global Coverage:</span> <strong>97.7% of countries</strong></li>
                    <li><span>Population Coverage:</span> <strong>~95% of world</strong></li>
                    <li><span>Time Span:</span> <strong>30 years (2000-2030)</strong></li>
                    <li><span>ML Objectives:</span> <strong>8 comprehensive</strong></li>
                </ul>
            </div>
        </div>
    </div>

    <!-- Historical vs Future Comparison -->
    <div class="comparison-section">
        <h2 class="section-title">Historical vs Future Comparison</h2>
        <div class="comparison-grid">
            <div class="comparison-card historical">
                <div class="comparison-value historical">252,987.47</div>
                <div class="comparison-label">Historical Consumption (TWh)</div>
                <p>21 years of actual electricity consumption data from 128 countries (2000-2020)</p>
            </div>
            <div class="comparison-card future">
                <div class="comparison-value future">21,532.57</div>
                <div class="comparison-label">Future Predictions (TWh)</div>
                <p>ML-powered predictions for 2030 with 87% growth over historical average</p>
            </div>
        </div>
    </div>

    <!-- Historical Energy Mix -->
    <div class="breakdown-chart">
        <h2 class="chart-title">Historical Electricity Consumption by Source (2000-2020)</h2>
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
                <span>Fossil Fuels (162,542.68 TWh)</span>
            </div>
            <div class="legend-item">
                <div class="legend-color renewable"></div>
                <span>Renewables (66,961.93 TWh)</span>
            </div>
            <div class="legend-item">
                <div class="legend-color nuclear"></div>
                <span>Nuclear (23,482.86 TWh)</span>
            </div>
        </div>
    </div>

    <!-- Future Energy Mix -->
    <div class="breakdown-chart">
        <h2 class="chart-title">Predicted Electricity Generation by Source (2030)</h2>
        <div class="energy-bar">
            <div class="energy-segment fossil" style="width: 62.0%;">
                Fossil Fuels 62.0%
            </div>
            <div class="energy-segment renewable" style="width: 31.1%;">
                Renewables 31.1%
            </div>
            <div class="energy-segment nuclear" style="width: 6.1%;">
                Nuclear 6.1%
            </div>
        </div>
        <div class="legend">
            <div class="legend-item">
                <div class="legend-color fossil"></div>
                <span>Fossil Fuels (13,344.47 TWh)</span>
            </div>
            <div class="legend-item">
                <div class="legend-color renewable"></div>
                <span>Renewables (6,706.91 TWh)</span>
            </div>
            <div class="legend-item">
                <div class="legend-color nuclear"></div>
                <span>Nuclear (1,312.23 TWh)</span>
            </div>
        </div>
    </div>

    <!-- Top Countries -->
    <div class="top-countries">
        <h2 class="section-title">Top Electricity Countries</h2>
        <div class="countries-grid">
            <div class="country-list">
                <h4>🏠 Historical Leaders (2000-2020)</h4>
                <div class="country-item">
                    <span class="country-name">🇨🇳 China</span>
                    <span class="country-value">90,239.46 TWh</span>
                </div>
                <div class="country-item">
                    <span class="country-name">🇮🇳 India</span>
                    <span class="country-value">21,486.72 TWh</span>
                </div>
                <div class="country-item">
                    <span class="country-name">🇯🇵 Japan</span>
                    <span class="country-value">21,251.36 TWh</span>
                </div>
                <div class="country-item">
                    <span class="country-name">🇩🇪 Germany</span>
                    <span class="country-value">12,876.96 TWh</span>
                </div>
                <div class="country-item">
                    <span class="country-name">🇨🇦 Canada</span>
                    <span class="country-value">12,817.42 TWh</span>
                </div>
            </div>
            <div class="country-list">
                <h4>🔮 Future Leaders (2030)</h4>
                <div class="country-item">
                    <span class="country-name">🇨🇳 China</span>
                    <span class="country-value">10,925.11 TWh</span>
                </div>
                <div class="country-item">
                    <span class="country-name">🇮🇳 India</span>
                    <span class="country-value">2,058.37 TWh</span>
                </div>
                <div class="country-item">
                    <span class="country-name">🇯🇵 Japan</span>
                    <span class="country-value">952.00 TWh</span>
                </div>
                <div class="country-item">
                    <span class="country-name">🇧🇷 Brazil</span>
                    <span class="country-value">750.26 TWh</span>
                </div>
                <div class="country-item">
                    <span class="country-name">🇨🇦 Canada</span>
                    <span class="country-value">641.91 TWh</span>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>'''
    
    try:
        # Create the template file
        template_path = "sustainable_energy/dashboard/templates/dashboard/electricity.html"
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(electricity_html)
        
        print("✅ Created Electricity dashboard template")
        
        # Now update the views.py to add the electricity view
        views_path = "sustainable_energy/dashboard/views.py"
        
        # Read current views
        with open(views_path, 'r', encoding='utf-8') as f:
            views_content = f.read()
        
        # Add electricity view function
        electricity_view = '''

def electricity_dashboard(request):
    """Electricity Dashboard - Complete consumption and predictions analysis"""
    return render(request, 'dashboard/electricity.html')
'''
        
        # Add the view if it doesn't exist
        if 'def electricity_dashboard' not in views_content:
            views_content += electricity_view
            
            with open(views_path, 'w', encoding='utf-8') as f:
                f.write(views_content)
            
            print("✅ Added electricity_dashboard view to views.py")
        
        # Update URLs
        urls_path = "sustainable_energy/dashboard/urls.py"
        
        with open(urls_path, 'r', encoding='utf-8') as f:
            urls_content = f.read()
        
        # Add electricity URL pattern
        electricity_url = "    path('electricity/', views.electricity_dashboard, name='electricity_dashboard'),"
        
        if 'electricity/' not in urls_content:
            # Find the urlpatterns list and add the new URL
            if 'urlpatterns = [' in urls_content:
                insertion_point = urls_content.find('urlpatterns = [') + len('urlpatterns = [')
                urls_content = urls_content[:insertion_point] + '\n    ' + electricity_url + urls_content[insertion_point:]
                
                with open(urls_path, 'w', encoding='utf-8') as f:
                    f.write(urls_content)
                
                print("✅ Added electricity URL to urls.py")
        
        print("✅ Electricity Dashboard created successfully!")
        print("📝 Features added:")
        print("   ⚡ Grand total: 274,520.04 TWh")
        print("   🏠 Historical consumption: 252,987.47 TWh")
        print("   🔮 Future predictions: 21,532.57 TWh")
        print("   📊 Energy mix breakdowns (historical & future)")
        print("   🏆 Top countries analysis")
        print("   🌍 Global access statistics")
        print("🔗 Access via: /electricity/")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating Electricity dashboard: {e}")
        return False

if __name__ == "__main__":
    create_electricity_dashboard()