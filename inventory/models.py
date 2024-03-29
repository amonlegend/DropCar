from django.db import models

# Create your models here.

class Vehicle(models.Model):
    name = models.CharField(max_length=200)
    vehicle_type = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    recommended_places = models.CharField(max_length=500, null= True)
    image = models.ImageField(upload_to='vehicle_images/')

    def __str__(self):
        return self.name