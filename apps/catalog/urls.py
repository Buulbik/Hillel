from django.urls import path
from apps.catalog import views

urlpatterns = [
    path('', views.CatalogIndexView.as_view(), name='catalog'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product'),
    path('<str:slug>/', views.ProductByCategoryView.as_view(), name='category'),
]
