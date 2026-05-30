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