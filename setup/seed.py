from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http.response import JsonResponse

admin_password = make_password("admin")
users = [
    User(username="admin", password=admin_password, is_staff=True, is_superuser=True)
]


def run_seed_view(_request):
    User.objects.all().delete()
    User.objects.bulk_create(users)

    return JsonResponse({"message": "Done"})
