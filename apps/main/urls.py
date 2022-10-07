from django.urls import path

from apps.main.views import home
from apps.main.views import PageView

urlpatterns = [
    path('', home, name='home'),
    path('<str:slug>/', PageView.as_view(), name='page'),
]
