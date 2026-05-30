// Quantum Sound Effects System
class QuantumSounds {
    constructor() {
        this.audioContext = null;
        this.sounds = {};
        this.init();
    }
    
    init() {
        // Initialize Web Audio API
        try {
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            this.createSounds();
            this.attachEventListeners();
        } catch (e) {
            console.log('Web Audio API not supported');
        }
    }
    
    createSounds() {
        // Create different sound effects using oscillators
        this.sounds = {
            hover: this.createHoverSound,
            click: this.createClickSound,
            whoosh: this.createWhooshSound,
            quantum: this.createQuantumSound,
            glitch: this.createGlitchSound
        };
    }
    
    createHoverSound() {
        if (!this.audioContext) return;
        
        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(this.audioContext.destination);
        
        oscillator.frequency.setValueAtTime(800, this.audioContext.currentTime);
        oscillator.frequency.exponentialRampToValueAtTime(1200, this.audioContext.currentTime + 0.1);
        
        gainNode.gain.setValueAtTime(0, this.audioContext.currentTime);
        gainNode.gain.linearRampToValueAtTime(0.1, this.audioContext.currentTime + 0.01);
        gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + 0.1);
        
        oscillator.start(this.audioContext.currentTime);
        oscillator.stop(this.audioContext.currentTime + 0.1);
    }
    
    createClickSound() {
        if (!this.audioContext) return;
        
        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(this.audioContext.destination);
        
        oscillator.frequency.setValueAtTime(1000, this.audioContext.currentTime);
        oscillator.frequency.exponentialRampToValueAtTime(100, this.audioContext.currentTime + 0.1);
        
        gainNode.gain.setValueAtTime(0, this.audioContext.currentTime);
        gainNode.gain.linearRampToValueAtTime(0.2, this.audioContext.currentTime + 0.01);
        gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + 0.1);
        
        oscillator.start(this.audioContext.currentTime);
        oscillator.stop(this.audioContext.currentTime + 0.1);
    }
    
    createWhooshSound() {
        if (!this.audioContext) return;
        
        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();
        const filter = this.audioContext.createBiquadFilter();
        
        oscillator.connect(filter);
        filter.connect(gainNode);
        gainNode.connect(this.audioContext.destination);
        
        oscillator.type = 'sawtooth';
        oscillator.frequency.setValueAtTime(200, this.audioContext.currentTime);
        oscillator.frequency.exponentialRampToValueAtTime(50, this.audioContext.currentTime + 0.3);
        
        filter.type = 'lowpass';
        filter.frequency.setValueAtTime(2000, this.audioContext.currentTime);
        filter.frequency.exponentialRampToValueAtTime(100, this.audioContext.currentTime + 0.3);
        
        gainNode.gain.setValueAtTime(0, this.audioContext.currentTime);
        gainNode.gain.linearRampToValueAtTime(0.15, this.audioContext.currentTime + 0.05);
        gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + 0.3);
        
        oscillator.start(this.audioContext.currentTime);
        oscillator.stop(this.audioContext.currentTime + 0.3);
    }
    
    createQuantumSound() {
        if (!this.audioContext) return;
        
        const oscillator1 = this.audioContext.createOscillator();
        const oscillator2 = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();
        
        oscillator1.connect(gainNode);
        oscillator2.connect(gainNode);
        gainNode.connect(this.audioContext.destination);
        
        oscillator1.frequency.setValueAtTime(440, this.audioContext.currentTime);
        oscillator2.frequency.setValueAtTime(880, this.audioContext.currentTime);
        
        oscillator1.frequency.exponentialRampToValueAtTime(220, this.audioContext.currentTime + 0.2);
        oscillator2.frequency.exponentialRampToValueAtTime(1760, this.audioContext.currentTime + 0.2);
        
        gainNode.gain.setValueAtTime(0, this.audioContext.currentTime);
        gainNode.gain.linearRampToValueAtTime(0.1, this.audioContext.currentTime + 0.02);
        gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + 0.2);
        
        oscillator1.start(this.audioContext.currentTime);
        oscillator2.start(this.audioContext.currentTime);
        oscillator1.stop(this.audioContext.currentTime + 0.2);
        oscillator2.stop(this.audioContext.currentTime + 0.2);
    }
    
    createGlitchSound() {
        if (!this.audioContext) return;
        
        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(this.audioContext.destination);
        
        oscillator.type = 'square';
        
        // Create glitch effect with rapid frequency changes
        const frequencies = [800, 400, 1200, 600, 1000];
        let time = this.audioContext.currentTime;
        
        frequencies.forEach((freq, index) => {
            oscillator.frequency.setValueAtTime(freq, time + index * 0.02);
        });
        
        gainNode.gain.setValueAtTime(0, this.audioContext.currentTime);
        gainNode.gain.linearRampToValueAtTime(0.15, this.audioContext.currentTime + 0.01);
        gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + 0.1);
        
        oscillator.start(this.audioContext.currentTime);
        oscillator.stop(this.audioContext.currentTime + 0.1);
    }
    
    playSound(soundType) {
        if (this.sounds[soundType]) {
            this.sounds[soundType].call(this);
        }
    }
    
    attachEventListeners() {
        // Add sound effects to interactive elements
        document.addEventListener('DOMContentLoaded', () => {
            // Hover sounds for quantum elements
            const quantumElements = document.querySelectorAll('.quantum-icon, .quantum-card, .quantum-sphere');
            quantumElements.forEach(element => {
                element.addEventListener('mouseenter', () => {
                    this.playSound('hover');
                });
            });
            
            // Click sounds for buttons and links
            const clickElements = document.querySelectorAll('.cta-holo, .card-btn-quantum, a');
            clickElements.forEach(element => {
                element.addEventListener('click', () => {
                    this.playSound('click');
                });
            });
            
            // Special sounds for title elements
            const titleElements = document.querySelectorAll('.title-holo, .main-title-holo');
            titleElements.forEach(element => {
                element.addEventListener('mouseenter', () => {
                    this.playSound('quantum');
                });
            });
            
            // Whoosh sound for page transitions
            const navLinks = document.querySelectorAll('a[href]');
            navLinks.forEach(link => {
                link.addEventListener('click', (e) => {
                    if (link.href && !link.href.includes('#')) {
                        this.playSound('whoosh');
                    }
                });
            });
        });
    }
}

// Initialize quantum sounds
const quantumSounds = new QuantumSounds();