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