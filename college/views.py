from rest_framework import viewsets, generics
from college.models import Student, Course, Registration
from .serializer import StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegistrationStudentsSerializer, ListRegistrationStudentsSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentsViewSet(viewsets.ModelViewSet):
    """ Showing all students """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CoursesViewSet(viewsets.ModelViewSet):
    """ Showing all courses """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class RegistrationViewSet(viewsets.ModelViewSet):
    """ Showing all registrations """
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListStudentRegistrations(generics.ListAPIView):
    """ Showing registration's students """

    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationStudentsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListRegistrationsStudents(generics.ListAPIView):
    """Showng students registrations in a course """

    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationStudentsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
