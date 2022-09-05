from django.urls import path
from apps.order import views

urlpatterns = [
    path('add/', views.add_to_cart, name='add_to_cart'),
]
