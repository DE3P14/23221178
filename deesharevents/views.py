from django.shortcuts import render, redirect
from . models import deesharevents
from django.contrib import messages
from .forms import UserSignUpForm
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            un = form.cleaned_data.get('username')
            messages.success(request,
                'Account has been successfully created for {}!'.format(un))
            return redirect('login')

    
        elif request.method == "GET":
            form = UserSignUpForm()

        return render(request, 'signup.html', {'form': form})
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
@login_required
def booking(request):
    return render(request,'booking.html')
@login_required
def confirm(request):
    return render(request,'confirm.html')
@login_required
def payment(request):
    return render(request,'payment.html')

