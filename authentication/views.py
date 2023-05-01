from django.contrib.auth.models import Group
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.serializers import GroupSerializer, TokenSerializer, UserSerializer
from accounts.models import User


class TokenView(TokenObtainPairView):
    serializer_class = TokenSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = {
            "GET": [permissions.IsAuthenticated],
            "POST": [permissions.IsAdminUser],
            "PUT": [permissions.IsAdminUser],
            "PATCH": [permissions.IsAdminUser],
            "DELETE": [permissions.IsAdminUser],
        }

        return [
            permission()
            for permission in permission_classes.get(
                self.request.method, [permissions.IsAdminUser]
            )
        ]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
