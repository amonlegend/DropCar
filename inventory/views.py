from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Location, Vehicle

from datetime import datetime

def search_vehicles(request):
    if request.method == "POST":
        # Retrieve form data
        pickup_location = request.POST.get('pickupLocation')
        dropoff_location = request.POST.get('dropOffLocation')
        pickup_datetime_str = request.POST.get('pickup-datetime')
        return_datetime_str = request.POST.get('return-datetime')
        road_type = request.POST.get('roadType')

        # Convert datetime strings to datetime objects
        pickup_datetime = datetime.strptime(pickup_datetime_str, '%Y-%m-%dT%H:%M')
        return_datetime = datetime.strptime(return_datetime_str, '%Y-%m-%dT%H:%M')

        # Format datetime objects into strings for storage in session
        pickup_datetime_formatted = pickup_datetime.strftime('%Y-%m-%dT%H:%M')
        return_datetime_formatted = return_datetime.strftime('%Y-%m-%dT%H:%M')

        # Store form data in session
        request.session['pickup_location'] = pickup_location
        request.session['dropoff_location'] = dropoff_location
        request.session['pickup_datetime'] = pickup_datetime_formatted
        request.session['return_datetime'] = return_datetime_formatted
        request.session['road_type'] = road_type

        return redirect('display_car')  # Redirect to the next page
    else:
        return render(request, 'index.html')


    
# views.py


def edit_booking_detail(request):
    if request.method == "POST":
        # Update session data with edited values
        request.session['pickup_location'] = request.POST.get('pickupLocation')
        request.session['dropoff_location'] = request.POST.get('dropOffLocation')
        request.session['pickup_datetime'] = request.POST.get('pickupDatetime')
        request.session['return_datetime'] = request.POST.get('returnDatetime')

        # Redirect to a success page or any other appropriate page
        return redirect('display_car')
    else:
        # Render the edit form page
        return render(request, 'DisplayCars.html')

def display_car(request):
    # Retrieve all vehicles from the database
    vehicles = Vehicle.objects.all()
    
        # Extract filter parameters from GET request
    transmission = request.GET.get('transmission')
    seats = request.GET.get('seats')
    car_type = request.GET.get('car_type')

    # Filter queryset based on parameters
    vehicles = Vehicle.objects.all()
    if transmission:
        vehicles = vehicles.filter(Transmission=transmission)
    if seats:
        vehicles = vehicles.filter(Seats=seats)
    if car_type:
        vehicles = vehicles.filter(Vehicle_Type=car_type)

    # Pass the vehicles to the template
    context = {'vehicles': vehicles}
    return render(request, 'DisplayCars.html', context)

def recommended_cars(request):
    if request.method == 'GET':
        road_type = request.GET.get('roadType')  # Assuming the name attribute of the select element in the form is 'roadType'

        # Filter vehicles based on the selected road type
        vehicles = Vehicle.objects.filter(road_type=road_type)

        # Filter recommended vehicles based on some criteria (replace this with your own logic)
        recommended_vehicles = vehicles.filter(is_recommended=True)

        # Pass the filtered vehicles to the template for rendering
        return render(request, 'DisplayCars.html', {'recommended_vehicles': recommended_vehicles, 'vehicles': vehicles})

    # Render the template with no vehicles if the request method is not GET
    return render(request, 'DisplayCars.html', {'recommended_vehicles': [], 'vehicles': []})



def View_car(request, vehicle_id):
    # Retrieve the vehicle object using the vehicle_id
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    # Pass the vehicle object to the template
    return render(request, "RentCar.html", {'vehicle': vehicle})


