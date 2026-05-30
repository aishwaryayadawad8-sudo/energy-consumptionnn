#!/usr/bin/env python3
"""
Script to add an "Explore Dashboard" button to the main page that leads to the full dashboard
"""

import os

def add_explore_button_to_main_page():
    """Add a prominent Explore Dashboard button to the main objectives page"""
    
    selector_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    if not os.path.exists(selector_path):
        print(f"❌ File not found: {selector_path}")
        return False
    
    try:
        # Read the selector file
        with open(selector_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the content section (after hero section, before objectives)
        content_section_start = content.find('<!-- Content Section -->')
        
        if content_section_start != -1:
            # Add the Explore Dashboard button section
            explore_button_section = '''
<!-- Explore Dashboard Section -->
<section class="explore-dashboard-section">
    <div class="explore-container">
        <div class="explore-card">
            <div class="explore-header">
                <div class="explore-icon">
                    <i class="fas fa-search"></i>
                </div>
                <h2>🔍 Explore Dashboard</h2>
                <p>Interactive Country Energy Analysis & Projections</p>
            </div>
            <div class="explore-content">
                <div class="explore-features">
                    <div class="feature-item">
                        <i class="fas fa-globe"></i>
                        <span>128+ Countries</span>
                    </div>
                    <div class="feature-item">
                        <i class="fas fa-chart-line"></i>
                        <span>Real-time Analysis</span>
                    </div>
                    <div class="feature-item">
                        <i class="fas fa-map"></i>
                        <span>Interactive Maps</span>
                    </div>
                    <div class="feature-item">
                        <i class="fas fa-robot"></i>
                        <span>ML Predictions</span>
                    </div>
                </div>
                <a href="/" class="explore-btn">
                    <i class="fas fa-rocket"></i>
                    Launch Explore Dashboard
                </a>
            </div>
        </div>
    </div>
</section>

'''
            
            # Insert the explore section before the content section
            content = content[:content_section_start] + explore_button_section + content[content_section_start:]
            print("✅ Added Explore Dashboard button section")
        else:
            print("⚠️ Could not find content section insertion point")
        
        # Add CSS styles for the explore section
        styles_end = content.find('</style>')
        if styles_end != -1:
            explore_styles = '''
    
    /* Explore Dashboard Section */
    .explore-dashboard-section {
        padding: 60px 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .explore-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 0 20px;
    }
    
    .explore-card {
        background: white;
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .explore-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
    }
    
    .explore-header {
        margin-bottom: 30px;
    }
    
    .explore-icon {
        width: 80px;
        height: 80px;
        background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 20px;
        color: white;
        font-size: 2rem;
        box-shadow: 0 10px 30px rgba(249, 115, 22, 0.3);
    }
    
    .explore-header h2 {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 10px;
    }
    
    .explore-header p {
        font-size: 1.2rem;
        color: #6b7280;
        margin: 0;
    }
    
    .explore-features {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 20px;
        margin-bottom: 40px;
    }
    
    .feature-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
        padding: 20px;
        background: #f8fafc;
        border-radius: 12px;
        transition: transform 0.3s ease;
    }
    
    .feature-item:hover {
        transform: translateY(-5px);
    }
    
    .feature-item i {
        font-size: 1.5rem;
        color: #f97316;
    }
    
    .feature-item span {
        font-weight: 600;
        color: #374151;
        font-size: 0.9rem;
    }
    
    .explore-btn {
        display: inline-flex;
        align-items: center;
        gap: 12px;
        background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
        color: white;
        padding: 18px 36px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
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
    
    .explore-btn i {
        font-size: 1.2rem;
    }
    
    @media (max-width: 768px) {
        .explore-features {
            grid-template-columns: repeat(2, 1fr);
        }
        
        .explore-header h2 {
            font-size: 2rem;
        }
        
        .explore-card {
            padding: 30px 20px;
        }
    }
'''
            
            content = content[:styles_end] + explore_styles + content[styles_end:]
            print("✅ Added CSS styles for Explore Dashboard section")
        
        # Write the file back
        with open(selector_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully updated {selector_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error adding explore button: {e}")
        return False

def main():
    """Main function"""
    print("🚀 Adding Explore Dashboard Button to Main Page")
    print("="*60)
    print("   • Adding prominent button section")
    print("   • Linking to full dashboard (/)")
    print("   • Beautiful design with features showcase")
    print()
    
    success = add_explore_button_to_main_page()
    
    if success:
        print("\n✅ SUCCESS! Explore Dashboard button added!")
        print("\n📋 What's new:")
        print("   • Prominent 'Explore Dashboard' section on main page")
        print("   • Beautiful card design with features showcase")
        print("   • 'Launch Explore Dashboard' button")
        print("   • Links to full dashboard at /")
        print("\n🎯 User Experience:")
        print("   1. Visit /objectives/ (main page)")
        print("   2. See prominent Explore Dashboard section")
        print("   3. Click 'Launch Explore Dashboard' button")
        print("   4. Go to full dashboard with country search")
        print("\n🎨 Features highlighted:")
        print("   • 128+ Countries")
        print("   • Real-time Analysis")
        print("   • Interactive Maps")
        print("   • ML Predictions")
        print("\n🔄 Refresh your browser to see the new button!")
    else:
        print("\n❌ Failed to add button. Please check the files manually.")

if __name__ == "__main__":
    main()