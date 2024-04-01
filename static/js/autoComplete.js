// Fetch locations from Django backend and update autocomplete
function fetchLocationsAndUpdateAutocomplete(inputElement, datalistElement) {
    fetch('locationsUrl')
        .then(response => response.json())
        .then(data => {
            const locations = data.map(location => location.name); // Assuming 'name' is the attribute for location name in your JSON response
            datalistElement.innerHTML = ''; // Clear existing options
            locations.forEach(location => {
                const option = document.createElement('option');
                option.value = location;
                datalistElement.appendChild(option);
            });
        })
        .catch(error => console.error('Error fetching locations:', error));
}

document.addEventListener('DOMContentLoaded', () => {
    const pickupLocationInput = document.getElementById('pickupLocation');
    const dropOffLocationInput = document.getElementById('dropOffLocation');
    const pickupLocationDatalist = document.getElementById('pickupLocationList');
    const dropOffLocationDatalist = document.getElementById('dropOffLocationList');

    // Fetch and update pickup locations on input change
    pickupLocationInput.addEventListener('input', () => {
        fetchLocationsAndUpdateAutocomplete(pickupLocationInput, pickupLocationDatalist);
    });

    // Fetch and update drop-off locations on input change
    dropOffLocationInput.addEventListener('input', () => {
        fetchLocationsAndUpdateAutocomplete(dropOffLocationInput, dropOffLocationDatalist);
    });
});
