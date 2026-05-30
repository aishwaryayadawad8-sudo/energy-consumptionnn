#!/usr/bin/env python3

"""
Create a stunning, attractive design for the website with modern UI elements
"""

def create_attractive_design():
    """Transform the website into a visually stunning, attractive design"""
    
    # Update Objective Selector with attractive design
    selector_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    with open(selector_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the entire content with attractive design
    new_attractive_selector = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SDG 7 - Sustainable Energy Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
        }
        
        /* Animated Background Particles */
        .particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
        }
        
        .particle {
            position: absolute;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            animation: float 6s ease-in-out infinite;
        }
        
        .particle:nth-child(1) { width: 80px; height: 80px; left: 10%; animation-delay: 0s; }
        .particle:nth-child(2) { width: 60px; height: 60px; left: 20%; animation-delay: 1s; }
        .particle:nth-child(3) { width: 100px; height: 100px; left: 35%; animation-delay: 2s; }
        .particle:nth-child(4) { width: 40px; height: 40px; left: 50%; animation-delay: 3s; }
        .particle:nth-child(5) { width: 120px; height: 120px; left: 65%; animation-delay: 4s; }
        .particle:nth-child(6) { width: 70px; height: 70px; left: 80%; animation-delay: 5s; }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 0.3; }
            50% { transform: translateY(-100px) rotate(180deg); opacity: 0.8; }
        }
        
        /* Main Container */
        .main-container {
            position: relative;
            z-index: 2;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 40px 20px;
        }
        
        /* Hero Section */
        .hero-section {
            text-align: center;
            margin-bottom: 60px;
            animation: fadeInUp 1s ease-out;
        }
        
        .hero-title {
            background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 20px;
            text-shadow: 0 4px 20px rgba(0,0,0,0.1);
            line-height: 1.2;
        }
        
        .hero-subtitle {
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.3rem;
            font-weight: 400;
            margin-bottom: 30px;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
        
        .hero-icon {
            width: 100px;
            height: 100px;
            background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 30px;
            box-shadow: 0 20px 40px rgba(255, 215, 0, 0.3);
            animation: pulse 2s ease-in-out infinite;
        }
        
        .hero-icon i {
            font-size: 3rem;
            color: #2c3e50;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        /* Dashboard Cards */
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            max-width: 1200px;
            width: 100%;
        }
        
        .dashboard-card {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(20px);
            border-radius: 25px;
            padding: 40px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.1);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
        }
        
        .dashboard-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            transition: left 0.5s;
        }
        
        .dashboard-card:hover::before {
            left: 100%;
        }
        
        .dashboard-card:hover {
            transform: translateY(-15px) scale(1.02);
            box-shadow: 0 35px 70px rgba(0, 0, 0, 0.2);
            border-color: rgba(255, 255, 255, 0.4);
        }
        
        .card-icon {
            width: 70px;
            height: 70px;
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 25px;
            box-shadow: 0 15px 30px rgba(79, 172, 254, 0.3);
        }
        
        .card-icon i {
            font-size: 2rem;
            color: white;
        }
        
        .card-title {
            color: white;
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 15px;
        }
        
        .card-description {
            color: rgba(255, 255, 255, 0.8);
            font-size: 1rem;
            line-height: 1.6;
            margin-bottom: 25px;
        }
        
        .card-features {
            list-style: none;
            margin-bottom: 30px;
        }
        
        .card-features li {
            color: rgba(255, 255, 255, 0.9);
            font-size: 0.95rem;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .card-features li::before {
            content: "✨";
            font-size: 1rem;
        }
        
        .explore-btn {
            background: linear-gradient(135deg, #ff6b6b 0%, #feca57 100%);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 50px;
            font-size: 1rem;
            font-weight: 600;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            transition: all 0.3s ease;
            box-shadow: 0 10px 25px rgba(255, 107, 107, 0.3);
            position: relative;
            overflow: hidden;
        }
        
        .explore-btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.5s;
        }
        
        .explore-btn:hover::before {
            left: 100%;
        }
        
        .explore-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 35px rgba(255, 107, 107, 0.4);
            text-decoration: none;
            color: white;
        }
        
        /* Objective Cards */
        .objectives-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
            margin-top: 40px;
            max-width: 1400px;
            width: 100%;
        }
        
        .objective-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(15px);
            border-radius: 20px;
            padding: 25px;
            border: 1px solid rgba(255, 255, 255, 0.15);
            transition: all 0.3s ease;
            text-align: center;
        }
        
        .objective-card:hover {
            transform: translateY(-8px);
            background: rgba(255, 255, 255, 0.2);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        }
        
        .objective-number {
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 15px;
            font-weight: 700;
            color: #2c3e50;
            font-size: 1.2rem;
        }
        
        .objective-title {
            color: white;
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 10px;
        }
        
        .objective-desc {
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9rem;
            line-height: 1.4;
        }
        
        /* Animations */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .dashboard-card {
            animation: fadeInUp 0.8s ease-out;
        }
        
        .dashboard-card:nth-child(2) { animation-delay: 0.2s; }
        .dashboard-card:nth-child(3) { animation-delay: 0.4s; }
        
        /* Mobile Responsive */
        @media (max-width: 768px) {
            .hero-title {
                font-size: 2.5rem;
            }
            
            .hero-subtitle {
                font-size: 1.1rem;
            }
            
            .dashboard-grid {
                grid-template-columns: 1fr;
                gap: 20px;
            }
            
            .dashboard-card {
                padding: 30px;
            }
            
            .main-container {
                padding: 20px 15px;
            }
        }
        
        /* Scrollbar Styling */
        ::-webkit-scrollbar {
            width: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.1);
        }
        
        ::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.3);
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(255, 255, 255, 0.5);
        }
    </style>
</head>
<body>
    <!-- Animated Background Particles -->
    <div class="particles">
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
    </div>

    <div class="main-container">
        <!-- Hero Section -->
        <div class="hero-section">
            <div class="hero-icon">
                <i class="fas fa-bolt"></i>
            </div>
            <h1 class="hero-title">TOWARDS AFFORDABLE AND CLEAN ENERGY</h1>
            <p class="hero-subtitle">A PREDICTIVE AND STRATEGIC FRAMEWORK FOR SDG 7</p>
        </div>

        <!-- Dashboard Grid -->
        <div class="dashboard-grid">
            <!-- Full Dashboard Card -->
            <div class="dashboard-card">
                <div class="card-icon">
                    <i class="fas fa-globe-americas"></i>
                </div>
                <h2 class="card-title">🌍 Full Dashboard: Comprehensive Analysis</h2>
                <p class="card-description">Complete energy analysis with world map and status alerts</p>
                <ul class="card-features">
                    <li>World map visualization</li>
                    <li>7 ML models comparison</li>
                    <li>Real-time status alerts</li>
                    <li>Interactive country analysis</li>
                </ul>
                <a href="/dashboard/" class="explore-btn">
                    <span>Explore Dashboard</span>
                    <i class="fas fa-arrow-right"></i>
                </a>
            </div>

            <!-- ML Comparison Card -->
            <div class="dashboard-card">
                <div class="card-icon">
                    <i class="fas fa-brain"></i>
                </div>
                <h2 class="card-title">🤖 Comprehensive ML Comparison</h2>
                <p class="card-description">Compare ML algorithms across all 8 objectives</p>
                <ul class="card-features">
                    <li>8 different ML objectives</li>
                    <li>Algorithm performance metrics</li>
                    <li>Visual model comparison</li>
                    <li>Best model recommendations</li>
                </ul>
                <a href="/comprehensive-comparison/" class="explore-btn">
                    <span>Compare Models</span>
                    <i class="fas fa-chart-bar"></i>
                </a>
            </div>
        </div>

        <!-- Objectives Grid -->
        <div class="objectives-grid">
            <div class="objective-card">
                <div class="objective-number">1</div>
                <h3 class="objective-title">Energy Consumption Prediction</h3>
                <p class="objective-desc">Predict future energy consumption patterns using advanced ML algorithms</p>
            </div>
            
            <div class="objective-card">
                <div class="objective-number">2</div>
                <h3 class="objective-title">CO2 Emissions Forecasting</h3>
                <p class="objective-desc">Forecast CO2 emissions and environmental impact analysis</p>
            </div>
            
            <div class="objective-card">
                <div class="objective-number">3</div>
                <h3 class="objective-title">Electricity Access Classification</h3>
                <p class="objective-desc">Classify and analyze electricity access levels globally</p>
            </div>
            
            <div class="objective-card">
                <div class="objective-number">4</div>
                <h3 class="objective-title">SDG 7 Monitoring</h3>
                <p class="objective-desc">Monitor progress towards Sustainable Development Goal 7</p>
            </div>
            
            <div class="objective-card">
                <div class="objective-number">5</div>
                <h3 class="objective-title">Energy Equity Analysis</h3>
                <p class="objective-desc">Analyze energy equity and accessibility across regions</p>
            </div>
            
            <div class="objective-card">
                <div class="objective-number">6</div>
                <h3 class="objective-title">Renewable Energy Potential</h3>
                <p class="objective-desc">Assess renewable energy potential and opportunities</p>
            </div>
            
            <div class="objective-card">
                <div class="objective-number">7</div>
                <h3 class="objective-title">Investment Strategy Classification</h3>
                <p class="objective-desc">Classify optimal investment strategies for clean energy</p>
            </div>
            
            <div class="objective-card">
                <div class="objective-number">8</div>
                <h3 class="objective-title">Email Alert System</h3>
                <p class="objective-desc">Automated alerts and notifications for energy insights</p>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Add smooth scrolling and interactive effects
        document.addEventListener('DOMContentLoaded', function() {
            // Animate cards on scroll
            const cards = document.querySelectorAll('.dashboard-card, .objective-card');
            
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }
                });
            });
            
            cards.forEach(card => {
                card.style.opacity = '0';
                card.style.transform = 'translateY(30px)';
                card.style.transition = 'all 0.6s ease';
                observer.observe(card);
            });
            
            // Add particle movement on mouse move
            document.addEventListener('mousemove', (e) => {
                const particles = document.querySelectorAll('.particle');
                const x = e.clientX / window.innerWidth;
                const y = e.clientY / window.innerHeight;
                
                particles.forEach((particle, index) => {
                    const speed = (index + 1) * 0.5;
                    const xPos = x * speed * 10;
                    const yPos = y * speed * 10;
                    
                    particle.style.transform = `translate(${xPos}px, ${yPos}px)`;
                });
            });
        });
    </script>
</body>
</html>'''
    
    # Write the new attractive selector
    with open(selector_path, 'w', encoding='utf-8') as f:
        f.write(new_attractive_selector)
    
    print("✅ Created stunning, attractive design for objective selector!")
    print("\n🎨 Attractive Features Added:")
    print("   - Animated background particles")
    print("   - Gradient text effects")
    print("   - Glass morphism cards")
    print("   - Hover animations and transitions")
    print("   - Interactive mouse effects")
    print("   - Modern typography (Inter font)")
    print("   - Colorful gradient backgrounds")
    print("   - Smooth scroll animations")

if __name__ == "__main__":
    create_attractive_design()