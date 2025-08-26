from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

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
    serializer_class = CoursesSerializer


    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (IsAuthenticated, ~ModeratorPermissionsAll,)
        elif self.action in ['update', 'partial_update', 'retrieve']:
            self.permission_classes = (IsAuthenticated, ModeratorPermissionsAll | IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (IsAuthenticated, IsOwner,)
        return super().get_permissions()

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.groups.filter(name='moders').exists():
            return qs

        return qs.filter(owner=user)


class LessonsViewSet(viewsets.ModelViewSet):
    """Контролер отображения фильтрации и сортировки"""

    queryset = Lessons.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["name"]
    ordering = ["-name"]
    serializer_class = LessonsSerializer



    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (IsAuthenticated, ~ModeratorPermissionsAll,)
        elif self.action in ['update', 'partial_update', 'retrieve']:
            self.permission_classes = (IsAuthenticated, ModeratorPermissionsAll | IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (IsAuthenticated, IsOwner,)
        return super().get_permissions()

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.groups.filter(name='moders').exists():
            return qs

        return qs.filter(owner=user)