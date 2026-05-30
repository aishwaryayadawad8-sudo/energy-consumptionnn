#!/usr/bin/env python3

import os
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sustainable_energy.settings')
django.setup()

def create_ultra_unique_design():
    """Create ultra-unique design enhancements for the webpage"""
    
    # 1. Create advanced CSS with morphing elements and 3D effects
    advanced_css = """
/* Ultra-Unique Morphing and 3D Effects */

/* Morphing Logo Animation */
.logo-orb {
    position: relative;
    background: 
        conic-gradient(from 0deg at 50% 50%, 
            #ff0080 0deg, 
            #00ff80 72deg, 
            #8000ff 144deg, 
            #ff8000 216deg, 
            #0080ff 288deg, 
            #ff0080 360deg);
    animation: morphLogo 8s ease-in-out infinite, orbRotate 4s linear infinite;
    filter: blur(0.5px) brightness(1.2);
    box-shadow: 
        0 0 40px rgba(255, 0, 128, 0.6),
        0 0 80px rgba(0, 255, 128, 0.4),
        inset 0 0 40px rgba(255, 255, 255, 0.2);
}

@keyframes morphLogo {
    0%, 100% { 
        border-radius: 50%; 
        transform: scale(1) rotate(0deg);
    }
    25% { 
        border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%; 
        transform: scale(1.1) rotate(90deg);
    }
    50% { 
        border-radius: 70% 30% 30% 70% / 70% 70% 30% 30%; 
        transform: scale(0.9) rotate(180deg);
    }
    75% { 
        border-radius: 40% 60% 60% 40% / 60% 40% 40% 60%; 
        transform: scale(1.05) rotate(270deg);
    }
}

/* Holographic Text with Glitch Effect */
.title-holo {
    position: relative;
    animation: titleGlow 3s ease-in-out infinite alternate, glitchText 5s infinite;
}

.title-holo::before,
.title-holo::after {
    content: attr(data-text);
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(45deg, #ff0080, #00ff80, #8000ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.title-holo::before {
    animation: glitch1 2s infinite;
    z-index: -1;
}

.title-holo::after {
    animation: glitch2 2s infinite;
    z-index: -2;
}

@keyframes glitchText {
    0%, 90%, 100% { transform: translate(0); }
    10% { transform: translate(-2px, 2px); }
    20% { transform: translate(2px, -2px); }
    30% { transform: translate(-2px, -2px); }
    40% { transform: translate(2px, 2px); }
    50% { transform: translate(-2px, 2px); }
    60% { transform: translate(2px, -2px); }
    70% { transform: translate(-2px, -2px); }
    80% { transform: translate(2px, 2px); }
}

@keyframes glitch1 {
    0%, 100% { transform: translate(0); }
    20% { transform: translate(-2px, 2px); }
    40% { transform: translate(-2px, -2px); }
    60% { transform: translate(2px, 2px); }
    80% { transform: translate(2px, -2px); }
}

@keyframes glitch2 {
    0%, 100% { transform: translate(0); }
    20% { transform: translate(2px, 0px); }
    40% { transform: translate(-2px, 0px); }
    60% { transform: translate(0px, 2px); }
    80% { transform: translate(0px, -2px); }
}

/* 3D Floating Navigation Icons */
.quantum-sphere {
    transform-style: preserve-3d;
    position: relative;
    background: 
        radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.4) 0%, transparent 70%),
        conic-gradient(from 0deg, 
            rgba(255, 0, 128, 0.3) 0deg, 
            rgba(0, 255, 128, 0.3) 120deg, 
            rgba(128, 0, 255, 0.3) 240deg, 
            rgba(255, 0, 128, 0.3) 360deg);
    animation: float3D 6s ease-in-out infinite;
}

.quantum-sphere::before {
    content: '';
    position: absolute;
    top: -5px;
    left: -5px;
    right: -5px;
    bottom: -5px;
    border-radius: 50%;
    background: conic-gradient(from 0deg, transparent, rgba(255, 0, 128, 0.5), transparent);
    animation: rotate3D 3s linear infinite;
    z-index: -1;
}

@keyframes float3D {
    0%, 100% { 
        transform: translateY(0px) rotateX(0deg) rotateY(0deg); 
    }
    33% { 
        transform: translateY(-10px) rotateX(15deg) rotateY(120deg); 
    }
    66% { 
        transform: translateY(5px) rotateX(-10deg) rotateY(240deg); 
    }
}

@keyframes rotate3D {
    0% { transform: rotateZ(0deg); }
    100% { transform: rotateZ(360deg); }
}

/* Quantum Tunnel Effect for Cards */
.quantum-card {
    perspective: 1000px;
    transform-style: preserve-3d;
    position: relative;
    overflow: visible;
}

.quantum-card::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 200%;
    height: 200%;
    transform: translate(-50%, -50%) rotateX(75deg);
    background: 
        repeating-conic-gradient(from 0deg at 50% 50%, 
            transparent 0deg, 
            rgba(0, 255, 255, 0.1) 10deg, 
            transparent 20deg);
    border-radius: 50%;
    opacity: 0;
    transition: all 0.5s ease;
    z-index: -1;
    animation: tunnelSpin 10s linear infinite;
}

.quantum-card:hover::before {
    opacity: 1;
    transform: translate(-50%, -50%) rotateX(75deg) scale(1.2);
}

@keyframes tunnelSpin {
    0% { transform: translate(-50%, -50%) rotateX(75deg) rotateZ(0deg); }
    100% { transform: translate(-50%, -50%) rotateX(75deg) rotateZ(360deg); }
}

/* Morphing Button with Liquid Effect */
.cta-holo {
    position: relative;
    overflow: hidden;
    background: 
        linear-gradient(135deg, 
            rgba(255, 0, 128, 0.2) 0%, 
            rgba(0, 255, 128, 0.2) 50%, 
            rgba(128, 0, 255, 0.2) 100%);
    border: 2px solid transparent;
    background-clip: padding-box;
    animation: morphButton 4s ease-in-out infinite;
}

.cta-holo::before {
    content: '';
    position: absolute;
    top: -2px;
    left: -2px;
    right: -2px;
    bottom: -2px;
    background: conic-gradient(from 0deg, #ff0080, #00ff80, #8000ff, #ff0080);
    border-radius: inherit;
    z-index: -1;
    animation: borderRotate 3s linear infinite;
}

@keyframes morphButton {
    0%, 100% { border-radius: 50px; }
    25% { border-radius: 20px 50px 20px 50px; }
    50% { border-radius: 10px; }
    75% { border-radius: 50px 20px 50px 20px; }
}

@keyframes borderRotate {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* Holographic Scan Lines */
.holo-header::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
        repeating-linear-gradient(
            0deg,
            transparent 0px,
            rgba(0, 255, 255, 0.03) 1px,
            transparent 2px,
            transparent 4px
        );
    animation: scanLines 2s linear infinite;
    pointer-events: none;
}

@keyframes scanLines {
    0% { transform: translateY(-100%); }
    100% { transform: translateY(100%); }
}

/* Quantum Particle System Enhancement */
.particle-background::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
        radial-gradient(1px 1px at 20px 30px, rgba(255, 0, 128, 0.8), transparent),
        radial-gradient(1px 1px at 40px 70px, rgba(0, 255, 128, 0.8), transparent),
        radial-gradient(1px 1px at 90px 40px, rgba(128, 0, 255, 0.8), transparent),
        radial-gradient(1px 1px at 130px 80px, rgba(255, 128, 0, 0.8), transparent),
        radial-gradient(1px 1px at 160px 30px, rgba(0, 128, 255, 0.8), transparent);
    background-repeat: repeat;
    background-size: 250px 150px;
    animation: quantumParticles 25s linear infinite;
}

@keyframes quantumParticles {
    0% { transform: translate(0, 0) rotate(0deg); }
    100% { transform: translate(-250px, -150px) rotate(360deg); }
}

/* Neural Network Connections */
.quantum-grid::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
        linear-gradient(45deg, transparent 48%, rgba(0, 255, 255, 0.1) 49%, rgba(0, 255, 255, 0.1) 51%, transparent 52%),
        linear-gradient(-45deg, transparent 48%, rgba(255, 0, 128, 0.1) 49%, rgba(255, 0, 128, 0.1) 51%, transparent 52%);
    background-size: 100px 100px;
    animation: neuralNetwork 8s ease-in-out infinite;
    pointer-events: none;
    z-index: 0;
}

@keyframes neuralNetwork {
    0%, 100% { opacity: 0.3; transform: scale(1); }
    50% { opacity: 0.6; transform: scale(1.05); }
}

/* Holographic Data Stream */
.main-title-holo::before {
    content: '';
    position: absolute;
    top: -20px;
    left: -20px;
    right: -20px;
    bottom: -20px;
    background: 
        repeating-linear-gradient(
            90deg,
            transparent 0px,
            rgba(0, 255, 255, 0.1) 1px,
            transparent 2px,
            transparent 20px
        ),
        repeating-linear-gradient(
            0deg,
            transparent 0px,
            rgba(255, 0, 128, 0.1) 1px,
            transparent 2px,
            transparent 20px
        );
    animation: dataStream 3s linear infinite;
    z-index: -1;
}

@keyframes dataStream {
    0% { transform: translate(0, 0); }
    100% { transform: translate(20px, 20px); }
}

/* Quantum Ripple Effect on Hover */
.quantum-icon::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(0, 255, 255, 0.3) 0%, transparent 70%);
    transform: translate(-50%, -50%);
    transition: all 0.6s ease;
    z-index: -1;
}

.quantum-icon:hover::after {
    width: 200px;
    height: 200px;
    animation: quantumRipple 1s ease-out;
}

@keyframes quantumRipple {
    0% { 
        width: 0; 
        height: 0; 
        opacity: 1; 
    }
    100% { 
        width: 200px; 
        height: 200px; 
        opacity: 0; 
    }
}

/* Responsive Enhancements */
@media (max-width: 768px) {
    .quantum-sphere {
        animation: float3D 4s ease-in-out infinite;
    }
    
    .morphButton {
        animation-duration: 3s;
    }
    
    .title-holo {
        animation-duration: 2s;
    }
}

/* Ultra-Unique Cursor Trail */
.cursor-trail {
    position: fixed;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(0, 255, 255, 0.6) 0%, transparent 70%);
    pointer-events: none;
    z-index: 9999;
    mix-blend-mode: screen;
    animation: cursorPulse 1s ease-in-out infinite alternate;
}

@keyframes cursorPulse {
    0% { transform: scale(0.8); opacity: 0.8; }
    100% { transform: scale(1.2); opacity: 0.4; }
}
"""
    
    # Write the advanced CSS
    css_path = Path("sustainable_energy/static/css/ultra-unique-effects.css")
    css_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(advanced_css)
    
    print("✅ Created ultra-unique CSS effects")
    
    # 2. Create advanced JavaScript for interactive effects
    advanced_js = """
// Ultra-Unique Interactive Effects
class UltraUniqueEffects {
    constructor() {
        this.cursorTrails = [];
        this.maxTrails = 10;
        this.init();
    }
    
    init() {
        this.createCursorTrail();
        this.createHolographicText();
        this.createQuantumParticles();
        this.createNeuralConnections();
        this.createMorphingElements();
        this.createInteractiveBackground();
    }
    
    // Cursor Trail Effect
    createCursorTrail() {
        document.addEventListener('mousemove', (e) => {
            // Create trail element
            const trail = document.createElement('div');
            trail.className = 'cursor-trail';
            trail.style.left = e.clientX - 10 + 'px';
            trail.style.top = e.clientY - 10 + 'px';
            document.body.appendChild(trail);
            
            // Remove after animation
            setTimeout(() => {
                if (trail.parentNode) {
                    trail.parentNode.removeChild(trail);
                }
            }, 1000);
        });
    }
    
    // Holographic Text Effect
    createHolographicText() {
        const titles = document.querySelectorAll('.title-holo, .main-title-holo');
        titles.forEach(title => {
            title.setAttribute('data-text', title.textContent);
            
            // Add glitch effect on hover
            title.addEventListener('mouseenter', () => {
                title.style.animation = 'glitchText 0.3s infinite, titleGlow 3s ease-in-out infinite alternate';
            });
            
            title.addEventListener('mouseleave', () => {
                title.style.animation = 'titleGlow 3s ease-in-out infinite alternate';
            });
        });
    }
    
    // Quantum Particle System
    createQuantumParticles() {
        const particleContainer = document.createElement('div');
        particleContainer.className = 'quantum-particles';
        particleContainer.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
        `;
        document.body.appendChild(particleContainer);
        
        // Create floating particles
        for (let i = 0; i < 20; i++) {
            const particle = document.createElement('div');
            particle.style.cssText = `
                position: absolute;
                width: ${2 + Math.random() * 4}px;
                height: ${2 + Math.random() * 4}px;
                background: radial-gradient(circle, rgba(${Math.random() * 255}, ${Math.random() * 255}, 255, 0.8) 0%, transparent 70%);
                border-radius: 50%;
                left: ${Math.random() * 100}%;
                top: ${Math.random() * 100}%;
                animation: quantumFloat ${10 + Math.random() * 10}s linear infinite;
            `;
            particleContainer.appendChild(particle);
        }
        
        // Add CSS for quantum float animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes quantumFloat {
                0% { transform: translateY(0px) translateX(0px) rotate(0deg); opacity: 0; }
                10% { opacity: 1; }
                90% { opacity: 1; }
                100% { transform: translateY(-100vh) translateX(${Math.random() * 200 - 100}px) rotate(360deg); opacity: 0; }
            }
        `;
        document.head.appendChild(style);
    }
    
    // Neural Network Connections
    createNeuralConnections() {
        const cards = document.querySelectorAll('.quantum-card');
        const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        svg.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
        `;
        document.body.appendChild(svg);
        
        // Create connections between cards
        cards.forEach((card, index) => {
            card.addEventListener('mouseenter', () => {
                this.drawNeuralConnections(svg, card, cards);
            });
            
            card.addEventListener('mouseleave', () => {
                svg.innerHTML = '';
            });
        });
    }
    
    drawNeuralConnections(svg, activeCard, allCards) {
        svg.innerHTML = '';
        const activeRect = activeCard.getBoundingClientRect();
        const activeCenterX = activeRect.left + activeRect.width / 2;
        const activeCenterY = activeRect.top + activeRect.height / 2;
        
        allCards.forEach(card => {
            if (card !== activeCard) {
                const rect = card.getBoundingClientRect();
                const centerX = rect.left + rect.width / 2;
                const centerY = rect.top + rect.height / 2;
                
                const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                line.setAttribute('x1', activeCenterX);
                line.setAttribute('y1', activeCenterY);
                line.setAttribute('x2', centerX);
                line.setAttribute('y2', centerY);
                line.setAttribute('stroke', 'rgba(0, 255, 255, 0.3)');
                line.setAttribute('stroke-width', '1');
                line.style.animation = 'neuralPulse 2s ease-in-out infinite';
                
                svg.appendChild(line);
            }
        });
        
        // Add pulse animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes neuralPulse {
                0%, 100% { stroke-opacity: 0.3; stroke-width: 1; }
                50% { stroke-opacity: 0.8; stroke-width: 2; }
            }
        `;
        document.head.appendChild(style);
    }
    
    // Morphing Elements
    createMorphingElements() {
        const morphElements = document.querySelectorAll('.quantum-sphere, .logo-orb');
        
        morphElements.forEach(element => {
            element.addEventListener('mouseenter', () => {
                element.style.animation = 'morphLogo 2s ease-in-out infinite, float3D 3s ease-in-out infinite';
            });
            
            element.addEventListener('mouseleave', () => {
                element.style.animation = 'float3D 6s ease-in-out infinite, orbRotate 4s linear infinite';
            });
        });
    }
    
    // Interactive Background
    createInteractiveBackground() {
        document.addEventListener('click', (e) => {
            this.createClickRipple(e.clientX, e.clientY);
        });
        
        // Add scroll-based effects
        window.addEventListener('scroll', () => {
            const scrollPercent = window.scrollY / (document.body.scrollHeight - window.innerHeight);
            document.documentElement.style.setProperty('--scroll-percent', scrollPercent);
        });
    }
    
    createClickRipple(x, y) {
        const ripple = document.createElement('div');
        ripple.style.cssText = `
            position: fixed;
            left: ${x - 25}px;
            top: ${y - 25}px;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(0, 255, 255, 0.6) 0%, transparent 70%);
            pointer-events: none;
            z-index: 9999;
            animation: clickRipple 1s ease-out forwards;
        `;
        
        document.body.appendChild(ripple);
        
        setTimeout(() => {
            if (ripple.parentNode) {
                ripple.parentNode.removeChild(ripple);
            }
        }, 1000);
        
        // Add ripple animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes clickRipple {
                0% { transform: scale(0); opacity: 1; }
                100% { transform: scale(4); opacity: 0; }
            }
        `;
        document.head.appendChild(style);
    }
}

// Enhanced Electric Background with 3D effects
class Enhanced3DElectricBackground extends ElectricBackground {
    constructor() {
        super();
        this.lightning = [];
        this.energyOrbs = [];
        this.initEnhanced();
    }
    
    initEnhanced() {
        // Create lightning bolts
        for (let i = 0; i < 5; i++) {
            this.lightning.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                segments: this.generateLightningSegments(),
                opacity: 0,
                life: 0,
                maxLife: 30 + Math.random() * 20
            });
        }
        
        // Create energy orbs
        for (let i = 0; i < 8; i++) {
            this.energyOrbs.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                radius: 5 + Math.random() * 10,
                vx: (Math.random() - 0.5) * 2,
                vy: (Math.random() - 0.5) * 2,
                color: `hsl(${180 + Math.random() * 60}, 80%, 60%)`,
                pulse: Math.random() * Math.PI * 2
            });
        }
    }
    
    generateLightningSegments() {
        const segments = [];
        let x = Math.random() * this.canvas.width;
        let y = 0;
        
        while (y < this.canvas.height) {
            segments.push({ x, y });
            x += (Math.random() - 0.5) * 100;
            y += 20 + Math.random() * 30;
        }
        
        return segments;
    }
    
    animate() {
        super.animate();
        
        // Draw lightning
        this.lightning.forEach(bolt => {
            bolt.life++;
            
            if (bolt.life > bolt.maxLife) {
                bolt.life = 0;
                bolt.segments = this.generateLightningSegments();
                bolt.opacity = 0;
            }
            
            if (bolt.life < 10) {
                bolt.opacity = bolt.life / 10;
            } else if (bolt.life > bolt.maxLife - 10) {
                bolt.opacity = (bolt.maxLife - bolt.life) / 10;
            } else {
                bolt.opacity = 0.8 + Math.random() * 0.2;
            }
            
            // Draw lightning bolt
            if (bolt.segments.length > 1) {
                this.ctx.beginPath();
                this.ctx.moveTo(bolt.segments[0].x, bolt.segments[0].y);
                
                for (let i = 1; i < bolt.segments.length; i++) {
                    this.ctx.lineTo(bolt.segments[i].x, bolt.segments[i].y);
                }
                
                this.ctx.strokeStyle = `rgba(0, 255, 255, ${bolt.opacity})`;
                this.ctx.lineWidth = 2 + Math.random() * 3;
                this.ctx.stroke();
                
                // Add glow effect
                this.ctx.shadowColor = 'rgba(0, 255, 255, 0.8)';
                this.ctx.shadowBlur = 10;
                this.ctx.stroke();
                this.ctx.shadowBlur = 0;
            }
        });
        
        // Draw energy orbs
        this.energyOrbs.forEach(orb => {
            orb.x += orb.vx;
            orb.y += orb.vy;
            orb.pulse += 0.1;
            
            // Bounce off edges
            if (orb.x < 0 || orb.x > this.canvas.width) orb.vx *= -1;
            if (orb.y < 0 || orb.y > this.canvas.height) orb.vy *= -1;
            
            const pulsedRadius = orb.radius + Math.sin(orb.pulse) * 3;
            
            // Draw orb with glow
            this.ctx.beginPath();
            this.ctx.arc(orb.x, orb.y, pulsedRadius, 0, Math.PI * 2);
            
            const gradient = this.ctx.createRadialGradient(
                orb.x, orb.y, 0,
                orb.x, orb.y, pulsedRadius
            );
            gradient.addColorStop(0, orb.color.replace('60%)', '80%)'));
            gradient.addColorStop(1, 'transparent');
            
            this.ctx.fillStyle = gradient;
            this.ctx.fill();
            
            // Add outer glow
            this.ctx.shadowColor = orb.color;
            this.ctx.shadowBlur = 20;
            this.ctx.fill();
            this.ctx.shadowBlur = 0;
        });
    }
}

// Initialize enhanced effects
document.addEventListener('DOMContentLoaded', () => {
    new UltraUniqueEffects();
    new Enhanced3DElectricBackground();
});
"""
    
    # Write the advanced JavaScript
    js_path = Path("sustainable_energy/static/js/ultra-unique-effects.js")
    js_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(advanced_js)
    
    print("✅ Created ultra-unique JavaScript effects")
    
    # 3. Update base template to include new effects
    base_template_path = Path("sustainable_energy/dashboard/templates/dashboard/base.html")
    
    with open(base_template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add new CSS and JS includes
    if 'ultra-unique-effects.css' not in content:
        content = content.replace(
            '<link rel="stylesheet" href="{% static \'css/electric-background.css\' %}">',
            '<link rel="stylesheet" href="{% static \'css/electric-background.css\' %}">\n    <link rel="stylesheet" href="{% static \'css/ultra-unique-effects.css\' %}">'
        )
    
    if 'ultra-unique-effects.js' not in content:
        content = content.replace(
            '<script src="{% static \'js/electric-animation.js\' %}"></script>',
            '<script src="{% static \'js/electric-animation.js\' %}"></script>\n    <script src="{% static \'js/ultra-unique-effects.js\' %}"></script>'
        )
    
    with open(base_template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Updated base template with new effects")
    
    # 4. Create a unique 404 page with special effects
    error_404_template = """
{% extends 'dashboard/base.html' %}
{% load static %}

{% block title %}404 - Quantum Void{% endblock %}

{% block extra_css %}
<style>
    .void-container {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        background: radial-gradient(circle at center, rgba(128, 0, 255, 0.1) 0%, transparent 70%);
        position: relative;
        overflow: hidden;
    }
    
    .void-content {
        text-align: center;
        z-index: 2;
        position: relative;
    }
    
    .void-title {
        font-family: 'Orbitron', monospace;
        font-size: 8rem;
        font-weight: 900;
        background: linear-gradient(45deg, #ff0080, #8000ff, #00ff80);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 30px;
        animation: voidGlitch 2s infinite, voidFloat 4s ease-in-out infinite;
        text-shadow: 0 0 50px rgba(128, 0, 255, 0.5);
    }
    
    .void-message {
        font-size: 1.5rem;
        color: rgba(255, 255, 255, 0.8);
        margin-bottom: 40px;
        animation: fadeInOut 3s ease-in-out infinite;
    }
    
    .void-portal {
        width: 300px;
        height: 300px;
        border-radius: 50%;
        background: 
            radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.2) 0%, transparent 70%),
            conic-gradient(from 0deg, #ff0080, #8000ff, #00ff80, #ff0080);
        margin: 0 auto 40px;
        animation: portalSpin 5s linear infinite, portalPulse 3s ease-in-out infinite;
        position: relative;
    }
    
    .void-portal::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 80%;
        height: 80%;
        background: radial-gradient(circle, rgba(0, 0, 0, 0.8) 30%, transparent 70%);
        border-radius: 50%;
        transform: translate(-50%, -50%);
    }
    
    @keyframes voidGlitch {
        0%, 90%, 100% { transform: translate(0); }
        10% { transform: translate(-5px, 5px); }
        20% { transform: translate(5px, -5px); }
        30% { transform: translate(-5px, -5px); }
        40% { transform: translate(5px, 5px); }
        50% { transform: translate(-5px, 5px); }
        60% { transform: translate(5px, -5px); }
        70% { transform: translate(-5px, -5px); }
        80% { transform: translate(5px, 5px); }
    }
    
    @keyframes voidFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    @keyframes fadeInOut {
        0%, 100% { opacity: 0.8; }
        50% { opacity: 1; }
    }
    
    @keyframes portalSpin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    @keyframes portalPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
</style>
{% endblock %}

{% block content %}
<div class="void-container">
    <div class="void-content">
        <h1 class="void-title">404</h1>
        <div class="void-portal"></div>
        <p class="void-message">You've entered the Quantum Void</p>
        <a href="/" class="cta-holo">
            <i class="fas fa-home"></i> Return to Reality
        </a>
    </div>
</div>
{% endblock %}
"""
    
    error_404_path = Path("sustainable_energy/dashboard/templates/dashboard/404.html")
    with open(error_404_path, 'w', encoding='utf-8') as f:
        f.write(error_404_template)
    
    print("✅ Created unique 404 error page")
    
    print("\n🎨 ULTRA-UNIQUE DESIGN ENHANCEMENTS COMPLETE!")
    print("\nNew Features Added:")
    print("• Morphing logo with shape-shifting animation")
    print("• Holographic text with glitch effects")
    print("• 3D floating navigation icons")
    print("• Quantum tunnel effects for cards")
    print("• Liquid morphing buttons")
    print("• Interactive cursor trails")
    print("• Neural network connections")
    print("• Enhanced lightning and energy orbs")
    print("• Click ripple effects")
    print("• Unique 404 error page")
    print("• Advanced particle systems")
    print("• Holographic scan lines")
    print("\n🚀 Your webpage is now ULTRA-UNIQUE!")

if __name__ == "__main__":
    create_ultra_unique_design()