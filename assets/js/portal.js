// Generate starfield
const starfield = document.getElementById('starfield');
for (let i = 0; i < 100; i++) {
    const star = document.createElement('div');
    star.className = 'star';
    star.style.left = Math.random() * 100 + '%';
    star.style.top = Math.random() * 100 + '%';
    star.style.animationDelay = Math.random() * 3 + 's';
    starfield.appendChild(star);
}

// Scene transition logic
const scene1 = document.getElementById('scene-1');
const pathSelection = document.getElementById('path-selection');
const nextBtn = document.getElementById('next-btn');
const overlay = document.getElementById('transition-overlay');

// Initial Fade In (Scene 1)
window.addEventListener('load', () => {
    overlay.style.animation = 'fadeFromBlack 2s ease-out forwards';
});

// Scene 1 -> Timeline Menu (Fade to black, swap, Fade from black)
nextBtn.addEventListener('click', function () {
    // 1. Fade OUT
    overlay.style.animation = 'none'; // reset
    overlay.offsetHeight; // trigger reflow
    overlay.style.animation = 'fadeToBlack 1.5s ease-in forwards';

    setTimeout(() => {
        // 2. SWAP Content (While Screen is Black)
        scene1.style.display = 'none';
        pathSelection.style.display = 'flex';
        window.scrollTo(0, 0);

        // 3. Fade IN (Reveal Timeline & Video)
        overlay.style.animation = 'none'; // reset
        overlay.offsetHeight; // trigger reflow
        overlay.style.animation = 'fadeFromBlack 2s ease-out forwards';

    }, 1500); // Wait for fade out to finish
});

// Smooth scroll for other links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        if (this.getAttribute('href') === '#') return; // Ignore placeholders
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Handle Portal Navigation (Fade out -> Go to URL)
document.querySelectorAll('.path-node').forEach(node => {
    node.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        
        // Ignore hash links (handled by smooth scroll or internal navigation)
        if (!href || href.startsWith('#')) return;

        e.preventDefault();

        // Trigger Fade to Black
        overlay.style.animation = 'none';
        overlay.offsetHeight; // trigger reflow
        overlay.style.animation = 'fadeToBlack 1.5s ease-in forwards';

        // Navigate after animation
        setTimeout(() => {
            window.location.href = href;
        }, 1500);
    });
});

// Debounce resize to prevent performance hit
let resizeTimer;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        drawTimelineLines(); // Call your existing drawing function
    }, 250);
});

// Update the drawTimelineLines function (or equivalent) to handle mobile X coordinates:
function drawTimelineLines() {
    const steps = document.querySelectorAll('.timeline-step');
    const isMobile = window.innerWidth <= 768;
    
    steps.forEach((step, index) => {
        if (index === steps.length - 1) return; // Skip last
        
        const nextStep = steps[index + 1];
        const connector = step.querySelector('.step-connector');
        
        // CLEAR existing SVG first
        if (connector) connector.innerHTML = ''; 
        
        if (!connector) return;

        // Get positions relative to the connector container
        const startX = isMobile ? 20 : (step.offsetWidth / 2); // Mobile: align left (20px), Desktop: center
        const startY = step.offsetHeight / 2;
        const endX = isMobile ? 20 : (nextStep.offsetLeft - step.offsetLeft + (nextStep.offsetWidth / 2));
        const endY = nextStep.offsetTop - step.offsetTop + (nextStep.offsetHeight / 2);
        
        // Create SVG
        const svgns = "http://www.w3.org/2000/svg";
        const svg = document.createElementNS(svgns, "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        
        const path = document.createElementNS(svgns, "path");
        // Simple curve logic
        const d = `M ${startX} ${startY} C ${startX} ${startY + 50}, ${endX} ${endY - 50}, ${endX} ${endY}`;
        
        path.setAttribute("d", d);
        path.setAttribute("stroke", "var(--grid-line)");
        path.setAttribute("stroke-width", "2");
        path.setAttribute("fill", "none");
        
        svg.appendChild(path);
        connector.appendChild(svg);
    });
}

// Initial draw
document.addEventListener('DOMContentLoaded', drawTimelineLines);
