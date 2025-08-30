from rest_framework.test import APITestCase

from lms.models import Courses, Lessons
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="1@1.com")
        self.course = Courses.objects.create(name="тестовый курс", owner=self.user)
        self.lesson = Lessons.objects.create(
            name="тестовый урок", course=self.course, owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    BASE_URL = "http://127.0.0.1:8000"

    def test_user_subscribe(self):
        response = self.client.post(
            f"{self.BASE_URL}/users/subscribe/", data={"course_id": self.course.id}
        )

        assert response.json() == {"message": "подписка добавлена"}

        response = self.client.post(
            f"{self.BASE_URL}/users/subscribe/", data={"course_id": self.course.id}
        )

        assert response.json() == {"message": "подписка удалена"}

    def test_list_lesson(self):
        response = self.client.get(
            f"{self.BASE_URL}/lms/lessons/", content_type="application/json"
        )

        assert response.json() == {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 4,
                    "name": "тестовый урок",
                    "picture": None,
                    "description": None,
                    "url_video": None,
                    "course": 3,
                }
            ],
        }

    def test_create_lesson(self):
        data = {
            "name": "in_valid",
            "url_video": "123.ru",
            "course": self.course.id,
            "owner": self.user,
        }
        response = self.client.post(f"{self.BASE_URL}/lms/lessons/", data=data)

        assert response.json() == {"url_video": ["не содержит youtube.com"]}

        data["url_video"] = "youtube.com"
        response = self.client.post(f"{self.BASE_URL}/lms/lessons/", data=data)

        assert response.json() == {
            "id": 2,
            "name": "in_valid",
            "picture": None,
            "description": None,
            "url_video": "youtube.com",
            "course": 1,
        }

    def test_update_lesson(self):
        data = {
            "name": "update_valid",
            "url_video": "youtube.com",
            "course": self.course.id,
            "owner": self.user,
        }
        response = self.client.put(
            f"{self.BASE_URL}/lms/lessons/{self.lesson.id}/", data=data
        )

        assert response.json() == {
            "id": 5,
            "name": "update_valid",
            "picture": None,
            "description": None,
            "url_video": "youtube.com",
            "course": 4,
        }

    def test_delete_lesson(self):
        self.client.delete(f"{self.BASE_URL}/lms/lessons/{self.lesson.id}/")
        response = self.client.get(
            f"{self.BASE_URL}/lms/lessons/", content_type="application/json"
        )

        assert response.json() == {
            "count": 0,
            "next": None,
            "previous": None,
            "results": [],
        }
