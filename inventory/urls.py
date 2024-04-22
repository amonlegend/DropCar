# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("search_vehicles",views.search_vehicles, name="search_vehicles"),
    path("display_car",views.display_car, name="display_car"),
    path("recommended_cars",views.recommended_cars, name="recommended_cars"),
    path('View_car/<int:vehicle_id>/', views.View_car, name='View_car'), 
    path('edit_booking_detail',views.edit_booking_detail, name='edit_booking_detail'),
    
]
