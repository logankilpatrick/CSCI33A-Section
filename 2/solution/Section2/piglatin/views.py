from django.shortcuts import render
from . import forms
from . import regex

# Create your views here.
def index(request):

    # Create new text form and empty translation
    form = forms.TextForm()
    translation = None

    # If user has submitted form, render that form and translation
    if request.method == "POST":
        form = forms.TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["plain"]
            translation = regex.piglatinify(text)

    return render(request, "piglatin/index.html", {
        "form": form,
        "translation": translation
    })