function validateForm() {
    var fullname = document.forms["signupForm"]["full_name"].value;
    var fullnameErrorField = document.getElementById("fullname-error");
    var email = document.forms["signupForm"]["email"].value;
    var emailError = document.getElementById("email-error");
    var phone = document.forms["signupForm"]["phone"].value;
    var phoneError = document.getElementById("phone-error");
    var password1 = document.forms["signupForm"]["password1"].value;
    var password1Error = document.getElementById("password1-error");
    var password2 = document.forms["signupForm"]["password2"].value;
    var password2Error = document.getElementById("password2-error");

    // Validate full name
    if (fullname.trim() === "") {
        fullnameErrorField.innerHTML = "Please enter your full name";
        return false;
    } else if (fullname.trim().split(" ").length < 2) {
        fullnameErrorField.innerHTML = "Please enter your full name";
        return false;
    } else if (fullname.length < 2) {
        fullnameErrorField.innerHTML = "Please enter your full name";
        return false;
    } else {
        fullnameErrorField.innerHTML = "";
    }

    // Validate email
    if (email.trim() === "") {
        emailError.innerHTML = "Please enter your email";
        return false;
    } else if (!email.includes("@")) {
        emailError.innerHTML = "Please enter a valid email";
        return false;
    } else {
        emailError.innerHTML = "";
    }

    // Validate Phone Number
    if (phone.trim() === "") {
        phoneError.innerHTML = "Please enter your phone number";
        return false;
    } else if (phone.length < 10 || isNaN(phone) || phone.startsWith("98")) {
        phoneError.innerHTML = "Please enter a valid phone number";
        return false;
    } else {
        phoneError.innerHTML = "";
    }

    // Validate Password
    if (password1.trim() === "") {
        password1Error.innerHTML = "Please enter your password";
        return false;
    } else if (password1.length < 8) {
        password1Error.innerHTML = "Password must be at least 8 characters";
        return false;
    } else {
        password1Error.innerHTML = "";
    }

    // Validate Confirm Password
    if (password2.trim() === "") {
        password2Error.innerHTML = "Please re-enter your password";
        return false;
    } else if (password2 !== password1) {
        password2Error.innerHTML = "Password does not match";
        return false;
    } else {
        password2Error.innerHTML = "";
    }

    // If all validations pass, the form is valid
    return true;
}
