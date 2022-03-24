from django import forms
from .models import Appointment, Service, Employee

class AppointmentForm(forms.Form):
    appointment_name = forms.CharField(label="Name")
    appointment_surname = forms.CharField(label="Surname")
    appointment_email = forms.EmailField(label="email")
    appointment_date = forms.DateTimeField(label="Date", widget=forms.SelectDateWidget)
    appointment_employee =forms.ModelChoiceField(queryset=Employee.objects.all())


class AppointmentEntryForm(forms.Form):
    appointment_service = forms.ModelChoiceField(queryset=Service.objects.all())
