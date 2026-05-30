#!/usr/bin/env python3

def create_eneroutlook_style_design():
    """Create a clean, professional design similar to EnerOutlook with all 7 objectives"""
    
    # Create the new objective selector template
    objective_selector_html = """
{% extends 'dashboard/base.html' %}
{% load static %}

{% block title %}Energy & Emissions Projections 2050 - EnerOutlook{% endblock %}

{% block extra_css %}
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
    /* Clean Professional Design */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Inter', sans-serif;
        background: #f8fafc;
        color: #334155;
        line-height: 1.6;
    }
    
    /* Header */
    .main-header {
        background: white;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        position: sticky;
        top: 0;
        z-index: 100;
    }
    
    .header-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        height: 70px;
    }
    
    .logo-section {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .logo-icon {
        width: 40px;
        height: 40px;
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
    }
    
    .logo-text {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1e293b;
    }
    
    .header-subtitle {
        font-size: 0.9rem;
        color: #64748b;
        margin-left: 52px;
        margin-top: -5px;
    }
    
    .header-actions {
        display: flex;
        gap: 15px;
        align-items: center;
    }
    
    .header-btn {
        padding: 8px 16px;
        border-radius: 6px;
        text-decoration: none;
        font-size: 0.9rem;
        font-weight: 500;
        transition: all 0.2s;
    }
    
    .btn-outline {
        border: 1px solid #d1d5db;
        color: #374151;
        background: white;
    }
    
    .btn-outline:hover {
        background: #f9fafb;
        text-decoration: none;
        color: #374151;
    }
    
    .btn-primary {
        background: #3b82f6;
        color: white;
        border: 1px solid #3b82f6;
    }
    
    .btn-primary:hover {
        background: #2563eb;
        text-decoration: none;
        color: white;
    }
    
    /* Navigation Tabs */
    .nav-tabs {
        background: white;
        border-bottom: 1px solid #e2e8f0;
        padding: 0;
    }
    
    .nav-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
        display: flex;
        gap: 0;
    }
    
    .nav-tab {
        padding: 20px 25px;
        text-decoration: none;
        color: #64748b;
        font-weight: 500;
        font-size: 0.9rem;
        border-bottom: 3px solid transparent;
        transition: all 0.2s;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 8px;
        min-width: 120px;
        text-align: center;
    }
    
    .nav-tab:hover {
        color: #3b82f6;
        text-decoration: none;
        background: #f8fafc;
    }
    
    .nav-tab.active {
        color: #3b82f6;
        border-bottom-color: #3b82f6;
        background: #f8fafc;
    }
    
    .nav-icon {
        width: 32px;
        height: 32px;
        background: #f1f5f9;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #64748b;
        font-size: 1rem;
        transition: all 0.2s;
    }
    
    .nav-tab:hover .nav-icon,
    .nav-tab.active .nav-icon {
        background: #dbeafe;
        color: #3b82f6;
    }
    
    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: white;
        padding: 80px 0;
        position: relative;
        overflow: hidden;
    }
    
    .hero-bg {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><defs><radialGradient id="a" cx="50%" cy="50%"><stop offset="0%" stop-color="%233b82f6" stop-opacity="0.1"/><stop offset="100%" stop-color="%233b82f6" stop-opacity="0"/></radialGradient></defs><rect width="100%" height="100%" fill="url(%23a)"/></svg>');
        opacity: 0.5;
    }
    
    .hero-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
        position: relative;
        z-index: 2;
        text-align: center;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 20px;
        background: linear-gradient(135deg, #60a5fa 0%, #34d399 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: #cbd5e1;
        margin-bottom: 40px;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .hero-cta {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        padding: 16px 32px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
        display: inline-flex;
        align-items: center;
        gap: 10px;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    }
    
    .hero-cta:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
        text-decoration: none;
        color: white;
    }
    
    /* Objectives Grid */
    .objectives-section {
        padding: 80px 0;
        background: white;
    }
    
    .objectives-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }
    
    .section-header {
        text-align: center;
        margin-bottom: 60px;
    }
    
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 15px;
    }
    
    .section-description {
        font-size: 1.1rem;
        color: #64748b;
        max-width: 600px;
        margin: 0 auto;
    }
    
    .objectives-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 30px;
        margin-top: 50px;
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
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
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
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.3rem;
    }
    
    .objective-number {
        background: #f1f5f9;
        color: #3b82f6;
        font-weight: 700;
        font-size: 0.8rem;
        padding: 4px 8px;
        border-radius: 4px;
        margin-left: auto;
    }
    
    .objective-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 12px;
    }
    
    .objective-description {
        color: #64748b;
        line-height: 1.6;
        margin-bottom: 25px;
        font-size: 0.95rem;
    }
    
    .objective-actions {
        display: flex;
        gap: 10px;
    }
    
    .objective-btn {
        flex: 1;
        padding: 12px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 500;
        font-size: 0.9rem;
        text-align: center;
        transition: all 0.2s;
    }
    
    .btn-view {
        background: #3b82f6;
        color: white;
    }
    
    .btn-view:hover {
        background: #2563eb;
        text-decoration: none;
        color: white;
    }
    
    .btn-api {
        background: #f8fafc;
        color: #64748b;
        border: 1px solid #e2e8f0;
    }
    
    .btn-api:hover {
        background: #f1f5f9;
        text-decoration: none;
        color: #64748b;
    }
    
    /* Additional Features */
    .features-section {
        background: #f8fafc;
        padding: 80px 0;
    }
    
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 30px;
        margin-top: 50px;
    }
    
    .feature-item {
        text-align: center;
        padding: 30px 20px;
    }
    
    .feature-icon {
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 20px;
        color: white;
        font-size: 1.5rem;
    }
    
    .feature-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 10px;
    }
    
    .feature-desc {
        color: #64748b;
        font-size: 0.9rem;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        
        .nav-container {
            flex-wrap: wrap;
            justify-content: center;
        }
        
        .nav-tab {
            min-width: 100px;
            padding: 15px 20px;
        }
        
        .objectives-grid {
            grid-template-columns: 1fr;
            gap: 20px;
        }
        
        .header-container {
            flex-direction: column;
            height: auto;
            padding: 15px 20px;
            gap: 15px;
        }
        
        .header-actions {
            order: -1;
        }
    }
</style>
{% endblock %}

{% block content %}
<!-- Main Header -->
<header class="main-header">
    <div class="header-container">
        <div>
            <div class="logo-section">
                <div class="logo-icon">E</div>
                <span class="logo-text">EnerOutlook</span>
            </div>
            <div class="header-subtitle">Energy & emissions projections 2050</div>
        </div>
        <div class="header-actions">
            <span style="font-size: 0.9rem; color: #64748b;">2025 Edition</span>
            <a href="#" class="header-btn btn-outline">GLOSSARY</a>
            <a href="#" class="header-btn btn-outline">SCENARIO DESCRIPTION</a>
            <a href="/admin-panel/" class="header-btn btn-primary">LOGIN/REGISTER</a>
        </div>
    </div>
</header>

<!-- Navigation Tabs -->
<nav class="nav-tabs">
    <div class="nav-container">
        <a href="{% url 'objective1_dashboard' %}" class="nav-tab">
            <div class="nav-icon"><i class="fas fa-bolt"></i></div>
            <span>TOTAL ENERGY</span>
        </a>
        <a href="{% url 'objective2_dashboard' %}" class="nav-tab">
            <div class="nav-icon"><i class="fas fa-plug"></i></div>
            <span>ELECTRICITY</span>
        </a>
        <a href="{% url 'objective3_dashboard' %}" class="nav-tab">
            <div class="nav-icon"><i class="fas fa-leaf"></i></div>
            <span>RENEWABLES</span>
        </a>
        <a href="{% url 'objective4_dashboard' %}" class="nav-tab">
            <div class="nav-icon"><i class="fas fa-smog"></i></div>
            <span>CO₂ EMISSIONS</span>
        </a>
        <a href="{% url 'objective5_dashboard' %}" class="nav-tab">
            <div class="nav-icon"><i class="fas fa-globe"></i></div>
            <span>COUNTRY FORECASTS</span>
        </a>
        <a href="{% url 'objective6_dashboard' %}" class="nav-tab">
            <div class="nav-icon"><i class="fas fa-chart-line"></i></div>
            <span>POLICY ANALYSIS</span>
        </a>
        <a href="{% url 'objective7_dashboard' %}" class="nav-tab">
            <div class="nav-icon"><i class="fas fa-lightbulb"></i></div>
            <span>INVESTMENT STRATEGY</span>
        </a>
        <a href="{% url 'objective8_dashboard' %}" class="nav-tab">
            <div class="nav-icon"><i class="fas fa-bell"></i></div>
            <span>ALERTS</span>
        </a>
        <a href="{% url 'comprehensive_comparison_dashboard' %}" class="nav-tab">
            <div class="nav-icon"><i class="fas fa-brain"></i></div>
            <span>ML COMPARISON</span>
        </a>
    </div>
</nav>

<!-- Hero Section -->
<section class="hero-section">
    <div class="hero-bg"></div>
    <div class="hero-container">
        <h1 class="hero-title">Energy & Emissions Projections 2050</h1>
        <p class="hero-subtitle">
            Advanced machine learning models and comprehensive analysis for sustainable energy forecasting and policy insights across 128+ countries worldwide.
        </p>
        <a href="#objectives" class="hero-cta">
            <i class="fas fa-chart-line"></i>
            Explore Projections
        </a>
    </div>
</section>

<!-- Objectives Section -->
<section class="objectives-section" id="objectives">
    <div class="objectives-container">
        <div class="section-header">
            <h2 class="section-title">Analysis Objectives</h2>
            <p class="section-description">
                Comprehensive energy and emissions analysis across multiple dimensions using advanced machine learning and data science techniques.
            </p>
        </div>
        
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
                <div class="objective-actions">
                    <a href="{% url 'objective1_dashboard' %}" class="objective-btn btn-view">
                        <i class="fas fa-eye"></i> View Analysis
                    </a>
                    <a href="/api/objective1/" class="objective-btn btn-api">
                        <i class="fas fa-code"></i> API
                    </a>
                </div>
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
                <div class="objective-actions">
                    <a href="{% url 'objective2_dashboard' %}" class="objective-btn btn-view">
                        <i class="fas fa-eye"></i> View Analysis
                    </a>
                    <a href="/api/objective2/" class="objective-btn btn-api">
                        <i class="fas fa-code"></i> API
                    </a>
                </div>
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
                <div class="objective-actions">
                    <a href="{% url 'objective3_dashboard' %}" class="objective-btn btn-view">
                        <i class="fas fa-eye"></i> View Analysis
                    </a>
                    <a href="/api/objective3/" class="objective-btn btn-api">
                        <i class="fas fa-code"></i> API
                    </a>
                </div>
            </div>
            
            <!-- Objective 4: CO2 Emissions -->
            <div class="objective-card">
                <div class="objective-header">
                    <div class="objective-icon">
                        <i class="fas fa-smog"></i>
                    </div>
                    <div class="objective-number">04</div>
                </div>
                <h3 class="objective-title">CO₂ Emissions Analysis</h3>
                <p class="objective-description">
                    Monitor and predict carbon dioxide emissions trends, reduction targets, and environmental impact assessment using machine learning models.
                </p>
                <div class="objective-actions">
                    <a href="{% url 'objective4_dashboard' %}" class="objective-btn btn-view">
                        <i class="fas fa-eye"></i> View Analysis
                    </a>
                    <a href="/api/objective4/" class="objective-btn btn-api">
                        <i class="fas fa-code"></i> API
                    </a>
                </div>
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
                <div class="objective-actions">
                    <a href="{% url 'objective5_dashboard' %}" class="objective-btn btn-view">
                        <i class="fas fa-eye"></i> View Analysis
                    </a>
                    <a href="/api/objective5/" class="objective-btn btn-api">
                        <i class="fas fa-code"></i> API
                    </a>
                </div>
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
                <div class="objective-actions">
                    <a href="{% url 'objective6_dashboard' %}" class="objective-btn btn-view">
                        <i class="fas fa-eye"></i> View Analysis
                    </a>
                    <a href="/api/objective6/" class="objective-btn btn-api">
                        <i class="fas fa-code"></i> API
                    </a>
                </div>
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
                <div class="objective-actions">
                    <a href="{% url 'objective7_dashboard' %}" class="objective-btn btn-view">
                        <i class="fas fa-eye"></i> View Analysis
                    </a>
                    <a href="/api/objective7/" class="objective-btn btn-api">
                        <i class="fas fa-code"></i> API
                    </a>
                </div>
            </div>
            
            <!-- Objective 8: Alerts & Monitoring -->
            <div class="objective-card">
                <div class="objective-header">
                    <div class="objective-icon">
                        <i class="fas fa-bell"></i>
                    </div>
                    <div class="objective-number">08</div>
                </div>
                <h3 class="objective-title">Intelligent Alert System</h3>
                <p class="objective-description">
                    Real-time monitoring and alert system for energy anomalies, policy changes, and critical thresholds with automated notifications.
                </p>
                <div class="objective-actions">
                    <a href="{% url 'objective8_dashboard' %}" class="objective-btn btn-view">
                        <i class="fas fa-eye"></i> View Analysis
                    </a>
                    <a href="/api/objective8/" class="objective-btn btn-api">
                        <i class="fas fa-code"></i> API
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Additional Features -->
<section class="features-section">
    <div class="objectives-container">
        <div class="section-header">
            <h2 class="section-title">Advanced Analytics</h2>
            <p class="section-description">
                Powered by cutting-edge machine learning algorithms and comprehensive data analysis
            </p>
        </div>
        
        <div class="features-grid">
            <div class="feature-item">
                <div class="feature-icon">
                    <i class="fas fa-brain"></i>
                </div>
                <h3 class="feature-title">ML Model Comparison</h3>
                <p class="feature-desc">Compare 7+ machine learning models with performance metrics and accuracy analysis</p>
            </div>
            
            <div class="feature-item">
                <div class="feature-icon">
                    <i class="fas fa-globe-americas"></i>
                </div>
                <h3 class="feature-title">128+ Countries</h3>
                <p class="feature-desc">Comprehensive coverage of global energy data and country-specific insights</p>
            </div>
            
            <div class="feature-item">
                <div class="feature-icon">
                    <i class="fas fa-chart-area"></i>
                </div>
                <h3 class="feature-title">Interactive Visualizations</h3>
                <p class="feature-desc">Dynamic charts, graphs, and interactive dashboards for data exploration</p>
            </div>
            
            <div class="feature-item">
                <div class="feature-icon">
                    <i class="fas fa-api"></i>
                </div>
                <h3 class="feature-title">RESTful APIs</h3>
                <p class="feature-desc">Access all data and analysis through comprehensive API endpoints</p>
            </div>
        </div>
    </div>
</section>

<script>
// Add smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Add active state to current nav tab
const currentPath = window.location.pathname;
document.querySelectorAll('.nav-tab').forEach(tab => {
    if (tab.getAttribute('href') === currentPath) {
        tab.classList.add('active');
    }
});
</script>

{% endblock %}
"""
    
    return objective_selector_html

if __name__ == "__main__":
    html_content = create_eneroutlook_style_design()
    print("EnerOutlook style design created!")
    print("Length:", len(html_content), "characters")