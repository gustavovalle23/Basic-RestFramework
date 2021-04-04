from django.contrib import admin
from college.models import Student, Course, Registration


class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'document', 'birth_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20
    ordering = ['id']


admin.site.register(Student, Students)


class Courses(admin.ModelAdmin):
    list_display = ('id', 'id_course', 'description')
    list_display_links = ('id', 'id_course')
    search_fields = ('id_course',)
    list_per_page = 20
    ordering = ['id']


admin.site.register(Course, Courses)


class Registrations(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period')
    list_display_links = ('id',)
    list_per_page = 20
    ordering = ['id']


admin.site.register(Registration, Registrations)
