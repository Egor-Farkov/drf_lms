from rest_framework import serializers

from lms.models import Courses, Lessons


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'
