#!/usr/bin/env python3

"""
Make the objective selector page fullscreen to match Objective 4
"""

def make_selector_fullscreen():
    """Convert objective selector to fullscreen layout"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    # Read current template
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if it already has fullscreen styling
    if '100vw' in content and '100vh' in content:
        print("✅ Objective selector already has fullscreen layout")
        return
    
    # Find the style section
    style_start = content.find('<style>')
    style_end = content.find('</style>') + 8
    
    if style_start == -1:
        print("❌ Could not find style section in objective selector")
        return
    
    # New fullscreen CSS for objective selector
    new_selector_css = '''    <style>
        /* Fullscreen Reset */
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
            overflow: hidden;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }
        
        /* Fullscreen Background */
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        /* Fullscreen Container */
        .container {
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        
        /* Main Title */
        .main-title {
            background: rgba(255, 255, 255, 0.98);
            padding: 40px 60px;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.15);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.2);
        }
        
        .main-title h1 {
            color: #2c3e50;
            font-size: 2.5rem;
            font-weight: 700;
            margin: 0;
            letter-spacing: -1px;
            line-height: 1.2;
        }
        
        /* Dashboard Card */
        .dashboard-card {
            background: rgba(255, 255, 255, 0.98);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.15);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.2);
            max-width: 600px;
            width: 100%;
        }
        
        .dashboard-card h2 {
            color: #2c3e50;
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .dashboard-card p {
            color: #64748b;
            font-size: 1.1rem;
            margin-bottom: 25px;
            line-height: 1.6;
        }
        
        .dashboard-card ul {
            list-style: none;
            margin-bottom: 30px;
        }
        
        .dashboard-card li {
            color: #374151;
            font-size: 1rem;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .dashboard-card li::before {
            content: "✓";
            color: #10b981;
            font-weight: bold;
            font-size: 1.2rem;
        }
        
        /* Explore Button */
        .explore-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 40px;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: 600;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            transition: all 0.3s ease;
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
        }
        
        .explore-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
            text-decoration: none;
            color: white;
        }
        
        /* Globe Icon */
        .globe-icon {
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 20px;
            box-shadow: 0 8px 25px rgba(59, 130, 246, 0.3);
        }
        
        .globe-icon svg {
            width: 30px;
            height: 30px;
            fill: white;
        }
        
        /* Mobile Optimization */
        @media (max-width: 768px) {
            .container {
                padding: 15px;
            }
            
            .main-title {
                padding: 30px 40px;
                margin-bottom: 30px;
            }
            
            .main-title h1 {
                font-size: 2rem;
            }
            
            .dashboard-card {
                padding: 30px;
            }
            
            .dashboard-card h2 {
                font-size: 1.5rem;
            }
            
            .explore-btn {
                padding: 12px 30px;
                font-size: 1rem;
            }
        }
        
        /* Animation */
        .main-title,
        .dashboard-card {
            animation: fadeInUp 0.8s ease-out;
        }
        
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
    </style>'''
    
    # Replace the CSS
    content = content[:style_start] + new_selector_css + content[style_end:]
    
    # Write the updated template
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Updated objective selector to fullscreen layout!")
    print("\n🎯 Selector Features:")
    print("   - Fullscreen centered layout")
    print("   - Consistent with Objective 4 styling")
    print("   - Professional glass morphism effects")
    print("   - Smooth animations and transitions")

if __name__ == "__main__":
    make_selector_fullscreen()