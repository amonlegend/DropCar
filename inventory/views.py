from django.http import JsonResponse
from django.shortcuts import render
from .models import Location, Vehicle


def search_vehicles(request):
    if request.method == 'POST':
        # Get form data
        pickup_location = request.POST.get('pickupLocation')
        drop_off_location = request.POST.get('dropOffLocation')
        pickup_datetime = request.POST.get('pickup-datetime')
        return_datetime = request.POST.get('return-datetime')
        road_type = request.POST.get('roadType')

        # Query the database based on form data
        vehicles = Vehicle.objects.filter(
            road_type=road_type
        )
        print(vehicles)

        # Render the data in a template or return it as a JSON response
        return render(request, 'DisplayCars.html', {'vehicles': vehicles})
    
    return render(request, 'index.html')
    
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
