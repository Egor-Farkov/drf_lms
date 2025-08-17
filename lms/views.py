from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, \
    ListAPIView
from rest_framework.response import Response

from lms.models import Courses, Lessons
from lms.serializers import CoursesSerializer, LessonsSerializer


# Create your views here.
class CoursesViewSet(viewsets.ViewSet):
    """
    Простой ViewSet-класс для вывода списка курсов и информации по одному объекту
    """

    def list(self, request):
        queryset = Courses.objects.all()
        serializer = CoursesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Courses.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CoursesSerializer(user)
        return Response(serializer.data)


class LessonsListAPIView(ListAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsRetrieveAPIView(RetrieveAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsCreateAPIView(CreateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsUpdateAPIView(UpdateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsDestroyAPIView(DestroyAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
