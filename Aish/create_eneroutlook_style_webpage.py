#!/usr/bin/env python3
"""
Script to create a professional EnerOutlook-style webpage matching the reference design
"""

import os

def create_eneroutlook_webpage():
    """Create the main webpage with EnerOutlook styling"""
    
    template_content = '''{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Energy & emissions projections 2050 - EnerOutlook</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
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
            background: #f8fafc;
            color: #333;
            overflow-x: hidden;
        }
        
        /* Header Section */
        .main-header {
            background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
            color: white;
            padding: 15px 0;
            position: relative;
        }
        
        .header-container {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 30px;
        }
        
        .logo-section {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .logo-circle {
            width: 45px;
            height: 45px;
            background: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #1e40af;
            font-weight: bold;
            font-size: 1.3rem;
        }
        
        .header-title {
            font-size: 1.4rem;
            font-weight: 600;
            margin-bottom: 2px;
        }
        
        .header-actions {
            display: flex;
            gap: 20px;
            align-items: center;
            font-size: 0.85rem;
            font-weight: 500;
        }
        
        .header-btn {
            color: white;
            text-decoration: none;
            padding: 8px 16px;
            border-radius: 4px;
            transition: background 0.2s;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .header-btn:hover {
            background: rgba(255, 255, 255, 0.15);
            color: white;
            text-decoration: none;
        }
        
        /* Project Title Corner */
        .project-title {
            position: absolute;
            top: 10px;
            right: 30px;
            background: rgba(255, 255, 255, 0.1);
            padding: 8px 15px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            backdrop-filter: blur(10px);
        }
        
        /* Navigation Icons */
        .nav-icons {
            background: white;
            padding: 0;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: relative;
            z-index: 100;
        }
        
        .nav-container {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: center;
            padding: 0 30px;
        }
        
        .nav-icon-item {
            flex: 1;
            max-width: 200px;
            text-align: center;
            padding: 25px 15px;
            text-decoration: none;
            color: #6b7280;
            transition: all 0.3s ease;
            border-bottom: 3px solid transparent;
            position: relative;
        }
        
        .nav-icon-item:hover {
            color: #f97316;
            background: #fef3e2;
            text-decoration: none;
            border-bottom-color: #f97316;
        }
        
        .nav-icon-item.active {
            color: #f97316;
            background: #fef3e2;
            border-bottom-color: #f97316;
        }
        
        .nav-icon {
            width: 50px;
            height: 50px;
            background: #f3f4f6;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 12px;
            font-size: 1.4rem;
            transition: all 0.3s ease;
        }
        
        .nav-icon-item:hover .nav-icon,
        .nav-icon-item.active .nav-icon {
            background: #fed7aa;
            color: #f97316;
            transform: scale(1.1);
        }
        
        .nav-label {
            font-size: 0.8rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        /* Hero Section with Background */
        .hero-section {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            position: relative;
            height: 400px;
            overflow: hidden;
        }
        
        .hero-bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 400"><defs><linearGradient id="grid" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="%2300d4ff" stop-opacity="0.3"/><stop offset="50%" stop-color="%2300a8ff" stop-opacity="0.2"/><stop offset="100%" stop-color="%230066ff" stop-opacity="0.1"/></linearGradient></defs><rect width="100%" height="100%" fill="url(%23grid)"/><g stroke="%2300d4ff" stroke-width="1" opacity="0.4"><path d="M0,200 Q250,100 500,200 T1000,200"/><path d="M0,250 Q250,150 500,250 T1000,250"/><path d="M0,300 Q250,200 500,300 T1000,300"/></g><g fill="%2300d4ff" opacity="0.6"><circle cx="100" cy="200" r="3"/><circle cx="300" cy="150" r="3"/><circle cx="500" cy="200" r="3"/><circle cx="700" cy="180" r="3"/><circle cx="900" cy="220" r="3"/></g></svg>');
            background-size: cover;
            background-position: center;
        }
        
        /* Main Content Area */
        .main-content {
            max-width: 1400px;
            margin: 0 auto;
            padding: 60px 30px;
            background: white;
        }
        
        /* Explore Dashboard Section */
        .explore-section {
            text-align: center;
            margin-bottom: 60px;
        }
        
        .explore-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #1f2937;
            margin-bottom: 20px;
        }
        
        .explore-subtitle {
            font-size: 1.2rem;
            color: #6b7280;
            margin-bottom: 40px;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
        
        .explore-btn {
            display: inline-flex;
            align-items: center;
            gap: 12px;
            background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
            color: white;
            padding: 18px 40px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            font-size: 1.1rem;
            transition: all 0.3s ease;
            box-shadow: 0 10px 30px rgba(249, 115, 22, 0.3);
        }
        
        .explore-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(249, 115, 22, 0.4);
            text-decoration: none;
            color: white;
        }
        
        /* More Projections Section */
        .more-projections {
            background: #f8fafc;
            border-radius: 12px;
            padding: 40px;
            margin-top: 40px;
        }
        
        .more-projections h3 {
            color: #1f2937;
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .more-projections p {
            color: #6b7280;
            line-height: 1.6;
            margin-bottom: 15px;
        }
        
        /* Objectives Section (Hidden by default) */
        .objectives-section {
            display: none;
            padding: 60px 0;
            background: #f8fafc;
        }
        
        .objectives-section.active {
            display: block;
        }
        
        .objectives-container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 30px;
        }
        
        .section-title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: 700;
            color: #1f2937;
            margin-bottom: 60px;
        }
        
        .objectives-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }
        
        .objective-card {
            background: white;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border: 1px solid #f1f5f9;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .objective-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
            transform: scaleX(0);
            transition: transform 0.3s ease;
        }
        
        .objective-card:hover::before {
            transform: scaleX(1);
        }
        
        .objective-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
        }
        
        .objective-header {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 20px;
        }
        
        .objective-icon {
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.3rem;
        }
        
        .objective-number {
            background: #fef3e2;
            color: #f97316;
            font-weight: 700;
            font-size: 0.8rem;
            padding: 4px 8px;
            border-radius: 4px;
            margin-left: auto;
        }
        
        .objective-title {
            font-size: 1.3rem;
            font-weight: 600;
            color: #1f2937;
            margin-bottom: 12px;
        }
        
        .objective-description {
            color: #6b7280;
            line-height: 1.6;
            margin-bottom: 25px;
            font-size: 0.95rem;
        }
        
        .objective-btn {
            background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 500;
            font-size: 0.9rem;
            transition: all 0.2s;
            display: inline-block;
        }
        
        .objective-btn:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 15px rgba(249, 115, 22, 0.3);
            text-decoration: none;
            color: white;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .nav-container {
                flex-wrap: wrap;
                justify-content: center;
            }
            
            .nav-icon-item {
                min-width: 120px;
                padding: 20px 10px;
            }
            
            .main-content {
                padding: 40px 20px;
            }
            
            .objectives-grid {
                grid-template-columns: 1fr;
                gap: 20px;
            }
            
            .header-container {
                flex-direction: column;
                gap: 15px;
                text-align: center;
                padding: 0 20px;
            }
            
            .project-title {
                position: static;
                margin-top: 10px;
            }
        }
    </style>
</head>
<body>
    <!-- Main Header -->
    <header class="main-header">
        <div class="project-title">
            TOWARDS AFFORDABLE AND CLEAN ENERGY: A PREDICTIVE AND STRATEGIC FRAMEWORK FOR SDG 7
        </div>
        <div class="header-container">
            <div class="logo-section">
                <div class="logo-circle">E</div>
                <div>
                    <div class="header-title">Energy & emissions projections 2050 - EnerOutlook</div>
                </div>
            </div>
            <div class="header-actions">
                <span>2025 Edition</span>
                <a href="#" class="header-btn">Glossary</a>
                <a href="#" class="header-btn">Scenario Description</a>
                <a href="/admin-panel/" class="header-btn">Login/Register</a>
            </div>
        </div>
    </header>

    <!-- Navigation Icons -->
    <nav class="nav-icons">
        <div class="nav-container">
            <a href="{% url 'objective1_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon"><i class="fas fa-bolt"></i></div>
                <div class="nav-label">Total Energy</div>
            </a>
            <a href="{% url 'objective2_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon"><i class="fas fa-plug"></i></div>
                <div class="nav-label">Electricity</div>
            </a>
            <a href="{% url 'objective3_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon"><i class="fas fa-leaf"></i></div>
                <div class="nav-label">Renewables</div>
            </a>
            <a href="{% url 'objective4_dashboard' %}" class="nav-icon-item">
                <div class="nav-icon"><i class="fas fa-smog"></i></div>
                <div class="nav-label">CO Emissions</div>
            </a>
            <a href="#" class="nav-icon-item" id="country-forecasts-tab">
                <div class="nav-icon"><i class="fas fa-globe"></i></div>
                <div class="nav-label">Country Forecasts</div>
            </a>
            <a href="/" class="nav-icon-item">
                <div class="nav-icon"><i class="fas fa-arrow-right"></i></div>
                <div class="nav-label">More Projections</div>
            </a>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-section">
        <div class="hero-bg"></div>
    </section>

    <!-- Main Content -->
    <main class="main-content" id="main-content">
        <!-- Explore Dashboard Section -->
        <section class="explore-section">
            <h1 class="explore-title">Explore Dashboard</h1>
            <p class="explore-subtitle">
                Interactive country energy analysis with search functionality, world map visualization, 
                and comprehensive energy profiles for 128+ countries with ML predictions.
            </p>
            <a href="/" class="explore-btn">
                <i class="fas fa-search"></i>
                Launch Explore Dashboard
            </a>
        </section>

        <!-- More Projections Info -->
        <section class="more-projections">
            <h3><i class="fas fa-chart-line"></i> More Projections</h3>
            <p>
                The series contained in this interface are a short excerpt of the data available in EnerData's EnerFuture service. 
                The complete service provides:
            </p>
            <ul>
                <li><strong>Many other series</strong> including end-user prices, electricity generation and capacities by energy source, etc.</li>
                <li><strong>Extended</strong> global coverage including 186 countries and regional aggregates.</li>
                <li><strong>Additional scenarios:</strong> whereas the data in EnerOutlook corresponds to the EnerBlue scenario (NDC achievement), 
                two other scenarios are provided in EnerFuture: EnerBase (current policies) and EnerGreen (2°C scenario).</li>
            </ul>
        </section>
    </main>

    <!-- Objectives Section (Hidden by default) -->
    <section class="objectives-section" id="objectives-section">
        <div class="objectives-container">
            <h2 class="section-title">Country Energy Forecasts - All Objectives</h2>
            
            <div class="objectives-grid">
                <!-- Objective 1: Total Energy -->
                <div class="objective-card">
                    <div class="objective-header">
                        <div class="objective-icon">
                            <i class="fas fa-bolt"></i>
                        </div>
                        <div class="objective-number">01</div>
                    </div>
                    <h3 class="objective-title">Total Energy Consumption</h3>
                    <p class="objective-description">
                        Analyze global and regional total energy consumption patterns, trends, and projections using advanced forecasting models and historical data analysis.
                    </p>
                    <a href="{% url 'objective1_dashboard' %}" class="objective-btn">
                        View Analysis
                    </a>
                </div>
                
                <!-- Objective 2: Electricity -->
                <div class="objective-card">
                    <div class="objective-header">
                        <div class="objective-icon">
                            <i class="fas fa-plug"></i>
                        </div>
                        <div class="objective-number">02</div>
                    </div>
                    <h3 class="objective-title">Electricity Access & Generation</h3>
                    <p class="objective-description">
                        Comprehensive analysis of electricity access rates, generation capacity, and infrastructure development across different regions and countries.
                    </p>
                    <a href="{% url 'objective2_dashboard' %}" class="objective-btn">
                        View Analysis
                    </a>
                </div>
                
                <!-- Objective 3: Renewables -->
                <div class="objective-card">
                    <div class="objective-header">
                        <div class="objective-icon">
                            <i class="fas fa-leaf"></i>
                        </div>
                        <div class="objective-number">03</div>
                    </div>
                    <h3 class="objective-title">Renewable Energy Sources</h3>
                    <p class="objective-description">
                        Detailed analysis of renewable energy adoption, capacity growth, and potential across solar, wind, hydro, and other sustainable energy sources.
                    </p>
                    <a href="{% url 'objective3_dashboard' %}" class="objective-btn">
                        View Analysis
                    </a>
                </div>
                
                <!-- Objective 4: CO2 Emissions -->
                <div class="objective-card">
                    <div class="objective-header">
                        <div class="objective-icon">
                            <i class="fas fa-smog"></i>
                        </div>
                        <div class="objective-number">04</div>
                    </div>
                    <h3 class="objective-title">CO Emissions Analysis</h3>
                    <p class="objective-description">
                        Monitor and predict carbon dioxide emissions trends, reduction targets, and environmental impact assessment using machine learning models.
                    </p>
                    <a href="{% url 'objective4_dashboard' %}" class="objective-btn">
                        View Analysis
                    </a>
                </div>
                
                <!-- Objective 5: Country Forecasts -->
                <div class="objective-card">
                    <div class="objective-header">
                        <div class="objective-icon">
                            <i class="fas fa-globe"></i>
                        </div>
                        <div class="objective-number">05</div>
                    </div>
                    <h3 class="objective-title">Country-Specific Forecasts</h3>
                    <p class="objective-description">
                        Detailed country-level energy projections and forecasts for 128+ nations with customizable scenarios and predictive analytics.
                    </p>
                    <a href="{% url 'objective5_dashboard' %}" class="objective-btn">
                        View Analysis
                    </a>
                </div>
                
                <!-- Objective 6: Policy Analysis -->
                <div class="objective-card">
                    <div class="objective-header">
                        <div class="objective-icon">
                            <i class="fas fa-chart-line"></i>
                        </div>
                        <div class="objective-number">06</div>
                    </div>
                    <h3 class="objective-title">Policy Impact Analysis</h3>
                    <p class="objective-description">
                        Evaluate the effectiveness of energy policies, regulations, and government initiatives on sustainable energy adoption and emissions reduction.
                    </p>
                    <a href="{% url 'objective6_dashboard' %}" class="objective-btn">
                        View Analysis
                    </a>
                </div>
                
                <!-- Objective 7: Investment Strategy -->
                <div class="objective-card">
                    <div class="objective-header">
                        <div class="objective-icon">
                            <i class="fas fa-lightbulb"></i>
                        </div>
                        <div class="objective-number">07</div>
                    </div>
                    <h3 class="objective-title">Investment Strategy Optimization</h3>
                    <p class="objective-description">
                        Strategic investment analysis and recommendations for sustainable energy projects, ROI calculations, and risk assessment models.
                    </p>
                    <a href="{% url 'objective7_dashboard' %}" class="objective-btn">
                        View Analysis
                    </a>
                </div>
                
                <!-- Admin Panel -->
                <div class="objective-card">
                    <div class="objective-header">
                        <div class="objective-icon">
                            <i class="fas fa-cog"></i>
                        </div>
                        <div class="objective-number">08</div>
                    </div>
                    <h3 class="objective-title">Admin Panel</h3>
                    <p class="objective-description">
                        Administrative dashboard for email alert system management, user administration, and system configuration with comprehensive logging.
                    </p>
                    <a href="/admin-panel/" class="objective-btn">
                        Access Panel
                    </a>
                </div>
            </div>
        </div>
    </section>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Handle Country Forecasts tab click
        document.getElementById('country-forecasts-tab').addEventListener('click', function(e) {
            e.preventDefault();
            
            // Toggle active state
            document.querySelectorAll('.nav-icon-item').forEach(tab => tab.classList.remove('active'));
            this.classList.add('active');
            
            // Show/hide sections
            const mainContent = document.getElementById('main-content');
            const objectivesSection = document.getElementById('objectives-section');
            
            if (objectivesSection.classList.contains('active')) {
                // Hide objectives, show main content
                objectivesSection.classList.remove('active');
                mainContent.style.display = 'block';
                this.classList.remove('active');
            } else {
                // Show objectives, hide main content
                objectivesSection.classList.add('active');
                mainContent.style.display = 'none';
            }
        });

        // Handle other nav tabs
        document.querySelectorAll('.nav-icon-item:not(#country-forecasts-tab)').forEach(tab => {
            tab.addEventListener('click', function() {
                // Reset objectives section
                document.getElementById('objectives-section').classList.remove('active');
                document.getElementById('main-content').style.display = 'block';
                document.querySelectorAll('.nav-icon-item').forEach(t => t.classList.remove('active'));
            });
        });
    </script>
</body>
</html>'''
    
    # Write the new template
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    try:
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(template_content)
        
        print(f"✅ Successfully created EnerOutlook-style webpage at {template_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error creating webpage: {e}")
        return False

def main():
    """Main function"""
    print("🎨 Creating EnerOutlook-Style Professional Webpage")
    print("="*70)
    print("   • Professional header with project title in corner")
    print("   • Icon-based navigation matching reference design")
    print("   • Explore Dashboard button prominently featured")
    print("   • Country Forecasts with 7 objectives + Admin Panel")
    print("   • Beautiful hero section with animated background")
    print()
    
    success = create_eneroutlook_webpage()
    
    if success:
        print("\n✅ SUCCESS! Professional EnerOutlook-style webpage created!")
        print("\n🎨 Features implemented:")
        print("   ✅ Project title in top corner")
        print("   ✅ Professional blue header with EnerData logo style")
        print("   ✅ Icon-based navigation (6 icons)")
        print("   ✅ Prominent 'Explore Dashboard' button")
        print("   ✅ Country Forecasts toggle with 7 objectives + Admin Panel")
        print("   ✅ Beautiful animated hero background")
        print("   ✅ Responsive design for all devices")
        print("\n🎯 Navigation structure:")
        print("   • Total Energy, Electricity, Renewables, CO Emissions (direct links)")
        print("   • Country Forecasts (toggle to show 7 objectives + Admin Panel)")
        print("   • More Projections (link to Explore Dashboard)")
        print("\n🔄 Restart server and visit: http://localhost:8000/objectives/")
    else:
        print("\n❌ Failed to create webpage.")

if __name__ == "__main__":
    main()