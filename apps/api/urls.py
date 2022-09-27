from django.urls import path, include

urlpatterns = [
    path('user/', include('apps.api.user.urls')),
    path('catalog/', include('apps.api.catalog.urls')),
    path('blog/', include('apps.api.blog.urls')),
]
