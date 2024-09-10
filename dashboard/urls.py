from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Homepage view for the root URL
    path('dashboard/', views.dashboard, name='dashboard'),
    path('payment-gateways/', views.payment_gateways, name='payment_gateways'),
    path('order-history/', views.order_history, name='order_history'),  # User order history
    path('sales-resources/', views.sales_resources, name='sales_resources'),  # Sales and marketing resources
    path('register/', views.register, name='register'),  # User registration
]
