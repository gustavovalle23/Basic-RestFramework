from django.urls import include, path
from rest_framework import routers

from authentication import views

router = routers.DefaultRouter()
router.register('api/users', views.UserViewSet)
router.register('api/groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
