template_content = """{% extends 'dashboard/base.html' %}
{% load static %}

{% block title %}SDG 7 Dashboard - Sustainable Energy Analysis & Prediction{% endblock %}

{% block extra_css %}
<style>
    body {
        margin: 0;
        padding: 0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .hero-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 0;
        position: relative;
        overflow: hidden;
    }
    
    .hero-content {
        position: relative;
        z-index: 2;
        padding: 3rem 0;
        text-align: center;
    }
    
    .hero-background {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300"><defs><linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:%23667eea;stop-opacity:0.8" /><stop offset="100%" style="stop-color:%23764ba2;stop-opacity:0.8" /></linearGradient></defs><rect width="1000" height="300" fill="url(%23grad)"/><circle cx="100" cy="50" r="20" fill="rgba(255,255,255,0.1)"/><circ