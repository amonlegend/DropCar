// document.addEventListener('DOMContentLoaded', () => {
//     const pickupLocationInput = document.getElementById('pickupLocation');
//     const dropOffLocationInput = document.getElementById('dropOffLocation');
//     const locationsInput = document.getElementById('locations');
//     const pickupLocationList = document.getElementById('pickupLocationList');
//     const dropOffLocationList = document.getElementById('dropOffLocationList');

//     // Parse the list of locations from the hidden input field
//     const allLocations = JSON.parse(locationsInput.value).map(location => location.fields.location.toLowerCase());

//     // Function to filter and show suggestions
//     const showSuggestions = (inputElement, dataListElement) => {
//         const inputText = inputElement.value.toLowerCase();
//         const filteredLocations = allLocations.filter(location => location.startsWith(inputText));

//         // Clear previous suggestions
//         dataListElement.innerHTML = '';

//         // Add filtered locations to the datalist
//         filteredLocations.forEach(location => {
//             const option = document.createElement('option');
//             option.value = location;
//             dataListElement.appendChild(option);
//         });

//         // Show the datalist
//         dataListElement.hidden = filteredLocations.length === 0;
//     };

//     // Event listener for input typing in pickup location
//     pickupLocationInput.addEventListener('input', () => {
//         showSuggestions(pickupLocationInput, pickupLocationList);
//     });

//     // Event listener for clearing the pickup location input field
//     pickupLocationInput.addEventListener('input', () => {
//         if (pickupLocationInput.value === '') {
//             pickupLocationList.innerHTML = '';
//             pickupLocationList.hidden = true;
//         }
//     });

//     // Event listener for input typing in drop-off location
//     dropOffLocationInput.addEventListener('input', () => {
//         showSuggestions(dropOffLocationInput, dropOffLocationList);
//     });

//     // Event listener for clearing the drop-off location input field
//     dropOffLocationInput.addEventListener('input', () => {
//         if (dropOffLocationInput.value === '') {
//             dropOffLocationList.innerHTML = '';
//             dropOffLocationList.hidden = true;
//         }
//     });
// });

document.addEventListener("DOMContentLoaded", function () {
  var form = document.getElementById("rentalForm");
  var pickupDateInput = document.getElementById("pickup-datetime");
  var returnDateInput = document.getElementById("return-datetime");

  form.addEventListener("submit", function (event) {
    var pickupDate = new Date(pickupDateInput.value);
    var returnDate = new Date(returnDateInput.value);
    var currentDate = new Date();

    // Add 1 minute to the current time to ensure that the current time is not considered as the past
    currentDate.setMinutes(currentDate.getMinutes() + 1);

    if (pickupDate <= currentDate || returnDate <= currentDate) {
      event.preventDefault(); // Prevent form submission
      alert(
        "Please select pick-up and drop-off dates and times in the future."
      );
    } else if (pickupDate >= returnDate) {
      event.preventDefault(); // Prevent form submission
      alert(
        "The drop-off date and time must be after the pick-up date and time."
      );
    }
  });
});
