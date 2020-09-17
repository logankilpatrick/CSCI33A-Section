from django.http import HttpResponse
from django.shortcuts import render

# Default function
def index(request):
    return(HttpResponse("Hello, World!"))
