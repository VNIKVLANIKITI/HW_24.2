from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter
from django.urls import path
from users.views import UsersListAPIView, PaymentsListAPIView

app_name = UsersConfig.name

router = DefaultRouter()
#router.register(r'users', UsersListAPIView, basename='users')

urlpatterns = [
    path("users/", UsersListAPIView.as_view(), name="users-list"),
    path("payments/", PaymentsListAPIView.as_view(), name="payments-list"),
    
]#+router.urls
