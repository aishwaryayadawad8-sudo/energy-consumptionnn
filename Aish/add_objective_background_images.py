#!/usr/bin/env python3

"""
Add background images for each objective card to match the energy wave theme
"""

def add_objective_background_images():
    """Add unique background images for each objective card"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective_selector.html"
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and update the objective card CSS to include background images
        old_card_css = '''        /* Objective Cards */
        .objective-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }'''
        
        new_card_css = '''        /* Objective Cards */
        .objective-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        /* Individual Objective Background Images */
        .objective-card:nth-child(1) {
            background: 
                linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.9) 100%),
                linear-gradient(45deg, rgba(255, 193, 7, 0.1) 0%, rgba(255, 152, 0, 0.1) 100%),
                radial-gradient(circle at 80% 20%, rgba(255, 193, 7, 0.2) 0%, transparent 50%);
        }
        
        .objective-card:nth-child(2) {
            background: 
                linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.9) 100%),
                linear-gradient(45deg, rgba(33, 150, 243, 0.1) 0%, rgba(3, 169, 244, 0.1) 100%),
                radial-gradient(circle at 20% 80%, rgba(33, 150, 243, 0.2) 0%, transparent 50%);
        }
        
        .objective-card:nth-child(3) {
            background: 
                linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.9) 100%),
                linear-gradient(45deg, rgba(76, 175, 80, 0.1) 0%, rgba(139, 195, 74, 0.1) 100%),
                radial-gradient(circle at 70% 30%, rgba(76, 175, 80, 0.2) 0%, transparent 50%);
        }
        
        .objective-card:nth-child(4) {
            background: 
                linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.9) 100%),
                linear-gradient(45deg, rgba(244, 67, 54, 0.1) 0%, rgba(255, 87, 34, 0.1) 100%),
                radial-gradient(circle at 30% 70%, rgba(244, 67, 54, 0.2) 0%, transparent 50%);
        }
        
        .objective-card:nth-child(5) {
            background: 
                linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.9) 100%),
                linear-gradient(45deg, rgba(156, 39, 176, 0.1) 0%, rgba(103, 58, 183, 0.1) 100%),
                radial-gradient(circle at 60% 40%, rgba(156, 39, 176, 0.2) 0%, transparent 50%);
        }
        
        .objective-card:nth-child(6) {
            background: 
                linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.9) 100%),
                linear-gradient(45deg, rgba(255, 107, 53, 0.1) 0%, rgba(255, 152, 0, 0.1) 100%),
                radial-gradient(circle at 40% 60%, rgba(255, 107, 53, 0.2) 0%, transparent 50%);
        }
        
        .objective-card:nth-child(7) {
            background: 
                linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.9) 100%),
                linear-gradient(45deg, rgba(0, 188, 212, 0.1) 0%, rgba(0, 150, 136, 0.1) 100%),
                radial-gradient(circle at 80% 80%, rgba(0, 188, 212, 0.2) 0%, transparent 50%);
        }
        
        .objective-card:nth-child(8) {
            background: 
                linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.9) 100%),
                linear-gradient(45deg, rgba(121, 85, 72, 0.1) 0%, rgba(158, 158, 158, 0.1) 100%),
                radial-gradient(circle at 20% 20%, rgba(121, 85, 72, 0.2) 0%, transparent 50%);
        }
        
        .objective-card:nth-child(9) {
            background: 
                linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.9) 100%),
                linear-gradient(45deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%),
                radial-gradient(circle at 50% 50%, rgba(102, 126, 234, 0.2) 0%, transparent 50%);
        }'''
        
        # Replace the CSS
        if old_card_css in content:
            content = content.replace(old_card_css, new_card_css)
        
        # Add animated wave patterns for each card
        wave_animation_css = '''
        
        /* Animated Wave Patterns for Each Card */
        .objective-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            opacity: 0.1;
            pointer-events: none;
            border-radius: 20px;
            z-index: 0;
        }
        
        .objective-card:nth-child(1)::before {
            background: 
                repeating-linear-gradient(
                    45deg,
                    transparent,
                    transparent 10px,
                    rgba(255, 193, 7, 0.1) 10px,
                    rgba(255, 193, 7, 0.1) 20px
                );
            animation: waveMove1 8s linear infinite;
        }
        
        .objective-card:nth-child(2)::before {
            background: 
                repeating-linear-gradient(
                    -45deg,
                    transparent,
                    transparent 15px,
                    rgba(33, 150, 243, 0.1) 15px,
                    rgba(33, 150, 243, 0.1) 30px
                );
            animation: waveMove2 10s linear infinite;
        }
        
        .objective-card:nth-child(3)::before {
            background: 
                repeating-linear-gradient(
                    90deg,
                    transparent,
                    transparent 12px,
                    rgba(76, 175, 80, 0.1) 12px,
                    rgba(76, 175, 80, 0.1) 24px
                );
            animation: waveMove3 12s linear infinite;
        }
        
        .objective-card:nth-child(4)::before {
            background: 
                repeating-linear-gradient(
                    135deg,
                    transparent,
                    transparent 8px,
                    rgba(244, 67, 54, 0.1) 8px,
                    rgba(244, 67, 54, 0.1) 16px
                );
            animation: waveMove4 9s linear infinite;
        }
        
        .objective-card:nth-child(5)::before {
            background: 
                repeating-linear-gradient(
                    60deg,
                    transparent,
                    transparent 14px,
                    rgba(156, 39, 176, 0.1) 14px,
                    rgba(156, 39, 176, 0.1) 28px
                );
            animation: waveMove5 11s linear infinite;
        }
        
        .objective-card:nth-child(6)::before {
            background: 
                repeating-linear-gradient(
                    -60deg,
                    transparent,
                    transparent 11px,
                    rgba(255, 107, 53, 0.1) 11px,
                    rgba(255, 107, 53, 0.1) 22px
                );
            animation: waveMove6 7s linear infinite;
        }
        
        .objective-card:nth-child(7)::before {
            background: 
                repeating-linear-gradient(
                    30deg,
                    transparent,
                    transparent 13px,
                    rgba(0, 188, 212, 0.1) 13px,
                    rgba(0, 188, 212, 0.1) 26px
                );
            animation: waveMove7 13s linear infinite;
        }
        
        .objective-card:nth-child(8)::before {
            background: 
                repeating-linear-gradient(
                    -30deg,
                    transparent,
                    transparent 9px,
                    rgba(121, 85, 72, 0.1) 9px,
                    rgba(121, 85, 72, 0.1) 18px
                );
            animation: waveMove8 6s linear infinite;
        }
        
        .objective-card:nth-child(9)::before {
            background: 
                repeating-linear-gradient(
                    0deg,
                    transparent,
                    transparent 16px,
                    rgba(102, 126, 234, 0.1) 16px,
                    rgba(102, 126, 234, 0.1) 32px
                );
            animation: waveMove9 14s linear infinite;
        }
        
        /* Wave Animation Keyframes */
        @keyframes waveMove1 {
            0% { background-position: 0 0; }
            100% { background-position: 40px 40px; }
        }
        
        @keyframes waveMove2 {
            0% { background-position: 0 0; }
            100% { background-position: -60px 60px; }
        }
        
        @keyframes waveMove3 {
            0% { background-position: 0 0; }
            100% { background-position: 48px 0; }
        }
        
        @keyframes waveMove4 {
            0% { background-position: 0 0; }
            100% { background-position: 32px 32px; }
        }
        
        @keyframes waveMove5 {
            0% { background-position: 0 0; }
            100% { background-position: 56px -56px; }
        }
        
        @keyframes waveMove6 {
            0% { background-position: 0 0; }
            100% { background-position: -44px 44px; }
        }
        
        @keyframes waveMove7 {
            0% { background-position: 0 0; }
            100% { background-position: 52px -52px; }
        }
        
        @keyframes waveMove8 {
            0% { background-position: 0 0; }
            100% { background-position: -36px 36px; }
        }
        
        @keyframes waveMove9 {
            0% { background-position: 0 0; }
            100% { background-position: 64px 0; }
        }
        
        /* Enhanced Hover Effects */
        .objective-card:hover::before {
            opacity: 0.2;
            animation-duration: 3s;
        }'''
        
        # Find where to insert the wave animations (before the existing animations)
        insert_point = '@keyframes energyPulse {'
        if insert_point in content:
            content = content.replace(insert_point, wave_animation_css + '\n        ' + insert_point)
        
        # Ensure content is properly layered
        content_layer_css = '''
        
        /* Ensure content appears above background patterns */
        .objective-title,
        .objective-description,
        .objective-btn,
        .objective-number {
            position: relative;
            z-index: 1;
        }'''
        
        # Add content layering
        if '/* Responsive Design */' in content:
            content = content.replace('/* Responsive Design */', content_layer_css + '\n        /* Responsive Design */')
        
        # Write the updated template
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("🎨 OBJECTIVE BACKGROUND IMAGES ADDED!")
        print("\n✅ Added Features:")
        print("   🎯 Unique background for each objective")
        print("   🌊 Animated wave patterns")
        print("   🎨 Color-coded themes")
        print("   ✨ Enhanced hover effects")
        print("\n🎨 Background Themes:")
        print("   01 - Energy Consumption: Golden waves")
        print("   02 - Electricity Access: Blue electric patterns")
        print("   03 - Renewable Energy: Green nature waves")
        print("   04 - CO₂ Emissions: Red warning patterns")
        print("   05 - Country Forecasting: Purple data waves")
        print("   06 - Investment Strategy: Orange energy flows")
        print("   07 - Policy Impact: Cyan policy patterns")
        print("   08 - Alert System: Brown alert waves")
        print("   09 - ML Comparison: Purple-blue tech patterns")
        print("\n🚀 Each objective now has its unique animated background!")
        
    except Exception as e:
        print(f"❌ Error adding objective backgrounds: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    add_objective_background_images()