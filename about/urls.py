from django.urls import path 
from . import views

urlpatterns = [
    path("about/", views.AboutUs.as_view(), name="about"),
]