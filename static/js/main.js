let menu = document.querySelector("#menu-icon");
let navbar = document.querySelector(".navbar");

menu.onclick = () => {
  menu.classList.toggle("bx-x");
  navbar.classList.toggle("active");
};

window.onscroll = () => {
  menu.classList.remove("bx-x");
  navbar.classList.remove("active");
};

const sr = ScrollReveal({
  distance: "60px",
  duration: 1000,
  delay: 100,
  reset: true,
});

sr.reveal(".text", { delay: 0.001, origin: "top" });
sr.reveal(".form-container form", { delay: 0.001, origin: "left" });
sr.reveal(".heading", { delay: 0.001, origin: "top" });
sr.reveal(".ride-container .box", { delay: 0.001, origin: "top" });
sr.reveal(".services-container .box", { delay: 0.001, origin: "top" });
sr.reveal(".about-container .box", { delay: 0.001, origin: "top" });
sr.reveal(".reviews-container", { delay: 0.001, origin: "top" });

// Get the current date and time
var today = new Date();

// Format the date and time as required for datetime-local input
var formattedDate =
  today.getFullYear() +
  "-" +
  ("0" + (today.getMonth() + 1)).slice(-2) +
  "-" +
  ("0" + today.getDate()).slice(-2);
var formattedTime =
  ("0" + today.getHours()).slice(-2) +
  ":" +
  ("0" + today.getMinutes()).slice(-2);
var currentDateTime = formattedDate + "T" + formattedTime;

// Set the minimum value for pickup-datetime and return-datetime inputs
document.getElementById("pickup-datetime").min = currentDateTime;
document.getElementById("return-datetime").min = currentDateTime;
