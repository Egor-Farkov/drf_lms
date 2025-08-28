from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import PayViewSet, UserCreateAPIView, UserViewSet, UserSubscribe
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'payments', PayViewSet)
router.register(r'', UserViewSet)

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('subscribe/', UserSubscribe.as_view(), name='subscribe'),
    path('login/', TokenObtainPairView.as_view(permission_classes = (AllowAny, )), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes = (AllowAny, )), name='token_refresh'),
]

urlpatterns += router.urls

