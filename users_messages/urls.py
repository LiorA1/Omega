from rest_framework.routers import DefaultRouter
from django.urls import path, include
from users_messages import views

router = DefaultRouter()

router.register(r"users_messages", views.MessagesViewSet)

app_name = "users_messages"
urlpatterns = [
    path("", include(router.urls)),
]
