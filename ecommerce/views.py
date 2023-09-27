from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import UserRegistrationForm, UserLoginForm, CheckoutForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Product Views
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

# User Registration and Login Views
def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Process registration logic (e.g., create user)
            # Redirect to a success page or login page
            return redirect('login')  # Assuming 'login' is the URL name for user login
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # Process login logic (e.g., authenticate user)
            # Redirect to a user dashboard or another page
            return redirect('dashboard')  # Replace 'dashboard' with the desired URL name
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

# Checkout View
def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Process checkout logic (e.g., create an order)
            # Redirect to a confirmation page or payment gateway
            return redirect('order_confirmation')  # Replace 'order_confirmation' with the desired URL name
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form})

# Register View (Separated from User Registration)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
