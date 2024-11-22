# Generated by Django 5.1.2 on 2024-10-30 07:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselor_app', '0005_enrollstudents'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollStudentsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('mobile', models.CharField(max_length=15, unique=True)),
                ('location', models.CharField(choices=[('Nanakramguda-Hub', 'Nanakramguda-Hub'), ('Ameerpet', 'Ameerpet')], max_length=50)),
                ('mode_of_attending', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=20)),
                ('qualification', models.CharField(choices=[('inter', 'Intermediate'), ('diploma', 'Diploma'), ('degree', 'Degree'), ('btech', 'Bachelor Technology'), ('mtech', 'Master Technology')], max_length=150)),
                ('branch', models.CharField(max_length=150)),
                ('course_name', models.CharField(choices=[('python_full_stack', 'Python Full Stack'), ('java_full_stack', 'Java Full Stack'), ('data_science', 'Data Science'), ('digital_marketing', 'Digital Marketing'), ('ui_ux', 'UI / UX')], max_length=50)),
                ('course_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('education_status', models.CharField(choices=[('completed', 'Completed'), ('in_progress', 'In Progress')], max_length=20)),
                ('passed_year', models.CharField(blank=True, max_length=4, null=True)),
                ('marks', models.CharField(blank=True, max_length=10, null=True)),
                ('current_year', models.CharField(blank=True, max_length=10, null=True)),
                ('enrolled_on', models.DateTimeField(auto_now_add=True)),
                ('counselor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counselor_app.role')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counselor_app.manager')),
            ],
        ),
        migrations.DeleteModel(
            name='EnrollStudents',
        ),
    ]
