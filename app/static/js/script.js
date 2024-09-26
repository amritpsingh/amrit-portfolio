// Smooth scroll functionality
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Fixed header on scroll
window.addEventListener('scroll', () => {
    const header = document.querySelector('.main-header');
    if (window.scrollY > 100) {
        header.classList.add('navbar-scrolled'); // 'fixed-header'
    } else {
        header.classList.remove('navbar-scrolled');  // 'fixed-header'
    }
});

// Typing animation (if you're using Typed.js)
document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('type-it')) {
        new Typed('#type-it', {
            strings: ['Data Analyst', 'ML Engineer', 'AI Engineer'],
            typeSpeed: 100,
            loop: true
        });
    }
});