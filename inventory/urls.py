# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("search_vehicles",views.search_vehicles, name="search_vehicles"),
    path("display_car",views.display_car, name="display_car"),
    path('View_car/<int:vehicle_id>/', views.View_car, name='View_car'), 
    path('edit_booking_detail',views.edit_booking_detail, name='edit_booking_detail'),
    
    
    path('initkhalti',views.initkhalti,name="initkhalti"),
    path('return_url/<int:vehicle_id>/', views.return_url, name='return_url')
    
]
