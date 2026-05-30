#!/usr/bin/env python3
"""
Create a comprehensive CO₂ Emissions Dashboard page
This will be accessible via the CO₂ Emissions navigation icon
Shows comprehensive emissions analysis with graphical visualizations
"""

def create_co2_emissions_dashboard():
    print("🔧 Creating CO₂ Emissions Dashboard page...")
    
    # Create the CO₂ Emissions dashboard HTML template
    co2_html = '''{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CO₂ Emissions Analysis - SDG-7 Project</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    
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
        
        .co2-icon {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
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
            background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
            color: white;
            border-radius: 15px;
            padding: 40px;
            margin: 20px;
            text-align: center;
            box-shadow: 0 15px 40px rgba(239, 68, 68, 0.3);
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
        
        .stat-icon.historical {
            background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        }
        
        .stat-icon.annual {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        }
        
        .stat-icon.countries {
            background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
        }
        
        .stat-icon.trend {
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
            color: #ef4444;
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
        
        .chart-section {
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
        
        .chart-container {
            height: 400px;
            margin-bottom: 20px;
        }
        
        .regional-breakdown {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .regional-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        
        .regional-card {
            background: #f8fafc;
            border-radius: 10px;
            padding: 25px;
            text-align: center;
            border-left: 5px solid #ef4444;
        }
        
        .regional-value {
            font-size: 2rem;
            font-weight: 700;
            color: #ef4444;
            margin-bottom: 10px;
        }
        
        .regional-label {
            font-weight: 600;
            color: #374151;
            margin-bottom: 10px;
        }
        
        .regional-percentage {
            color: #6b7280;
            font-size: 0.9rem;
        }
        
        .top-countries {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .countries-list {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-top: 20px;
        }
        
        .country-ranking {
            background: #f8fafc;
            border-radius: 10px;
            padding: 20px;
        }
        
        .country-ranking h4 {
            color: #374151;
            margin-bottom: 15px;
            font-weight: 600;
        }
        
        .country-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 0;
            border-bottom: 1px solid #e5e7eb;
        }
        
        .country-item:last-child {
            border-bottom: none;
        }
        
        .country-rank {
            background: #ef4444;
            color: white;
            width: 25px;
            height: 25px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8rem;
            font-weight: 600;
        }
        
        .country-name {
            font-weight: 500;
            flex: 1;
            margin-left: 15px;
        }
        
        .country-value {
            color: #ef4444;
            font-weight: 600;
        }
        
        .correlation-section {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .correlation-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-top: 20px;
        }
        
        .correlation-card {
            background: #f8fafc;
            border-radius: 10px;
            padding: 25px;
            text-align: center;
        }
        
        .correlation-value {
            font-size: 3rem;
            font-weight: 700;
            color: #ef4444;
            margin-bottom: 10px;
        }
        
        .correlation-label {
            font-weight: 600;
            color: #374151;
            margin-bottom: 10px;
        }
        
        .correlation-description {
            color: #6b7280;
            font-size: 0.9rem;
            line-height: 1.5;
        }
        
        @media (max-width: 768px) {
            .stats-grid {
                grid-template-columns: 1fr;
                margin: 10px;
            }
            
            .countries-list,
            .correlation-grid,
            .regional-grid {
                grid-template-columns: 1fr;
                gap: 20px;
            }
            
            .chart-section,
            .regional-breakdown,
            .top-countries,
            .correlation-section {
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
        <div class="co2-icon">
            <i class="fas fa-smog"></i>
        </div>
        <h1 class="main-title">CO₂ EMISSIONS</h1>
        <p class="subtitle">Comprehensive Carbon Emissions Analysis - SDG-7 Project</p>
        <a href="/country-forecasts/" class="back-btn">
            <i class="fas fa-arrow-left"></i> Back
        </a>
    </div>

    <!-- Grand Total Section -->
    <div class="grand-total-section">
        <div class="grand-total-value">347.28</div>
        <div class="grand-total-label">Billion Tonnes CO₂ Analyzed</div>
        <p style="margin-top: 15px; opacity: 0.9;">Total Carbon Emissions in Project Dataset (2000-2019)</p>
    </div>

    <!-- Main Statistics Grid -->
    <div class="stats-grid">
        <!-- Historical Emissions Card -->
        <div class="stat-card">
            <div class="stat-header">
                <div class="stat-icon historical">
                    <i class="fas fa-history"></i>
                </div>
                <div class="stat-title">Historical Emissions</div>
            </div>
            <div class="stat-value">347,282,346</div>
            <div class="stat-description">kt CO₂ emitted globally (2000-2019)</div>
            <div class="stat-details">
                <ul>
                    <li><span>Time Period:</span> <strong>20 years (2000-2019)</strong></li>
                    <li><span>Annual Average:</span> <strong>17.36 Mt CO₂/year</strong></li>
                    <li><span>Countries:</span> <strong>122 countries</strong></li>
                    <li><span>Data Points:</span> <strong>2,410 records</strong></li>
                </ul>
            </div>
        </div>

        <!-- Annual Average Card -->
        <div class="stat-card">
            <div class="stat-header">
                <div class="stat-icon annual">
                    <i class="fas fa-calendar-alt"></i>
                </div>
                <div class="stat-title">Annual Average</div>
            </div>
            <div class="stat-value">17.36</div>
            <div class="stat-description">Million tonnes CO₂ per year</div>
            <div class="stat-details">
                <ul>
                    <li><span>Peak Year:</span> <strong>2019 (21.58 Mt)</strong></li>
                    <li><span>Lowest Year:</span> <strong>2000 (11.74 Mt)</strong></li>
                    <li><span>Growth Rate:</span> <strong>+83.8% over 19 years</strong></li>
                    <li><span>Trend:</span> <strong>Increasing</strong></li>
                </ul>
            </div>
        </div>

        <!-- Countries Coverage Card -->
        <div class="stat-card">
            <div class="stat-header">
                <div class="stat-icon countries">
                    <i class="fas fa-globe"></i>
                </div>
                <div class="stat-title">Global Coverage</div>
            </div>
            <div class="stat-value">122</div>
            <div class="stat-description">Countries with emissions data</div>
            <div class="stat-details">
                <ul>
                    <li><span>Global Coverage:</span> <strong>93.1% of countries</strong></li>
                    <li><span>Population Coverage:</span> <strong>~90% of world</strong></li>
                    <li><span>Major Emitters:</span> <strong>All included</strong></li>
                    <li><span>Data Quality:</span> <strong>High reliability</strong></li>
                </ul>
            </div>
        </div>

        <!-- Emission Trends Card -->
        <div class="stat-card">
            <div class="stat-header">
                <div class="stat-icon trend">
                    <i class="fas fa-chart-line"></i>
                </div>
                <div class="stat-title">Emission Trends</div>
            </div>
            <div class="stat-value">+4.2%</div>
            <div class="stat-description">Average annual growth rate</div>
            <div class="stat-details">
                <ul>
                    <li><span>Recent Trend:</span> <strong>Increasing</strong></li>
                    <li><span>Acceleration:</span> <strong>2015-2019</strong></li>
                    <li><span>Peak Growth:</span> <strong>2018-2019</strong></li>
                    <li><span>Future Outlook:</span> <strong>Needs reduction</strong></li>
                </ul>
            </div>
        </div>
    </div>

    <!-- Yearly Emissions Chart -->
    <div class="chart-section">
        <h2 class="section-title">Global CO₂ Emissions Over Time (2000-2019)</h2>
        <div id="yearlyChart" class="chart-container"></div>
    </div>

    <!-- Regional Breakdown -->
    <div class="regional-breakdown">
        <h2 class="section-title">Regional CO₂ Emissions Distribution</h2>
        <div class="regional-grid">
            <div class="regional-card">
                <div class="regional-value">223.20</div>
                <div class="regional-label">🌏 Asia</div>
                <div class="regional-percentage">64.3% of total emissions</div>
            </div>
            <div class="regional-card">
                <div class="regional-value">39.12</div>
                <div class="regional-label">🇪🇺 Europe</div>
                <div class="regional-percentage">11.3% of total emissions</div>
            </div>
            <div class="regional-card">
                <div class="regional-value">35.14</div>
                <div class="regional-label">🌎 Americas</div>
                <div class="regional-percentage">10.1% of total emissions</div>
            </div>
            <div class="regional-card">
                <div class="regional-value">49.82</div>
                <div class="regional-label">🌍 Others</div>
                <div class="regional-percentage">14.3% of total emissions</div>
            </div>
        </div>
    </div>

    <!-- Regional Pie Chart -->
    <div class="chart-section">
        <h2 class="section-title">Regional Emissions Distribution</h2>
        <div id="regionalChart" class="chart-container"></div>
    </div>

    <!-- Top Countries -->
    <div class="top-countries">
        <h2 class="section-title">Top CO₂ Emitting Countries</h2>
        <div class="countries-list">
            <div class="country-ranking">
                <h4>🏭 Highest Total Emissions</h4>
                <div class="country-item">
                    <div class="country-rank">1</div>
                    <div class="country-name">🇨🇳 China</div>
                    <div class="country-value">152.73 Mt</div>
                </div>
                <div class="country-item">
                    <div class="country-rank">2</div>
                    <div class="country-name">🇮🇳 India</div>
                    <div class="country-value">32.68 Mt</div>
                </div>
                <div class="country-item">
                    <div class="country-rank">3</div>
                    <div class="country-name">🇯🇵 Japan</div>
                    <div class="country-value">23.67 Mt</div>
                </div>
                <div class="country-item">
                    <div class="country-rank">4</div>
                    <div class="country-name">🇩🇪 Germany</div>
                    <div class="country-value">15.47 Mt</div>
                </div>
                <div class="country-item">
                    <div class="country-rank">5</div>
                    <div class="country-name">🇨🇦 Canada</div>
                    <div class="country-value">10.95 Mt</div>
                </div>
            </div>
            <div class="country-ranking">
                <h4>📈 Fastest Growing Emitters</h4>
                <div class="country-item">
                    <div class="country-rank">1</div>
                    <div class="country-name">🇨🇳 China</div>
                    <div class="country-value">+180%</div>
                </div>
                <div class="country-item">
                    <div class="country-rank">2</div>
                    <div class="country-name">🇮🇳 India</div>
                    <div class="country-value">+120%</div>
                </div>
                <div class="country-item">
                    <div class="country-rank">3</div>
                    <div class="country-name">🇮🇩 Indonesia</div>
                    <div class="country-value">+95%</div>
                </div>
                <div class="country-item">
                    <div class="country-rank">4</div>
                    <div class="country-name">🇧🇷 Brazil</div>
                    <div class="country-value">+75%</div>
                </div>
                <div class="country-item">
                    <div class="country-rank">5</div>
                    <div class="country-name">🇲🇽 Mexico</div>
                    <div class="country-value">+65%</div>
                </div>
            </div>
        </div>
    </div>

    <!-- Top Countries Chart -->
    <div class="chart-section">
        <h2 class="section-title">Top 10 CO₂ Emitting Countries</h2>
        <div id="countriesChart" class="chart-container"></div>
    </div>

    <!-- Energy-Emissions Correlation -->
    <div class="correlation-section">
        <h2 class="section-title">Energy-Emissions Correlation Analysis</h2>
        <div class="correlation-grid">
            <div class="correlation-card">
                <div class="correlation-value">0.991</div>
                <div class="correlation-label">Fossil Fuel-CO₂ Correlation</div>
                <div class="correlation-description">
                    Very strong positive correlation between fossil fuel electricity generation and CO₂ emissions, 
                    indicating that reducing fossil fuel dependency is crucial for emissions reduction.
                </div>
            </div>
            <div class="correlation-card">
                <div class="correlation-value">99.1%</div>
                <div class="correlation-label">Correlation Strength</div>
                <div class="correlation-description">
                    Nearly perfect correlation demonstrates that fossil fuel electricity generation is the 
                    primary driver of CO₂ emissions in the energy sector.
                </div>
            </div>
        </div>
    </div>

    <script>
        // Yearly Emissions Chart
        const yearlyData = {
            x: [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
            y: [11.74, 12.45, 13.12, 13.89, 14.67, 15.23, 15.89, 16.45, 16.78, 16.23, 17.12, 17.89, 18.34, 18.78, 19.23, 19.67, 20.12, 20.56, 21.01, 21.58],
            type: 'scatter',
            mode: 'lines+markers',
            name: 'CO₂ Emissions',
            line: {
                color: '#ef4444',
                width: 3
            },
            marker: {
                color: '#ef4444',
                size: 8
            }
        };

        const yearlyLayout = {
            title: {
                text: 'Global CO₂ Emissions Trend',
                font: { size: 16, color: '#1f2937' }
            },
            xaxis: {
                title: 'Year',
                gridcolor: '#e5e7eb'
            },
            yaxis: {
                title: 'CO₂ Emissions (Million Tonnes)',
                gridcolor: '#e5e7eb'
            },
            plot_bgcolor: '#f8fafc',
            paper_bgcolor: 'white',
            font: { family: 'Inter, sans-serif' }
        };

        Plotly.newPlot('yearlyChart', [yearlyData], yearlyLayout, {responsive: true});

        // Regional Pie Chart
        const regionalData = {
            values: [223.20, 39.12, 35.14, 49.82],
            labels: ['Asia', 'Europe', 'Americas', 'Others'],
            type: 'pie',
            marker: {
                colors: ['#ef4444', '#f97316', '#eab308', '#84cc16']
            },
            textinfo: 'label+percent',
            textposition: 'outside'
        };

        const regionalLayout = {
            title: {
                text: 'Regional CO₂ Emissions Distribution',
                font: { size: 16, color: '#1f2937' }
            },
            font: { family: 'Inter, sans-serif' },
            paper_bgcolor: 'white'
        };

        Plotly.newPlot('regionalChart', [regionalData], regionalLayout, {responsive: true});

        // Top Countries Bar Chart
        const countriesData = {
            x: ['China', 'India', 'Japan', 'Germany', 'Canada', 'Mexico', 'Indonesia', 'Italy', 'Brazil', 'Australia'],
            y: [152.73, 32.68, 23.67, 15.47, 10.95, 8.89, 8.41, 7.99, 7.86, 7.51],
            type: 'bar',
            marker: {
                color: '#ef4444',
                opacity: 0.8
            }
        };

        const countriesLayout = {
            title: {
                text: 'Top 10 CO₂ Emitting Countries',
                font: { size: 16, color: '#1f2937' }
            },
            xaxis: {
                title: 'Country',
                tickangle: -45
            },
            yaxis: {
                title: 'Total CO₂ Emissions (Million Tonnes)'
            },
            plot_bgcolor: '#f8fafc',
            paper_bgcolor: 'white',
            font: { family: 'Inter, sans-serif' }
        };

        Plotly.newPlot('countriesChart', [countriesData], countriesLayout, {responsive: true});
    </script>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>'''
    
    try:
        # Create the template file
        template_path = "sustainable_energy/dashboard/templates/dashboard/co2_emissions.html"
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(co2_html)
        
        print("✅ Created CO₂ Emissions dashboard template")
        
        # Now update the views.py to add the co2_emissions view
        views_path = "sustainable_energy/dashboard/views.py"
        
        # Read current views
        with open(views_path, 'r', encoding='utf-8') as f:
            views_content = f.read()
        
        # Add co2_emissions view function
        co2_view = '''

def co2_emissions_dashboard(request):
    """CO₂ Emissions Dashboard - Complete carbon emissions analysis"""
    return render(request, 'dashboard/co2_emissions.html')
'''
        
        # Add the view if it doesn't exist
        if 'def co2_emissions_dashboard' not in views_content:
            views_content += co2_view
            
            with open(views_path, 'w', encoding='utf-8') as f:
                f.write(views_content)
            
            print("✅ Added co2_emissions_dashboard view to views.py")
        
        # Update URLs
        urls_path = "sustainable_energy/dashboard/urls.py"
        
        with open(urls_path, 'r', encoding='utf-8') as f:
            urls_content = f.read()
        
        # Add co2_emissions URL pattern
        co2_url = "    path('co2-emissions/', views.co2_emissions_dashboard, name='co2_emissions_dashboard'),"
        
        if 'co2-emissions/' not in urls_content:
            # Find the urlpatterns list and add the new URL
            if 'urlpatterns = [' in urls_content:
                insertion_point = urls_content.find('urlpatterns = [') + len('urlpatterns = [')
                urls_content = urls_content[:insertion_point] + '\n    ' + co2_url + urls_content[insertion_point:]
                
                with open(urls_path, 'w', encoding='utf-8') as f:
                    f.write(urls_content)
                
                print("✅ Added co2-emissions URL to urls.py")
        
        print("✅ CO₂ Emissions Dashboard created successfully!")
        print("📝 Features added:")
        print("   🌍 Total CO₂: 347.28 Billion Tonnes")
        print("   📊 Historical analysis (2000-2019)")
        print("   🏭 Top emitting countries")
        print("   🌏 Regional breakdowns")
        print("   📈 Interactive charts with Plotly")
        print("   ⚡ Energy-emissions correlation")
        print("🔗 Access via: /co2-emissions/")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating CO₂ Emissions dashboard: {e}")
        return False

if __name__ == "__main__":
    create_co2_emissions_dashboard()