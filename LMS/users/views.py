from rest_framework import generics
from rest_framework.filters import OrderingFilter
from users.serializers import UsersSerializer, PaymentsSerializer
from users.models import User, Payment
from django_filters.rest_framework import DjangoFilterBackend


class UsersListAPIView(generics.ListAPIView):
    serializer_class = UsersSerializer
    queryset = User.objects.all()


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payment.objects.all()
    
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course_or_lesson', 'payment_method')
    ordering_fields = ['payment_date']
    
