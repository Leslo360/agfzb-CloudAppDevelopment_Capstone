from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create an `about` view to render a static about page
def about_view(request):
    # Logic or data processing here
    # ...

    # Render the template
    return render(request, 'djangoapp/about.html')

# Create a `contact` view to return a static contact page
def contact_view(request):
    # Logic or data processing here
    # ...

    # Render the template
    return render(request, 'djangoapp/contact.html')


# Create a `login_request` view to handle sign in request
def login_view(request):
    # Logic or data processing here
    # ...

    # Render the template
    return render(request, 'djangoapp/login.html')


# Create a `logout_request` view to handle sign out request
def logout_request_view(request):
    # Logic or data processing here
    # ...

    # Render the template
    return render(request, 'logout_request.html')


# Create a `registration_request` view to handle sign up request
def registration_request_view(request):
    # Logic or data processing here
    # ...

    # Render the template
    return render(request, 'djangoapp/registration_request.html')


# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

