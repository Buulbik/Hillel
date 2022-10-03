from django.urls import path

from apps.main.views import PageView

urlpatterns = [
    path('<str:slug>/', PageView.as_view(), name='page'),
]
