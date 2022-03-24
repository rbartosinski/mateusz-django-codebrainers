import datetime
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

class Service(models.Model):

    service_text = models.CharField(max_length=50)
    service_price = models.IntegerField()
    service_time = models.DurationField()
    service_description = models.CharField(max_length=100)

    def __str__(self):
        return self.service_text

class Employee(models.Model):
    employee_name = models.CharField(max_length=50)
    employee_service = models.ManyToManyField(Service)

    def __str__(self):
        return self.employee_name

class Appointment(models.Model):
    appointment_name = models.CharField(max_length=50)
    appointment_surname = models.CharField(max_length=50)
    appointment_email = models.EmailField(max_length=50)
    appointment_date = models.DateTimeField()
    appointment_service = models.ForeignKey(Service,  on_delete=models.CASCADE)
    appointment_employee = models.OneToOneField(Employee, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)
