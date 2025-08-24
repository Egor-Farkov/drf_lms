from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import PayViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'payments', PayViewSet)

urlpatterns = router.urls