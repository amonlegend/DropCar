document.addEventListener("DOMContentLoaded", function () {
    var showPassword = document.getElementById("show-icon");
    var showPassword1 = document.getElementById("show-icon1");
    var showPassword2 = document.getElementById("show-icon2");
    var passwordField = document.querySelector("#password-input-field");
    var passwordField1 = document.querySelector("#password1-field");
    var passwordField2 = document.querySelector("#password2-field");
    var showPassword3 = document.getElementById("show-icon3");
    var showPassword4 = document.getElementById("show-icon4");
    var showPassword5 = document.getElementById("show-icon5");
    var passwordField3 = document.querySelector("#exampleInputPassword1");
    var passwordField4 = document.querySelector("#exampleInputPassword2");
    var passwordField5 = document.querySelector("#exampleInputPassword3"); 
  
  
  
    showPassword.addEventListener("click", function () {
      this.classList.toggle("view-hide");
      const type = passwordField.getAttribute("type") === "password" ? "text" : "password";
      passwordField.setAttribute("type", type);
    });
  
    showPassword1.addEventListener("click", function () {
      this.classList.toggle("view-hide");
      const type = passwordField1.getAttribute("type") === "password" ? "text" : "password";
      passwordField1.setAttribute("type", type);
    });
  
  
    showPassword2.addEventListener("click", function () {
      this.classList.toggle("view-hide");
      const type = passwordField2.getAttribute("type") === "password" ? "text" : "password";
      passwordField2.setAttribute("type", type);
    });
  
    showPassword3.addEventListener("click", function () {
        this.classList.toggle("view-hide");
        const type = passwordField3.getAttribute("type") === "password" ? "text" : "password";
        passwordField3.setAttribute("type", type);
      });
      
      showPassword4.addEventListener("click", function () {
        this.classList.toggle("view-hide");
        const type = passwordField4.getAttribute("type") === "password" ? "text" : "password";
        passwordField4.setAttribute("type", type);
      });
      
      showPassword5.addEventListener("click", function () {
        this.classList.toggle("view-hide");
        const type = passwordField5.getAttribute("type") === "password" ? "text" : "password";
        passwordField5.setAttribute("type", type);
      });
      
  });