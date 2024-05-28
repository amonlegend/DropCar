from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Location, Vehicle, Booking
from django.core.mail import send_mail
from datetime import datetime
import json
import uuid
import requests
from django.contrib import messages
from django.utils import timezone

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



# def View_car(request, vehicle_id):
#     uuid_value = uuid.uuid4()
#     # Retrieve the vehicle object using the vehicle_id
#     vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
#     # Pass the vehicle object to the template
#     return render(request, "RentCar.html", {'vehicle': vehicle, 'uuid_value':uuid_value})
def View_car(request, vehicle_id):
    uuid_value = uuid.uuid4()
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    is_logged_in = request.user.is_authenticated
    return render(request, "RentCar.html", {'vehicle': vehicle, 'uuid_value': uuid_value, 'is_logged_in': is_logged_in})


# def return_url(request):
#     return render(request,'payment_success.html')
def initkhalti(request):
    url = "https://a.khalti.com/api/v2/epayment/initiate/"
    user = request.user

    return_url = request.POST.get('return_url')
    purchase_order_id = str(uuid.uuid4())  # Generate a unique order ID
    amount = request.POST.get('amount')

    # Create a booking instance
    vehicle_name = request.POST.get('vehicle_name')
    print("the vehicle name is " + vehicle_name)
    location = request.POST.get('location')
    pickup_date = request.POST.get('pickup_date')
    drop_off_date = request.POST.get('drop_off_date')
    cost = request.POST.get('cost')
    print("the cost is " + cost)
    vehicle = Vehicle.objects.get(name=vehicle_name)
    booking = Booking.objects.create(
        vehicle=vehicle,
        location=location,
        pickup_date=pickup_date,
        drop_off_date=drop_off_date,
        cost = cost,
        status='pending',
        user=user
    )

    payload = json.dumps({
        "return_url": return_url,
        "website_url": "http://127.0.0.1:8000/",
        "amount": amount,
        "purchase_order_id": purchase_order_id,
        "purchase_order_name": "Drop Car",
        "customer_info": {
            "name": user.full_name,
            "email": user.email,
            "phone": user.phone  # Assuming phone is a field in a user profile model
        }
    })
    headers = {
        'Authorization': 'key a9eeea1fb39645d28254dce00beab257',
        'Content-Type': 'application/json',
    }

    response = requests.post(url, headers=headers, data=payload)
    new_response = json.loads(response.text)

    # Update the booking with the purchase_order_id
    booking.purchase_order_id = purchase_order_id
    booking.save()

    return redirect(new_response['payment_url'])

def return_url(request, vehicle_id):
    if request.method == 'GET':
        url = "https://a.khalti.com/api/v2/epayment/lookup/"
        headers = {
            'Authorization': 'key a9eeea1fb39645d28254dce00beab257',
            'Content-Type': 'application/json',
        }
        pidx = request.GET.get('pidx')
        data = json.dumps({
            'pidx': pidx
        })

        res = requests.post(url, headers=headers, data=data)
        new_res = json.loads(res.text)

        # Print the entire response for debugging
        print("Response from Khalti API:", new_res)

        # Check if payment status is 'Completed'
        if new_res.get('status') == 'Completed':
            vehicle = Vehicle.objects.get(id=vehicle_id)
            vehicle.status = 'Booked'
            vehicle.save()

                # Check and print all keys in new_res for debugging
            print("Keys in response:", new_res.keys())

                # purchase_order_id = new_res.get('transaction_id')
                # if purchase_order_id is None:
                #     # Handle missing purchase_order_id
                #     print("Missing purchase_order_ id:")
                #     messages.error(request, 'Purchase order ID not found in response.')
                #     return render(request, 'index.html')

            booking = Booking.objects.get(vehicle = vehicle)
            booking.status = 'booked'
            # vehicle = Booking.vehicles.get(booking = vehicle)
            # vehicle.status = "Booked"
            # vehicle.save()
            booking.save()
            # mail
            # Send confirmation email
            # Constructing the email message
            email_subject = 'Booking Confirmation - DropCar'
            email_body = f'Dear {booking.user.full_name},\n\n' \
                        'We are pleased to inform you that your booking has been approved.\n\n' \
                        'Your booking details are as follows:\n\n' \
                        f'- Vehicle: {booking.vehicle.name}\n' \
                        f'- Vehicle Number: {booking.vehicle.vehicle_number}\n' \
                        f'- Pick Up Location: {booking.location}\n' \
                        f'- Pick Up Date: {booking.pickup_date}\n' \
                        f'- Drop Off Date: {booking.drop_off_date}\n' \
                        f'- Cost: {booking.cost}\n\n' \
                        'Please visit the specified branch location to pick your vehicle.\n\n' \
                        'Thank you for choosing DropCar!'

            # Sending the email
            send_mail(
                email_subject,
                email_body,
                'info.DropCar@gmail.com',  # Sender's email
                [booking.user.email],  # Recipient's email
                fail_silently=False,
            )
            messages.success(request, 'Payment successful! Your booking has been confirmed.')
        else:
            messages.error(request, 'Payment Failed!')

    return render(request, 'index.html')

def my_booking(request):
    user = request.user
    current_time = timezone.now()
    
    # Fetch all bookings for the current user
    bookings = Booking.objects.filter(user=user)
    
    # Separate bookings by status
    booked = bookings.filter(status="booked")
    cancelled_bookings = bookings.filter(status="cancelled")
    running_bookings = bookings.filter(pickup_date__lte=current_time, drop_off_date__gte=current_time)
    completed_bookings = bookings.filter(drop_off_date__lt=current_time)

    return render(request, 'myBooking.html', {
        'running_bookings': running_bookings,
        'completed_bookings': completed_bookings,
        'cancelled_bookings': cancelled_bookings,
        'bookings': bookings,
        'booked': booked,
    })
def cancel_booking(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        try:
            booking = Booking.objects.get(id=booking_id)
            booking.status = 'cancelled'
            booking.save()
        except Booking.DoesNotExist:
            # Handle case where booking does not exist
            pass
    return redirect('my_booking')
