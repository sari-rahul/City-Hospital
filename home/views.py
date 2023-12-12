from django.shortcuts import render
from .models import Departments, Doctors

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def booking(request):
    return render(request, 'booking.html')


def doctors(request):
    dict_docs = {
        'docs': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)


def contact(request):
    return render(request, 'contact.html')


def department(request):
    dict_dept = {
        'dept': Departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)
