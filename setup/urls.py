from django.contrib import admin
from django.urls import path, include
from college.views import *
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views


router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('courses', CoursesViewSet, basename='Courses')
router.register('registrations', RegistrationViewSet, basename='Registrations')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('student/<int:pk>/registrations/', ListStudentRegistrations.as_view()),
    path('course/<int:pk>/registrations/', ListRegistrationsStudents.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
