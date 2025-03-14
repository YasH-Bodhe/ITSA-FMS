from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Registration
from .forms import AdminLoginForm
from .forms import EventForm, UserRegistrationForm, UserEventRegistrationForm
from django.http import JsonResponse
from django.contrib.auth.models import User

import qrcode
import io
import base64
import random
import string

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/login/')  # Redirect to a login page or home
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST) # AuthenticationForm is imported from a library
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page or dashboard after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def adminlogin_view(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            # Check if the user exists and is a superuser
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard')  # Adjust this to your admin home URL
            else:
                messages.error(request, "Invalid admin credentials.")
    else:
        form = AdminLoginForm()

    return render(request, 'adminlogin.html', {'form': form})

def index(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    user = request.user  # Get the currently logged-in user
    return render(request, 'profile.html', {'user': user})

@login_required
def home(request):
    sports_events = Event.objects.filter(category='Sports')
    cultural_events = Event.objects.filter(category='Cultural')
    gaming_events = Event.objects.filter(category='Gaming')
    technical_events = Event.objects.filter(category='Technical')
    non_technical_events = Event.objects.filter(category='Non Technical')
    
    return render(request, 'home.html', {
        'sports_events': sports_events,
        'cultural_events': cultural_events,
        'gaming_events': gaming_events,
        'technical_events': technical_events,
        'non_technical_events': non_technical_events
    })

@login_required
def admin_dashboard(request):
    events = Event.objects.all()  # Fetch all events
    total_registrations = Registration.objects.count()  # Count total registrations

    if request.method == 'POST':
        if 'delete_event' in request.POST:  # Handle delete event request
            event_id = request.POST.get('delete_event')
            event_to_delete = Event.objects.get(id=event_id)
            event_to_delete.delete()
            return redirect('admin_dashboard')

        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = EventForm()

    return render(request, 'admin_dashboard.html', {
        'form': form,
        'events': events,
        'total_registrations': total_registrations,
    })

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('admin_dashboard')

@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = UserEventRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)  # Don't save to the database yet
            registration.event = event  # Associate the registration with the event
            registration.user = request.user  # Automatically set the logged-in user
            registration.save()  # Save the registration to the database
            return redirect('home')  # Redirect to a success page or another view
    else:
        form = UserEventRegistrationForm()

    return render(request, 'event_reg.html', {'form': form, 'event': event})

@login_required
def event_registrations(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    registrations = Registration.objects.filter(event=event)
    data = {
        "registrations": [
            {"name": reg.name, "email": reg.email, "phone": reg.phone} for reg in registrations
        ]
    }
    return JsonResponse(data)

def manage_registrations(request):
    # Ensure the user is authenticated before accessing their registrations
    if request.user.is_authenticated:
        # Filter registrations based on the logged-in user
        user_registrations = Registration.objects.filter(user=request.user)
    else:
        user_registrations = []  # No registrations if the user is not authenticated

    return render(request, 'manage_reg.html', {'registrations': user_registrations})


def delete_registration(request, registration_id):
    registration = get_object_or_404(Registration, id=registration_id, user=request.user)
    registration.delete()
    return redirect('manage_registrations')  # Redirect to manage page


# This code if for QR Code genration

def generate_random_data(length=20):
    """Generate a random string to use as QR code data"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def generate_qr_code(data):
    """Generate a QR code from the given data and return as base64 string"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert the image to a base64 string
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    return img_str

# Assuming this is your existing view function - modify as needed for your application
def manage_registrations(request):
    # Get all registrations for the current user
    registrations = Registration.objects.filter(user=request.user)
    
    # Generate a random QR code for each registration
    for registration in registrations:
        # Generate a unique data string for the QR code
        qr_data = f"Event: {registration.event.name}\nName: {registration.name}\nEmail: {registration.email}\nID: {generate_random_data()}"
        
        # Generate the QR code as a base64 string
        registration.qr_code = generate_qr_code(qr_data)
    
    return render(request, 'manage_reg.html', {'registrations': registrations})