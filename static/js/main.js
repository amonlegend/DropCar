let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menu.onclick = () => {
    menu.classList.toggle('bx-x');
    navbar.classList.toggle('active');
}

window.onscroll = () => {
    menu.classList.remove('bx-x');
    navbar.classList.remove('active');
}

const sr = ScrollReveal ({
    distance: '60px',
    duration: 1000,
    delay: 100,
    reset: true
})

sr.reveal('.text', {delay: 0.001, origin: 'top'});
sr.reveal('.form-container form', {delay: 0.001, origin: 'left'});
sr.reveal('.heading', {delay: 0.001, origin: 'top'});
sr.reveal('.ride-container .box', {delay: 0.001, origin: 'top'});
sr.reveal('.services-container .box', {delay: 0.001, origin: 'top'});
sr.reveal('.about-container .box', {delay: 0.001, origin: 'top'});
sr.reveal('.reviews-container', {delay: 0.001, origin: 'top'});







