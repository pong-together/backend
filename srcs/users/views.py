from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from auth.utils import get_user
from users.models import User
from users.serializers import UserInfoSerializer


# Create your views here.
class UserInfoAPIView(APIView):
    def get(self, request):
        user = get_user(request)
        if not isinstance(user, User):
            return user
        serializer = UserInfoSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
