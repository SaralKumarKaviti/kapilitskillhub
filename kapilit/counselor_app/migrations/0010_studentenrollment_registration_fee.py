# Generated by Django 5.1.2 on 2024-11-04 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselor_app', '0009_paymentdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentenrollment',
            name='registration_fee',
            field=models.DecimalField(decimal_places=2, default=2000, max_digits=10),
        ),
    ]
