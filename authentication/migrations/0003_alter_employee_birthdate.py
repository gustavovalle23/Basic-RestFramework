# Generated by Django 4.2 on 2023-05-01 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_employee_birthdate_employee_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='birthDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]