from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet

app_name = 'users'

router = DefaultRouter()

router.register('users', CustomUserViewSet)

authpatterns = [
    path('auth/', include('djoser.urls.authtoken'))
]

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include(authpatterns)),
]
