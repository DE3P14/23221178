from django.shortcuts import render, redirect
from . models import deesharevents
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})
        # Create new user
        user = User.objects.create_user(username=username, password=password)
        auth_login(request, user)  # Log in the user
        return redirect('login')  # Redirect to home page after signup
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Log in the user
            return redirect('index')  # Redirect to home page after login
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def events(request):
    # Query all events from the database
    events = deesharevents.objects.all()
    # Pass events data to the template context
    return render(request, 'events.html', {'events': events})
def booking(request):
    return render(request,'booking.html')
def confirm(request):
    return render(request,'confirm.html')
def payment(request):
    return render(request,'payment.html')

