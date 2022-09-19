from django.urls import path, include

urlpatterns = [
    path('user/', include('apps.api.user.urls')),
]
