from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class AuthenticationTests(TestCase):
    def setUp(self) -> None:
        User.objects.create(username="admin", password="admin")
        self.client = APIClient()
        self.access_token = "access token"
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

    def test_should_return_unauthorized_without_credentials(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 401)

    def test_get_users_page_1(self):
        response = self.client.get("/users/?page=1", headers=self.headers)
        self.assertEqual(response.status_code, 200)
