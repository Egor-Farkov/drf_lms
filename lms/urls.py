from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views import CoursesViewSet, LessonsListAPIView, LessonsRetrieveAPIView, LessonsCreateAPIView, \
    LessonsUpdateAPIView, LessonsDestroyAPIView


app_name = LmsConfig.name
# Описание маршрутизации для ViewSet
router = DefaultRouter()
router.register(r'', CoursesViewSet, basename='courses')
urlpatterns = [
    path('lessons/', LessonsListAPIView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonsRetrieveAPIView.as_view(), name='lesson-detail'),
    path('lessons/create/', LessonsCreateAPIView.as_view(), name='lesson-create'),
    path('lessons/update/<int:pk>/', LessonsUpdateAPIView.as_view(), name='lesson-update'),
    path('lessons/delete/<int:pk>/', LessonsDestroyAPIView.as_view(), name='lesson-delete'),
]
urlpatterns += router.urls