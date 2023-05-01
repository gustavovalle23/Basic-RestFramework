import datetime
from typing import Dict
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import User


def get_tokens_for_user(user: User) -> Dict[str, str]:
    refresh: RefreshToken = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class AuthenticationTests(TestCase):
    def setUp(self) -> None:
        user = User.objects.create(
            email="admin@email.com",
            birth_date=datetime.datetime(1999, 1, 1),
            username="admin",
            password="admin",
        )

        access_token = get_tokens_for_user(user).get("access")

        self.client = APIClient()
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

    def test_should_return_unauthorized_without_credentials(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 401)

    def test_get_users_page_1(self):
        response = self.client.get("/users/", headers=self.headers)
        self.assertEqual(response.status_code, 200)
