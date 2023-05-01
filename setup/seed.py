from django.http.response import JsonResponse
from django.contrib.auth.hashers import make_password
import datetime

from accounts.models import User

admin_password = make_password("admin")
seed_password = make_password("seed")

users = [
    User(
        username="admin",
        email="admin@email.com",
        birth_date=datetime.datetime(1999, 1, 1),
        password=admin_password,
        is_superuser=True,
        is_staff=True,
    )
] + [
    User(
        username=f"seed{str(i)}",
        email=f"seed{str(i)}@email.com",
        birth_date=datetime.datetime(1999, 1, 1),
        password=seed_password,
    )
    for i in range(1, 25)
]


def run_seed_view(_request):
    User.objects.bulk_create(users, ignore_conflicts=True)

    return JsonResponse({"message": "Done"})
