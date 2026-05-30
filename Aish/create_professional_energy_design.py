#!/usr/bin/env python3

"""
Create a professional energy website design matching the EnerOutlook style
"""

def create_professional_energy_design():
    """Transform the website to match the professional EnerOutlook design"""
    
    # Update Objective Selector with professional energy design
    selector_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    # Create the new professional design matching the image
    new_professional_design = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Energy & Emissions Projections 2050 - EnerOutlook</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Roboto', sans-serif;
            background: #f8f9fa;
            color: #333;
        }
        
        /* Header Navigation */
        .top-header {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 15px 0;
        }
        
        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 20px;
        }
        
        .logo-section {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .logo {
            width: 50px;
            height: 50px;
            background: #00bcd4;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            font-weight: bold;
        }
        
        .site-title {
            font-size: 1.8rem;
            font-weight: 500;
            margin: 0;
        }
        
        .nav-links {
            display: flex;
            gap: 30px;
            align-items: center;
        }
        
        .nav-link {
            color: white;
            text-decoration: none;
            font-weight: 500;
            padding: 8px 16px;
            border-radius: 20px;
            transition: all 0.3s ease;
        }
        
        .nav-link:hover {
            background: rgba(255, 255, 255, 0.1);
            color: white;
        }
        
        /* Main Navigation Bar */
        .main-nav {
            background: white;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            padding: 0;
        }
        
        .nav-tabs {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            border: none;
            padding: 0 20px;
        }
        
        .nav-tab {
            flex: 1;
            text-align: center;
            padding: 20px 15px;
            border: none;
            background: none;
            color: #666;
            font-weight: 500;
            text-decoration: none;
            transition: all 0.3s ease;
            position: relative;
        }
        
        .nav-tab:hover,
        .nav-tab.active {
            color: #1e3c72;
            background: #f8f9fa;
        }
        
        .nav-tab i {
            display: block;
            font-size: 2rem;
            margin-bottom: 8px;
            color: #ff6b35;
        }
        
        .nav-tab .tab-title {
            font-size: 0.9rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        /* Hero Section */
        .hero-section {
            background: linear-gradient(rgba(30, 60, 114, 0.8), rgba(42, 82, 152, 0.8)), 
                        url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600"><defs><pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="1"/></pattern></defs><rect width="100%" height="100%" fill="url(%23grid)"/></svg>');
            background-size: cover;
            background-position: center;
            color: white;
            padding: 80px 0;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .hero-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600"><circle cx="200" cy="150" r="3" fill="rgba(255,255,255,0.3)"/><circle cx="400" cy="250" r="2" fill="rgba(255,255,255,0.4)"/><circle cx="600" cy="180" r="4" fill="rgba(255,255,255,0.2)"/><circle cx="800" cy="320" r="3" fill="rgba(255,255,255,0.3)"/><circle cx="1000" cy="200" r="2" fill="rgba(255,255,255,0.4)"/></svg>');
            animation: float 20s linear infinite;
        }
        
        @keyframes float {
            0% { transform: translateX(0); }
            100% { transform: translateX(-100px); }
        }
        
        .hero-content {
            max-width: 800px;
            margin: 0 auto;
            position: relative;
            z-index: 2;
        }
        
        .hero-title {
            font-size: 3rem;
            font-weight: 300;
            margin-bottom: 20px;
            line-height: 1.2;
        }
        
        .hero-subtitle {
            font-size: 1.3rem;
            font-weight: 400;
            margin-bottom: 40px;
            opacity: 0.9;
        }
        
        /* Content Section */
        .content-section {
            max-width: 1200px;
            margin: 60px auto;
            padding: 0 20px;
        }
        
        .section-header {
            background: white;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            margin-bottom: 40px;
        }
        
        .section-title {
            color: #1e3c72;
            font-size: 1.8rem;
            font-weight: 500;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .section-icon {
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, #00bcd4 0%, #0097a7 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.2rem;
        }
        
        .section-description {
            color: #666;
            font-size: 1.1rem;
            line-height: 1.6;
            margin-bottom: 25px;
        }
        
        .feature-list {
            list-style: none;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin-bottom: 30px;
        }
        
        .feature-item {
            display: flex;
            align-items: center;
            gap: 10px;
            color: #555;
            font-weight: 500;
        }
        
        .feature-item i {
            color: #00bcd4;
            font-size: 1.1rem;
        }
        
        .cta-button {
            background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
            color: white;
            border: none;
            padding: 15px 40px;
            border-radius: 30px;
            font-size: 1.1rem;
            font-weight: 600;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(255, 107, 53, 0.3);
        }
        
        .cta-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(255, 107, 53, 0.4);
            color: white;
        }
        
        /* Dashboard Grid */
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }
        
        .dashboard-card {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            border-left: 5px solid #00bcd4;
        }
        
        .dashboard-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        }
        
        .card-header {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 20px;
        }
        
        .card-icon {
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.5rem;
        }
        
        .card-title {
            color: #1e3c72;
            font-size: 1.3rem;
            font-weight: 600;
            margin: 0;
        }
        
        .card-description {
            color: #666;
            line-height: 1.6;
            margin-bottom: 20px;
        }
        
        .card-features {
            list-style: none;
            margin-bottom: 25px;
        }
        
        .card-features li {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 8px;
            color: #555;
        }
        
        .card-features li::before {
            content: "✓";
            color: #00bcd4;
            font-weight: bold;
            font-size: 1.1rem;
        }
        
        .card-button {
            background: #1e3c72;
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 25px;
            font-weight: 500;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.3s ease;
        }
        
        .card-button:hover {
            background: #2a5298;
            transform: translateX(5px);
            color: white;
        }
        
        /* Footer */
        .footer {
            background: #1e3c72;
            color: white;
            text-align: center;
            padding: 40px 20px;
            margin-top: 80px;
        }
        
        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .nav-container {
                flex-direction: column;
                gap: 20px;
            }
            
            .nav-links {
                gap: 15px;
            }
            
            .nav-tabs {
                flex-direction: column;
            }
            
            .nav-tab {
                padding: 15px;
            }
            
            .hero-title {
                font-size: 2.2rem;
            }
            
            .dashboard-grid {
                grid-template-columns: 1fr;
                gap: 20px;
            }
        }
    </style>
</head>
<body>
    <!-- Top Header -->
    <header class="top-header">
        <div class="nav-container">
            <div class="logo-section">
                <div class="logo">E</div>
                <h1 class="site-title">Energy & emissions projections 2050 - EnerOutlook</h1>
            </div>
            <nav class="nav-links">
                <a href="#" class="nav-link">2025 Edition</a>
                <a href="#" class="nav-link">GLOSSARY</a>
                <a href="#" class="nav-link">SCENARIO DESCRIPTION</a>
                <a href="#" class="nav-link">LOGIN/REGISTER</a>
            </nav>
        </div>
    </header>

    <!-- Main Navigation -->
    <nav class="main-nav">
        <div class="nav-tabs">
            <a href="#" class="nav-tab active">
                <i class="fas fa-bolt"></i>
                <div class="tab-title">Total Energy</div>
            </a>
            <a href="#" class="nav-tab">
                <i class="fas fa-plug"></i>
                <div class="tab-title">Electricity</div>
            </a>
            <a href="#" class="nav-tab">
                <i class="fas fa-leaf"></i>
                <div class="tab-title">Renewables</div>
            </a>
            <a href="#" class="nav-tab">
                <i class="fas fa-smog"></i>
                <div class="tab-title">CO2 Emissions</div>
            </a>
            <a href="#" class="nav-tab">
                <i class="fas fa-globe"></i>
                <div class="tab-title">Country Energy Forecasts</div>
            </a>
            <a href="#" class="nav-tab">
                <i class="fas fa-arrow-right"></i>
                <div class="tab-title">More Projections</div>
            </a>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-section">
        <div class="hero-content">
            <h2 class="hero-title">TOWARDS AFFORDABLE AND CLEAN ENERGY</h2>
            <p class="hero-subtitle">A PREDICTIVE AND STRATEGIC FRAMEWORK FOR SDG 7</p>
        </div>
    </section>

    <!-- Main Content -->
    <main class="content-section">
        <!-- More Projections Section -->
        <div class="section-header">
            <h2 class="section-title">
                <div class="section-icon">
                    <i class="fas fa-chart-line"></i>
                </div>
                More projections
            </h2>
            <p class="section-description">
                The series contained in this interface are a short excerpt of the data available in enerdata's EnerFuture service. The complete service provides:
            </p>
            <ul class="feature-list">
                <li class="feature-item">
                    <i class="fas fa-check-circle"></i>
                    Many other series including end-user prices, electricity generation and capacities by energy source, etc.
                </li>
                <li class="feature-item">
                    <i class="fas fa-check-circle"></i>
                    Extended global coverage including 186 countries and regional aggregates.
                </li>
                <li class="feature-item">
                    <i class="fas fa-check-circle"></i>
                    Additional scenarios: whereas the data in enerOutlook corresponds to the EnerBlue scenario (NDC achievement), two other scenarios are provided in EnerFuture: EnerBase (current policies) and EnerGreen (2°C scenario).
                </li>
            </ul>
        </div>

        <!-- Dashboard Grid -->
        <div class="dashboard-grid">
            <!-- Full Dashboard Card -->
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-tachometer-alt"></i>
                    </div>
                    <h3 class="card-title">Full Dashboard: Comprehensive Analysis</h3>
                </div>
                <p class="card-description">Complete energy analysis with world map and status alerts</p>
                <ul class="card-features">
                    <li>World map visualization</li>
                    <li>7 ML models comparison</li>
                    <li>Real-time status alerts</li>
                    <li>Interactive country analysis</li>
                </ul>
                <a href="/dashboard/" class="card-button">
                    <span>Explore Dashboard</span>
                    <i class="fas fa-arrow-right"></i>
                </a>
            </div>

            <!-- ML Comparison Card -->
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-brain"></i>
                    </div>
                    <h3 class="card-title">Comprehensive ML Comparison</h3>
                </div>
                <p class="card-description">Compare ML algorithms across all 8 objectives with detailed performance metrics</p>
                <ul class="card-features">
                    <li>8 different ML objectives</li>
                    <li>Algorithm performance metrics</li>
                    <li>Visual model comparison</li>
                    <li>Best model recommendations</li>
                </ul>
                <a href="/comprehensive-comparison/" class="card-button">
                    <span>Compare Models</span>
                    <i class="fas fa-arrow-right"></i>
                </a>
            </div>

            <!-- Objective 4 Card -->
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-chart-bar"></i>
                    </div>
                    <h3 class="card-title">SDG 7 Monitoring Dashboard</h3>
                </div>
                <p class="card-description">Monitor progress towards Sustainable Development Goal 7 with advanced analytics</p>
                <ul class="card-features">
                    <li>Interactive country analysis</li>
                    <li>Historical electricity access trends</li>
                    <li>Future predictions (7 years)</li>
                    <li>ML-powered forecasting</li>
                </ul>
                <a href="/objective4/" class="card-button">
                    <span>View SDG 7 Analysis</span>
                    <i class="fas fa-arrow-right"></i>
                </a>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="footer-content">
            <p>&copy; 2025 EnerOutlook - Energy & Emissions Projections. All rights reserved.</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Add smooth scrolling and interactive effects
        document.addEventListener('DOMContentLoaded', function() {
            // Smooth hover effects for cards
            const cards = document.querySelectorAll('.dashboard-card');
            cards.forEach(card => {
                card.addEventListener('mouseenter', function() {
                    this.style.transform = 'translateY(-5px)';
                });
                
                card.addEventListener('mouseleave', function() {
                    this.style.transform = 'translateY(0)';
                });
            });
            
            // Active tab functionality
            const navTabs = document.querySelectorAll('.nav-tab');
            navTabs.forEach(tab => {
                tab.addEventListener('click', function(e) {
                    e.preventDefault();
                    navTabs.forEach(t => t.classList.remove('active'));
                    this.classList.add('active');
                });
            });
        });
    </script>
</body>
</html>'''
    
    # Write the new professional design
    with open(selector_path, 'w', encoding='utf-8') as f:
        f.write(new_professional_design)
    
    print("✅ Created professional EnerOutlook-style design!")
    print("\n🎯 Professional Features Added:")
    print("   - Blue gradient header matching the image")
    print("   - Navigation tabs with icons (Total Energy, Electricity, etc.)")
    print("   - Professional typography (Roboto font)")
    print("   - Clean white cards with subtle shadows")
    print("   - Orange accent buttons")
    print("   - Grid pattern background in hero section")
    print("   - Responsive design for all devices")
    print("   - Professional color scheme (blues, whites, orange)")

if __name__ == "__main__":
    create_professional_energy_design()