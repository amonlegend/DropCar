# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("search_vehicles",views.search_vehicles, name="search_vehicles"),
    path("display_car",views.display_car, name="display_car"),
]
