from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Location, Vehicle

from datetime import datetime
import json
import uuid
import requests
from django.contrib import messages
def search_vehicles(request):
    if request.method == "POST":
        # Retrieve form data
        pickup_location = request.POST.get('pickupLocation')
        dropoff_location = request.POST.get('dropOffLocation')
        pickup_datetime_str = request.POST.get('pickup-datetime')
        return_datetime_str = request.POST.get('return-datetime')
        road_type = request.POST.get('roadType')
        print("Road type: " ,road_type)

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
    # Retrieve road type from session
    road_type = request.session.get('road_type')
    print("New Road Type: ", road_type)

    # If road type is provided, filter vehicles by road type
    if road_type:
        vehicles = Vehicle.objects.filter(Road_Type=road_type)
    else:
        # If road type is not provided, retrieve all vehicles
        vehicles = Vehicle.objects.all()

    # Retrieve additional filter parameters from GET request
    transmission = request.GET.get('transmission')
    seats = request.GET.get('seats')
    car_type = request.GET.get('car_type')

    all_vehicles = Vehicle.objects.all()
    # Filter queryset based on additional parameters
    if transmission:
        vehicles = all_vehicles.filter(Transmission=transmission)
    if seats:
        vehicles = all_vehicles.filter(Seats=seats)
    if car_type:
        vehicles = all_vehicles.filter(Vehicle_Type=car_type)

    # Pass the vehicles to the template
    context = {'vehicles': vehicles}
    return render(request, 'DisplayCars.html', context)



def View_car(request, vehicle_id):
    uuid_value = uuid.uuid4()
    # Retrieve the vehicle object using the vehicle_id
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    # Pass the vehicle object to the template
    return render(request, "RentCar.html", {'vehicle': vehicle, 'uuid_value':uuid_value})

# def return_url(request):
#     return render(request,'payment_success.html')

def initkhalti(request):
    url = "https://a.khalti.com/api/v2/epayment/initiate/"
    user = request.user


    return_url = request.POST.get('return_url')
    purchase_order_id = request.POST.get('purchase_order_id')
    amount = request.POST.get('amount')

    print(purchase_order_id)
    print(amount)
    print(return_url)


    payload = json.dumps({
        "return_url": return_url,
        "website_url": "http://127.0.0.1:8000/",
        "amount": amount,
        "purchase_order_id": purchase_order_id,
        "purchase_order_name": "Drop Car",
        "customer_info": {
        "name": user.full_name,
        "email": user.email,
        "phone": user.phone
        }
    })
    headers = {
        'Authorization': 'key a9eeea1fb39645d28254dce00beab257',
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

    new_response = json.loads(response.text)
    print(new_response)

    return redirect(new_response['payment_url'])


def return_url(request,vehicle_id):
    if request.method == 'GET':
        url = "https://a.khalti.com/api/v2/epayment/lookup/"
        headers = {
            'Authorization': 'key a9eeea1fb39645d28254dce00beab257',
            'Content-Type': 'application/json',
        }
        pidx = request.GET.get('pidx')
        data = json.dumps({
            'vehicle_id': vehicle_id,
            'pidx': pidx
        })
        print("Data", data)
        # Make a POST request to the Khalti API to verify payment
        res = requests.post(url, headers=headers, data=data)
        print(res.text)

        new_res = json.loads(res.text)
        print("new_res hai: ", new_res)

        # # Check if payment status is 'Completed'
        if new_res.get('status') == 'Completed':
            vehicle = Vehicle.objects.get(id=vehicle_id)
            vehicle.status = 'booked'
            vehicle.save()
            messages.success(request, 'Payment Successful!')

    # Pass vehicle_id to the template
    return render(request, 'index.html')
