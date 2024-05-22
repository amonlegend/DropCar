// Get the modal element
var modal = document.getElementById("message-modal");
var modalClose = document.getElementById("close-info");

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modalClose) {
        modal.style.display = "none";
    }
}
const popupForm = document.getElementById('popupForm');
const editProfileButton = document.getElementById('edit_profile_pic_button');

// Get the close button and the file input
const closeButton = popupForm.querySelector('.close-btn');
const fileInput = popupForm.querySelector('input[type="file"]');

// Add event listener to the edit profile button
editProfileButton.addEventListener('click', () => {
  popupForm.style.display = 'block'; // Show the popup form
});

// Add event listener to the close button
closeButton.addEventListener('click', () => {
  popupForm.style.display = 'none'; // Hide the popup form
});

// Add event listener to the file input
fileInput.addEventListener('change', () => {
  // Handle the file upload logic here
  // You can use the FormData API to submit the form
  const formData = new FormData();
  formData.append('profile_pic', fileInput.files[0]);

  // Make the AJAX request to the server
  fetch('{% url "update_profile_pic" %}', {
    method: 'POST',
    body: formData,
    headers: {
      'X-CSRFToken': '{{ csrf_token }}'
    }
  })
  .then(response => {
    // Handle the response from the server
    console.log(response);
  })
  .catch(error => {
    // Handle any errors
    console.error(error);
  });
});