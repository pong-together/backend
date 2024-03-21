from rest_framework import serializers

from users.models import User


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'intra_id', 'image', 'language', 'game_status', 'chat_connection')
