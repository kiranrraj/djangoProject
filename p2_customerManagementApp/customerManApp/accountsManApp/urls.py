from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products, name='products'),
    path('customer/', views.customer, name='customer'),
] 