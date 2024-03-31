from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import student_data


def first(request):
    mymembers=student_data.objects.all().values()
    if request.method=='POST':
        first_name=request.POST.get('first_date')
        last_name=request.POST.get('last_date')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        
        student_data.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender
        )
    return HttpResponse ("Data added successfully")
    return render(request,'first.html',{'mymembers':mymembers})

