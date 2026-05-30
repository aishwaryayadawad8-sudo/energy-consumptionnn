#!/usr/bin/env python3

"""
Create an attractive design for Objective 4 to match the new stunning homepage
"""

def create_attractive_objective4():
    """Transform Objective 4 into a visually stunning, attractive design"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective4.html"
    
    # Read current template
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the CSS section with attractive design
    css_start = content.find('<style>')
    css_end = content.find('</style>') + 8
    
    if css_start == -1 or css_end == -1:
        print("❌ Could not find CSS section")
        return
    
    # New attractive CSS for Objective 4
    new_attractive_css = '''    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }
        
        html, body {
            width: 100%;
            height: 100vh;
            overflow-x: hidden;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        /* Animated Background */
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
            position: relative;
        }
        
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* Floating Particles */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                radial-gradient(circle at 20% 80%, rgba(255, 255, 255, 0.1) 2px, transparent 2px),
                radial-gradient(circle at 80% 20%, rgba(255, 255, 255, 0.1) 2px, transparent 2px),
                radial-gradient(circle at 40% 40%, rgba(255, 255, 255, 0.05) 1px, transparent 1px);
            background-size: 100px 100px, 150px 150px, 80px 80px;
            animation: float 20s linear infinite;
            pointer-events: none;
            z-index: 1;
        }
        
        @keyframes float {
            0% { transform: translateY(0px) translateX(0px); }
            33% { transform: translateY(-30px) translateX(20px); }
            66% { transform: translateY(-60px) translateX(-20px); }
            100% { transform: translateY(0px) translateX(0px); }
        }
        
        /* Main Container */
        .dashboard-container {
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-y: auto;
            position: relative;
            z-index: 2;
        }
        
        /* Attractive Header */
        .header-section {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            padding: 25px 40px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .back-btn {
            background: linear-gradient(135deg, #ff6b6b 0%, #feca57 100%);
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 50px;
            margin-bottom: 15px;
            font-weight: 600;
            font-size: 14px;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 8px 25px rgba(255, 107, 107, 0.3);
            position: relative;
            overflow: hidden;
        }
        
        .back-btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.5s;
        }
        
        .back-btn:hover::before {
            left: 100%;
        }
        
        .back-btn:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 15px 35px rgba(255, 107, 107, 0.4);
        }
        
        .header-section h1 {
            color: white;
            font-size: 2.2rem;
            font-weight: 800;
            margin: 0;
            text-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }
        
        .header-section p {
            color: rgba(255, 255, 255, 0.8);
            font-size: 1.1rem;
            margin: 5px 0 0 0;
            font-weight: 400;
        }
        
        /* Content Area */
        .content-area {
            flex: 1;
            padding: 30px 40px;
            display: flex;
            flex-direction: column;
            gap: 30px;
        }
        
        /* Attractive Section Cards */
        .section-card {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(25px);
            border-radius: 25px;
            padding: 35px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.1);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
        }
        
        .section-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            transition: left 0.6s;
        }
        
        .section-card:hover::before {
            left: 100%;
        }
        
        .section-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 35px 70px rgba(0, 0, 0, 0.15);
            border-color: rgba(255, 255, 255, 0.3);
        }
        
        .section-title {
            color: white;
            font-weight: 700;
            margin-bottom: 20px;
            font-size: 1.6rem;
            letter-spacing: -0.5px;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .section-title i {
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            box-shadow: 0 10px 25px rgba(79, 172, 254, 0.3);
        }
        
        /* Chart Containers */
        .chart-container {
            position: relative;
            height: calc(100vh - 500px);
            min-height: 400px;
            max-height: 600px;
            margin-top: 20px;
            background: rgba(248, 250, 252, 0.9);
            border-radius: 20px;
            padding: 25px;
            border: 1px solid rgba(226, 232, 240, 0.8);
            box-shadow: inset 0 2px 10px rgba(0,0,0,0.05);
        }
        
        .interactive-chart-container {
            position: relative;
            height: calc(100vh - 450px);
            min-height: 450px;
            max-height: 700px;
            margin-top: 20px;
            background: rgba(240, 248, 255, 0.95);
            border-radius: 20px;
            padding: 30px;
            border: 1px solid rgba(59, 130, 246, 0.2);
            box-shadow: 0 15px 35px rgba(59, 130, 246, 0.1);
        }
        
        /* Form Elements */
        .country-select {
            border-radius: 15px;
            padding: 15px 20px;
            border: 2px solid rgba(255, 255, 255, 0.3);
            font-size: 16px;
            font-weight: 500;
            background: rgba(255, 255, 255, 0.9);
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }
        
        .country-select:focus {
            border-color: #4facfe;
            box-shadow: 0 0 0 4px rgba(79, 172, 254, 0.2);
            outline: none;
            transform: translateY(-2px);
        }
        
        .btn-load {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 15px;
            font-weight: 600;
            font-size: 16px;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 8px 25px rgba(79, 172, 254, 0.3);
            position: relative;
            overflow: hidden;
        }
        
        .btn-load::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.5s;
        }
        
        .btn-load:hover::before {
            left: 100%;
        }
        
        .btn-load:hover {
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 15px 35px rgba(79, 172, 254, 0.4);
        }
        
        /* Loading States */
        .loading {
            text-align: center;
            padding: 50px;
            color: rgba(255, 255, 255, 0.8);
        }
        
        .spinner-border {
            width: 3.5rem;
            height: 3.5rem;
            border-width: 4px;
            border-color: rgba(255, 255, 255, 0.3);
            border-top-color: white;
        }
        
        .best-model-badge {
            background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
            color: #2c3e50;
            padding: 12px 20px;
            border-radius: 25px;
            font-weight: 700;
            display: inline-block;
            margin-top: 15px;
            box-shadow: 0 8px 25px rgba(255, 215, 0, 0.3);
            animation: glow 2s ease-in-out infinite alternate;
        }
        
        @keyframes glow {
            from { box-shadow: 0 8px 25px rgba(255, 215, 0, 0.3); }
            to { box-shadow: 0 8px 35px rgba(255, 215, 0, 0.6); }
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
            color: rgba(255, 255, 255, 0.7) !important;
            font-weight: 500;
        }
        
        .mt-2 { margin-top: 0.5rem; }
        .mb-2 { margin-bottom: 0.5rem; }
        .w-100 { width: 100%; }
        
        /* Mobile Responsive */
        @media (max-width: 768px) {
            .header-section {
                padding: 20px 25px;
            }
            
            .content-area {
                padding: 20px 25px;
            }
            
            .section-card {
                padding: 25px;
            }
            
            .chart-container,
            .interactive-chart-container {
                height: calc(100vh - 400px);
                min-height: 300px;
                padding: 20px;
            }
            
            .col-md-8,
            .col-md-4 {
                flex: 0 0 100%;
                margin-bottom: 15px;
            }
            
            .section-title {
                font-size: 1.4rem;
            }
            
            .header-section h1 {
                font-size: 1.8rem;
            }
        }
        
        /* Animations */
        .section-card {
            animation: slideInUp 0.8s ease-out;
        }
        
        .section-card:nth-child(2) { animation-delay: 0.2s; }
        .section-card:nth-child(3) { animation-delay: 0.4s; }
        .section-card:nth-child(4) { animation-delay: 0.6s; }
        
        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Scrollbar Styling */
        .dashboard-container::-webkit-scrollbar {
            width: 10px;
        }
        
        .dashboard-container::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 5px;
        }
        
        .dashboard-container::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            border-radius: 5px;
        }
        
        .dashboard-container::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #3d8bfe 0%, #00d4fe 100%);
        }
        
        /* Enhanced Canvas Quality */
        canvas {
            image-rendering: -webkit-optimize-contrast;
            image-rendering: crisp-edges;
            border-radius: 15px;
        }
    </style>'''
    
    # Replace the CSS
    content = content[:css_start] + new_attractive_css + content[css_end:]
    
    # Write the enhanced template
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Created stunning, attractive design for Objective 4!")
    print("\n🎨 Attractive Features Added:")
    print("   - Animated gradient background")
    print("   - Floating particle effects")
    print("   - Glass morphism cards with blur effects")
    print("   - Smooth hover animations")
    print("   - Gradient buttons with shine effects")
    print("   - Glowing best model badge")
    print("   - Enhanced scrollbar styling")
    print("   - Modern Inter typography")
    print("   - Responsive design for all devices")

if __name__ == "__main__":
    create_attractive_objective4()