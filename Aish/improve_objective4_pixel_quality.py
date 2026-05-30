#!/usr/bin/env python3

"""
Improve pixel quality and visual appearance of Objective 4 web page
"""

def improve_pixel_quality():
    """Enhance visual quality, resolution, and pixel clarity of Objective 4"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective4.html"
    
    # Read current template
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update the CSS for better visual quality
    old_styles = '''    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px 0;
        }
        
        .dashboard-container {
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .header-section {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        .back-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 50px;
            margin-bottom: 15px;
        }
        
        .back-btn:hover {
            opacity: 0.9;
        }
        
        .section-card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        .section-title {
            color: #2c3e50;
            font-weight: bold;
            margin-bottom: 20px;
            font-size: 1.5rem;
        }
        
        .chart-container {
            position: relative;
            height: 500px;
            margin-top: 20px;
        }
        
        .interactive-chart-container {
            position: relative;
            height: 550px;
            margin-top: 20px;
            background: rgba(240, 248, 255, 0.6);
            border-radius: 8px;
            padding: 20px;
            border: 1px solid rgba(0,0,0,0.1);
        }
        
        .country-select {
            border-radius: 50px;
            padding: 12px 20px;
            border: 2px solid #e0e0e0;
        }
        
        .country-select:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
        }
        
        .btn-load {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 50px;
            font-weight: bold;
        }
        
        .btn-load:hover {
            opacity: 0.9;
        }
        
        .loading {
            text-align: center;
            padding: 40px;
            color: #7f8c8d;
        }
        
        .spinner-border {
            width: 3rem;
            height: 3rem;
        }
        
        .best-model-badge {
            background: linear-gradient(135deg, #f39c12 0%, #f1c40f 100%);
            color: white;
            padding: 8px 15px;
            border-radius: 20px;
            font-weight: bold;
            display: inline-block;
            margin-top: 10px;
        }
    </style>'''
    
    new_styles = '''    <style>
        /* High-DPI and Retina Display Optimization */
        * {
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            text-rendering: optimizeLegibility;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px 0;
            line-height: 1.6;
            font-size: 16px;
            color: #2c3e50;
        }
        
        .dashboard-container {
            max-width: 1600px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .header-section {
            background: rgba(255, 255, 255, 0.98);
            border-radius: 20px;
            padding: 40px;
            margin-bottom: 30px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.15);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.2);
        }
        
        .back-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 50px;
            margin-bottom: 20px;
            font-weight: 600;
            font-size: 14px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }
        
        .back-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        }
        
        .section-card {
            background: rgba(255, 255, 255, 0.98);
            border-radius: 20px;
            padding: 35px;
            margin-bottom: 30px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.15);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.2);
        }
        
        .section-title {
            color: #2c3e50;
            font-weight: 700;
            margin-bottom: 25px;
            font-size: 1.75rem;
            letter-spacing: -0.5px;
        }
        
        .chart-container {
            position: relative;
            height: 600px;
            margin-top: 25px;
            background: rgba(248, 250, 252, 0.8);
            border-radius: 15px;
            padding: 25px;
            border: 1px solid rgba(226, 232, 240, 0.8);
        }
        
        .interactive-chart-container {
            position: relative;
            height: 650px;
            margin-top: 25px;
            background: rgba(240, 248, 255, 0.9);
            border-radius: 15px;
            padding: 30px;
            border: 1px solid rgba(59, 130, 246, 0.2);
            box-shadow: 0 10px 40px rgba(59, 130, 246, 0.1);
        }
        
        .country-select {
            border-radius: 12px;
            padding: 15px 20px;
            border: 2px solid #e2e8f0;
            font-size: 16px;
            font-weight: 500;
            background: rgba(255, 255, 255, 0.9);
            transition: all 0.3s ease;
        }
        
        .country-select:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
            outline: none;
        }
        
        .btn-load {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 35px;
            border-radius: 12px;
            font-weight: 600;
            font-size: 16px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }
        
        .btn-load:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        }
        
        .loading {
            text-align: center;
            padding: 50px;
            color: #64748b;
        }
        
        .spinner-border {
            width: 3.5rem;
            height: 3.5rem;
        }
        
        .best-model-badge {
            background: linear-gradient(135deg, #f59e0b 0%, #f97316 100%);
            color: white;
            padding: 12px 20px;
            border-radius: 25px;
            font-weight: 600;
            display: inline-block;
            margin-top: 15px;
            box-shadow: 0 4px 15px rgba(245, 158, 11, 0.3);
        }
        
        /* High-DPI Canvas Optimization */
        canvas {
            image-rendering: -webkit-optimize-contrast;
            image-rendering: crisp-edges;
            image-rendering: pixelated;
        }
        
        /* Responsive Typography */
        @media (max-width: 768px) {
            .dashboard-container {
                padding: 0 15px;
            }
            
            .section-card {
                padding: 25px;
            }
            
            .chart-container,
            .interactive-chart-container {
                height: 400px;
                padding: 20px;
            }
        }
        
        /* Smooth Animations */
        .section-card {
            animation: fadeInUp 0.6s ease-out;
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
        
        /* Better Text Rendering */
        h1, h2, h3, h4, h5, h6 {
            font-weight: 700;
            letter-spacing: -0.025em;
        }
        
        .text-muted {
            color: #64748b !important;
            font-weight: 500;
        }
        
        /* Enhanced Form Elements */
        .form-select {
            background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%23343a40' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='m1 6 7 7 7-7'/%3e%3c/svg%3e");
        }
        
        /* Improved Shadows and Depth */
        .section-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 25px 80px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
        }
    </style>'''
    
    content = content.replace(old_styles, new_styles)
    
    # Add viewport meta tag for better mobile rendering
    if '<meta name="viewport"' not in content:
        viewport_meta = '<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">'
        head_start = content.find('<head>')
        if head_start != -1:
            head_end = content.find('>', head_start) + 1
            content = content[:head_end] + '\n    ' + viewport_meta + content[head_end:]
    
    # Enhance Chart.js configuration for better pixel quality
    chart_config_improvements = '''
        // High-DPI Canvas Configuration
        Chart.defaults.font.family = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
        Chart.defaults.font.size = 13;
        Chart.defaults.font.weight = '500';
        Chart.defaults.color = '#374151';
        Chart.defaults.borderColor = 'rgba(229, 231, 235, 0.8)';
        Chart.defaults.backgroundColor = 'rgba(249, 250, 251, 0.8)';
        
        // Device Pixel Ratio for Retina Displays
        Chart.defaults.devicePixelRatio = window.devicePixelRatio || 2;
        
        '''
    
    # Find the script section and add improvements
    script_start = content.find('<script>')
    if script_start != -1:
        content = content[:script_start + 8] + chart_config_improvements + content[script_start + 8:]
    
    # Write the enhanced template
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Enhanced pixel quality and visual appearance!")
    print("\n🎨 Visual Improvements:")
    print("   - High-DPI and Retina display optimization")
    print("   - Anti-aliased fonts and smooth text rendering")
    print("   - Enhanced shadows and depth effects")
    print("   - Better color contrast and readability")
    print("   - Improved chart canvas quality")
    print("   - Responsive design for all screen sizes")
    print("\n📱 Technical Enhancements:")
    print("   - Device pixel ratio optimization")
    print("   - Crisp canvas rendering")
    print("   - Smooth animations and transitions")
    print("   - Better typography and spacing")
    print("   - Enhanced form elements")
    print("   - Backdrop blur effects")

if __name__ == "__main__":
    improve_pixel_quality()