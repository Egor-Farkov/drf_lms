from rest_framework import serializers

from users.models import Pay, User


class UserDetailViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "last_name", "first_name"]


class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "last_name", "first_name"]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]


class PaySerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source="user.email", read_only=True)
    course_name = serializers.CharField(
        source="course.name", read_only=True, allow_null=True
    )
    lesson_name = serializers.CharField(
        source="lesson.name", read_only=True, allow_null=True
    )

    class Meta:
        model = Pay
        fields = [
            "id",
            "user_email",
            "course_name",
            "lesson_name",
            "created_at",
            "total_pay",
            "choose_pay",
            "session_id",
            "link",
        ]
