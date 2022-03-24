# Generated by Django 4.0.2 on 2022-03-17 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_name', models.CharField(max_length=50)),
                ('appointment_surname', models.CharField(max_length=50)),
                ('appointment_email', models.EmailField(max_length=50)),
                ('appointment_date', models.DateTimeField()),
                ('appointment_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.service')),
            ],
        ),
    ]
