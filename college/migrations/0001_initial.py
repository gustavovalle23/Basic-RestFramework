# Generated by Django 3.1.7 on 2021-04-04 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_2', models.IntegerField()),
                ('id_course', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('level', models.CharField(choices=[('B', 'Basic'), ('I', 'Intermediary'), ('A', 'Advanced')], default='B', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('document', models.CharField(max_length=9)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('M', 'Morning'), ('E', 'Evening'), ('N', 'Nightly')], default='M', max_length=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.student')),
            ],
        ),
    ]