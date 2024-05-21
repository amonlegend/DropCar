from django.contrib import admin
from .models import Vehicle, Location, Booking
# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Location)
admin.site.register(Booking)

