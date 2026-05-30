// Quantum Loading Screen
class QuantumLoader {
    constructor() {
        this.createLoader();
        this.showLoader();
    }
    
    createLoader() {
        const loaderHTML = `
            <div class="quantum-loader-overlay" id="quantum-loader">
                <div class="quantum-loader">
                    <div class="quantum-spinner">
                        <div class="quantum-ring"></div>
                        <div class="quantum-ring"></div>
                        <div class="quantum-ring"></div>
                        <div class="quantum-ring"></div>
                        <div class="quantum-core"></div>
                    </div>
                    <div class="quantum-text">Initializing Quantum Matrix</div>
                    <div class="quantum-progress">
                        <div class="quantum-progress-bar"></div>
                    </div>
                </div>
            </div>
        `;
        
        document.body.insertAdjacentHTML('beforeend', loaderHTML);
    }
    
    showLoader() {
        const loader = document.getElementById('quantum-loader');
        const text = loader.querySelector('.quantum-text');
        const progressBar = loader.querySelector('.quantum-progress-bar');
        
        const messages = [
            'Initializing Quantum Matrix',
            'Loading Neural Networks',
            'Calibrating Energy Sensors',
            'Synchronizing Data Streams',
            'Activating Holographic Interface'
        ];
        
        let messageIndex = 0;
        let progress = 0;
        
        const updateLoader = () => {
            if (messageIndex < messages.length) {
                text.textContent = messages[messageIndex];
                progress += 20;
                progressBar.style.width = progress + '%';
                messageIndex++;
                
                setTimeout(updateLoader, 600);
            } else {
                setTimeout(() => {
                    this.hideLoader();
                }, 500);
            }
        };
        
        setTimeout(updateLoader, 500);
    }
    
    hideLoader() {
        const loader = document.getElementById('quantum-loader');
        loader.classList.add('fade-out');
        
        setTimeout(() => {
            if (loader && loader.parentNode) {
                loader.parentNode.removeChild(loader);
            }
        }, 500);
    }
}

// Auto-initialize loader on page load
document.addEventListener('DOMContentLoaded', () => {
    new QuantumLoader();
});