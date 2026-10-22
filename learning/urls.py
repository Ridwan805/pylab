from django.urls import path 
from . import views  

urlpatterns = [
    path("", views.home, name = 'home') ## path() definse the URL pattern, view.home refers to our home function, name="home" gives the URL a reusable name.
]