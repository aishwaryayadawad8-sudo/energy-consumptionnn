#!/usr/bin/env python3

"""
Make Objective 4 website cover fullscreen without margins or padding
"""

def make_fullscreen_layout():
    """Convert Objective 4 to fullscreen layout covering entire viewport"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective4.html"
    
    # Read current template
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the entire CSS section for fullscreen layout
    old_css_start = content.find('<style>')
    old_css_end = content.find('</style>') + 8
    
    if old_css_start == -1 or old_css_end == -1:
        print("❌ Could not find CSS section")
        return
    
    # New fullscreen CSS
    new_fullscreen_css = '''    <style>
        /* Fullscreen Reset - Remove all margins and padding */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            text-rendering: optimizeLegibility;
        }
        
        html, body {
            width: 100%;
            height: 100vh;
            overflow-x: hidden;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            line-height: 1.6;
            font-size: 16px;
            color: #2c3e50;
        }
        
        /* Fullscreen Dashboard Container */
        .dashboard-container {
            width: 100vw;
            height: 100vh;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            overflow-y: auto;
        }
        
        /* Fullscreen Header */
        .header-section {
            background: rgba(255, 255, 255, 0.98);
            padding: 20px 30px;
            margin: 0;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            backdrop-filter: blur(10px);
            border: none;
            border-radius: 0;
            flex-shrink: 0;
        }
        
        .back-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 25px;
            margin-bottom: 15px;
            font-weight: 600;
            font-size: 14px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }
        
        .back-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        }
        
        /* Fullscreen Content Area */
        .content-area {
            flex: 1;
            padding: 20px 30px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        /* Fullscreen Section Cards */
        .section-card {
            background: rgba(255, 255, 255, 0.98);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.2);
            flex-shrink: 0;
        }
        
        .section-title {
            color: #2c3e50;
            font-weight: 700;
            margin-bottom: 20px;
            font-size: 1.5rem;
            letter-spacing: -0.5px;
        }
        
        /* Fullscreen Chart Containers */
        .chart-container {
            position: relative;
            height: calc(100vh - 400px);
            min-height: 400px;
            max-height: 600px;
            margin-top: 15px;
            background: rgba(248, 250, 252, 0.8);
            border-radius: 12px;
            padding: 20px;
            border: 1px solid rgba(226, 232, 240, 0.8);
        }
        
        .interactive-chart-container {
            position: relative;
            height: calc(100vh - 350px);
            min-height: 450px;
            max-height: 700px;
            margin-top: 15px;
            background: rgba(240, 248, 255, 0.9);
            border-radius: 12px;
            padding: 25px;
            border: 1px solid rgba(59, 130, 246, 0.2);
            box-shadow: 0 8px 32px rgba(59, 130, 246, 0.1);
        }
        
        /* Form Elements */
        .country-select {
            border-radius: 8px;
            padding: 12px 16px;
            border: 2px solid #e2e8f0;
            font-size: 15px;
            font-weight: 500;
            background: rgba(255, 255, 255, 0.9);
            transition: all 0.3s ease;
            width: 100%;
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
            padding: 12px 25px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 15px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
            width: 100%;
        }
        
        .btn-load:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        }
        
        /* Loading States */
        .loading {
            text-align: center;
            padding: 40px;
            color: #64748b;
        }
        
        .spinner-border {
            width: 3rem;
            height: 3rem;
        }
        
        .best-model-badge {
            background: linear-gradient(135deg, #f59e0b 0%, #f97316 100%);
            color: white;
            padding: 10px 16px;
            border-radius: 20px;
            font-weight: 600;
            display: inline-block;
            margin-top: 12px;
            box-shadow: 0 4px 15px rgba(245, 158, 11, 0.3);
        }
        
        /* Responsive Grid */
        .row {
            display: flex;
            flex-wrap: wrap;
            margin: 0 -10px;
        }
        
        .col-md-8 {
            flex: 0 0 66.666667%;
            padding: 0 10px;
        }
        
        .col-md-4 {
            flex: 0 0 33.333333%;
            padding: 0 10px;
        }
        
        .col-12 {
            flex: 0 0 100%;
            padding: 0 10px;
        }
        
        /* Mobile Fullscreen Optimization */
        @media (max-width: 768px) {
            .header-section {
                padding: 15px 20px;
            }
            
            .content-area {
                padding: 15px 20px;
            }
            
            .section-card {
                padding: 20px;
            }
            
            .chart-container,
            .interactive-chart-container {
                height: calc(100vh - 300px);
                min-height: 300px;
                padding: 15px;
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
        
        /* Tablet Optimization */
        @media (min-width: 769px) and (max-width: 1024px) {
            .chart-container,
            .interactive-chart-container {
                height: calc(100vh - 350px);
                min-height: 400px;
            }
        }
        
        /* Large Screen Optimization */
        @media (min-width: 1400px) {
            .chart-container,
            .interactive-chart-container {
                height: calc(100vh - 400px);
                min-height: 500px;
                max-height: 800px;
            }
        }
        
        /* Smooth Scrolling */
        .dashboard-container {
            scroll-behavior: smooth;
        }
        
        /* Enhanced Canvas Quality */
        canvas {
            image-rendering: -webkit-optimize-contrast;
            image-rendering: crisp-edges;
            image-rendering: pixelated;
        }
        
        /* Text Selection */
        ::selection {
            background: rgba(102, 126, 234, 0.2);
        }
        
        /* Scrollbar Styling */
        .dashboard-container::-webkit-scrollbar {
            width: 8px;
        }
        
        .dashboard-container::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.1);
        }
        
        .dashboard-container::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.3);
            border-radius: 4px;
        }
        
        .dashboard-container::-webkit-scrollbar-thumb:hover {
            background: rgba(255, 255, 255, 0.5);
        }
        
        /* Utility Classes */
        .text-muted {
            color: #64748b !important;
            font-weight: 500;
        }
        
        .mt-2 {
            margin-top: 0.5rem;
        }
        
        .mb-2 {
            margin-bottom: 0.5rem;
        }
        
        .w-100 {
            width: 100%;
        }
    </style>'''
    
    # Replace the CSS
    content = content[:old_css_start] + new_fullscreen_css + content[old_css_end:]
    
    # Update the body structure for fullscreen layout
    old_body_structure = '''<body>
    <div class="dashboard-container">
        <div class="header-section">'''
    
    new_body_structure = '''<body>
    <div class="dashboard-container">
        <div class="header-section">'''
    
    # Find and wrap content sections in content-area div
    content_start = content.find('<!-- Model Comparison Section')
    if content_start != -1:
        # Insert content-area wrapper
        content = content[:content_start] + '        </div>\n        <div class="content-area">\n        ' + content[content_start:]
        
        # Close content-area before closing dashboard-container
        script_start = content.find('    <script')
        if script_start != -1:
            content = content[:script_start] + '        </div>\n    ' + content[script_start:]
    
    # Write the fullscreen template
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Converted Objective 4 to fullscreen layout!")
    print("\n🖥️ Fullscreen Features:")
    print("   - 100vw x 100vh coverage (full viewport)")
    print("   - Zero margins and padding")
    print("   - Responsive chart heights based on viewport")
    print("   - Optimized for all screen sizes")
    print("   - Smooth scrolling for content overflow")
    print("   - Custom scrollbar styling")
    print("\n📱 Responsive Breakpoints:")
    print("   - Mobile: < 768px (compact layout)")
    print("   - Tablet: 769px - 1024px (medium layout)")
    print("   - Desktop: > 1024px (full layout)")
    print("   - Large: > 1400px (expanded layout)")

if __name__ == "__main__":
    make_fullscreen_layout()