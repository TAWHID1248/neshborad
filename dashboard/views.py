# dashboard/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import *


from django.shortcuts import render

def homepage(request):
    return render(request, 'dashboard/homepage.html')
        

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'dashboard/register.html', {'form': form})

# dashboard/views.py
from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard/dashboard.html', {
        'sales_target': 50000,
        'revenue': 30000,
        'top_products': ['Product A', 'Product B'],
        'alerts': ['New order received!', 'Payment gateway updated.'],
    })


def payment_gateways(request):
    gateways = PaymentGateway.objects.all()
    return render(request, 'dashboard/payment_gateways.html', {'gateways': gateways})


def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'dashboard/order_history.html', {'orders': orders})


def sales_resources(request):
    resources = SalesResource.objects.all()
    return render(request, 'dashboard/sales_resources.html', {'resources': resources})

