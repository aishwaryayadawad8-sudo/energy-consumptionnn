#!/usr/bin/env python3

"""
Create a professional Objective 4 design matching the EnerOutlook style
"""

def create_professional_objective4():
    """Transform Objective 4 to match the professional EnerOutlook design"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective4.html"
    
    # Read current template
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the CSS section with professional design
    css_start = content.find('<style>')
    css_end = content.find('</style>') + 8
    
    if css_start == -1 or css_end == -1:
        print("❌ Could not find CSS section")
        return
    
    # New professional CSS matching EnerOutlook style
    new_professional_css = '''    <style>
        /* Import Professional Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        html, body {
            width: 100%;
            height: 100vh;
            overflow-x: hidden;
            font-family: 'Roboto', sans-serif;
            background: #f8f9fa;
            color: #333;
        }
        
        /* Professional Header */
        .top-header {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 15px 0;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
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
            width: 45px;
            height: 45px;
            background: #00bcd4;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.3rem;
            font-weight: bold;
        }
        
        .site-title {
            font-size: 1.5rem;
            font-weight: 500;
            margin: 0;
        }
        
        .back-btn {
            background: #ff6b35;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 20px;
            font-weight: 500;
            text-decoration: none;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }
        
        .back-btn:hover {
            background: #f7931e;
            transform: translateY(-2px);
            color: white;
        }
        
        /* Main Container */
        .dashboard-container {
            width: 100vw;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            background: #f8f9fa;
        }
        
        /* Content Area */
        .content-area {
            flex: 1;
            max-width: 1200px;
            margin: 0 auto;
            padding: 30px 20px;
            width: 100%;
        }
        
        /* Professional Section Cards */
        .section-card {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            border-left: 5px solid #00bcd4;
            transition: all 0.3s ease;
        }
        
        .section-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 30px rgba(0,0,0,0.15);
        }
        
        .section-title {
            color: #1e3c72;
            font-weight: 600;
            margin-bottom: 20px;
            font-size: 1.5rem;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .section-icon {
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.2rem;
        }
        
        /* Chart Containers */
        .chart-container {
            position: relative;
            height: 500px;
            margin-top: 20px;
            background: #fafbfc;
            border-radius: 12px;
            padding: 25px;
            border: 1px solid #e9ecef;
        }
        
        .interactive-chart-container {
            position: relative;
            height: 600px;
            margin-top: 20px;
            background: #fafbfc;
            border-radius: 12px;
            padding: 30px;
            border: 1px solid #e9ecef;
        }
        
        /* Form Elements */
        .form-section {
            background: #f8f9fa;
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 20px;
            border: 1px solid #e9ecef;
        }
        
        .form-label {
            color: #1e3c72;
            font-weight: 600;
            margin-bottom: 10px;
            display: block;
        }
        
        .country-select {
            border-radius: 8px;
            padding: 12px 16px;
            border: 2px solid #e9ecef;
            font-size: 15px;
            font-weight: 500;
            background: white;
            transition: all 0.3s ease;
            width: 100%;
        }
        
        .country-select:focus {
            border-color: #00bcd4;
            box-shadow: 0 0 0 3px rgba(0, 188, 212, 0.1);
            outline: none;
        }
        
        .btn-load {
            background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 25px;
            font-weight: 600;
            font-size: 15px;
            transition: all 0.3s ease;
            box-shadow: 0 3px 10px rgba(255, 107, 53, 0.3);
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }
        
        .btn-load:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 107, 53, 0.4);
        }
        
        /* Loading States */
        .loading {
            text-align: center;
            padding: 40px;
            color: #666;
        }
        
        .spinner-border {
            width: 3rem;
            height: 3rem;
            border-width: 3px;
            border-color: #00bcd4;
            border-top-color: transparent;
        }
        
        .best-model-badge {
            background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
            color: white;
            padding: 10px 20px;
            border-radius: 20px;
            font-weight: 600;
            display: inline-block;
            margin-top: 15px;
            box-shadow: 0 3px 10px rgba(255, 107, 53, 0.3);
        }
        
        /* Grid System */
        .row {
            display: flex;
            flex-wrap: wrap;
            margin: 0 -15px;
        }
        
        .col-md-8 {
            flex: 0 0 66.666667%;
            padding: 0 15px;
        }
        
        .col-md-4 {
            flex: 0 0 33.333333%;
            padding: 0 15px;
        }
        
        .col-12 {
            flex: 0 0 100%;
            padding: 0 15px;
        }
        
        /* Text Styling */
        .text-muted {
            color: #666 !important;
            font-weight: 400;
        }
        
        .mt-2 { margin-top: 0.5rem; }
        .mb-2 { margin-bottom: 0.5rem; }
        .w-100 { width: 100%; }
        
        /* Professional Info Cards */
        .info-card {
            background: linear-gradient(135deg, #e3f2fd 0%, #f3e5f5 100%);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            border-left: 4px solid #00bcd4;
        }
        
        .info-card h4 {
            color: #1e3c72;
            font-weight: 600;
            margin-bottom: 10px;
        }
        
        .info-card p {
            color: #555;
            margin: 0;
            line-height: 1.5;
        }
        
        /* Mobile Responsive */
        @media (max-width: 768px) {
            .nav-container {
                flex-direction: column;
                gap: 15px;
                text-align: center;
            }
            
            .site-title {
                font-size: 1.2rem;
            }
            
            .content-area {
                padding: 20px 15px;
            }
            
            .section-card {
                padding: 20px;
            }
            
            .chart-container,
            .interactive-chart-container {
                height: 400px;
                padding: 20px;
            }
            
            .col-md-8,
            .col-md-4 {
                flex: 0 0 100%;
                margin-bottom: 15px;
            }
            
            .section-title {
                font-size: 1.3rem;
            }
        }
        
        /* Tablet Responsive */
        @media (min-width: 769px) and (max-width: 1024px) {
            .chart-container,
            .interactive-chart-container {
                height: 450px;
            }
        }
        
        /* Large Screen Optimization */
        @media (min-width: 1200px) {
            .chart-container {
                height: 550px;
            }
            
            .interactive-chart-container {
                height: 650px;
            }
        }
        
        /* Smooth Animations */
        .section-card {
            animation: fadeInUp 0.6s ease-out;
        }
        
        .section-card:nth-child(2) { animation-delay: 0.1s; }
        .section-card:nth-child(3) { animation-delay: 0.2s; }
        .section-card:nth-child(4) { animation-delay: 0.3s; }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Enhanced Canvas Quality */
        canvas {
            border-radius: 8px;
        }
        
        /* Professional Scrollbar */
        .dashboard-container::-webkit-scrollbar {
            width: 8px;
        }
        
        .dashboard-container::-webkit-scrollbar-track {
            background: #f1f1f1;
        }
        
        .dashboard-container::-webkit-scrollbar-thumb {
            background: #00bcd4;
            border-radius: 4px;
        }
        
        .dashboard-container::-webkit-scrollbar-thumb:hover {
            background: #0097a7;
        }
    </style>'''
    
    # Replace the CSS
    content = content[:css_start] + new_professional_css + content[css_end:]
    
    # Update the body structure to match professional layout
    old_body_start = content.find('<body>')
    old_header_end = content.find('</div>\n        <div class="content-area">')
    
    if old_body_start != -1 and old_header_end != -1:
        # Insert professional header
        new_header = '''<body>
    <!-- Professional Header -->
    <header class="top-header">
        <div class="nav-container">
            <div class="logo-section">
                <div class="logo">E</div>
                <h1 class="site-title">Objective 4: SDG 7 Monitoring Dashboard</h1>
            </div>
            <a href="/" class="back-btn">
                <i class="fas fa-arrow-left"></i>
                <span>Back to Overview</span>
            </a>
        </div>
    </header>

    <div class="dashboard-container">
        <div class="content-area">'''
        
        content = content[:old_body_start + 6] + new_header + content[old_header_end + len('</div>\n        <div class="content-area">'):]
    
    # Write the enhanced template
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Created professional Objective 4 design matching EnerOutlook!")
    print("\n🎯 Professional Features Added:")
    print("   - Blue gradient header with logo")
    print("   - Clean white background (#f8f9fa)")
    print("   - Professional cards with subtle shadows")
    print("   - Orange accent buttons")
    print("   - Roboto typography")
    print("   - Responsive design")
    print("   - Professional color scheme")

if __name__ == "__main__":
    create_professional_objective4()