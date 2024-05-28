from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.location

class Vehicle(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='vehicle_images/')
    vehicle_number = models.CharField(max_length=100)
    Transmission_choices = {
        'automatic': "Automatic",
        'manual': "Manual"
    }
    Transmission = models.CharField(max_length=100, choices=Transmission_choices, default='automatic')
    Seats_choices = {
        '4/5': "4/5",
        '6/10': "6/10"
    }
    Seats = models.CharField(max_length=100, choices=Seats_choices, default="4/5")
    Vahicle_type_choices = {
        'hatchback': "Hatchback",
        'sedan': "Sedan",
        'suv': "SUV",
        'muv': "MUV",
        'minivan': "Mini Van"
    }
    Vehicle_Type = models.CharField(max_length=100, choices=Vahicle_type_choices, default="hatchback")
    ROAD_TYPE_CHOICES = {
        'Highway' : 'Highway',
        'Rural' : 'Rural',
        'Street' : 'Street',
        'Off-road' : 'Off-road'

    }
    Road_Type = models.CharField(max_length=100, choices=ROAD_TYPE_CHOICES, default="Highway")
    model_year = models.IntegerField()
    Status_choices = [
        ('Available','Available'),
        ('Booked','Booked'),
    ]
    status = models.CharField(max_length=100,choices=Status_choices,default="Available")
    
    def __str__(self):
        return self.name + "    -   " + str(self.model_year) + "    -   " + str(self.vehicle_number) 

class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('booked', 'Booked'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    )

    vehicle = models.ForeignKey(Vehicle, blank=True, null=True, default=None, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    pickup_date = models.DateTimeField()
    drop_off_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cost = models.IntegerField()
    purchase_order_id = models.CharField(max_length=100, unique=True, null=True, blank=True)  

    def __str__(self):
        return f"{self.vehicle} - {self.user.full_name}"

    def save(self, *args, **kwargs):
        if self.status == 'booked' and self.vehicle:
            self.vehicle.status = 'booked'
            self.vehicle.save()
        super().save(*args, **kwargs)