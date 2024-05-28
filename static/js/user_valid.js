document.getElementById('profileForm').addEventListener('submit', function(event) {
    let valid = true;

    // Clear previous error messages
    document.getElementById('full_name_error').textContent = '';
    document.getElementById('phone_number_error').textContent = '';
    document.getElementById('email_error').textContent = '';

    // Full Name validation
    const fullName = document.getElementById('full_name').value.trim();
    const nameParts = fullName.split(' ');
    if (nameParts.length < 2) {
        document.getElementById('full_name_error').textContent = 'Please enter at least two words for full name.';
        valid = false;
    }

    // Mobile Number validation
    const phoneNumber = document.getElementById('phone_number').value.trim();
    const phonePattern = /^98\d{8}$/; // Phone number should start with "98" followed by 8 digits
    if (!phonePattern.test(phoneNumber)) {
        document.getElementById('phone_number_error').textContent = 'Phone number should start with "98" and have 10 digits in total.';
        valid = false;
    }

    // Email validation
    const email = document.getElementById('inputEmail4').value.trim();
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        document.getElementById('email_error').textContent = 'Please enter a valid email address.';
        valid = false;
    }

    // If any validation fails, prevent form submission
    if (!valid) {
        event.preventDefault();
    }
});



function validatePasswordForm() {
    var password = document.forms["passwordForm"]["new_password1"].value;
    var passwordErrorField = document.getElementById("password-error");
    var confirmPassword = document.forms["passwordForm"]["new_password2"].value;
    var confirmPasswordErrorField = document.getElementById("confirm-password-error");
  
    // Password validation
    if (password.trim === "") {
      passwordErrorField.innerText = "Please enter password.";
      return false;
    } else if (password.length < 8) {
      passwordErrorField.innerText ="Password must be at least 8 characters long.";
      return false;
    } else {
      passwordErrorField.innerText = "";
    }
  
    // Validate Confirm Password
  
    if (confirmPassword.trim() === "") {
      confirmPasswordErrorField.innerText = "Please enter password to confirm.";
      return false;
    } else{
      confirmPasswordErrorField.innerText = "";
    }
  
    // Confirm password validation
    if (password !== confirmPassword) {
      confirmPasswordErrorField.innerText = "Passwords do not match.";
      return false;
    } else {
      confirmPasswordErrorField.innerText = "";
    }
  
    return true;
  }