from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.contrib.auth.hashers import make_password

admin_password = make_password("admin")
seed_password = make_password("seed")

users = [
    User(username="admin", password=admin_password, is_staff=True, is_superuser=True)
] + [User(username="seed" + str(i), password=seed_password) for i in range(1, 25)]


def run_seed_view(_request):
    User.objects.bulk_create(users, ignore_conflicts=True)

    return JsonResponse({"message": "Done"})
