from django.urls import path

from auth.views import login

urlpatterns = [
    path('', view=login, name='login')
]