from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from cc.models import *  # Import the missing models

# Create your views here.

def index(request):
    return render(request, 'fpage/index.html')  # Ensure this view renders the correct template

@csrf_protect
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                request.session['username'] = username
                return HttpResponseRedirect(reverse('home'))  # Updated namespace
            else:
                return render(request, 'fpage/login.html', {
                    "error_message": "Your account is disabled.",
                })
        else:
            return render(request, 'fpage/login.html', {
                "error_message": "Invalid login details. Please check your username and password.",
            })
    else:
        return render(request, 'fpage/login.html')

@csrf_protect
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        
        if User.objects.filter(username=username).exists():
            return render(request, 'fpage/signup.html', {
                "error": "Username already exists",
                "username": username,
                "email": email,
            })
        
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        
        # Automatically log in the user after signup
        auth_login(request, user)
        request.session['username'] = username  # Add session
        return HttpResponseRedirect(reverse('cc:index'))  # Updated namespace
    return render(request, 'fpage/signup.html')

def logout(request):
    # Clear the session data
    request.session.flush()
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))  # Updated namespace

def about(request):
    username = request.session.get('username', None)
    return render(request, 'fpage/about.html', {
        "username": username,
    })

def contact(request):    
    username = request.session.get('username', None)
    return render(request, 'fpage/contact.html', {
        "username": username,
    })

def services(request):
    if request.user.is_authenticated:
        return render(request, 'spage/services.html', {
            "username": request.user.username,
            'Schedule': Schedule.objects.all(),
            'Roster': Roster.objects.all(),
        })
    else:
        return HttpResponseRedirect(reverse('user_login'))

def home(request):
    username = request.session.get('username', None)
    return render(request, 'spage/home.html', {
        "username": username,
        'Announcement': Announcement.objects.all(),  # Ensure this model is imported correctly
    })

from cc.models import Event, Biblestudy, Youth, Outreach  # Use the correct model names

def events(request):
    return render(request, 'spage/events.html', {
        'event': Event.objects.all(),  # Correct model usage
        'biblestudy': Biblestudy.objects.all(),  # Correct model usage
        'youth': Youth.objects.all(),  # Correct model usage
        'ouchreach': Outreach.objects.all(),  # Correct model usage
    })
    

def facebook(request):
    return render(request, 'https://www.facebook.com/share/1B3neCpxC9/')

def twitter(request):
    return render(request, 'https://twitter.com/yourpage')

def instagram(request):
    return render(request, 'https://www.instagram.com/yourpage')

def donations(request):
    username = request.session.get('username', None)
    return render(request, 'spage/donations.html', {
        "username": username,
    })

def contacts(request):
    return render(request, 'spage/contact.html')

@csrf_protect
def process_donation(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        amount = request.POST['amount']
        # Process the donation (e.g., save to database, send email, etc.)
        return HttpResponseRedirect(reverse('donations'))
    return HttpResponse("Invalid request method.")

def policies(request):
    return render(request, 'fpage/policies.html')

def terms(request):
    return render(request, 'fpage/terms.html')

def adindex(request):
    return render(request, 'fpage/adindex.html')  # Corrected template path
