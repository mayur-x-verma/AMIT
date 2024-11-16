// static/js/main.js

// Change navbar opacity on scroll
window.addEventListener("scroll", function() {
    const header = document.querySelector("header");
    if (window.scrollY > 50) {
        header.style.opacity = "0.7"; // Less opaque when scrolled
    } else {
        header.style.opacity = "1"; // Fully opaque when at top
    }
});
