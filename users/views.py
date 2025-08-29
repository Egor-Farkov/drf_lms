from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from lms.models import Courses
from users.filters import PayFilter
from users.models import Pay, SubscribeCourse, User
from users.serializers import (PaySerializer, UserCreateSerializer,
                               UserDetailViewSerializer, UserViewSerializer)
from users.services import create_stripe_price_amount, create_stripe_session


class UserSubscribe(APIView):

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course_id")
        course_item = get_object_or_404(Courses, pk=course_id)

        subs_item = SubscribeCourse.objects.filter(
            user=user, course=course_item
        ).first()

        # Если подписка у пользователя на этот курс есть - удаляем ее
        if subs_item:
            subs_item.delete()

            message = "подписка удалена"
        # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            SubscribeCourse.objects.create(user=user, course=course_item)
            message = "подписка добавлена"
        # Возвращаем ответ в API
        return Response({"message": message})


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


# Create your views here.
class PayViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pay.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = PayFilter
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]

    serializer_class = PaySerializer


class CreateProductView(CreateAPIView):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()

    def perform_create(self, serializer):
        pay = serializer.save(user=self.request.user)
        name_product = pay.lesson or pay.course
        price = create_stripe_price_amount(name_product, pay.total_pay)
        session_id, link = create_stripe_session(price)
        pay.session_id = session_id
        pay.link = link
        pay.save()




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["email"]
    ordering = ["-email"]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailViewSerializer
        return UserViewSerializer
