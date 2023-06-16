from rest_framework import serializers
from django.contrib.auth.models import User
from tastyapi.models import TastyUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class TastyUserSerializer(serializers.ModelSerializer):

    user = UserSerializer(serializers.ModelSerializer)

    class Meta:
        model = TastyUser
        fields = (
            "id",
            "bio",
            "profile_image_url",
            "created_on",
            "active",
            "user"
        )
