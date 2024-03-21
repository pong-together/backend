from django.urls import path

from users.views import UserInfoAPIView

urlpatterns = [
    path('', UserInfoAPIView.as_view()),
]