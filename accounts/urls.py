from django.urls import path, include
from rest_framework import routers

from .views import RegisterView, AddressViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

router = routers.DefaultRouter()
router.register('addresses', AddressViewSet, basename='address')


urlpatterns = [
    path('signup/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', include(router.urls)),
]