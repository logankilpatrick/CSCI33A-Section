from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index")
    # Path, which view to ender
]