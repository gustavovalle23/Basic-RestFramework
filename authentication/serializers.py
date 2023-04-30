from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User) -> RefreshToken:
        token: RefreshToken = super().get_token(user)
        token["username"] = user.username
        return token
