"""
Update base template to include electric animation canvas and script
"""

def update_base_template():
    with open('sustainable_energy/dashboard/templates/dashboard/base.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Add canvas and wrapper
    old_body = '''<body class="electric-bg">
    {% block content %}{% endblock %}
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    {% block extra_js %}{% endblock %}
</body>'''
    
    new_body = '''<body class="electric-bg">
    <!-- Electric Shock Wave Canvas -->
    <canvas id="electric-canvas"></canvas>
    
    <!-- Main content wrapper -->
    <div class="main-content-wrapper">
        {% block content %}{% endblock %}
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- Electric Animation Script -->
    <script src="{% static 'js/electric-animation.js' %}"></script>
    {% block extra_js %}{% endblock %}
</body>'''
    
    if old_body in content:
        content = content.replace(old_body, new_body)
        
        with open('sustainable_energy/dashboard/templates/dashboard/base.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Updated base template with electric animation!")
        print("📊 Added:")
        print("   - Canvas element for animation")
        print("   - Main content wrapper")
        print("   - Animation script reference")
        return True
    
    print("❌ Could not find the body section")
    return False

if __name__ == '__main__':
    update_base_template()
