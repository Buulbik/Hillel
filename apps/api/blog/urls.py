from rest_framework.routers import DefaultRouter

from apps.api.blog.views import ArticleViewSet

urlpatterns = [

]

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns += router.urls
