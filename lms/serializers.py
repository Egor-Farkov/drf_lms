from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from lms.models import Courses, Lessons


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ['id', 'name', 'picture', 'description', 'url_video', 'course']


class CoursesSerializer(serializers.ModelSerializer):
    lessons = LessonsSerializer(many=True, read_only=True)
    count_lessons = SerializerMethodField(read_only=True)


    def get_count_lessons(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Courses
        fields = ['name', 'picture', 'description', 'count_lessons', 'lessons']



