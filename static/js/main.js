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
    duration: 2500,
    delay: 400,
    reset: true
})

sr.reveal('.text', {delay: 200, origin: 'top'})
sr.reveal('.form-container form', {delay: 800, origin: 'left'})
sr.reveal('.heading', {delay: 300, origin: 'top'})
sr.reveal('.ride-container .box', {delay: 200, origin: 'top'})
sr.reveal('.services-container .box', {delay: 200, origin: 'top'})
sr.reveal('.about-container .box', {delay: 200, origin: 'top'})
sr.reveal('.reviews-container', {delay: 200, origin: 'top'})

const showPopupBtn = document.querySelector(".log-in");
const formPopup = document.querySelector(".form-popup");
const hidePopupBtn = document.querySelector(".form-popup .close-btn");
const loginSignupLink = document.querySelectorAll(".form-box .bottom-link a")

//Show form popup
showPopupBtn.addEventListener("click", () =>{
    document.body.classList.toggle("show-popup");
});

//Hide form popup
hidePopupBtn.addEventListener("click", () => {
    document.body.classList.remove("show-popup");
    formPopup.classList.remove("show-signup");
});

loginSignupLink.forEach(link =>{
    link.addEventListener("click", (e) =>{
        e.preventDefault();
        formPopup.classList[link.id === "signup-link" ? 'add' : 'remove']("show-signup");
    });
});

//Sign Up Form
const signUpBtn = document.querySelector(".sign-up");

//Show form popup
signUpBtn.addEventListener("click", () => {
    document.body.classList.toggle("show-popup");
    formPopup.classList.add("show-signup");
});

//Hide form popup
hidePopupBtn.addEventListener("click", () => {
    document.body.classList.remove("show-popup");
    formPopup.classList.remove("show-signup");
});





