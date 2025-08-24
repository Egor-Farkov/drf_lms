from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.models import Lessons
from lms.views import CoursesViewSet, LessonsViewSet

app_name = LmsConfig.name
router = DefaultRouter()
router.register(r'courses', CoursesViewSet, basename='courses')
router.register(r'lessons', LessonsViewSet, basename='lessons')
urlpatterns = router.urls