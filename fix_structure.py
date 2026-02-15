import os
import shutil

# --- CONTENT DEFINITIONS ---

CSS_CONTENT = """:root {
    --kubrick-white: #f5f5f5;
    --kubrick-red: #d32f2f;
    --kubrick-black: #0a0a0a;
    --spielberg-blue: #1a237e;
    --spielberg-gold: #ffc107;
    --glow: rgba(255, 193, 7, 0.6);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Futura', 'Gill Sans', 'Century Gothic', sans-serif;
    background: linear-gradient(180deg, #000000 0%, #0a0a14 50%, #000000 100%);
    color: var(--kubrick-white);
    overflow-x: hidden;
    letter-spacing: 0.05em;
}

/* Opening Scene - Full Screen Film Experience */
.opening-scene {
    height: 100vh;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    background: radial-gradient(ellipse at center, rgba(26, 35, 126, 0.3) 0%, transparent 70%);
    z-index: 10;
}

/* Fixed Video Background for Timeline */
.video-background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    opacity: 0.6;
}

    .video-background video {
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: brightness(0.7) contrast(1.1);
    }

.video-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(ellipse at center, transparent 0%, rgba(0, 0, 0, 0.8) 100%);
    mix-blend-mode: multiply;
}

.title-card {
    position: relative;
    z-index: 2;
    text-align: center;
    animation: fadeInTitle 2s ease-out 0.5s both;
}

@keyframes fadeInTitle {
    from {
        opacity: 0;
        transform: translateY(30px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.film-title {
    font-size: clamp(3rem, 10vw, 8rem);
    font-weight: 100;
    letter-spacing: 0.15em;
    line-height: 1.1;
    text-transform: uppercase;
    margin: 0;
    text-shadow: 0 0 40px rgba(255, 193, 7, 0.6), 0 0 80px rgba(255, 193, 7, 0.3), 2px 2px 4px rgba(0, 0, 0, 0.8);
    animation: titlePulse 4s ease-in-out infinite;
}

@keyframes titlePulse {
    0%, 100% {
        text-shadow: 0 0 40px rgba(255, 193, 7, 0.6), 0 0 80px rgba(255, 193, 7, 0.3), 2px 2px 4px rgba(0, 0, 0, 0.8);
    }

    50% {
        text-shadow: 0 0 60px rgba(255, 193, 7, 0.8), 0 0 120px rgba(255, 193, 7, 0.5), 2px 2px 4px rgba(0, 0, 0, 0.8);
    }
}

.film-subtitle {
    font-size: clamp(1rem, 2vw, 1.8rem);
    font-weight: 300;
    letter-spacing: 0.3em;
    margin-top: 1.5rem;
    opacity: 0.85;
    text-shadow: 0 2px 10px rgba(0, 0, 0, 0.8);
}

/* Fade Overlay for Scene Transitions */
.fade-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: #000000;
    z-index: 9999;
    pointer-events: none;
    opacity: 0;
}

@keyframes fadeToBlack {
    0% {
        opacity: 0;
    }

    100% {
        opacity: 1;
    }
}

@keyframes fadeFromBlack {
    0% {
        opacity: 1;
    }

    100% {
        opacity: 0;
    }
}

/* Next Button - Cinematic Style */
.next-button {
    position: absolute;
    bottom: 3rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 2;
    background: transparent;
    border: 2px solid rgba(255, 193, 7, 0.5);
    color: var(--kubrick-white);
    padding: 1rem 2.5rem;
    font-family: inherit;
    font-size: 1rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    cursor: pointer;
    transition: all 0.4s;
    display: flex;
    align-items: center;
    gap: 1rem;
    animation: fadeInPrompt 2s ease-out 3s both;
}

    .next-button:hover {
        border-color: var(--spielberg-gold);
        background: rgba(255, 193, 7, 0.1);
        box-shadow: 0 0 30px rgba(255, 193, 7, 0.3);
        transform: translateX(-50%) scale(1.05);
    }

    .next-button .arrow {
        font-size: 1.5rem;
        transition: transform 0.4s;
    }

    .next-button:hover .arrow {
        transform: translateX(5px);
    }

@keyframes fadeInPrompt {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

/* Path Selection - Choose Your Own Adventure */
.path-selection {
    min-height: 100vh;
    padding: 6rem 2rem;
    position: relative;
    display: none; /* Hidden initially */
    flex-direction: column;
    align-items: center;
}

.chapter-title {
    font-size: clamp(2rem, 5vw, 3.5rem);
    font-weight: 100;
    letter-spacing: 0.2em;
    text-align: center;
    margin-bottom: 4rem;
    text-transform: uppercase;
    opacity: 0.9;
    text-shadow: 0 0 20px rgba(0,0,0,0.8);
}

.path-container {
    position: relative;
    max-width: 800px;
    width: 100%;
}

.path-line {
    position: absolute;
    left: 50%;
    top: 0;
    bottom: 0;
    width: 2px;
    background: linear-gradient(180deg, transparent 0%, rgba(255, 193, 7, 0.3) 10%, rgba(255, 193, 7, 0.3) 90%, transparent 100%);
    transform: translateX(-50%);
}

.path-node {
    position: relative;
    display: flex;
    align-items: center;
    margin: 4rem 0;
    text-decoration: none;
    color: inherit;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

    .path-node:hover:not(.path-locked) {
        transform: scale(1.05);
    }

.node-ring {
    position: absolute;
    left: 50%;
    width: 60px;
    height: 60px;
    border: 2px solid rgba(255, 193, 7, 0.5);
    border-radius: 50%;
    transform: translateX(-50%);
    transition: all 0.4s;
    z-index: 2;
    background: rgba(0, 0, 0, 0.8);
    box-shadow: 0 0 20px rgba(255, 193, 7, 0.3);
}

.path-node:hover:not(.path-locked) .node-ring {
    border-color: var(--spielberg-gold);
    box-shadow: 0 0 30px rgba(255, 193, 7, 0.6), 0 0 60px rgba(255, 193, 7, 0.3), inset 0 0 20px rgba(255, 193, 7, 0.2);
    transform: translateX(-50%) scale(1.2);
}

.node-content {
    background: rgba(10, 10, 20, 0.7);
    border: 1px solid rgba(255, 193, 7, 0.2);
    padding: 2rem;
    margin-left: 60%;
    width: 40%;
    backdrop-filter: blur(10px);
    transition: all 0.4s;
}

.path-node:nth-child(odd) .node-content {
    margin-left: 0;
    margin-right: 60%;
    text-align: right;
}

.path-node:hover:not(.path-locked) .node-content {
    border-color: rgba(255, 193, 7, 0.5);
    background: rgba(10, 10, 20, 0.85);
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
}

.node-number {
    display: block;
    font-size: 3rem;
    font-weight: 100;
    opacity: 0.3;
    line-height: 1;
    margin-bottom: 0.5rem;
}

.node-content h3 {
    font-size: 1.5rem;
    font-weight: 300;
    letter-spacing: 0.1em;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
}

.node-content p {
    font-size: 0.9rem;
    opacity: 0.7;
    letter-spacing: 0.05em;
    line-height: 1.6;
}

.path-locked {
    opacity: 0.5;
    cursor: not-allowed;
    pointer-events: none;
}

.coming-soon {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 0.75rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    background: rgba(0, 0, 0, 0.9);
    padding: 0.5rem 1rem;
    border: 1px solid rgba(255, 193, 7, 0.3);
    border-radius: 20px;
    white-space: nowrap;
    z-index: 3;
    animation: superNova 2s infinite ease-in-out;
}

@keyframes superNova {
    0% {
        box-shadow: 0 0 10px rgba(255, 193, 7, 0.3);
        text-shadow: 0 0 5px rgba(255, 193, 7, 0.3);
        border-color: rgba(255, 193, 7, 0.3);
    }
    50% {
        box-shadow: 0 0 30px rgba(255, 193, 7, 0.8), 0 0 60px rgba(255, 50, 0, 0.4);
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.8);
        border-color: rgba(255, 255, 255, 0.8);
    }
    100% {
        box-shadow: 0 0 10px rgba(255, 193, 7, 0.3);
        text-shadow: 0 0 5px rgba(255, 193, 7, 0.3);
        border-color: rgba(255, 193, 7, 0.3);
    }
}

/* Footer - Minimalist */
footer {
    text-align: center;
    padding: 3rem 2rem;
    font-size: 0.9rem;
    opacity: 0.6;
    letter-spacing: 0.1em;
    border-top: 1px solid rgba(255, 193, 7, 0.1);
    margin-top: 4rem;
}

/* Responsive */
@media (max-width: 768px) {
    .film-title {
        letter-spacing: 0.1em;
    }

    .path-selection {
        padding: 4rem 1rem;
    }

    .chapter-title {
        margin-bottom: 3rem;
    }

    .path-node {
        margin: 3rem 0;
        align-items: flex-start;
    }

    .node-content {
        margin-left: 0 !important;
        margin-right: 0 !important;
        width: calc(100% - 2rem);
        text-align: left !important;
        padding: 1.5rem;
        margin-top: 5rem;
    }

    .node-ring {
        left: 1rem;
        top: 0;
        transform: none;
    }

    .path-node:hover:not(.path-locked) .node-ring {
        transform: scale(1.2);
    }

    .path-line {
        left: calc(1rem + 30px);
    }
}

/* Starfield Background */
.stars {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: -2; /* Behind everything */
}

.star {
    position: absolute;
    width: 2px;
    height: 2px;
    background: white;
    border-radius: 50%;
    animation: twinkle 3s infinite;
}

@keyframes twinkle {
    0%, 100% {
        opacity: 0.3;
    }

    50% {
        opacity: 1;
    }
}

/* Fix SVG scaling on mobile */
.step-connector svg {
    width: 100% !important;
    height: 100% !important;
    min-height: 100px; /* Ensure minimum height */
    overflow: visible; /* Prevent cutting off curves */
}

/* Fix step layout overlap */
.timeline-step {
    position: relative;
    padding-bottom: 2rem; /* Add space between cards */
    display: flex;
    flex-direction: column;
}

/* Mobile specific fixes */
@media (max-width: 768px) {
    .timeline {
        padding: 0 1rem;
    }
    
    .timeline-step {
        margin-bottom: 3rem; /* More space between steps on mobile */
    }

    /* Force line to stay behind/left properly */
    .step-connector {
        position: absolute;
        left: 20px; /* Adjust based on your number circle position */
        top: 50px;
        bottom: -30px;
        width: 2px;
        background: var(--grid-line); /* Fallback straight line if SVG fails */
        z-index: 0;
    }
    
    /* Hide the complex SVG on mobile if it's too broken, use straight line */
    .step-connector svg {
        display: none; 
    }
}

/* Ensure timeline step has relative positioning context */
.timeline-step {
    position: relative !important;
    min-height: 150px; /* Give it vertical breathing room */
    margin-bottom: 2rem;
}

/* Force the SVG container to cover the full height */
.step-connector {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 0;
}

/* Make SVG responsive */
.step-connector svg {
    width: 100%;
    height: 100%;
    overflow: visible;
}
"""

JS_CONTENT = """// Generate starfield
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
"""

def fix_project_structure():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"📂 Working in: {base_dir}")
    
    # 1. Ensure directories exist
    dirs_to_create = [
        'assets/css',
        'assets/js',
        'assets/video',
        'assets/images',
        'portals/media-career',
        'portals/portfolio',
        'portals/portfolio/Brian-Krawitz-Portfolio'
    ]
    
    for d in dirs_to_create:
        path = os.path.join(base_dir, d)
        os.makedirs(path, exist_ok=True)
        print(f"📁 Verified directory: {d}")

    # 2. Write CSS and JS files (Force Restore)
    css_path = os.path.join(base_dir, 'assets/css/portal.css')
    js_path = os.path.join(base_dir, 'assets/js/portal.js')
    
    try:
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(CSS_CONTENT)
        print(f"✅ Restored: assets/css/portal.css")
    except Exception as e:
        print(f"❌ Error writing CSS: {e}")

    try:
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(JS_CONTENT)
        print(f"✅ Restored: assets/js/portal.js")
    except Exception as e:
        print(f"❌ Error writing JS: {e}")

    # 3. Find and Move Video (Preserve existing video)
    video_filename = 'abstract-video.mp4'
    video_target = os.path.join(base_dir, 'assets/video', video_filename)
    
    if os.path.exists(video_target):
        print(f"✅ Video found at: assets/video/{video_filename}")
    else:
        # Search for it
        found = False
        for root, dirs, files in os.walk(base_dir):
            if video_filename in files:
                src = os.path.join(root, video_filename)
                try:
                    shutil.move(src, video_target)
                    print(f"🚚 Moved video to: assets/video/{video_filename}")
                    found = True
                    break
                except Exception as e:
                    print(f"❌ Error moving video: {e}")
        
        if not found:
            print(f"⚠️  MISSING VIDEO: {video_filename} (Please place your video in assets/video/)")

    # 4. Print Final Structure
    print("\n--- FINAL STRUCTURE CHECK ---")
    for root, dirs, files in os.walk(base_dir):
        level = root.replace(base_dir, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if f in ['portal.css', 'portal.js', 'index.html', 'abstract-video.mp4']:
                print(f"{subindent}{f}")

if __name__ == "__main__":
    print("🔧 RESTORING PROJECT ASSETS...")
    fix_project_structure()
    print("\nDone! Please run 'python3 server.py' and open http://localhost:8001")