from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    document = models.CharField(max_length=9)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL = (
        ('B', 'Basic'),
        ('I', 'Intermediary'),
        ('A', 'Advanced')
    )
    id_2 = models.IntegerField()
    id_course = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(max_length=1,
                             choices=LEVEL,
                             blank=False,
                             null=False,
                             default='B')

    def __str__(self):
        return self.description


class Registration(models.Model):
    PERIOD = (
        ('M', 'Morning'),
        ('E', 'Evening'),
        ('N', 'Nightly')
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(max_length=1,
                              choices=PERIOD,
                              blank=False,
                              null=False,
                              default='M')

    def __str__(self):
        return f'{self.student} - {self.course}'
