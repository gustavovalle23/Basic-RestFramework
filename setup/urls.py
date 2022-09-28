from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

from authentication.views import TokenView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls'), name='auth'),
    path('api/user/authenticate', TokenView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
]
