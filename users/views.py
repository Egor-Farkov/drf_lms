from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.filters import PayFilter
from users.models import Pay, User
from users.serializers import PaySerializer, UserCreateSerializer, UserDetailViewSerializer, UserViewSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny, )

    def perform_create(self, serializer):
        user = serializer.save(is_active = True)
        user.set_password(user.password)
        user.save()


# Create your views here.
class PayViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pay.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = PayFilter
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    serializer_class = PaySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # filterset_class = PayFilter
    ordering_fields = ['email']
    ordering = ['-email']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailViewSerializer
        return UserViewSerializer


