# Generated by Django 4.0.2 on 2022-03-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_question_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50)),
                ('service_price', models.IntegerField()),
                ('service_time', models.DurationField()),
                ('service_description', models.CharField(max_length=100)),
                ('employee_choice', models.CharField(choices=[('Kasia', 'Kasia'), ('Asia', 'Asia')], default='Kasia', max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
