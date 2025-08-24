from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters


from lms.models import Courses, Lessons
from lms.serializers import CoursesSerializer, LessonsSerializer
from users.permissions import ModeratorPermissionsAll, IsOwner


# Create your views here.
class CoursesViewSet(viewsets.ModelViewSet):
    """Контролер отображения фильтрации и сортировки"""

    queryset = Courses.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["name"]
    ordering = ["-name"]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CoursesSerializer


    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~ModeratorPermissionsAll,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (ModeratorPermissionsAll | IsOwner)
        elif self.action == 'destroy':
            self.permission_classes = (~ModeratorPermissionsAll, IsOwner)
        return super().get_permissions()

class LessonsViewSet(viewsets.ModelViewSet):
    """Контролер отображения фильтрации и сортировки"""

    queryset = Lessons.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["name"]
    ordering = ["-name"]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return LessonsSerializer


    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~ModeratorPermissionsAll,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (ModeratorPermissionsAll | IsOwner)
        elif self.action == 'destroy':
            self.permission_classes = (~ModeratorPermissionsAll, IsOwner)
        return super().get_permissions()