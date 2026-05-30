// Electric Shock Wave Animation
class ElectricBackground {
    constructor() {
        this.canvas = document.getElementById('electric-canvas');
        if (!this.canvas) return;
        
        this.ctx = this.canvas.getContext('2d');
        this.waves = [];
        this.particles = [];
        this.time = 0;
        
        this.init();
        this.animate();
    }
    
    init() {
        this.resize();
        window.addEventListener('resize', () => this.resize());
        
        // Create initial waves
        for (let i = 0; i < 3; i++) {
            this.waves.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                radius: 0,
                maxRadius: 200 + Math.random() * 100,
                speed: 0.2 + Math.random() * 0.2, // Slowed down from 0.5 + Math.random() * 0.5
                opacity: 0.1 + Math.random() * 0.2,
                color: `hsl(${210 + Math.random() * 30}, 70%, 60%)`
            });
        }
        
        // Create particles
        for (let i = 0; i < 50; i++) {
            this.particles.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                vx: (Math.random() - 0.5) * 0.2, // Slowed down from 0.5
                vy: (Math.random() - 0.5) * 0.2, // Slowed down from 0.5
                size: 1 + Math.random() * 2,
                opacity: 0.3 + Math.random() * 0.4,
                color: `hsl(${25 + Math.random() * 30}, 80%, 60%)`
            });
        }
    }
    
    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }
    
    animate() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Create gradient background
        const gradient = this.ctx.createLinearGradient(0, 0, 0, this.canvas.height);
        gradient.addColorStop(0, 'rgba(30, 60, 114, 0.05)');
        gradient.addColorStop(0.5, 'rgba(102, 126, 234, 0.03)');
        gradient.addColorStop(1, 'rgba(118, 75, 162, 0.05)');
        
        this.ctx.fillStyle = gradient;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Update and draw waves
        this.waves.forEach((wave, index) => {
            wave.radius += wave.speed;
            
            if (wave.radius > wave.maxRadius) {
                // Reset wave
                wave.x = Math.random() * this.canvas.width;
                wave.y = Math.random() * this.canvas.height;
                wave.radius = 0;
                wave.maxRadius = 200 + Math.random() * 100;
                wave.opacity = 0.1 + Math.random() * 0.2;
            }
            
            // Draw wave
            this.ctx.beginPath();
            this.ctx.arc(wave.x, wave.y, wave.radius, 0, Math.PI * 2);
            this.ctx.strokeStyle = wave.color.replace('60%)', `60%, ${wave.opacity * (1 - wave.radius / wave.maxRadius)})`);
            this.ctx.lineWidth = 2;
            this.ctx.stroke();
        });
        
        // Update and draw particles
        this.particles.forEach(particle => {
            particle.x += particle.vx;
            particle.y += particle.vy;
            
            // Wrap around screen
            if (particle.x < 0) particle.x = this.canvas.width;
            if (particle.x > this.canvas.width) particle.x = 0;
            if (particle.y < 0) particle.y = this.canvas.height;
            if (particle.y > this.canvas.height) particle.y = 0;
            
            // Draw particle
            this.ctx.beginPath();
            this.ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
            this.ctx.fillStyle = particle.color.replace('60%)', `60%, ${particle.opacity})`);
            this.ctx.fill();
        });
        
        // Add floating energy lines
        this.time += 0.005; // Slowed down from 0.01
        for (let i = 0; i < 3; i++) {
            const x1 = Math.sin(this.time + i) * 100 + this.canvas.width / 2;
            const y1 = Math.cos(this.time + i * 0.5) * 50 + this.canvas.height / 2;
            const x2 = Math.sin(this.time + i + 1) * 120 + this.canvas.width / 2;
            const y2 = Math.cos(this.time + i * 0.5 + 1) * 60 + this.canvas.height / 2;
            
            this.ctx.beginPath();
            this.ctx.moveTo(x1, y1);
            this.ctx.lineTo(x2, y2);
            this.ctx.strokeStyle = `hsla(${210 + i * 15}, 70%, 60%, 0.1)`;
            this.ctx.lineWidth = 1;
            this.ctx.stroke();
        }
        
        requestAnimationFrame(() => this.animate());
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ElectricBackground();
});