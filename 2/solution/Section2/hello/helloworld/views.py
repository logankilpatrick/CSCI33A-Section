from django.http import HttpResponse
from django.shortcuts import render

# Default function
def index(request):
    return render(request, "app_name/file_name.html", {
        “var_name_1”: value1,
        “var_name_2”: value2
    })


def helloworld(request):
    return render(request, "app_name/file_name.html", {
        “var_name_1”: value1,
        “var_name_2”: value2
    })
