# Generated by Django 4.0.2 on 2022-03-17 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_service',
        ),
    ]
