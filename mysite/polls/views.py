from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, Group
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.utils.datastructures import MultiValueDictKeyError
from django.views import generic, View

from .forms import AppointmentForm, AppointmentEntryForm
from .models import Service, Appointment, Employee


class IndexView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'polls/index.html')


class ServicesView(View):
    def get(self, request):
        servicesList = Service.objects.all()
        context = {
            'servicesList': servicesList
        }
        return render(request, 'polls/services.html', context)


class DetailView(View):
    def get(self, request, pk):
        service = Service.objects.get(pk=pk)
        context = {
            'service': service,
        }
        return render(request, 'polls/detail.html', context)


class StaffView(View):
    def get(self, request):
        employees = User.objects.all()
        context = {
            'employees': employees
        }
        return render(request, 'polls/staff.html', context)


class StaffDetailView(View):
    def get(self, request, pk):
        staff = User.objects.get(pk=pk)
        id = User.pk
        context = {
            'staff': staff,
        }
        return render(request, 'polls/staffdetail.html', context)


class Book2View(View):
    def get(self, request):
        form = AppointmentEntryForm()
        context = {
            'form': form,
        }
        return render(request, 'polls/book2.html', context)

    def post(self, request):
        form = AppointmentEntryForm(request.POST)
        if form.is_valid():
            appointment_service = form.cleaned_data['appointment_service']
            request.session['appointment_service'] = str(appointment_service.id)
        return HttpResponseRedirect(reverse('polls:book'))


class BookView(View):
    def get(self, request):
        form = AppointmentForm()
        form.fields['appointment_employee'] = forms.ModelChoiceField(
            Employee.objects.filter(employee_service=request.session['appointment_service']))
        context = {
            'form': form,

        }
        return render(request, 'polls/book.html', context)

    def post(self, request):
        service = Service.objects.get(id=request.session['appointment_service'])
        form = AppointmentForm(request.POST)
        if form.is_valid():
            Appointment.objects.create(
                appointment_name=form.cleaned_data['appointment_name'],
                appointment_surname=form.cleaned_data['appointment_surname'],
                appointment_email=form.cleaned_data['appointment_email'],
                appointment_date=form.cleaned_data['appointment_date'],
                appointment_service=service,
            )
        messages.success(request, 'Great, your on {} visit is now reserved'.format(form.cleaned_data['appointment_date']))
        return HttpResponseRedirect(reverse('polls:index'))
