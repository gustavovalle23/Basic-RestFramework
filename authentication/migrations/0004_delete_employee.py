# Generated by Django 4.2 on 2023-05-01 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_employee_birthdate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
