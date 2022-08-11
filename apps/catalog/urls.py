from django.urls import path
from apps.catalog import views

urlpatterns = [
    path('', views.CatalogIndexView.as_view(), name='catalog'),
    path('<str:slug>', views.CatalogIndexView.as_view(), name='category'),
]
