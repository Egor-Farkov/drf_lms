from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from users.filters import PayFilter
from users.models import Pay
from users.serializers import PaySerializer


# Create your views here.
class PayViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pay.objects.all()
    filter_backends = [DjangoFilterBackend,]
    filterset_class = PayFilter
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    serializer_class = PaySerializer