# Generated by Django 4.0.2 on 2022-03-22 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_remove_employee_employee_service_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_employee',
            field=models.ManyToManyField(to='polls.Employee'),
        ),
    ]
