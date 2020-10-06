from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('helloworld', views.helloworld, name="helloworld"),
    # Path, which view to ender
]