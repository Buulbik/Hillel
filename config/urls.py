from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include("apps.blog.urls")),
    path('catalog/', include("apps.catalog.urls")),
    path('user/', include("apps.user.urls")),
    path('order/', include("apps.order.urls")),
    path('api/', include("apps.api.urls")),
    path('tinymce/', include('tinymce.urls')),
    path('', include('apps.main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
